"""
Recherche sémantique dans les traités HEMA avec expansion conditionnelle.

Usage:
    python search.py
    python search.py --query "votre paragraphe" --sources marozzo_book3 anonimo_epee_deux_mains
    python search.py --sources marozzo_book3 --query "requête 1" --query "requête 2"
    python search.py --sources marozzo_book3 --exclude-section 164 166 --query "votre paragraphe"
    python search.py --sources marozzo_book3 --include-section 161 --exclude-section 164 166 --n-results 10 --query "votre paragraphe"
    python search.py list --sources marozzo_book3
    python search.py list --sources marozzo_book3 marozzo_book1
    python search.py show --sources marozzo_book3 --section "161"
    python search.py show --sources marozzo_book3 --section "161" --subsection "cinquième"
"""

import argparse
import json
import os
import re

import chromadb
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "hema_treatises"
EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2"

SCORE_THRESHOLD = 0.75
N_RESULTS = 5
MIN_EXCERPT_CHARS = 350
MAX_EXCERPT_CHARS = 1200


def resolve_ollama_base_url() -> str | None:
    """Resolve Ollama URL from env and normalize host:port values to http://host:port."""
    raw = os.getenv("OLLAMA_BASE_URL") or os.getenv("OLLAMA_HOST")
    if not raw:
        return None
    raw = raw.strip()
    if raw.startswith("http://") or raw.startswith("https://"):
        return raw
    return f"http://{raw}"

def _excerpt_window_for_query(query: str) -> int:
    """Size excerpt window from query length with sane limits."""
    query_len = len(query.strip())
    # Keep excerpt around query size, with small padding for context.
    return max(MIN_EXCERPT_CHARS, min(MAX_EXCERPT_CHARS, query_len + 120))


def best_excerpt(text: str, query: str, window: int | None = None) -> str:
    """Return the ~window-char substring of text with the most query word overlap."""
    if window is None:
        window = _excerpt_window_for_query(query)

    query_words = set(w.lower() for w in re.findall(r"\w+", query) if len(w) > 3)
    if not query_words or len(text) <= window:
        return text[:window]

    best_start = 0
    best_score = -1
    step = 50
    for start in range(0, max(1, len(text) - window), step):
        window_text = text[start : start + window].lower()
        score = sum(1 for w in query_words if w in window_text)
        if score > best_score:
            best_score = score
            best_start = start

    excerpt = text[best_start : best_start + window]
    if best_start > 0:
        excerpt = "…" + excerpt
    if best_start + window < len(text):
        excerpt = excerpt + "…"
    return excerpt


def _is_excluded_hit(meta: dict, exclude_sections: list[str]) -> bool:
    if not exclude_sections:
        return False
    section = meta.get("section", "").lower()
    subsection = meta.get("subsection", "").lower()
    for token in exclude_sections:
        t = token.lower().strip()
        if t and (t in section or t in subsection):
            return True
    return False


def _is_included_hit(meta: dict, include_sections: list[str]) -> bool:
    if not include_sections:
        return True
    section = meta.get("section", "").lower()
    subsection = meta.get("subsection", "").lower()
    for token in include_sections:
        t = token.lower().strip()
        if t and (t in section or t in subsection):
            return True
    return False


def search_sources(
    query: str,
    source_ids: list[str],
    collection,
    embeddings: OllamaEmbeddings,
    n_results: int = N_RESULTS,
    exclude_sections: list[str] | None = None,
    include_sections: list[str] | None = None,
) -> list[dict]:
    exclude_sections = exclude_sections or []
    include_sections = include_sections or []
    query_embedding = embeddings.embed_query(query)

    where_filter = {"source_id": {"$in": source_ids}} if len(source_ids) > 1 else {"source_id": source_ids[0]}

    fetch_multiplier = 4 if (exclude_sections or include_sections) else 1

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results * len(source_ids) * fetch_multiplier,
        where=where_filter,
        include=["documents", "metadatas", "distances"],
    )

    hits = []
    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        if not _is_included_hit(meta, include_sections):
            continue
        if _is_excluded_hit(meta, exclude_sections):
            continue

        score = 1 - dist
        hits.append(
            {
                "text": meta.get("original_text", doc),
                "source_id": meta.get("source_id", ""),
                "author": meta.get("author", ""),
                "book": meta.get("book", ""),
                "section": meta.get("section", ""),
                "subsection": meta.get("subsection", ""),
                "score": round(score, 4),
            }
        )

    hits.sort(key=lambda x: x["score"], reverse=True)
    return hits[: n_results * len(source_ids)]


def _highlight_excerpt(excerpt: str, query: str, min_len: int = 4) -> str:
    """Wrap query words found in excerpt with Rich bold yellow markup."""
    if not query:
        return excerpt
    query_words = sorted(
        set(w.lower() for w in re.findall(r"\w+", query) if len(w) >= min_len),
        key=len,
        reverse=True,  # replace longer words first to avoid partial matches
    )
    result = excerpt
    for word in query_words:
        result = re.sub(
            rf"(?i)({re.escape(word)})",
            r"[bold yellow]\1[/bold yellow]",
            result,
        )
    return result


def display_results(hits: list[dict], label: str, query: str = ""):
    if not hits:
        console.print(f"[yellow]Aucun résultat pour : {label}[/yellow]")
        return

    table = Table(title=f"📜 {label}", box=box.ROUNDED, show_lines=True, expand=True)
    table.add_column("Score", style="bold", width=7, justify="center")
    table.add_column("Source", style="cyan", width=20)
    table.add_column("Section", style="yellow", width=25)
    table.add_column("Extrait", style="white")

    for hit in hits:
        score_val = hit["score"]
        score_color = "green" if score_val >= SCORE_THRESHOLD else "yellow" if score_val >= 0.6 else "red"
        score_str = f"[{score_color}]{score_val:.3f}[/{score_color}]"

        source_str = f"{hit['author']}\n{hit['book']}"

        section_str = hit["section"]
        if hit["subsection"]:
            section_str += f"\n  › {hit['subsection']}"

        excerpt = best_excerpt(hit["text"], query)
        excerpt = _highlight_excerpt(excerpt, query) if query else excerpt

        table.add_row(score_str, source_str, section_str, excerpt)

    console.print(table)


def evaluate_results_with_llm(query: str, hits: list[dict], llm: ChatOllama) -> tuple[bool, str]:
    hits_summary = "\n\n".join(
        [
            f"Score: {h['score']:.3f} | {h['author']} - {h['book']} | Section: {h['section']}\n{h['text'][:400]}"
            for h in hits[:5]
        ]
    )

    messages = [
        SystemMessage(
            content="""Tu es un expert en arts martiaux historiques européens (HEMA).
Tu analyses des résultats de recherche sémantique dans des traités d'escrime anciens.
Réponds TOUJOURS en JSON avec ce format exact:
{"concluant": true/false, "score_moyen": 0.00, "explication": "...", "passages_pertinents": 1}"""
        ),
        HumanMessage(
            content=f"""Paragraphe recherché:
{query}

Résultats trouvés:
{hits_summary}

Ces résultats sont-ils concluants (similarité thématique et technique significative) ?
Considère que c'est concluant si au moins 2 résultats ont un score > {SCORE_THRESHOLD} ET traitent du même geste/technique."""
        ),
    ]

    response = llm.invoke(messages)
    content = response.content.strip()

    try:
        json_match = re.search(r"\{.*\}", content, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group())
            return data.get("concluant", False), data.get("explication", content)
    except Exception:
        pass

    avg_score = sum(h["score"] for h in hits) / len(hits) if hits else 0
    return avg_score >= SCORE_THRESHOLD, f"Score moyen: {avg_score:.3f}"


def list_sources(collection):
    results = collection.get(include=["metadatas"], limit=10000)
    sources = {}
    for meta in results["metadatas"]:
        sid = meta.get("source_id", "")
        if sid and sid not in sources:
            sources[sid] = {
                "author": meta.get("author", ""),
                "book": meta.get("book", ""),
                "title": meta.get("title", ""),
            }

    table = Table(title="📚 Sources disponibles", box=box.ROUNDED)
    table.add_column("source_id", style="cyan")
    table.add_column("Auteur", style="yellow")
    table.add_column("Livre", style="green")
    table.add_column("Titre")

    for sid, info in sorted(sources.items()):
        table.add_row(sid, info["author"], info["book"], info["title"])

    console.print(table)


def list_sections(source_ids: list[str], collection):
    results = collection.get(include=["metadatas"], limit=10000)
    # Collect (section, subsection) pairs per source
    seen: set[tuple[str, str, str]] = set()
    rows: list[tuple[str, str, str]] = []
    for meta in results["metadatas"]:
        sid = meta.get("source_id", "")
        if sid not in source_ids:
            continue
        section = meta.get("section", "")
        subsection = meta.get("subsection", "")
        key = (sid, section, subsection)
        if key not in seen:
            seen.add(key)
            rows.append(key)

    rows.sort()
    table = Table(title="📑 Sections", box=box.ROUNDED, show_lines=False)
    table.add_column("Source", style="cyan", no_wrap=True)
    table.add_column("Section", style="yellow")
    table.add_column("Sous-section", style="white")

    def _trunc(s: str, n: int = 50) -> str:
        return s if len(s) <= n else s[:n] + "…"

    for sid, section, subsection in rows:
        table.add_row(sid, _trunc(section), _trunc(subsection) if subsection else "[dim]—[/dim]")

    console.print(table)


def show_chunks(source_ids: list[str], collection, section_kw: str, subsection_kw: str = ""):
    """Affiche tous les chunks correspondant aux mots-clés de section/sous-section."""
    results = collection.get(include=["metadatas"], limit=10000)
    matches = []
    for meta in results["metadatas"]:
        if meta.get("source_id", "") not in source_ids:
            continue
        section = meta.get("section", "").lower()
        subsection = meta.get("subsection", "").lower()
        if section_kw.lower() not in section:
            continue
        if subsection_kw and subsection_kw.lower() not in subsection:
            continue
        matches.append(meta)

    if not matches:
        console.print("[yellow]Aucun chunk trouvé pour ces critères.[/yellow]")
        return

    for i, meta in enumerate(matches, start=1):
        section_str = meta.get("section", "")
        subsection_str = meta.get("subsection", "")
        header = f"[bold cyan]Chunk {i}[/bold cyan]  [yellow]{section_str}[/yellow]"
        if subsection_str:
            header += f"  [dim]›[/dim] [white]{subsection_str}[/white]"
        console.print(header)
        console.print(meta.get("original_text", ""))
        console.print("[dim]" + "─" * 80 + "[/dim]")


def process_prompt(prompt: str, collection, embeddings, llm):
    parse_messages = [
        SystemMessage(
            content="""Tu extrais des informations d'un prompt de recherche HEMA.
Réponds UNIQUEMENT en JSON valide:
{
  "sources_phase1": ["source_id_1", "source_id_2"],
  "sources_phase2": ["source_id_3"],
  "query": "le paragraphe ou passage à rechercher",
  "has_expansion": true/false
}
Les source_ids suivent le pattern: auteur_livre (ex: marozzo_book3, anonimo_epee_deux_mains, manciolino_opera_nova)"""
        ),
        HumanMessage(content=f"Prompt:\n{prompt}"),
    ]

    parse_response = llm.invoke(parse_messages)

    try:
        json_match = re.search(r"\{.*\}", parse_response.content, re.DOTALL)
        parsed = json.loads(json_match.group()) if json_match else {}
    except Exception:
        console.print("[red]Erreur de parsing du prompt. Essayez de reformuler.[/red]")
        return

    query = parsed.get("query", "")
    sources_p1 = parsed.get("sources_phase1", [])
    sources_p2 = parsed.get("sources_phase2", [])
    has_expansion = parsed.get("has_expansion", False)

    if not query or not sources_p1:
        console.print("[red]Impossible d'extraire la requête ou les sources.[/red]")
        return

    console.print(f"\n[bold]🔍 Recherche Phase 1[/bold] dans : [cyan]{', '.join(sources_p1)}[/cyan]")
    console.print(f"[dim]Paragraphe : {query[:150]}...[/dim]\n")

    hits_p1 = search_sources(query, sources_p1, collection, embeddings)
    display_results(hits_p1, f"Phase 1 — {', '.join(sources_p1)}", query)

    if has_expansion and sources_p2 and hits_p1:
        console.print("\n[dim]🤖 Évaluation des résultats par le LLM...[/dim]")
        is_conclusive, explanation = evaluate_results_with_llm(query, hits_p1, llm)

        console.print(
            Panel(
                f"[bold]Résultats Phase 1 {'✅ Concluants' if is_conclusive else '❌ Non concluants'}[/bold]\n{explanation}",
                border_style="green" if is_conclusive else "yellow",
            )
        )

        if is_conclusive:
            console.print(f"\n[bold]🔍 Recherche Phase 2[/bold] dans : [cyan]{', '.join(sources_p2)}[/cyan]")
            hits_p2 = search_sources(query, sources_p2, collection, embeddings)
            display_results(hits_p2, f"Phase 2 — {', '.join(sources_p2)}", query)

            all_hits = sorted(hits_p1 + hits_p2, key=lambda x: x["score"], reverse=True)
            display_results(all_hits[:5], "📊 Synthèse globale — Top 5", query)
        else:
            console.print("[yellow]Expansion annulée — résultats insuffisants en Phase 1.[/yellow]")


def interactive_search(collection, embeddings, llm):
    console.print(
        Panel(
            "[bold cyan]🗡  HEMA Semantic Search[/bold cyan]\n\n"
            "Format du prompt:\n"
            "[yellow]Recherche des paragraphes similaires dans [sources]. "
            "Si concluant, recherche dans [autres sources]\n"
            "<paragraphe à rechercher>[/yellow]\n\n"
            "Commandes: [green]exit[/green] pour quitter, [green]list[/green] pour les sources disponibles",
            expand=False,
        )
    )

    while True:
        console.print("\n[bold]> Votre prompt :[/bold]")
        lines = []
        try:
            while True:
                line = input()
                if line.lower() in ("exit", "quit"):
                    return
                if line.lower() == "list":
                    list_sources(collection)
                    break
                lines.append(line)
                if len(lines) >= 2 and lines[-1] == "" and lines[-2] == "":
                    break
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Au revoir ![/yellow]")
            return

        full_prompt = "\n".join(lines).strip()
        if not full_prompt or full_prompt.lower() == "list":
            continue

        process_prompt(full_prompt, collection, embeddings, llm)


def main():
    parser = argparse.ArgumentParser(description="HEMA Semantic Search")
    parser.add_argument("command", nargs="?", choices=["list", "show"], help="Sous-commandes : 'list' liste les sections, 'show' affiche les chunks d'une section")
    parser.add_argument(
        "--query",
        type=str,
        action="append",
        help="Paragraphe à rechercher. Répétez --query pour lancer plusieurs recherches séparées.",
    )
    parser.add_argument("--sources", nargs="+", help="source_ids à chercher")
    parser.add_argument(
        "--include-section",
        nargs="+",
        default=[],
        help="Mots-clés de section/sous-section à inclure (ex: 161 Première partie)",
    )
    parser.add_argument(
        "--exclude-section",
        nargs="+",
        default=[],
        help="Mots-clés de section/sous-section à exclure (ex: 164 166)",
    )
    parser.add_argument(
        "--n-results",
        type=int,
        default=N_RESULTS,
        help=f"Nombre de résultats à afficher (défaut: {N_RESULTS})",
    )
    parser.add_argument(
        "--section",
        type=str,
        default="",
        help="Mot-clé de section pour la commande show (ex: 161)",
    )
    parser.add_argument(
        "--subsection",
        type=str,
        default="",
        help="Mot-clé de sous-section pour la commande show (ex: cinquième)",
    )
    args = parser.parse_args()

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    ollama_base_url = resolve_ollama_base_url()

    # list/show ne nécessitent pas Ollama — on évite la connexion inutile
    if args.command in ("list", "show"):
        if not args.sources:
            console.print(f"[red]--sources requis avec la commande {args.command}.[/red]")
            return

        class _DummyEmbedFn(chromadb.EmbeddingFunction):
            def __call__(self, input: list[str]) -> list:
                return []

        collection = client.get_collection(name=COLLECTION_NAME, embedding_function=_DummyEmbedFn())
        if args.command == "list":
            list_sections(args.sources, collection)
        else:
            if not args.section:
                console.print("[red]--section requis avec la commande show.[/red]")
                return
            show_chunks(args.sources, collection, args.section, args.subsection)
        return

    if ollama_base_url:
        console.print(f"[dim]Ollama URL: {ollama_base_url}[/dim]")
    embeddings_kwargs = {"model": EMBED_MODEL}
    llm_kwargs = {"model": LLM_MODEL, "temperature": 0.1}
    if ollama_base_url:
        embeddings_kwargs["base_url"] = ollama_base_url
        llm_kwargs["base_url"] = ollama_base_url

    embeddings = OllamaEmbeddings(**embeddings_kwargs)

    class OllamaEmbeddingFunction(chromadb.EmbeddingFunction):
        def __call__(self, input: list[str]) -> list:
            return embeddings.embed_documents(input)

    collection = client.get_collection(name=COLLECTION_NAME, embedding_function=OllamaEmbeddingFunction())
    llm = ChatOllama(**llm_kwargs)

    if args.query and args.sources:
        queries = [query.strip() for query in args.query if query and query.strip()]
        if not queries:
            console.print("[red]Aucune requête valide fournie.[/red]")
            return

        for index, query in enumerate(queries, start=1):
            hits = search_sources(
                query,
                args.sources,
                collection,
                embeddings,
                n_results=max(1, args.n_results),
                exclude_sections=args.exclude_section,
                include_sections=args.include_section,
            )
            console.print(f"\n[bold cyan]Requête {index}[/bold cyan]\n[white]{query}[/white]")
            display_results(hits, " + ".join(args.sources), query)
    else:
        interactive_search(collection, embeddings, llm)


if __name__ == "__main__":
    main()

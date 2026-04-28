"""
Recherche sémantique dans les traités HEMA avec expansion conditionnelle.

Usage:
    python search.py
    python search.py --query "votre paragraphe" --sources marozzo_book3 anonimo_epee_deux_mains
"""

import argparse
import json
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


def search_sources(query: str, source_ids: list[str], collection, embeddings: OllamaEmbeddings, n_results: int = N_RESULTS) -> list[dict]:
    query_embedding = embeddings.embed_query(query)

    where_filter = {"source_id": {"$in": source_ids}} if len(source_ids) > 1 else {"source_id": source_ids[0]}

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results * len(source_ids),
        where=where_filter,
        include=["documents", "metadatas", "distances"],
    )

    hits = []
    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
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
    return hits


def display_results(hits: list[dict], label: str):
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

        excerpt = hit["text"]
        if len(excerpt) > 300:
            excerpt = excerpt[:297] + "..."

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
    display_results(hits_p1, f"Phase 1 — {', '.join(sources_p1)}")

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
            display_results(hits_p2, f"Phase 2 — {', '.join(sources_p2)}")

            all_hits = sorted(hits_p1 + hits_p2, key=lambda x: x["score"], reverse=True)
            display_results(all_hits[:5], "📊 Synthèse globale — Top 5")
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
    parser.add_argument("--query", type=str, help="Paragraphe à rechercher")
    parser.add_argument("--sources", nargs="+", help="source_ids à chercher")
    args = parser.parse_args()

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)

    class OllamaEmbeddingFunction(chromadb.EmbeddingFunction):
        def __call__(self, input: list[str]) -> list:
            return embeddings.embed_documents(input)

    collection = client.get_collection(name=COLLECTION_NAME, embedding_function=OllamaEmbeddingFunction())
    llm = ChatOllama(model=LLM_MODEL, temperature=0.1)

    if args.query and args.sources:
        hits = search_sources(args.query, args.sources, collection, embeddings)
        display_results(hits, " + ".join(args.sources))
    else:
        interactive_search(collection, embeddings, llm)


if __name__ == "__main__":
    main()

"""
Indexation des traités HEMA dans ChromaDB.
Usage: python ingest.py
"""

import argparse
import frontmatter
import chromadb
import os
from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from rich.console import Console
from rich.progress import track

console = Console()

TREATISES_DIR = Path("treatises")
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "hema_treatises"
EMBED_MODEL = "nomic-embed-text"


def resolve_ollama_base_url() -> str | None:
    """Resolve Ollama URL from env and normalize host:port values to http://host:port."""
    raw = os.getenv("OLLAMA_BASE_URL") or os.getenv("OLLAMA_HOST")
    if not raw:
        return None
    raw = raw.strip()
    if raw.startswith("http://") or raw.startswith("https://"):
        return raw
    return f"http://{raw}"

MIN_CHUNK_CHARS = 200
MAX_CHUNK_CHARS = 5000


def split_into_paragraphs(text: str, metadata: dict) -> list[dict]:
    """Découpe un texte markdown en paragraphes, en gardant le contexte de section."""
    chunks = []
    current_section = ""
    current_subsection = ""
    buffer = []

    for line in text.split("\n"):
        if line.startswith("## "):
            if buffer:
                chunks.append(_make_chunk(buffer, current_section, current_subsection, metadata))
                buffer = []
            current_section = line.lstrip("# ").strip()
            current_subsection = ""
        elif line.startswith("### "):
            if buffer:
                chunks.append(_make_chunk(buffer, current_section, current_subsection, metadata))
                buffer = []
            current_subsection = line.lstrip("# ").strip()
        elif line.strip():
            buffer.append(line.strip())
            content = " ".join(buffer)
            if len(content) >= MAX_CHUNK_CHARS:
                chunks.append(_make_chunk(buffer, current_section, current_subsection, metadata))
                buffer = []

    if buffer:
        content = " ".join(buffer)
        if len(content) >= MIN_CHUNK_CHARS:
            chunks.append(_make_chunk(buffer, current_section, current_subsection, metadata))

    return chunks


def _make_chunk(lines: list, section: str, subsection: str, metadata: dict) -> dict:
    content = " ".join(lines)
    context_header = ""
    if section:
        context_header = f"[{section}"
        if subsection:
            context_header += f" > {subsection}"
        context_header += "] "

    return {
        "text": content,
        "text_with_context": context_header + content,
        "section": section,
        "subsection": subsection,
        **metadata,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Indexer des traites HEMA Markdown dans une collection ChromaDB locale.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Fonctionnement global:\n"
            "  1) Lecture des fichiers .md (frontmatter YAML + contenu)\n"
            "  2) Decoupage en chunks par section/sous-section\n"
            "  3) Generation d'embeddings via Ollama\n"
            "  4) Insertion des chunks et metadonnees dans ChromaDB\n\n"
            "Bibliotheques utilisees:\n"
            "  - frontmatter: lecture frontmatter YAML\n"
            "  - chromadb: stockage vectoriel local\n"
            "  - langchain_ollama: embeddings via Ollama\n"
            "  - rich: affichage console/progression\n"
            "  - pathlib/os: gestion des chemins et environnement"
        ),
    )
    parser.add_argument("--treatises-dir", default=str(TREATISES_DIR), help="Dossier racine des traites markdown")
    parser.add_argument("--chroma-dir", default=CHROMA_DIR, help="Dossier de persistence ChromaDB")
    parser.add_argument("--collection-name", default=COLLECTION_NAME, help="Nom de la collection ChromaDB")
    parser.add_argument("--embed-model", default=EMBED_MODEL, help="Modele d'embedding Ollama")
    parser.add_argument("--min-chunk-chars", type=int, default=MIN_CHUNK_CHARS, help="Taille minimale d'un chunk")
    parser.add_argument("--max-chunk-chars", type=int, default=MAX_CHUNK_CHARS, help="Taille maximale cible d'un chunk")
    return parser.parse_args()


def ingest_file(filepath: Path, collection) -> int:
    post = frontmatter.load(filepath)
    meta = dict(post.metadata)

    for field in ["author", "source_id", "book"]:
        if field not in meta:
            console.print(f"[yellow]⚠ Champ manquant '{field}' dans {filepath}[/yellow]")
            meta.setdefault(field, filepath.stem)
            meta.setdefault("source_id", f"{filepath.parent.name}_{filepath.stem}")

    chunks = split_into_paragraphs(post.content, meta)

    if not chunks:
        console.print(f"[yellow]⚠ Aucun chunk extrait de {filepath}[/yellow]")
        return 0

    ids = [f"{meta['source_id']}__chunk_{i}" for i in range(len(chunks))]
    documents = [c["text_with_context"] for c in chunks]
    metadatas = [
        {
            "author": c.get("author", ""),
            "source_id": c.get("source_id", ""),
            "book": c.get("book", ""),
            "section": c.get("section", ""),
            "subsection": c.get("subsection", ""),
            "title": c.get("title", ""),
            "original_text": c["text"],
            "filepath": str(filepath),
        }
        for c in chunks
    ]

    batch_size = 50
    for i in range(0, len(chunks), batch_size):
        collection.add(
            ids=ids[i : i + batch_size],
            documents=documents[i : i + batch_size],
            metadatas=metadatas[i : i + batch_size],
        )

    return len(chunks)


def main():
    global TREATISES_DIR, CHROMA_DIR, COLLECTION_NAME, EMBED_MODEL, MIN_CHUNK_CHARS, MAX_CHUNK_CHARS

    args = parse_args()
    TREATISES_DIR = Path(args.treatises_dir)
    CHROMA_DIR = args.chroma_dir
    COLLECTION_NAME = args.collection_name
    EMBED_MODEL = args.embed_model
    MIN_CHUNK_CHARS = args.min_chunk_chars
    MAX_CHUNK_CHARS = args.max_chunk_chars

    console.print("[bold cyan]🗡  HEMA Treatise Indexer[/bold cyan]\n")

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    ollama_base_url = resolve_ollama_base_url()
    embeddings_kwargs = {"model": EMBED_MODEL}
    if ollama_base_url:
        embeddings_kwargs["base_url"] = ollama_base_url
        console.print(f"[dim]Ollama URL: {ollama_base_url}[/dim]")
    embeddings = OllamaEmbeddings(**embeddings_kwargs)

    class OllamaEmbeddingFunction(chromadb.EmbeddingFunction):
        def __call__(self, input: list[str]) -> list:
            return embeddings.embed_documents(input)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=OllamaEmbeddingFunction(),
        metadata={"hnsw:space": "cosine"},
    )

    md_files = list(TREATISES_DIR.rglob("*.md"))
    console.print(f"[green]Fichiers trouvés : {len(md_files)}[/green]\n")

    total_chunks = 0
    for filepath in track(md_files, description="Indexation..."):
        n = ingest_file(filepath, collection)
        total_chunks += n
        console.print(f"  ✓ {filepath} → {n} chunks")

    console.print(f"\n[bold green]✅ Indexation terminée : {total_chunks} chunks au total[/bold green]")
    console.print(f"   Collection : '{COLLECTION_NAME}' dans {CHROMA_DIR}")


if __name__ == "__main__":
    main()

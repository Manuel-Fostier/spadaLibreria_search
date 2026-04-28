"""
Indexation des traités HEMA dans ChromaDB.
Usage: python ingest.py
"""

import frontmatter
import chromadb
from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from rich.console import Console
from rich.progress import track

console = Console()

TREATISES_DIR = Path("treatises")
CHROMA_DIR = "./chroma_db"
COLLECTION_NAME = "hema_treatises"
EMBED_MODEL = "nomic-embed-text"

MIN_CHUNK_CHARS = 200
MAX_CHUNK_CHARS = 1500


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
    console.print("[bold cyan]🗡  HEMA Treatise Indexer[/bold cyan]\n")

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)

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

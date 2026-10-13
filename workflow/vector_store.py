"""
DRAM Foundation VN - Persistent Vector Store Interface
Wraps ChromaDB for local offline storage and semantic retrieval of semiconductor knowledge.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
import chromadb
from chromadb.config import Settings

DEFAULT_DB_DIR = Path(__file__).resolve().parent.parent / "data" / "chroma_db"
COLLECTION_NAME = "dram_semiconductor_knowledge"


class SemiconductorVectorStore:
    def __init__(self, persist_dir: Optional[Path] = None):
        self.persist_dir = Path(persist_dir) if persist_dir else DEFAULT_DB_DIR
        self.persist_dir.mkdir(parents=True, exist_ok=True)
        
        self.client = chromadb.PersistentClient(
            path=str(self.persist_dir),
            settings=Settings(anonymized_telemetry=False)
        )
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={"description": "DRAM 180nm, lithography, chemistry, and equipment literature"}
        )

    def add_document(self, doc_id: str, text: str, metadata: Dict[str, Any]):
        """Index a text document chunk with provenance metadata."""
        self.collection.upsert(
            ids=[doc_id],
            documents=[text],
            metadatas=[metadata]
        )

    def add_documents_batch(self, docs: List[Dict[str, Any]]):
        """Batch index documents."""
        if not docs:
            return
        ids = [d["id"] for d in docs]
        texts = [d["text"] for d in docs]
        metadatas = [d["metadata"] for d in docs]
        self.collection.upsert(ids=ids, documents=texts, metadatas=metadatas)

    def query(self, query_text: str, n_results: int = 3) -> List[Dict[str, Any]]:
        """Query semantic knowledge with citations."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        hits = []
        if results and results.get("documents"):
            docs = results["documents"][0]
            metas = results["metadatas"][0] if results.get("metadatas") else []
            dists = results["distances"][0] if results.get("distances") else []
            ids = results["ids"][0] if results.get("ids") else []

            for i in range(len(docs)):
                hits.append({
                    "id": ids[i] if i < len(ids) else f"hit-{i}",
                    "document": docs[i],
                    "metadata": metas[i] if i < len(metas) else {},
                    "distance": dists[i] if i < len(dists) else 0.0
                })
        return hits

    def count(self) -> int:
        return self.collection.count()

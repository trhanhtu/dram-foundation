"""
DRAM Foundation VN - Vector Store Test Suite
Verifies ChromaDB persistent client, semantic similarity retrieval,
literature metadata indexing, and citation formatting.
"""

from pathlib import Path
import pytest
from workflow.vector_store import SemiconductorVectorStore


@pytest.fixture
def store():
    return SemiconductorVectorStore()


def test_vector_store_initialization(store):
    """Verify that vector store initializes with ChromaDB collection."""
    assert store.collection is not None
    assert store.collection.name == "dram_semiconductor_knowledge"


def test_vector_store_corpus_count(store):
    """Verify that the baseline semiconductor corpus contains at least 20 chunks."""
    count = store.count()
    assert count >= 20, f"Expected >= 20 chunks in ChromaDB, found {count}"


def test_semantic_query_retrieval(store):
    """Verify semantic search retrieves relevant semiconductor literature."""
    # Test query for Deal-Grove oxidation
    hits = store.query("thermal oxidation Deal-Grove kinetics dry gate oxide", n_results=3)
    assert len(hits) > 0
    found_deal_grove = any("Deal-Grove" in h["metadata"].get("title", "") for h in hits)
    assert found_deal_grove, "Expected Deal-Grove document in top search hits"


def test_query_dram_cell_architecture(store):
    """Verify semantic query for DRAM cell capacitance and sense amplifier."""
    hits = store.query("1T1C storage cell capacitance femtofarad sense amplifier", n_results=3)
    assert len(hits) > 0
    top_meta = hits[0]["metadata"]
    assert "title" in top_meta
    assert "category" in top_meta
    assert "source" in top_meta


def test_single_document_upsert_and_query(store, tmp_path):
    """Verify upserting a new document chunk and retrieving it."""
    test_id = "test-doc-thermal-diffusion-001"
    test_text = "Boron dopant diffusion profile in silicon substrate modeled by Fick's second law."
    test_meta = {
        "title": "Thermal Diffusion of Boron in Silicon",
        "source": "Foundry Process Handbook",
        "category": "Thermal Processing",
        "chunk_index": 0
    }
    
    store.add_document(test_id, test_text, test_meta)
    
    hits = store.query("Boron dopant diffusion Fick's law", n_results=2)
    assert len(hits) > 0
    matched = [h for h in hits if h["id"] == test_id]
    assert len(matched) == 1
    assert matched[0]["metadata"]["title"] == test_meta["title"]


def test_batch_document_upsert(store):
    """Verify batch indexing of multiple chunks."""
    batch = [
        {
            "id": "batch-doc-1",
            "text": "Ellipsometry measures phase change delta and amplitude ratio psi.",
            "metadata": {"title": "Ellipsometry Basics", "source": "Optical Handbook", "category": "Metrology"}
        },
        {
            "id": "batch-doc-2",
            "text": "Four point probe measures sheet resistance with tungsten carbide tips.",
            "metadata": {"title": "Four Point Probe Method", "source": "ASTM Standard", "category": "Metrology"}
        }
    ]
    store.add_documents_batch(batch)
    
    res = store.query("tungsten carbide probe tips sheet resistance", n_results=2)
    assert any(h["id"] == "batch-doc-2" for h in res)

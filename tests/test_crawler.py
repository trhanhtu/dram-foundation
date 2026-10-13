"""
DRAM Foundation VN - Crawler Test Suite
Verifies text chunking, seed document structures, and ingestion pipelines.
"""

import pytest
from workflow.crawler import SemiconductorCrawler, SEED_SEMICONDUCTOR_DOCUMENTS


@pytest.fixture
def crawler():
    return SemiconductorCrawler()


def test_seed_documents_structure():
    """Verify that all seed semiconductor documents contain required provenance metadata."""
    assert len(SEED_SEMICONDUCTOR_DOCUMENTS) >= 15, "Expected at least 15 comprehensive seed documents"
    categories = set()
    for doc in SEED_SEMICONDUCTOR_DOCUMENTS:
        assert "id" in doc
        assert "title" in doc
        assert "source" in doc
        assert "category" in doc
        assert "content" in doc
        assert len(doc["content"].strip()) > 50
        categories.add(doc["category"])

    # Must cover multiple disciplines
    assert len(categories) >= 5, f"Expected coverage across >= 5 disciplines, got {categories}"


def test_chunk_text_logic(crawler):
    """Verify word chunking preserves paragraphs and filters trivial chunks."""
    long_text = " ".join([f"word_{i}" for i in range(350)])
    chunks = crawler._chunk_text(long_text, chunk_size=100)
    assert len(chunks) == 4
    assert len(chunks[0].split()) == 100
    assert len(chunks[-1].split()) == 50

    # Short trivial text < 30 chars filtered out
    short_text = "tiny bit"
    short_chunks = crawler._chunk_text(short_text, chunk_size=100)
    assert len(short_chunks) == 0

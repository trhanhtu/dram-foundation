"""
DRAM Foundation VN - FastAPI Bridge Server Test Suite
Verifies all REST API endpoints for graph traversal, module loading,
semantic search, and AI Council multi-agent review.
"""

import pytest
from fastapi.testclient import TestClient
from workflow.server import app


@pytest.fixture
def client():
    return TestClient(app)


def test_api_status(client):
    """Verify /api/status returns healthy system state."""
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["chroma_chunks"] >= 20
    assert data["total_nodes"] >= 12
    assert data["total_edges"] >= 10
    assert data["modules_count"] >= 6
    assert "Gemini" in data["exclusive_model"]


def test_api_graph(client):
    """Verify /api/graph returns full modular nodes and edges."""
    response = client.get("/api/graph")
    assert response.status_code == 200
    data = response.json()
    assert "nodes" in data
    assert "edges" in data
    assert len(data["nodes"]) >= 12
    assert len(data["edges"]) >= 10


def test_api_manifest(client):
    """Verify /api/manifest returns valid manifest with registered modules."""
    response = client.get("/api/manifest")
    assert response.status_code == 200
    data = response.json()
    assert "modules" in data
    assert len(data["modules"]) >= 6


def test_api_modules_list(client):
    """Verify /api/modules returns modules with nested data."""
    response = client.get("/api/modules")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 6
    first_mod = data[0]
    assert "info" in first_mod
    assert "data" in first_mod


def test_api_single_module_valid(client):
    """Verify /api/modules/{module_id} returns specific module."""
    response = client.get("/api/modules/module_wet_chemistry_gen1")
    assert response.status_code == 200
    data = response.json()
    assert data["module_id"] == "module_wet_chemistry_gen1"
    assert len(data["nodes"]) >= 3


def test_api_single_module_not_found(client):
    """Verify /api/modules/{module_id} returns 404 for non-existent module."""
    response = client.get("/api/modules/non_existent_module_xyz")
    assert response.status_code == 404


def test_api_search(client):
    """Verify /api/search performs semantic vector query against ChromaDB."""
    payload = {
        "query": "Buffered Oxide Etch hydrofluoric acid",
        "n_results": 2
    }
    response = client.post("/api/search", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == payload["query"]
    assert len(data["results"]) > 0
    assert "title" in data["results"][0]["metadata"]


def test_api_council_review_approval(client):
    """Verify /api/council/review approves a valid candidate node."""
    payload = {
        "node_id": "node-plasma-asher-strip",
        "title": "Downstream Oxygen Plasma Photoresist Ashing",
        "description": "Strip cross-linked positive photoresist using RF downstream oxygen plasma at 250W and 300 mTorr.",
        "generation": "Gen 1 (mm)",
        "category": "Chemical Processing",
        "prerequisite_node_ids": ["node-wet-bench-safety"]
    }
    response = client.post("/api/council/review", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["approved"] is True
    assert data["verdict"] == "COUNCIL_APPROVED"
    assert data["node"]["id"] == "node-plasma-asher-strip"
    assert 8 <= data["node"]["estimated_hours"] <= 80
    assert len(data["node"]["citations"]) > 0


def test_api_council_review_cycle_rejection(client):
    """Verify /api/council/review rejects duplicate or cyclic nodes."""
    # Attempt to add an already existing node ID
    payload = {
        "node_id": "node-gen1-mm",
        "title": "Duplicate Macroscopic Stage",
        "description": "Trying to duplicate node-gen1-mm",
        "generation": "Gen 1 (mm)",
        "category": "Precision Mechanics",
        "prerequisite_node_ids": []
    }
    response = client.post("/api/council/review", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["approved"] is False
    assert data["verdict"] == "REJECTED"
    assert "Systems Engineer" in data["stage"]


def test_api_crawl_seed(client):
    """Verify /api/crawl with seed=True triggers re-ingestion."""
    response = client.post("/api/crawl", json={"seed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["indexed_chunks"] >= 20

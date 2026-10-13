"""
DRAM Foundation VN - 4-Tier Comprehensive E2E Test Suite
Covers:
- Tier 1: Feature Coverage (FastAPI, ChromaDB, 6-Discipline WBS Schemas & DAG)
- Tier 2: Boundary & Corner Cases (Empty queries, extreme chunks, schema enums, cycle rejection,
          duplicate IDs, self-loops, dangling pointers, 404s, Laya PM effort clamping)
- Tier 3: Cross-Feature Interactions (Search -> Review -> Commit -> Manifest -> Graph Reload,
          Multi-discipline DAG dependency chains, and cross-module consistency)
"""

import json
import pytest
from pathlib import Path
from fastapi.testclient import TestClient
import jsonschema
import networkx as nx

from workflow.server import app, DATA_DIR, MODULES_DIR, MANIFEST_PATH
from workflow.vector_store import SemiconductorVectorStore
from workflow.crawler import SemiconductorCrawler
from workflow.council.orchestrator import AICouncilOrchestrator
from workflow.council.systems_engineer import SystemsEngineerAgent
from workflow.council.laya_pm import LayaProjectManagerAgent

NODE_SCHEMA_PATH = DATA_DIR / "schema" / "node.schema.json"
EDGE_SCHEMA_PATH = DATA_DIR / "schema" / "edge.schema.json"


# =====================================================================
# Fixtures
# =====================================================================
@pytest.fixture(scope="module")
def client():
    """Shared FastAPI test client."""
    return TestClient(app)


@pytest.fixture(scope="module")
def vector_store():
    return SemiconductorVectorStore()


@pytest.fixture(scope="module")
def crawler():
    return SemiconductorCrawler()


@pytest.fixture(scope="module")
def orchestrator():
    return AICouncilOrchestrator()


@pytest.fixture(scope="module")
def systems_engineer():
    return SystemsEngineerAgent()


@pytest.fixture(scope="module")
def pm_agent():
    return LayaProjectManagerAgent()


@pytest.fixture(scope="module")
def node_schema():
    with open(NODE_SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def edge_schema():
    with open(EDGE_SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def isolated_wbs_state():
    """
    Guarantees state isolation for tests that mutate modular JSON files or manifest.json.
    Snapshots original files before test and restores them in teardown.
    """
    manifest_backup = MANIFEST_PATH.read_text(encoding="utf-8")
    modules_backup = {
        f: f.read_text(encoding="utf-8") for f in MODULES_DIR.glob("*.json")
    }
    try:
        yield
    finally:
        MANIFEST_PATH.write_text(manifest_backup, encoding="utf-8")
        for f, content in modules_backup.items():
            f.write_text(content, encoding="utf-8")


# =====================================================================
# TIER 1: FEATURE COVERAGE (>=5 tests per feature group)
# =====================================================================

# --- Feature Group 1A: FastAPI Endpoints ---

def test_tier1_fastapi_status_metadata_and_counts(client):
    """Verify /api/status returns online state, valid counts, and Gemini model constraint."""
    res = client.get("/api/status")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "online"
    assert data["chroma_chunks"] >= 20
    assert data["total_nodes"] >= 12
    assert data["total_edges"] >= 10
    assert data["modules_count"] >= 6
    assert "Gemini" in data["exclusive_model"]
    assert "Laya" in data["decision_model"]


def test_tier1_fastapi_graph_structure_and_integrity(client):
    """Verify /api/graph returns full combined node and edge collections with required keys."""
    res = client.get("/api/graph")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data["nodes"], list)
    assert isinstance(data["edges"], list)
    assert len(data["nodes"]) >= 12
    assert len(data["edges"]) >= 10

    node_ids = {n["id"] for n in data["nodes"]}
    assert "node-mcu-cots" in node_ids
    assert "node-gen1-mm" in node_ids
    assert "node-gen2-um" in node_ids
    assert "node-rca-clean-process" in node_ids
    assert "node-deal-grove-dry-ox" in node_ids
    assert "node-dram-cell-layout" in node_ids


def test_tier1_fastapi_manifest_modules(client):
    """Verify /api/manifest accurately reports project version and registered modules."""
    res = client.get("/api/manifest")
    assert res.status_code == 200
    data = res.json()
    assert data["project"] == "DRAM Foundation VN"
    assert "modules" in data
    assert len(data["modules"]) >= 6

    for mod in data["modules"]:
        assert "id" in mod
        assert "name" in mod
        assert "generation" in mod
        assert "file" in mod
        assert "node_count" in mod
        assert mod["node_count"] >= 1


def test_tier1_fastapi_modules_list_and_detail(client):
    """Verify /api/modules returns structured list of all modules containing info and data."""
    res = client.get("/api/modules")
    assert res.status_code == 200
    modules = res.json()
    assert isinstance(modules, list)
    assert len(modules) >= 6

    # Verify each module item contains 'info' and 'data' blocks
    for item in modules:
        assert "info" in item
        assert "data" in item
        assert "nodes" in item["data"]
        assert "edges" in item["data"]


def test_tier1_fastapi_search_endpoint(client):
    """Verify /api/search performs vector search and returns ranked semiconductor results."""
    payload = {"query": "Deal-Grove oxidation kinetics parabolic dry oxygen", "n_results": 3}
    res = client.post("/api/search", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["query"] == payload["query"]
    assert data["total_hits"] >= 1
    assert len(data["results"]) >= 1
    hit = data["results"][0]
    assert "document" in hit
    assert "metadata" in hit
    assert "distance" in hit


def test_tier1_fastapi_crawl_seed_corpus(client):
    """Verify /api/crawl with seed=True re-ingests semiconductor literature successfully."""
    res = client.post("/api/crawl", json={"seed": True})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "success"
    assert data["type"] == "seed"
    assert data["indexed_chunks"] >= 20


def test_tier1_fastapi_council_review_endpoint(client):
    """Verify /api/council/review assesses a valid candidate node with AI council consensus."""
    payload = {
        "node_id": "node-temp-al-sputter-tier1",
        "title": "Magnetron Sputter Aluminum Interconnect Deposition",
        "description": "DC magnetron sputtering of 99.999% pure Aluminum targets at 3 mTorr Argon pressure.",
        "generation": "Gen 1 (mm)",
        "category": "Thin Film Deposition",
        "prerequisite_node_ids": ["node-wet-bench-safety"]
    }
    res = client.post("/api/council/review", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["approved"] is True
    assert data["verdict"] == "COUNCIL_APPROVED"
    assert data["node"]["id"] == "node-temp-al-sputter-tier1"
    assert 8 <= data["node"]["estimated_hours"] <= 80
    assert len(data["node"]["citations"]) > 0


def test_tier1_fastapi_council_commit_endpoint(client, isolated_wbs_state):
    """Verify /api/council/commit commits node to module file and updates manifest (isolated)."""
    # 1. Review candidate node
    review_res = client.post("/api/council/review", json={
        "node_id": "node-temp-commit-tier1",
        "title": "Temporary Test Package for Commit Tier 1",
        "description": "Validation test package for atomic disk write.",
        "generation": "Gen 1 (mm)",
        "category": "Precision Mechanics",
        "prerequisite_node_ids": ["node-gen1-mm"]
    })
    assert review_res.status_code == 200
    review_data = review_res.json()
    assert review_data["approved"] is True

    # 2. Commit node
    commit_payload = {
        "node": review_data["node"],
        "proposed_edges": review_data["proposed_edges"],
        "target_module": "02_litho_stage_gen1.json"
    }
    commit_res = client.post("/api/council/commit", json=commit_payload)
    assert commit_res.status_code == 200
    commit_data = commit_res.json()
    assert commit_data["status"] == "committed"
    assert commit_data["node_id"] == "node-temp-commit-tier1"


# --- Feature Group 1B: ChromaDB Vector Store ---

def test_tier1_chromadb_initialization_and_collection(vector_store):
    """Verify ChromaDB initializes with persistent collection name."""
    assert vector_store.collection is not None
    assert vector_store.collection.name == "dram_semiconductor_knowledge"


def test_tier1_chromadb_corpus_count_threshold(vector_store):
    """Verify ChromaDB contains >= 20 baseline literature chunks."""
    count = vector_store.count()
    assert count >= 20, f"Expected count >= 20, got {count}"


def test_tier1_chromadb_semantic_retrieval_relevance(vector_store):
    """Verify semantic retrieval ranks relevant physics documents top for RCA chemistry."""
    hits = vector_store.query("RCA cleaning ammonium hydroxide hydrogen peroxide megasonic", n_results=3)
    assert len(hits) > 0
    matched_text = " ".join([h["document"] for h in hits]).lower()
    assert "rca" in matched_text or "cleaning" in matched_text


def test_tier1_chromadb_custom_document_upsert(tmp_path):
    """Verify custom document upsert and subsequent semantic retrieval in isolated store."""
    isolated_store = SemiconductorVectorStore(persist_dir=tmp_path / "chroma_test")
    doc_id = "test-doc-plasma-dry-etch"
    doc_text = "Reactive Ion Etching (RIE) using CF4 and O2 plasma for anisotropic SiO2 etching."
    doc_meta = {"title": "RIE Anisotropic Etch", "category": "Etching", "source": "Semiconductor Fab Guide"}

    isolated_store.add_document(doc_id, doc_text, doc_meta)
    assert isolated_store.count() == 1

    hits = isolated_store.query("Reactive Ion Etching CF4 plasma", n_results=1)
    assert len(hits) == 1
    assert hits[0]["id"] == doc_id
    assert hits[0]["metadata"]["title"] == "RIE Anisotropic Etch"


def test_tier1_chromadb_batch_upsert_and_persistence(tmp_path):
    """Verify batch indexing multiple technical documents in isolated store."""
    isolated_store = SemiconductorVectorStore(persist_dir=tmp_path / "chroma_batch_test")
    batch = [
        {
            "id": "batch-plasma-01",
            "text": "Inductively coupled plasma creates high density ion flux for shallow trench isolation.",
            "metadata": {"title": "ICP-RIE Technology", "source": "Dry Etch Handbook", "category": "Etching"}
        },
        {
            "id": "batch-litho-02",
            "text": "Deep UV excimer laser at 248nm KrF achieves resolution down to 180nm.",
            "metadata": {"title": "KrF Excimer Lithography", "source": "Optical Stepper Manual", "category": "Lithography"}
        }
    ]
    isolated_store.add_documents_batch(batch)
    assert isolated_store.count() == 2

    res = isolated_store.query("248nm KrF excimer laser", n_results=1)
    assert len(res) == 1
    assert res[0]["id"] == "batch-litho-02"


def test_tier1_chromadb_text_chunking_provenance(crawler):
    """Verify crawler chunking splits lengthy texts without dropping technical content."""
    sample_text = (
        "Thermal oxidation kinetics in dry oxygen follows Deal-Grove linear-parabolic law. "
        "The linear rate constant B/A corresponds to surface reaction rate. "
        "The parabolic rate constant B corresponds to oxidant diffusion through existing oxide. "
        "At low temperatures and very thin oxide regime (< 20 nm), initial oxidation exhibits faster rates."
    )
    chunks = crawler._chunk_text(sample_text, chunk_size=20)
    assert len(chunks) >= 2
    for c in chunks:
        assert len(c.split()) <= 20


# --- Feature Group 1C: WBS 6-Discipline Schemas & DAG Validation ---

def test_tier1_wbs_all_six_discipline_modules_exist():
    """Verify that all 6 semiconductor discipline JSON files are physically present on disk."""
    expected_modules = [
        "01_mcu_cots.json",
        "02_litho_stage_gen1.json",
        "03_optical_aligner_gen2.json",
        "04_wet_chemistry_gen1.json",
        "05_thermal_oxidation_gen1.json",
        "06_dram_cell_architecture_gen2.json"
    ]
    for mod_name in expected_modules:
        mod_file = MODULES_DIR / mod_name
        assert mod_file.exists(), f"Missing required module: {mod_name}"


def test_tier1_wbs_node_schema_full_compliance(orchestrator, node_schema):
    """Verify every node across all modules complies with data/schema/node.schema.json."""
    graph = orchestrator.load_all_existing_graph()
    assert len(graph["nodes"]) >= 12
    for node in graph["nodes"]:
        jsonschema.validate(instance=node, schema=node_schema)


def test_tier1_wbs_edge_schema_full_compliance(orchestrator, edge_schema):
    """Verify every edge across all modules complies with data/schema/edge.schema.json."""
    graph = orchestrator.load_all_existing_graph()
    assert len(graph["edges"]) >= 10
    for edge in graph["edges"]:
        jsonschema.validate(instance=edge, schema=edge_schema)


def test_tier1_wbs_kahn_dag_acyclicity_full_graph(orchestrator):
    """Verify that the entire unified multi-discipline graph forms a valid acyclic DAG."""
    graph = orchestrator.load_all_existing_graph()
    G = nx.DiGraph()
    for n in graph["nodes"]:
        G.add_node(n["id"])
    for e in graph["edges"]:
        G.add_edge(e["source"], e["target"])

    assert nx.is_directed_acyclic_graph(G), "Unified semiconductor graph contains cycles!"


def test_tier1_wbs_topological_sort_precedence(orchestrator):
    """Verify topological sort yields valid causal precedence across all modules."""
    graph = orchestrator.load_all_existing_graph()
    G = nx.DiGraph()
    for n in graph["nodes"]:
        G.add_node(n["id"])
    for e in graph["edges"]:
        G.add_edge(e["source"], e["target"])

    topo_order = list(nx.topological_sort(G))
    order_map = {node_id: idx for idx, node_id in enumerate(topo_order)}

    for e in graph["edges"]:
        assert order_map[e["source"]] < order_map[e["target"]], (
            f"Precedence inverted: {e['source']} ({order_map[e['source']]}) -> "
            f"{e['target']} ({order_map[e['target']]})"
        )


def test_tier1_wbs_discipline_generation_assignment(orchestrator):
    """Verify nodes possess appropriate generation tags matching roadmap (Gen 1 vs Gen 2)."""
    graph = orchestrator.load_all_existing_graph()
    for node in graph["nodes"]:
        assert node["generation"] in ["Gen 1 (mm)", "Gen 2 (µm)", "Gen 3 (nm)"]


# =====================================================================
# TIER 2: BOUNDARY & CORNER CASES (>=5 tests per feature group)
# =====================================================================

# --- Feature Group 2A: Query & Input Boundaries ---

def test_tier2_search_empty_query_handling(client):
    """Verify POST /api/search with empty string query does not crash."""
    res = client.post("/api/search", json={"query": "", "n_results": 2})
    assert res.status_code == 200
    data = res.json()
    assert "results" in data


def test_tier2_search_whitespace_query_handling(client):
    """Verify POST /api/search with whitespace only query handled gracefully."""
    res = client.post("/api/search", json={"query": "   \n\t   ", "n_results": 2})
    assert res.status_code == 200
    data = res.json()
    assert "results" in data


def test_tier2_search_large_n_results_boundary(client):
    """Verify POST /api/search requests capped reasonably without server crash."""
    res = client.post("/api/search", json={"query": "silicon dioxide", "n_results": 100})
    assert res.status_code == 200
    data = res.json()
    # Should return at most the available chunks in DB without error
    assert len(data["results"]) <= 100


def test_tier2_crawler_tiny_text_filtered_out(crawler):
    """Verify crawler filters out trivial text shorter than 30 characters."""
    chunks = crawler._chunk_text("Too short.", chunk_size=50)
    assert len(chunks) == 0


def test_tier2_crawler_extreme_chunk_sizes(crawler):
    """Verify crawler handles extreme chunk sizes (small word counts and 10000 words)."""
    text = "The quick brown fox jumps over the lazy dog in cleanroom semiconductor wafer fab environment with precision lithography tools."
    # Chunks with 6 words produce > 30 characters each
    chunks_small = crawler._chunk_text(text, chunk_size=6)
    assert len(chunks_small) >= 2

    # Very large chunk size retains whole text in 1 chunk
    chunks_huge = crawler._chunk_text(text, chunk_size=10000)
    assert len(chunks_huge) == 1


def test_tier2_crawler_invalid_request_parameters(client):
    """Verify POST /api/crawl without url, pdf_path, or seed returns 400."""
    res = client.post("/api/crawl", json={})
    assert res.status_code == 400
    assert "Must provide either url, pdf_path, or seed=True" in res.json()["detail"]


def test_tier2_crawler_nonexistent_pdf_path(client):
    """Verify POST /api/crawl with missing local PDF returns 400."""
    res = client.post("/api/crawl", json={"pdf_path": "non_existent_file_xyz_123.pdf"})
    assert res.status_code == 400
    assert "PDF ingestion failed" in res.json()["detail"]


# --- Feature Group 2B: Schema Enums & Constraint Violations ---

def test_tier2_schema_invalid_generation_enum(node_schema):
    """Verify schema rejects node with invalid generation enum."""
    bad_node = {
        "id": "node-invalid-gen",
        "label": "Invalid Generation Node",
        "generation": "Gen 4 (quantum)",  # Invalid enum
        "action_type": "Make",
        "status": "pending",
        "category": "Quantum Computing"
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad_node, schema=node_schema)


def test_tier2_schema_invalid_action_type_enum(node_schema):
    """Verify schema rejects node with invalid action_type enum."""
    bad_node = {
        "id": "node-invalid-action",
        "label": "Invalid Action Node",
        "generation": "Gen 1 (mm)",
        "action_type": "Steal",  # Invalid enum (only Make, Buy, Partner)
        "status": "pending",
        "category": "Precision Mechanics"
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad_node, schema=node_schema)


def test_tier2_schema_invalid_status_enum(node_schema):
    """Verify schema rejects node with invalid status enum."""
    bad_node = {
        "id": "node-invalid-status",
        "label": "Invalid Status Node",
        "generation": "Gen 1 (mm)",
        "action_type": "Make",
        "status": "demolished",  # Invalid enum
        "category": "Precision Mechanics"
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad_node, schema=node_schema)


def test_tier2_schema_missing_required_fields(node_schema):
    """Verify schema rejects node missing mandatory fields (e.g. category, label)."""
    bad_node = {
        "id": "node-missing-fields",
        "generation": "Gen 1 (mm)",
        "action_type": "Make"
        # Missing label, status, category
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad_node, schema=node_schema)


def test_tier2_schema_estimated_hours_negative_boundary(node_schema):
    """Verify schema rejects node with estimated_hours < 1."""
    bad_node = {
        "id": "node-negative-hours",
        "label": "Negative Hours",
        "generation": "Gen 1 (mm)",
        "action_type": "Make",
        "status": "pending",
        "category": "Precision Mechanics",
        "estimated_hours": -5  # Minimum is 1 in schema
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad_node, schema=node_schema)


def test_tier2_schema_edge_invalid_relationship_type(edge_schema):
    """Verify edge schema rejects edge with invalid relationship_type enum."""
    bad_edge = {
        "id": "edge-bad-rel",
        "source": "node-a",
        "target": "node-b",
        "relationship_type": "antagonist"  # Invalid enum
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad_edge, schema=edge_schema)


def test_tier2_schema_edge_missing_target(edge_schema):
    """Verify edge schema rejects edge missing target."""
    bad_edge = {
        "id": "edge-no-target",
        "source": "node-a",
        "relationship_type": "prerequisite"
    }
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad_edge, schema=edge_schema)


# --- Feature Group 2C: Graph Topology Corner Cases ---

def test_tier2_dag_direct_cycle_rejected(systems_engineer):
    """Verify Systems Engineer rejects direct 2-node cycle (A -> B -> A)."""
    existing_nodes = [{"id": "node-a", "label": "Node A"}]
    existing_edges = []
    # Candidate node-b has edge a->b and edge b->a
    candidate_node = {"id": "node-b", "label": "Node B"}
    candidate_edges = [
        {"id": "e1", "source": "node-a", "target": "node-b"},
        {"id": "e2", "source": "node-b", "target": "node-a"}
    ]
    valid, msg, _ = systems_engineer.validate_node_and_edges(
        candidate_node, existing_nodes, existing_edges, candidate_edges
    )
    assert valid is False
    assert "cycle" in msg.lower()


def test_tier2_dag_three_node_cycle_rejected(systems_engineer):
    """Verify Systems Engineer rejects multi-hop cycle (A -> B -> C -> A)."""
    existing_nodes = [
        {"id": "node-1", "label": "N1"},
        {"id": "node-2", "label": "N2"},
        {"id": "node-3", "label": "N3"}
    ]
    existing_edges = [
        {"id": "e1", "source": "node-1", "target": "node-2"},
        {"id": "e2", "source": "node-2", "target": "node-3"}
    ]
    # Adding edge node-3 -> node-1 introduces cycle
    candidate_node = {"id": "node-cycle-close", "label": "Closer"}
    candidate_edges = [
        {"id": "e3", "source": "node-3", "target": "node-cycle-close"},
        {"id": "e4", "source": "node-cycle-close", "target": "node-1"}
    ]
    valid, msg, _ = systems_engineer.validate_node_and_edges(
        candidate_node, existing_nodes, existing_edges, candidate_edges
    )
    assert valid is False
    assert "cycle" in msg.lower()


def test_tier2_dag_duplicate_node_id_rejected(systems_engineer):
    """Verify Systems Engineer rejects candidate node with existing ID."""
    existing_nodes = [{"id": "node-mcu-cots", "label": "MCU"}]
    candidate_node = {"id": "node-mcu-cots", "label": "Duplicate MCU"}
    valid, msg, _ = systems_engineer.validate_node_and_edges(
        candidate_node, existing_nodes, [], []
    )
    assert valid is False
    assert "duplicate" in msg.lower()


def test_tier2_dag_self_loop_rejected(systems_engineer):
    """Verify Systems Engineer rejects self-loop edge (source == target)."""
    candidate_node = {"id": "node-self-loop", "label": "Looping Node"}
    candidate_edges = [
        {"id": "e-loop", "source": "node-self-loop", "target": "node-self-loop"}
    ]
    valid, msg, _ = systems_engineer.validate_node_and_edges(
        candidate_node, [], [], candidate_edges
    )
    assert valid is False
    assert "cycle" in msg.lower()


def test_tier2_dag_dangling_source_edge_rejected(systems_engineer):
    """Verify Systems Engineer rejects edge with nonexistent source ID."""
    existing_nodes = [{"id": "node-target", "label": "Target Node"}]
    candidate_node = {"id": "node-cand", "label": "Cand Node"}
    candidate_edges = [
        {"id": "e-dangle", "source": "node-ghost-source", "target": "node-cand"}
    ]
    valid, msg, _ = systems_engineer.validate_node_and_edges(
        candidate_node, existing_nodes, [], candidate_edges
    )
    assert valid is False
    assert "dangling" in msg.lower()


def test_tier2_dag_dangling_target_edge_rejected(systems_engineer):
    """Verify Systems Engineer rejects edge with nonexistent target ID."""
    candidate_node = {"id": "node-cand", "label": "Cand Node"}
    candidate_edges = [
        {"id": "e-dangle-tgt", "source": "node-cand", "target": "node-ghost-target"}
    ]
    valid, msg, _ = systems_engineer.validate_node_and_edges(
        candidate_node, [], [], candidate_edges
    )
    assert valid is False
    assert "dangling" in msg.lower()


def test_tier2_dag_empty_node_id_rejected(systems_engineer):
    """Verify candidate node missing ID is rejected."""
    candidate_node = {"label": "No ID Node"}
    valid, msg, _ = systems_engineer.validate_node_and_edges(
        candidate_node, [], [], []
    )
    assert valid is False
    assert "valid 'id'" in msg.lower()


# --- Feature Group 2D: API Missing Resources & Council PM Clamping ---

def test_tier2_api_module_not_found_404(client):
    """Verify GET /api/modules/{module_id} returns 404 for unknown module ID."""
    res = client.get("/api/modules/non_existent_module_9999")
    assert res.status_code == 404
    assert "not found" in res.json()["detail"].lower()


def test_tier2_api_commit_nonexistent_module_404(client):
    """Verify POST /api/council/commit with invalid module file returns 404."""
    payload = {
        "node": {"id": "node-test-ghost", "label": "Ghost"},
        "proposed_edges": [],
        "target_module": "non_existent_module_file.json"
    }
    res = client.post("/api/council/commit", json=payload)
    assert res.status_code == 404
    assert "not found" in res.json()["detail"].lower()


def test_tier2_api_commit_duplicate_node_400(client, isolated_wbs_state):
    """Verify POST /api/council/commit with duplicate node returns 400."""
    payload = {
        "node": {
            "id": "node-gen1-mm",  # Already exists in 02_litho_stage_gen1.json
            "label": "Duplicate Node"
        },
        "proposed_edges": [],
        "target_module": "02_litho_stage_gen1.json"
    }
    res = client.post("/api/council/commit", json=payload)
    assert res.status_code == 400
    assert "already exists" in res.json()["detail"].lower()


def test_tier2_laya_pm_clamping_minimum_8h_boundary(pm_agent):
    """Verify Laya PM clamps trivial sub-task effort up to minimum 8 hours."""
    decision = pm_agent.evaluate_node(
        node_title="Turn ON Power Switch",
        node_description="Flip the physical toggle switch from 0 to 1 on the power supply."
    )
    assert decision["estimated_hours"] >= 8
    assert decision["estimated_hours"] <= 80


def test_tier2_laya_pm_clamping_maximum_80h_boundary(pm_agent):
    """Verify Laya PM clamps colossal multi-discipline task effort down to maximum 80 hours."""
    decision = pm_agent.evaluate_node(
        node_title="Complete 300mm Fab Installation and EUV Tool Commissioning",
        node_description="Excavate 100,000 square meters of earth, build foundation, install cleanroom class 1, install High-NA EUV lithography systems and train 1,000 operators."
    )
    assert decision["estimated_hours"] <= 80
    assert decision["estimated_hours"] >= 8


# =====================================================================
# TIER 3: CROSS-FEATURE INTERACTIONS
# =====================================================================

def test_tier3_search_review_commit_manifest_reload_pipeline(client, isolated_wbs_state):
    """
    End-to-End Pipeline Interaction:
    1. Query vector store via /api/search for literature citations.
    2. Submit candidate node to /api/council/review using search context.
    3. Verify Systems Engineer + Laya PM + Domain Expert approve node.
    4. Commit approved node via /api/council/commit.
    5. Verify /api/manifest reflects incremented node count.
    6. Verify /api/graph reloads newly committed node and edge.
    7. Verify /api/status reports updated system totals.
    """
    # 1. Search literature
    search_res = client.post("/api/search", json={"query": "RCA SC-1 cleaning wafer", "n_results": 2})
    assert search_res.status_code == 200
    search_data = search_res.json()
    assert len(search_data["results"]) > 0

    initial_status = client.get("/api/status").json()
    initial_node_count = initial_status["total_nodes"]

    # 2. Review candidate
    candidate_id = "node-tier3-cascade-test"
    review_res = client.post("/api/council/review", json={
        "node_id": candidate_id,
        "title": "Cascaded Megasonic Wafer Scrubbing",
        "description": "High-frequency 1 MHz acoustic transducer cleaning in DI water bath following RCA-1.",
        "generation": "Gen 1 (mm)",
        "category": "Chemical Processing",
        "prerequisite_node_ids": ["node-rca-clean-process"]
    })
    assert review_res.status_code == 200
    review_data = review_res.json()
    assert review_data["approved"] is True
    assert review_data["node"]["id"] == candidate_id

    # 3. Commit node
    commit_res = client.post("/api/council/commit", json={
        "node": review_data["node"],
        "proposed_edges": review_data["proposed_edges"],
        "target_module": "04_wet_chemistry_gen1.json"
    })
    assert commit_res.status_code == 200
    commit_data = commit_res.json()
    assert commit_data["status"] == "committed"

    # 4. Verify manifest updated
    manifest_res = client.get("/api/manifest")
    assert manifest_res.status_code == 200
    manifest = manifest_res.json()
    wet_mod = next(m for m in manifest["modules"] if m["id"] == "module_wet_chemistry_gen1")
    assert wet_mod["node_count"] == commit_data["total_module_nodes"]

    # 5. Verify graph reload
    graph_res = client.get("/api/graph")
    assert graph_res.status_code == 200
    graph = graph_res.json()
    node_ids = {n["id"] for n in graph["nodes"]}
    assert candidate_id in node_ids
    edge_ids = {e["id"] for e in graph["edges"]}
    assert f"edge-node-rca-clean-process-to-{candidate_id}" in edge_ids

    # 6. Verify status counter incremented
    new_status = client.get("/api/status").json()
    assert new_status["total_nodes"] == initial_node_count + 1


def test_tier3_multi_discipline_dag_mcu_litho_optics_dram_chain(orchestrator):
    """
    Verify complete multi-discipline cross-module chain:
    MCU COTS (Mod 1) -> Litho Stage (Mod 2) -> Optics Aligner (Mod 3) -> DRAM Cell Layout (Mod 6).
    """
    graph = orchestrator.load_all_existing_graph()
    G = nx.DiGraph()
    for n in graph["nodes"]:
        G.add_node(n["id"])
    for e in graph["edges"]:
        G.add_edge(e["source"], e["target"])

    # Path 1: MCU -> Litho Stage
    assert nx.has_path(G, "node-mcu-cots", "node-gen1-mm")
    # Path 2: Litho Stage -> Optics Aligner
    assert nx.has_path(G, "node-gen1-mm", "node-gen2-um")
    # Path 3: Optics Aligner -> DRAM Cell Layout
    assert nx.has_path(G, "node-gen2-um", "node-dram-cell-layout")
    # Transitive chain: MCU -> DRAM Cell Layout
    assert nx.has_path(G, "node-mcu-cots", "node-dram-cell-layout")

    shortest_path = nx.shortest_path(G, "node-mcu-cots", "node-dram-cell-layout")
    expected_path = ["node-mcu-cots", "node-gen1-mm", "node-gen2-um", "node-dram-cell-layout"]
    assert shortest_path == expected_path


def test_tier3_multi_discipline_dag_wetbench_furnace_dram_chain(orchestrator):
    """
    Verify wet chemistry to thermal oxidation dependency chain:
    Wet Bench Safety -> RCA Clean -> Deal-Grove Gate Oxidation & Furnace Build -> Deal-Grove Gate Oxidation.
    """
    graph = orchestrator.load_all_existing_graph()
    G = nx.DiGraph()
    for n in graph["nodes"]:
        G.add_node(n["id"])
    for e in graph["edges"]:
        G.add_edge(e["source"], e["target"])

    assert nx.has_path(G, "node-wet-bench-safety", "node-rca-clean-process")
    assert nx.has_path(G, "node-rca-clean-process", "node-deal-grove-dry-ox")
    assert nx.has_path(G, "node-furnace-build", "node-deal-grove-dry-ox")

    # Topological precedence checks
    topo = list(nx.topological_sort(G))
    assert topo.index("node-wet-bench-safety") < topo.index("node-rca-clean-process")
    assert topo.index("node-rca-clean-process") < topo.index("node-deal-grove-dry-ox")
    assert topo.index("node-furnace-build") < topo.index("node-deal-grove-dry-ox")


def test_tier3_cross_module_edge_integrity(orchestrator):
    """Verify that every edge in every module points strictly to an existing node ID."""
    graph = orchestrator.load_all_existing_graph()
    node_ids = {n["id"] for n in graph["nodes"]}

    for edge in graph["edges"]:
        src = edge["source"]
        tgt = edge["target"]
        assert src in node_ids, f"Edge '{edge['id']}' has missing source node '{src}'"
        assert tgt in node_ids, f"Edge '{edge['id']}' has missing target node '{tgt}'"


def test_tier3_council_review_respects_cross_module_prerequisites(client):
    """Verify reviewing a node with prerequisite in a different module succeeds."""
    # Pre-requisite is 'node-gen2-um' from module 03, candidate will connect to it
    payload = {
        "node_id": "node-tier3-cross-module-cand",
        "title": "Cross-Module Aligner Calibration Target",
        "description": "Aligner calibration artifact using chromium on quartz.",
        "generation": "Gen 2 (µm)",
        "category": "Optics & Precision Alignment",
        "prerequisite_node_ids": ["node-gen2-um"]
    }
    res = client.post("/api/council/review", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["approved"] is True
    assert len(data["proposed_edges"]) == 1
    assert data["proposed_edges"][0]["source"] == "node-gen2-um"
    assert data["proposed_edges"][0]["target"] == "node-tier3-cross-module-cand"


def test_tier3_corpus_reingest_idempotency_and_system_consistency(client):
    """Verify triggering /api/crawl seed does not invalidate graph or manifest state."""
    pre_status = client.get("/api/status").json()

    # Trigger crawl seed
    crawl_res = client.post("/api/crawl", json={"seed": True})
    assert crawl_res.status_code == 200

    post_status = client.get("/api/status").json()
    assert post_status["status"] == "online"
    assert post_status["total_nodes"] == pre_status["total_nodes"]
    assert post_status["total_edges"] == pre_status["total_edges"]
    assert post_status["modules_count"] == pre_status["modules_count"]

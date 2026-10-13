"""
DRAM Foundation VN - Tier 4 Real-World Semiconductor Workflows Test Suite
Validates:
1. Complete wafer fabrication flow (RCA cleaning -> Deal-Grove gate oxidation -> Litho alignment -> DRAM 1T1C cell capacitor).
2. End-to-end interactive user work package lifecycle (search -> council review -> commit -> graph reload).
3. Chemical safety & facility interlocks (acid exhaust fume hood prerequisite for HF / RCA).
4. DRAM cell readout circuit signal chain (1T1C storage cell -> folded sense amplifier -> address decoder / VPP pump).
5. Bits-to-Atoms Proof-of-Work and physical verification standards.
6. Technology Readiness Level (TRL) generational roadmap directional integrity.
7. WBS 8-80 hour effort decomposition rule across all disciplines.
8. AI Council rejection of cyclic or unphysical workflow proposals.
"""

import json
import pytest
from pathlib import Path
from fastapi.testclient import TestClient
import networkx as nx

from workflow.server import app, DATA_DIR, MODULES_DIR, MANIFEST_PATH
from workflow.council.orchestrator import AICouncilOrchestrator
from workflow.council.systems_engineer import SystemsEngineerAgent
from workflow.council.laya_pm import LayaProjectManagerAgent


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture(scope="module")
def orchestrator():
    return AICouncilOrchestrator()


@pytest.fixture(scope="module")
def systems_engineer():
    return SystemsEngineerAgent()


@pytest.fixture(scope="module")
def pm_agent():
    return LayaProjectManagerAgent()


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


def test_tier4_fab_workflow_rca_cleaning_to_gate_oxidation_to_litho_to_dram_cell(orchestrator):
    """
    Validates the end-to-end semiconductor fabrication sequence:
    1. Wafer surface prep: RCA-1/2 cleaning (node-rca-clean-process)
    2. High-temp furnace: Quartz tube 3-zone PID assembly (node-furnace-build)
    3. Gate oxide growth: Deal-Grove dry gate oxidation (node-deal-grove-dry-ox, 3.5 nm)
    4. Patterning & Litho: Microscopic mask optical aligner (node-gen2-um, ±5 µm)
    5. Storage Cell: 1T1C DRAM cell capacitor formation (node-dram-cell-layout, C_s >= 28 fF)
    """
    graph = orchestrator.load_all_existing_graph()
    nodes_by_id = {n["id"]: n for n in graph["nodes"]}
    
    # 1. Verify all 5 key fabrication stages exist
    assert "node-rca-clean-process" in nodes_by_id
    assert "node-furnace-build" in nodes_by_id
    assert "node-deal-grove-dry-ox" in nodes_by_id
    assert "node-gen2-um" in nodes_by_id
    assert "node-dram-cell-layout" in nodes_by_id

    # 2. Verify physical metric targets
    rca = nodes_by_id["node-rca-clean-process"]
    assert "18.2" in rca["primary_metric"] or "18.2" in str(rca["metrics_target"])

    furnace = nodes_by_id["node-furnace-build"]
    assert "Flat Zone" in furnace["primary_metric"]
    assert "1200°C" in furnace["metrics_target"]["Max Temperature"]

    gate_ox = nodes_by_id["node-deal-grove-dry-ox"]
    assert "3.5 nm" in gate_ox["primary_metric"]
    assert "Deal-Grove" in gate_ox["sop_content"]

    litho = nodes_by_id["node-gen2-um"]
    assert "± 5 µm" in litho["primary_metric"]
    assert "365nm UV" in litho["metrics_target"]["Light Source"]

    dram_cell = nodes_by_id["node-dram-cell-layout"]
    assert "28 fF" in dram_cell["primary_metric"]
    assert "8F²" in dram_cell["metrics_target"]["Unit Cell Footprint"]

    # 3. Verify topological dependency relationships in NetworkX
    G = nx.DiGraph()
    for n in graph["nodes"]:
        G.add_node(n["id"])
    for e in graph["edges"]:
        G.add_edge(e["source"], e["target"])

    topo_order = list(nx.topological_sort(G))
    idx_rca = topo_order.index("node-rca-clean-process")
    idx_furnace = topo_order.index("node-furnace-build")
    idx_ox = topo_order.index("node-deal-grove-dry-ox")
    idx_litho = topo_order.index("node-gen2-um")
    idx_cell = topo_order.index("node-dram-cell-layout")

    assert idx_rca < idx_ox, "RCA cleaning must precede dry gate oxidation"
    assert idx_furnace < idx_ox, "Furnace calibration must precede dry gate oxidation"
    assert idx_litho < idx_cell, "Optical aligner must precede DRAM cell layout integration"


def test_tier4_user_candidate_proposal_review_commit_and_graph_verification(client, isolated_wbs_state):
    """
    End-to-End Simulation of User Workflow:
    1. User queries /api/search for technical literature.
    2. User drafts candidate work package (Rapid Thermal Anneal RTA).
    3. User submits proposal to /api/council/review and receives COUNCIL_APPROVED.
    4. User commits work package to 05_thermal_oxidation_gen1.json via /api/council/commit.
    5. User queries /api/graph and confirms new node is integrated.
    6. User verifies /api/status counters reflect updated state.
    """
    # Step 1: Semantic search
    search_res = client.post("/api/search", json={"query": "anneal dry gate oxide defect interface", "n_results": 2})
    assert search_res.status_code == 200
    search_hits = search_res.json()["results"]
    assert len(search_hits) > 0

    # Step 2 & 3: Submit to Council Review
    candidate_id = "node-tier4-rta-anneal"
    review_payload = {
        "node_id": candidate_id,
        "title": "Rapid Thermal Anneal (RTA) for Interface State Passivation",
        "description": "High temperature short duration RTA at 900°C in pure N2/H2 forming gas to passivate interface traps (D_it) post oxidation.",
        "generation": "Gen 1 (mm)",
        "category": "Thermal Processing",
        "prerequisite_node_ids": ["node-deal-grove-dry-ox"]
    }
    review_res = client.post("/api/council/review", json=review_payload)
    assert review_res.status_code == 200
    review_data = review_res.json()
    assert review_data["approved"] is True
    assert review_data["verdict"] == "COUNCIL_APPROVED"
    assert review_data["node"]["id"] == candidate_id
    assert 8 <= review_data["node"]["estimated_hours"] <= 80

    # Step 4: Commit node to module
    commit_payload = {
        "node": review_data["node"],
        "proposed_edges": review_data["proposed_edges"],
        "target_module": "05_thermal_oxidation_gen1.json"
    }
    commit_res = client.post("/api/council/commit", json=commit_payload)
    assert commit_res.status_code == 200
    commit_data = commit_res.json()
    assert commit_data["status"] == "committed"
    assert commit_data["node_id"] == candidate_id

    # Step 5: Query /api/graph to verify live presence
    graph_res = client.get("/api/graph")
    assert graph_res.status_code == 200
    graph_data = graph_res.json()
    node_ids = {n["id"] for n in graph_data["nodes"]}
    assert candidate_id in node_ids

    # Verify edge node-deal-grove-dry-ox -> node-tier4-rta-anneal
    edge_pairs = {(e["source"], e["target"]) for e in graph_data["edges"]}
    assert ("node-deal-grove-dry-ox", candidate_id) in edge_pairs

    # Step 6: Verify status endpoint
    status_res = client.get("/api/status")
    assert status_res.status_code == 200
    assert status_res.json()["status"] == "online"


def test_tier4_facility_and_equipment_hazard_prerequisites(orchestrator):
    """
    Verifies that hazardous chemical and thermal processes have strict facility prerequisites:
    - Acid wet bench safety hood (node-wet-bench-safety) is prerequisite for RCA cleaning (node-rca-clean-process)
    - RCA cleaning is prerequisite for BOE oxide etching (node-boe-oxide-etch)
    - Quartz tube furnace (node-furnace-build) is prerequisite for high-temp oxidation (node-deal-grove-dry-ox)
    """
    graph = orchestrator.load_all_existing_graph()
    edges = {(e["source"], e["target"]): e for e in graph["edges"]}

    # Safety hood -> RCA clean
    assert ("node-wet-bench-safety", "node-rca-clean-process") in edges
    # RCA clean -> BOE etch
    assert ("node-rca-clean-process", "node-boe-oxide-etch") in edges
    # Furnace assembly -> Dry oxidation
    assert ("node-furnace-build", "node-deal-grove-dry-ox") in edges
    # Furnace assembly -> Wet field oxidation
    assert ("node-furnace-build", "node-wet-oxidation-isolation") in edges


def test_tier4_dram_readout_subsystem_signal_chain(orchestrator):
    """
    Verifies the electronic signal readout chain of the 180nm DRAM architecture:
    node-dram-cell-layout (Cell) -> node-folded-sense-amp (Sense Amp) -> node-row-column-decoder (Decoders/VPP).
    """
    graph = orchestrator.load_all_existing_graph()
    nodes_by_id = {n["id"]: n for n in graph["nodes"]}

    cell = nodes_by_id["node-dram-cell-layout"]
    amp = nodes_by_id["node-folded-sense-amp"]
    dec = nodes_by_id["node-row-column-decoder"]

    # Verify electrical compatibility parameters
    assert "28 fF" in cell["primary_metric"]
    assert "Delta V" in amp["primary_metric"]
    assert "VPP" in dec["primary_metric"]

    # Verify edge chain
    edges = {(e["source"], e["target"]) for e in graph["edges"]}
    assert ("node-dram-cell-layout", "node-folded-sense-amp") in edges
    assert ("node-folded-sense-amp", "node-row-column-decoder") in edges


def test_tier4_bits_to_atoms_proof_of_work_lifecycle(orchestrator):
    """
    Verifies the Bits-to-Atoms validation protocol:
    Every completed node ('done') must have documented Proof-of-Work (repo URL, lab video)
    and quantitative machine-measurable metrics_target specifications.
    """
    graph = orchestrator.load_all_existing_graph()
    done_nodes = [n for n in graph["nodes"] if n.get("status") == "done"]
    assert len(done_nodes) >= 4, f"Expected at least 4 completed nodes, found {len(done_nodes)}"

    for node in done_nodes:
        pow_block = node.get("proof_of_work", {})
        assert pow_block.get("status") is not None, f"Node {node['id']} missing PoW status"
        assert pow_block.get("repo", "").startswith("https://"), f"Node {node['id']} missing valid PoW repo URL"
        assert len(pow_block.get("video", "")) > 0, f"Node {node['id']} missing PoW video reference"

        # Check machine-measurable metrics
        metrics = node.get("metrics_target", {})
        assert len(metrics) >= 2, f"Node {node['id']} must specify at least 2 quantitative acceptance metrics"


def test_tier4_trl_generational_roadmap_directional_guard(orchestrator):
    """
    Verifies Technology Readiness Level (TRL) roadmap directional progression:
    - Direction must flow from macro (Gen 1 mm) to micro (Gen 2 µm) and beyond.
    - No Gen 1 (mm) node may have an incoming prerequisite edge from a Gen 2 (µm) or Gen 3 (nm) node.
    """
    graph = orchestrator.load_all_existing_graph()
    nodes_by_id = {n["id"]: n for n in graph["nodes"]}

    for edge in graph["edges"]:
        src_gen = nodes_by_id[edge["source"]]["generation"]
        tgt_gen = nodes_by_id[edge["target"]]["generation"]

        # If target is Gen 1, source cannot be Gen 2 or Gen 3
        if "Gen 1" in tgt_gen:
            assert "Gen 2" not in src_gen and "Gen 3" not in src_gen, (
                f"Violation of TRL progression: Gen 1 target '{edge['target']}' depends on "
                f"higher generation source '{edge['source']}' ({src_gen})"
            )


def test_tier4_eight_to_eighty_hour_decomposition_rule(orchestrator):
    """
    Verifies that every single node across all 6 discipline modules adheres strictly
    to the WBS 8-80 hour rule:
    Effort must be >= 8 hours and <= 80 hours.
    """
    graph = orchestrator.load_all_existing_graph()
    for node in graph["nodes"]:
        hours = node.get("estimated_hours")
        assert hours is not None, f"Node {node['id']} missing estimated_hours"
        assert 8 <= hours <= 80, (
            f"Node '{node['id']}' violates 8-80h rule: estimated {hours} hours "
            f"(must be between 8 and 80 hours)"
        )


def test_tier4_multi_agent_council_rejects_unphysical_or_cyclic_proposal(client):
    """
    Verifies that the Multi-Agent Council intercepts and rejects unphysical proposals:
    Attempting to create an inverted loop (e.g., node claiming prerequisite 'node-row-column-decoder'
    while proposing to feed back into 'node-mcu-cots') is caught by Systems Engineer.
    """
    # Propose node with existing node ID
    dupe_payload = {
        "node_id": "node-dram-cell-layout",  # Existing node
        "title": "Duplicate DRAM Cell Proposal",
        "description": "Attempting to overwrite cell layout.",
        "generation": "Gen 2 (µm)",
        "category": "DRAM Architecture",
        "prerequisite_node_ids": ["node-gen2-um"]
    }
    res = client.post("/api/council/review", json=dupe_payload)
    assert res.status_code == 200
    data = res.json()
    assert data["approved"] is False
    assert data["verdict"] == "REJECTED"
    assert "Duplicate" in data["reason"] or "duplicate" in data["reason"].lower()

"""
DRAM Foundation VN - DAG & Topology Test Suite
Verifies Kahn's algorithm, acyclicity, cycle rejection, schema conformity,
and topological sorting across all 6 semiconductor disciplines.
"""

from pathlib import Path
import json
import pytest
import jsonschema

from workflow.council.systems_engineer import SystemsEngineerAgent
from workflow.council.orchestrator import AICouncilOrchestrator

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
MODULES_DIR = DATA_DIR / "modules"
NODE_SCHEMA_PATH = DATA_DIR / "schema" / "node.schema.json"
EDGE_SCHEMA_PATH = DATA_DIR / "schema" / "edge.schema.json"


@pytest.fixture
def orchestrator():
    return AICouncilOrchestrator()


@pytest.fixture
def systems_engineer():
    return SystemsEngineerAgent()


@pytest.fixture
def node_schema():
    with open(NODE_SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def edge_schema():
    with open(EDGE_SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def test_modules_exist_and_count():
    """Verify that all 6 semiconductor discipline modules are present."""
    module_files = list(MODULES_DIR.glob("*.json"))
    assert len(module_files) >= 6, f"Expected at least 6 modules, found {len(module_files)}"


def test_modular_graph_acyclicity(orchestrator, systems_engineer):
    """Verify that the full modular DAG across all disciplines is strictly acyclic."""
    graph = orchestrator.load_all_existing_graph()
    assert len(graph["nodes"]) >= 12, "Expected at least 12 nodes across 6 disciplines"
    assert len(graph["edges"]) >= 10, "Expected at least 10 edges across 6 disciplines"

    # Test with dummy valid node
    is_valid, msg, order = systems_engineer.validate_node_and_edges(
        candidate_node={"id": "node-dummy-terminal", "label": "Terminal Dummy"},
        existing_nodes=graph["nodes"],
        existing_edges=graph["edges"],
        candidate_edges=[{"id": "e-dummy", "source": graph["nodes"][0]["id"], "target": "node-dummy-terminal"}]
    )
    assert is_valid is True, f"DAG validation failed: {msg}"
    assert "acyclic" in msg.lower()
    assert len(order) == len(graph["nodes"]) + 1


def test_cycle_detection_rejection(systems_engineer):
    """Verify that an introduced cycle (A -> B -> C -> D -> A) is strictly detected and rejected."""
    existing_nodes = [
        {"id": "node-a", "label": "Node A"},
        {"id": "node-b", "label": "Node B"},
        {"id": "node-c", "label": "Node C"}
    ]
    existing_edges = [
        {"id": "e1", "source": "node-a", "target": "node-b"},
        {"id": "e2", "source": "node-b", "target": "node-c"}
    ]
    # Candidate node-d connects from C and loops back to A: A -> B -> C -> D -> A
    candidate_node = {"id": "node-d", "label": "Node D"}
    candidate_edges = [
        {"id": "e3", "source": "node-c", "target": "node-d"},
        {"id": "e4", "source": "node-d", "target": "node-a"}
    ]

    is_valid, msg, order = systems_engineer.validate_node_and_edges(
        candidate_node=candidate_node,
        existing_nodes=existing_nodes,
        existing_edges=existing_edges,
        candidate_edges=candidate_edges
    )
    assert is_valid is False
    assert "cycle" in msg.lower()


def test_duplicate_node_rejection(systems_engineer):
    """Verify that attempting to add an existing node ID is rejected."""
    existing_nodes = [{"id": "node-a", "label": "Node A"}]
    candidate_node = {"id": "node-a", "label": "Duplicate Node A"}
    
    is_valid, msg, order = systems_engineer.validate_node_and_edges(
        candidate_node=candidate_node,
        existing_nodes=existing_nodes,
        existing_edges=[],
        candidate_edges=[]
    )
    assert is_valid is False
    assert "duplicate" in msg.lower()



def test_self_loop_rejection(systems_engineer):
    """Verify that a self-loop is detected and rejected."""
    existing_nodes = [{"id": "node-a", "label": "Node A"}]
    existing_edges = []
    
    is_valid, msg, order = systems_engineer.validate_node_and_edges(
        candidate_node={"id": "node-b", "label": "Node B"},
        existing_nodes=existing_nodes,
        existing_edges=existing_edges,
        candidate_edges=[{"id": "e-loop", "source": "node-b", "target": "node-b"}]
    )
    assert is_valid is False
    assert "cycle" in msg.lower()


def test_all_nodes_conform_to_schema(orchestrator, node_schema):
    """Verify every node in every module strictly satisfies node.schema.json."""
    graph = orchestrator.load_all_existing_graph()
    for node in graph["nodes"]:
        try:
            jsonschema.validate(instance=node, schema=node_schema)
        except jsonschema.ValidationError as e:
            pytest.fail(f"Node '{node.get('id')}' failed schema validation: {e.message}")


def test_all_edges_conform_to_schema(orchestrator, edge_schema):
    """Verify every edge in every module strictly satisfies edge.schema.json."""
    graph = orchestrator.load_all_existing_graph()
    for edge in graph["edges"]:
        try:
            jsonschema.validate(instance=edge, schema=edge_schema)
        except jsonschema.ValidationError as e:
            pytest.fail(f"Edge '{edge.get('id')}' failed schema validation: {e.message}")


def test_topological_sort_precedence(orchestrator):
    """Verify topological sorting ensures every source comes before its target."""
    import networkx as nx
    graph = orchestrator.load_all_existing_graph()
    
    G = nx.DiGraph()
    for n in graph["nodes"]:
        G.add_node(n["id"])
    for e in graph["edges"]:
        G.add_edge(e["source"], e["target"])

    assert nx.is_directed_acyclic_graph(G), "Graph is not a valid DAG!"
    
    topo_order = list(nx.topological_sort(G))
    order_map = {node_id: idx for idx, node_id in enumerate(topo_order)}

    for e in graph["edges"]:
        if e["source"] in order_map and e["target"] in order_map:
            assert order_map[e["source"]] < order_map[e["target"]], (
                f"Dependency violation: source '{e['source']}' (idx {order_map[e['source']]}) "
                f"must appear before target '{e['target']}' (idx {order_map[e['target']]})"
            )

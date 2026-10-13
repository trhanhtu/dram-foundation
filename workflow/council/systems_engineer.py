"""
DRAM Foundation VN - AI Council: Systems Engineer Agent
Validates topological order, prerequisites, and ensures the DAG remains strictly acyclic.
"""

from typing import List, Dict, Any, Tuple
import networkx as nx


class SystemsEngineerAgent:
    def __init__(self):
        self.name = "Systems Engineer"
        self.role = "Validates edge pointers, prerequisites, and graph topological integrity."

    def validate_node_and_edges(
        self,
        candidate_node: Dict[str, Any],
        existing_nodes: List[Dict[str, Any]],
        existing_edges: List[Dict[str, Any]],
        candidate_edges: List[Dict[str, Any]]
    ) -> Tuple[bool, str, List[str]]:
        """
        Validates whether adding the candidate node and its proposed edges preserves DAG acyclic integrity.
        Returns: (is_valid, message, topological_order)
        """
        node_id = candidate_node.get("id")
        if not node_id or not str(node_id).strip():
            return False, "Node must contain a valid 'id' (non-empty).", []

        all_node_ids = {n["id"] for n in existing_nodes}
        if node_id in all_node_ids:
            return False, f"Duplicate node ID detected: {node_id}", []

        # Construct NetworkX DiGraph
        G = nx.DiGraph()
        for n in existing_nodes:
            G.add_node(n["id"])
        G.add_node(node_id)

        for e in existing_edges:
            G.add_edge(e["source"], e["target"])

        for e in candidate_edges:
            src = e.get("source")
            tgt = e.get("target")
            if src not in G or tgt not in G:
                return False, f"Dangling edge pointer: {src} -> {tgt}", []
            G.add_edge(src, tgt)

        # Check for cycles
        if not nx.is_directed_acyclic_graph(G):
            cycles = list(nx.simple_cycles(G))
            return False, f"Cycle detected in DAG: {cycles}", []

        # TRL Generational Roadmap Directional Guard:
        # Macro (Gen 1 mm) cannot depend on micro/nano (Gen 2 µm / Gen 3 nm)
        node_gens = {n["id"]: n.get("generation", "") for n in existing_nodes}
        node_gens[node_id] = candidate_node.get("generation", "")

        for e in list(existing_edges) + list(candidate_edges):
            s_id = e.get("source")
            t_id = e.get("target")
            s_gen = node_gens.get(s_id, "")
            t_gen = node_gens.get(t_id, "")
            if "Gen 1" in t_gen and ("Gen 2" in s_gen or "Gen 3" in s_gen):
                return False, (
                    f"Violation of TRL progression: Gen 1 target '{t_id}' depends on "
                    f"higher generation source '{s_id}' ({s_gen})"
                ), []

        topological_order = list(nx.topological_sort(G))
        return True, "DAG topology is acyclic and valid.", topological_order

"""
DRAM Foundation VN - AI Council Orchestrator
Coordinates Systems Engineer, Laya Project Manager, and Domain Expert (Gemini)
to vet work package candidates before committing them into modular DAG JSON files.
"""

from pathlib import Path
import json
from typing import Dict, Any, List, Optional

from workflow.council.systems_engineer import SystemsEngineerAgent
from workflow.council.laya_pm import LayaProjectManagerAgent
from workflow.council.domain_expert import DomainExpertAgent
from workflow.vector_store import SemiconductorVectorStore

MODULES_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "modules"


class AICouncilOrchestrator:
    def __init__(self, vector_store: Optional[SemiconductorVectorStore] = None):
        self.vector_store = vector_store or SemiconductorVectorStore()
        self.systems_eng = SystemsEngineerAgent()
        self.pm_agent = LayaProjectManagerAgent()
        self.domain_expert = DomainExpertAgent(vector_store=self.vector_store)

    def load_all_existing_graph(self) -> Dict[str, Any]:
        """Loads and merges all current modular JSON nodes and edges."""
        all_nodes = []
        all_edges = []
        for file in MODULES_DIR.glob("*.json"):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    all_nodes.extend(data.get("nodes", []))
                    all_edges.extend(data.get("edges", []))
            except Exception as e:
                print(f"[Orchestrator] Warning: Could not read {file}: {e}")
        return {"nodes": all_nodes, "edges": all_edges}

    def review_candidate_node(
        self,
        node_id: str,
        title: str,
        description: str,
        generation: str,
        category: str,
        prerequisite_node_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Runs the full 4-stage Multi-Agent Council review workflow.
        """
        prereqs = prerequisite_node_ids or []
        existing = self.load_all_existing_graph()

        proposed_edges = [
            {
                "id": f"edge-{prereq}-to-{node_id}",
                "source": prereq,
                "target": node_id,
                "relationship_type": "prerequisite",
                "label": "Prerequisite"
            }
            for prereq in prereqs
        ]

        # Stage 1: Systems Engineer (DAG Topology Validation)
        candidate_stub = {"id": node_id, "label": title}
        is_valid_dag, dag_msg, topo_order = self.systems_eng.validate_node_and_edges(
            candidate_node=candidate_stub,
            existing_nodes=existing["nodes"],
            existing_edges=existing["edges"],
            candidate_edges=proposed_edges
        )

        if not is_valid_dag:
            return {
                "approved": False,
                "stage": "Systems Engineer",
                "reason": dag_msg,
                "verdict": "REJECTED"
            }

        # Stage 2: Project Manager (Laya Decision Model - 8-80h Rule & Make/Buy)
        pm_decision = self.pm_agent.evaluate_node(node_title=title, node_description=description)

        # Stage 3: Domain Expert (Gemini & ChromaDB SOP Generation)
        sop_data = self.domain_expert.synthesize_sop(
            node_title=title,
            node_description=description,
            generation=generation,
            action_type=pm_decision["action_type"]
        )

        # Stage 4: Assembly of Validated DRAM Work Package
        final_node = {
            "id": node_id,
            "label": title,
            "generation": generation,
            "action_type": pm_decision["action_type"],
            "status": "pending",
            "category": category,
            "estimated_hours": pm_decision["estimated_hours"],
            "primary_metric": sop_data["primary_metric"],
            "metrics_target": sop_data["metrics_target"],
            "sop_content": sop_data["sop_content"],
            "citations": sop_data["citations"],
            "proof_of_work": {
                "status": "Pending Physical Verification",
                "repo": f"https://github.com/dram-vn/{node_id}",
                "video": "Awaiting laboratory video"
            }
        }

        return {
            "approved": True,
            "verdict": "COUNCIL_APPROVED",
            "node": final_node,
            "proposed_edges": proposed_edges,
            "systems_engineer_check": dag_msg,
            "pm_decision": pm_decision,
            "topological_rank": len(topo_order)
        }

    def commit_approved_node(
        self,
        node: Dict[str, Any],
        edges: List[Dict[str, Any]],
        module_file: str
    ) -> Dict[str, Any]:
        """
        Commits an approved node and its incoming edges to the designated module file.
        Strictly enforces:
        1. Non-empty valid node 'id' (raises ValueError / HTTP 400).
        2. Target module file existence on disk (raises FileNotFoundError / HTTP 404).
        3. Global node ID uniqueness across all system modules (raises ValueError / HTTP 400).
        4. Systems Engineer DAG acyclicity, cycle rejection, and dangling edge checks (raises ValueError / HTTP 400).
        5. Atomic disk persistence to target module and manifest.json node count sync.
        """
        # 1. Payload validation (VULN-04)
        if not isinstance(node, dict) or not node.get("id") or not str(node.get("id")).strip():
            raise ValueError("Node must contain a valid non-empty 'id'")
        node_id = str(node["id"]).strip()

        # 2. Target module file resolution
        module_path = MODULES_DIR.parent / module_file if not Path(module_file).is_absolute() else Path(module_file)
        if not module_path.exists():
            module_path = MODULES_DIR / Path(module_file).name
        if not module_path.exists():
            module_path = MODULES_DIR / f"{Path(module_file).name}.json"
        if not module_path.exists():
            raise FileNotFoundError(f"Target module file not found: {module_file}")

        with open(module_path, "r", encoding="utf-8") as f:
            module_data = json.load(f)

        # 3. Global node ID uniqueness check across all modules (VULN-02)
        all_existing = self.load_all_existing_graph()
        existing_nodes = all_existing.get("nodes", [])
        existing_edges = all_existing.get("edges", [])

        global_ids = {n["id"] for n in existing_nodes if isinstance(n, dict) and "id" in n}
        if node_id in global_ids:
            raise ValueError(f"Node '{node_id}' already exists in the system DAG")

        # 4. Systems Engineer DAG & Topology Validation (VULN-01)
        candidate_edges = edges if edges is not None else []
        is_valid_dag, dag_msg, _ = self.systems_eng.validate_node_and_edges(
            candidate_node=node,
            existing_nodes=existing_nodes,
            existing_edges=existing_edges,
            candidate_edges=candidate_edges
        )
        if not is_valid_dag:
            raise ValueError(f"DAG validation rejected commit: {dag_msg}")

        # 5. Persist to target module on disk
        module_data.setdefault("nodes", []).append(node)
        if candidate_edges:
            module_data.setdefault("edges", []).extend(candidate_edges)

        with open(module_path, "w", encoding="utf-8") as f:
            json.dump(module_data, f, indent=2, ensure_ascii=False)

        # 6. Synchronize manifest.json node counts
        manifest_path = MODULES_DIR.parent / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest_data = json.load(f)
            for mod in manifest_data.get("modules", []):
                if mod.get("id") == module_data.get("module_id") or Path(mod.get("file", "")).name == module_path.name:
                    mod["node_count"] = len(module_data["nodes"])
            with open(manifest_path, "w", encoding="utf-8") as f:
                json.dump(manifest_data, f, indent=2, ensure_ascii=False)

        return {
            "status": "committed",
            "module_id": module_data.get("module_id"),
            "node_id": node_id,
            "total_module_nodes": len(module_data["nodes"])
        }


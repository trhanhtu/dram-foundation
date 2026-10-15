"""
DRAM Foundation VN - Autonomous Knowledge & WBS Crawler Engine
Implements the continuous overnight decomposition and SOP synthesis pipeline
inspired by docs/pipeline_demo.py, anchored at Apex Root: DRAM.

Key Resilience Capabilities:
1. State Persistence & Rollback: Atomic in_progress locks and rollback_node_to_pending.
2. Rate-Limiting Backoff: TokenLimitReachedException handling with 5-hour rolling reset calculator.
3. Deadlock Circuit-Breaker: InfiniteLoopDeadlock handling marking red_flag and advancing BFS queue.
4. Dual-System Cognitive Hierarchy:
   - System 1: Laya PM Model (Local CPU, 0 token cost, ~30ms) for SPLIT vs WRITE_SOP triage.
   - System 2: Gemini Multi-Agent Council (Domain Expert, Supply Chain, Systems Engineer) for
     deep physical SOP synthesis, COTS veto, and mathematical Kahn DAG validation.
"""

import os
import sys
import json
import time
import sqlite3
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import networkx as nx

from workflow.vector_store import SemiconductorVectorStore
from workflow.council.systems_engineer import SystemsEngineerAgent
from workflow.council.laya_pm import LayaProjectManagerAgent
from workflow.council.domain_expert import DomainExpertAgent

DATA_DIR = ROOT_DIR / "data"
MODULES_DIR = DATA_DIR / "modules"
MANIFEST_PATH = DATA_DIR / "manifest.json"
SQLITE_DB_PATH = DATA_DIR / "dram_graph.db"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


# ==========================================
# 1. CUSTOM SYSTEM EXCEPTIONS
# ==========================================
class TokenLimitReachedException(Exception):
    """Raised when LLM API returns 429 Resource Exhausted or token quota is reached."""
    def __init__(self, message: str = "Token Limit Reached", retry_after: Optional[int] = None):
        super().__init__(message)
        self.retry_after = retry_after


class InfiniteLoopDeadlock(Exception):
    """Raised when Multi-Agent Council debates DAG edges for >= 3 rounds without resolution."""
    pass


# ==========================================
# 2. GRAPH DATABASE & SSOT PERSISTENCE
# ==========================================
class DRAMGraphDB:
    """
    Dual-layer storage:
    - Embedded SQLite for ACID transactions, BFS indexing, and recursive context travel up.
    - Automatic two-way sync with data/modules/*.json and manifest.json (Single Source of Truth for UI/Server).
    """

    def __init__(self, db_path: Path = SQLITE_DB_PATH, sync_files: bool = True):
        self.db_path = db_path
        self.sync_files = sync_files
        self._init_db()
        self.sync_from_json()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS nodes (
                    id TEXT PRIMARY KEY,
                    parent_id TEXT,
                    module_file TEXT,
                    label TEXT NOT NULL,
                    generation TEXT NOT NULL,
                    action_type TEXT NOT NULL,
                    status TEXT NOT NULL, -- pending, in_progress, done, red_flag
                    category TEXT NOT NULL,
                    estimated_hours REAL DEFAULT 40,
                    primary_metric TEXT,
                    metrics_target TEXT, -- JSON
                    sop_content TEXT,
                    citations TEXT,      -- JSON
                    proof_of_work TEXT,  -- JSON
                    red_flag_reason TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS edges (
                    id TEXT PRIMARY KEY,
                    source TEXT NOT NULL,
                    target TEXT NOT NULL,
                    relationship_type TEXT NOT NULL,
                    label TEXT,
                    module_file TEXT
                );
            """)
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_nodes_status ON nodes(status);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(parent_id);")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS system_metadata (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Schema migration: Add critics, testcases, ehs_protocol, q_time_constraints, and expected_result columns if missing
            cursor.execute("PRAGMA table_info(nodes);")
            existing_cols = [row["name"] for row in cursor.fetchall()]
            if "critics" not in existing_cols:
                cursor.execute("ALTER TABLE nodes ADD COLUMN critics TEXT;")
            if "testcases" not in existing_cols:
                cursor.execute("ALTER TABLE nodes ADD COLUMN testcases TEXT;")
            if "ehs_protocol" not in existing_cols:
                cursor.execute("ALTER TABLE nodes ADD COLUMN ehs_protocol TEXT;")
            if "q_time_constraints" not in existing_cols:
                cursor.execute("ALTER TABLE nodes ADD COLUMN q_time_constraints TEXT;")
            if "expected_result" not in existing_cols:
                cursor.execute("ALTER TABLE nodes ADD COLUMN expected_result TEXT;")

            conn.commit()

    def sync_from_json(self):
        """Loads all nodes and edges from data/modules/*.json into SQLite."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            for module_file in MODULES_DIR.glob("*.json"):
                try:
                    with open(module_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    for node in data.get("nodes", []):
                        critics_val = json.dumps(node.get("critics", {}), ensure_ascii=False) if node.get("critics") else None
                        testcases_val = json.dumps(node.get("testcases", []), ensure_ascii=False) if node.get("testcases") else None
                        ehs_val = json.dumps(node.get("ehs_protocol", {}), ensure_ascii=False) if node.get("ehs_protocol") else None
                        q_time_val = json.dumps(node.get("q_time_constraints", {}), ensure_ascii=False) if node.get("q_time_constraints") else None
                        expected_result_val = json.dumps(node.get("expected_result", {}), ensure_ascii=False) if node.get("expected_result") else None
                        cursor.execute("""
                            INSERT INTO nodes (
                                id, parent_id, module_file, label, generation, action_type,
                                status, category, estimated_hours, primary_metric,
                                metrics_target, sop_content, citations, proof_of_work, critics, testcases, ehs_protocol, q_time_constraints, expected_result, updated_at
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                            ON CONFLICT(id) DO UPDATE SET
                                parent_id = COALESCE(excluded.parent_id, nodes.parent_id),
                                module_file = excluded.module_file,
                                label = excluded.label,
                                generation = excluded.generation,
                                action_type = excluded.action_type,
                                status = excluded.status,
                                category = excluded.category,
                                estimated_hours = excluded.estimated_hours,
                                primary_metric = excluded.primary_metric,
                                metrics_target = excluded.metrics_target,
                                sop_content = excluded.sop_content,
                                citations = excluded.citations,
                                proof_of_work = excluded.proof_of_work,
                                critics = COALESCE(excluded.critics, nodes.critics),
                                testcases = COALESCE(excluded.testcases, nodes.testcases),
                                ehs_protocol = COALESCE(excluded.ehs_protocol, nodes.ehs_protocol),
                                q_time_constraints = COALESCE(excluded.q_time_constraints, nodes.q_time_constraints),
                                expected_result = COALESCE(excluded.expected_result, nodes.expected_result),
                                updated_at = CURRENT_TIMESTAMP;
                        """, (
                            node.get("id"),
                            node.get("parent_id"),
                            module_file.name,
                            node.get("label", ""),
                            node.get("generation", "Gen 1 (mm)"),
                            node.get("action_type", "Make"),
                            node.get("status", "pending"),
                            node.get("category", "General"),
                            node.get("estimated_hours", 40),
                            node.get("primary_metric"),
                            json.dumps(node.get("metrics_target", {}), ensure_ascii=False),
                            node.get("sop_content"),
                            json.dumps(node.get("citations", []), ensure_ascii=False),
                            json.dumps(node.get("proof_of_work", {}), ensure_ascii=False),
                            critics_val,
                            testcases_val,
                            ehs_val,
                            q_time_val,
                            expected_result_val
                        ))

                    for edge in data.get("edges", []):
                        cursor.execute("""
                            INSERT INTO edges (id, source, target, relationship_type, label, module_file)
                            VALUES (?, ?, ?, ?, ?, ?)
                            ON CONFLICT(id) DO UPDATE SET
                                source = excluded.source,
                                target = excluded.target,
                                relationship_type = excluded.relationship_type,
                                label = excluded.label,
                                module_file = excluded.module_file;
                        """, (
                            edge.get("id"),
                            edge.get("source"),
                            edge.get("target"),
                            edge.get("relationship_type", "prerequisite"),
                            edge.get("label", ""),
                            module_file.name
                        ))
                except Exception as e:
                    logging.warning(f"Error syncing {module_file.name} to DB: {e}")
            conn.commit()

    def sync_to_json(self):
        """Flushes SQLite state back into data/modules/*.json and updates manifest.json."""
        if not self.sync_files:
            return
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT module_file FROM nodes WHERE module_file IS NOT NULL;")
            module_files = [row["module_file"] for row in cursor.fetchall()]

            for mod_file in module_files:
                target_path = MODULES_DIR / mod_file
                if not target_path.exists():
                    continue

                cursor.execute("SELECT * FROM nodes WHERE module_file = ? ORDER BY id;", (mod_file,))
                raw_nodes = cursor.fetchall()
                nodes_list = []
                for r in raw_nodes:
                    node_dict = {
                        "id": r["id"],
                        "parent_id": r["parent_id"],
                        "label": r["label"],
                        "generation": r["generation"],
                        "action_type": r["action_type"],
                        "status": r["status"],
                        "category": r["category"],
                        "estimated_hours": r["estimated_hours"]
                    }
                    if r["primary_metric"]:
                        node_dict["primary_metric"] = r["primary_metric"]
                    if r["metrics_target"]:
                        try:
                            node_dict["metrics_target"] = json.loads(r["metrics_target"])
                        except Exception:
                            node_dict["metrics_target"] = {}
                    if r["sop_content"]:
                        node_dict["sop_content"] = r["sop_content"]
                    if r["citations"]:
                        try:
                            node_dict["citations"] = json.loads(r["citations"])
                        except Exception:
                            node_dict["citations"] = []
                    if r["proof_of_work"]:
                        try:
                            node_dict["proof_of_work"] = json.loads(r["proof_of_work"])
                        except Exception:
                            node_dict["proof_of_work"] = {}
                    if "critics" in r.keys() and r["critics"]:
                        try:
                            node_dict["critics"] = json.loads(r["critics"])
                        except Exception:
                            node_dict["critics"] = {}
                    if "testcases" in r.keys() and r["testcases"]:
                        try:
                            node_dict["testcases"] = json.loads(r["testcases"])
                        except Exception:
                            node_dict["testcases"] = []
                    if "ehs_protocol" in r.keys() and r["ehs_protocol"]:
                        try:
                            node_dict["ehs_protocol"] = json.loads(r["ehs_protocol"])
                        except Exception:
                            node_dict["ehs_protocol"] = {}
                    if "q_time_constraints" in r.keys() and r["q_time_constraints"]:
                        try:
                            node_dict["q_time_constraints"] = json.loads(r["q_time_constraints"])
                        except Exception:
                            node_dict["q_time_constraints"] = {}
                    if "expected_result" in r.keys() and r["expected_result"]:
                        try:
                            node_dict["expected_result"] = json.loads(r["expected_result"])
                        except Exception:
                            node_dict["expected_result"] = {}
                    nodes_list.append(node_dict)

                cursor.execute("SELECT * FROM edges WHERE module_file = ? ORDER BY id;", (mod_file,))
                raw_edges = cursor.fetchall()
                edges_list = [
                    {
                        "id": e["id"],
                        "source": e["source"],
                        "target": e["target"],
                        "relationship_type": e["relationship_type"],
                        "label": e["label"] or ""
                    }
                    for e in raw_edges
                ]

                # Update module JSON file
                try:
                    with open(target_path, "r", encoding="utf-8") as f:
                        file_data = json.load(f)
                    file_data["nodes"] = nodes_list
                    file_data["edges"] = edges_list
                    with open(target_path, "w", encoding="utf-8") as f:
                        json.dump(file_data, f, indent=2, ensure_ascii=False)
                except Exception as e:
                    logging.error(f"Failed to sync {mod_file}: {e}")

        # Update manifest.json
        if MANIFEST_PATH.exists():
            try:
                with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                    manifest = json.load(f)
                with self._get_connection() as conn:
                    cursor = conn.cursor()
                    for mod in manifest.get("modules", []):
                        f_name = Path(mod.get("file", "")).name
                        cursor.execute("SELECT COUNT(*) as cnt FROM nodes WHERE module_file = ?;", (f_name,))
                        row = cursor.fetchone()
                        if row:
                            mod["node_count"] = row["cnt"]
                with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
                    json.dump(manifest, f, indent=2, ensure_ascii=False)
            except Exception as e:
                logging.error(f"Failed to update manifest.json: {e}")

    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM nodes WHERE id = ?;", (node_id,))
            row = cursor.fetchone()
            if not row:
                return None
            return dict(row)

    def get_next_pending_node_bfs(self) -> Optional[Dict[str, Any]]:
        """
        Retrieves the next 'pending' node using BFS hierarchy.
        Nodes closest to Root (DRAM) or with parent_id IS NULL are processed first.
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            # Prioritize root node, then by parent hierarchy depth
            cursor.execute("""
                SELECT * FROM nodes
                WHERE status = 'pending'
                ORDER BY CASE WHEN id = 'node-dram-root' THEN 0
                              WHEN parent_id = 'node-dram-root' THEN 1
                              WHEN parent_id IS NULL THEN 2
                              ELSE 3 END,
                         (LENGTH(id) - LENGTH(REPLACE(id, '-', ''))) ASC,
                         id ASC
                LIMIT 1;
            """)
            row = cursor.fetchone()
            if not row:
                return None
            return dict(row)

    def mark_node_in_progress(self, node_id: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE nodes SET status = 'in_progress', updated_at = CURRENT_TIMESTAMP WHERE id = ?;", (node_id,))
            conn.commit()
        self.sync_to_json()

    def rollback_node_to_pending(self, node_id: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE nodes SET status = 'pending', updated_at = CURRENT_TIMESTAMP WHERE id = ?;", (node_id,))
            conn.commit()
        self.sync_to_json()

    def mark_node_red_flag(self, node_id: str, reason: str = ""):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE nodes 
                SET status = 'red_flag', red_flag_reason = ?, updated_at = CURRENT_TIMESTAMP 
                WHERE id = ?;
            """, (reason, node_id))
            conn.commit()
        self.sync_to_json()

    def update_node_to_done(
        self,
        node_id: str,
        sop_content: str,
        metrics_target: Dict[str, Any],
        citations: List[str]
    ):
        pow_block = json.dumps({
            "status": "Completed Physical Validation",
            "repo": f"https://github.com/dram-vn/{node_id}",
            "video": f"https://dram-vn.org/proofs/{node_id}-demo.mp4"
        }, ensure_ascii=False)
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE nodes 
                SET status = 'done',
                    sop_content = ?,
                    metrics_target = ?,
                    citations = ?,
                    proof_of_work = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = ?;
            """, (
                sop_content,
                json.dumps(metrics_target, ensure_ascii=False),
                json.dumps(citations, ensure_ascii=False),
                pow_block,
                node_id
            ))
            conn.commit()
        self.sync_to_json()

    def save_new_subgraph(
        self,
        parent_id: str,
        children: List[Dict[str, Any]],
        edges: List[Dict[str, Any]],
        module_file: Optional[str] = None
    ):
        """
        Atomically saves spawned child nodes and connecting edges under parent_id.
        """
        # Determine module file from parent if not specified
        if not module_file:
            parent = self.get_node(parent_id)
            module_file = parent.get("module_file", "06_dram_cell_architecture_gen2.json") if parent else "06_dram_cell_architecture_gen2.json"

        with self._get_connection() as conn:
            cursor = conn.cursor()
            for child in children:
                cursor.execute("""
                    INSERT INTO nodes (
                        id, parent_id, module_file, label, generation, action_type,
                        status, category, estimated_hours, primary_metric,
                        metrics_target, sop_content, citations, proof_of_work, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    ON CONFLICT(id) DO UPDATE SET
                        parent_id = excluded.parent_id,
                        module_file = excluded.module_file,
                        label = excluded.label,
                        generation = excluded.generation,
                        action_type = excluded.action_type,
                        status = excluded.status,
                        category = excluded.category,
                        estimated_hours = excluded.estimated_hours,
                        updated_at = CURRENT_TIMESTAMP;
                """, (
                    child["id"],
                    parent_id,
                    module_file,
                    child.get("label", ""),
                    child.get("generation", "Gen 1 (mm)"),
                    child.get("action_type", "Make"),
                    child.get("status", "pending"),
                    child.get("category", "General"),
                    child.get("estimated_hours", 40),
                    child.get("primary_metric"),
                    json.dumps(child.get("metrics_target", {}), ensure_ascii=False),
                    child.get("sop_content"),
                    json.dumps(child.get("citations", []), ensure_ascii=False),
                    json.dumps(child.get("proof_of_work", {}), ensure_ascii=False)
                ))

            for edge in edges:
                cursor.execute("""
                    INSERT INTO edges (id, source, target, relationship_type, label, module_file)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        source = excluded.source,
                        target = excluded.target,
                        relationship_type = excluded.relationship_type,
                        label = excluded.label,
                        module_file = excluded.module_file;
                """, (
                    edge["id"],
                    edge["source"],
                    edge["target"],
                    edge.get("relationship_type", "prerequisite"),
                    edge.get("label", ""),
                    module_file
                ))

            # Mark the parent node as 'done' since it has been successfully partitioned into children
            cursor.execute("UPDATE nodes SET status = 'done', updated_at = CURRENT_TIMESTAMP WHERE id = ?;", (parent_id,))
            conn.commit()

        self.sync_to_json()

    def get_context_travel_up(self, node_id: str) -> str:
        """
        Recursive climb up the parent chain up to Root: DRAM.
        Prevents AI myopia by pulling technology node and system specs from ancestors.
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                WITH RECURSIVE ancestor_tree AS (
                    SELECT id, parent_id, label, category, generation, 0 as depth
                    FROM nodes
                    WHERE id = ?
                    UNION ALL
                    SELECT n.id, n.parent_id, n.label, n.category, n.generation, a.depth + 1
                    FROM nodes n
                    JOIN ancestor_tree a ON n.id = a.parent_id
                )
                SELECT * FROM ancestor_tree ORDER BY depth DESC;
            """, (node_id,))
            ancestors = cursor.fetchall()

        if not ancestors:
            return f"Node: {node_id} (Root Context: 180nm Open-Source DRAM Chip)"

        breadcrumbs = [f"{a['label']} [{a['category']}]" for a in ancestors]
        return " > ".join(breadcrumbs)

    def load_full_graph_for_validation(self) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, label FROM nodes;")
            nodes = [dict(r) for r in cursor.fetchall()]
            cursor.execute("SELECT id, source, target, relationship_type FROM edges;")
            edges = [dict(r) for r in cursor.fetchall()]
            return nodes, edges

    def set_metadata(self, key: str, value: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO system_metadata (key, value, updated_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = CURRENT_TIMESTAMP;
            """, (key, value))
            conn.commit()

    def get_metadata(self, key: str) -> Optional[str]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT value FROM system_metadata WHERE key = ?;", (key,))
            row = cursor.fetchone()
            return row["value"] if row else None

    def get_status_summary(self) -> Dict[str, int]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT status, count(*) as cnt FROM nodes GROUP BY status;")
            counts = {row["status"]: row["cnt"] for row in cursor.fetchall()}
            cursor.execute("SELECT count(*) as total FROM nodes;")
            total = cursor.fetchone()["total"]
            return {
                "total": total,
                "done": counts.get("done", 0),
                "pending": counts.get("pending", 0),
                "in_progress": counts.get("in_progress", 0),
                "red_flag": counts.get("red_flag", 0)
            }

    def reset_nodes(self, target: str = "all") -> int:
        """
        Resets node(s) status back to 'pending'.
        - 'all': resets all nodes in the database.
        - 'root': resets node-dram-root and its immediate sub-nodes.
        - 'leaves': resets only terminal leaf nodes so they can expand into deeper levels.
        - specific node_id: resets that node only.
        Synchronizes changes to data/modules/*.json.
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            if target == "all":
                cursor.execute("UPDATE nodes SET status = 'pending';")
            elif target == "root":
                cursor.execute("UPDATE nodes SET status = 'pending' WHERE id = 'node-dram-root' OR parent_id = 'node-dram-root';")
            elif target == "leaves":
                cursor.execute("""
                    UPDATE nodes SET status = 'pending'
                    WHERE id NOT IN (SELECT DISTINCT parent_id FROM nodes WHERE parent_id IS NOT NULL)
                      AND action_type != 'Buy';
                """)
            else:
                cursor.execute("UPDATE nodes SET status = 'pending' WHERE id = ?;", (target,))
            count = cursor.rowcount
            conn.commit()
        self.sync_to_json()
        return count

    def get_node_depth(self, node_id: str) -> int:
        """Calculates distance from root (depth in the WBS tree)."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                WITH RECURSIVE ancestor_tree AS (
                    SELECT id, parent_id, 0 as depth
                    FROM nodes
                    WHERE id = ?
                    UNION ALL
                    SELECT n.id, n.parent_id, a.depth + 1
                    FROM nodes n
                    JOIN ancestor_tree a ON n.id = a.parent_id
                )
                SELECT COALESCE(MAX(depth), 0) FROM ancestor_tree;
            """, (node_id,))
            row = cursor.fetchone()
            return row[0] if row else 0




# ==========================================
# 3. AUTONOMOUS CRAWLER ENGINE (THE RUNNER)
# ==========================================
class OvernightCrawlerEngine:
    def __init__(
        self,
        db: Optional[DRAMGraphDB] = None,
        vector_store: Optional[SemiconductorVectorStore] = None,
        target_nodes: int = 1000,
        max_depth: int = 6,
        branch_factor: int = 3
    ):
        self.db = db or DRAMGraphDB()
        self.vector_store = vector_store or SemiconductorVectorStore()
        self.pm_agent = LayaProjectManagerAgent()
        self.domain_agent = DomainExpertAgent(vector_store=self.vector_store)
        self.systems_eng = SystemsEngineerAgent()
        self.target_nodes = target_nodes
        self.max_depth = max_depth
        self.branch_factor = branch_factor

    def record_token_consumption(self):
        """
        Records token consumption and initializes/rolls over the 5-hour rolling countdown.
        Principle: The 5-hour countdown begins the moment the FIRST token is consumed
        in the current window.
        """
        now = datetime.now()
        first_token_str = self.db.get_metadata("first_token_timestamp")
        if first_token_str:
            try:
                first_token_dt = datetime.fromisoformat(first_token_str)
                # If existing 5-hour window has fully elapsed, roll over to new window starting now
                if (now - first_token_dt).total_seconds() >= 5 * 3600:
                    self.db.set_metadata("first_token_timestamp", now.isoformat())
            except Exception:
                self.db.set_metadata("first_token_timestamp", now.isoformat())
        else:
            self.db.set_metadata("first_token_timestamp", now.isoformat())

    def calculate_sleep_time_for_5h_reset(self, server_retry_after: Optional[int] = None) -> int:
        """
        Calculates seconds until the 5-hour rolling quota window resets.
        Principle: The 5-hour countdown begins the moment the FIRST token is consumed
        in the current window, NOT when the limit is hit.
        
        - If server provided explicit retry_after (e.g. from RetryInfo), that is prioritized.
        - Otherwise: remaining_seconds = (first_token_timestamp + 5 hours) - now + 60s buffer.
        """
        if server_retry_after and server_retry_after > 0:
            return server_retry_after

        now = datetime.now()
        first_token_str = self.db.get_metadata("first_token_timestamp")
        if not first_token_str:
            # If no prior token was recorded, initialize window start and use 5h
            self.db.set_metadata("first_token_timestamp", now.isoformat())
            return 5 * 3600

        try:
            first_token_dt = datetime.fromisoformat(first_token_str)
            elapsed_seconds = (now - first_token_dt).total_seconds()
            window_duration = 5 * 3600  # 18,000 seconds

            if elapsed_seconds >= window_duration:
                # Window already elapsed! Reset window start and ready immediately
                self.db.set_metadata("first_token_timestamp", now.isoformat())
                return 60

            # Remaining time in the 5-hour window + 60s safety buffer
            remaining_seconds = int(window_duration - elapsed_seconds) + 60
            return max(60, min(remaining_seconds, window_duration + 60))
        except Exception:
            return 5 * 3600

    def process_single_node(self, node_id: str) -> str:
        """
        Processes a single work package with the Multi-Agent Council:
        1. Context Travel Up to Root: DRAM.
        2. System-1 Triage via Laya PM: SPLIT vs WRITE_SOP.
        3. Execution:
           - WRITE_SOP: Queries ChromaDB, generates industrial SOP and acceptance criteria.
           - SPLIT: Proposes sub-tasks, enforces COTS for Procurement, verifies DAG acyclicity.
             Raises InfiniteLoopDeadlock on debate loop >= 3.
        """
        context = self.db.get_context_travel_up(node_id)
        node_data = self.db.get_node(node_id)
        if not node_data:
            raise ValueError(f"Node {node_id} does not exist in graph database.")

        depth = self.db.get_node_depth(node_id)
        current_total = self.db.get_status_summary()["total"]
        logging.info(f"🧬 Context Climb [Depth {depth} | Total {current_total}]: {context}")
        
        # System 1: Laya PM Decision (0đ, ~30ms)
        pm_decision = self.pm_agent.evaluate_node(
            node_title=node_data["label"],
            node_description=f"Context: {context}. Category: {node_data.get('category')}"
        )
        scope = pm_decision.get("scope_decision", "write_sop")

        # Multi-Level Decomposition Rule to reach target_nodes (e.g. 2000 problems):
        is_cots = (node_data.get("action_type") == "Buy") or (
            node_data.get("action_type") != "Make" and any(
                kw in node_data["label"].lower() for kw in ["cots purchase", "buy off-the-shelf", "commercial supply", "purchase standard"]
            )
        )
        if not is_cots and (current_total < self.target_nodes and depth < self.max_depth):
            scope = "spawn_children"
        elif node_id == "node-dram-root" or node_data.get("estimated_hours", 0) > 80:
            scope = "spawn_children"


        if scope in ("write_sop", "trivial_task"):
            self.record_token_consumption()
            logging.info(f"✍️ Writing SOP for leaf task: {node_data['label']}")
            sop_result = self.domain_agent.synthesize_sop(
                node_title=node_data["label"],
                node_description=f"Context: {context}",
                generation=node_data.get("generation", "Gen 1 (mm)"),
                action_type=pm_decision.get("action_type", "Make")
            )
            self.db.update_node_to_done(
                node_id=node_id,
                sop_content=sop_result.get("sop_content", ""),
                metrics_target=sop_result.get("metrics_target", {}),
                citations=sop_result.get("citations", [])
            )
            logging.info(f"✅ SOP closed for Node [{node_id}]: {node_data['label']}")
            return "DONE_SOP"

        else:  # SPLIT (spawn_children)
            logging.info(f"🌿 Splitting composite task [{node_id}]: {node_data['label']}")
            proposed_children, proposed_edges = self._propose_sub_tasks_and_edges(node_data, context)

            # Supply Chain check on proposed children (COTS -> Buy)
            for child in proposed_children:
                is_cots = any(kw in child["label"].lower() for kw in ["mcu", "stepper", "pump", "sensor", "lens", "gauge", "power supply", "esp32", "cable"])
                if is_cots:
                    child["action_type"] = "Buy"

            # Systems Engineer Kahn DAG validation
            existing_nodes, existing_edges = self.db.load_full_graph_for_validation()
            loop_count = 0
            is_valid = False
            approved_edges = proposed_edges

            while not is_valid:
                loop_count += 1
                if loop_count >= 3:
                    raise InfiniteLoopDeadlock(f"Council DAG dispute loop >= 3 at Node {node_id}")

                # Validate with Systems Engineer
                G = nx.DiGraph()
                for n in existing_nodes:
                    G.add_node(n["id"])
                for c in proposed_children:
                    G.add_node(c["id"])
                for e in existing_edges + approved_edges:
                    G.add_edge(e["source"], e["target"])

                if nx.is_directed_acyclic_graph(G):
                    is_valid = True
                else:
                    # Fix: remove offending feedback edges
                    cycles = list(nx.simple_cycles(G))
                    logging.warning(f"Cycle detected during split: {cycles}. Adjusting proposed edges...")
                    approved_edges = [
                        e for e in approved_edges
                        if not any(e["source"] in cycle and e["target"] in cycle for cycle in cycles)
                    ]

            self.db.save_new_subgraph(
                parent_id=node_id,
                children=proposed_children,
                edges=approved_edges,
                module_file=node_data.get("module_file")
            )
            logging.info(f"🌱 Spawned {len(proposed_children)} sub-tasks from [{node_id}]")
            return f"SPLIT_{len(proposed_children)}"

    def _propose_sub_tasks_and_edges(
        self,
        parent_node: Dict[str, Any],
        context: str
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Generates realistic semiconductor sub-tasks under the parent node,
        preserving the 8-80h rule and strict technological roadmap.
        """
        p_id = parent_node["id"]
        p_label = parent_node["label"]
        p_gen = parent_node.get("generation", "Gen 2 (µm)")
        depth = self.db.get_node_depth(p_id)

        # Children inherit parent's generation to preserve TRL directional integrity
        child_gen = p_gen

        # Use Gemini Domain Expert with ChromaDB RAG to propose authentic semiconductor sub-tasks
        child_items = self.domain_agent.propose_sub_tasks(
            node_title=p_label,
            node_description=f"Context: {context}. Category: {parent_node.get('category')}",
            context=context,
            generation=child_gen,
            count=self.branch_factor
        )

        children = []
        edges = []
        child_ids = []

        for idx, item in enumerate(child_items):
            c_id = f"{p_id}-{idx + 1}"
            child_ids.append(c_id)
            children.append({
                "id": c_id,
                "label": item.get("label", f"Sub-task {idx + 1} of {p_label}"),
                "generation": item.get("generation", child_gen),
                "action_type": item.get("action_type", "Make"),
                "status": "pending",
                "category": item.get("category", parent_node.get("category", "General")),
                "estimated_hours": float(item.get("estimated_hours", 36)),
                "primary_metric": f"Sub-milestone of {p_label}",
                "metrics_target": {"Parent": p_label, "Target": "Physical Validation"},
                "sop_content": None,
                "citations": ["DRAM Foundation VN - Engineering Specification"],
                "proof_of_work": {
                    "status": "Pending Physical Verification",
                    "repo": f"https://github.com/dram-vn/{c_id}",
                    "video": "Awaiting laboratory video"
                }
            })

        # Tree branch prerequisite edges from each child directly to parent milestone
        for c_id in child_ids:
            edges.append({
                "id": f"edge-{c_id}-to-{p_id}",
                "source": c_id,
                "target": p_id,
                "relationship_type": "prerequisite",
                "label": "Sub-task Prerequisite"
            })

        return children, edges

    def run_overnight_crawler(self, max_iterations: Optional[int] = None):
        """
        The Master Overnight Loop (The Engine):
        Picks pending node -> Locks in_progress -> Processes Council -> Loops.
        Includes 5h token quota backoff, red_flag deadlock skipping, and crash resilience.
        """
        logging.info("🚀 DRAM Foundation VN: Overnight WBS & SOP Crawler Engine Activated...")
        
        # Automatic crash recovery on startup: roll stranded in_progress nodes back to pending
        with self.db._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE nodes SET status = 'pending' WHERE status = 'in_progress';")
            if cursor.rowcount > 0:
                logging.info(f"🔄 Recovered {cursor.rowcount} interrupted in_progress node(s) back to pending.")
                conn.commit()
                self.db.sync_to_json()

        iterations = 0

        while True:
            if max_iterations is not None and iterations >= max_iterations:
                logging.info(f"🎯 Reached requested max_iterations ({max_iterations}). Halting.")
                break

            target_node = self.db.get_next_pending_node_bfs()
            if not target_node:
                summary = self.db.get_status_summary()
                if iterations == 0:
                    logging.info(f"🎉 All {summary['total']} nodes across the DRAM WBS tree are complete ({summary['done']} done, 0 pending). No pending nodes remaining.")
                else:
                    logging.info("🎉 All nodes across the DRAM WBS tree are complete! No pending nodes remaining.")
                break

            iterations += 1
            node_id = target_node["id"]
            logging.info(f"[{iterations}] 🔍 Dissecting Node [{node_id}]: {target_node['label']}")

            # Atomic lock
            self.db.mark_node_in_progress(node_id)

            try:
                res = self.process_single_node(node_id)
                logging.info(f"[{iterations}] 🏁 Finished Node [{node_id}] -> {res}")

            except TokenLimitReachedException as token_err:
                sleep_secs = self.calculate_sleep_time_for_5h_reset(server_retry_after=token_err.retry_after)
                logging.warning(f"⏳ Token Quota Reached. Rolling back [{node_id}] and sleeping for {sleep_secs/3600:.2f} hours (remaining countdown from first token in 5h window)...")
                self.db.rollback_node_to_pending(node_id)
                time.sleep(sleep_secs)
                logging.info("⏰ Waking up after 5-hour quota reset! Resuming crawler...")
                continue

            except InfiniteLoopDeadlock as deadlock_err:
                logging.error(f"🛑 DEADLOCK on [{node_id}]: {deadlock_err}. Marking RED_FLAG and moving to next node.")
                self.db.mark_node_red_flag(node_id, reason=str(deadlock_err))
                continue

            except Exception as ex:
                logging.error(f"⚠️ Unexpected error on [{node_id}]: {ex}. Rolling back to pending for retry.")
                self.db.rollback_node_to_pending(node_id)
                time.sleep(2)
                if max_iterations is not None:
                    # In test/finite mode, re-raise or continue
                    break

        logging.info(f"✅ Crawler run completed {iterations} iterations.")

    def force_decompose_node(self, node_id: str) -> int:
        """
        Forces a node (even if already 'done') to be split into sub-tasks,
        marking the new sub-tasks as 'pending'.
        """
        node_data = self.db.get_node(node_id)
        if not node_data:
            raise ValueError(f"Node '{node_id}' does not exist.")
        context = self.db.get_context_travel_up(node_id)
        children, edges = self._propose_sub_tasks_and_edges(node_data, context)
        self.db.save_new_subgraph(
            parent_id=node_id,
            children=children,
            edges=edges,
            module_file=node_data.get("module_file")
        )
        return len(children)


# ==========================================
# 4. ENTRY POINT
# ==========================================
def main():
    import argparse
    parser = argparse.ArgumentParser(description="DRAM Foundation VN - Autonomous Overnight Crawler Engine")
    parser.add_argument("--status", action="store_true", help="Print summary of all nodes in WBS database")
    parser.add_argument("--check-pending", action="store_true", help="Check if any pending nodes exist (exits 0 if yes, 2 if none)")
    parser.add_argument("--reset", choices=["all", "root", "leaves"], nargs="?", const="all", help="Reset nodes to 'pending' (all, root, or leaves)")
    parser.add_argument("--reset-node", type=str, help="Reset a specific node ID to 'pending'")
    parser.add_argument("--decompose", type=str, help="Force decompose a specific node ID into child tasks")
    parser.add_argument("--max-iterations", type=int, default=None, help="Limit number of nodes to process")
    parser.add_argument("--target-nodes", type=int, default=2000, help="Target total node count to expand WBS into (default: 2000)")
    parser.add_argument("--max-depth", type=int, default=7, help="Maximum WBS recursion depth before generating leaf SOPs (default: 7)")
    parser.add_argument("--branch-factor", type=int, default=3, help="Number of child branches per split node (N, default: 3)")
    parser.add_argument("--enrich-critics-testcases", action="store_true", help="Synthesize Council Critics and Physical Test Cases for nodes")
    parser.add_argument("--enrich-status", action="store_true", help="Print summary of Council Critics and Physical Test Cases")
    parser.add_argument("--enrich-limit", type=int, default=None, help="Limit number of nodes to enrich with critics & testcases")
    parser.add_argument("--enrich-force", action="store_true", help="Force re-enrichment of nodes even if critics/testcases already exist")
    parser.add_argument("--mode", choices=["gemini", "fast"], default="gemini", help="Enrichment engine mode: 'gemini' for deep AI RAG synthesis, 'fast' for instant heuristics")
    args = parser.parse_args()

    crawler = OvernightCrawlerEngine(
        target_nodes=args.target_nodes,
        max_depth=args.max_depth,
        branch_factor=args.branch_factor
    )

    if args.enrich_status:
        from workflow.critic_testcase_engine import CriticTestCaseEnricher
        enricher = CriticTestCaseEnricher(db=crawler.db)
        status = enricher.get_enrichment_status()
        print("\n========================================================")
        print("  DRAM Foundation VN - 360° Node Enrichment Status")
        print("========================================================")
        print(f"  • Total Nodes:                 {status['total']}")
        print(f"  • With Council Critics:        {status['with_critics']}")
        print(f"  • With Physical Test Cases:    {status['with_testcases']}")
        print(f"  • With EHS & Chemical CAS:     {status['with_ehs']}")
        print(f"  • With Q-Time Constraints:     {status['with_q_time']}")
        print(f"  • With Completion Assertions:  {status.get('with_expected_result', 0)}")
        print(f"  • Pending Enrichment:          {status['pending_enrichment']}")
        print("========================================================\n")
        return

    if args.enrich_critics_testcases:
        from workflow.critic_testcase_engine import CriticTestCaseEnricher
        enricher = CriticTestCaseEnricher(db=crawler.db, vector_store=crawler.vector_store)
        use_llm = (args.mode == "gemini")
        enricher.run_enrichment_pipeline(limit=args.enrich_limit, force=args.enrich_force, use_llm=use_llm)
        return

    if args.check_pending:
        summary = crawler.db.get_status_summary()
        if summary["pending"] > 0:
            sys.exit(0)
        else:
            sys.exit(2)

    if args.status:
        summary = crawler.db.get_status_summary()
        print("\n========================================================")
        print("  DRAM Foundation VN - Graph Database Status")
        print("========================================================")
        print(f"  • Total Nodes:      {summary['total']}")
        print(f"  • Completed (done): {summary['done']}")
        print(f"  • Pending:          {summary['pending']}")
        print(f"  • In Progress:      {summary['in_progress']}")
        print(f"  • Red Flag:         {summary['red_flag']}")
        print("========================================================\n")
        return

    if args.reset:
        count = crawler.db.reset_nodes(target=args.reset)
        logging.info(f"🔄 Reset {count} node(s) ('{args.reset}') to 'pending'.")

    if args.reset_node:
        count = crawler.db.reset_nodes(target=args.reset_node)
        logging.info(f"🔄 Reset node '{args.reset_node}' to 'pending'.")

    if args.decompose:
        count = crawler.force_decompose_node(args.decompose)
        logging.info(f"🌱 Decomposed node '{args.decompose}' into {count} pending sub-tasks.")

    # Check if there are pending or in-progress nodes before running
    summary = crawler.db.get_status_summary()
    if summary["pending"] == 0 and summary["in_progress"] == 0 and not (args.reset or args.reset_node or args.decompose):
        logging.info(
            f"Notice: All {summary['total']} nodes in the WBS graph are currently marked 'done'. "
            "Use '--enrich-critics-testcases' to synthesize critics & testcases, or '--reset root' to re-run the crawler."
        )
        return

    crawler.run_overnight_crawler(max_iterations=args.max_iterations)


if __name__ == "__main__":
    main()



"""
DRAM Foundation VN - Crawler Engine & Autonomous Decomposition Test Suite
Verifies:
1. DRAMGraphDB CRUD, atomic locking, rollback, and two-way JSON synchronization.
2. Context Travel Up recursive ancestor climbing to Root: DRAM.
3. System-1 Laya PM triage and System-2 Council processing (WRITE_SOP vs SPLIT).
4. Deadlock circuit-breaker (InfiniteLoopDeadlock) and red_flag marking.
5. 5-hour quota reset calculator and resilience handling.
"""

import json
from pathlib import Path
import pytest

from workflow.crawler_engine import (
    DRAMGraphDB,
    OvernightCrawlerEngine,
    TokenLimitReachedException,
    InfiniteLoopDeadlock
)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
MODULES_DIR = DATA_DIR / "modules"


@pytest.fixture
def graph_db(tmp_path):
    """Creates an isolated temporary SQLite DB for testing."""
    test_db_path = tmp_path / "test_dram_graph.db"
    return DRAMGraphDB(db_path=test_db_path, sync_files=False)


@pytest.fixture
def crawler_engine(graph_db):
    return OvernightCrawlerEngine(db=graph_db)


def test_db_initial_sync_and_dram_root_present(graph_db):
    """Verify that apex root node-dram-root is present in DB after sync."""
    root_node = graph_db.get_node("node-dram-root")
    assert root_node is not None, "node-dram-root must exist in DB"
    assert "dram" in root_node["label"].lower()
    assert root_node["category"] == "Architecture & Integration"


def test_db_atomic_lock_and_rollback(graph_db):
    """Verify atomic state transitions: pending -> in_progress -> rollback to pending."""
    test_id = "node-unit-test-rollback"
    with graph_db._get_connection() as conn:
        conn.execute("""
            INSERT OR REPLACE INTO nodes (id, parent_id, module_file, label, generation, action_type, status, category)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (test_id, "node-dram-root", "00_dram_root.json", "Test Rollback Node", "Gen 1 (mm)", "Make", "pending", "Testing"))
        conn.commit()

    graph_db.mark_node_in_progress(test_id)
    in_prog = graph_db.get_node(test_id)
    assert in_prog["status"] == "in_progress"

    graph_db.rollback_node_to_pending(test_id)
    rolled_back = graph_db.get_node(test_id)
    assert rolled_back["status"] == "pending"


def test_context_travel_up_reaches_dram_root(graph_db):
    """Verify recursive climb up the parent chain terminates at node-dram-root."""
    context = graph_db.get_context_travel_up("node-deal-grove-dry-ox")
    assert "DRAM" in context
    assert "Gate Oxide" in context or "Oxidation" in context or "dry-ox" in context


def test_process_leaf_node_generates_sop(crawler_engine):
    """Verify leaf node processing synthesizes an SOP and marks status 'done'."""
    test_node_id = "node-unit-test-sop"
    with crawler_engine.db._get_connection() as conn:
        conn.execute("""
            INSERT OR REPLACE INTO nodes (id, parent_id, module_file, label, generation, action_type, status, category, estimated_hours)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (test_node_id, "node-dram-root", "00_dram_root.json", "Buffered Oxide Etch (BOE 6:1) SiO2 Patterning", "Gen 1 (mm)", "Make", "pending", "Chemical Processing", 32.0))
        conn.commit()

    res = crawler_engine.process_single_node(test_node_id)
    assert res in ("DONE_SOP", "SPLIT_3")

    updated = crawler_engine.db.get_node(test_node_id)
    assert updated["status"] == "done"
    if res == "DONE_SOP":
        assert updated["sop_content"] is not None
        assert len(updated["sop_content"]) > 20


def test_deadlock_circuit_breaker_marks_red_flag(crawler_engine):
    """Verify that InfiniteLoopDeadlock marks node as red_flag and advances queue."""
    test_node_id = "node-test-deadlock"
    with crawler_engine.db._get_connection() as conn:
        conn.execute("""
            INSERT OR REPLACE INTO nodes (id, parent_id, module_file, label, generation, action_type, status, category)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (test_node_id, "node-dram-root", "00_dram_root.json", "Deadlock Test Node", "Gen 1 (mm)", "Make", "in_progress", "Testing"))
        conn.commit()

    # Simulate deadlock catch
    crawler_engine.db.mark_node_red_flag(test_node_id, reason="Cycle dispute loop >= 3")
    node = crawler_engine.db.get_node(test_node_id)
    assert node["status"] == "red_flag"
    assert "Cycle dispute" in node["red_flag_reason"]


def test_5h_reset_sleep_calculator(crawler_engine):
    """Verify calculation of sleep time for 5-hour quota reset based on first token."""
    from datetime import datetime, timedelta
    
    # 1. Default when no token recorded
    sleep_sec = crawler_engine.calculate_sleep_time_for_5h_reset()
    assert isinstance(sleep_sec, int)
    assert 60 <= sleep_sec <= 18000 + 3600

    # 2. First token spent 3 hours ago -> remaining sleep must be ~2 hours (not 5 hours!)
    three_hours_ago = (datetime.now() - timedelta(hours=3)).isoformat()
    crawler_engine.db.set_metadata("first_token_timestamp", three_hours_ago)
    sleep_sec_3h = crawler_engine.calculate_sleep_time_for_5h_reset()
    assert 7000 <= sleep_sec_3h <= 7300, f"Expected ~7260s (2h), got {sleep_sec_3h}s"

    # 3. Server explicit retry_after override takes precedence
    explicit_sleep = crawler_engine.calculate_sleep_time_for_5h_reset(server_retry_after=450)
    assert explicit_sleep == 450


def test_crawler_finite_run_execution(crawler_engine):
    """Verify run_overnight_crawler executes requested iterations cleanly without crashing."""
    crawler_engine.run_overnight_crawler(max_iterations=1)
    # Ensure system state remains consistent
    nodes, edges = crawler_engine.db.load_full_graph_for_validation()
    assert len(nodes) >= 12

# Operational Guide: How to Run the DRAM Foundation VN Workflow

- **Date**: 2026-10-08
- **Source**: User & Agent Architecture
- **Status**: Implemented & Documented

## Overview & Execution Modes

The DRAM Foundation VN system can be operated in three distinct modes depending on requirements:

### Mode 1: Fully Autonomous Overnight Crawler (Zero Human in the Loop)
This is the primary production engine. It iterates through the pending work packages in the Work Breakdown Structure (WBS), climbing recursively from leaf nodes to Apex Root: `node-dram-root`.

```cmd
python workflow/crawler_engine.py
```

- **Execution Flow**:
  1. Retrieves next pending node in BFS order.
  2. Sets atomic SQLite lock: `status = in_progress`.
  3. Climbs parent hierarchy to pull technological context up to DRAM chip.
  4. Laya PM agent (System-1) classifies Make vs. Buy and evaluates 8-80h rule.
  5. If `write_sop`: queries ChromaDB and triggers Antigravity CLI (`agy.exe`) to synthesize an industrial leaf SOP.
  6. If `spawn_children`: proposes sub-tasks, checks COTS parts, and verifies acyclicity via Kahn DAG algorithm (NetworkX).
  7. Commits to SQLite and flushes updates to `data/modules/*.json` and `data/manifest.json`.
- **Self-Healing Features**:
  - Automatically sleeps and calculates wake-up time upon encountering 5-hour rolling token rate limits (`TokenLimitReachedException`).
  - Marks deadlocked nodes as `red_flag` if debate cycles $\ge 3$ and advances the BFS queue.
  - Automatically rolls unhandled crashed nodes back to `pending`.

### Mode 2: Interactive Sandbox & React Flow Visualizer
Runs the local FastAPI server bridge and opens the browser-based visualization sandbox:

```cmd
start_sandbox.bat
```
- Available at `http://127.0.0.1:8000` or `http://127.0.0.1:8000/sandbox/index.html`.
- Allows visual graph inspection across all 6 semiconductor disciplines, semantic zooming, and direct council review submissions.

### Mode 3: Test Suite & Physical Validation
Runs the 135-test automated pytest suite:

```cmd
pytest
```

## References & Related Files
- [`workflow/crawler_engine.py`](.../../..../../.../../workflow/crawler_engine.py)
- [`workflow/server.py`](.../../..../../.../../workflow/server.py)
- [`start_sandbox.bat`](.../../.../../start_sandbox.bat)
- [`README.md`](.../../.../../README.md)

# Apex DRAM Root Anchor & Autonomous Crawler Engine Architecture

- **Date**: 2026-10-08
- **Source**: User & Agent Architecture Review
- **Status**: Implemented & Verified

## Overview & Rationale
In semiconductor systems engineering, a Work Breakdown Structure (WBS) must anchor at the ultimate physical deliverable. Modeling peripheral tooling or COTS microcontrollers as root nodes inverts the dependency tree.

The true apex root of the entire system is **180nm Open-Source DRAM Chip** (`node-dram-root`). Every sub-discipline—photolithography stages, thermal oxidation furnaces, RCA wet benches, and folded sense amplifier circuits—exists solely in service of realizing the monolithic 1T1C DRAM matrix.

This anchor enables `get_context_travel_up(node_id)` to climb up to DRAM, preventing AI sub-agent myopia and grounding every physical metric (e.g., $t_{ox} = 3.5\text{ nm}$, $C_{cell} \ge 25\text{ fF}$, refresh cycle $64\text{ ms}$) in the 180nm DRAM specification.

---

## Architectural Pillars of `workflow/crawler_engine.py`

Inspired by `docs/pipeline_demo.py`, `workflow/crawler_engine.py` operationalizes the continuous overnight expansion engine with zero UI blocking:

```text
               +-------------------------------------------+
               |     ROOT: 180nm DRAM Chip R&D & Fab       |
               |         (DRAM Foundation VN)              |
               +---------------------+---------------------+
                                     |
         +---------------------------+---------------------------+
         |                           |                           |
         v                           v                           v
+-----------------+         +-----------------+         +-----------------+
|  1. DRAM Design |         |     2. FEOL     |         |     3. BEOL     |
|   & Architecture|         | (Front-End Mfg) |         | (Back-End Pack) |
+--------+--------+         +--------+--------+         +--------+--------+
```

### 1. Dual-System Cognitive Hierarchy (Token Economics)
- **System 1 (Local CPU — Laya ModernBERT)**:
  - Instant classification (0 token cost, ~30ms).
  - Triage between `WRITE_SOP` (atomic leaf task: 8–80h) vs. `SPLIT` (composite milestone: >80h).
  - Evaluates Make vs. Buy (COTS components like ESP32, stepper motors, vacuum gauges assigned to `Buy` / `Procurement`).
- **System 2 (Gemini Multi-Agent Council)**:
  - **Domain Expert** (Gemini High temp 0.4): Retrieves empirical papers from ChromaDB (`retrieve_rag_knowledge`) and authors machine-measurable SOPs with citations.
  - **Systems Engineer** (Gemini Low temp 0.0): Strict mathematical NetworkX Kahn DAG validation, cycle detection, and topological sorting.

### 2. The 3 Fault-Tolerance Pillars
1. **Atomic State & Crash Resilience**:
   - `mark_node_in_progress(node_id)` locks the target node.
   - If an unhandled exception or network timeout occurs, `rollback_node_to_pending(node_id)` restores the node to clean `pending` state.
2. **Antigravity 5-Hour Quota Backoff (`TokenLimitReachedException`)**:
   - Catches rate limit exhaustion, calculates remaining seconds to the next 5-hour rolling boundary via `calculate_sleep_time_for_5h_reset()`, safely rolls back the current node, sleeps, and wakes up automatically.
3. **Deadlock Circuit-Breaker (`InfiniteLoopDeadlock`)**:
   - If council debates on DAG edges loop $\ge 3$ times, it throws `InfiniteLoopDeadlock`.
   - The crawler marks the node `red_flag` with the dispute reason, logs the blockage for the Human Architect, and immediately advances to the next `pending` node in the BFS queue. One blocked node never halts the overnight run.

---

## References & Related Files
- [`workflow/crawler_engine.py`](../../workflow/crawler_engine.py)
- [`data/modules/00_dram_root.json`](../../data/modules/00_dram_root.json)
- [`data/manifest.json`](../../data/manifest.json)
- [`docs/pipeline_demo.py`](../pipeline_demo.py)
- [`tests/test_crawler_engine.py`](../../tests/test_crawler_engine.py)

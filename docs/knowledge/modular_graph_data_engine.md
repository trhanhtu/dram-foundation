# DRAM Foundation VN - Phase 2: Modular Graph Data Engine

- **Date**: 2026-10-08
- **Source**: Agent
- **Status**: Implemented & Verified

---

## 1. Objective & Strategic Purpose
As specified in [docs/context3.yaml](.../../context3.yaml) (*Graph Pull Requests*) and [docs/plan_n_days.md](.../../plan_n_days.md) (*Phase 2*), Phase 2 solves the critical challenge of collaborative graph authoring:
- **The Problem**: A monolithic 1,000-node JSON file creates catastrophic Git merge conflicts when multiple engineers and sub-agents contribute concurrently.
- **The Solution**: **Modular JSON Architecture** where sub-graphs are isolated into domain modules (e.g. `01_mcu_cots.json`, `02_litho_stage_gen1.json`), assembled dynamically by a local-first client engine, and verifiable via Kahn's topological cycle detection.

---

## 2. Directory Layout & Schemas

```text
data/
├── manifest.json                  # Registry of active graph modules
├── schema/
│   ├── node.schema.json           # JSON Schema Draft-07 for WBS Nodes
│   └── edge.schema.json           # JSON Schema Draft-07 for DAG Edges
└── modules/
    ├── 01_mcu_cots.json           # Drive Electronics & Firmware (COTS)
    ├── 02_litho_stage_gen1.json   # Precision Mechanics (Gen 1 mm)
    └── 03_optical_aligner_gen2.json # Mask Optical Alignment (Gen 2 µm)
```

---

## 3. Data Engine Components (`sandbox/data-engine.js`)

```text
┌────────────────────────┐
│  data/manifest.json    │
│  (Module Registry)     │
└───────────┬────────────┘
            │ Parallel Fetch
            ▼
┌────────────────────────┐
│  data/modules/*.json   │
│  (Modular Sub-Graphs)  │
└───────────┬────────────┘
            │ Dynamic Merge
            ▼
┌────────────────────────┐
│  Kahn's Algorithm      │
│  Cycle & DAG Checker   │
└───────────┬────────────┘
            │ Validated DAG
            ▼
┌────────────────────────┐
│  LocalStorage Cache    │
│  (Offline-First Sync)  │
└───────────┬────────────┘
            │
            ├────────────────────────────╮
            ▼                            ▼
┌────────────────────────┐  ┌────────────────────────┐
│  React Flow Canvas UI  │  │  Export Graph PR JSON  │
│  (Live Interactive)    │  │  (GitHub Review Ready) │
└────────────────────────┘  └────────────────────────┘
```

1. **Dynamic Module Loader**: Fetches all registered modules in parallel via standard `fetch()` and stitches them into a unified React Flow graph with automatic grid positioning.
2. **Kahn's Topological DAG Validator**: Calculates node in-degrees and iteratively visits zero-indegree nodes. If `visitedCount !== totalNodes`, immediately detects cyclic dependencies and flags the graph.
3. **Local-First State Persistence**: Edits (status transitions, parameter tweaks) save instantly to `localStorage` (`dram_graph_override_v1`), ensuring offline resilience without requiring an active database server in Phase 2.
4. **Modular PR Exporter**: Generates clean, downloadable JSON payloads of individual modules or the full working graph, enabling peer review via GitHub PRs without code reviews.

---

## 4. Node Lifecycle State Machine

Each node transitions across four standardized states:
- `pending`: Work package scoped by Systems Engineer, awaiting assignment or resources.
- `in_progress`: Active laboratory prototyping or procurement.
- `done`: Verified with attached **Proof of Work** (CAD repository and physical test video).
- `red_flag`: Technical roadblock, supply chain embargo, or testing failure triggering an upstream Feedback Loop.

---

## References & Related Files
- [data/manifest.json](.../../..../../.../../data/manifest.json)
- [data/schema/node.schema.json](.../../..../../.../../data/schema/node.schema.json)
- [data/schema/edge.schema.json](.../../..../../.../../data/schema/edge.schema.json)
- [sandbox/data-engine.js](.../../.../../sandbox/data-engine.js)
- [sandbox/index.html](.../../.../../sandbox/index.html)
- [docs/context3.yaml](.../../context3.yaml)

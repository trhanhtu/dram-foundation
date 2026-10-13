# E2E Testing & Semantic Zoom Architecture

- **Date**: 2026-10-08
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale

To deliver the DRAM Foundation VN Semiconductor Knowledge OS under an autonomous overnight mandate without human-in-the-loop, the system established two advanced architectural capabilities:
1. A **4-Tier Opaque-Box E2E Testing Architecture** spanning 89 automated tests with a 100% pytest pass rate.
2. A **Nested Graphs & 3-Tier Semantic Zooming Canvas** in React Flow with live FastAPI bridge synchronization and zero `localStorage` persistence.

---

## 1. 4-Tier Opaque-Box E2E Test Suite

The test suite validates the entire vertical stack from REST endpoints to physical semiconductor manufacturing rules.

```text
┌────────────────────────┐    ┌────────────────────────┐    ┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │    │                        │    │                        │
│    Tier 1: Feature     │    │   Tier 2: Boundary &   │    │  Tier 3: Cross-Module  │    │      Tier 4: Fab       │
│        Coverage        │    │         Corner         │    │      Interactions      │    │       Workflows        │
│                        │    │                        │    │                        │    │                        │
└─────────┬──────────────┘    └────────────┬───────────┘    └────────────┬───────────┘    └────────────┬───────────┘
          │                                │                             │                             │
          │ ╭──────────────────────────────┴─────────────────────────────╯                             │
          ▼ ▼                                                                                          ▼
┌────────────────────────┐                                                                ┌────────────────────────┐
│                        │                                                                │                        │
│  FastAPI Bridge Server │                                                                │  Realistic Wafer Fab   │
│  (workflow/server.py)  │                                                                │    Process Pipeline    │
│                        │                                                                │                        │
└─────────┬──────────────┘                                                                └────────────┬───────────┘
          │                                                                                            │
          │ ╭─────────────────────────────┬─────────────────────────────╮                              │
          ▼ ▼                             ▼                             ▼                              ▼
┌────────────────────────┐   ┌────────────────────────┐   ┌────────────────────────┐     ┌────────────────────────┐
│  Systems Engineer DAG  │   │  Laya PM 8-80h Model   │   │  ChromaDB RAG Corpus   │     │    Modular WBS JSON    │
│       Validator        │   │  (Make vs Buy Bounds)  │   │  (22 Literature Chunks)│     │     SSOT on Disk       │
└────────────────────────┘   └────────────────────────┘   └────────────────────────┘     └────────────────────────┘
```

### Coverage Tiers & Distribution

- **Tier 1 (Feature Coverage - 20 tests)**: Exhaustive endpoint contracts for `/api/status`, `/api/graph`, `/api/manifest`, `/api/modules`, `/api/search`, `/api/crawl`, `/api/council/review`, and `/api/council/commit`.
- **Tier 2 (Boundary & Corner Cases - 26 tests)**: Empty query handling, extreme chunk sizes, invalid schema enums, multi-node cycles, self-loops, duplicate IDs, dangling edges, 404 missing modules, and strict Laya PM effort clamping to $[8, 80]$ hours.
- **Tier 3 (Cross-Module Interactions - 6 tests)**: Full pipeline testing from vector literature search to AI Council review, disk commit, manifest count synchronization, and live graph reload.
- **Tier 4 (Real-World Semiconductor Workflows - 8 tests)**: Authentic fabrication sequences:
  - RCA-1/2 cleaning $\to$ Deal-Grove dry gate oxidation ($3.5\text{ nm}$) $\to$ photolithography alignment $\to$ 1T1C DRAM cell capacitor layout ($28\text{ fF}$).
  - Signal chain: 1T1C storage cell $\to$ Folded bitline sense amplifier $\to$ Row/column decoders with $2.8\text{V } V_{PP}$ charge pump.
  - Bits-to-Atoms validation: verified hardware repositories and laboratory demonstration videos.
- **Baseline Unit Tests (29 tests)**: Foundational tests covering DAG acyclicity, vector store, crawler, and server API.
- **Total: 89 passed in ~41s (100% pass rate).**

### Test Idempotency & Data Safety
Tests that mutate files utilize an automated snapshot-and-restore fixture (`isolated_wbs_state`) in pytest. Backups of `data/manifest.json` and all `data/modules/*.json` are captured before mutation and restored immediately upon teardown, preventing test suite leakage.

---

## 2. React Flow Nested Graphs & 3-Tier Semantic Zooming

To prevent visual clutter ("Spaghetti Graph" anti-pattern) when scaling to hundreds of nodes, the UI implements a hierarchical containment pattern:

```text
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
│   RCA Wafer Cleaning   │    │  Electronics & Stage   │
│          Line          │    │         Drive          │
│                        │    │                        │
└────────────┬───────────┘    └────────────┬───────────┘
             │                             │
             │                             │
             ▼                             ▼
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
│  Deal-Grove Dry Gate   │    │    Microscopic Mask    │
│       Oxidation        │    │        Aligner         │
│                        │    │                        │
└─────────────┬──────────┘    └────────────┬───────────┘
              │                            │
            ╭─┼────────────────────────────╯
            ▼ ▼
┌────────────────────────┐
│                        │
│     DRAM 1T1C Cell     │
│    Capacitor Layout    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Folded Bitline Sense  │
│       Amplifier        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Wordline Decoders &   │
│        VPP Pump        │
│                        │
└────────────────────────┘
```

### Hierarchy & Positioning
- **Parent Group Nodes (`disciplineGroup`)**: Represent each of the 6 disciplines (Electronics & Drive, Litho Stage, Optics Aligner, Wet Chemistry, Thermal Oxidation, DRAM Cell). Dimensions dynamically scale with child count.
- **Child Semiconductor Nodes (`semiconductorNode`)**: Positioned relative to parent group coordinates using `parentNode: 'group-...'` and `extent: 'parent'`.
- **Breadcrumb Navigation**: Supports drill-down into individual module sub-graphs with one-click return to full overview.

### 3-Tier Level-of-Detail (LOD)
1. **Macro Level (`zoom < 0.70`)**: Displays minimal footprint with action pill (Make/Buy), node ID, and title.
2. **Standard Level (`0.70 ≤ zoom ≤ 1.30`)**: Standard engineering view displaying status badge, category tag, TRL generation badge, and primary quantitative metric.
3. **Deep Level (`zoom > 1.30`)**: Deep-dive inspection view expanding to display empirical literature citations, estimated hours ($8-80\text{h}$ rule), machine-measurable acceptance criteria, and laboratory SOP links.

---

## 3. Single Source of Truth (SSOT) & Model Constraints

- **No `localStorage` Persistence**: The system strictly uses modular JSON files on disk (`data/modules/*.json` and `data/manifest.json`) as the single source of truth.
- **Exclusively Gemini**: Generative RAG lookup and SOP authoring exclusively invoke Gemini via Google Antigravity. No OpenAI/ChatGPT or Anthropic/Claude models are used.
- **Local CPU System 1**: Laya ModernBERT CPU performs Make vs. Buy classification and 8-80h effort bounds with 0 token expenditure.

---

## References & Related Files

- [TEST_INFRA.md](../../TEST_INFRA.md)
- [TEST_READY.md](../../TEST_READY.md)
- [tests/test_e2e_comprehensive.py](../../tests/test_e2e_comprehensive.py)
- [tests/test_semiconductor_workflows.py](../../tests/test_semiconductor_workflows.py)
- [sandbox/index.html](../../sandbox/index.html)
- [sandbox/data-engine.js](../../sandbox/data-engine.js)
- [index.html](../../index.html)
- [data-engine.js](../../data-engine.js)
- [workflow/server.py](../../workflow/server.py)
- [PROJECT.md](../../PROJECT.md)

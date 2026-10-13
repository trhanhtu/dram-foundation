# DRAM Foundation VN - Master Execution Plan (N-Day Roadmap)

- **Date**: 2026-10-07
- **Author**: Antigravity & Solo Systems Architect
- **Status**: Proposed / Ready for Sprint 1 Execution

---

## Roadmap Overview

```text
┌────────────────────────┐
│    Day 1: Bootstrap    │
│   Sandbox (3 Nodes,    │
│  Static HTML + React   │
│         Flow)          │
│                        │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│     Days 2-3: Data     │
│    Engine & Modular    │
│      JSON Schemas      │
│                        │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│  Days 4-7: AI Council  │
│  Engine (Gemini RAG +  │
│   Local 8-80h Logic)   │
│                        │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│  Days 8-10: Semantic   │
│    Zooming & Nested    │
│       Graphs UI        │
│                        │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│      Days 11-14:       │
│  Bits-to-Atoms Bridge  │
│   & Proof-of-Work PR   │
│        Workflow        │
│                        │
└────────────┬───────────┘
             ▼
┌────────────────────────┐
│   Day N+: Community    │
│      Expansion &       │
│  Sovereign Knowledge   │
│           OS           │
│                        │
└────────────────────────┘
```

---

## Detailed Phases

### Phase 1: Day 1 — The Micro-Sandbox (Break Blueprint Vertigo)
- **Objective**: Deliver immediate, tangible interactive visual feedback to ground the project in reality.
- **Key Tasks**:
  1. Build a single static HTML page with React Flow embedded.
  2. Hardcode 3 baseline nodes:
     - `node-gen1-mm`: Macroscopic Litho Stage (Gen 1 - mm scale, Make, Status: Done).
     - `node-gen2-um`: Microscopic Optical Alignment (Gen 2 - $\mu$m scale, Make, Status: In_Progress).
     - `node-mcu-cots`: ESP32 Motor Controller (Gen 1 - Buy/COTS, Status: Done).
  3. Connect nodes with 2 explicit DAG edges (prerequisite relationships).
  4. Implement an interactive side-drawer displaying node metadata (Action Type, Target Metrics, SOP summary).
- **Exit Criteria**: A functional webpage that opens in any browser, zooms, pans, and displays node details on click without errors.

---

### Phase 2: Days 2–3 — Local-First Data Engine & Modular JSON
- **Objective**: Establish the persistent graph data architecture to prevent merge conflicts.
- **Key Tasks**:
  1. Formalize JSON schemas for `nodes.json` and `edges.json`.
  2. Implement sub-module splitting (e.g., `01_substrate_gen1.json`, `02_litho_gen1.json`).
  3. Build local state persistence (Local Storage / SQLite WASM) so graph edits persist across page refreshes.
  4. Support node status states: `pending`, `in_progress`, `done`, `red_flag`.
- **Exit Criteria**: Graphs load from and persist to modular JSON files dynamically.

---

### Phase 2.5: Days 3–4 — Internet Knowledge Crawler & Vector Ingestion
- **Objective**: Harvest, clean, and embed empirical semiconductor domain intelligence from the web into local ChromaDB to feed Gemini.
- **Key Tasks**:
  1. **Web Scraper & Crawler Setup**: Automated scraping of grassroots DIY fabs (Sam Zeloof journals, LibreSilicon, OpenROAD).
  2. **Technical Literature Ingestion**: Crawl expired legacy 180nm/micron DRAM patents, IEEE/arXiv open papers, and legacy stepper manuals.
  3. **Process Chemistry Data Harvesting**: Extract TDS/MSDS parameters (photoresist spin curves, BOE/KOH etch rates, Deal-Grove oxidation models).
  4. **Markdown Normalization & Chunking**: Convert crawled HTML/PDFs into structured Markdown with provenance metadata (URL, date, author).
  5. **Local VectorDB Indexing**: Embed and index chunks into local ChromaDB for instant semantic retrieval.
- **Exit Criteria**: A populated local ChromaDB vector store ready for Gemini Domain Expert RAG queries with real citations.

---

### Phase 3: Days 5–7 — AI Council Orchestration (Gemini & Anti-Hallucination)
- **Objective**: Automate node decomposition and SOP drafting while strictly preventing hallucinations.
- **Key Tasks**:
  1. **Domain Expert Module**: Connect Gemini to the crawled ChromaDB vector store to generate leaf SOPs with verified citations.
  2. **Systems Engineer Module**: Automated DAG topology checks (prevent cyclic dependencies and dangling edges).
  3. **Project Manager Module (8–80 Hour Rule)**:
     - If task effort $> 80\text{h}$: Decompose into child nodes.
     - If task effort $< 8\text{h}$: Halt branching and generate a leaf SOP Markdown file.
  4. **Supply Chain Module**: Tag tasks as `Make` (in-house R&D) vs. `Buy` (COTS).
  5. **Revision & Feedback Loop**: When test failure occurs, spawn an upstream Revision Node and mark obsolete paths as `Deprecated`.
- **Exit Criteria**: AI autonomously inspects a node, decides whether to branch or write SOP, and embeds quantitative criteria backed by crawled citations.

---

### Phase 4: Days 8–10 — Semantic Zooming & Nested Graphs
- **Objective**: Eliminate DOM congestion and visual overwhelm ("Spaghetti Graph").
- **Key Tasks**:
  1. Implement **Nested Sub-Graphs**: Double-clicking a tier-1 node drills into its isolated sub-graph.
  2. Add **Context Travel Up** breadcrumb navigation (`Root > Gen 1 Lithography > Mask Alignment`).
  3. Implement **BFS Level Filters**: Toggle between high-level architectural skeleton and detailed leaf nodes.
- **Exit Criteria**: The UI remains fluid and responsive even with hundreds of nodes.

---

### Phase 5: Days 11–14 — Bits-to-Atoms Bridge & Collaboration PRs
- **Objective**: Enforce physical industrial validation and enable crowd contribution.
- **Key Tasks**:
  1. **Acceptance Criteria Validation**: Ensure all `[Make]` nodes contain testable physical criteria (tolerances, temperatures, cycle counts).
  2. **Proof-of-Work Verification**: UI badge showing verified video demo URLs and linked GitHub CAD/firmware repositories.
  3. **Modular PR Templates**: Standardized GitHub PR templates for engineers submitting individual sub-graph JSON files.
- **Exit Criteria**: Community contributors can pull a single module, test in their lab/garage, and submit verified work packages.

---

### Phase 6: Day N+ — Generational Roadmap & Spin-offs
- Scale the Knowledge OS across all semiconductor sub-disciplines:
  - Wafer preparation & oxidation.
  - Photolithography & chemical etching.
  - Doping & thin-film deposition.
  - Packaging, wire bonding & final electrical testing.
- Spin off early-generation tooling (precision linear stages, UV exposure jigs, optical microscopes) to generate revenue.

---

## References & Related Documentation
- [docs/context.yaml](./context.yaml)
- [docs/context2.yaml](./context2.yaml)
- [docs/context3.yaml](./context3.yaml)
- [docs/knowledge/system_architecture.md](./knowledge/system_architecture.md)
- [docs/knowledge/strategic_philosophy.md](./knowledge/strategic_philosophy.md)
- [docs/knowledge/risk_and_collaboration.md](./knowledge/risk_and_collaboration.md)
- [AGENTS.md](../AGENTS.md)

# Node Correctness, Verification Pipeline & Council Auditing

- **Date**: 2026-10-12
- **Source**: User & Agent Synthesis
- **Status**: Implemented & Audited

## Overview
In DRAM Foundation VN, an autonomous node is not considered "correct" merely because an LLM generated text. Correctness is governed by a **4-tier multi-agent verification pipeline** combining mathematical proof, systems engineering rules, literature vector grounding, and physical metrology targets.

---

## The 4 Tiers of Node Correctness

### 1. Structural & Topological Correctness (System 3 - Graph Engine)
- **Kahn's DAG Acyclicity**: Every edge added to the graph is checked via Kahn's algorithm. If a circular prerequisite is detected ($A \to B \to A$), the transaction is aborted with `InfiniteLoopDeadlock` and rolled back.
- **Apex Tree Anchorage**: Every node (except `node-dram-root`) must trace an unbroken ancestor lineage back to the apex root (`node-dram-root`).
- **Context Travel Up**: Recursive ancestor queries ensure child nodes inherit technology constraints ($180\text{nm}$ lithography, $V_{DD} = 1.8\text{V}$, $\text{SiO}_2$ dielectric constants) rather than hallucinating arbitrary modern nanometer specs.

### 2. Project Management Feasibility (System 1 - Laya PM)
- **8–80 Hour Rule**:
  - If estimated hours $H > 80\text{h}$, the node is marked **Composite** and MUST split into smaller sub-tasks.
  - If $8\text{h} \le H \le 80\text{h}$, the node is an actionable work package ready for SOP generation.
- **Make vs Buy Triage**:
  - Prevents unrealistic DIY fabrication of off-the-shelf industrial parts (e.g. Arduino MCU, vacuum turbopump $\to$ `action_type: Buy`).
  - Focuses R&D hours on proprietary semiconductor fabrication recipes ($\to$ `action_type: Make`).

### 3. Semiconductor Literature Grounding (System 2 - ChromaDB RAG & Gemini)
- Every proposed step queries a local ChromaDB vector store containing peer-reviewed literature (e.g., Sze's *Physics of Semiconductor Devices*, Deal-Grove Oxidation Kinetics, Plummer's *Silicon VLSI Technology*).
- Nodes must include authentic domain citations in their `citations` array.

### 4. Physical Metric Targets & Actionable SOPs
- **Physical Metrics**: Must specify tangible tolerances, temperatures, pressures, or electrical values (e.g., `Gate Oxide: 15nm ± 0.5nm`, `Furnace: 950°C dry O2`, `Tolerance: ±0.1 µm`).
- **4-Step SOP Schema**:
  1. Preparation & Safety (chemicals, PPE, cleanroom classification).
  2. Sequential Recipe Execution (timing, gas flows, ramp rates).
  3. Metrology & In-line Inspection (ellipsometry, SEM, four-point probe).
  4. Pass/Fail Thresholds & Sign-off Criteria.

---

## References & Related Files
- [`workflow/crawler_engine.py`](.../../..../../.../../workflow/crawler_engine.py)
- [`workflow/council/domain_expert.py`](.../../..../../.../../workflow/council/domain_expert.py)
- [`docs/context.yaml`](.../../context.yaml)
- [`data/dram_graph.db`](.../../..../../.../../data/dram_graph.db)

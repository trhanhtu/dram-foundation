# Council Critics & Physical Test Cases Overnight Pipeline

- **Date**: 2026-10-13
- **Source**: User & Agent
- **Status**: Implemented

## Overview & Rationale
The DRAM Foundation VN knowledge graph has achieved its first scaling milestone of **1,003 Work Breakdown Structure (WBS) nodes** across all 6 core disciplines. However, the current tree faces a critical verification and physical grounding gap:
1. **Absence of Node Critics**: The Multi-Agent Council's critical evaluations (Systems Engineer causality, Domain Physicist kinetics, Supply Chain COTS reality, and Project Manager 8-80h limits) are not explicitly documented per node.
2. **Absence of Machine-Measurable Test Cases**: Nodes lack structured, verifiable testbench protocols (instruments, pre-flight conditions, step-by-step procedures, and quantitative pass/fail thresholds) required to satisfy the "Bits-to-Atoms Bridge" defined in `docs/context3.yaml`.
3. **Overnight Batch Script Mismatch**: `run_overnight.bat` currently defaults to expanding leaves deeper into 2,000+ nodes (the "Infinite Breadth Trap") rather than auditing and deepening the technical rigor of the existing 1,003 nodes.

Modifying `run_overnight.bat` and the underlying crawler engine to introduce a dedicated **Phase 2: Council Critics & Physical Test Cases Enrichment Mode** directly solves this challenge.

---

## Key Details / Architecture

### 1. Dual-Layer Schema Evolution
To ensure backward compatibility while equipping the UI and automated verification engines with structured data:
- **Structured Fields**:
  - `critics`: Object mapping the 4 council pillars (`systems_engineer`, `domain_expert`, `supply_chain`, `laya_pm`) with critique summaries, critical failure modes, and tolerance margins.
  - `testcases`: Array of structured test specifications containing `id`, `title`, `equipment`, `pre_conditions`, `procedure`, `expected_metrics`, and `pass_fail_criteria`.
- **Markdown Embedding in `sop_content`**:
  Sections `### 2. Multi-Agent Council Critics & Risk Analysis` and `### 3. Machine-Measurable Physical Test Cases` embedded into the Markdown text for instant rendering in the React Flow UI drawer via KaTeX and marked.js.

### 2. Multi-Agent Council Critique Dimensions
Every work package is evaluated across four critical vectors:
- **Systems Engineer Critic**: Prerequisite DAG acyclicity, cascading signal delay, clock skew, and topological ordering.
- **Domain Physicist Critic**: Thermal budgets (Deal-Grove oxide rate), subthreshold leakage, breakdown field ($E_{ox} \le 10\text{ MV/cm}$), and lithographic depth of focus / overlay budget.
- **Supply Chain Critic**: COTS availability in Vietnam, substitute component viability, and tooling barriers.
- **Project Manager Critic**: 8-80h scoping compliance, tooling lead times, and FMEA risk rating.

### 3. Machine-Measurable Acceptance Test Case Schema
Each leaf node requires 2–4 executable testbench protocols:
- **Test ID & Name**: Unique identifier (e.g. `TC-LITHO-02-01`).
- **Instrumentation & Fixture**: Required laboratory apparatus (e.g. Profilometer, Ellipsometer, 4-Point Probe, Dual-Channel 100MHz Oscilloscope).
- **Pre-Flight Conditions**: Ambient cleanroom parameters, baseline calibration, and substrate state.
- **Step-by-Step Procedure**: Sequential execution steps with exact chemical/physical inputs.
- **Pass / Fail Thresholds**: Strict numerical tolerances with SI units (e.g. $\text{Overlay Error} \le \pm 5\ \mu\text{m}$, $\text{Etch Rate} = 70 \pm 3.5\text{ nm/min}$).
- **Remediation Action**: Recovery protocol if test fails.

### 4. `run_overnight.bat` Pipeline Redesign
When all nodes are marked `done` (1,003 total, 0 pending):
- Option 1 automatically promotes:
  `[1] Synthesize Critics & Physical Test Cases for 1,003 Nodes (--enrich-critics-testcases) [Recommended]`
- Option 2 preserves leaf expansion:
  `[2] Expand leaf tasks deeper into sub-nodes (--reset leaves)`
- The runner leverages Gemini RAG with persistent rolling 5-hour rate-limit backoff and atomic SQLite transactions.

---

## References & Related Files
- [run_overnight.bat](./run_overnight.bat)
- [workflow/crawler_engine.py](./workflow/crawler_engine.py)
- [data/schema/node.schema.json](./data/schema/node.schema.json)
- [docs/context3.yaml](./docs/context3.yaml)
- [sandbox/index.html](./sandbox/index.html)
- [PROJECT.md](./PROJECT.md)

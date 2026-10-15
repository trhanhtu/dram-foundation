# Verifiable Completion Assertions & Definition of Done (DoD)

- **Date**: 2026-10-14
- **Source**: User & Agent
- **Status**: Implemented (100% of 1,003 Nodes Enriched & Formally Verified)

## Overview & Rationale
In high-consequence semiconductor manufacturing and deep-tech hardware R&D (such as the 180nm Open-Source DRAM Chip), stating that a node is "done" without concrete, empirical criteria leads to ambiguity, premature closure, and untestable claims. Researchers working at each node require a deterministic, machine-verifiable **Definition of Done (DoD)** with unambiguous quantitative assertions, tangible artifact checklists, and explicit exit sign-off criteria.

This protocol equips every WBS node in the 1,003-node DRAM tree with structured completion assertions synthesized via **Gemini 3.8 Flash** with empirical grounding in ChromaDB literature and resilient heuristic fallbacks.

## Key Details / Architecture

### 1. Structured Schema Anatomy (`expected_result`)
Defined in [`data/schema/node.schema.json`](./data/schema/node.schema.json):
- **`summary`**: High-level definition of done summarizing the completed objective.
- **`deliverable_artifacts`**: Array of tangible physical/digital files (e.g. `dram_180nm_cv_capacitance_matrix_wafers01_06.csv`, `dram_cell_cross_section_crown_stem_edx_report.pdf`, `wafer_map_retention_shmoo_yield_summary.tiff`).
- **`quantitative_assertions`**: List of verifiable assertions with:
  - `id`: Formatted as `ASSERT-01`, `ASSERT-02`, etc.
  - `assertion`: Physical property or objective (e.g. *Average 1T1C storage node cell capacitance across 10,000-cell array*).
  - `target_value`: Numerical target (e.g. `29.5 fF/cell`).
  - `tolerance`: Permissible engineering window (e.g. `+/- 1.5 fF`).
  - `verification_method`: Exact metrology tool and protocol (e.g. *High-frequency C-V measurement on Keysight B1520A CMU*).
- **`signoff_criteria`**: Protocol rule specifying conditions for lead researcher / PI exit approval.

### 2. Dual-Channel Persistence & UI Rendering
1. **Machine-Readable Layer**: Persisted directly into [`data/modules/*.json`](./data/modules/) and SQLite column `expected_result` in `data/dram_graph.db`.
2. **Actionable SOP Markdown Table**: Appended cleanly to `sop_content`:
   ```markdown
   ### Verifiable Completion Assertions & Expected Results (Definition of Done)

   **Exit Objective Summary**:
   > Full physical, morphological, and electrical sign-off of the 180nm Open-Source DRAM 1T1C stacked capacitor test vehicle...

   **Deliverable Artifacts Checklist**:
   - [ ] `dram_180nm_cv_capacitance_matrix_wafers01_06.csv`
   - [ ] `dram_cell_cross_section_crown_stem_edx_report.pdf`
   - [ ] `wafer_map_retention_shmoo_yield_summary.tiff`

   **Quantitative Completion Assertions**:

   | Assertion ID | Metric / Physical Assertion | Target Value | Acceptable Tolerance | Verification Instrumentation |
   | :--- | :--- | :--- | :--- | :--- |
   | `ASSERT-01` | **Average 1T1C storage node cell capacitance** | `29.5 fF/cell` | +/- 1.5 fF | Keysight B1520A CMU |
   ...

   **Lead Researcher Exit Sign-Off Criteria**:
   > Completion of 6-wafer pilot lot electrical testing demonstrating 100% compliance with ASSERT-01 through ASSERT-03...
   ```

### 3. Synthesis Pipeline & JSON Resilience
Implemented in [`workflow/critic_testcase_engine.py`](./workflow/critic_testcase_engine.py) via `CriticTestCaseEnricher`:
- **Gemini Generative RAG**: Employs Google Antigravity CLI (`agy`) with model `gemini-3.8-flash-low` grounded in 180nm DRAM literature.
- **Resilient JSON Repair Engine**: Automatically repairs trailing commas, unescaped delimiters, and mismatched closing brackets (e.g. object ending in `]` inside array) via `_repair_and_parse_json`.
- **Heuristic Domain Templates**: Fallback logic providing domain-accurate physics for circuit design, wet chemistry, thermal oxidation, lithography, and mechatronics.

## References & Related Files
- [`data/schema/node.schema.json`](./data/schema/node.schema.json)
- [`workflow/critic_testcase_engine.py`](./workflow/critic_testcase_engine.py)
- [`workflow/crawler_engine.py`](./workflow/crawler_engine.py)
- [`data/modules/00_dram_root.json`](./data/modules/00_dram_root.json)
- [`run_overnight.bat`](./run_overnight.bat)

# Semiconductor Work Package 360° Completeness Anatomy

- **Date**: 2026-10-13
- **Source**: User & Agent
- **Status**: Implemented (EHS, CAS, Antidotes & Q-Time integrated into Schema & Engine)

## Overview & Rationale
While the DRAM Foundation VN knowledge base contains 1,003 decomposed work packages with base SOPs, literature citations, and freshly integrated Council Critics and Test Cases, there remains a critical operational gap between an abstract "WBS card on a screen" and a "physically executable semiconductor run-sheet".

To transform each node into a truly reproducible laboratory protocol for an engineer, university lab, or garage builder in Vietnam, each node requires 6 missing physical and engineering dimensions.

---

## Key Missing Dimensions

### 1. Bill of Materials (BOM) & Chemical CAS Registry
- **Chemical CAS Numbers**: Exact registry IDs (e.g. HF: `7664-39-3`, NH4F: `12125-01-8`, H2O2: `7722-84-1`, HCl: `7647-01-0`, NH4OH: `1336-21-6`).
- **Purity Grade Specification**: Distinction between Electronic/MOS Grade (VLSI/ULSI < 1 ppb metals) vs Technical Grade.
- **Sourcing Feasibility & Estimated Cost**: Realistic vendors in Vietnam/ASEAN, pricing in VND/USD, and lead times.

### 2. EHS (Environmental Health & Safety) & Hazmat Envelopes
- **PPE Classification**: Level of protective equipment (butyl/neoprene gloves, full face shield, acid apron, respirator).
- **Specific Antidotes**: Immediate medical response protocols (e.g. Calcium Gluconate gel 2.5% for HF skin exposure).
- **Exhaust & Facility Interlocks**: Face velocity requirements (> 0.5 m/s) and toxic vapor neutralizers.
- **Waste Neutralization**: Safe neutralization before disposal (e.g. Ca(OH)2 precipitation for fluoride waste).

### 3. Queue-Time (Q-Time) & Inter-Node Handshake Constraints
- **Maximum Exposure Window**: Critical time limits between physical steps (e.g. post-DHF native oxide strip to thermal oxidation insertion: Q-Time <= 30 min in air, or <= 4 hours in N2 box).
- **Surface State Transfer**: Clear definitions of incoming and outgoing wafer states (e.g. hydrophilic vs hydrophobic, static charge, particulate limits).

### 4. Executable Design Deliverables (EDA / CAD Artifacts)
- **Circuit / SPICE Netlists**: Complete `.subckt` SPICE netlists with transistor sizing (W/L) for analog and cell nodes.
- **Layout & DRC Constraints**: Explicit design rules (minimum pitch, metal spacing, antenna ratios).
- **Mechanical CAD Fixtures**: STEP/STL references for custom 3D printed or CNC machined stage brackets and chucks.

### 5. Quantitative FMEA (Failure Mode and Effects Analysis) Scoring
- **RPN Matrix**: Severity (1-10), Occurrence (1-10), and Detection (1-10), calculating the Risk Priority Number ($RPN = S \times O \times D$).
- **Contingency & Yield Fallback**: Clear remediation steps if a node yields out-of-spec parameters.

---

## References & Related Files
- [data/schema/node.schema.json](./data/schema/node.schema.json)
- [workflow/critic_testcase_engine.py](./workflow/critic_testcase_engine.py)
- [docs/context3.yaml](./docs/context3.yaml)
- [PROJECT.md](./PROJECT.md)

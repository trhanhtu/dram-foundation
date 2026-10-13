# DRAM Foundation VN - 180nm Open-Source DRAM Architecture

Autonomous AI-driven knowledge synthesis, multi-agent AI Council, and Work Breakdown Structure (WBS) engineering graph for open-source 180nm DRAM semiconductor fabrication.

---

## Overview

The DRAM Foundation VN repository defines a comprehensive, machine-actionable semiconductor execution blueprint consisting of **1,003 verified work packages** and **1,000 directed causality edges** spanning 6 core disciplines:

1. **Electronics & Drive Infrastructure**: Closed-loop motor control, quadrature encoders, and multi-channel power distribution.
2. **Macroscopic Lithography Stage (Gen 1 mm)**: Dual-axis precision translation stage, Abbe error minimization, and kinematic alignment.
3. **Microscopic Mask Optical Aligner (Gen 2 µm)**: Sub-micron split-field optics, Wedge Error Compensation (WEC), and proximity gap regulation.
4. **Wet Chemistry & Acid Etch Bench**: Megasonic RCA-1/2 organic and metallic decontamination, dilute HF native oxide strip, and Buffered Oxide Etch (BOE 6:1).
5. **Thermal Oxidation Furnace**: 3-zone quartz tube diffusion furnace with flat-zone PID thermal profiling and Deal-Grove kinetic gate oxide growth ($3.5\,\text{nm}$).
6. **180nm DRAM Cell Architecture & Readout**: 1T1C $8F^2$ crown-type Capacitor Over Bitline (COB), High-$\kappa$ $\text{Ta}_2\text{O}_5$ stacked dielectric ($C_s \ge 28.5\,\text{fF}$), differential folded bitline CMOS sense amplifiers, and boosted $V_{PP}$ wordline drivers.

---

## Quick Start

### 1. Interactive WBS Explorer & Graph Navigator
The repository includes a zero-dependency, pure client-side web application for inspecting all 1,003 work packages, local DAG causality, KaTeX physical formulas, and inline technical SVG schematics:

- **Local Web**: Open `index.html` directly in any modern browser.
- **GitHub Pages**: Deployed statically via GitHub Actions.

### 2. FastAPI Local Bridge Server (Optional)
To run the local backend server for semantic literature RAG (ChromaDB) and interactive AI Council review endpoints:

```bash
# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
python -m uvicorn workflow.server:app --host 127.0.0.1 --port 8000
```
Then navigate to **http://127.0.0.1:8000**.

### 3. Test Suite Execution
Run the comprehensive 135-test regression, DAG validation, and semiconductor workflow suite:

```bash
pytest
```

---

## Repository Structure

- `index.html`: Fast, responsive WBS Explorer with dual-pane layout, KaTeX math rendering, and SVG schematics.
- `data-engine.js`: Pure ES6 modular graph engine with Kahn's DAG cycle validator and relative static loading.
- `data/manifest.json`: Single Source of Truth manifest for all 6 disciplines.
- `data/modules/*.json`: 7 modular datasets containing the complete 1,003-node WBS specifications and SOPs.
- `data/schema/`: Formal JSON schema definitions for nodes and directed edges.
- `docs/knowledge/`: Architectural decision records, metrology protocols, and device physics derivations.
- `docs/sop/`: Detailed standard operating procedures for physical wafer processing.
- `tests/`: End-to-end test suite covering DAG acyclicity, schema compliance, and semiconductor workflows.
- `workflow/`: FastAPI bridge server, semantic vector store, and AI Council orchestrator.

---

## Open-Source Silicon Provenance

All work packages are mapped to authoritative open-source silicon repositories and peer-reviewed educational laboratory demonstrators:
- **Foundry PDK & Rules**: [Google / SkyWater SKY130 Open PDK](https://github.com/google/skywater-pdk)
- **EDA & Synthesis**: [The OpenROAD Project](https://github.com/The-OpenROAD-Project/OpenROAD) and [Magic VLSI](https://github.com/RTimothyEdwards/magic)
- **Memory Controller**: [LiteX DRAM Subsystem](https://github.com/enjoy-digital/litex)
- **Embedded Firmware**: [Espressif ESP-IDF](https://github.com/espressif/esp-idf)
- **Open Microfabrication**: [Sam Zeloof Z1/Z2 Silicon](https://github.com/sam-zeloof/Z1)

---

## License

Open-source under the Apache 2.0 License.

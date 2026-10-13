# Leaf Node Actionability Audit and the Generational Jump Gap

- **Date**: 2026-10-13
- **Source**: User & Agent Physical Audit
- **Status**: Identified & Architecture Formulated

## 1. Actionability Audit of the 1,003 Work Packages
A deep database audit of `data/dram_graph.db` across all 1,003 nodes revealed:
- **Genuinely Actionable Core (~30% / 317 nodes)**: Highly detailed physical specifications grounded in established literature (Deal-Grove 1000°C oxidation kinetics, Kern RCA SC-1/SC-2 ratios, 6:1 BOE etch rates, Shipley 1813 spin curves, Dickson charge pumps).
- **Generic Metric Stubs (68.5% / 687 nodes)**: Hardcoded fallback dictionary in `domain_expert.py` defaulted to `"Inspection Standard": "Caliper / Optical Micrometer"`, even for chemical etching, sputtering, and electrical simulation.
- **Placeholder Fallback SOPs (5.4% / 54 nodes)**: Repetitive Vietnamese boilerplate text (*"Chuẩn bị vật tư... Thực hiện gá đặt..."*).

## 2. The "Quantum Leap" Trap (Generational Jump Gap)
- **Current Database Distribution**:
  - Gen 1 (mm): 29 nodes
  - Gen 2 (µm): 974 nodes
  - Gen 3 (nm): 0 nodes
- **The Physical Problem**: The crawler jumped from macroscopic mechanical stage parts directly into claiming 180nm DRAM fabrication without intermediate physical stepping stones.
- **Why $1\text{ mm} \rightarrow \text{nm}$ cannot be leaped**:
  - Lead screws and stepper motors have $\pm 10-20\text{ }\mu\text{m}$ backlash, incapable of sub-micron overlay.
  - Optical microscopy cannot resolve $< 250\text{ nm}$ (diffraction limit).
  - Normal room environments ($100,000$ particles/$\text{ft}^3$) immediately destroy $3.5\text{ nm}$ gate oxide.

## 3. The 3-Stage Generational Reality Ladder
To make the project physically actionable and prevent generic AI bluff:
1. **Gen 1 (mm $\rightarrow$ $50\text{ }\mu\text{m}$)**: Macroscopic mechanics, bulk quartz tube, 4-point probe. Proof: Planar Diode & $100\text{ }\mu\text{m}$ MOS capacitor.
2. **Gen 2 ($50\text{ }\mu\text{m} \rightarrow 2\text{ }\mu\text{m}$)**: Flexure stages, 365nm contact mask aligner, Shipley 1813 resist, BOE patterning. Proof: Discrete NMOS transistor, CD4007 inverter, ring oscillator.
3. **Gen 3 ($2\text{ }\mu\text{m} \rightarrow 180\text{ nm}$)**: Piezoelectric nano-positioners, laser interferometry, ALD thin films, Class 100 mini-environment. Proof: 16x16 1T1C DRAM array & folded bitline sense amplifiers.

## 4. Multi-Agent Research Squad Architecture
Deploy specialized subagents to crawl authoritative technical literature into ChromaDB:
- **Agent A**: Wet Chemistry & RCA / Etch Standards.
- **Agent B**: Thermal Oxidation Kinetics & Gas Manifolds.
- **Agent C**: Photolithography Exposure & Overlay Metrology.
- **Agent D**: DRAM Circuit Netlists, SPICE Timing & 1T1C Physics.

## References
- [data/dram_graph.db](../../data/dram_graph.db)
- [workflow/council/domain_expert.py](../../workflow/council/domain_expert.py)
- [docs/context2.yaml](../context2.yaml)

# MOSCAP Diagnostic Test Structure Micro-Probing & Backside Contact Preparation

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for sample preparation and electrical micro-probing of planar MOS capacitor (MOSCAP) diagnostic test structures fabricated on P-type (100) silicon substrates. This metrology step evaluates gate dielectric integrity, physical and equivalent oxide thickness ($t_{ox}$), flatband voltage ($V_{fb}$), and interface trap density ($D_{it}$) via High-Frequency (1 MHz) and Quasi-Static C-V characterization following post-HTOL dynamic thermal-voltage stress screening.

## Key Details / Architecture
- **Backside Ohmic Contact**: HF 5% native oxide etch followed by gold (Au) or aluminum (Al) ohmic metallization.
- **Top Gate Contacts**: Sputtered aluminum circular gate dots with nominal diameters of 200 µm, 500 µm, and 1000 µm.
- **Target Dielectric Range**: Thermally grown gate oxide between 3.5 nm and 25 nm.
- **C-V Profiling Modes**:
  1. *Accumulation ($V_G < V_{fb}$)*: Saturation at $C_{ox} = (\varepsilon_{ox} \cdot \varepsilon_0 \cdot \text{Area}) / t_{ox}$ yielding $t_{ox}$ within $\pm 0.1\text{ nm}$.
  2. *Depletion ($V_{fb} < V_G < V_T$)*: Capacitance reduction due to silicon space-charge depletion layer.
  3. *Inversion ($V_G > V_T$)*: High-frequency (1 MHz) capacitance remains at minimum, whereas quasi-static low-frequency capacitance recovers to $C_{ox}$.

## References & Related Files
- [Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction](./docs/context.yaml)
- [180nm DRAM Cell Layout Topology](./docs/context2.yaml)

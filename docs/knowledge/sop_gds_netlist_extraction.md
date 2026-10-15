# Hierarchical GDS Layout Netlist Extraction & Device Recognition Execution

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Accepted

## Overview & Rationale
Standard Operating Procedure (SOP) for hierarchical GDSII netlist extraction and device recognition tailored to the 180nm open-source 1T1C folded bitline DRAM chip. Ensures accurate identification of sub-micron access NMOS transistors, stacked crown/MIM capacitors, shared bitline contacts, and interconnect parasitics for LVS sign-off.

## Key Details / Architecture
- **Process Generation**: 180nm Open-Source DRAM (Gen 3 nm)
- **Cell Topology**: Folded Bitline $8F^2$ ($0.259\,\mu\text{m}^2$) Stacked Capacitor-over-Bitline (COB)
- **Extracted Elements**:
  - Access NMOS: $L = 180\,\text{nm}$, $W = 220\,\text{nm}$, gate oxide thickness $T_{\text{ox}} \approx 3.5\,\text{nm}$
  - Storage Capacitor ($C_s$): Crown/Cylinder stacked capacitor, $C_s \ge 25\text{--}30\,\text{fF}$ (nominal $28\,\text{fF}$)
  - Dielectric Stack: ONO or $\text{Ta}_2\text{O}_5$/$\text{Al}_2\text{O}_3$ ($\kappa > 15$, $\text{EOT} \approx 3\text{--}4\,\text{nm}$)
  - Array Capacitance Budget: $C_b = 150\text{--}250\,\text{fF}$, $C_b/C_s$ ratio $5:1$ to $9:1$
  - Retention & Leakage: Sub-threshold/junction leakage $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$ to ensure retention $> 64\,\text{ms}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

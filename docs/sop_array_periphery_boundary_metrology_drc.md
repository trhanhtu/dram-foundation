# Full-Chip Array-to-Periphery Boundary Metrology & DRC Sign-off Run

- **Date**: 2026-10-13
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure (SOP) for boundary metrology verification and full-chip design rule checking (DRC) sign-off between the dense periodic 8F² DRAM cell array and the loose logic/analog periphery circuits in a 180nm open-source DRAM architecture.

## Key Details / Architecture
- **Technology Node**: 180nm (Feature size $F = 180\text{ nm}$).
- **Cell Topology**: 8F² folded bitline unit cell ($0.259\ \mu\text{m}^2$).
- **Key Boundary Metrics**:
  - Unit cell gate dimensions: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
  - Array pitch: Bitline and wordline pitch $360\text{ nm}$ to $400\text{ nm}$.
  - Storage node capacitance budget: $C_s \ge 25\text{ fF}$ to $30\text{ fF}$ (nominal $28\text{ fF}$).
  - Refresh leakage ceiling: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ ($> 64\text{ ms}$ retention).
  - Bitline capacitance limit: $C_b = 150\text{ fF}$ to $250\text{ fF}$ ($C_b / C_s$ ratio between $5:1$ and $9:1$, strictly $< 10:1$).
- **Gate Dielectric**: Dry $\text{SiO}_2$ physical thickness $\sim 3.5\text{ nm}$ ($850^\circ\text{C}$–$900^\circ\text{C}$).
- **Capacitor Dielectric**: ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-k stack with $\text{EOT} = 3\text{ nm}$ to $4\text{ nm}$ ($\kappa > 15$).

## References & Related Files
- [docs/context.yaml](./context.yaml)
- [docs/context2.yaml](./context2.yaml)

# Automated AFM/Profilometer Polar-to-Cartesian Polar Coordinate Recipe Setup for Multi-Point Radial Wafer Scanning

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Accepted

## Overview & Rationale
In 180nm DRAM fabrication (COB topology with stacked capacitors over bitline contacts), Chemical Mechanical Planarization (CMP) of Inter-Layer Dielectrics (ILD) and Tungsten (W) plugs requires precise cross-wafer profiling. Radial film non-uniformity across polishing and deposition tools is intrinsically symmetric around the wafer center, necessitating automated conversion of polar coordinates $(r_i, \theta_j)$ into Cartesian stage coordinates $(X, Y)$ to drive automated AFM/profilometer stages across 9-point or 49-point wafer inspection grids.

## Key Details / Architecture
- **Polar-to-Cartesian Transformation**:
  $$X_k = r_i \cos(\theta_j) + X_{\text{offset}}, \quad Y_k = r_i \sin(\theta_j) + Y_{\text{offset}}$$
- **Inspection Grids**: Standardized 9-point and 49-point sampling schemes.
- **Physical Integration Targets**:
  - Transistor gate dimensions: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
  - Storage node requirements: $C_{\text{cell}} \ge 28\text{ fF/cell}$, $I_{\text{leak}} \le 1\text{ fA/cell}$ at $85^\circ\text{C}$.
  - Metrology precision: Gate oxide thickness baseline ($3.5\text{ nm}$) tracked within $\pm0.05\text{ nm}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

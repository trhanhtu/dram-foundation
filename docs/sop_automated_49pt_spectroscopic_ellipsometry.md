# Automated 49-Point Spectroscopic Ellipsometry Multi-Site Dielectric Thickness Acquisition

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for automated 49-point spectroscopic ellipsometry wafer mapping post-CMP in a 180nm DRAM fabrication process. The protocol tracks within-wafer non-uniformity (WIWNU), dishing, and dielectric erosion across inter-layer dielectric (ILD) oxide films and stacked cell capacitor layers.

## Key Details / Architecture
- **Metrology Node**: 180nm Open-Source DRAM (DRAM Foundation VN), Gen 3 (nm).
- **Physical Modeling**: Spectroscopic parameterization using Cauchy and Sellmeier dispersion relations for complex reflection ratio $\rho = r_p / r_s = \tan(\Psi) \cdot \exp(i \cdot \Delta)$.
- **Map Grid**: Polar/Cartesian 49-point pattern covering center, concentric annular rings, and edge-exclusion zones.
- **Precision Requirement**: Sub-angstrom repeatability ($\pm 0.05\text{ nm}$) on thin reference dielectrics and $\pm 2.0\text{ nm}$ across thick film / resist layers.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- [docs/context3.yaml](../context3.yaml)

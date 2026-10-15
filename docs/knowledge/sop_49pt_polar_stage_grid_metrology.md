# 49-Point Polar Coordinate Polarized Stage Grid & Focus Pattern Generation

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the standard 49-point polar coordinate stage sampling and autofocus pattern for post-CMP Inter-Layer Dielectric (ILD) oxide film metrology on 200mm wafers for the 180nm Open-Source DRAM project. Automated polar mapping tracks radial non-uniformity and edge roll-off across spin coating, furnace, and CMP operations using multi-angle spectroscopic ellipsometry.

## Key Details / Architecture
- **Stage Topology**: 5 concentric rings (R0: Center r=0 mm, R1: r=32 mm, R2: r=58 mm, R3: r=78 mm, R4: r=95 mm) with 5 mm edge exclusion on 200mm wafer. Point breakdown: 1 + 6 + 12 + 14 + 16 = 49 points.
- **Physical Optical Measurement**: Dual-quadrant laser triangulation autofocus (Z-repeatability <= 0.05 um), spectroscopic ellipsometry measuring angles $\Psi$ and $\Delta$ across $240 \text{ nm} - 800 \text{ nm}$.
- **Dispersion Modeling**: Cauchy / Sellmeier dispersion models $n(\lambda), k(\lambda)$ for ILD oxide and photoresist / gate oxide baseline validation.
- **Acceptance Thresholds**: Sub-Angstrom precision (<= 0.05 nm for thin gate oxide baselines), <= 2.0 nm precision for thick dielectric/resist, Goodness-of-Fit $R^2 \ge 0.992$, stage indexing settling time <= 320 ms.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

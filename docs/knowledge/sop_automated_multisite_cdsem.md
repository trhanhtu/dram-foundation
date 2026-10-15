# Automated Multi-Site Wafer Navigation & Critical Dimension Recipe Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure (SOP) for setting up and executing automated multi-site wafer navigation and Critical Dimension Scanning Electron Microscopy (CD-SEM) metrology on 180nm open-source DRAM wafers under the DRAM Foundation VN architecture (SkyWater SKY130 compatibility).

## Key Details / Architecture
- **Tooling & Metrology Platform**: In-line CD-SEM with multi-die automated laser stage interferometer and pattern recognition.
- **Physical Grid Resolution**: 0.005 µm (5 nm) manufacturing placement grid.
- **Target Metrics**:
  - DRAM access transistor gate critical dimension: $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
  - SkyWater SKY130 min poly gate length: $150\text{ nm}$, poly spacing $\ge 210\text{ nm}$.
  - Active diffusion width: $\ge 150\text{ nm}$.
  - Contact hole dimension: $170\text{ nm} \times 170\text{ nm}$.
  - Poly-to-active gate overlay tolerance: $\le 35\text{ nm}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

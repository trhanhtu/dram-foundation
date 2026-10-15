# Process Window Matrix Definition & DUV Illumination Condition Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operational flow, optical parameter qualification, and Focus-Exposure Matrix (FEM) lithography evaluation for 180nm commercial MPW tapeout / open-source DRAM peripheral integration based on 248nm KrF DUV illumination.

## Key Details / Architecture
- **Exposure Source**: 248 nm KrF excimer laser.
- **Numerical Aperture (NA)**: 0.65 with process resolution factor $k_1 = 0.40$ yielding $R = 152\text{ nm}$ resolvable half-pitch ($R = k_1 \frac{\lambda}{\text{NA}}$).
- **Physical Placement Grid**: 0.005 $\mu\text{m}$ (5 nm).
- **DOF Margin**: $k_2 \frac{\lambda}{\text{NA}^2} \ge 0.5\ \mu\text{m}$.
- **Metrology**: Spectroscopic ellipsometry for photoresist ($1.3\ \mu\text{m} \pm 2\text{ nm}$) mapping and CD-SEM measurement.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

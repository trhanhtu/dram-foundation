# AFM Calibration and High-Aspect-Ratio Tip Selection for W-Plug Metrology

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for Atomic Force Microscopy (AFM) calibration and High-Aspect-Ratio (HAR) probe selection to quantify Tungsten (W) plug recess, oxide erosion, and dishing profile on 180nm DRAM access transistor drains (channel length L = 180 nm, access width W = 220 nm, bitline/wordline pitch = 360 nm to 400 nm).

## Key Details / Architecture
- Tip geometry: High-Aspect-Ratio silicon/diamond-like carbon cantilever with aspect ratio >= 10:1, tip apex radius <= 10 nm, cone half-angle <= 3°.
- Calibration standard: Standard 100 nm 1D/2D pitch grid and certified step-height standard (20.0 nm ± 0.3 nm).
- Metrology targets: W-plug recess < 35.0 nm, AFM Z-step calibration error <= 0.3 nm, lateral XY calibration linearity <= 0.5%.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

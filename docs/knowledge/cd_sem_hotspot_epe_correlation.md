# Pitch-Calibrated CD-SEM Hotspot Auditing and Model EPE Correlation Analysis

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure for wafer/reticle CD-SEM auditing across post-OPC lithography hotspots in the 180nm DRAM tapeout (SkyWater SKY130 compatible baseline). Focuses on pitch-based tool magnification calibration, edge placement error (EPE) extraction against drawn GDSII contours, and statistical correlation against optical proximity correction (OPC) simulation predictions.

## Key Details / Architecture
- Calibration standard: 1D grating target with known pitch on a 5 nm manufacturing placement grid.
- Critical dimensions audited: Gate poly length (150 nm min / 180 nm access transistor), poly spacing (210 nm min), active diffusion width (150 nm min / 220 nm cell width), contact hole (170 nm x 170 nm), Metal 1 pitch (340 nm min).
- Maximum gate poly to active diffusion overlay tolerance: <= 35 nm.
- Minimum model-to-silicon correlation threshold: $R^2 \ge 0.95$.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)

# Knowledge Note: Contact Profilometer Oxide Step-Height Verification & Calibration Protocol

- **Date**: 2026-10-13
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
For the 180nm DRAM process node (Gen 1 baseline validation), post-etch oxide pattern verification requires strict cross-calibration of stylus profilometry against certified step-height standards. Measuring thermally grown SiO2 (etch rate 80–100 nm/min in BOE 6:1 at 25°C) and CVD/TEOS SiO2 (150–220 nm/min) ensures exact gate, capacitor contact, and trench depth control before dielectric deposition.

## Key Physical Standards & Parameters
- **Stylus Tip Radius**: 2.0 µm diamond stylus, low contact force (0.05 mN to 0.10 mN / 5 to 10 mgf) to prevent scratching oxide or resist margins.
- **Scan Parameters**: 500 µm scan length, 10 µm/s scan speed, 200 Hz sample rate (0.05 µm spatial sampling resolution).
- **Calibration Standard**: 100.0 nm (± 1.0 nm / 1000 Å) certified step-height standard with instrument linearity tolerance ≤ 1.0%.
- **Chemical Etch Baseline (BOE 6:1 at 25°C)**:
  - Thermal SiO2 target etch rate: 80 to 100 nm/min (800 to 1000 Å/min).
  - CVD/TEOS SiO2 target etch rate: 150 to 220 nm/min.
  - Selectivity: SiO2:Si > 100:1; SiO2:Si3N4 > 20:1.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

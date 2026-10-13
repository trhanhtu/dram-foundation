# Transient Contact Angle Video Profiling & Surface Hydrophobicity Uniformity Analysis

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented
- **Module**: Metrology / Pre-Oxidation Surface Preparation / 180nm DRAM Gate Dielectric

## Overview & Rationale
Prior to growing the ultra-thin 3.5 nm dry gate oxide (grown at 850°C–900°C) for access transistors (L = 180 nm, W = 220 nm), the silicon surface undergoes pre-oxidation RCA clean followed by an in-situ dilute HF / BOE strip. Effective HF termination leaves a hydrophobic, hydrogen-passivated (Si-H) surface. Incomplete oxide stripping or native oxide regrowth yields hydrophilic patches, degrading gate oxide uniformity, breakdown voltage, and retention. Transient high-speed video contact angle profiling quantifies dynamic wetting, droplet relaxation, and across-wafer hydrophobicity uniformity.

## Process Flow & Operational Criteria
1. **Chamber Setup & Environmental Equilibrium**: 23°C ± 0.5°C, 45% ± 3% RH, Class 1 mini-environment with N2 micro-purge.
2. **Automated Multi-Site Dispense**: High-precision micro-syringe dispensing 2.0 µL ± 0.1 µL UPW (Ultra-Pure Water, 18.2 MΩ·cm) across 5 sites (Center, Top, Right, Bottom, Left with 5 mm edge exclusion).
3. **High-Speed Video Acquisition**: Capture video at >= 60 fps for 10 s from droplet touch-down.
4. **Transient Dynamic Angle & Uniformity Analysis**: Fit droplet profile using Young-Laplace / tangent method to compute static contact angle $\theta_0$ at $t = 1.0\text{ s}$ and relaxation rate $\frac{d\theta}{dt}$.

## Acceptance Criteria
- HF-Last Passivated Contact Angle: $\theta \ge 75^\circ$ across all 5 test sites.
- Within-Wafer Contact Angle Uniformity ($3\sigma$): $\le 3.0\%$.
- Transient Drop Relaxation Rate ($t = 1\text{ s}$ to $5\text{ s}$): $|\Delta\theta| \le 1.5^\circ$.
- Pre-Oxidation Gate Oxide Target: Clean substrate released for 3.5 nm dry gate oxide growth at 850°C–900°C.

## References & Related Files
- [180nm DRAM Architecture & Cell Capacitor Engineering](../context.yaml)
- [Silicon Dioxide Etching with Buffered Oxide Etch (BOE)](../context.yaml)

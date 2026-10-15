# Spectroscopic Ellipsometer Hardware Alignment and Multi-Angle Goniometer Calibration

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Actionable standard operating procedure (SOP) for optical hardware alignment, source intensity balancing, and multi-angle goniometer calibration of a spectroscopic ellipsometer before performing post-CMP inter-layer dielectric (ILD) oxide characterization and Cauchy dispersion modeling in 180nm DRAM fabrication.

## Key Details / Architecture
- **Fundamental Principle**: Measures amplitude ratio $\Psi$ and phase change $\Delta$ governed by:
  $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
- **Hardware Calibration Chain**:
  1. Straight-through transmission ($0^\circ$ direct beam) baseline and detector quadrant balancing.
  2. Z-height autofocus and tilt (pitch/roll tip-tilt) alignment to position reflected beam within quadrant detector centers.
  3. Multi-angle goniometer sweep ($65^\circ, 70^\circ, 75^\circ$) on reference standard wafer.
  4. Accuracy verification across dry oxide calibration wafer standard ($\pm 0.05\text{ nm}$ sub-Angstrom precision limit).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/sop/sop_ellipsometer_alignment_calibration.md](./docs/sop/sop_ellipsometer_alignment_calibration.md)

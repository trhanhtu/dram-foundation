# Spectroscopic Ellipsometry Optical Dispersion Model Calibration & Standard Baseline Verification

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Accepted

## Overview & Rationale
Establishes the standard calibration and baseline verification procedure for spectroscopic ellipsometry optical dispersion models within the 180nm Open-Source DRAM node. Accurate parameterization of optical constants ($n(\lambda)$, $k(\lambda)$) via Cauchy or Sellmeier formulations is essential for non-destructive multi-point thickness and planarity tracking post-ILD oxide chemical mechanical planarization (CMP).

## Key Details / Architecture
- **Fundamental Measurement**: Measures the polarization state change upon reflection:
  $$\rho = \frac{r_p}{r_s} = \tan(\Psi) e^{i\Delta}$$
  where $r_p$ and $r_s$ are the complex Fresnel reflection coefficients, $\Psi$ is the amplitude ratio, and $\Delta$ is the phase difference.
- **Model Parameterization**:
  - Uses Cauchy or Sellmeier optical dispersion formulations to model dielectric response across the spectrum.
- **Calibration & Verification Routine**:
  1. Calibrate on standard reference wafer (bare silicon and certified dry thermal oxide).
  2. Baseline accuracy verified against dry gate oxide target ($3.5\text{ nm}$) with sub-Angstrom precision ($\pm 0.05\text{ nm}$) and thick films/photoresist ($1.3\ \mu\text{m}$) within $\pm 2\text{ nm}$.
  3. Deploy 9-point or 49-point automated polar/radial wafer mapping routines for ILD oxide polish qualification.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

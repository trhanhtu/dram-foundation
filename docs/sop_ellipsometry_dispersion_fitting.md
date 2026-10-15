# SOP: Dispersion Model Fitting & 3.5nm Oxide Thickness Radial Uniformity Extraction

- **Date**: 2026-10-12
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure for spectroscopic ellipsometry model fitting and radial thickness mapping of thermally grown dry gate oxide (target 3.5 nm) on 180nm DRAM access transistor gates.

## Key Details / Architecture
- **Metrology Node**: 180nm Open-Source DRAM (Gate length $L = 180\text{ nm}$, thermal dry $\text{SiO}_2$ grown at $850^\circ\text{C}\text{--}900^\circ\text{C}$).
- **Optical Principle**: $\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$.
- **Dispersion Models**: Cauchy and Sellmeier formulations for dielectric parameterization ($n(\lambda)$, $k(\lambda)$).
- **Wafer Mapping**: Automated 49-point / 9-point radial tracking.
- **Precision Target**: Sub-angstrom measurement precision ($\pm 0.05\text{ nm}$).

## References & Related Files
- [context.yaml](../context.yaml)
- Verified Literature: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
- Verified Literature: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*

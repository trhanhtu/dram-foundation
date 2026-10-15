# SOP: Dose-Array Matrix Automated 49-Point Film Thickness Mapping

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 3 (nm) / 180nm Open-Source DRAM Node

## Overview & Rationale
Automated non-destructive optical metrology SOP for spectroscopic ellipsometry mapping across a dose-array matrix test wafer. Tracks radial film non-uniformity and post-exposure resist contrast profiles for 180nm gate critical dimensions (L = 180 nm, W = 220 nm) and gate dielectric interfaces.

## Key Details / Metrology Metrics
- **Polarization Measurement**: Ratio of complex Fresnel reflection coefficients $\rho = r_p / r_s = \tan(\Psi) \cdot e^{i\Delta}$.
- **Dispersion Models**: Cauchy or Sellmeier models parameterizing refractive index $n(\lambda)$ and extinction coefficient $k(\lambda)$.
- **Measurement Targets**:
  - Dry gate oxide physical thickness: 3.5 nm with sub-Angstrom precision (±0.05 nm).
  - Photoresist nominal thickness: 1.3 µm with metrology precision within ±2 nm.
  - Wafer mapping grid: Automated 49-point matrix tracking spin-coating and exposure uniformity.

## References & Related Files
- [Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology](file:///docs/knowledge/dose_array_49pt_ellipsometry_sop.md)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](file:///docs/context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](file:///docs/context2.yaml)

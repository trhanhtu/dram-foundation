# Micro-Knowledge: Spectroscopic Ellipsometry & X-Ray Reflectivity Metrology for 180nm DRAM BEOL Metallization

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Metrology protocol for post-deposition characterization of DC magnetron sputtered Al-0.5%Cu thin films (Metal-1/Metal-2) in 180nm DRAM fabrication. Uses spectroscopic ellipsometry (optical Fresnel reflection polarization angles $\Psi, \Delta$) and X-Ray Reflectivity (XRR specular interference fringes) to measure physical film thickness, native oxide passivation, and across-wafer thickness non-uniformity without destructive cross-sectioning.

## Key Details / Architecture
- **Target Substrate**: Al-0.5%Cu Metal-1 layer deposited over ILD/interconnect topography.
- **Physical Thickness Target**: Metal-1 thickness target is $350\text{ nm} \pm 5\%$ ($332.5\text{ nm}$ to $367.5\text{ nm}$).
- **Metrology Modalities**:
  - Spectroscopic Ellipsometry: Measures $\rho = r_p / r_s = \tan(\Psi) \exp(i\Delta)$ using parameterized Drude-Lorentz or Cauchy/Sellmeier models.
  - XRR Profile: Grazing incidence X-ray reflection to resolve Kiessig oscillation fringes for high-resolution metal layer thickness and interface density.
- **Sampling Strategy**: Automated 9-point or 49-point wafer mapping to track radial deposition profile across 200mm wafers.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- Sourced from: *Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects* and *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*.

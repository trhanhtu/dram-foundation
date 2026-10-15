# Spectroscopic Ellipsometry 49-Point Dielectric Thickness Mapping Across Post-CMP Wafers

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Accepted

## Overview & Rationale
Standard Operating Procedure (SOP) for non-destructive automated 49-point wafer mapping of post-CMP Inter-Layer Dielectric (ILD) thin films in the 180nm Open-Source DRAM platform (DRAM Foundation VN). The protocol monitors post-polish film thickness, cross-wafer non-uniformity (WIWNU), and CMP edge/center profile variation using optical polarization changes parameterized by Cauchy and Sellmeier dispersion models.

## Key Details / Architecture
- **Governing Physics**: Fresnel reflection ratio $\rho = r_p / r_s = \tan(\Psi) \cdot e^{i\Delta}$.
- **Dispersion Models**: Cauchy ($n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4}$) and Sellmeier formulations for transparent and high-$\kappa$ dielectric stacks ($\mathrm{SiO_2}$, $\mathrm{Si_3N_4}$, $\mathrm{Ta_2O_5}$, ONO).
- **Sampling Topology**: 49-point polar/radial layout across wafer radius $R$ capturing center, mid-radius, and edge-exclusion zones.
- **Precision Target**: Sub-angstrom precision ($\pm 0.05\text{ nm}$) on standard calibration dielectric films (~$3.5\text{ nm}$ gate oxide equivalent).

## References & Related Files
- [Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology](./docs/knowledge/sop_post_cmp_ellipsometry_49pt.md)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context.yaml)

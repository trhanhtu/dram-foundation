# Spectroscopic Ellipsometry 49-Point Recipe Calibration & Dispersion Modeling

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented

## Overview & Rationale
Automated optical thin film metrology is indispensable for post-Buffered Oxide Etch (BOE 6:1) verification across 180nm DRAM fabrication runs. Standardizing a 49-point wafer mapping protocol paired with Cauchy dispersion modeling enables sub-Angstrom precision monitoring of residual oxide thicknesses, dry thermal gate oxide targets (~3.5 nm), and etching non-uniformities without destructive cross-sectioning.

## Key Details / Architecture
- **Polarization Measurement**: Quantifies Fresnel reflection ratio $\rho = r_p / r_s = \tan(\Psi) \cdot \exp(i\Delta)$.
- **Dispersion Formulation**: Transparent dielectric modeling using Cauchy parameterization $n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}$, with $k(\lambda) \approx 0$ across UV-visible spectra.
- **Mapping Topology**: Polar 49-point concentric radial distribution tracking wafer center, mid-radius, and edge-die non-uniformity across spin coating and furnace runs.
- **Calibration Routine**: Bare silicon reference calibration ($n_{Si}$, $k_{Si}$) prior to fitting residual $\text{SiO}_2$ dielectric targets.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- Context Literature: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
- Context Literature: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- Context Literature: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*

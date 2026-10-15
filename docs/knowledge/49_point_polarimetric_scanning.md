# Micro-Knowledge: 49-Point Polarimetric Scanning Script & Stage Motion Trajectory Implementation

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented

## Overview & Rationale
Automated wafer-level polarimetric ellipsometry scanning routine for 180nm CMOS/DRAM post-CMP Inter-Layer Dielectric (ILD) oxide films. Establishes a serpentine stage trajectory across 49 coordinate sites with dual-angle polarimetric acquisition $(\Psi, \Delta)$, minimizing stage acceleration overhead, avoiding edge exclusion zones, and enforcing Cauchy dispersion model inversions for nanometer-precision non-uniformity mapping.

## Key Details / Architecture
- **Stage Motion Trajectory**: 49-site concentric/serpentine layout over 200 mm substrate with a 5 mm edge exclusion zone (effective metrology radius: 95 mm).
- **Physical Optical Measurement**: Spectroscopic polarimetry measuring complex reflectance ratio:
  $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot e^{i\Delta}$$
- **Dielectric Model**: Cauchy dispersion model parameterization for ILD SiO2:
  $$n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}, \quad k(\lambda) = 0$$
- **Throughput & Quality Safeguards**: Settling time damping ($\le 200\text{ ms}$), autofocus Z-tracking ($\le 1.0\ \mu\text{m}$), and goodness-of-fit $\chi^2$ filtering.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- Context source: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
- Context source: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*

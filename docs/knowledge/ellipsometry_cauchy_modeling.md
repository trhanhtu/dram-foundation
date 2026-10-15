# Spectroscopic Ellipsometry Cauchy Optical Model Parameterization for Resist Thin Films (HSQ and ZEP520A)

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented

## Overview & Rationale
Establishes the non-destructive spectroscopic ellipsometry calibration, Cauchy dispersion modeling, and wafer-mapping protocols for electron-beam and high-resolution photoresist films (such as HSQ, ZEP520A, and novolak standards) on silicon substrates.

## Key Details / Architecture
- **Polarization Measurement**: Quantifies Fresnel reflection ratio $\rho = r_p / r_s = \tan(\Psi) \exp(i\Delta)$ across spectroscopic wavelengths.
- **Cauchy Dispersion Formulation**: Models transparent resist layers where $n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4}$ and extinction coefficient $k(\lambda) \approx 0$ in the transparent visible/NIR spectrum.
- **Radial Non-Uniformity Tracking**: Standardizes 9-point and 49-point wafer mapping to decouple spin-coating fluid dynamics from edge-bead or bake anomalies.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

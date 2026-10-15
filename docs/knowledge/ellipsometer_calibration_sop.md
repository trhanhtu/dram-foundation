# Spectroscopic Ellipsometer Calibration & Polarimetric Hardware Alignment

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Establishes standard operating procedures for calibrating spectroscopic ellipsometers and aligning polarimetric optics prior to automated 49-point full-wafer thin film metrology (e.g. ILD oxide post-CMP or thin dielectric characterization in 180nm DRAM fabrication).

## Key Details / Architecture
- **Polarimetric Formulation**: $\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot e^{i\Delta}$
- **Dispersion Models**: Cauchy and Sellmeier formulations for $n(\lambda)$ and $k(\lambda)$.
- **Measurement Targets**:
  - Thin gate dielectric / standard oxide: $3.5\text{ nm} \pm 0.05\text{ nm}$
  - Thick films ($1.3\ \mu\text{m}$ resist / ILD): $\pm 2\text{ nm}$
  - Optical beam uniformity: $>95\%$
- **Alignment Mechanism**: Auto-collimation tilt & closed-loop piezo/micrometer gap/height adjustment ($0.1\ \mu\text{m}$ sensitivity).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

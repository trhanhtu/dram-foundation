# Post-CMP Automated 49-Point Polarized Optical Measurement Recipe Execution

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Captures the standard operating procedure for executing automated 49-point spectroscopic ellipsometry mapping on post-CMP wafers in the 180nm DRAM process flow (DRAM Foundation VN). Polarized optical metrology extracts across-wafer thickness distributions of residual Inter-Layer Dielectric (ILD) oxide above planarized tungsten contacts and stacked capacitor test structures.

## Key Details / Architecture
- **Polarization Physics**: Measures change in polarization state upon reflection:
  $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
- **Dispersion Parameterization**: Fits refractive index $n(\lambda)$ and extinction coefficient $k(\lambda)$ using Cauchy/Sellmeier dispersion formulations.
- **Pattern Layout**: 49-point polar/concentric map tracking radial film non-uniformity across post-CMP wafer surface.
- **Precision Criteria**: Sub-Angstrom dry oxide precision ($\pm 0.05\text{ nm}$) and high-precision thick film validation ($\pm 2\text{ nm}$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

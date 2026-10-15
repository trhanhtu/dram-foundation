# Knowledge: Cauchy-Sellmeier Optical Dispersion Model Regression & Sub-Angstrom Oxide Fitting

- **Date**: 2026-10-12
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
For the 180nm DRAM process generation (Gen 2 µm), dry gate oxide grown at 850°C–900°C requires precise physical thickness validation around 3.5 nm with sub-Angstrom precision (±0.05 nm). This SOP documents the regression and fitting protocol using Cauchy dispersion modeling on spectroscopic ellipsometry data ($\Psi, \Delta$).

## Key Details / Architecture
- **Model Equation**: $n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}$, $k(\lambda) = 0$ for non-absorbing thermal oxide in the transparent spectral band.
- **Fundamental Ellipsometric Ratio**: $\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot e^{i\Delta}$.
- **Mapping**: Automated 9-point or 49-point wafer mapping to quantify radial uniformity.
- **Fitting Precision**: Sub-Angstrom precision target of $\pm0.05\text{ nm}$.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)
- Context Sources: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*, *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*

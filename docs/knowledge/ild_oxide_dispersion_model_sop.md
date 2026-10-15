# ILD Oxide Cauchy/Sellmeier Dispersion Model Parameterization & Sensitivity Analysis

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) and dispersion model engineering for spectroscopic ellipsometry characterization of post-CMP Inter-Layer Dielectric (ILD) silicon dioxide films in 180nm DRAM fabrication (DRAM Foundation VN). This protocol establishes parameterization using Cauchy/Sellmeier dispersion formulations and sensitivity cross-correlation screening to support 49-point full-wafer automated thickness and non-uniformity mapping.

## Key Details / Architecture
- **Model Physics**: Complex reflectance ratio $\rho = r_p / r_s = \tan(\Psi) \exp(i\Delta)$ parameterized over UV-VIS-NIR spectroscopic spectrum.
- **Cauchy Dispersion Formulation**: $n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}$, $k(\lambda) = 0$ (transparent regime $\lambda \ge 350\text{ nm}$).
- **Sellmeier Formulation (Alternative wideband)**: $n^2(\lambda) = 1 + \sum_i \frac{A_i \lambda^2}{\lambda^2 - \lambda_i^2}$.
- **Sensitivity & Correlation Guardrail**: Cross-correlation $|r_{A_n, d}| < 0.90$ to break optical thickness-index parameter correlation.
- **Full Wafer Metrology**: Automated 49-point wafer mapping to track radial film non-uniformity across post-CMP planarized wafers.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- Verified Local Literature Context: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
- Verified Local Literature Context: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- Verified Local Literature Context: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*

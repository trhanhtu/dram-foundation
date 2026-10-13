# Micro-Knowledge: Cauchy & Sellmeier Optical Dispersion Modeling for SiO2/Si Stack

- **Date**: 2026-10-12
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Spectroscopic ellipsometry parameterizes complex Fresnel reflection coefficients $\rho = r_p / r_s = \tan(\Psi) \exp(i\Delta)$ across single-crystal silicon substrates with thermal silicon dioxide ($\text{SiO}_2$) films. For transparent dielectric oxides in the visible to near-infrared spectrum, optical constants $n(\lambda)$ and $k(\lambda)$ are parameterized using Cauchy ($n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}$) or Sellmeier oscillator formulations.

## Optical Modeling Architecture
1. **Substrate Definition**: Single-crystal silicon (c-Si) reference dielectric tensor.
2. **Dielectric Layer Formulation**: Cauchy formulation with $k(\lambda) = 0$ for transparent thermal oxide across UV-Vis-NIR, or Sellmeier single/multi-resonance model.
3. **Fresnel Multi-Layer Stack Propagation**: Transfer-matrix calculation matching experimental $\Psi(\lambda)$ and $\Delta(\lambda)$ across automated 49-point wafer mapping.
4. **Target Precision & Validation**: Sub-angstrom precision ($\pm 0.05\text{ nm}$) on ultra-thin gate oxides ($3.5\text{ nm}$) and $\pm 2\text{ nm}$ across thicker dielectric/resist layers.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

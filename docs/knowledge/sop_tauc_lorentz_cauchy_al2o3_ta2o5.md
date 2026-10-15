# SOP: Tauc-Lorentz and Cauchy Optical Dispersion Model Formulation for Al2O3/Ta2O5 Stacks

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented
- **Module**: Spectroscopic Ellipsometry Modeling and Planar Monitor Wafer Thickness/Index Mapping

## Overview & Rationale
Formulation of optical dispersion models for planar monitor wafers hosting atomic layer deposition (ALD) high-k $\text{Al}_2\text{O}_3/\text{Ta}_2\text{O}_5$ dielectric stacks within the 180nm DRAM node (MIM Crown Capacitor over Bitline architecture). Decoupling ultra-thin $\text{Al}_2\text{O}_3$ interfacial barrier layers and $\text{Ta}_2\text{O}_5$ high-$\kappa$ bulk layers ensures non-destructive validation of Equivalent Oxide Thickness (EOT: 3 to 4 nm, $\kappa > 15$).

## Model Formulations
- **Cauchy Dispersion (Transparent Regime, $\lambda > 350\text{ nm}$)**:
  $$n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4}, \quad k(\lambda) \approx 0$$
- **Tauc-Lorentz Dispersion (Interband Transition / UV Absorption Regime)**:
  Parameterizes dielectric functions $\varepsilon_1(E)$ and $\varepsilon_2(E)$ using optical bandgap $E_g$, amplitude $A$, broadening $C$, and resonance peak $E_0$.

## Target Metrics
- Equivalent Oxide Thickness (EOT): 3.0 to 4.0 nm
- Cell capacitance budget: $\ge 28\text{ fF/cell}$ (retention $> 64\text{ ms}$ at $85^\circ\text{C}$)
- Dielectric leakage current: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$
- Spectroscopic ellipsometer precision: sub-Angstrom ($\pm 0.05\text{ nm}$) on calibration oxide (3.5 nm thermally grown $\text{SiO}_2$)
- Wafer non-uniformity mapping: Automated 9-point or 49-point array

## References & Related Files
- [docs/context.yaml](..../../context.yaml)
- [docs/context2.yaml](..../../context2.yaml)
- [docs/context3.yaml](..../../context3.yaml)

# SOP: Mean Squared Error Goodness-of-Fit Validation and Cross-Verification via Stylus Profilometry Step Height

- **Date**: 2026-10-13
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN)
- **Status**: Implemented
- **Module**: Metrology / Optical Dispersion Model Calibration & Physical Cross-Verification
- **Target Node**: 180nm Open-Source DRAM (Gen 1 mm)

## Overview & Rationale
Establishes an industrial Standard Operating Procedure (SOP) for qualifying thin dielectric film thickness ($SiO_2$ / gate oxide / hardmask steps) post-Buffered Oxide Etch (BOE 6:1). Combines non-destructive Spectroscopic Ellipsometry (SE) optical dispersion model fitting (Cauchy-Sellmeier parameterization) with physical contact stylus profilometry step-height cross-validation. Ensures robust elimination of optical parameter cross-correlation, optical voiding, and interfacial roughness errors.

## Key Acceptance Criteria
- SE Measurement Precision (Dry Gate Oxide $3.5\text{ nm}$): $\le \pm 0.05\text{ nm}$
- SE Measurement Precision (Thick Resist / Dielectric $1.3\ \mu\text{m}$): $\le \pm 2\text{ nm}$
- SE Cauchy-Sellmeier Goodness-of-Fit Mean Squared Error (MSE): $\le 2.50$
- Optical vs. Stylus Profilometry Step Height Discrepancy ($\Delta t$): $\le \pm 1.0\text{ nm}$

## Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

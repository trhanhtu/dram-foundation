# Spectroscopic Ellipsometry Calibration Standard and Blanket Monitor Wafer Preparation

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Accepted

## Overview & Rationale
Preparation protocol for spectroscopic ellipsometry calibration standards and planar blanket monitor test wafers supporting 180nm DRAM high-k capacitor dielectric qualifying runs (ALD $\text{Al}_2\text{O}_3/\text{Ta}_2\text{O}_5$). Calibration wafer integrity and thickness modeling precision ($\pm 0.05\text{ nm}$) ensure reliable baseline determination before 3D crown capacitor deposition.

## Key Details / Architecture
- **Thermal Baseline Standard**: High-purity p-type Si (100), pre-cleaned via RCA-1 and 0.5% DHF strip, followed by dry oxidation at 850°C–900°C to achieve a nominal $3.5\text{ nm}$ $\text{SiO}_2$ calibration reference.
- **Optical Polarimetry Principle**: Measurement of complex reflectance ratio $\rho = r_p / r_s = \tan(\Psi)\exp(i\Delta)$ across spectroscopic wavelengths parameterized via Cauchy/Sellmeier dispersion models.
- **Wafer Mapping Grid**: Automated 49-point polar grid mapping tracking radial uniformity and edge exclusion ($5\text{ mm}$).
- **Correlation with Capacitor Specs**: Ensures high-$k$ dielectric stack conforms to Equivalent Oxide Thickness (EOT) window ($3\text{ to } 4\text{ nm}$) targeting cell capacitance $\ge 28\text{ fF/cell}$ ($\ge 25\text{ to }30\text{ fF/cell}$) and leakage $< 1\text{ fA/cell}$ at 85°C.

## References & Related Files
- `docs/context.yaml`
- `docs/context2.yaml`
- `docs/context3.yaml`

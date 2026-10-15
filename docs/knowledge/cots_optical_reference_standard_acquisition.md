# SOP Micro-Knowledge: COTS Optical Reference Calibration Standard Wafer Kit & Standard Material Library Acquisition

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Calibration standards and optical dispersion libraries are required for spectroscopic ellipsometry and reflectometry metrology in 180nm DRAM CMP/ILD workflows. High-accuracy extraction of complex reflection coefficients ($\rho = r_p / r_s = \tan(\Psi) e^{i\Delta}$) requires certified reference wafers to parameterize Cauchy and Sellmeier models ($n(\lambda)$, $k(\lambda)$) across ultra-thin gate oxides (3.5 nm) and thick organic films (1.3 $\mu\text{m}$ photoresist).

## Key Technical Specifications & Criteria
- **Gate Oxide Standard**: Nominal $3.5\text{ nm}$ dry thermal $\text{SiO}_2$ on $\text{Si}\langle100\rangle$, verified to sub-Angstrom precision within $\pm 0.05\text{ nm}$.
- **Thick Organic Film Standard**: Nominal $1.3\ \mu\text{m}$ photoresist (Shipley 1813 baseline) verified within $\pm 2\text{ nm}$.
- **Automated Mapping**: 49-point full-wafer automated polar/Cartesian grid metrology to verify radial film non-uniformity across post-CMP ILD and furnace runs.
- **Optical Dispersion Library**: Dispersion parameters fitting Cauchy ($n(\lambda) = A + B/\lambda^2 + C/\lambda^4$) and Sellmeier models with zero unphysical absorption ($k=0$) in dielectric transparency bands.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- Context Sources: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*, *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*, *Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose*.

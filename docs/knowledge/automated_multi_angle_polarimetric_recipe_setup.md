# Automated Multi-Angle Polarimetric Recipe Setup & Psi/Delta Baseline Repeatability Verification

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Node Context**: 180nm Open-Source DRAM Chip > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > Chemical Mechanical Planarization (CMP) of Inter-Layer Dielectrics & Tungsten Plugs > Inter-Layer Dielectric (ILD) Oxide CMP Recipe Optimization and Polish > Post-CMP Spectroscopic Ellipsometry Thickness & AFM Surface Roughness Metrology > 49-Point Full-Wafer Automated Optical Thickness and Non-Uniformity Mapping > Spectroscopic Ellipsometry Optical Dispersion Model & Baseline Recipe Setup > Automated Multi-Angle Polarimetric Recipe Setup & Psi/Delta Baseline Repeatability Verification
- **Generation**: Gen 3 (180nm)
- **Action Type**: Make

## Overview & Rationale
Non-destructive spectroscopic ellipsometry measures polarization state changes upon reflection ($\rho = r_p / r_s = \tan(\Psi) \cdot e^{i\Delta}$), enabling sub-angstrom optical thickness parameterization for critical dielectrics (e.g. gate oxide and post-CMP ILD planarization layers). To establish reproducible full-wafer metrology, baseline multi-angle polarimetric calibration and $\Psi / \Delta$ repeatability verification are required prior to 49-point wafer mapping.

## Key Implementation Parameters
- **Fundamental Polarimetric Ratio**: $\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$
- **Optical Dispersion Models**: Cauchy ($n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4}$) and Sellmeier formulations for dielectric parameterization.
- **Reference Precision Targets**:
  - Dry Gate Oxide ($3.5\,\text{nm}$): $\pm 0.05\,\text{nm}$ ($\pm 0.5\,\text{\AA}$) precision.
  - Photoresist ($1.3\,\mu\text{m}$, Shipley 1813): $\pm 2.0\,\text{nm}$ precision.
- **Wafer Mapping Grid**: Automated 49-point polar coordinate grid tracking radial non-uniformity across post-CMP ILD oxide.
- **Tool Alignment Reference**: Manufacturing placement grid constraint of $0.005\,\mu\text{m}$ ($5\,\text{nm}$).

## References & Related Files
- [Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology](./docs/context.yaml)
- [SkyWater SKY130 Open PDK Design Rules & Lithography Grid](./docs/context.yaml)
- [Sam Zeloof Z1 Garage Semiconductor Journal (2018)](./docs/context.yaml)

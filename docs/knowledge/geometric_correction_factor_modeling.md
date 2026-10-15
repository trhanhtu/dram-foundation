# Geometric Correction Factor Modeling and Uniformity Contour Extraction

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented

## Overview & Rationale
Defines the mathematical modeling and automated contour extraction workflow for collinear four-point probe sheet resistance ($R_s$) mapping of Metal-1 (BEOL) thin films in the 180nm Open-Source DRAM process. Uncorrected measurements near wafer boundaries deviate significantly from the idealized infinite-sheet semi-infinite boundary conditions ($R_{s,\text{raw}} = \frac{\pi}{\ln(2)} \frac{V}{I} \approx 4.5324 \frac{V}{I}$); geometric correction factor (GCF) integration and spatial interpolation are required to produce reliable uniformity maps across full 200mm wafers.

## Key Details / Architecture
- **Probe Head Geometry**: Collinear tungsten carbide tips, tip radius $r = 50\text{--}100\,\mu\text{m}$, inter-probe pitch $s = 1.0\,\text{mm}$.
- **Measurement Conditions**: Constant DC excitation current $I = 1.0\text{--}10.0\,\text{mA}$ through outer probes (1 and 4), differential floating potential $V$ sensed across inner probes (2 and 3).
- **Geometric Modeling**:
  - Thin-film condition: $t \ll s/2$ ($0.5\,\text{mm}$).
  - Finite boundary correction factor $F(d/s)$ applied when wafer/boundary distance $d < 40s$ ($40\,\text{mm}$).
  - Fully corrected sheet resistance: $R_s = 4.5324 \cdot \frac{V}{I} \cdot F(d/s)$.
- **Uniformity Contour Extraction**: 49-point/81-point polar-grid sampling, kriging/spline spatial interpolation, and $1\sigma / \text{Mean}$ metric extraction.

## References & Related Files
- [Four-Point Collinear Probe Metrology for Semiconductor Sheet Resistance](./docs/metrology_4pp.md)

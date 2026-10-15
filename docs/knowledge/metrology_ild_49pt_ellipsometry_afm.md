# 49-Point Full-Wafer ILD Thickness Mapping, Optical Constant (n, k) Cross-Validation, and AFM Surface Roughness Correlation

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Post-CMP Inter-Layer Dielectric (ILD) oxide planarization in 180nm DRAM tapeout requires precise cross-validation between optical spectroscopic ellipsometry and physical atomic force microscopy (AFM). Automated 49-point wafer mapping tracks radial film non-uniformity across spin coating, deposition, and polish runs, while Cauchy dispersion parameter fitting extracts refractive index $n(\lambda)$ and extinction coefficient $k(\lambda)$. Correlating optical goodness-of-fit against high-frequency AFM micro-roughness ($R_q$) prevents dielectric breakdown and guarantees planar baseline for subsequent metal/via lithography.

## Key Details / Architecture
- **Spectroscopic Ellipsometry Principle**:
  $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
- **Cauchy Optical Dispersion Model**:
  $$n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}, \quad k(\lambda) = 0 \text{ (in transparent oxide regime)}$$
- **Wafer Mapping**: Automated 49-point polar/concentric pattern tracking within-wafer non-uniformity (WIWNU).
- **Physical Validation**: Atomic Force Microscopy (AFM) tapping mode over $5\,\mu\text{m} \times 5\,\mu\text{m}$ area on center, mid-radius, and edge exclusion dies.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)
- Source: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
- Source: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*

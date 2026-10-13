# 49-Point Radial Oxide Thickness Mapping and Regression Fitting Analysis

- **Date**: 2026-10-13
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Accepted
- **Node**: 180nm Open-Source DRAM (Generation 1, mm-scale test vehicle / wafer metrology)

## Overview & Rationale
For the 180nm DRAM node, the access transistor gate oxide ($T_{ox}$) is thermally grown at 850°C–900°C under dry oxidation to reach a nominal physical thickness of 3.5 nm. Achieving uniform threshold voltage ($V_{th}$) and access transistor reliability across the wafer requires strict monitoring of cross-wafer non-uniformity and radial roll-off. This document specifies the 49-point automated spectroscopic ellipsometry protocol and mathematical regression framework.

## Key Details / Metrology Architecture
1. **Dispersion Parameterization**: Cauchy model parameterization for thermal $\text{SiO}_2$ on $\text{Si}\langle100\rangle$:
   $$n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}, \quad k(\lambda) \approx 0$$
   Fundamental ellipsometric equation:
   $$\rho = \frac{r_p}{r_s} = \tan(\Psi) e^{i\Delta}$$
2. **Radial Sampling Scheme**: 49-point polar coordinate map comprising:
   - 1 center point ($r=0$)
   - 4 concentric rings:
     - Ring 1: $r = 0.25 R$ (8 sites)
     - Ring 2: $r = 0.50 R$ (12 sites)
     - Ring 3: $r = 0.75 R$ (12 sites)
     - Ring 4: $r = 0.95 R$ (16 sites)
3. **Regression Model**: 4th-order polynomial radial fit:
   $$T_{ox}(r) = a_0 + a_2 r^2 + a_4 r^4 + \epsilon$$

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

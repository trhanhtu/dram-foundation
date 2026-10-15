# Pattern-Dependent Dishing & Dielectric Erosion Metrology Correlation Against CMP Targets

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Metrology correlation protocol for 180nm open-source DRAM inter-layer dielectric (ILD) and tungsten plug (W-plug) chemical mechanical planarization (CMP). Characterizes optical film thickness, pattern-dependent dielectric erosion, and plug dishing across variable density structures (dense memory array 8F²/6F² cell layout vs. low-density periphery and TLM test structures).

## Key Details / Architecture
- **Spectroscopic Ellipsometry Modeling**: Cauchy/Sellmeier dispersion parameterized via angles $\Psi$ and $\Delta$ with Fresnel ratio $\rho = r_p / r_s = \tan(\Psi)\exp(i\Delta)$.
- **Thickness & Contour Mapping**: 49-point polar coordinate automated mapping for within-wafer non-uniformity (WIWNU).
- **AFM Micro-Topography Profilometry**: High-aspect ratio tapping mode AFM scanning across dense DRAM cell arrays (access transistor $L=180\text{ nm}$, $W=220\text{ nm}$) and scribe-line TLM pads ($W=100\ \mu\text{m}$, $L_{\text{pad}}=50\ \mu\text{m}$).
- **Electrical Verification**: Transmission Line Measurement (TLM) correlation of specific contact resistivity ($\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2$) across pad spacings $d \in \{5, 10, 20, 40, 80\}\ \mu\text{m}$.

## References & Related Files
- [`docs/context.yaml`](./docs/context.yaml)
- [`docs/context2.yaml`](./docs/context2.yaml)
- [`docs/context3.yaml`](./docs/context3.yaml)

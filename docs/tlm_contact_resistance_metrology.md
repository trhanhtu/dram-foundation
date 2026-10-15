# TLM Characterization & Specific Contact Resistivity Metrology

- **Date**: 2026-10-15
- **Source**: User & Literature Synthesis
- **Status**: Accepted

## Overview & Rationale
Transmission Line Measurement (TLM) structures are deployed in the Process Control Monitor (PCM) scribe lines to extract sheet resistance ($R_s$), contact resistance ($R_c$), transfer length ($L_T$), and specific contact resistivity ($\rho_c$) between metal interconnects and doped silicon diffusion. This validates ohmic contact integrity for 180nm CMOS/DRAM test chips.

## Key Details / Architecture
- **Pad Geometry**: Identical rectangular test pads with width $W = 100\ \mu\text{m}$, length $L_{\text{pad}} = 50\ \mu\text{m}$.
- **Gap Progression**: Spacing intervals $d \in \{5, 10, 20, 40, 80\}\ \mu\text{m}$.
- **Formulation**:
  - $R_T = 2 R_c + \left(\frac{R_s}{W}\right) d$
  - Slope $= \frac{R_s}{W} \implies R_s = \text{Slope} \times W$
  - $Y\text{-intercept} = 2 R_c \implies R_c = \frac{Y\text{-intercept}}{2}$
  - $X\text{-intercept} = -2 L_T \implies L_T = \frac{|X\text{-intercept}|}{2}$
  - $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\ [\Omega\cdot\text{cm}^2]$

## References & Related Files
- [context.yaml](../context.yaml)
- [context2.yaml](../context2.yaml)
- [docs/sop_tlm_probing_iv.md](../sop_tlm_probing_iv.md)

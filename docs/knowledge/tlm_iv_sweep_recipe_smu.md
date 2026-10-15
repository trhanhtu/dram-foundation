# Automated Multi-Pad TLM I-V Sweep Recipe Execution via SMU

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for executing automated multi-pad Transmission Line Measurement (TLM) current-voltage (I-V) sweeps using a multi-channel Source Measure Unit (SMU) and probe station. The methodology enables precise extraction of contact resistance ($R_c$), sheet resistance ($R_s$), transfer length ($L_T$), and specific contact resistivity ($\rho_c$) on 180nm CMOS/DRAM test structures.

## Key Details / Architecture
- **Structure**: Rectangular pads $W = 100\,\mu\text{m}$, $L_{\text{pad}} = 50\,\mu\text{m}$, gaps $d \in \{5, 10, 20, 40, 80\}\,\mu\text{m}$.
- **Formulation**:
  - $R_T = 2 R_c + \frac{R_s}{W} d$
  - Slope $= \frac{R_s}{W} \implies R_s = \text{Slope} \cdot W$
  - Y-intercept $= 2 R_c \implies R_c = \frac{Y\text{-intercept}}{2}$
  - X-intercept $= -2 L_T \implies L_T = \frac{|X\text{-intercept}|}{2}$
  - $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\,[\Omega\cdot\text{cm}^2]$
- **Interconnect Baseline**: Al-0.5% Cu or pure Al (Metal-1 thickness $350\,\text{nm} \pm 5\%$, sheet resistance $R_s < 0.08\,\Omega/\square$).

## References & Related Files
- [context.yaml](./docs/context.yaml)
- Context Sources: Transmission Line Measurement (TLM) for Specific Contact Resistivity; Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects.

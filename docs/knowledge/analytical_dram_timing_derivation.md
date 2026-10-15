# Analytical Derivation of Critical DRAM Timing Parameters (tRP, tRCD, tRAS, tRC)

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN Council)
- **Status**: Implemented

## Overview & Rationale
Establishes the analytical derivation and RC verification methodology for critical timing parameters ($t_{RCD}$, $t_{RAS}$, $t_{RP}$, $t_{RC}$) of the 180nm Open-Source DRAM node (1T1C stacked capacitor over bitline architecture).

## Key Parameters & Formulations
- **Cell Geometry**: Access NMOS $L = 180\text{ nm}$, $W = 220\text{ nm}$; gate oxide thickness $T_{ox} \approx 3.5\text{ nm}$.
- **Capacitance Budgets**: $C_s \ge 28\text{ fF}$ (25 to 30 fF range), $C_b = 150\text{ to } 250\text{ fF}$ (256–512 cells/BL).
- **Capacitance Ratio**: $C_b / C_s \in [5:1, 9:1]$ yielding signal margin $\Delta V_{BL} = \frac{V_{DD}/2}{1 + C_b/C_s} \approx 135\text{ to } 180\text{ mV}$ at $V_{DD} = 1.8\text{ V}$.
- **Timing Equations**:
  - $t_{RCD} = t_{WL\_rise} + t_{cell\_share} + t_{SA\_sense}$
  - $t_{RAS} = t_{RCD} + t_{restore}$
  - $t_{RP} = \tau_{eq} \cdot \ln\left(\frac{\Delta V_{diff}}{V_{target\_error}}\right) = R_{eq\_net} \cdot C_b \cdot \ln(100)$
  - $t_{RC} = t_{RAS} + t_{RP}$

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

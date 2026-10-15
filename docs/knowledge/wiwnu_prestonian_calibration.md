# Within-Wafer Non-Uniformity (WIWNU) Contour Modeling & Prestonian Coefficient Calibration

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Node ID**: `node-cmp-ild-wiwnu-preston-calib`
- **Context Level**: Gen 3 (180nm CMOS / DRAM Foundation VN MPW Tapeout)

## Overview & Rationale
During Chemical Mechanical Planarization (CMP) of Inter-Layer Dielectric (ILD) oxide over 180nm polysilicon gate and active diffusion topographies (minimum drawn gate length $0.15\,\mu\text{m}$, poly pitch $0.21\,\mu\text{m}$, overlay budget $\le 35\,\text{nm}$), removal rate variations across the wafer diameter introduce Within-Wafer Non-Uniformity (WIWNU). Non-uniform residual oxide thickness directly impacts subsequent DUV photolithography depth-of-focus (DoF) and contact-to-diffusion contact resistance ($R_c$ / specific contact resistivity $\rho_c$). This SOP provides an empirical, calibrated multi-zone Prestonian model and contour mapping protocol to maintain WIWNU $\le 5.0\%$.

## Key Physical Calibration Model
The Preston equation governs empirical material removal rate ($MRR$):
$$MRR = K_p \cdot P \cdot V + C_0$$
Where:
- $MRR$: Oxide removal rate ($\text{\AA/min}$).
- $P$: Applied polishing downforce pressure ($\text{psi}$).
- $V$: Relative linear pad-wafer velocity ($\text{m/s}$).
- $K_p$: Prestonian kinetic coefficient ($\text{\AA} \cdot \text{min}^{-1} \cdot \text{psi}^{-1} \cdot (\text{m/s})^{-1}$).
- $C_0$: Sub-threshold non-mechanical chemical dissolution offset ($\text{\AA/min}$).

WIWNU is quantified across multi-point concentric radial grids (49-point polar map, $3\,\text{mm}$ edge exclusion):
$$\text{WIWNU } (1\sigma, \%) = \left( \frac{\sigma_{THK}}{\mu_{THK}} \right) \times 100\%$$

## References & Related Files
- [context.yaml](./docs/context.yaml)
- [context2.yaml](./docs/context2.yaml)
- [context3.yaml](./docs/context3.yaml)

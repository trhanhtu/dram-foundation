# 8F² 1T1C Cell 3D Field Solver Parasitic Extraction (RC Extraction)

- **Date**: 2026-10-13
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for 3D field solver-based full-wave and electrostatic/magnetoquasistatic parasitic resistance and capacitance (RC) extraction of an 8F² 1T1C DRAM unit cell and folded bitline mini-array at the 180nm technology node. Accurate extraction guarantees sensing read margins, capacitor charge retention, and noise immunity against bitline cross-coupling and alpha-particle soft errors.

## Key Details / Architecture
- Unit Cell Footprint: $8F^2 = 0.259\ \mu\text{m}^2$ ($F = 180\ \text{nm}$, access transistor $L = 180\ \text{nm}, W = 220\ \text{nm}$).
- Bitline and Wordline Pitch: $360\ \text{nm} - 400\ \text{nm}$.
- Capacitor Stack: Crown-shaped polysilicon or Metal-Insulator-Metal (MIM) Capacitor-Over-Bitline (COB) contacted via Tungsten plug (W-plug).
- Dielectric: ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ ($\kappa > 15$, $\text{EOT} = 3 - 4\ \text{nm}$, physical gate oxide $\sim 3.5\ \text{nm}\ \text{SiO}_2$).
- Capacitance targets: $C_s \ge 25 - 30\ \text{fF}$ (nominal $28\ \text{fF}$), $C_b = 150 - 250\ \text{fF}$ (for $256/512$ cells/BL), ratio $C_b/C_s \in [5:1, 9:1]$.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

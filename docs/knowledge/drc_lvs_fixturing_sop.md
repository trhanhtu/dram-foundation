# SOP: Precision Tooling & Fixturing for Full-Chip Physical Sign-Off DRC, LVS, and Metal Density Fill Verification

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN)
- **Status**: Implemented
- **Domain**: Semiconductor Tapeout / Physical Sign-Off & Tooling Fixturing

## Overview & Rationale
Defines standard physical verification execution and mechanical mask fixturing tolerances for 180nm Open-Source DRAM tapeout, ensuring DRC, LVS, seal ring integrity, and reticle plate clamping tolerances conform to commercial foundry tapeout guidelines.

## Physical Verification Targets & Specifications
- **Cell Transistor Dimensions**: Channel length $L = 180\,\text{nm}$, width $W = 220\,\text{nm}$.
- **Wiring Pitch**: Bitline and wordline pitch = $360\,\text{nm}$ to $400\,\text{nm}$.
- **Storage Capacitor Budget**: Minimum $25\,\text{fF}$ to $28\,\text{fF}$ per cell (stacked crown/cylinder COB).
- **Dielectric Equivalent Oxide Thickness (EOT)**: $3\,\text{nm}$ to $4\,\text{nm}$ (ONO or $\text{Ta}_2\text{O}_5$/$\text{Al}_2\text{O}_3$, $\kappa > 15$).
- **Sub-threshold & Junction Leakage**: $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$ (retention $> 64\,\text{ms}$).
- **Pad Opening Fixture**: $100\,\mu\text{m} \times 100\,\mu\text{m}$ aluminum bonding pads.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

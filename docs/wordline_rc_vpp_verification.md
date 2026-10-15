# Wordline RC Extraction & High-Voltage VPP Overdrive DRC/LVS Verification

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure (SOP) and metrology flow for extracting Wordline parasitic RC network values and verifying High-Voltage $V_{PP}$ Overdrive design rules (DRC) and layout-versus-schematic (LVS) consistency for the 180nm 1T1C $8F^2$ Folded Bitline Open-Source DRAM layout.

## Key Details & Verification Checklist
- **Operating Voltages**: Nominal core $V_{DD} = 1.8\text{ V}$, Wordline Overdrive Boost $V_{PP} = 2.5\text{ V to } 2.8\text{ V}$ to overcome access transistor $V_{th} \sim 0.5\text{ V to } 0.7\text{ V}$.
- **Storage Node Target**: $C_s \ge 28\text{ fF}$ nominal ($25\text{ fF to } 30\text{ fF}$).
- **Bitline Ratio**: $C_b / C_s \le 9:1$ (nominal $150\text{ fF to } 250\text{ fF}$ for 256/512 cell array blocks).
- **Leakage Floor**: $I_{\text{leak}} \le 1.0\text{ fA/cell}$ at $85^\circ\text{C}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

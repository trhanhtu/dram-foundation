# SOP: JEDEC Protocol Compliance Verification & Transient Timing Signoff Simulation

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure for JEDEC protocol compliance verification and SPICE transient timing signoff simulation across 180nm open-source DRAM 1T1C bitcells, folded bitline sense amplifiers, and access transistors.

## Key Details / Architecture
Integrates folded bitline (8F^2) architecture, cross-coupled regenerative sense amplifier timing phases, boosted wordline levels ($V_{PP} = 2.6\text{ V to }2.8\text{ V}$), and target capacitance budgets ($C_s \ge 25\text{ fF}$, $C_b/C_s$ between $5:1$ and $9:1$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

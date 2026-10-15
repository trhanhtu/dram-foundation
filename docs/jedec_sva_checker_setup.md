# JEDEC Timing Assertions & SVA Checker Testbench Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the cycle-accurate SystemVerilog Assertions (SVA) protocol verification testbench for the 180nm Open-Source DRAM Chip architecture. Aligns digital command state machine checking against underlying discrete transistor and sense amplifier physical boundaries ($t_{RP}$, $t_{RCD}$, $t_{RFC}$).

## Key Details / Architecture
- **Physical Cell Boundary Constraints**: Access transistor dimensions ($W/L = 220\,\text{nm} / 180\,\text{nm}$), stacked capacitor $C_{cell} \ge 28\,\text{fF}$, boosted wordline overdrive $V_{PP} = 2.6\,\text{V} - 2.8\,\text{V}$, and $I_{leak} \le 1\,\text{fA/cell}$ at 85°C.
- **Sense Amp Phase Dynamics**: SAN pull-down followed by SAP pull-up ($1 - 2\,\text{ns}$ delay), driving equalization to $V_{BLP} = V_{DD} / 2 = 0.9\,\text{V}$.
- **Verification Directives**: SVA properties binding Command Bus (`CS_N`, `RAS_N`, `CAS_N`, `WE_N`, `BA`, `ADDR`) to cycle constraints for PRECHARGE-to-ACTIVATE ($t_{RP}$), ACTIVATE-to-READ/WRITE ($t_{RCD}$), and AUTO-REFRESH-to-ACTIVATE ($t_{RFC}$).

## References & Related Files
- [Stage 3 Discrete Long-Channel MOSFET & CMOS Inverter Verification](./docs/context.yaml)
- [Cross-Coupled Regenerative Sense Amplifier Timing & Charge Restoration](./docs/context2.yaml)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context3.yaml)

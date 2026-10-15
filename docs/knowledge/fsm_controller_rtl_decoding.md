# Finite State Machine (FSM) Controller RTL Implementation & Command Decoding

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Council Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Actionable industrial leaf Standard Operating Procedure (SOP) for the RTL implementation, JEDEC command decoding, and physical sequence coordination of the DRAM controller on 180nm CMOS technology (Gen 2 µm).

## Key Details / Architecture
- **Control Sequencer**: Synchronous Moore/Mealy hybrid FSM orchestrating Wordline boost ($V_{PP} = 2.6\,\text{V} - 2.8\,\text{V}$), Sense Amplifier activation ($SAN$ pulldown, $SAP$ pullup delayed by $1-2\,\text{ns}$), and equalization ($EQ$ high to $V_{BLP} = V_{DD}/2$).
- **Command Truth Table**: Active low control bus decoding $\{CS\_n, RAS\_n, CAS\_n, WE\_n\}$ for NOP, ACT, PRE, READ, WRITE, and REF.
- **Physical Cell Target Parameters**: 
  - $C_s \ge 28\,\text{fF}$ stacked capacitor over bitline (COB).
  - $C_{BL} \approx 250\,\text{fF}$ folded bitline capacitance yielding $\Delta V \approx 100 - 150\,\text{mV}$.
  - Transistor dimensions $W/L = 220\,\text{nm} / 180\,\text{nm}$.
  - Leakage limit $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/sop_fsm_controller_rtl_decoding.md](./docs/sop_fsm_controller_rtl_decoding.md)

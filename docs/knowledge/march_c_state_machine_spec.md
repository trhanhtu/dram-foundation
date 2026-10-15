# March C- State Machine Register Architecture & Timing Parameter Specification

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
This specification defines the hardware register architecture, timing sequence, and finite state machine (FSM) control parameters for the on-chip March C- Built-In Self-Test (BIST) engine integrated within the open-source 180nm DRAM test vehicle (DRAM Foundation VN). It interfaces directly with the closed-loop ESP32 motor controller and telemetry engine to automate VDD retention shmoo plotting and bit-flip auditing.

## Key Details / Architecture
- **March C- Sequence**: `{ ⇕ (w0); ⇑ (r0, w1); ⇑ (r1, w0); [Pause]; ⇓ (r0, w1); ⇓ (r1, w0); ⇕ (r0) }`
- **Register Map**: Base offset `0x4000_1000` covering Control (`MARCH_CTRL`), Timing (`MARCH_TIMING`), Pause Duration (`MARCH_PAUSE`), Base/Bound Address ranges, and Bit-Flip Error Telemetry (`MARCH_ERR_CNT`, `MARCH_FAIL_ADDR`).
- **Physical Integration**: Calibrated against stacked capacitor cell parameters ($C_s = 28\text{ fF}$, folded bitline $C_b = 150 - 250\text{ fF}$, leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

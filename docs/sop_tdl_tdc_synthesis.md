# Tapped-Delay-Line TDC RTL Core & Calibration Engine Synthesis

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for the RTL implementation, carry-chain synthesis, and code-density calibration engine of a Tapped-Delay-Line (TDL) Time-to-Digital Converter (TDC) deployed in an FPGA Hardware-in-the-Loop (HIL) timing metrology testbench. This TDC precisely characterizes bitline signal development latency and sense amplifier activation margins on 180nm open-source DRAM arrays.

## Key Details / Architecture
- **TDC Architecture**: Dedicated carry-chain tapped delay lines mapped to fast lookahead arithmetic primitives (e.g., CARRY4/CARRY8 / dedicated carry cells) with DFF capture registers.
- **Calibration Engine**: On-chip statistical code density calibration histogram generator to linearize delay bin non-uniformity (DNL/INL) across PVT variations.
- **Physical DRAM Coupling**: Calibrated against physical signal development $\Delta V = \frac{C_s}{C_{BL} + C_s} (V_{cell} - V_{DD}/2)$ with $C_s = 25\text{ to }30\text{ fF}$ and $C_{BL} = 250\text{ fF}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

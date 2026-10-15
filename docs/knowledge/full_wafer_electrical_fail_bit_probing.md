# Full-Wafer High-Density Electrical Fail-Bit Array Probing Execution

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure (SOP) for automated full-wafer electrical sort, bitmapping, and fail-bit clustering on 180nm open-source DRAM wafers (DRAM Foundation VN). It establishes screening protocols for contact overdrive, DC parametric baselines, marching functional patterns, and elevated temperature retention stress.

## Key Details / Architecture
- **Thermal Chuck Setpoint**: 85°C for elevated retention stress.
- **Transistor Baseline (W/L = 2.0 µm / 0.18 µm)**: Extracted $V_{thn} = +0.55\text{ V} \pm 50\text{ mV}$, $I_{on}/I_{off} > 10^7$ at $V_{DS} = 1.8\text{ V}$.
- **Storage Cell Budget**: Capacitance budget $\ge 28\text{ fF/cell}$ (nominal range 25 to 30 fF), cell leakage $< 1\text{ fA/cell}$ at 85°C.
- **Array Retention**: Data retention time $> 64\text{ ms}$ at 85°C.
- **Fail-Bit Clustering**: Maps single-bit fails, pair fails, wordline/bitline opens/shorts across 360 nm to 400 nm pitch structures.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

# Micro-Knowledge: 1T1C Device Extraction & LVS Rule Deck Benchmark Validation

- **Date**: 2026-10-15
- **Source**: Domain Expert Agent
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure (SOP) and verification benchmark for physical device extraction and Layout Versus Schematic (LVS) comparison of an 8F^2 folded bitline 1T1C DRAM cell in open-source 180nm CMOS technology.

## Key Details / Architecture
- **Cell Architecture**: Folded bitline 8F^2 footprint ($0.259\ \mu\text{m}^2$ at $F = 180\ \text{nm}$).
- **Capacitance Targets**: Storage capacitor $C_s \ge 25\ \text{fF}$ to $30\ \text{fF}$ (nominal $28\ \text{fF}$). Bitline capacitance $C_b = 150\ \text{fF}$ to $250\ \text{fF}$ for 256/512 cells/BL.
- **Ratio Budget**: $C_b / C_s$ constrained to $5:1$ to $9:1$ (must not exceed $10:1$ to maintain read margins $> 100\ \text{mV}$).
- **Access Transistor**: Verified against $180\ \text{nm}$ sub-micron transistor gate target ($W/L = 2.0\ \mu\text{m} / 0.18\ \mu\text{m}$), $V_{thn} = +0.55\ \text{V} \pm 50\ \text{mV}$, $I_{on} \ge 500\ \mu\text{A}/\mu\text{m}$, $I_{off} \le 10\ \text{pA}/\mu\text{m}$ ($I_{on}/I_{off} > 10^7$).

## References & Related Files
- [1T1C Device Extraction & LVS Rule Deck Benchmark Validation SOP](./docs/knowledge/sop_1t1c_device_extraction_lvs.md)

# Statistical Tail-Bit Decay Extraction & Thermal Retention Limit Analysis

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for 180nm Open-Source DRAM (Gen 2, 1T1C stacked capacitor architecture). Focuses on statistical tail-bit identification, parametric charge-decay extraction, and Arrhenius thermal limit characterization across wafer/package test setups.

## Key Details / Architecture
- Unit Cell: Access NMOS L = 180 nm, W = 220 nm; 8F^2 folded bitline (cell area = 0.259 µm²).
- Capacitance: Nominal C_s = 28 fF (spec: 25 fF to 30 fF), C_b = 150 fF to 250 fF per 256/512 cell bitline; C_b / C_s target: 5:1 to 9:1 (< 10:1).
- Retention & Leakage: Minimum 64 ms at 85°C with cell leakage <= 1 fA/cell.
- Characterization Flow: Closed-loop ESP32 motor controller / thermal stage -> Variable retention hold (10 ms to 1000 ms) -> March C- read/compare telemetry -> Weibull/log-normal tail extraction.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/knowledge/statistical_tail_bit_decay_analysis.md](./docs/knowledge/statistical_tail_bit_decay_analysis.md)

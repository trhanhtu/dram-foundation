# Automated DC Parametric Test Recipe Development & Test Pattern Mapping (180nm DRAM)

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operational sequence for Electrical Die Sort (EDS) automated DC parametric test recipe execution and wafer-level test pattern mapping. Validates discrete sub-micron MOSFETs, reference test structures, and dense DRAM memory cell arrays fabricated on an open-source 180nm architecture (SKY130 / 180nm CMOS rules).

## Key Details / Architecture
- **Probe Card Alignment**: Stepper positioning compliant with the 5 nm manufacturing grid and <= 35 nm gate-to-active overlay budget.
- **Linear Region Metrology**: Low-drain ($V_{DS} = 50\text{ mV}$) extraction of transconductance ($g_m$) and $V_{th}$.
- **High-Drain Current Ratio**: Saturation characterization ($V_{DS} = 1.8\text{ V}$) for $I_{on}/I_{off}$ verification ($> 10^7$).
- **Cell Retention / Leakage Screening**: Stacked capacitor capacitance extraction ($\ge 28\text{ fF/cell}$) and refresh leakage screening ($\le 1\text{ fA/cell}$ at 85°C).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

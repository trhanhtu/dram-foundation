# Statistical Cpk Calculation & Multi-Lot Yield Margin Validation

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) defining the multi-lot statistical capability index ($C_{pk}$ and $P_{pk}$) evaluation and pass/fail operating margin sign-off for Gen 3 (180nm) DRAM across ATE 2D VDD-Frequency Shmoo boundaries.

## Key Details / Architecture
- **Process Technology Integration**: SkyWater SKY130 (130nm-to-180nm commercial open-source foundry technology, $L_{\text{drawn}} = 150\,\text{nm}$, 5 nm grid).
- **Cell Metrology Targets**: Minimum access transistor channel $L = 180\,\text{nm}$, $W = 220\,\text{nm}$, cell capacitance budget $\ge 28\,\text{fF}$, leakage target $< 1\,\text{fA/cell}$ at 85°C.
- **Statistical Yield Rule**: Minimum $C_{pk} \ge 1.33$ ($4\sigma$ operating margin coverage) and overall process capability $P_{pk} \ge 1.33$ across $\ge 3$ distinct fabrication wafer lots.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

# SOP: Address Decoders & Wordline VPP Voltage Pump Design

- **Date**: 2026-10-08
- **Source**: Agent (Domain Expert AI)
- **Status**: Accepted
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Chip

## Overview & Rationale
In 180nm DRAM architectures (access transistor $L = 180\,\text{nm}$, $W = 220\,\text{nm}$), passing a full $V_{DD}$ level into the 1T1C stacked storage capacitor ($C_s \ge 25\text{--}28\,\text{fF}$) requires overdriving the selected wordline to an elevated voltage $V_{PP} \approx V_{DD} + V_{th} + \Delta V$. The Address Decoders and Wordline $V_{PP}$ Pump circuit network coordinates address predecoding, main/sub-wordline selection, Dickson charge pump boost, and high-voltage driving while protecting the $\sim 3.5\,\text{nm}$ gate oxide against dielectric breakdown.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- [docs/context3.yaml](../context3.yaml)

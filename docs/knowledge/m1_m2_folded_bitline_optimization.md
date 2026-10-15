# SOP: M1-M2 Folded Bitline Cross-Coupling and Route Pitch Optimization

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure for optimizing M1/M2 interconnect routing pitch and mitigating inter-bitline capacitive cross-coupling ($C_{c}$) in an $8F^2$ folded bitline 1T1C DRAM cell array on a 180nm commercial MPW process.

## Key Details & Physical Parameters
- Access Transistor: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
- Interconnect Pitch: Wordline and Bitline pitch targeted at $360\text{ nm}$ to $400\text{ nm}$.
- Storage Node Capacitance: $25\text{ fF}$ to $30\text{ fF}$ (Nominal $\ge 28\text{ fF}$).
- Subthreshold/Junction Leakage: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ for retention $> 64\text{ ms}$.
- Supply and Wordline Levels: $V_{DD} = 1.8\text{ V}$, $V_{th} = 0.5\text{ V} - 0.7\text{ V}$, boosted wordline $V_{PP} \ge 2.5\text{ V} - 2.8\text{ V}$.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context.yaml)
- [High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture](./docs/context.yaml)

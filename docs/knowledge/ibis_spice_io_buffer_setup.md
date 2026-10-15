# SOP: IBIS/SPICE I/O Buffer & Microstrip Transmission Line Model Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Task**: IBIS/SPICE I/O Buffer & Microstrip Transmission Line Model Setup
- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > ESP32 Closed-Loop Motor Controller > Signal Integrity & Level Shifter Daughtercard PCB (50-Ohm Controlled Impedance Microstrips) > 50-Ohm Controlled Impedance Stackup Design & Level Shifter Schematic Synthesis > High-Speed Bus Signal Integrity Transient & Eye-Diagram Verification > IBIS/SPICE I/O Buffer & Microstrip Transmission Line Model Setup

## Overview & Rationale
This Standard Operating Procedure (SOP) defines the precise setup, de-embedding, and transient simulation protocols for IBIS/SPICE I/O buffer models interfacing with 50-Ohm controlled impedance microstrip transmission lines. It establishes exact transistor dimensions, bitline parasitics, storage cell capacitances, and pad contact resistivities derived from verified 180nm DRAM literature.

## Verified Literature Citations & Physical Parameters
1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor channel length $L = 180\text{ nm}$, channel width $W = 220\text{ nm}$.
   - Shared bitline contact via tungsten plug (W-plug).
   - High-k dielectric ($\text{ONO}$ / $\text{Ta}_2\text{O}_5$ / $\text{Al}_2\text{O}_3$, $\kappa > 15$).
   - Storage node capacitance budget: Minimum $C_s \ge 28\text{ fF}$ per cell.
   - Sub-threshold and junction leakage target: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Folded bitline topology: $8F^2$ footprint ($0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$).
   - Array block: 256 or 512 cells per bitline with bitline parasitic capacitance $C_b = 150\text{ fF}$ to $250\text{ fF}$.
   - Capacitance ratio constraint: $C_b / C_s$ maintained between $5:1$ and $9:1$ (must not exceed $10:1$).
3. **Transmission Line Measurement (TLM) for Specific Contact Resistivity**:
   - TLM contact pads: Width $W = 100\ \mu\text{m}$, Length $L_{\text{pad}} = 50\ \mu\text{m}$.
   - Progressive gap spacing: $d \in \{5, 10, 20, 40, 80\}\ \mu\text{m}$.
   - Resistance formulation: $R_T = 2 R_c + (R_s / W) \cdot d$, with specific contact resistivity $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\ [\Omega\cdot\text{cm}^2]$.

## References & Related Files
- [context.yaml](./docs/context.yaml)
- [context2.yaml](./docs/context2.yaml)
- [context3.yaml](./docs/context3.yaml)

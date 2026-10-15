# Active Area DRC Verification & Diffusion-to-Gate Overlay Margin Metrology Analysis

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the leaf Standard Operating Procedure (SOP) for the 180nm Open-Source DRAM Chip (Gen 3 nm) folded bitline 1T1C unit cell layout. Focuses on physical Design Rule Check (DRC) verification of active diffusion islands and metrology analysis of gate-to-diffusion overlay/extension margins.

## Key Details / Architecture
- Unit Cell Footprint: Folded bitline $8F^2 = 0.259\ \mu\text{m}^2$ ($F = 180\ \text{nm}$).
- Channel Geometry: Length $L = 180\ \text{nm}$, Width $W = 220\ \text{nm}$.
- Gate/Bitline Pitch: $360\ \text{nm}$ to $400\ \text{nm}$.
- Storage Node Capacitance: $C_s \ge 25\ \text{fF}$ to $30\ \text{fF}$ (nominal $28\ \text{fF}$).
- Subthreshold & Junction Leakage Target: $< 1\ \text{fA/cell}$ at $85^\circ\text{C}$ for retention $> 64\ \text{ms}$.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- [docs/context3.yaml](../context3.yaml)

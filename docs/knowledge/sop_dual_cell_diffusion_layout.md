# Dual-Cell Shared Bitline Contact Diffusion Island Polygon Synthesis & Layout

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for synthesizing and laying out the active area (OD/diffusion) island for 8F² folded-bitline 1T1C DRAM cells in 180nm CMOS technology. A continuous active diffusion island encompasses two pass transistors sharing a single central bitline (BL) contact plug, flanked symmetrically by two wordline gates and terminating in dual storage node contact pads.

## Key Physical Dimensions & Rules
- Access Transistor Channel Length ($L$): $180\text{ nm}$
- Access Transistor Channel Width ($W$): $220\text{ nm}$
- Bitline / Wordline Pitch: $360\text{ nm} - 400\text{ nm}$
- Gate Dielectric ($T_{ox}$): $3.5\text{ nm}$ dry $\text{SiO}_2$
- Retention Requirement: $> 64\text{ ms}$ at $85^\circ\text{C}$
- Maximum Off-State Leakage: $< 1.0\text{ fA/cell}$ at $85^\circ\text{C}$

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](../../context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](../../context2.yaml)

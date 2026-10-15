# GDSII Integration and Hierarchy Flattening for Full-Chip DRC Deck Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Establishes standard operating procedures for integrating macro-level GDSII files (1T1C DRAM core array, periphery sense amplifiers, row decoders, and metal-fix routing) and selective hierarchy flattening. This prevents false positive DRC boundary violations across repetitive 8F² folded bitline arrays and ensures antenna deck accuracy prior to tapeout sign-off on 180nm commercial MPW runs.

## Key Details / Architecture
- **Technology Node**: 180nm CMOS (Feature size $F = 180\text{ nm}$).
- **Core Cell Topology**: 8F² folded bitline stacked capacitor cell ($0.259\ \mu\text{m}^2$).
- **Transistor Parameters**: Access NMOS channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
- **Array Wiring Pitches**: Bitline pitch = $360\text{ nm}$ to $400\text{ nm}$, Wordline pitch = $360\text{ nm}$ to $400\text{ nm}$.
- **Storage Capacitor Budget**: $C_s \ge 25\text{ to }30\text{ fF}$ (nominally $28\text{ fF}$), retention time $> 64\text{ ms}$ at $85^\circ\text{C}$, subthreshold/junction leakage $< 1\text{ fA/cell}$.
- **Capacitance Ratio**: $C_b / C_s$ maintained between $5:1$ and $9:1$ (for $256$ to $512$ cells/BL where $C_b = 150\text{ to }250\text{ fF}$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

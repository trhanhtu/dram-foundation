# Parasitic RC Extraction & Wordline Mesh Netlist Generation

- **Date**: 2026-10-13
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Actionable Standard Operating Procedure (SOP) for Parasitic RC Extraction (PEX) and Wordline Distributed Mesh Netlist Generation tailored for the 180nm Open-Source DRAM Chip architecture (DRAM Foundation VN). Wordline slew rate and settling directly determine charge transfer into the 1T1C storage capacitor under high-voltage V_PP overdrive conditions.

## Key Details / Architecture
- Process node: 180nm CMOS (Gen 2 µm DRAM).
- Cell layout topology: Folded bitline (8F^2 footprint = 0.259 µm² at F = 180nm).
- Access transistor: NMOS enhancement mode with L = 180nm, W = 220nm, V_th ~ 0.5V to 0.7V.
- Wordline overdrive pump: V_PP >= 2.5V to 2.8V supplied by 4-stage Dickson oscillator architecture.
- Storage node capacitor: Crown-shaped stacked capacitor (C_s >= 25 fF to 30 fF, nominally 28 fF) with ONO or Ta2O5 / Al2O3 high-k dielectric (kappa > 15).
- Distributed RC mesh segmentation: Per-cell Pi/Tee network modeling poly/metal wordline resistance and gate-to-channel / gate-to-diffusion overlap capacitances across 256 to 512 cells per bitline/wordline sector.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- [docs/context3.yaml](../context3.yaml)

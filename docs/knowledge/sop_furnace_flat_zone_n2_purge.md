# Fused Quartz Tube Furnace N2 Pre-Purge, Thermal Flat-Zone Profiling & MFC Leak Rate Verification

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) covering fused quartz tube furnace conditioning prior to Forming Gas Anneal (FGA) and high-temperature thermal steps in the 180nm Open-Source DRAM process. Defines leak integrity checks, mass flow controller verification, high-purity nitrogen pre-purge dynamics, and 3-zone PID flat-zone profiling.

## Key Details / Architecture
- **Hardware Architecture**: Horizontal fused quartz process tube (OD 150–200 mm, 99.999% SiO2 purity), 3-zone resistive heating coils (Kanthal A1 / APM or MoSi2) divided into Source, Center, and Load zones.
- **Gas Manifold**: MFC-regulated ultra-pure N2 purge at 2.0 to 5.0 SLPM laminar sweep to prevent ambient back-diffusion.
- **Thermal Uniformity**: Digital triple-loop PID with dual Type-R / Type-S Pt-Pt/Rh thermocouples per zone maintaining $\le \pm 0.5^\circ\text{C}$ across the central 300–350 mm wafer boat flat zone (800°C–1200°C).
- **Mechanical Integrity**: Wafer boat push/pull speed limited to $< 50\text{ mm/min}$ to prevent crystallographic slip dislocations.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

# SOP: Folded Wordline Gate Poly Patterning & Shared Drain Node Placement

- **Date**: 2026-10-12
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for 180nm open-source DRAM folded wordline patterning and shared drain (bitline contact) node placement in an $8F^2$ cell architecture. This document defines step-by-step processing parameters and quantitative acceptance criteria derived from local literature.

## Key Details / Architecture
- Wordline gate length $L = 180\text{ nm}$, active channel width $W = 220\text{ nm}$.
- Gate dielectric: Dry thermal $\text{SiO}_2$ at 850°C–900°C with ~3.5 nm physical thickness.
- Wordline pitch: 360 nm to 400 nm.
- Shared drain node between adjacent cells connected to bitline via shared contact.
- Leakage target: $< 1\text{ fA/cell}$ at 85°C.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](.../../context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](.../../context2.yaml)

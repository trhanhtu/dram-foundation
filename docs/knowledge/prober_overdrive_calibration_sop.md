# SOP: Prober Stage Overdrive Stepping & Micro-Cantilever Alignment Calibration

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Proposed
- **Subsystem**: Electrical Die Sort (EDS) & Metrology
- **Node**: 180nm Open-Source DRAM Chip (DRAM Foundation VN)

## Overview & Rationale
Calibration protocol for micro-cantilever probe card alignment, planarity planarization, Z-touchdown sensing, and stage overdrive stepping on 180nm DRAM test pads to ensure low contact resistance (<1.5 Ω) without punching through thin top-metal or damaging BEOL dielectric layers.

## Key Details / Architecture
- Micro-cantilever tip planarization across array within ≤ 3.0 µm.
- Optical theta-XY alignment with pattern recognition targeting alignment tolerance ≤ 2.0 µm (within Gen 2 ±5 µm tolerance).
- Z-touchdown detection threshold at 0.5 µm stepping intervals.
- Overdrive step calibrated to nominal 50.0 µm (range 40.0 - 60.0 µm) with controlled scrub trace length of 10.0 - 15.0 µm.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/knowledge/prober_overdrive_calibration_sop.md](./docs/knowledge/prober_overdrive_calibration_sop.md)

# Microstrip & Stripline Route Execution with Serpentine Skew-Matched Length Tuning

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented

## Overview & Rationale
High-speed ATE DUT loadboard routing for the 180nm DRAM test vehicle requires deterministic propagation delay and controlled characteristic impedance across high-speed signals (DQ, DQS, Address/Command, Clock). Mismatches across byte lanes distort setup/hold margins during JEDEC DDR speed-bin qualification and HTOL burn-in characterization. This SOP establishes physical layer geometries, serpentine meander tuning rules, and return path constraints.

## Key Details / Architecture
- Layer Stackup: Symmetrical 12-layer high-Tg low-loss PCB substrate (Isola FR408HR / Megtron 6).
- Controlled Impedance: 50 Ohm +/- 10% single-ended microstrip/stripline, 100 Ohm +/- 10% differential pairs.
- Serpentine Tuning: Trombone/accordion patterns with spacing S >= 3W (or 4W in dense striplines) to eliminate self-coupling and pseudo-velocity acceleration.
- Return Ground: Continuous reference ground planes without antipad slot crossing; ground stitching vias spaced < lambda/10 (<= 1.0 mm) alongside layer transitions.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/knowledge/ate_dut_loadboard_routing_sop.md](./docs/knowledge/ate_dut_loadboard_routing_sop.md)

# Micro-Knowledge: High-Frequency C-SAM Pulse-Echo Scanning Recipe Execution for Leadframe & Die Attach Interface

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the C-Mode Scanning Acoustic Microscopy (C-SAM) pulse-echo inspection recipe for packaged 180nm DRAM dies (TSOP-54 / 54-ball FBGA). Focuses on detecting interface delamination and void formation between the silicon die, silver-filled conductive epoxy die attach (Ablebond 84-1LMIS), and leadframe paddle/substrate.

## Key Details & Process Specifications
- **Coupling Medium**: Deionized water degassed to prevent false void artifacts.
- **A-Scan Gating**: Time-domain gating on the reflection peak at the die-to-die-attach and die-attach-to-leadframe interfaces; phase inversion detection indicates acoustic impedance drop (epoxy to air void).
- **Physical Targets**:
  - Total void area under die: `< 5%`
  - Silver-filled epoxy cure verification baseline: `150°C` for `60 minutes`
  - Post-assembly thermal resistance target: `R_th <= 5°C/W`

## References & Related Files
- [Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging](./docs/sop_csam_die_attach_inspection.md)

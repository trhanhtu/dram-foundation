# SOP: Reference Die Acoustic Resolution Standard Verification & Delamination Gate Mapping

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the C-Mode Scanning Acoustic Microscopy (C-SAM) transducer calibration, time-of-flight (ToF) gating, and resolution verification for TSOP-54 / 54-ball FBGA packaged 180nm DRAM dies.

## Key Details / Metrology Metrics
- **Immersion Medium**: Degassed DI water at 25°C.
- **Reference Resolution Standard**: Acoustic calibration standard with known air void micro-cavities across 100 µm x 100 µm bonding pad zones.
- **Time-of-Flight Gate Mapping**:
  - G1: Mold compound / die surface interface.
  - G2: Silicon substrate / die-attach epoxy interface (Ablebond 84-1LMIS cured at 150°C, 60 min).
  - G3: Die-attach / leadframe/substrate interface.
- **Acceptance Criteria**:
  - Total die-attach void area: < 5.0%
  - Minimum wire pull strength correlation: >= 4.0 gf
  - Thermal resistance compliance: R_th <= 5.0 °C/W
  - Resolvable pad feature pitch: 100 µm x 100 µm square pad acoustic delineation

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

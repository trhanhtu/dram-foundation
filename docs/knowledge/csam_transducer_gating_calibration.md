# High-Frequency C-SAM Transducer Setup & Gating Calibration

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for setting up high-frequency scanning acoustic microscopy (C-SAM), focal plane alignment, and time-of-flight (ToF) gating to non-destructively evaluate epoxy plastic encapsulation, die attach integrity, and internal interfacial delamination in 180nm DRAM TSOP-54 / 54-ball FBGA packages.

## Key Details / Architecture
- **Acoustic Coupling**: Degassed DI water bath maintained at 25°C.
- **Transducer Alignment**: High-frequency acoustic transducer focused across the mold compound-to-silicon and silicon-to-die-attach interfaces.
- **Signal Gating & Phase Inversion**: Time-of-flight gating isolated to the die-attach interface (Ablebond 84-1LMIS cured at 150°C for 60 min). Delamination and voids identified via phase inversion (180° acoustic phase flip from positive to negative reflection polarity due to lower acoustic impedance of air/void).
- **Acceptance Metrics**:
  - Die attach void area < 5% via acoustic microscopy.
  - Package thermal resistance $R_{th} \le 5^\circ\text{C/W}$.
  - Aluminum bonding pad dimensional integrity over $100\,\mu\text{m} \times 100\,\mu\text{m}$ pads.
  - Wire pull strength $\ge 4.0\,\text{grams-force}$ for $25\,\mu\text{m}$ wire.

## References & Related Files
- [`docs/context.yaml`](./docs/context.yaml)
- Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging

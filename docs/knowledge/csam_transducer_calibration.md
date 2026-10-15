# CSAM Transducer Calibration & Acoustic Impedance Setup (180nm DRAM Packaging)

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for Confocal Scanning Acoustic Microscopy (C-SAM) setup, transducer focal length calibration, and acoustic impedance boundary gating. Designed to inspect die attach epoxy encapsulation integrity (e.g. Ablebond 84-1LMIS cured at 150°C) and wire bond pad interfaces (100 µm × 100 µm aluminum pads) for 180nm DRAM chips packaged in TSOP-54 / 54-ball FBGA packages.

## Key Operational & Calibration Parameters
1. **Coupling Medium**: Degassed deionized (DI) water maintained at 25°C room ambient to prevent thermal acoustic velocity drift.
2. **Acoustic Impedance Boundary Calibration**:
   - Die attach interface: Silicon substrate ($Z_{\text{Si}} \approx 19.7 \times 10^6 \, \text{Rayl}$) to silver-filled conductive epoxy ($Z_{\text{epoxy}} \approx 3.0\text{--}5.5 \times 10^6 \, \text{Rayl}$).
   - Delamination / Void interface: Solid to air/vacuum ($Z_{\text{air}} \approx 400 \, \text{Rayl}$), generating a near 100% phase-inverted echo reflection.
3. **Acceptance Thresholds**:
   - Total void area under the die attach: $< 5\%$.
   - Die attach thermal resistance: $R_{\text{th}} \le 5^\circ\text{C/W}$.
   - Wire pull strength post-inspection baseline: $\ge 4.0 \, \text{gf}$ (Mil-Std-883 Method 2011).
   - Bond pad geometry: $100 \, \mu\text{m} \times 100 \, \mu\text{m}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- Source: *Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging*
- Source: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*

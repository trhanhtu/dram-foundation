# SOP: Interferometer Optical Setup & Kinematic Mirror Mount Procurement

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Proposed
- **Node Context**: 180nm Open-Source DRAM Chip > 1T1C DRAM Cell Topology & Layout (8F²) > 1T1C Access Transistor & Bitline Contact Layout DRC/LVS Design (8F²) > Precision Tooling & Fixturing > Interferometric Kinematic Fixture Calibration & Runout Metrology Validation > Interferometer Optical Setup & Kinematic Mirror Mount Procurement
- **Generation**: Gen 2 (µm)
- **Action Type**: Buy (COTS Precision Hardware)

## Overview & Rationale
To support precision photolithography tooling alignment for 180nm 1T1C DRAM cell fabrication and validate fixture runout metrology at Gen 2 (µm), precision optical hardware must be commercially procured (COTS). High-stability kinematic mirror mounts and an interferometer optical setup enable non-contact interferometric verification of gap control (0.1 µm resolution) and fiducial alignment within Gen 2 tolerances (±5 µm).

## Workflow Architecture
```text
┌───────────────────────┐
│                       │
│      Procurement      │
│     Specification     │
│      Definition       │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│   Optical Element &   │
│  Kinematic Mount BOM  │
│     Verification      │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│   Vendor Quality &    │
│  Metrology Rigidity   │
│         Audit         │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│  Delivery & Baseline  │
│  Interferometric QA   │
│      Validation       │
│                       │
└───────────────────────┘
```

## Key Details / SOP Steps
1. **Procurement Specification Definition**: Define technical requisites for high-precision optical mounts, beam splitters, and reference mirrors capable of supporting Gen 2 alignment tolerances (±5 µm) and gap control sensitivity down to 0.1 µm.
2. **COTS Bill of Materials (BOM) Compilation**:
   - High-stability kinematic mirror mounts with 2-axis tip/tilt adjustment featuring sub-micron or differential micrometer adjustment screws (<0.1 µm sensitivity).
   - Optical flat reference mirrors with surface flatness rating compatible with i-line/visible inspection.
   - Laser diode or interferometer source mount compatible with 365nm UV / visible alignment lasers.
3. **Vendor Qualification & Kinematic Rigidity Audit**: Screen precision mechanical optics vendors (e.g., Thorlabs, Newport, Edmund Optics, or local equivalent distributors) to ensure drift-free kinematic springs, hardened carbide/sapphire contact seats, and zero-backlash fine-pitch adjustment screws.
4. **Incoming Inspection & Bench Acceptance Test**:
   - Inspect components for cosmetic surface imperfections, burrs, and thread runout.
   - Mount optical components on a granite surface plate or damped optical breadboard.
   - Validate pitch/yaw sensitivity and backlash against manufacturer specifications using dial indicators / differential micrometer gauges.

## Machine-Measurable Acceptance Criteria
- **Actuator/Gap Control Sensitivity**: $\le 0.1\ \mu\text{m}$ resolution (achieved via differential micrometer or closed-loop piezo adjustment).
- **Kinematic Fixture Alignment Tolerance**: $\le \pm 5\ \mu\text{m}$ alignment runout validation across Gen 2 operational travel.
- **Proximity Gap Metrology Range**: $10\ \mu\text{m}$ to $20\ \mu\text{m}$ calibrated clearance verification for non-contact proximity printing mode.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose](./sop-interferometer-procurement.md)
- [Sam Zeloof Z1 Garage Semiconductor Journal (2018)](./sop-interferometer-procurement.md)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./sop-interferometer-procurement.md)

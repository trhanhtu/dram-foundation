# Post-OPC Reticle Critical Dimension Measurement & Feature Pitch Verification

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council)
- **Status**: Accepted

## Overview & Rationale
Standard Operating Procedure (SOP) for Gen 3 (nm scale) metrology verification on 5x reduction reticles designed for 180nm open-source DRAM tapeouts. Post-Optical Proximity Correction (OPC) reticles require sub-micron optical dimension tracking and feature pitch validation across quartz plates before exposure release to prevent printability faults and line-end pullback.

## Key Details / Metrology Architecture
1. **Mechanical & Isolation Stability**:
   - Rigidity provided via extruded aluminum 4040 frame and MGN12H precision ground guide rails (< 5 µm / 100 mm straightness).
   - Low-frequency damping (> 30 Hz) with sorbothane/neoprene isolation pads.
   - Closed-loop stage positioning with 1 µm resolution linear magnetic or optical scales.
2. **Optics & Alignment**:
   - Dual split-field optical inspection setup (5x, 10x, 20x objectives) or 10x Plan Achromat objective (NA 0.25) paired with high-resolution CMOS imaging.
   - Planar parallelism compensation (< 1 µm across stage) via air-bearing spherical leveling / WEC mechanics.
3. **Acceptance Criteria Targets**:
   - Stage straightness: < 5 µm per 100 mm travel.
   - Stage closed-loop linear positioning resolution: 1 µm.
   - Leveling / parallelism error: < 1 µm across 100 mm span.
   - 5x Reticle target CD (representing 180nm wafer features): 0.90 µm (900 nm).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

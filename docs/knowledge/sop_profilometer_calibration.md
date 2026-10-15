# Dual-Axis Optical & X-Ray Micro-CT Loop Profilometer Calibration

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Establishes standardized calibration procedures for dual-axis optical profilometry and high-resolution X-ray Micro-CT systems. This setup verifies wire bonding loop trajectories, loop heights, and clearance margins for 180nm DRAM open-source dies packaged in TSOP-54 / 54-ball FBGA configurations under MIL-STD-883 standards.

## Key Metrology & Dimensional Bounds
- **Bonding Wire Geometry**: 25 μm diameter 99.99% Au (thermosonic ball) or Al-1% Si (ultrasonic wedge).
- **Die Bond Pad Dimensions**: 100 μm × 100 μm aluminum pads.
- **Stage Positioning & Actuation**: Closed-loop piezo actuators with 0.1 μm sensitivity.
- **Mechanical Pull Threshold**: MIL-STD-883 Method 2011 requiring pull force $\ge 4.0\text{ gf}$ for 25 μm wire.
- **Void Area Acceptance**: Acoustic / X-ray void area under die $< 5\%$; thermal resistance $R_{th} \le 5^\circ\text{C/W}$.

## References & Related Files
- [Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging](./docs/knowledge/sop_profilometer_calibration.md)
- [Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose](./docs/knowledge/sop_profilometer_calibration.md)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/knowledge/sop_profilometer_calibration.md)

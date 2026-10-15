# High-Frequency C-SAM Acoustic Microscopy Void & Delamination Inspection

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Captures the operating parameters, calibration, gating, and acceptance thresholds for non-destructive Scanning Acoustic Microscopy (C-SAM) inspection of encapsulated 180nm DRAM packages (TSOP-54 / 54-ball FBGA). Ensures structural integrity of the die-attach interface (Ablebond 84-1LMIS cured at 150°C for 60 min) and encapsulation mold compound.

## Key Details & Physical Parameters
- **Couplant**: High-purity degassed deionized (DI) water bath.
- **Transducer**: High-frequency acoustic transducer (100 MHz – 230 MHz range, focal length ~0.25 to 0.5 inches) for resolving thin-film packaging layers.
- **A-Scan Gating**: Calibrated at the die-attach epoxy and leadframe interface. Phase inversion indicates acoustic impedance mismatch (solid-to-air boundary) representing voids or delamination.
- **Acceptance Threshold**:
  - Total void area under the die: `< 5%` total interface area via acoustic microscopy integration.
  - Thermal resistance: $R_{th} \le 5\text{ }^\circ\text{C/W}$.
  - Post-inspection drying: Vacuum bake at 100°C–125°C to eliminate absorbed DI water moisture before electrical sort.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging

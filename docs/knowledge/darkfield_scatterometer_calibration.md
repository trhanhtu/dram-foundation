# Darkfield Laser Scatterometer Sensitivity Calibration across PSL Particle Sizes

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
This standard operating procedure documents the optical sensitivity calibration of an automated darkfield laser scatterometer across Polystyrene Latex (PSL) sphere reference sizes. Accurately mapping scattered optical power to equivalent latex sphere diameter is essential for post-CMP defect metrology on 180nm/130nm process layers (e.g. poly gates, contact plugs, and inter-layer dielectrics), ensuring sub-micron defect excursion monitoring adheres to foundry critical dimension budgets.

## Key Details / Architecture
- **Calibration Standards**: Traceable PSL deposition standards matching key physical critical dimensions: 150 nm (minimum poly gate length), 170 nm (contact hole CD), 210 nm (poly spacing), and 340 nm (metal 1 pitch).
- **Measurement Geometry & Optics**: DUV (248 nm) or high-intensity narrow-band solid-state illumination incident at oblique angles, collecting wide-angle scattered light via high-NA collection optics to eliminate specular reflection.
- **Detector Response Mapping**: Photomultiplier tube (PMT) / avalanche photodiode (APD) integrated voltage pulse area calibrated using Rayleigh scattering cross-section scaling ($C_{scat} \propto d_p^6 / \lambda^4$).
- **Wafer Grid Integration**: Coordinate mapping aligned to 5 nm (0.005 µm) physical placement grid with 49-point reference checks.

## References & Related Files
- [Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology](./docs/knowledge/darkfield_scatterometer_calibration.md)
- [SkyWater SKY130 Open PDK Design Rules & Lithography Grid](./docs/knowledge/darkfield_scatterometer_calibration.md)
- [Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose](./docs/knowledge/darkfield_scatterometer_calibration.md)

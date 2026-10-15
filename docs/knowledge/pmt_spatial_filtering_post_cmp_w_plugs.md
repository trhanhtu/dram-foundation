# PMT Spatial Filtering Aperture and Gain Threshold Configuration for Post-CMP W-Plugs

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the calibrated spatial filtering aperture geometry and PMT (photomultiplier tube) gain detection thresholds for automated darkfield laser scatterometry on post-CMP tungsten (W) contact plugs in 180nm/130nm open-source DRAM fabrication.

## Key Details / Architecture
- **Lithography & Feature Grid**: Aligned to SkyWater SKY130 manufacturing grid (0.005 µm / 5 nm) with minimum contact hole dimensions of 0.17 µm × 0.17 µm and overlay tolerance budget $\le 35\text{ nm}$.
- **Diffraction Suppression**: Spatial Fourier-plane aperture mask blocks the periodic specular diffraction array orders from dense contact arrays (pitch matching 0.34 µm - 0.36 µm patterns).
- **PMT Voltage & Sensitivity Calibration**: Calibrated using standard 9-point or 49-point wafer mapping across radial zones to decouple CMP slurry micro-scratches and residual tungsten from background dielectric roughness.

## References & Related Files
- [docs/context.yaml](..../../context.yaml)
- [docs/context2.yaml](..../../context2.yaml)

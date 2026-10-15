# High-Magnification CD-SEM Top-Down Image Acquisition & Edge Digitization Recipe Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operational sequence and digitization recipe for in-line Critical Dimension Scanning Electron Microscopy (CD-SEM) metrology on 180nm open-source DRAM cell access gates and SkyWater SKY130 poly gates.

## Key Details / Architecture
- **Stage & Beam Setup**: Low landing energy (<800 eV, nominal 500 eV) to prevent resist shrinking and charge build-up.
- **Physical Grid Placement**: Pixel quantization aligned to the SKY130 manufacturing grid ($0.005\,\mu\text{m} = 5\,\text{nm}$).
- **Edge Digitization**: Maximum secondary electron (SE) intensity gradient thresholding along the line profile.
- **Metrology Verification**: Target nominal gate length $L = 180\,\text{nm}$ (access transistor), minimum poly gate length $150\,\text{nm}$, active diffusion $150\,\text{nm}$, contact hole $170\,\text{nm} \times 170\,\text{nm}$, and maximum overlay error $\le 35\,\text{nm}$.

## References & Related Files
- [SKY130 Design Rules Context](file:///d:/coding/dram/docs/context.yaml)

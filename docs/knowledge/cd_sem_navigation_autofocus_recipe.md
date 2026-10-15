# Automated Low-Dose Multi-Point Navigation & Autofocus Calibration Recipe Programming

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Low-dose multi-point navigation and autofocus calibration standard operating procedure for in-line Critical Dimension Scanning Electron Microscopy (CD-SEM) verification of 180nm DRAM cell gate arrays and SkyWater SKY130-compatible transistor architectures. Minimizes photoresist shrinkage and beam-induced charge distortion while securing nanoscale alignment repeatability.

## Key Details & Specifications
- **Physical Grid Snap**: 0.005 µm (5 nm manufacturing grid).
- **Target Topologies**: 180nm DRAM access transistor channel length ($L = 180\text{ nm}$), active width ($W = 220\text{ nm}$), and minimum drawn poly gate length of 150 nm (spacing $\ge 0.21\text{ µm}$).
- **Metrology Overlay Margin**: $\le 35\text{ nm}$ maximum permissible overlay between gate poly and active diffusion.
- **Beam Protection**: Multi-point off-site autofocus and stigmation routine separated from the target array to avoid line shrinkage in sub-200nm resist profiles.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

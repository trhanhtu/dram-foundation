# 3D Topography Extraction and Plug Recess/Dishing Metrology Analysis

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Actionable Standard Operating Procedure (SOP) for 3D Topography Extraction and Plug Recess/Dishing Metrology Analysis in the 180nm Open-Source DRAM process (DRAM Foundation VN). Following Tungsten (W) chemical-mechanical planarization (CMP) of bitline contact and storage node contact plugs, nanoscale AFM profilometry is mandatory to extract plug recess, inter-layer dielectric (ILD) dishing, and erosion across dense array patterns.

## Metrology Workflow & Specs
- AFM Mode: Tapping Mode (Intermittent Contact) with high-aspect-ratio silicon tip (tip radius < 10 nm, cone half-angle <= 10°).
- Scan Dimensions: 2.0 um x 2.0 um, resolution 512 x 512 pixels across 180nm DRAM dense bitline contact and storage node plug matrices (pitch 360 nm - 400 nm).
- Image Corrections: First-order tilt plane correction, line-by-line zero-order polynomial flattening excluding recessed plug mask areas.
- Automated Extraction: Step-height cross-sectional profiling across the oxide dielectric plane down to the center of the W-plug.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

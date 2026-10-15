# Automated Full-Wafer Dicing Street Scan, Die Chipping Quantification & Electronic Wafer Map Binning

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure (SOP) for post-saw automated optical inspection (AOI) across dicing streets for 180nm DRAM wafers on dicing film frames. Quantifies kerf width variation, silicon chipping intrusions toward the seal ring and active circuitry, and classifies dies directly into digital wafer maps (SEMI G85 / SECS-GEM XML) to ensure mechanical integrity prior to die attach pick-and-place.

## Key Details / Architecture
- **Alignment Grid & Positioning**: Optical alignment using wafer notch/flat and global fiducials registered to the physical placement grid resolution of 0.005 µm (5 nm).
- **Inspection Illumination**: Multi-channel brightfield (normal coaxial LED) and darkfield (high-angle oblique illumination) imaging to resolve silicon micro-cleavage, chipping, and kerf edge delamination down to sub-micron scales.
- **Defect Metrics**:
  - Dicing Street Kerf Width: 35.0 µm nominal kerf line width.
  - Maximum Allowable Chipping Extent: <= 15.0 µm from street edge (maintaining > 15.0 µm clearance to die seal ring).
  - Kerf Centerline Tracking Error: <= 3.5 µm drift across full wafer span.
  - Active Area Encroachment: 0 tolerance for cracks propagating into active silicon or seal ring metallization.
- **Electronic Map Binning**: Ingests incoming wafer map (wafer sort CP1/CP2), overlays visual defect classification, assigns Bin 7 (Mechanical Chipping / Visual Reject), and transmits via SEMI G85 / SECS-GEM XML to pick-and-place sorters.

## References & Related Files
- [docs/context.yaml](../../context.yaml)
- [docs/context2.yaml](../../context2.yaml)
- [docs/context3.yaml](../../context3.yaml)

# Micro-Knowledge: Automated Micro-Scratch Defect Metrology for 180nm ILD Post-CMP

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Council)
- **Status**: Implemented

## Overview & Rationale
In 180nm CMOS/DRAM manufacturing (Gen 3 nm-scale), Inter-Layer Dielectric (ILD) Chemical Mechanical Planarization (CMP) removes topography prior to contact lithography and tungsten plug (W-plug) formation. Micro-scratches induced by CMP slurry agglomerates or pad debris can bridge adjacent memory access transistor features (channel length L = 180 nm, width W = 220 nm) or cause leakage across stacked capacitor contacts. Automated micro-scratch defect thresholding and spatial density quantification via Tapping-Mode Atomic Force Microscopy (AFM) and automated spectroscopic ellipsometry mapping establishes strict planarization gate quality control.

## Key Technical Specifications
- **Metrology Integration**: Cross-correlates automated 9-point/49-point wafer mapping (ellipsometry) with high-resolution localized tapping-mode AFM scans.
- **Defect Segmentation Threshold**: Micro-scratch depth thresholded relative to ILD RMS roughness (Sq) and access channel geometry (depth >= 3.5 nm, corresponding to gate oxide equivalent thickness, with scratch length >= 180 nm).
- **Physical Acceptance Targets**:
  - Scratch depth threshold: <= 3.5 nm.
  - Spatial scratch defect density: < 0.2 defects/cm^2.
  - Baseline surface roughness Sa / Sq: <= 0.2 nm (post-CMP ILD).
  - Spatial mapping grid: Automated 49-point wafer mapping.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- Verified Local Literature: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
- Verified Local Literature: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*

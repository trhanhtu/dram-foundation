# SOP: Brightfield Optical & Laser Darkfield Automated Surface Micro-Scratch / Slurry Residue Defectivity Inspection

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Process Tier**: 180nm Open-Source DRAM Chip (Gen 3 nm) / SkyWater SKY130 Alignment

## Overview & Rationale
Defect inspection following Inter-Layer Dielectric (ILD) Oxide Chemical Mechanical Planarization (CMP) is vital to identify residual slurry abrasive clusters and polishing-induced micro-scratches before subsequent metallization or contact etching. Unmitigated slurry residue or micro-scratches exceeding critical layer dimensions cause short-circuits across tight metal/poly pitches or cause contact open failures.

## Inspection Workflow Architecture

```text
┌───────────────────────┐
│                       │
│   Post-CMP DI Water   │
│   Rinse & Megasonic   │
│         Clean         │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Wafer Alignment &   │
│  5nm Grid Coordinate  │
│     Registration      │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│    Laser Darkfield    │
│   High-Speed Defect   │
│       Scanning        │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Brightfield Optical  │
│    Defect Review &    │
│    Classification     │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│      Acceptance       │
│  Verification & Lot   │
│      Disposition      │
│                       │
└───────────────────────┘
```

## Step-by-Step Procedure
1. **Pre-Inspection Surface Preparation**:
   - Ensure the polished ILD wafer has completed post-CMP scrubber/megasonic clean and a rigorous deionized (DI) water rinse.
   - Load wafer onto the vacuum chuck of the automated inspection station under cleanroom Class 1/10 conditions.

2. **Stage Alignment and Manufacturing Grid Registration**:
   - Perform automated notch/flat alignment and optical global fiducial alignment.
   - Register inspection coordinates directly against the foundry physical placement manufacturing grid resolution of **0.005 µm (5 nm)**.
   - Validate stage placement repeatability within the manufacturing grid constraint.

3. **High-Speed Laser Darkfield Surface Scanning**:
   - Engage darkfield laser illumination to detect Rayleigh scattering from surface micro-imperfections, scratches, and slurry nanoparticle aggregates.
   - Execute a spiral/raster scan across the entire wafer surface with full 49-point wafer mapping coverage to detect radial slurry residue patterns.
   - Capture defect polar coordinates $(r, \theta)$ and mapped scatter intensities.

4. **Automated High-Resolution Brightfield Defect Review**:
   - Direct the optical inspection turret to high-scattering coordinates flagged during darkfield scanning.
   - Illuminate using DUV/i-line wavelengths (248 nm KrF or 365 nm i-line) with a high-NA objective ($NA = 0.65$ or $NA = 0.25$ review) to resolve fine morphology.
   - Classify defects into:
     - **Micro-Scratches**: Linear abrasions across dielectric surfaces.
     - **Slurry Residues**: Concentrated particulate clusters or residual chemical binding.

5. **Defect Sizing and Layer Critical Dimension Comparison**:
   - Measure scratch width and depth against Metal 1 critical dimension (**0.14 µm / 140 nm**) and contact hole dimension (**0.17 µm × 0.17 µm / 170 nm**).
   - Flag any defect that spans or bridges the minimum poly gate spacing (**0.21 µm / 210 nm**).

## Critical Thresholds

```text
Defectivity & Metrology Critical Dimensions (nm)
                    ┌──────────────────────────────────┐
                    │░░░░░░░░                          │
Overlay Registration┤░░░░░░░░                          │
                    │▒▒                                │
 Stage Repeatability┤▒▒                                │
 Micro-Scratch Width┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      │
                    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      │
 Slurry Residue Size┤██████████████████████████████████│
                    │██████████████████████████████████│
                    └┬───────┬────────┬───────┬───────┬┘
                    0.0    42.5     85.0    127.5 170.0 
```

## Acceptance Criteria
1. **Residual Slurry Aggregate Size**: Maximum particle/cluster size on post-CMP ILD surface must be $< 0.17\,\mu\text{m}$ ($< 170\,\text{nm}$, below contact hole dimension $0.17\,\mu\text{m} \times 0.17\,\mu\text{m}$) across all mapped sites.
2. **Surface Micro-Scratch Critical Width**: Maximum micro-scratch width must be $< 0.14\,\mu\text{m}$ ($< 140\,\text{nm}$, strictly below Metal 1 minimum width) and scratch length $< 5\,\mu\text{m}$.
3. **Wafer Inspection Coordinate Registration Error**: Defect stage placement and coordinate repeatability registration error must be $\le 0.005\,\mu\text{m}$ ($5\,\text{nm}$, aligned with physical manufacturing grid resolution) and within the overlay budget $\le 35\,\text{nm}$.
4. **Surface Defect Density**: Surface defect density (slurry residue + scratches) across automated 49-point wafer mapping must be $< 0.05\,\text{defects/cm}^2$.

## Context References
- **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**: Physical placement grid resolution $0.005\,\mu\text{m}$ ($5\,\text{nm}$); minimum poly gate spacing $0.21\,\mu\text{m}$; minimum contact hole dimension $0.17\,\mu\text{m} \times 0.17\,\mu\text{m}$; Metal 1 minimum width $0.14\,\mu\text{m}$; maximum permissible overlay error $\le 35\,\text{nm}$; DUV $248\,\text{nm}$ KrF ($NA=0.65$) and i-line $365\,\text{nm}$.
- **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**: Automated 49-point wafer mapping methodology for radial uniformity and defect tracking.
- **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**: Post-process DI water rinse protocol and optical inspection magnification mechanics.

# W Removal Rate and Surface Defectivity Post-CMP Metrology

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operational procedure (SOP) for post-CMP metrology targeting Tungsten (W) overburden removal rate, within-wafer non-uniformity (WIWNU), and surface defectivity (scratches, residue, plug coring/dishing) for the 180nm DRAM process line (Gen 3). This step is critical prior to stacked capacitor over bitline (COB) or metal-insulator-metal (MIM) plug formation to ensure low contact resistance and prevent alpha/soft-error leakage.

## Key Details / Architecture
- **Metrology Steps**:
  1. Film Thickness / Removal Rate mapping via 49-point 4-point probe (4PP) or X-ray Fluorescence (XRF) on blanket monitor wafers.
  2. Removal rate calculation: $RR = (T_{pre} - T_{post}) / t_{polish}$ and WIWNU $1\sigma \le 5\%$.
  3. Laser darkfield surface defectivity inspection (> 0.18 µm particle sensitivity).
  4. Topography / Plug Coring verification using CD-SEM and Atomic Force Microscopy (AFM).
- **Physical Specifications**:
  - W Plug Contact: Shared bitline contact for access transistor ($L = 180\text{ nm}$, $W = 220\text{ nm}$).
  - Contact Resistivity: Measured via TLM structures with rectangular pads ($W = 100\ \mu\text{m}$, $L_{pad} = 50\ \mu\text{m}$) across gaps $d \in \{5, 10, 20, 40, 80\}\ \mu\text{m}$.

## References & Related Files
- [docs/context.yaml](..../../context.yaml)
- [docs/context2.yaml](..../../context2.yaml)
- [docs/context3.yaml](..../../context3.yaml)

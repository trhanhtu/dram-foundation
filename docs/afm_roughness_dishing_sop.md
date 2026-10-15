# Micro-Knowledge: AFM Surface Micro-Roughness and DRAM Dense Array Dishing/Erosion Profiling SOP

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for Atomic Force Microscopy (AFM) surface metrology following Inter-Layer Dielectric (ILD) and Tungsten (W) plug Chemical Mechanical Planarization (CMP) on the 180nm Open-Source DRAM process. Metrology quantifies nanoscale ILD micro-roughness ($R_q$, $R_a$) and array-level dishing/erosion across dense 1T1C memory arrays ($8F^2$ / $6F^2$ architecture with $360\text{ nm}$ to $400\text{ nm}$ bitline/wordline pitch).

## Key Physical Bounds & Metrology Correlation
- **Cell Geometry Constraints**: Bitline & wordline pitch of $360\text{ nm} - 400\text{ nm}$; access transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$; W-plug drain contacts beneath stacked capacitors.
- **AFM Probe Requirements**: High-aspect-ratio silicon tip (tip radius $< 5\text{ nm}$, cone angle $< 15^\circ$) operating in tapping/non-contact mode to resolve intra-array tungsten plug recess and oxide erosion without tip damage.
- **Topography Targets**:
  - ILD Oxide Surface Micro-Roughness: $R_q \le 0.40\text{ nm}$ ($R_a \le 0.30\text{ nm}$).
  - Dense Array CMP Dishing / Thinning: $\Delta z \le 25\text{ nm}$ across $50\ \mu\text{m} \times 50\ \mu\text{m}$ array window.
  - W-Plug Recess / Protrusion: $\Delta h_{\text{plug}} \le 15\text{ nm}$ over $180\text{ nm} - 220\text{ nm}$ contact structures.
  - Array Boundary Oxide Step Height / Erosion: $\Delta z_{\text{erosion}} \le 20\text{ nm}$.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](.../context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](.../context2.yaml)

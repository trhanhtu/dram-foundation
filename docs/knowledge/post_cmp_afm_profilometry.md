# Micro-Knowledge: Post-CMP AFM Dishing, Erosion & RMS Roughness Profilometry (180nm DRAM)

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Metrology Council)
- **Status**: Implemented

## Overview & Rationale
In the 180nm open-source DRAM architecture (stacked capacitor over bitline / COB topology), tungsten plug (W-plug) CMP and inter-layer dielectric (ILD) oxide planarization are critical prerequisites for subsequent capacitor bottom-electrode crown formation and metallization. Excessive tungsten dishing or field oxide erosion impairs contact resistance and leads to stacked capacitor lithography depth-of-focus (DOF) margin failure. This document defines the standard AFM metrology protocol for dishing, array erosion, and surface micro-roughness characterization.

## Key Details & Metrics
- **Cantilever**: High-aspect-ratio silicon tip (tip radius $R_{tip} \le 7\text{ nm}$, half-cone angle $\le 10^\circ$, resonance frequency $f_0 \approx 300\text{ kHz}$, spring constant $k \approx 40\text{ N/m}$).
- **Mode**: Non-contact / Intermittent Contact (Tapping Mode) to prevent tip blunting and surface scratching.
- **Scan Areas**:
  - Global ILD surface micro-roughness: $5\,\mu\text{m} \times 5\,\mu\text{m}$, 512×512 pixels at $0.5\text{ Hz}$.
  - W-Plug contact dishing: $2\,\mu\text{m} \times 2\,\mu\text{m}$ centered over $L=180\text{ nm}, W=220\text{ nm}$ contacts.
  - Dense array erosion: $40\,\mu\text{m} \times 10\,\mu\text{m}$ line profiles across active memory array into field oxide.
- **Acceptance Thresholds**:
  - ILD RMS surface micro-roughness ($R_q$): $\le 0.35\text{ nm}$.
  - W-Plug dishing ($D_{plug}$): $\le 18.0\text{ nm}$.
  - Dense array erosion ($E_{array}$): $\le 22.0\text{ nm}$.
  - Post-CMP step height delta across array boundary: $\le 25.0\text{ nm}$.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](../../context.yaml)
- [`docs/knowledge/post_cmp_afm_profilometry.md`](./docs/knowledge/post_cmp_afm_profilometry.md)

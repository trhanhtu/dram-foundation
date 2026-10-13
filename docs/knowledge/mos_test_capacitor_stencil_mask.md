# MOS Test Capacitor Stencil Shadow Mask Design & Micro-Machining

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Detailed standard operating procedure (SOP) and engineering specifications for designing and micro-machining physical shadow stencil masks (Gen 2: µm scale) for top-electrode metallization of MOS test capacitors. These capacitor arrays enable spectroscopic ellipsometry correlation and C-V profiling of high-k gate dielectric stacks (target EOT ~3.5 nm, dry thermal SiO2 at 850°C–900°C) for the 180nm open-source DRAM fabrication line.

## Key Details / Architecture
- Stencil material: Ultra-flat Invar / 304 Stainless steel foil (50 µm thickness).
- Aperture array: Micromachined circular/square pad apertures (Gen 2: 100 µm to 500 µm diameter) matching split-field dual CMOS alignment microscope requirements.
- Acceptance criteria aligned with 180nm node metrics: minimum 28 fF capacitance budget, <= 1 fA/cell leakage target at 85°C, and gate oxidation parameters.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/sop_mos_capacitor_stencil_shadow_mask.md](../sop_mos_capacitor_stencil_shadow_mask.md)

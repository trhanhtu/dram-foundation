# Active-to-Poly Overlap & Pitch DRC Rule Deck Verification

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines physical layout design rule check (DRC) verification steps for the 180nm 8F² folded bitline DRAM unit cell array, focusing on access transistor gate poly (Wordline), active diffusion geometry, active-to-poly overlap/endcaps, and periodic wordline pitch.

## Key Details / Architecture
- **Active Channel Length ($L$)**: 180 nm.
- **Active Channel Width ($W$)**: 220 nm.
- **Wordline Pitch**: 360 nm to 400 nm.
- **Layout Topology**: 8F² folded bitline with shared bitline contact between adjacent access transistors.
- **DRC Rules Enforced**: Channel length/width integrity, minimum active extension beyond gate, gate poly endcap overlap, and wordline pitch regularity.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

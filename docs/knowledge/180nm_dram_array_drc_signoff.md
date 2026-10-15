# Micro-Knowledge: 180nm DRAM High-Density Array DRC Sign-Off

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Sign-off DRC methodology for an open-source 180nm 1T1C DRAM chip targeting commercial MPW runs. High-density memory arrays require strict pitch matching, access transistor gate alignment, and tungsten plug contact enclosure verification to prevent yield loss.

## Key Details / Architecture
- **Cell Geometry**: 8F² folded bitline footprint (0.259 µm² at F = 180 nm).
- **Access Transistor**: L = 180 nm, W = 220 nm.
- **Array Wiring Pitch**: Wordline & Bitline pitch between 360 nm and 400 nm.
- **Storage Node Stack**: Stacked Capacitor Over Bitline (COB) Crown or MIM structure via Tungsten plug (W-plug).
- **Dielectric Target**: ONO or Ta2O5 / Al2O3 high-k stack (EOT 3–4 nm, κ > 15) delivering nominal Cs = 28 fF (≥ 25 fF).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

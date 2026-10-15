# 2D Bitline/Wordline Physical Bitmap Failure Coordinate Mapper & Defect Logger Engine

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Captures March C- test failures and converts logical row/column addresses into exact physical micron coordinates for 180nm 1T1C DRAM cells configured in an $8F^2$ folded bitline topology with stacked capacitors over bitlines (COB).

## Key Details / Architecture
- Unit Cell Footprint: $8F^2 = 0.259\,\mu\text{m}^2$ ($F = 0.18\,\mu\text{m}$).
- Dimension Pitch: $\Delta X = 2F = 0.36\,\mu\text{m}$ (Bitline pitch), $\Delta Y = 4F = 0.72\,\mu\text{m}$ (Wordline pitch).
- Shared bitline contacts between adjacent memory cells with W-plug drain connections.
- Defect signatures categorized into single-cell, bitline stuck-at/leakage, wordline opens/leakage, and 2D spatial clusters.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

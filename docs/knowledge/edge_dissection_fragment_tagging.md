# Edge Dissection & Multi-Property Fragment Tagging Rule Deck Synthesis

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for synthesizing edge dissection and multi-property fragment tagging rule decks for 180nm open-source DRAM chip critical layers (Active Diffusion, Poly Gate, Contact). Ensures accurate Edge Placement Error (EPE) control and optical proximity correction across DUV KrF lithography constraints.

## Key Details / Architecture
- Physical placement grid snap: 0.005 µm (5 nm).
- Access transistor channel target: length L = 180 nm, width W = 220 nm.
- Minimum gate pitch / spacing: 210 nm spacing, 150 nm minimum drawn poly gate length, 150 nm active width.
- Multi-property fragment tagging: line-ends, convex/concave corners, channel regions, contact borders (0.17 µm x 0.17 µm).
- Overlay error budget constraint: <= 35 nm.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

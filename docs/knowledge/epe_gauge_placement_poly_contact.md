# Micro-Knowledge: EPE Gauge Placement & Process Window Corner Setup for Poly/Contact Layers

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Council)
- **Status**: Implemented

## Overview & Rationale
Defines the edge placement error (EPE) gauge seeding strategy and multi-corner process window (PW) setup for 248nm KrF DUV optical proximity correction (OPC) and litho rule checking (ORC) on 180nm DRAM access transistors and contact layers.

## Key Details / Architecture
- **Lithography Platform**: DUV 248 nm KrF excimer stepper, NA = 0.65, k1 = 0.40, minimum resolvable half-pitch = 152 nm.
- **Physical Grid**: 0.005 µm (5 nm) placement resolution.
- **CD Targets**:
  - Minimum drawn poly gate length: 150 nm (0.15 µm).
  - DRAM access transistor channel length: L = 180 nm, width W = 220 nm.
  - Contact hole size: 0.17 µm x 0.17 µm (170 nm x 170 nm).
  - Minimum poly gate spacing: 0.21 µm (210 nm).
  - Maximum poly-to-active overlay budget: <= 35 nm.
- **Process Window Matrix**: 5-point corner setup (Nominal, Max Dose / Positive Defocus, Min Dose / Negative Defocus, Max Dose / Negative Defocus, Min Dose / Positive Defocus).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/knowledge/epe_gauge_placement_poly_contact.md](./docs/knowledge/epe_gauge_placement_poly_contact.md)

# Automated DRC Pitch Metrology & Calibration Rule Deck Execution

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for automated design rule check (DRC) pitch metrology and calibration deck execution in the 180nm Open-Source DRAM Chip architecture (DRAM Foundation VN). Ensures geometric fidelity, overlay limits, and lithographic manufacturability across critical active, polysilicon, contact, and metal layers prior to tapeout.

## Key Details / Architecture
- **Manufacturing Grid**: 0.005 µm (5 nm) placement snap grid.
- **Critical Dimensions (CD)**:
  - Minimum active diffusion width: 0.15 µm (150 nm).
  - Minimum poly gate length: 0.15 µm (150 nm).
  - Minimum poly gate spacing: 0.21 µm (210 nm).
  - Contact hole dimension: 0.17 µm × 0.17 µm.
  - Metal 1 pitch: >= 0.34 µm (minimum width: 0.14 µm).
- **Overlay Budget**: Maximum permissible poly-to-active overlay error <= 35 nm.
- **Process Window**: Rayleigh half-pitch resolution R = 152 nm (DUV KrF 248 nm laser, NA = 0.65, k1 = 0.40), Depth of Focus DOF >= 0.5 µm.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- SkyWater SKY130 Open PDK Design Rules & Lithography Grid

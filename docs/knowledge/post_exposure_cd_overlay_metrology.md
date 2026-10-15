# Knowledge Note: Post-Exposure CD-SEM & Overlay Metrology for 180nm DRAM Cell Gate

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the metrology standard operating procedure for post-exposure validation of 180nm DRAM access transistor polysilicon gates patterned via Electron Beam Direct Write (EBDW) over active diffusion. Ensures compliance with physical placement grid limits (5 nm grid), SkyWater SKY130 design rules (minimum drawn 150 nm gate length, <= 35 nm overlay budget), and 180nm unit cell access transistor channel length ($L = 180\text{ nm}$).

## Key Metrology & Inspection Constraints
- **Primary Gate CD**: $180\text{ nm} \pm 10\text{ nm}$ (DRAM access transistor) and SKY130 minimum threshold $\ge 150\text{ nm}$.
- **Overlay Budget**: $|\Delta X|, |\Delta Y| \le 35\text{ nm}$ between poly gate and underlying active diffusion.
- **Physical Grid Quantization**: Inspection CD verification aligned to the $0.005\ \mu\text{m}$ ($5\text{ nm}$) manufacturing grid.
- **Poly Pitch & Spacing**: Verification against minimum poly gate spacing ($0.21\ \mu\text{m} = 210\text{ nm}$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

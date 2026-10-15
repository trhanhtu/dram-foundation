# Die Ejector Pin and Rubber/Vespel Collet Tooling Selection & Calibration

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Calibration protocol for dicing ejector needle arrays and pick-and-place rubber/Vespel collets utilized in 180nm DRAM open-source chip assembly. Prevents micro-cracking of crown stacked capacitor over bitline (COB) architectures and back-surface silicon fracture during die delamination from dicing tape.

## Key Details / Architecture
- **Ejector Needles**: Multi-pin tungsten carbide array (3 to 5 pins), spherical radius 25–40 µm, push-up stroke height 350 µm calibrated via dial indicator.
- **Collet Material**: Conductive ESD-safe Vespel SP-1 / static-dissipative rubber collet with perimeter contact preventing contact with active center DRAM cell topology and 100 µm × 100 µm Al bond pads.
- **Pick Vacuum**: >= -75 kPa gauge pressure.
- **Bonding/Attach**: Placement onto conductive silver epoxy (Ablebond 84-1LMIS), bond force 40–50 gf, void area target < 5%, curing at 150°C for 60 min.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

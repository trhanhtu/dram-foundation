# Process Parameter Benchmarking for Full-Chip Array-to-Periphery Boundary Metrology & DRC Sign-off Run

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Establishes benchmarking parameters and DRC/metrology sign-off procedures for the dense memory array-to-periphery transition boundary on an open-source 180nm 1T1C DRAM architecture. Addresses optical proximity, nested-to-isolated line bias, and design rule clean-up across boundary interfaces.

## Key Details / Architecture
- Unit cell channel length: 180 nm, width: 220 nm.
- Array pitch standard: 360 nm to 400 nm for bitline and wordline.
- Gate dielectric baseline: 3.5 nm physical thickness thermally grown at 850°C–900°C dry oxidation.
- Capacitance target: 25 fF to 30 fF per cell (minimum 28 fF target for soft-error margin).
- Sense amplifier boundary interface matching: Folded BL/BLB differential sensing balance ($\Delta V = 100\text{ mV to } 150\text{ mV}$ for $C_{s}=25\text{ fF}$, $C_{BL}=250\text{ fF}$).

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)

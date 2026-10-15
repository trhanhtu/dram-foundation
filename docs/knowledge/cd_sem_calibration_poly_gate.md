# Knowledge: CD-SEM Calibration & Beam Energy Recipe Setup for Poly Gate Target (150nm/180nm)

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the industrial Standard Operating Procedure (SOP) for setting up CD-SEM magnification calibration, beam energy recipes, and automated edge-detection metrology for polysilicon gate features across 150 nm minimum physical gate length (SkyWater SKY130 PDK limit) and 180 nm DRAM cell access transistors / discrete reference transistors.

## Key Details & Metrology Specifications
- **Beam Energy Tuning**: Low acceleration voltage ($V_{acc} = 500\text{ V} - 800\text{ V}$) and ultra-low beam probe current ($I_p = 8\text{ pA} - 15\text{ pA}$) prevent gate dielectric damage, charging distortions, and e-beam shrinkage on sensitive poly/photoresist features.
- **Physical Calibration Grid**: Calibrated using certified pitch standard grating aligned to the physical placement grid resolution of $0.005\ \mu\text{m}$ ($5\text{ nm}$).
- **Target Dimensions**:
  - Minimum Drawn Gate Poly Length: $150\text{ nm}$ ($0.15\ \mu\text{m}$).
  - DRAM Cell Access Transistor Channel Length: $L = 180\text{ nm}$ ($W = 220\text{ nm}$).
  - Minimum Gate Poly Spacing: $0.21\ \mu\text{m}$ ($210\text{ nm}$).
  - Gate Poly to Active Diffusion Overlay Limit: $\le 35\text{ nm}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

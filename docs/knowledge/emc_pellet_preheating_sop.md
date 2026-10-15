# Epoxy Molding Compound (EMC) Pellet Sourcing & Pre-Heating Optimization

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN Council)
- **Status**: Accepted

## Overview & Rationale
Optimizes Epoxy Molding Compound (EMC) pellet handling, cold storage, dielectric RF pre-heating, and viscosity profiling prior to transfer molding encapsulation of 180nm DRAM dies in TSOP-54 and 54-ball FBGA leadframe/substrate assemblies. Proper pellet temperature control prevents wire sweep on 25 µm thermosonic gold wire bonds and minimizes mold voids around high-density interconnects.

## Key Details & Process Parameters
- **Pellet Cold Chain & Storage**: Multi-functional epoxy cresol novolac (ECN) or biphenyl resin stored at 5°C ± 3°C, relative humidity < 30%.
- **Thawing Protocol**: Vacuum desiccator conditioning at room temperature (25°C) for 4 to 8 hours until core temperature stabilizes without condensation.
- **High-Frequency RF Pre-Heating**: Pre-heat dielectric heater (27.12 MHz) set to 85°C to 95°C for 20 to 35 seconds to reduce spiral flow viscosity without premature B-stage gelation.
- **Wire Bond & Die Integrity**: Compatible with thermosonic gold ball bonds (25 µm diameter wire, >= 4.0 gf pull strength) and silver-filled die attach epoxy (void area < 5%, R_th <= 5°C/W).

## References & Related Files
- [docs/context.yaml](..../../context.yaml)
- [docs/context2.yaml](..../../context2.yaml)

# Conductive Epoxy Rheology Characterization & Dispense Tip Sizing

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the rheological characterization and dispense tip sizing standard operating procedure (SOP) for silver-filled conductive die attach epoxy (Ablebond 84-1LMIS) utilized in 180nm open-source DRAM packaging on leadframe carriers.

## Key Details / Architecture
- **Material**: Silver-filled conductive die attach epoxy (Ablebond 84-1LMIS).
- **Rheology Protocol**: Viscosity and thixotropic index qualification under controlled shear rates.
- **Dispense Tip Selection**: Internal diameter sizing tailored to filler particle size and dot volume constraints to avoid needle clogging and tailing/stringing.
- **Curing & Metrology**: Thermal profile at 150°C for 60 min, verified by C-Mode Scanning Acoustic Microscopy (C-SAM) and transient thermal resistance testing.

## Acceptance Criteria
- Curing Temperature: $150^\circ\text{C}$
- Curing Duration: $60\text{ min}$
- Maximum Void Area: $< 5\%$ via acoustic microscopy
- Maximum Thermal Resistance ($R_{th}$): $\le 5^\circ\text{C/W}$

## References & Related Files
- [Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging](./docs/context.yaml)
- SOP Implementation: `docs/sop_conductive_epoxy_rheology_tip_sizing.md`

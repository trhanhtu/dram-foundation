# Automated Laser Surface Particle & Organic Residue Cleanliness Inspection

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for automated laser surface particle and organic residue inspection on 180nm DRAM crown capacitor bottom electrode/substrate surfaces prior to ALD high-k dielectric stack deposition ($\text{Al}_2\text{O}_3/\text{Ta}_2\text{O}_5$). Surface cleanliness directly dictates dielectric interface trap density, leakage breakdown, and refresh intervals.

## Key Details / Architecture
- Integrated optical inspection protocol combining laser scattering particle detection and spectroscopic ellipsometry ($\Psi, \Delta$) wafer mapping (9-point / 49-point).
- Aligned to standard RCA clean (SC-1, 1:50 HF dip, SC-2) rinse and dry requirements.
- Strictly bounds measurement precision to sub-Angstrom limits ($\pm 0.05\text{ nm}$).

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)

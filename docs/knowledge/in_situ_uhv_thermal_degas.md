# In-Situ UHV Thermal Degas and Chamber Moisture Desorption Profiling

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Accepted

## Overview & Rationale
For high-aspect-ratio 3D crown capacitor stacks in 180nm DRAM (such as Ta2O5 / Al2O3 or ONO MIM/SIS topologies), physisorbed atmospheric moisture ($H_2O$, $OH^-$ groups) within deep capacitor cylinders causes local dielectric oxidation, pinhole formation, and excessive leakage current (> 1 fA/cell). Conducting an in-situ Ultra-High Vacuum (UHV) thermal degas before ALD TiN top electrode deposition eliminates deep-recess moisture, preventing non-uniform TiCl4 precursor hydrolysis.

## Key Details / Architecture
- **Vacuum Regime**: Degas chamber base pressure pumpdown $< 2 \times 10^{-6}\text{ Torr}$ via high-capacity turbomolecular and cryopump set.
- **RGA Monitoring**: Continuous Quadrupole Residual Gas Analysis tracking mass amu 18 ($H_2O$), amu 17 ($OH^+$), and amu 28 ($N_2/CO$).
- **Thermal Degas Profile**: Stage ramp to $350^\circ\text{C} - 400^\circ\text{C}$ under UHV to desorb moisture without exceeding thermal budget for bottom plugs.
- **Target Cell Integrity**: Ensures retention $> 64\text{ ms}$ at $85^\circ\text{C}$ and cell capacitance in the $25\text{ to }30\text{ fF}$ (nominal $28\text{ fF}$) window.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

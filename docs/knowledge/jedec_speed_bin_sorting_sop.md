# JEDEC Speed-Bin Classification and Parametric Shmoo Margin Sorting

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the final Automated Test Equipment (ATE) metrology procedure for speed-bin classification and parametric Shmoo margin characterization of the 180nm Open-Source DRAM (SkyWater SKY130/180nm derivative backend and digital controller). Following High-Temperature Operating Life (HTOL) and post-stress screening, packaged dies undergo high-precision timing vector execution to bin parts into JEDEC standard grades (DDR-400, DDR-333, DDR-266) or scrap based on critical timing metrics ($t_{CK}$, $t_{RCD}$, $t_{RP}$) and operating margin boundaries.

## Key Details & Operational Flow
- **2D Shmoo Margin Matrix**: Sweeps core/IO voltage ($V_{DD} / V_{DDQ}$ across 1.70 V to 2.70 V) versus cycle time ($t_{CK}$ step resolution $\le 50\text{ ps}$).
- **Speed-Bin Classification**:
  - **Bin 1 (DDR-400 / 3-3-3)**: $t_{CK} \le 5.0\text{ ns}$, $t_{RCD} \le 15.0\text{ ns}$, $t_{RP} \le 15.0\text{ ns}$, margin $\ge 15\%$.
  - **Bin 2 (DDR-333 / 2.5-3-3)**: $t_{CK} \le 6.0\text{ ns}$, $t_{RCD} \le 18.0\text{ ns}$, $t_{RP} \le 18.0\text{ ns}$, margin $\ge 12\%$.
  - **Bin 3 (DDR-266 / 2.5-3-3)**: $t_{CK} \le 7.5\text{ ns}$, $t_{RCD} \le 20.0\text{ ns}$, $t_{RP} \le 20.0\text{ ns}$, margin $\ge 10\%$.
  - **Bin 7 (Reject/Scrap)**: Failure to close setup/hold timing or margin $< 10\%$.
- **Automated Handler Mapping**: Direct synchronization with ATE handler bin categories for physical packaging and tape-and-reel sorting.

## References & Related Files
- [OpenROAD Physical Design & Synthesis Toolflow](https://openroad-flow-scripts.readthedocs.io/en/latest/)
- [SkyWater SKY130 Open PDK Design Rules & Lithography Grid](./docs/context.yaml)
- [BEOL Multi-Layer Metallization & Wafer Sort](./docs/)

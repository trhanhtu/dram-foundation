# Knowledge Note: ATE Multi-Site Loadboard Docking & Calibration for Post-Stress DDR

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines standard operating calibration and physical docking protocols for multi-site Automated Test Equipment (ATE) running post-stress HTOL speed-binning and Shmoo margin characterization on 180nm commercial MPW DDR DRAM.

## Key Details / Architecture
- **Process Technology**: 180nm CMOS DRAM node (1T1C stacked capacitor over bitline topology).
- **Physical Calibration Parameters**:
  - TDR skew calibration across multi-site test channels (< 15 ps channel-to-channel skew).
  - Pogo pin contact resistance matched to Metal-1 interconnect sheet resistance ($R_s < 0.08\ \Omega/\Box$).
  - Post-stress HTOL thermal chamber stabilization at $85^\circ\text{C}$ to qualify cell leakage ($< 1\text{ fA/cell}$) and refresh retention ($> 64\text{ ms}$).
  - Cell storage capacitance verification target: $\ge 28\text{ fF}$ (effective stack $\kappa > 15$).

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

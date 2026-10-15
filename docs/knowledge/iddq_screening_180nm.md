# Micro-Knowledge: 180nm DRAM Iddq Quiescent Current Screening & Power Rail Leakage Extraction

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Wafer-level Electrical Die Sort (EDS) DC parametric screening requires discriminating intrinsic leakage currents from extrinsic bridging/pinhole defects without destructively stressing the array. In a 180nm 1T1C DRAM node, access transistors ($W=220\text{ nm}, L=180\text{ nm}$) and high-voltage wordline pump rails ($V_{PP}=2.5\text{ V to }2.8\text{ V}$) impose strict quiescent current envelopes to meet retention specifications (>64 ms at 85°C).

## Key Details / Architecture
1. **Power Rail Isolation & Bias Condition**:
   - $V_{DD}$ nominal core rail: $1.8\text{ V}$
   - $V_{PP}$ wordline overdrive pump rail: $2.5\text{ V}$ to $2.8\text{ V}$ (Dickson charge pump feedback deactivated or externally bypassed during PPMU forcing)
   - Gate oxide physical thickness: $3.5\text{ nm}$ thermally grown dry $\text{SiO}_2$
2. **Quiescent Testing Metrics**:
   - Access transistor junction and subthreshold leakage: $\le 1.0\text{ fA/cell}$ at $85^\circ\text{C}$
   - Storage capacitance target: $25\text{ fF}$ to $30\text{ fF/cell}$ (minimum $28\text{ fF}$)
   - Total chip quiescent current thresholding via PPMU integration window: $50\ \mu\text{s}$ to $100\ \mu\text{s}$ post vector latch
3. **Statistical Outlier Detection**:
   - Real-time wafer-map regression applying $\text{Median} \pm 3\sigma$ or nearest-neighbor residual gating to weed out latent gate oxide breakdown and high-k dielectric micro-shorts.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

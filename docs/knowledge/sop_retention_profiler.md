# Variable-Pause Retention Time & Sub-fA Junction Leakage Degradation Profiler

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for metrology characterization of 180nm 1T1C DRAM storage cells. Focuses on parametric variable-pause retention testing, measuring sub-fA junction and sub-threshold leakage degradation, and validating sense amplifier margins across folded bitline arrays.

## Key Details / Architecture
- **Topology**: 8F^2 Folded Bitline, Stacked Capacitor Over Bitline (COB) with crown-shaped MIM or ONO / Ta2O5 / Al2O3 dielectric ($\kappa > 15$).
- **Cell Geometry**: NMOS access transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$.
- **Wordline Drive**: On-chip Dickson charge pump overdrive ($V_{PP} = 2.5\text{V} - 2.8\text{V}$, driven at $20\text{ MHz} - 50\text{ MHz}$, $C_{\text{pump}} = 20\text{ pF} - 50\text{ pF}$) to eliminate $V_{th} \sim 0.5\text{V}-0.7\text{V}$ threshold voltage loss.
- **Leakage Metrology**: Stored charge degradation extraction: $I_{\text{leak}} = C_s \cdot \frac{\Delta V_{\text{cell}}}{\Delta t_{\text{pause}}} < 1.0\text{ fA/cell}$ at $85^\circ\text{C}$ with $C_s \ge 28\text{ fF}$.
- **Sense Margin Requirement**: $C_b / C_s \le 9:1$ (nominal $5:1$ to $9:1$, where $C_b = 150\text{ fF} - 250\text{ fF}$ per 256/512-cell bitline).

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs)
- [1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets](./docs)
- [High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture](./docs)

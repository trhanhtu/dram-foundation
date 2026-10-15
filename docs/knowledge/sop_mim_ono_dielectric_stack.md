# SOP: MIM/ONO High-k Dielectric & Top Plate Conformal Stack Parameterization

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented
- **Node Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > 1T1C DRAM Cell Topology & Layout (8F²) > Crown-Type COB Storage Node & MIM/ONO High-k Dielectric Stack Solid Modeling > MIM/ONO High-k Dielectric & Top Plate Conformal Stack Parameterization
- **Generation**: Gen 2 (µm) | **Action Type**: Make

## Overview & Rationale
Parametric design, conformal deposition specification, and 3D field-solver modeling of the high-k dielectric stack (ONO / Ta2O5) and top plate counter-electrode across an 8F² folded-bitline stacked capacitor over bitline (COB) architecture. This guarantees cell capacitance sufficient for soft-error immunity and robust bitline sense amplification.

## Key Specifications & Machine Acceptance Criteria
- **Cell Storage Capacitance ($C_s$)**: 25 fF to 30 fF per cell (Minimum 28 fF for soft-error & coupling noise immunity)
- **Equivalent Oxide Thickness (EOT)**: 3.0 nm to 4.0 nm
- **Dielectric Permittivity**: Effective dielectric constant $\kappa > 15$
- **Retention Leakage**: $< 1.0\text{ fA/cell}$ at 85°C (Retention time $> 64\text{ ms}$)
- **Readout Differential Voltage ($\Delta V$)**: 100 mV to 150 mV (with $C_{BL} \approx 250\text{ fF}$)

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)
- Source 1: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- Source 2: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*
- Source 3: *Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout*

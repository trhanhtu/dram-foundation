# Micro-Knowledge: PCM Wafer Prober Setup & C-V Profiling Recipe Generation

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Parametric test protocol establishing the setup of automated wafer probers and high-frequency/quasi-static C-V profiling recipes for Process Control Monitor (PCM) test arrays in the 180nm Open-Source DRAM process node.

## Key Details / Architecture
1. **Metallization & Probe Contact Integrity**:
   - Verification of sputtered Al-0.5% Cu / pure Al Metal-1 (350 nm ± 5%) contact structures.
   - Sheet resistance benchmark $R_s < 0.08\ \Omega/\Box$ after 400°C forming gas anneal.
   - Repeatability qualification using 9-point wafer mapping with Gauge R&R $CV < 1.0\%$.

2. **DRAM Stacked Storage Capacitor C-V Metrics**:
   - Access transistor cell footprint: $L = 180\ \text{nm}, W = 220\ \text{nm}$ (8F² / 6F² folded bitline).
   - Dielectric: ONO triple dielectric or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-$k$ stack ($\kappa > 15$).
   - Storage capacitance threshold: $\ge 28\ \text{fF/cell}$ for noise immunity against alpha-particle soft errors and bitline coupling.
   - Leakage current threshold: $< 1\ \text{fA/cell}$ at $85^\circ\text{C}$ chuck temperature to sustain refresh retention requirements.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)

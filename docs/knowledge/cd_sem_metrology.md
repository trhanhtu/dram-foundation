# Automated CD-SEM Critical Dimension & Line-Edge Roughness Metrology

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Automated Critical Dimension Scanning Electron Microscopy (CD-SEM) metrology protocol for the 180nm Open-Source DRAM process node. Covers high-throughput, non-destructive linewidth verification, Line-Edge Roughness (LER), and gate-to-active overlay verification across EBDW and DUV patterned wafers.

## Key Details / Architecture
- **Tool Configuration**: Low accelerating voltage (300 V – 800 V), landing beam current (8 – 15 pA) to prevent HSQ/ZEP520A resist shrinkage and charging.
- **Physical Targets**:
  - DRAM access transistor gate length: $L = 180\text{ nm}$, width: $W = 220\text{ nm}$.
  - SkyWater SKY130 minimum poly gate length: $150\text{ nm}$ ($0.15\ \mu\text{m}$), minimum poly spacing: $210\text{ nm}$ ($0.34\ \mu\text{m}$ pitch minimum).
  - Wordline and bitline pitch: $360\text{ nm}$ to $400\text{ nm}$.
  - Overlay tolerance (Poly to Active Diffusion): $\le 35\text{ nm}$.
  - Manufacturing physical grid: $5\text{ nm}$ ($0.005\ \mu\text{m}$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

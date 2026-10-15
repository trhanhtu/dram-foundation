# Zero-Copy Circular Buffer & Ring-Buffer Telemetry Pipeline Design

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
High-speed automated Shmoo characterization (VDD vs. retention time) for the 180nm Open-Source DRAM chip requires streaming dense bit-cell failure maps from an ESP32-based controller to metrology ingestion hosts. To eliminate CPU-bound copying and memory bottlenecks during high-throughput bit-cell testing across 256/512 cells-per-bitline array blocks, a zero-copy circular ring buffer pipeline with DMA-backed descriptors is utilized.

## Key Physical & Design Parameters
- **DRAM Technology Node**: 180 nm, 1T1C stacked capacitor (COB) architecture.
- **Transistor Geometry**: Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
- **Storage Node Capacitance ($C_s$)**: $25\text{ fF}$ to $30\text{ fF}$ (nominal $28\text{ fF}$).
- **Bitline Parasitic Capacitance ($C_b$)**: $150\text{ fF}$ to $250\text{ fF}$ for 256 or 512 cells/bitline.
- **Capacitance Ratio ($C_b / C_s$)**: $5:1$ to $9:1$ (must not exceed $10:1$).
- **Dielectric / Retention Limit**: Leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ to maintain retention time $> 64\text{ ms}$.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context2.yaml)
- [1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets](./docs/context3.yaml)

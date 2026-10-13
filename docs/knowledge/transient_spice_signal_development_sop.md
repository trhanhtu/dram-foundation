# SOP: Transient SPICE Simulation for Signal Development & Equalization Recovery

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Chip

## Overview & Rationale
Verification of differential signal development ($\Delta V$) and subsequent equalization recovery in 180nm folded bitline CMOS sense amplifiers is critical to guarantee readout fidelity, noise margin, and timing closure across refresh cycles.

## Key Architecture & Parameters
- **Access Transistor Dimension**: Channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
- **Storage Capacitor ($C_s$)**: $25\text{ fF}$ nominal (minimum $28\text{ fF}$ budget for soft-error / coupling immunity).
- **Bitline Capacitance ($C_{BL}$)**: $250\text{ fF}$.
- **Signal Development Margin**: $\Delta V \approx 100\text{ mV} - 150\text{ mV}$.
- **Pitch Matching**: $360\text{ nm}$ bitline array pitch (interleaved sense amplifier layout).
- **Leakage Target**: Sub-threshold and junction leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

## References & Related Files
- `Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout`
- `180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench`

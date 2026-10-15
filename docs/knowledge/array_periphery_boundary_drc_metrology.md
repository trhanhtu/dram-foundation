# Quality Acceptance & Metrology Protocol for Full-Chip Array-to-Periphery Boundary Metrology & DRC Sign-off Run

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Accepted

## Overview & Rationale
Defines the sign-off criteria and metrology inspection verification for the interface between the dense 8F² DRAM cell array and peripheral logic/sense amplifier circuits in a 180nm CMOS DRAM process. The array boundary experiences optical proximity effects, pitch mismatches, and step-height variations between the stacked capacitor-over-bitline (COB) architecture and peripheral metal layers.

## Key Details / Architecture
- **Boundary Pitch Transition**: Array bitline/wordline pitch transitions from 360–400 nm to relaxed peripheral metal spacing.
- **Access Transistor Dimension Verification**: Channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
- **Gate Dielectric Thickness**: Dry oxidation target $3.5\text{ nm}$ grown at $850^\circ\text{C}-900^\circ\text{C}$.
- **Storage Capacitor Budget**: $C_s \ge 25\text{ to }30\text{ fF/cell}$ (nominal $28\text{ fF}$) with dielectric stack EOT $3\text{ to }4\text{ nm}$.
- **Sense Amplifier Interface Integrity**: Verified against $C_{BL} \approx 250\text{ fF}$ ensuring signal $\Delta V \ge 100\text{ to }150\text{ mV}$.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)

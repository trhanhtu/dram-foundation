# Micro-Knowledge: Post-Layout Wordline Rise-Time Transient Simulation & Slew/Overshoot Verification

- **Date**: 2026-10-13
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Wordline (WL) drivers in 180nm DRAM architectures deliver boosted gate overdrive ($V_{PP} > V_{DD} + V_{TH}$) to activate array access transistors ($W/L = 220\,\text{nm} / 180\,\text{nm}$) and transfer cell charge without $V_{TH}$ threshold drop. Post-layout RC parasitics along long poly/metal wordlines create distributed transmission-line effects, leading to signal attenuation, slew degradation, and inductive/capacitive overshoot. This verification SOP ensures rise-time and overshoot do not degrade gate oxide reliability or refresh intervals.

## Key Verification Parameters
- **Access Transistor Geometry**: $L = 180\,\text{nm}$, $W = 220\,\text{nm}$.
- **Gate Dielectric**: Thermally grown $\text{SiO}_2$ with physical thickness $t_{ox} \approx 3.5\,\text{nm}$.
- **Cell Retention & Capacitance Target**: Retention $> 64\,\text{ms}$ at $85^\circ\text{C}$ with $C_s \ge 25\,\text{fF}$ to $28\,\text{fF}$.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

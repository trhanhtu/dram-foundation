# Micro-Knowledge: 8F2 Wordline Pitch Routing & Poly-Silicide Strapping

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
In commercial 180nm CMOS MPW full-custom DRAM arrays (8F^2 folded bitline topology), long continuous polysilicon wordlines introduce severe RC propagation delays and rise-time degradation if left unstrapped. By implementing continuous wordline pitch layout (360 nm to 400 nm) with poly-silicide clad gates and periodic metal strapping through tungsten plugs (W-plugs), Wordline RC delay is constrained, safeguarding write full-rail restoration under $V_{PP}$ boosted conditions (2.5 V - 2.8 V).

## Key Physical & Electrical Parameters
- **Gate Dimensions**: Access transistor length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
- **Wordline Pitch**: $360\text{ nm}$ to $400\text{ nm}$ continuous pitch.
- **Gate Dielectric**: Thermally grown $\text{SiO}_2$ at $850^\circ\text{C} - 900^\circ\text{C}$ dry oxidation with $\sim 3.5\text{ nm}$ physical thickness.
- **Overdrive Supply ($V_{PP}$)**: $V_{PP} = V_{DD} + V_{th} + \Delta V_{\text{overdrive}} \ge 2.5\text{ V} - 2.8\text{ V}$ to prevent $V_{th}$ write degradation ($V_{DD} = 1.8\text{ V}$, $V_{th} \approx 0.5\text{ V} - 0.7\text{ V}$).
- **Storage & Leakage Budget**: Cell capacitance $C_s \ge 25\text{ to } 30\text{ fF}$ (nominal target $\ge 28\text{ fF}$), cell leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ for $> 64\text{ ms}$ refresh retention.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture](./docs/context2.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context3.yaml)

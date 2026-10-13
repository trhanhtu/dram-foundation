# SOP: Dickson Charge Pump VPP Generator & Level Shifter Design

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Proposed
- **Generation**: Gen 2 (µm / 180nm Open-Source DRAM Chip)
- **Subsystem**: Address Decoders & Wordline VPP Voltage Pump > Dickson Charge Pump VPP Generator & Level Shifter Design

## Overview & Rationale
In 180nm DRAM architectures (1T1C cell topology), an access transistor requires a boosted gate voltage $V_{PP} > V_{DD} + V_{th}$ (typically $\sim 2.8\,\text{V}$ to $3.3\,\text{V}$ on a $1.8\,\text{V}$ nominal $V_{DD}$) to eliminate threshold voltage drop ($V_{th}$) when writing a full '1' ($V_{DD}$) into a 25 fF - 30 fF stacked capacitor. Without boosted $V_{PP}$, signal margin $\Delta V$ developed across folded bitlines drops significantly below the required 100 mV - 150 mV window.

## Architectural Flow
```text
┌───────────────────────┐
│                       │
│  Ring Oscillator CLK  │
│        / CLKB         │◄───────────╮
│                       │            │
└───────────┬───────────┘            │
            │                        │
            ▼                        │
┌───────────────────────┐            │
│                       │            │
│    4-Stage Dickson    │            │
│      Charge Pump      │            │Feedback Enable/Disable
│                       │            │
└───────────┬───────────┘            │
            │                        │
            ├────────────────────────┼───────────────────────╮
            ▼                        │                       ▼
┌───────────────────────┐            │           ┌───────────────────────┐
│                       │            │           │                       │
│    VPP Regulator &    │            │           │    Wordline Driver    │
│      Hysteresis       ├────────────╯           │     Level Shifter     │
│      Comparator       │                        │                       │
│                       │                        │                       │
└───────────────────────┘                        └───────────┬───────────┘
                                                             │
            ╭────────────────────────────────────────────────╯
            ▼
┌───────────────────────┐
│                       │
│      1T1C Access      │
│  Transistor Wordline  │
│          WL           │
│                       │
└───────────────────────┘
```

## Step-by-Step SOP Procedure
1. **Clock Generator & Non-Overlapping Phase Synthesis**:
   - Synthesize a two-phase non-overlapping clock ($\Phi$ and $\bar{\Phi}$) via a current-starved ring oscillator with duty-cycle correction to prevent reverse charge sharing between Dickson stages.
2. **Dickson Charge Pump Sizing & Stage Optimization**:
   - Implement a multi-stage Dickson pump employing dynamic body-biasing / cross-coupled gate-boosted NMOS transfer switches to eliminate threshold voltage loss per stage ($V_{th}$ loss).
   - Dimension pumping capacitors utilizing MIM/poly-insulator-poly capacitors sized to supply instantaneous wordline turn-on charge without sagging below regulated limits.
3. **Closed-Loop $V_{PP}$ Regulation & Ripple Suppression**:
   - Implement a resistive voltage divider coupled to a bandgap reference comparator with built-in hysteresis ($20\,\text{mV}$ window) to gate the ring oscillator clock when $V_{PP}$ reaches target voltage.
4. **High-Voltage Wordline Level Shifter Circuit Design**:
   - Design cross-coupled dual-rail level shifters translating nominal core logic levels ($0\,\text{V}$ to $V_{DD}$) up to boosted wordline rails ($0\,\text{V}$ to $V_{PP}$).
   - Ensure thick-oxide transistors (preventing gate-dielectric breakdown beyond $3.5\,\text{nm}$ equivalent physical oxide limit) are placed across high-voltage nodes.
5. **Transient & Corner SPICE Simulation Verification**:
   - Perform full-parasitic post-layout SPICE simulations across PVT corners (FF, TT, SS at $-40^\circ\text{C}$ to $85^\circ\text{C}$) under heavy wordline activation loading.

## Acceptance Criteria Targets
1. **Capacitance & Charge Restoration Margin**: Minimum storage cell capacitance $C_s \ge 28\,\text{fF}$ per cell (range: $25\,\text{fF}$ to $30\,\text{fF}$) fully chargeable to $V_{DD}$ without $V_{th}$ degradation.
2. **Folded Bitline Readout Signal Margin**: Readout differential voltage $\Delta V \ge 100\,\text{mV}$ (target window $100\,\text{mV}$ to $150\,\text{mV}$) developed onto bitline with nominal $C_{BL} = 250\,\text{fF}$.
3. **Sub-threshold and Junction Leakage Budget**: Access transistor sub-threshold and junction leakage $\le 1.0\,\text{fA/cell}$ at $85^\circ\text{C}$.
4. **Gate Dielectric Physical Thickness / EOT**: Wordline gate dielectric physical thickness $\sim 3.5\,\text{nm}$ ($\text{SiO}_2$ thermal oxidation) and capacitor dielectric EOT of $3.0\,\text{nm}$ to $4.0\,\text{nm}$.

## References & Literature Sources
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**

# SOP: Loadboard Multi-Rail PDN & Pogo-Pin Interface Schematic Capture

- **Date**: 2026-10-15
- **Source**: DRAM Foundation VN Council (Circuit Design & ATE Testing Group)
- **Status**: Implemented
- **Generation**: Gen 3 (180nm)

## Overview & Rationale
Capturing the multi-rail Power Delivery Network (PDN) and pogo-pin testhead interface for the 180nm Open-Source DRAM automated test equipment (ATE) loadboard. The DUT requires an ultra-low impedance supply delivery across core VDD (1.8 V), boosted wordline overdrive VPP (2.5 V to 2.8 V), peripheral I/O, and reference ground (VSS). Due to high-frequency transients when charging the wordline pass gates and bitline sense amplifiers, pogo-pin interface parasitic inductance and multi-rail decoupling networks must be strictly captured and bounded in schematics.

## Key Physical & Electrical Parameters
1. **Power Rails**:
   - $V_{DD}$ Core & Periphery: $1.8\text{ V} \pm 2\%$ ($36\text{ mV}$ peak-to-peak maximum transient ripple).
   - $V_{PP}$ Wordline Overdrive Boost Supply: $2.5\text{ V} \text{ to } 2.8\text{ V}$ ($V_{DD} + V_{th} + \Delta V_{\text{overdrive}}$, pass transistor NMOS $V_{th} \sim 0.5\text{ V to } 0.7\text{ V}$, write target without $V_{th}$ loss: full $1.8\text{ V}$ stored into $28\text{ fF}$ cell capacitance).
   - Dickson charge pump clocking reference monitor: $20\text{ MHz to } 50\text{ MHz}$, flying capacitance $C_{\text{pump}} = 20\text{ pF to } 50\text{ pF}$.
2. **Pogo-Pin Interface Assignment**:
   - Contact resistance per pin: $R_{\text{cont}} \le 35\text{ m}\Omega$.
   - Current carrying capacity: $\ge 2.0\text{ A}$ continuous per power contact.
   - Pogo-pin pair loop inductance: $L_{\text{loop}} \le 1.5\text{ nH}$ achieved via interleaved signal-ground-power pin matrix.
3. **Decoupling Hierarchy**:
   - High-frequency bulk / ceramic decoupling: $100\text{ pF}$, $1\text{ nF}$, $100\text{ nF}$, and $10\ \mu\text{F}$ low-ESR ceramic multi-layer capacitors (MLCC 0402/0603) located within $< 3.0\text{ mm}$ of the DUT socket pogo-ring footprint.
4. **DUT Interface & Packaging**:
   - Packaged in Ceramic DIP / QFN package using $25\ \mu\text{m}$ bonding wire (Gold Ball or Al-1% Si Wedge) on $100\ \mu\text{m} \times 100\ \mu\text{m}$ aluminum die pads with die attach Ablebond 84-1LMIS ($R_{\text{th}} \le 5^\circ\text{C/W}$).

## References & Related Files
- [context.yaml](..../../context.yaml)
- [context2.yaml](..../../context2.yaml)
- [context3.yaml](..../../context3.yaml)

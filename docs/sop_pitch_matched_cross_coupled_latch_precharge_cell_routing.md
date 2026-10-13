# SOP: Pitch-Matched Cross-Coupled Latch & Precharge Pass-Gate Cell Layout Routing

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Node
- **Module**: Circuit Design & Physical Layout

---

## 1. Scope & Objective
Define the physical layout and routing execution procedure for the CMOS cross-coupled sense amplifier latch (NMOS SAN pulldown, PMOS SAP pullup) and precharge/equalization pass-gate cell in a 180nm folded bitline open-source DRAM architecture. Ensure pitch alignment matching the memory array bitline pitch (360 nm) through an interleaved layout topology while strictly preserving parasitic balance, symmetric differential bitline development, and clean DRC/LVS closure.

---

## 2. Process Flow Diagram

```text
┌──────────────────────────────────────────────┐
│  1. Bitline Pitch & Interleave Grid Setup    │
│     (360 nm array pitch boundary alignment)  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  2. Precharge & Equalizer Transistor Layout  │
│     (V_DD/2 precharge pass-gate placement)   │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  3. Cross-Coupled Latch Device Placement     │
│     (NMOS SAN to GND, PMOS SAP to V_DD)      │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  4. Symmetric Differential Metal Routing     │
│     (BL and /BL parasitic capacitance match) │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  5. Extraction & Sign-Off Verification       │
│     (DRC/LVS, Delta V: 100-150 mV check)     │
└──────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

1. **Interleaved Pitch Grid & Boundary Definition**:
   - Establish the column pitch boundary aligned strictly to the memory array bitline pitch ($360\text{ nm}$).
   - Because standard CMOS cross-coupled latch devices cannot fit inside a single $360\text{ nm}$ pitch width, configure an alternating interleaved floorplan spanning two adjacent sense amplifier banks (even bitlines sensed on one bank, odd bitlines routed through pass-through channels to the opposing bank, yielding an effective layout pitch of $720\text{ nm}$ per physical amplifier slot).

2. **Precharge & Equalization Pass-Gate Cell Placement**:
   - Place the three-transistor equalization/precharge network (one equalizing pass transistor bridging $BL$ and $/BL$, and two series pass transistors connecting $BL$ and $/BL$ to the $V_{DD}/2$ precharge rail).
   - Route the equalization control signal ($EQ$) perpendicular to the bitlines using Poly or low-resistance lower metal (M1), ensuring minimal rise/fall skew across adjacent columns.

3. **Cross-Coupled Inverter Latch Layout**:
   - Place the NMOS cross-coupled latch pair connected to the $SAN$ node (sensing activation pulling to GND).
   - Place the PMOS cross-coupled latch pair connected to the $SAP$ node (sensing activation pulling to $V_{DD}$).
   - Enforce symmetric, cross-under routing for the cross-coupled inverter gates (drain of NMOS1/PMOS1 tied to gate of NMOS2/PMOS2, and vice versa) using identical metal-to-poly via counts and symmetrical lengths to eliminate capacitive offset between $BL$ and $/BL$.

4. **Symmetric Differential Routing of $BL$ and $/BL$**:
   - Route complementary folded bitlines ($BL$ and $/BL$) through the sense amplifier strip using parallel metal traces (M1/M2) with matched parasitics.
   - Constrain total column bitline capacitance budget to $C_{BL} \approx 250\text{ fF}$ against the cell storage capacitance $C_s \ge 25\text{ fF}$ (nominal min $28\text{ fF}$ for the stacked capacitor).
   - Maintain identical run lengths and shield bitline pairs from adjacent column coupling using grounded or supply shielding traces where pitch permits.

5. **Physical Verification & Parasitic Netlist Extraction**:
   - Execute DRC verification on active diffusion, gate polysilicon, contact plugs (W-plugs), and lower metal interconnects to ensure 0 geometric errors.
   - Run LVS verification confirming proper 1:1 netlist topology for the cross-coupled inverter latch and equalization pass gates.
   - Run Parasitic Extraction (PEX) to extract differential parasitic mismatch ($\Delta C_{BL} = |C_{BL} - C_{/BL}|$) and verify that the signal window $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \left(V_{cell} - \frac{V_{DD}}{2}\right)$ achieves the required $100\text{ mV}$ to $150\text{ mV}$ differential read margin before latch activation.

---

## 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Physical Unit | Verification Method |
|---|---|---|---|
| **Array Bitline Pitch Matching** | **360** | **nm** | GDS Layout Coordinate & DRC Pitch Check |
| **Bitline Parasitic Capacitance ($C_{BL}$)** | **250** | **fF** | Post-Layout Parasitic Extraction (PEX) |
| **Minimum Unit Cell Storage Capacitance ($C_s$)** | **25 to 28** | **fF** | Stacked Capacitor 3D PEX / Metrology |
| **Differential Signal Margin ($\Delta V$)** | **100 to 150** | **mV** | Post-Layout SPICE Transient Read Simulation |
| **DRC / LVS Extraction Errors** | **0** | **Count** | Foundry Sign-Off Batch Verification Deck |

---

## 5. Literature Citations & Local Context

- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
  - CMOS cross-coupled inverter latch between complementary bitlines $BL$ and $/BL$ in folded-bitline topology.
  - Bitlines equalized to $V_{DD}/2$ using an equalization transistor network prior to wordline assertion.
  - Signal development formula $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \left(V_{cell} - \frac{V_{DD}}{2}\right)$.
  - Cell capacitance $C_s = 25\text{ fF}$, bitline capacitance $C_{BL} = 250\text{ fF}$, yielding differential voltage $\Delta V = 100\text{ mV}$ to $150\text{ mV}$.
  - Sensing activation via $SAN$ (pulls to GND) and $SAP$ (pulls to $V_{DD}$), driving full rail CMOS levels ($0\text{ V}$ and $V_{DD}$) and restoring cell charge.
  - Sense amplifier pitch matching memory array bitline pitch ($360\text{ nm}$ in 180nm node) requiring interleaved layout.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - 180nm access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
  - Stacked capacitor over bitline (COB) architecture via tungsten plug (W-plug).
  - Minimum storage capacitance budget of $28\text{ fF}$ per cell.
  - Sub-threshold and junction leakage target below $1\text{ fA/cell}$ at $85^\circ\text{C}$.

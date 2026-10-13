# SOP: Sense Amp Stripe DRC/LVS Verification & Parasitic RC Bitline Imbalance Extraction

- **Date**: 2026-10-13
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented / Ready for Physical Verification & Sign-off
- **Node / Context**: 180nm Open-Source DRAM Chip (Gen 2 µm)
- **Hierarchy**: [Architecture & Integration] > Folded Bitline CMOS Sense Amplifier & Equalizer > Folded Bitline Pitch-Matched Layout & DRC/LVS Extraction > Interleaved Sense Amp & Precharge Pitch-Matched Layout Floorplanning > Sense Amp Stripe DRC/LVS Verification & Parasitic RC Bitline Imbalance Extraction [Metrology]

---

## 1. Overview & Operational Principle
In a folded-bitline 180nm DRAM architecture, the sense amplifier stripe executes differential sensing and full-rail restoration on small charge-sharing signals ($\Delta V \approx 100\text{ mV to } 150\text{ mV}$) developed from 1T1C storage cells ($C_s \ge 25\text{–}28\text{ fF}$) onto complementary bitline pairs ($C_{BL} \approx 250\text{ fF}$). 

Because unit memory cell access transistors require aggressive pitch matching ($360\text{ nm}$ array bitline pitch for $2F = 360\text{ nm}$, with transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$), sense amplifiers and equalizers are laid out in an interleaved configuration across adjacent stripes. Physical layout asymmetries, metal pitch transitions, contact poly resistance variations, and lateral coupling can induce a parasitic resistance-capacitance imbalance between true ($BL$) and complement ($\overline{BL}$) lines ($\Delta C_{BL} = |C_{BL} - C_{\overline{BL}}|$, $\Delta R_{BL} = |R_{BL} - R_{\overline{BL}}|$). Any significant parasitic asymmetry degrades the differential sensing margin, causes false sensing during precharge equalization ($V_{DD}/2$), and violates refresh retention margins.

This Standard Operating Procedure (SOP) formalizes the complete step-by-step physical DRC rule deck validation, layout-versus-schematic (LVS) device extraction, and 2.5D/3D field solver parasitic RC extraction protocol to qualify the Sense Amp stripe.

---

## 2. Process Flow Architecture

```
┌────────────────────────────────────────────────────────┐
│  Stream In GDSII / OASIS Layout of Sense Amp Stripe    │
│  (Interleaved Sense Amp + Equalizer + Bitline Arrays)   │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Step 1: Pitch-Matched DRC Rule Deck Execution         │
│  - Enforce 360 nm Array Bitline Pitch Verification     │
│  - Validate Access Gate L = 180 nm, W = 220 nm         │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Step 2: Hierarchical LVS & Pin Matching               │
│  - Latch Cross-Coupled Pairs (SAN/SAP & EQ Network)    │
│  - Validate Substrate Taps, Isolations & Pin Nets      │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Step 3: 2.5D/3D Field-Solver Parasitic RC Extraction  │
│  - Extract 3D Distributed Parasitics on BL and /BL     │
│  - Solve Mutual Coupling & Plate Substrate Capacitance │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Step 4: BL / /BL Imbalance Screening & Sign-off       │
│  - Evaluate Delta C_BL (target: C_BL ~ 250 fF)         │
│  - Verify Signal Margin: Delta V in [100 mV, 150 mV]   │
└────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step SOP Procedure

### Step 1: Layout Preparation & Pitch-Matched DRC Execution
1. Export the top-level layout of the interleaved sense amplifier stripe including dummy boundary cells, equalizer pass gates, and cell array bitline tapers in GDSII/OASIS format.
2. In the DRC engine (e.g., KLayout / Magic / Calibre-compatible open rule deck), load the 180nm design rules for FEOL/BEOL layers.
3. Execute automated pitch checks across the boundary:
   - Verify array bitline metal/poly pitch equals precisely $360\text{ nm}$.
   - Verify all unit cell access transistor channel dimensions enforce $L = 180\text{ nm}$ and $W = 220\text{ nm}$.
4. Screen for minimum contact enclosure, stacked capacitor tungsten plug (W-plug) landing pads, and inter-metal spacing across Metal-1 and Metal-2 layers.

### Step 2: Hierarchical LVS Netlist Verification & Cross-Coupled Latch Recognition
1. Extract device connectivity directly from the mask layers:
   - Identify PMOS pull-up cross-coupled pair (SAP actuation line to $V_{DD}$).
   - Identify NMOS pull-down cross-coupled pair (SAN actuation line to $GND$).
   - Identify equalization/precharge bridge transistors biased at $V_{DD}/2$.
2. Compare the extracted layout netlist against the golden SPICE subcircuit netlist (`folded_bl_sa.sp`).
3. Ensure $0$ net mismatches, $0$ port mismatches, and $0$ device property parameter errors ($W/L$, dummy tap connectivity, well-tap proximity).

### Step 3: 2.5D/3D Parasitic RC Extraction (PEX)
1. Configure the PEX extraction profile for distributed RC (`R + C + CC` coupled capacitance) with corner models at typical ($25^\circ\text{C}$) and worst-case high-temperature operational limit ($85^\circ\text{C}$).
2. Include all adjacent lines within the stripe bounding box to model lateral fringing capacitance to neighboring bitlines ($BL_{n-1}$, $\overline{BL}_{n-1}$, $BL_{n+1}$, $\overline{BL}_{n+1}$).
3. Extract lump-sum and distributed segment networks into Standard Parasitic Exchange Format (SPEF / DSPF).

### Step 4: Differential Bitline Imbalance & Margin Calculation
1. Calculate the total lump-sum capacitance of the true bitline ($C_{BL}$) and complementary bitline ($C_{\overline{BL}}$) against the nominal target budget of $250\text{ fF}$.
2. Compute the bitline capacitive imbalance metric:
   $$\Delta C_{BL} = |C_{BL} - C_{\overline{BL}}|$$
3. Run transient dynamic read-cycle simulations in SPICE:
   - Set cell storage capacitance $C_s \ge 25\text{ fF}$ (typically $25\text{ fF}$ to $28\text{ fF}$).
   - Equalize bitlines to $V_{DD}/2$.
   - Assert wordline, transferring charge $Q_s = C_s \cdot (V_{cell} - V_{BL})$ onto $BL$.
   - Measure generated differential readout voltage:
     $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left|V_{cell} - \frac{V_{DD}}{2}\right|$$
   - Confirm differential voltage $\Delta V$ falls squarely within the design target window of $100\text{ mV}$ to $150\text{ mV}$.
   - Verify sense amplifier latching speed upon SAN/SAP activation to full CMOS rails ($0\text{ V}$ and $V_{DD}$) without regenerative latch metastability or flip.

---

## 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Physical Unit | Verification Method / Rule |
| :--- | :--- | :--- | :--- |
| **Array Bitline Pitch** | $360$ | $\text{nm}$ | Automated DRC geometric edge-to-edge pitch rule check |
| **Transistor Channel Length ($L$)** | $180$ | $\text{nm}$ | In-line DRC gate poly dimension verification |
| **Transistor Channel Width ($W$)** | $220$ | $\text{nm}$ | In-line DRC active diffusion width check |
| **Nominal Bitline Capacitance ($C_{BL}$)** | $250$ | $\text{fF}$ | 3D PEX parasitic capacitive extraction |
| **Cell Storage Capacitance ($C_s$)** | $\ge 25\text{ to } 28$ | $\text{fF}$ | 3D PEX / LVS extraction of stacked capacitor stack |
| **Differential Signal Voltage ($\Delta V$)** | $100\text{ to } 150$ | $\text{mV}$ | SPICE transient readout simulation at $85^\circ\text{C}$ |
| **Bitline Parasitic Imbalance ($\Delta C_{BL}$)** | $\le 2.5$ ($< 1\%$) | $\text{fF}$ | SPEF differential extraction ($|C_{BL} - C_{\overline{BL}}|$) |
| **Subthreshold / Junction Cell Leakage** | $< 1.0$ | $\text{fA/cell}$ | SPICE DC leakage simulation at $85^\circ\text{C}$ |

---

## 5. Source Citations
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**: Differential sensing of 1T1C cell, $V_{DD}/2$ precharge equalization, SAN/SAP full-rail activation ($0\text{V}$ and $V_{DD}$), $C_s = 25\text{ fF}$, $C_{BL} = 250\text{ fF}$, $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{cell} - V_{DD}/2) \approx 100\text{ mV to } 150\text{ mV}$, and $360\text{ nm}$ bitline pitch-matched interleaved layout.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: 180nm technology node access transistor geometry $L = 180\text{ nm}$, $W = 220\text{ nm}$, minimum $28\text{ fF}$ cell capacitance budget, and junction/subthreshold leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

# Parasitic RC Extraction (PEX) & Differential Bitline Signal-Margin Metrology

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM
- **Action Type**: Make

---

## 1. Scope & Engineering Context
This Standard Operating Procedure (SOP) governs the extraction of parasitic resistance and capacitance ($RC$) across pitch-matched folded bitlines ($BL$ and $/BL$) and the subsequent transient SPICE signal-margin metrology in a 180nm open-source DRAM architecture. 

During read operation, access transistors dump small cell charges onto precharged bitlines ($V_{DD}/2$), developing a differential voltage signal:
$$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right)$$
Accurate pitch-matched parasitic extraction is mandatory to guarantee differential sense amplifier latching margin prior to full-rail activation ($SAN \to \text{GND}$, $SAP \to V_{DD}$).

---

## 2. Metrology Workflow & Execution Pipeline

```text
┌────────────────────────┐
│                        │
│  GDSII Layout & Layer  │
│      Stack Input       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       LVS Clean        │
│      Connectivity      │
│      Verification      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  3D Field Solver PEX   │
│    & RC Extraction     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Back-Annotated     │
│    Transistor-Level    │
│   Netlist Generation   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Transient Bitline    │
│     Signal-Margin      │
│       Metrology        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       Full-Rail        │
│  Restoration & Noise   │
│       Validation       │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Layout Geometrical & Connectivity Ingestion
1. Ingest the physical layout database (GDSII / OASIS) containing the folded bitline array, shared bitline contacts, and interleaved CMOS sense amplifier blocks.
2. Confirm array bitline pitch conforms to physical design constraints:
   - Access transistor geometry: Channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - Array bitline pitch: Exactly $360\text{ nm}$ pitch-matched to sense amplifier latch pitches.
3. Perform Layout Versus Schematic (LVS) checking to ensure pin-level connectivity match across $BL$, $/BL$, storage nodes, and equalization gates.

### Step 2: 3D/2.5D Field Solver Parasitic RC Extraction (PEX)
1. Load process techfile specifying FEOL and BEOL dielectric constants ($\kappa$), tungsten plug contacts, and metal stack thickness.
2. Run detailed coupled field extraction on $BL$ and $/BL$:
   - Extract total lump/distributed bitline capacitance $C_{BL}$, targeting nominal $250\text{ fF}$.
   - Separate near-neighbor coupling capacitance ($C_{c}$) between complementary bitlines and adjacent pairs to evaluate crosstalk susceptibility.
   - Extract bitline wire resistance $R_{BL}$ along metal lines and tungsten plugs (W-plug).
3. Back-annotate storage capacitor cell node parameters:
   - Target nominal cell capacitance $C_s \ge 25\text{ fF}$ (stacked capacitor structure requiring a minimum budget of $28\text{ fF}$ for soft-error and coupling noise immunity).
4. Output back-annotated netlist in SPEF / DSPF format.

### Step 3: Precharge & Wordline Activation Transient Simulation
1. Initialize the folded bitline simulation testbench:
   - Precharge complementary bitlines $BL$ and $/BL$ to $V_{DD}/2$ using the equalization transistor network.
   - Set cell storage voltage $V_{cell} = V_{DD}$ (logic '1') and $V_{cell} = 0\text{ V}$ (logic '0') across worst-case corners.
2. Assert wordline voltage ($V_{WL} = V_{PP}$ boosted level) to turn on the access transistor ($L = 180\text{ nm}$, $W = 220\text{ nm}$).
3. Dump cell charge $Q_s = C_s \cdot (V_{cell} - V_{BL})$ onto the bitline and measure differential signal development prior to sense amplifier strobe.

### Step 4: Differential Signal Margin Metrology & Latching Verification
1. Probe dynamic signal split between $BL$ and $/BL$:
   - Measure differential voltage $\Delta V = |V_{BL} - V_{/BL}|$.
   - Confirm developed signal meets the target window of $100\text{ mV}$ to $150\text{ mV}$.
2. Trigger sense amplifier strobe signals:
   - Ramp $SAN$ to $\text{GND}$ ($0\text{ V}$) and $SAP$ to $V_{DD}$.
   - Verify regenerative positive feedback drives $BL$ and $/BL$ to full CMOS rails ($0\text{ V}$ and $V_{DD}$).
   - Verify storage cell charge restoration reaches $100\%$.
3. Inspect leakage current profile at elevated operating temperature ($85^\circ\text{C}$):
   - Measure combined access transistor sub-threshold and junction leakage to confirm $I_{leak} \le 1\text{ fA/cell}$.

---

## 4. Machine-Measurable Acceptance Criteria Metrics

```text
                     ┌─────────────────────────────────┐
                     │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
           Pitch (nm)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
                     │▒▒▒▒▒▒▒▒▒▒▒▒                     │
Signal Margin dV (mV)┤▒▒▒▒▒▒▒▒▒▒▒▒                     │
 Bitline Cap CBL (fF)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          │
                     │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          │
     Cell Cap Cs (fF)┤███                              │
                     │███                              │
                     └┬───────┬───────┬───────┬───────┬┘
                      0      90      180     270    360 
```

| Metric Parameter | Target Value / Tolerance | Measurement Mode | Conformance Standard |
| :--- | :--- | :--- | :--- |
| **Array Bitline Pitch** | **$360\text{ nm}$** | Automated GDSII/DRC measurement | Sense amplifier pitch-matched layout |
| **Bitline Parasitic Capacitance ($C_{BL}$)** | **$250\text{ fF}$** nominal | Post-PEX netlist integration | LVS/PEX 3D extraction engine |
| **Cell Storage Capacitance ($C_s$)** | **$25\text{ fF}$** (nominal) / **$\ge 28\text{ fF}$** (budget) | PEX & C-V cell model metrology | Soft error & coupling immunity budget |
| **Differential Signal Margin ($\Delta V$)** | **$100\text{ mV}$ to $150\text{ mV}$** | Transient post-PEX differential probe | Readout window prior to $SAN$/$SAP$ strobe |
| **Cell Off-State Leakage Current ($I_{leak}$)** | **$\le 1\text{ fA/cell}$ at $85^\circ\text{C}$** | DC/transient junction leakage probe | Retention / refresh interval target |

---

## 5. Verified Local Literature Citations
All technical specifications, geometric pitch limits, capacitance parameters, and voltage margins strictly originate from verified local context:
1. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
   - Differential signal formulation: $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{cell} - V_{DD}/2)$.
   - Parametric signal window: Differential $\Delta V \approx 100\text{ mV}$ to $150\text{ mV}$ for $C_s = 25\text{ fF}$ and $C_{BL} = 250\text{ fF}$.
   - Strobe dynamics: Equalization to $V_{DD}/2$, $SAN$ pulling to $\text{GND}$, $SAP$ pulling to $V_{DD}$, driving full rails and $100\%$ cell charge restoration.
   - Array layout: Pitch matching to memory array bitline pitch ($360\text{ nm}$ in 180nm node) via interleaved layout.
2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor dimensions: Gate length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - Minimum cell storage capacitance budget: $28\text{ fF/cell}$ minimum.
   - Off-state cell leakage criterion: Sub-threshold and junction leakage kept below $1\text{ fA/cell}$ at $85^\circ\text{C}$.

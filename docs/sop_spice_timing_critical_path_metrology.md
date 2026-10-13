# SOP: SPICE Timing Critical-Path Metrology & Post-Layout Parasitic Delay Verification

- **Date**: 2026-10-13
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Node Classification**: Gen 2 (µm) / Leaf Node / Action: Make
- **Hierarchy Context**: 180nm Open-Source DRAM Chip [Architecture & Integration] > Address Decoders & Wordline VPP Voltage Pump [DRAM Circuit Design] > Hierarchical Row/Column Address Predecoder & Wordline Driver Sizing [Circuit Design] > Hierarchical Address Predecoder Tree & Multi-Stage Logic Topology Design [Circuit Design] > SPICE Timing Critical-Path Metrology & Post-Layout Parasitic Delay Verification [Metrology]

---

## 1. Overview & Scope
This Standard Operating Procedure (SOP) governs the extraction, full-path RC back-annotation, and SPICE transient metrology for verifying address predecoder propagation latency, wordline assert timing, bitline differential signal development, and sense-amplifier latch synchronization in an open-source 180nm DRAM design.

---

## 2. Structural Metrology Workflow

```text
┌────────────────────────┐
│                        │
│   1. PEX Extraction    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  2. Netlist Stitching  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  3. SPICE Simulation   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      4. Metrology      │
│        Sign-Off        │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Procedure

### Step 1: Post-Layout Parasitic Extraction (PEX)
1. Load finalized layout database (GDSII/OASIS) with DRC-clean metal routing on 360 nm to 400 nm pitch wordline/bitline tracks.
2. Execute 3D field-solver parasitic extraction (PEX) on critical address input pins, predecoder multi-stage NAND/NOR trees, wordline drivers, and array folded bitlines ($BL$, $\overline{BL}$).
3. Extract distributed R-L-C networks into DSPF/SPEF formats, maintaining substrate coupling and inter-wire coupling capacitance.

### Step 2: Critical-Path Netlist Stitching
1. Back-annotate extracted parasitics into the hierarchical SPICE netlist:
   - Row predecoder tree logic.
   - Wordline driver stages ($V_{PP}$ boosted node).
   - Array 1T1C storage cell ($W = 220\text{ nm}$, $L = 180\text{ nm}$).
   - Folded bitline pairs and CMOS cross-coupled sense amplifier.
2. Parameterize thermal and operational corners: $T = 85^\circ\text{C}$ (maximum junction specification), $V_{DD} = 1.8\text{ V}$, $V_{PP}$ boost level, and nominal bitline precharge voltage $V_{DD}/2 = 0.9\text{ V}$.

### Step 3: Multi-Corner Transient Simulation
1. Initialize array precharge network to equalize bitlines to $V_{DD}/2 = 0.9\text{ V}$.
2. Stimulate input address transition at row predecoder inputs.
3. Track propagation delay through address predecoder buffers, level shifter, and wordline driver.
4. Trigger wordline assertion, activating access transistor ($L = 180\text{ nm}$, $W = 220\text{ nm}$) to dump cell charge $Q_s = C_s \cdot (V_{\text{cell}} - V_{BL})$ onto $BL$.

### Step 4: Sense Amplifier & Latch Strobe Metrology
1. Measure differential voltage signal development across $BL$ and $\overline{BL}$:
   $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left|V_{\text{cell}} - \frac{V_{DD}}{2}\right|$$
2. Measure delay from wordline trigger to sense amplifier latch strobe ($SAN$ pull-down and $SAP$ pull-up).
3. Verify that leakage does not degrade signal retention margin over 64 ms refresh window budget.

---

## 4. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Acceptance Target Metric | Unit | Physical Context / Verification Condition |
| :--- | :--- | :--- | :--- |
| **Cell Storage Capacitance ($C_s$)** | $\ge 25.0 \text{ to } 28.0$ | $\text{fF}$ | Stacked crown/cylinder capacitor ($Ta_2O_5 / Al_2O_3$ or ONO stack, $\kappa > 15$, $\text{EOT} = 3\text{--}4\text{ nm}$) |
| **Bitline Parasitic Capacitance ($C_{BL}$)** | $\le 250.0$ | $\text{fF}$ | Post-layout folded bitline parasitic extraction over array column |
| **Differential Signal Window ($\Delta V$)** | $\ge 100.0 \text{ to } 150.0$ | $\text{mV}$ | Signal development prior to sense amplifier latch activation |
| **Cell Leakage Current ($I_{\text{leak}}$)** | $\le 1.0$ | $\text{fA/cell}$ | Access transistor subthreshold + junction leakage at $T = 85^\circ\text{C}$ for retention $\ge 64\text{ ms}$ |

---

## 5. Citations & References
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Cell geometry: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
  - Capacitance budget: Minimum $28\text{ fF/cell}$ ($\kappa > 15$, Ta2O5/Al2O3 or ONO stack).
  - Sub-threshold and junction leakage target: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
  - Precharge equalization to $V_{DD}/2$.
  - Charge dump formula: $Q_s = C_s \cdot (V_{\text{cell}} - V_{BL})$.
  - Differential signal: $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{\text{cell}} - V_{DD}/2)$.
  - Sizing & parameters: Typical $C_s = 25\text{ fF}$, $C_{BL} = 250\text{ fF}$, signal $\Delta V = 100\text{ mV to } 150\text{ mV}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - 1T1C storage capacitor $25\text{ to } 30\text{ fF/cell}$ ensuring data retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
  - Wordline and bitline pitch: $360\text{ nm to } 400\text{ nm}$.
  - Gate oxide: dry thermal $SiO_2$ with $\sim 3.5\text{ nm}$ physical thickness.

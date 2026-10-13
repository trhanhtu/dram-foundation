# Standard Operating Procedure: DRC Rule Deck Extension for Stacked Capacitor (COB) & Dense Contact Geometries

- **Document ID**: SOP-MET-DRC-180-COB
- **Version**: 1.0
- **Technology Node**: 180nm Open-Source DRAM (Gen 2 µm)
- **Hierarchy Path**: Context: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm 1T1C DRAM Cell Bitline & Wordline Matrix Layout [Circuit Design] > DRC/LVS Verification & Parasitic Extraction for Bitline/Wordline Matrix [Metrology] > DRC Deck Customization & Geometric Design Rule Clean-up [Metrology] > DRC Rule Deck Extension for Stacked Capacitor (COB) & Dense Contact Geometries [Metrology]
- **Action Type**: Buy (Commercial/PDK Extension Procured & Configured)

---

## 1. Process Overview & Objectives
Extend, tailor, and qualify the commercial 180nm baseline design rule check (DRC) rule deck to support 8F² and 6F² folded bitline Capacitor-Over-Bitline (COB) topologies, dense shared bitline contacts, and high-aspect-ratio tungsten plug (W-plug) landing pads.

```text
┌────────────────────────┐
│                        │
│    Procure Base PDK    │
│       Rule Deck        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Define COB & Contact  │
│      Mask Layers       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Encode Design Rule   │
│      Constraints       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Calibrate Pitches &   │
│   Overlay Tolerances   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Execute Regression &  │
│   Metrology Sign-Off   │
│                        │
└────────────────────────┘
```

---

## 2. Step-by-Step Procedure

### Step 1: Procurement & Ingestion of Base DRC Rule Deck
1. Procure and ingest the qualified 180nm CMOS base rule deck (`.calibre`, `.klayout`, or open-source compatible rule syntax).
2. Validate layer mapping definitions against the 180nm mask set catalog.

### Step 2: Definition of COB & Dense Contact Mask Layers
1. Instantiate layer definitions for the stacked capacitor node:
   - `SN_CONT` (Storage Node Contact / W-plug drain contact).
   - `SN_BOT` (Bottom Electrode / Crown polysilicon / MIM structure).
   - `SN_DIEL` (High-k Dielectric layer: ONO / Ta₂O₅ / Al₂O₃).
   - `SN_TOP` (Top Plate / Cell Common Plate).
2. Instantiate `BL_CONT` (Shared Bitline Contact between two adjacent 1T1C memory cells).

### Step 3: Geometric Constraint Encoding for Array Core
1. **Access Transistor Channel Geometry**:
   - Enforce minimum gate length $L = 180\text{ nm}$.
   - Enforce active width $W = 220\text{ nm}$.
   - Restrict gate dielectric physical thickness verification to $3.5\text{ nm}$ equivalent spacing.
2. **Dense Array Pitch & Spacing Rules**:
   - Encode minimum bitline (BL) and wordline (WL) pitch constraint: $[360\text{ nm}, 400\text{ nm}]$.
   - Enforce shared bitline contact spacing, enclosure, and corner rounding clearances.
3. **Capacitor Over Bitline (COB) Stacking Rules**:
   - Constrain minimum bottom electrode area and aspect ratio to ensure effective node capacitance $C_s \ge 25\text{ fF}$ (nominal budget $28\text{ fF}$ to $30\text{ fF}$).
   - Set enclosure of `SN_CONT` by `SN_BOT` to avoid dielectric puncture and landing misalignments.

### Step 4: Rule Deck Regression & Error Flagging Calibration
1. Execute synthetic test pattern layouts with programmed DRC perturbations (sub-180 nm channels, pitch pinching below 360 nm, and undersized contact landing pads).
2. Verify that 100% of DRC violations are accurately caught without false negatives.

### Step 5: Clean-up & Metrology Sign-Off
1. Run extended rule deck on the full 180nm 1T1C Bitline/Wordline matrix layout.
2. Generate clean DRC run log confirming zero unexempted DRC errors prior to LVS and parasitic extraction.

---

## 3. Dimensional Reference Summary

```text
                     ┌─────────────────────────────────┐
                     │■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■│
      BL/WL Min Pitch┤■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■│
                     │█████████████████████            │
      Channel Width W┤█████████████████████            │
     Channel Length L┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                │
                     │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                │
Cap EOT (Si3N4/Ta2O5)┤▒                                │
                     │▒                                │
    Gate Oxide (SiO2)┤░                                │
                     │░                                │
                     └┬───────┬───────┬───────┬───────┬┘
                      0      90      180     270    360 
```

---

## 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value & Tolerance | Physical Unit | Measurement / Validation Method |
|---|---|---|---|
| **Access Transistor Channel Length ($L$)** | $180 \pm 0$ (min limit) | nm | DRC geometric width check (`LENGTH == 180 nm`) |
| **Access Transistor Channel Width ($W$)** | $220 \pm 0$ (min limit) | nm | DRC geometric width check (`WIDTH == 220 nm`) |
| **Bitline & Wordline Pitch Range** | $360\text{ to }400$ | nm | DRC spacing/pitch verification (`PITCH >= 360 nm`) |
| **Cell Capacitance Target ($C_s$)** | $25\text{ to }30$ (min budget $28$) | fF/cell | Post-layout parasitic extraction calculation |
| **Cell Retention & Leakage at Elevated Temp** | Leakage $< 1$ at $85$ (Retention $> 64$) | fA/cell, °C (ms) | Electrical metrology verification & sign-off |

---

## 5. Literature Sources Cited
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Transistor dimensions $L = 180\text{ nm}$, $W = 220\text{ nm}$.
  - Shared bitline contact between adjacent cells.
  - Stacked COB crown polysilicon/MIM with W-plug drain contact.
  - ONO / $\text{Ta}_2\text{O}_5$ / $\text{Al}_2\text{O}_3$ high-k stack ($\kappa > 15$).
  - Capacitance budget $\ge 28\text{ fF/cell}$, leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - 1T1C architecture with $8F^2$ / $6F^2$ layout.
  - Storage capacitor target $25\text{ to }30\text{ fF/cell}$, retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
  - EOT around $3\text{ to }4\text{ nm}$ ($\text{Si}_3\text{N}_4$ / $\text{Ta}_2\text{O}_5$).
  - Bitline and wordline pitch $360\text{ nm}$ to $400\text{ nm}$.
  - Thermally grown $\text{SiO}_2$ gate dielectric at $850^\circ\text{C}\text{--}900^\circ\text{C}$ dry oxidation with $\sim 3.5\text{ nm}$ physical thickness.
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
  - $C_s = 25\text{ fF}$, bitline capacitance $C_{BL} = 250\text{ fF}$.
  - Readout signal development $\Delta V = 100\text{ to }150\text{ mV}$.

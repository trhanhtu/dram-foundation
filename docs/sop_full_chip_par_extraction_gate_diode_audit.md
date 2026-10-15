# Standard Operating Procedure (SOP): Full-Chip Process Antenna Ratio (PAR) Extraction & Gate Diode Fix Audit

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Accepted
- **Context Track**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > MPW Shuttle GDSII Tapeout Package & Foundry Sign-Off > Full-Chip Physical Verification (DRC/LVS/ERC/Antenna) & Dummy Metal Fill Synthesis > Full-Chip Hierarchical DRC & Process Antenna Rule Verification > Full-Chip Process Antenna Ratio (PAR) Extraction & Gate Diode Fix Audit

---

## 1. Overview & Operational Scope
During reactive ion etching (RIE) and high-density plasma deposition in 180nm CMOS processing, long metal and polysilicon interconnects act as antenna collectors. Charge accumulation on conductor surfaces induces tunneling Fowler-Nordheim currents through thin gate dielectrics ($T_{ox} \approx 3.5\text{ nm}$ grown at $850^\circ\text{C}-900^\circ\text{C}$ dry oxidation). Unprotected gates suffer gate oxide breakdown, early $V_{th}$ drift, or latent pinhole defects.

This SOP details the extraction and hierarchical verification of Process Antenna Ratios (PAR) across the full-chip DRAM layout—specifically addressing long wordline (WL) distributions, bitline (BL) interfaces, sense-amplifier decoders, and peripheral control logic. It specifies insertion criteria for reverse-biased PN gate protection diodes while enforcing strict junction leakage limits ($< 1\text{ fA/cell}$ at $85^\circ\text{C}$) to guarantee data retention across memory blocks.

---

## 2. Process Antenna Verification & Diode Insertion Workflow

```text
┌───────────────────────┐
│                       │
│    Input Full-Chip    │
│     GDSII & Layer     │
│      Definitions      │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│   Hierarchical PAR    │
│   Extraction & Net    │
│        Tracing        │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────◇───────────┐
│                       │
│     PAR Threshold     │
│       Exceeded?       │
│                       │
└───────────◇───────────┘
            │
            ├────────────────────────────╮
         Yes│                            │No
            ▼                            ▼
┌───────────────────────┐    ┌───────────────────────┐
│        Insert         │    │                       │
│   Reverse-Biased PN   │    │   Clean Net Flagged   │
│  Gate Tie-Down Diode  │    │                       │
└───────────┬───────────┘    └───────────┬───────────┘
            │                            │
            ▼                            ▼
┌───────────────────────┐    ┌───────────────────────┐
│    Verify Junction    │    │    MPW DRC/Antenna    │
│   Leakage Target &    ├───►│    Sign-Off Clean     │
│    Re-Extract PAR     │    │                       │
└───────────────────────┘    └───────────────────────┘
```

---

## 3. Step-by-Step SOP Procedure

### Step 1: Geometry & Thin-Oxide Gate Net Mapping
1. Extract gate perimeter and gate oxide areas ($A_g = W \times L$) for all FETs connected to long routing tracks. For access transistor arrays, evaluate the nominal channel dimensions: length $L = 180\text{ nm}$ ($0.18\ \mu\text{m}$) and width $W = 220\text{ nm}$ ($0.22\ \mu\text{m}$), yielding $A_g = 0.0396\ \mu\text{m}^2$.
2. Trace connected conductor segments across Polysilicon, Metal 1 through Top Metal, and inter-metal vias (W-plugs).
3. Compute cumulative and per-layer antenna ratios:
   $$\text{PAR}_{\text{cumulative}} = \frac{\sum A_{\text{conductor}}}{A_g}$$
   $$\text{PAR}_{\text{sidewall}} = \frac{\sum A_{\text{perimeter\_sidewall}}}{A_g}$$

### Step 2: Hierarchical Antenna Extraction Run
1. Run the foundry antenna extraction deck across all hierarchical blocks:
   - 1T1C Core Array Matrix ($8F^2$ folded bitline cell area $= 0.259\ \mu\text{m}^2$; $6F^2$ open bitline cell area $= 0.194\ \mu\text{m}^2$).
   - Wordline and bitline pitches ($360\text{ nm}$ to $400\text{ nm}$).
   - Peripheral Decoders, Sense Amplifiers, and Global Routing Buses.
2. Flag all nets violating foundry maximum permissible PAR limits for thin-oxide gates ($T_{ox} \approx 3.5\text{ nm}$).

### Step 3: Diode Tie-Down Synthesis & Physical Placement
1. For violating nets where metal jumper bridging (routing upper layers down to lower layers near the gate) cannot clear the violation, synthesize reverse-biased PN junction protection diodes connected directly between the gate net and $V_{SS}$ (for NMOS gates) or $V_{DD}$ (for PMOS gates).
2. Diode physical dimensioning:
   - Set diode junction perimeter and active area to discharge RIE-induced charge, lowering effective PAR below foundry ratio rules.
   - Maintain minimum distance constraints to active wordlines and bitline contacts.
   - Ensure the diode cathode/anode active tap satisfies latch-up ground-rule spacing.

### Step 4: Diode Junction Leakage & Parasitic Audit
1. Audit total added leakage per memory cell branch. Sub-threshold and junction reverse leakage across the tie-down diode must not compromise the array leakage ceiling of $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. Audit capacitance loading added by protection diodes:
   - Verify that bitline parasitic capacitance ($C_b$) remains strictly within $150\text{ fF}$ to $250\text{ fF}$ for an array block of 256 or 512 cells per bitline.
   - Confirm that the bitline-to-storage-node capacitance ratio $C_b / C_s$ remains within the nominal operating envelope of $5:1$ to $9:1$ (below the $10:1$ critical degradation ceiling), preserving the nominal storage cell budget ($C_s \ge 25\text{ fF}$ to $30\text{ fF}$, nominal $28\text{ fF}$).

### Step 5: Post-Fix Hierarchical DRC & MPW Sign-Off
1. Re-run DRC, LVS, and Antenna check decks on the modified GDSII.
2. Ensure 0 PAR violations across core and peripheral domains prior to tapeout freeze.

---

## 4. Machine-Measurable Acceptance Criteria

```text
                       ┌───────────────────────────────┐
                       │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
      W-L Geometry (nm)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
                       │▒▒▒▒▒                          │
        C_s Budget (fF)┤▒▒▒▒▒                          │
Leakage Floor (fA/cell)┤▓                              │
                       │▓                              │
    Gate Oxide Tox (nm)┤█                              │
                       │█                              │
                       └┬───────┬──────┬───────┬──────┬┘
                        0      55     110     165   220 
```

| Metric / Parameter | Target Value | Verification Method | Unit | Pass/Fail Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **Thin Gate Oxide Physical Thickness ($T_{ox}$)** | $\approx 3.5$ (grown at $850^\circ\text{C}-900^\circ\text{C}$) | Metrology / PDK DRC Antenna Layer Model | $\text{nm}$ | Mandatory thickness reference for antenna breakdown limits |
| **Access Transistor Channel Geometry ($L \times W$)** | $180 \times 220$ | GDSII Layout / DRC Gate Area Extraction | $\text{nm}$ | $A_g = 0.0396\ \mu\text{m}^2$ baseline |
| **Sub-threshold & Junction Leakage Ceiling** | $< 1.0$ at $85^\circ\text{C}$ | TCAD / SPICE Reverse Diode Leakage Sim | $\text{fA/cell}$ | Required for $\ge 64\text{ ms}$ refresh interval retention |
| **Bitline Parasitic Capacitance ($C_b$) Loading** | $150$ to $250$ ($256$ to $512$ cells/BL) | Post-Layout 3D Parasitic Extraction (PEX) | $\text{fF}$ | Keeps $C_b / C_s$ ratio between $5:1$ and $9:1$ ($< 10:1$) |
| **Unresolved Antenna Rule Violations** | $0$ | Full-Chip Hierarchical Antenna DRC Sign-Off | Count | Absolute zero violations on tapeout GDSII |

---

## 5. Literature Sources Cited
1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - Access transistor geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$).
   - Tungsten plug (W-plug) stacked capacitor interconnects.
   - Storage cell capacitance budget: minimum $28\text{ fF/cell}$.
   - Sub-threshold and junction leakage target: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**
   - Folded bitline ($8F^2$) and open bitline ($6F^2$) layouts.
   - Storage capacitance requirement: $25\text{ fF}$ to $30\text{ fF/cell}$ for data retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Bitline and wordline pitch: $360\text{ nm}$ to $400\text{ nm}$.
   - Gate dielectric: thermally grown $\text{SiO}_2$ at $850^\circ\text{C}-900^\circ\text{C}$ dry oxidation with $\sim 3.5\text{ nm}$ physical thickness.
3. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**
   - Physical footprint: $6F^2 = 0.194\ \mu\text{m}^2$, $8F^2 = 0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$.
   - Bitline capacitance budget ($C_b$): $150\text{ fF}$ to $250\text{ fF}$ across $256/512$ cell array blocks.
   - Capacitance ratio constraint: $C_b / C_s$ maintained between $5:1$ and $9:1$ (strictly avoiding $> 10:1$).

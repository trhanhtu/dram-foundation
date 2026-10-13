# Standard Operating Procedure (SOP): Procurement of Electronic-Grade BOE 6:1 Chemical Solution & Safety Supplies

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 1 (mm) / 180nm Open-Source DRAM Architecture
- **Action Type**: Buy
- **Context Level**: 180nm Open-Source DRAM Chip > Buffered Oxide Etch (BOE 6:1) SiO2 Patterning > Procurement of Electronic-Grade BOE 6:1 Chemical Solution & Safety Supplies

---

## 1. Scope & Objective
This SOP defines the technical procurement, incoming quality control (IQC), receiving inspection, and environmental health & safety (EHS) requirements for acquiring electronic-grade Buffered Oxide Etch (BOE 6:1) chemical solution and hydrofluoric acid safety supplies required for $\text{SiO}_2$ patterning in the 180nm DRAM fabrication line.

---

## 2. Procurement Workflow Diagram

```text
┌────────────────────────┐
│                        │
│    Procurement Spec    │
│   Verification: BOE    │
│      6:1 & Safety      │
│        Supplies        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Vendor Quality & COA  │
│       Validation       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Safety First:      │
│   Calcium Gluconate    │
│   Gel & PPE Staging    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Physical Receiving,   │
│   Seal Inspection &    │
│        Storage         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Acceptance Testing:   │
│  Thermally Grown SiO2  │
│       Etch Rate        │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Procedure

### Step 1: Technical Requisition Specification
1. **Chemical Formulation Verification**: Requisition pre-mixed electronic-grade BOE 6:1 consisting precisely of:
   - **6 parts by volume $40\%\ \text{NH}_4\text{F}$** (Ammonium Fluoride, electronic grade).
   - **1 part by volume $49\%\ \text{HF}$** (Hydrofluoric Acid, electronic grade).
2. **Surfactant Additive Option**: Verify if the chemical solution includes pre-dosed surfactant or order separately:
   - **$0.1\%$ Triton X-100 or Fluorad** wetting agent to eliminate bubble entrapment across high-aspect-ratio micro-trenches and bitline contact vias.
3. **Mandatory Safety Supplies Requisition**:
   - Issue purchase orders for fresh **Calcium Gluconate Gel ($2.5\%$)** in unexpired tubes for immediate skin contact decontamination.
   - Requisition HF-rated personal protective equipment (PPE): Heavy neoprene / butyl gloves, face shields, and chemical aprons.

### Step 2: Vendor Audit & Certificate of Analysis (COA) Review
1. Inspect vendor Certificate of Analysis (COA) for each chemical lot prior to container unloading.
2. Confirm component assays comply with $40.0\% \pm 0.5\%\ \text{NH}_4\text{F}$ and $49.0\% \pm 0.5\%\ \text{HF}$.
3. Verify trace metal impurities and particulate counts satisfy ultra-clean requirements for 180nm gate dielectric ($~3.5\text{ nm}$ physical thickness) and storage capacitor dielectric interfaces.

### Step 3: Safety Supplies Verification & Wet Bench Staging
1. Cross-examine expiration dates of incoming **Calcium Gluconate Gel** lots (minimum 12 months shelf-life remaining).
2. Distribute and mount calcium gluconate gel kits directly at all chemical receiving docks, acid transfer stations, and the wet bench chemical cabinet.
3. Verify eye-wash and safety shower flow rates and accessibility.

### Step 4: Physical Receiving, Container Integrity & Storage
1. Inspect container seals (fluoropolymer / HDPE drums or bottles) for zero leakage, bulges, or acid fume crystallization.
2. Verify secondary containment pallets are acid-compatible and rated for total stored chemical volume.
3. Transfer BOE 6:1 containers to dedicated acid storage cabinets maintained at $18^\circ\text{C} - 25^\circ\text{C}$, segregated strictly from bases, organic solvents, and oxidizers.

### Step 5: Incoming Quality Control (IQC) Acceptance Etch Rate Test
1. Prepare a pilot test bath with the received BOE 6:1 lot at calibrated temperature **$25.0^\circ\text{C} \pm 0.5^\circ\text{C}$**.
2. Submerge a test wafer with known thermally grown $\text{SiO}_2$ for a timed duration (e.g., 60 seconds).
3. Measure pre- and post-etch oxide thickness using spectroscopic ellipsometry.
4. Verify the baseline etch rate settles within $100\text{ nm/min} \pm 5\text{ nm/min}$ ($1000\ \text{\AA/min} \pm 50\ \text{\AA/min}$).

---

## 4. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Target Value | Tolerance | Measurement Method / Tool |
| :--- | :--- | :--- | :--- |
| **Thermally Grown $\text{SiO}_2$ Etch Rate** | $100\text{ nm/min}$ ($1000\ \text{\AA/min}$) | $\pm 5\text{ nm/min}$ | Spectroscopic Ellipsometry / Film Thickness Metrology |
| **IQC Test Bath Temperature** | $25.0^\circ\text{C}$ | $\pm 0.5^\circ\text{C}$ | In-situ calibrated RTD / Thermocouple probe |
| **Chemical Mixing Volumetric Ratio** | $6:1$ ($40\%\ \text{NH}_4\text{F} : 49\%\ \text{HF}$) | $\pm 1.0\%$ relative volume | Vendor COA Titration / Specific Gravity Hydrometer |
| **Surfactant / Wetting Agent Concentration** | $0.1\%$ (Triton X-100 or Fluorad) | $\pm 0.01\%$ | Gravimetric dispensing metrology / HPLC |
| **Safety Inventory Availability (Calcium Gluconate Gel)** | $\ge 2\text{ unexpired tubes/station}$ | Minimum $100\%$ compliance | Barcode visual audit / EHS physical checklist |

---

## 5. Metric Visualization

```text
                     ┌─────────────────────────────────┐
                     │█████████████████████████████████│
   Etch Rate (nm/min)┤█████████████████████████████████│
                     │▓▓▓▓▓▓▓▓▓                        │
 Bath Temp Target (C)┤▓▓▓▓▓▓▓▓▓                        │
Therm SiO2 Thick (nm)┤▒▒                               │
                     │▒▒                               │
Surfactant Dosing (%)┤░                                │
                     │░                                │
                     └┬───────┬───────┬───────┬───────┬┘
                      0      25      50      75     100 
```

---

## 6. Citations & Literature Context
- **Silicon Dioxide Etching with Buffered Oxide Etch (BOE)**:
  - Chemical formulation: 6 parts $40\%\ \text{NH}_4\text{F}$ (Ammonium Fluoride) and 1 part $49\%\ \text{HF}$ (Hydrofluoric Acid).
  - Thermal $\text{SiO}_2$ etch rate: $\approx 100\text{ nm/min}$ ($1000\ \text{\AA/min}$) at $25^\circ\text{C}$.
  - Surfactant dosing: $0.1\%$ Triton X-100 or Fluorad wetting agent to eliminate bubble entrapment in micro-trenches.
  - Mandatory EHS safety: Calcium gluconate gel must be present at all times due to HF skin penetration and calcium binding.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - Thermally grown $\text{SiO}_2$ gate dielectric physical thickness: $\approx 3.5\text{ nm}$ grown at $850^\circ\text{C} - 900^\circ\text{C}$ dry oxidation.
  - Bitline and wordline pitch: $360\text{ nm} - 400\text{ nm}$.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Unit cell geometry: Channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$, stacked capacitor over bitline (COB) architecture.

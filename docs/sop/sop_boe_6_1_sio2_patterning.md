# Standard Operating Procedure (SOP): Buffered Oxide Etch (BOE 6:1) SiO2 Patterning

- **Date**: 2026-10-11
- **Domain**: DRAM Foundation VN — 180nm Open-Source DRAM Chip Architecture & Integration
- **Generation**: Gen 1 (mm)
- **Module**: Chemical Processing / Wet Etch
- **Action Type**: Make

---

## 1. Process Overview & Objectives
This Standard Operating Procedure defines the wet chemical patterning and stripping of silicon dioxide ($SiO_2$) layers using Buffered Oxide Etch (BOE 6:1) in a 180nm DRAM node cell layout fabrication. The procedure provides precise oxide removal with stable etch rates, uniform micro-trench wetting, and maximum photoresist adhesion.

---

## 2. Process Flow Diagram

```text
┌────────────────────────┐
│   HMDS Vapor Prime @   │
│         120°C          │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│      Photoresist       │
│  Coating & Patterning  │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Safety Gate Check:   │
│ Calcium Gluconate Gel  │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   BOE 6:1 Bath Prep    │
│ (6:1 NH4F:HF + 0.1%    │
│  Surfactant @ 25°C)    │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Timed Wet Etching:   │
│  ~100 nm/min Rate      │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│ Quick Dump Rinse (QDR) │
│    & N2 Spin Rinse     │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│ Optical/Ellipsometric  │
│  Thickness Validation  │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Substrate Surface Adhesion Preparation
1. Load wafer into the vapor prime chamber.
2. Execute Hexamethyldisilazane (HMDS) vapor prime at **120°C** to dehydrate the surface and form a hydrophobic monolayer, ensuring photoresist adhesion during BOE immersion.
3. Apply standard photoresist coat, soft bake, lithographic exposure, post-exposure bake, and develop steps to pattern the $SiO_2$ windows.

### Step 2: Safety Verification & Personal Protective Equipment (PPE)
1. Verify presence of unexpired **Calcium Gluconate Gel** at the wet chemical bench station before any chemical handling (critical safety requirement against HF tissue penetration and calcium depletion).
2. Don acid-resistant chemical apron, sleeve covers, heavy-duty neoprene/nitrile gloves, and face shield.

### Step 3: BOE 6:1 Bath Preparation & Thermal Stabilization
1. Prepare or verify the composition of the Buffered Oxide Etch solution:
   - **6 parts** 40% Ammonium Fluoride ($NH_4F$)
   - **1 part** 49% Hydrofluoric Acid ($HF$)
2. Dose bath with **0.1%** wetting agent (Triton X-100 or Fluorad) to reduce surface tension and eliminate bubble entrapment in high-aspect micro-trenches.
3. Regulate and stabilize wet bench bath temperature at **25°C**.

### Step 4: Timed Chemical Etching
1. Immerse wafer cassette gently into the stabilized BOE bath with continuous laminar agitation.
2. Maintain immersion according to target film thickness, referencing the nominal etch rate of **100 nm/min (1000 Å/min)** for thermally grown $SiO_2$.

### Step 5: Quench, Cascade Rinse, and Dry
1. Immediately transfer cassette from BOE bath to the Quick Dump Rinse (QDR) / Cascade DI water overflow bath (< 5 seconds transfer time).
2. Rinse until bath resistivity reaches > 15 MΩ·cm.
3. Spin-rinse dry under heated high-purity $N_2$.

---

## 4. Machine-Measurable Acceptance Criteria Target Metrics

| Parameter | Nominal Target | Tolerance / Range | Measurement Instrument |
| :--- | :--- | :--- | :--- |
| **Thermally Grown $SiO_2$ Etch Rate** | **100 nm/min** (1000 Å/min) | $\pm 5$ nm/min | Spectroscopic Ellipsometry |
| **Etch Bath Temperature** | **25.0 °C** | $\pm 0.5$ °C | Inline RTD / Thermocouple |
| **HMDS Vapor Prime Temperature** | **120 °C** | $\pm 2$ °C | Chamber Thermal Controller |
| **Wetting Agent Concentration** | **0.1 %** (Triton X-100 / Fluorad) | $0.08\% - 0.12\%$ | Inline Dosing / Titration |

```text
                     BOE 6:1 Process Metrics          
           ┌─────────────────────────────────────────┐
 Surfactant┤░                                        │
           │░                                        │
  HMDS Temp┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
           │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
  Etch Temp┤▓▓▓▓▓▓▓▓▓                                │
Target Rate┤██████████████████████████████████       │
           │██████████████████████████████████       │
           └┬─────────┬─────────┬─────────┬─────────┬┘
            0        30        60        90       120 
```

---

## 5. Citations & Context Traceability
- **[Source: Silicon Dioxide Etching with Buffered Oxide Etch (BOE)]**: Chemical formulation (6:1 40% $NH_4F$ : 49% $HF$), thermal $SiO_2$ etch rate (100 nm/min / 1000 Å/min at 25°C), surfactant wetting requirement (0.1% Triton X-100 or Fluorad), HMDS vapor prime temperature (120°C), and mandatory safety protocol (Calcium Gluconate gel).
- **[Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering]**: Integration context for gate dielectric thermal $SiO_2$ thickness (~3.5 nm grown at 850°C–900°C) and cell layout features.

# Standard Operating Procedure (SOP): Buffered Oxide Etch (BOE 6:1) SiO2 Patterning

- **Date**: 2026-10-09
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 1 (mm) / 180nm Open-Source DRAM Architecture
- **Action Type**: Make

---

## 1. Scope & Objective
This SOP defines the wet chemical etching procedure for patterning silicon dioxide ($\text{SiO}_2$) layers (including pad oxide and gate dielectric isolation boundaries) using Buffered Oxide Etch (BOE 6:1) in a 180nm open-source DRAM fabrication flow.

---

## 2. Process Flow Diagram

```text
┌────────────────────────┐
│                        │
│   HMDS Vapor Prime @   │
│          120C          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   PR Coat & Exposure   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  BOE 6:1 Bath @ 25C +  │
│   0.1% Wetting Agent   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  DI Water Rinse & N2   │
│          Dry           │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Procedure

### Step 1: Surface Preparation & Adhesion Promotion
1. Transfer wafer cassettes to the vapor priming chamber.
2. Subject wafers to **Hexamethyldisilazane (HMDS)** vapor prime at **$120^\circ\text{C}$** to dehydrate the surface and promote photoresist adhesion against BOE wet undermining.
3. Spin-coat photoresist, soft-bake, expose using reticle mask (pitch: $360\text{ nm} - 400\text{ nm}$), post-exposure bake, and develop patterns.

### Step 2: Chemical Bath Preparation & Safety Pre-Check
1. Confirm that **calcium gluconate gel** is stocked, inspected, and immediately accessible at the wet bench.
2. Prepare or verify the premixed BOE solution composed of **$6\text{ parts } 40\% \text{ NH}_4\text{F}$** and **$1\text{ part } 49\% \text{ HF}$**.
3. Incorporate **$0.1\%$ Triton X-100 or Fluorad** wetting agent into the chemical bath to prevent bubble entrapment in high-aspect-ratio micro-trenches.
4. Stabilize the chemical recirculating bath temperature at **$25^\circ\text{C} \pm 0.5^\circ\text{C}$** to ensure stable pH and uniform etch rates.

### Step 3: Buffered Oxide Etching
1. Calculate the required immersion duration based on the film thickness (e.g., thermally grown $\text{SiO}_2$ at an etch rate of $\approx 100\text{ nm/min}$ / $1000\text{ \AA/min}$, or gate dielectric target physical thickness of $\approx 3.5\text{ nm}$).
2. Load wafer boat into the BOE 6:1 bath with moderate, continuous bath agitation.
3. Etch for the calibrated duration while monitoring chemical bath temperature.

### Step 4: Quench, Rinse & Dry
1. Immediately transfer the wafer carrier into the Quick Dump Rinse (QDR) bath charged with high-purity deionized (DI) water.
2. Cycle dump rinse 4-5 times until resistivity reaches $> 18\text{ M}\Omega\cdot\text{cm}$.
3. Transfer wafers to a spin rinse dryer (SRD) and dry under filtered $\text{N}_2$ flow.

---

## 4. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Target Value | Tolerance | Measurement Method / Tool |
| :--- | :--- | :--- | :--- |
| **BOE 6:1 Chemical Bath Temperature** | $25.0^\circ\text{C}$ | $\pm 0.5^\circ\text{C}$ | In-situ RTD / Thermocouple Sensor |
| **Thermally Grown $\text{SiO}_2$ Etch Rate** | $100\text{ nm/min}$ ($1000\text{ \AA/min}$) | $\pm 5\text{ nm/min}$ | Spectroscopic Ellipsometry / Film Thickness Metrology |
| **HMDS Vapor Prime Temperature** | $120^\circ\text{C}$ | $\pm 2^\circ\text{C}$ | Chamber Thermocouple / Pyrometer |
| **Surfactant / Wetting Agent Concentration** | $0.1\%$ (Triton X-100 / Fluorad) | $\pm 0.01\%$ | Dosing metrology / Gravimetric control |

---

## 5. Metric Visualization

```text
                             ┌─────────────────────────┐
                             │░░                       │
       Gate Oxide Target (nm)┤░░                       │
                             │▒▒▒▒▒▒                   │
           Etch Bath Temp (C)┤▒▒▒▒▒▒                   │
          HMDS Prime Temp (C)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                             │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
Therm SiO2 Etch Rate (nm/min)┤█████████████████████    │
                             │█████████████████████    │
                             └┬─────┬─────┬─────┬─────┬┘
                              0    30    60    90   120 
```

---

## 6. Citations & Literature Context
- **Silicon Dioxide Etching with Buffered Oxide Etch (BOE)**: Formulations (6:1 $40\% \text{ NH}_4\text{F} : 49\% \text{ HF}$), thermal $\text{SiO}_2$ etch rate ($100\text{ nm/min}$ at $25^\circ\text{C}$), surfactant requirement ($0.1\%$ Triton X-100 / Fluorad), HMDS prime condition ($120^\circ\text{C}$), and mandatory safety protocols (calcium gluconate gel).
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry ($L = 180\text{ nm}, W = 220\text{ nm}$), 8F² / 6F² folded bitline architecture, stacked capacitor over bitline (COB).
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: Pitch guidelines ($360\text{ nm} - 400\text{ nm}$) and thermal gate oxide thickness ($\approx 3.5\text{ nm}$).

# SOP: Pre- and Post-Clean Laser Surface Particle Counting (PRE) Qualification

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Action Type**: Make
- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm Dry Gate Oxide Growth (3.5 nm) [Thermal Processing] > Pre-Oxidation RCA Clean and In-Situ HF Dip Surface Preparation [Wet Chemistry] > RCA-1 (SC-1) Organic & Particle Removal Bath Formulation and Bench Qualification [Wet Chemistry] > RCA-1 (SC-1) Chemical Mixing Formulation and Thermal Stability Bench Qualification [Wet Chemistry] > Post-SC-1 Megasonic Bath Particle Removal Efficiency & Surface Roughness Qualification [Metrology] > Pre- and Post-Clean Laser Surface Particle Counting (PRE) Qualification [Metrology]

---

## 1. Overview & Operational Objectives

This Standard Operating Procedure (SOP) defines the protocol for qualifying **Particle Removal Efficiency (PRE)** across the RCA-1 (SC-1) and dilute HF pre-gate clean sequence using automated laser surface particle scanning metrology.

In a 180nm DRAM architecture with stacked capacitor over bitline (COB) topology, access transistors feature channel length $L = 180\text{ nm}$ and width $W = 220\text{ nm}$. Prior to growing the thin $3.5\text{ nm}$ dry gate oxide, particulate contamination creates fatal gate oxide pinholes, non-uniform dielectric breakdown, and junction leakage exceeding the cell leakage budget ($< 1\text{ fA/cell}$ at $85^\circ\text{C}$). High-precision laser particle counting and wafer coordinate mapping before and after cleaning qualify cleaning bath efficacy and prevent defect propagation into oxidation furnaces.

```text
┌────────────────────────┐
│                        │
│   Pre-Clean Incoming   │
│       Laser Scan       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    RCA-1 Megasonic     │
│     Clean: 70C-80C     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  DI Water Dump Rinse:  │
│      18.2 MOhm-cm      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Dilute HF Native    │
│    Oxide Dip: 1:50     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Post-Clean Laser    │
│   Scan & Coordinate    │
│        Matching        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   PRE Calculation &    │
│     SPC Validation     │
│                        │
└────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Pre-Clean Metrology Baseline Scan
1. Transfer test wafers (qualification monitor wafers with pre-deposited challenge silicon nitride / silica spheres or incoming production monitor wafers) to the laser surface particle counter load port.
2. Align wafer notch/flat and execute darkfield laser surface inspection across the full active wafer area (3 mm edge exclusion).
3. Record baseline particle coordinate map and bin particle counts:
   - $N_{\text{pre}}$ (total particle count at optical equivalent diameter $\ge 0.18\ \mu\text{m}$, matched to the 180nm critical dimension).
   - Export coordinates $(x_i, y_i)$ into metrology database.

### Step 2: Wet Chemical Cleaning & Rinse Processing
1. **RCA-1 (SC-1) Megasonic Clean**:
   - Submerge wafer cassette into fresh RCA-1 solution formulated at $5:1:1\ \text{DI H}_2\text{O} : \text{NH}_4\text{OH}\,(29\%) : \text{H}_2\text{O}_2\,(30\%)$.
   - Maintain bath temperature strictly at **$70^\circ\text{C} - 80^\circ\text{C}$** for **$10 - 15\text{ minutes}$** with continuous megasonic agitation.
2. **Intermediate Dump Rinse**:
   - Transfer to quick-dump rinser using high-purity deionized water ($18.2\ \text{M}\Omega\cdot\text{cm}$) for **$3\text{ minutes}$** to quench reaction and flush boundary chemicals.
3. **Dilute Hydrofluoric Dip**:
   - Dip wafer in **$1:50\ \text{HF} : \text{H}_2\text{O}$** for **$15 - 30\text{ seconds}$** to strip native chemical oxide and convert surface from hydrophilic to hydrophobic passivated termination.
4. **Final Rinse & Dry**:
   - Final dump rinse with $18.2\ \text{M}\Omega\cdot\text{cm}$ DI water followed by high-purity filtered $\text{N}_2$ spin-rinse dry.

### Step 3: Post-Clean Metrology Scan & Defect Pairing
1. Load dried wafers into the laser particle scanner within $< 30\text{ minutes}$ of cleaning to avoid cleanroom airborne fallout.
2. Run post-clean inspection using identical optical sensitivity and recipe settings as Step 1.
3. Record post-clean particle count $N_{\text{post}}$ and coordinate locations.
4. Perform software coordinate matching (spatial tolerance radius $\le 0.5\text{ mm}$) to classify:
   - **Removed particles** ($N_{\text{removed}}$)
   - **Remaining incoming particles** ($N_{\text{residual}}$)
   - **New adders** ($N_{\text{adder}}$)

### Step 4: Particle Removal Efficiency (PRE) Calculation & SPC Gating
1. Compute Particle Removal Efficiency according to:
   $$\text{PRE} = \left(\frac{N_{\text{pre}} - N_{\text{residual}}}{N_{\text{pre}}}\right) \times 100\%$$
   *(or $\text{PRE}_{\text{net}} = \frac{N_{\text{pre}} - N_{\text{post}}}{N_{\text{pre}}} \times 100\%$ where $N_{\text{post}} = N_{\text{residual}} + N_{\text{adder}}$).*
2. Verify all metrics against Statistical Process Control (SPC) thresholds before releasing downstream $3.5\text{ nm}$ dry thermal gate oxidation furnaces.

---

## 3. Acceptance Criteria & Target Metrics

| Parameter | Target Specification | Physical Units | Verification Method |
| :--- | :--- | :--- | :--- |
| **RCA-1 Bath Temperature** | $70.0 - 80.0$ | $^\circ\text{C}$ | Calibrated in-situ quartz-sheathed RTD / thermocouple probe |
| **Intermediate Rinse Water Resistivity** | $\ge 18.2$ | $\text{M}\Omega\cdot\text{cm}$ | In-line resistivity sensor in dump rinse manifold |
| **Dilute HF Dip Residence Time** | $15.0 - 30.0$ | $\text{s}$ | Automated robotic wet bench immersion timer ($1:50\ \text{HF:H}_2\text{O}$) |
| **Particle Removal Efficiency (PRE @ $\ge 180\text{ nm}$)** | $\ge 95.0\%$ (Adder Delta $\le 5$ particles/wafer) | $\%$ / counts | Pre- and post-clean laser scattering particle counter |

```text
                                                        
                  ┌────────────────────────────────────┐
                  │░                                   │
 Adder Delta (Max)┤░                                   │
  Post-Clean (Max)┤▒▒▒                                 │
                  │▒▒▒                                 │
Pre-Clean (Target)┤████████████████████████████████████│
                  │████████████████████████████████████│
                  └┬────────┬────────┬───────┬────────┬┘
                   0       250      500     750    1000 
```

---

## 4. Source Citations & References
- **Standard RCA-1 and RCA-2 Silicon Wafer Cleaning Procedure**: RCA-1 formulation ($5:1:1\ \text{DI H}_2\text{O} : 29\%\ \text{NH}_4\text{OH} : 30\%\ \text{H}_2\text{O}_2$), process temperature ($70^\circ\text{C}-80^\circ\text{C}$, $10-15\text{ min}$), intermediate dump rinse ($18.2\ \text{M}\Omega\cdot\text{cm}$ DI water, $3\text{ min}$), and native oxide strip ($1:50\ \text{HF}:\text{H}_2\text{O}$, $15-30\text{ s}$).
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$), cell leakage target ($< 1\text{ fA/cell}$ at $85^\circ\text{C}$), and soft-error immunity capacitance budget ($28\text{ fF/cell}$).
- **Silicon Dioxide Etching with Buffered Oxide Etch (BOE)**: Hydrofluoric acid handling precautions, safety protocol, and native oxide strip chemistry.

# Standard Operating Procedure (SOP): Semiconductor-Grade Reagents and Megasonic Immersion Bath Equipment Procurement

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Architecture
- **Action Type**: Make
- **Context Level**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm Dry Gate Oxide Growth (3.5 nm) [Thermal Processing] > Pre-Oxidation RCA Clean and In-Situ HF Dip Surface Preparation [Wet Chemistry] > RCA-1 (SC-1) Organic & Particle Removal Bath Formulation and Bench Qualification [Wet Chemistry] > Semiconductor-Grade Reagents and Megasonic Immersion Bath Equipment Procurement [Wet Chemistry]

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) governs the technical specification, supplier qualification, procurement, incoming physical quality inspection (IQC), and bench qualification of electronic/semiconductor-grade chemical reagents ($29\%\ \text{NH}_4\text{OH}$, $30\%\ \text{H}_2\text{O}_2$, $18.2\ \text{M}\Omega\cdot\text{cm}$ DI water integration) and megasonic-assisted wet immersion tank equipment. These materials and hardware are required for the standard RCA-1 (Standard Clean 1 / SC-1) formulation bench to perform organic film strip and sub-micron particle removal prior to 3.5 nm dry gate oxide growth on 180nm DRAM wafers.

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│    Spec Requisition    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       Vendor COA       │
│       Validation       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Safety & PPE Staging  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Physical Receiving &  │
│          IQC           │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Megasonic Bath     │
│     Qualification      │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Technical Requisition Specification
1. **Reagent Chemistry Specifications**: Requisition semiconductor-grade (SEMI Tier 1 / Grade 1) reagents compliant with RCA-1 volumetric mixing ratios ($5:1:1\ \text{DI H}_2\text{O}:\text{NH}_4\text{OH}:\text{H}_2\text{O}_2$):
   - **Ammonium Hydroxide ($\text{NH}_4\text{OH}$)**: Assay concentration $29.0\% \pm 0.5\%$, electronic/trace metal grade (<10 ppb trace cation impurities).
   - **Hydrogen Peroxide ($\text{H}_2\text{O}_2$)**: Assay concentration $30.0\% \pm 0.5\%$, unstabilized or electronic-grade (<10 ppb trace metals).
   - **Deionized (DI) Water Supply**: Point-of-use polishing line interface delivering ultra-pure water with resistivity $\ge 18.2\ \text{M}\Omega\cdot\text{cm}$ at $25^\circ\text{C}$.
2. **Megasonic Immersion Bath Equipment Specifications**:
   - **Tank Construction**: High-purity PFA (perfluoroalkoxy) or seamless electropolished quartz vessel resistant to alkaline/peroxide oxidation up to $90^\circ\text{C}$.
   - **Megasonic Transducer Array**: Direct-bonded or bottom-mounted transducer operating in the megasonic acoustic frequency regime ($800\ \text{kHz} - 1.2\ \text{MHz}$) to ensure uniform sub-micron particle acoustic streaming without gate oxide cavitation damage.
   - **Inline Immersion Heater & Recirculation**: PFA-sheathed immersion heating element with closed-loop PID temperature controller capable of steady maintenance between $70^\circ\text{C}$ and $80^\circ\text{C}$.
   - **N2 Purge & Exhaust Porting**: Integrated nitrogen ($N_2$) blanket shroud and rear plenum exhaust interface for volatile ammonia ($NH_3$) vapor containment.

### Step 2: Vendor Qualification & Certificate of Analysis (COA) Verification
1. Verify vendor Certificates of Analysis (COA) for each chemical lot prior to receipt authorization.
2. Confirm ionic trace metal contents ($\text{Fe}, \text{Cu}, \text{Ni}, \text{Na}, \text{K}, \text{Ca}$) are strictly $< 10\ \text{ppb}$ per element to eliminate deep-level trap and gate dielectric breakdown precursors.
3. Validate packaging integrity: Heavy-duty fluoropolymer (HDPE/PFA) bottles sealed with tamper-evident dual caps and double-bagged cleanroom wrapping.

### Step 3: Cleanroom Receiving, Physical IQC & Secondary Containment
1. Unpack chemical shipments in cleanroom sub-fab receiving bay; inspect exterior containers for leakage, bulging, or chemical precipitation.
2. Transfer chemical bottles into designated flammables/corrosives secondary containment cabinets equipped with dedicated exhaust plenums:
   - Store $\text{NH}_4\text{OH}$ (base) separately from acids.
   - Store $\text{H}_2\text{O}_2$ (oxidizer) in vented secondary containment away from reducing agents and organic solvents.
3. Megasonic Tank Inspection: Conduct mechanical fit check, helium leak check on plumbing joints, and electrical grounding inspection of transducer power generators.

### Step 4: Megasonic Immersion Bath Hardware Installation & Power Benchmarking
1. Mount the immersion bath within the wet bench wet station deck; connect quick-disconnect PFA fluid lines to the DI water feed ($18.2\ \text{M}\Omega\cdot\text{cm}$) and waste neutralization drain.
2. Connect RF generator cables to the bottom-plate megasonic transducer assembly.
3. Fill tank with $18.2\ \text{M}\Omega\cdot\text{cm}$ DI water to operational level sensor mark; power on the megasonic generator at rated setpoint power ($200\text{--}400\ \text{W}$) and verify uniform acoustic sound field using a calibrated hydrophone or aluminum foil acoustic cavitation map.

### Step 5: Thermal & Formulation Bench Run Validation
1. Formulate test bath with standard RCA-1 recipe: $5\ \text{parts DI H}_2\text{O}$, $1\ \text{part } 29\%\ \text{NH}_4\text{OH}$, $1\ \text{part } 30\%\ \text{H}_2\text{O}_2$.
2. Engage immersion heater PID loop set to $75^\circ\text{C}$.
3. Verify bath stabilization within the specified operating temperature window ($70^\circ\text{C}\text{--}80^\circ\text{C}$) for $10\text{--}15\ \text{minutes}$.
4. Verify exhaust plenum face velocity ($\ge 100\ \text{FPM}$) preventing ammonia vapor build-up in operator breathing zones.

---

## 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Tolerance / Range | Physical Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Ammonium Hydroxide ($\text{NH}_4\text{OH}$) Assay** | $29.0$ | $\pm 0.5$ | $\%$ | Acid-base titration / Vendor COA validation |
| **Hydrogen Peroxide ($\text{H}_2\text{O}_2$) Assay** | $30.0$ | $\pm 0.5$ | $\%$ | Iodometric / Redox titration / Vendor COA |
| **Point-of-Use DI Water Resistivity** | $18.2$ | $\ge 18.2$ | $\text{M}\Omega\cdot\text{cm}$ | Inline calibrated conductivity/resistivity probe ($25^\circ\text{C}$) |
| **RCA-1 Operating Bath Temperature** | $75.0$ | $70.0\text{--}80.0$ | $^\circ\text{C}$ | Immersion RTD / PFA-sheathed thermocouple probe |
| **Process Immersion Cycle Duration** | $12.5$ | $10.0\text{--}15.0$ | $\text{minutes}$ | Digital process automation sequence timer |

```text
                               Acceptance Target Metrics
                              ┌────────────────────────┐
                              │░░░░░░░░░░              │
                H2O2 Assay (%)┤░░░░░░░░░░              │
                              │▒▒▒▒▒▒▒▒▒▒              │
               NH4OH Assay (%)┤▒▒▒▒▒▒▒▒▒▒              │
       RCA-1 Bath Temp (deg C)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                              │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
DI Water Resistivity (MOhm-cm)┤███████                 │
                              │███████                 │
                              └┬─────┬─────┬────┬─────┬┘
                              0.0  18.8  37.5 56.2 75.0 
```

---

## 5. Environmental Health & Safety (EHS) and Hazard Mitigation
1. **Chemical Handling PPE**: Heavy-duty neoprene or butyl rubber apron, sleeve guards, full-face polycarbonate shield, and chemical-resistant gloves (Viton or heavy nitrile).
2. **Incompatible Materials Segregation**: Do not mix concentrated $\text{H}_2\text{O}_2$ with organic solvents or metals to avoid runaway exothermic decomposition.
3. **Spill & Exposure Protocols**:
   - Provide eye-wash stations and emergency drench showers within 10 seconds unhindered reach.
   - For ammonia vapor release, maintain emergency cleanroom evacuation protocol if scrubber exhaust drops below $80\ \text{CFM}$.

---

## 6. Literature Citations & Traceability
- **[Standard RCA-1 and RCA-2 Silicon Wafer Cleaning Procedure]**: Defines RCA-1 (SC-1) bath volumetric chemistry ($5\ \text{parts DI H}_2\text{O} : 1\ \text{part } 29\%\ \text{NH}_4\text{OH} : 1\ \text{part } 30\%\ \text{H}_2\text{O}_2$), process operating temperature ($70^\circ\text{C}\text{--}80^\circ\text{C}$), immersion cleaning window ($10\text{--}15\ \text{minutes}$), and dump rinse resistivity requirement ($18.2\ \text{M}\Omega\cdot\text{cm}$ DI water).
- **[180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench]**: Details access transistor dimensions ($L = 180\ \text{nm}, W = 220\ \text{nm}$) and ultra-low leakage requirements ($< 1\ \text{fA/cell}$ at $85^\circ\text{C}$), mandating zero ionic contamination and rigorous particle removal prior to 3.5 nm dry gate oxidation.
- **[Silicon Dioxide Etching with Buffered Oxide Etch (BOE)]**: Informs chemical compatibility standards, fluoropolymer materials selection, and safety baseline for wet chemistry bench environments.

# SOP: Access Transistor Gate Oxide & 180nm Channel Poly-1 Patterning

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council - Domain Expert AI)
- **Status**: Implemented
- **Process Node**: 180nm CMOS DRAM Generation 3
- **Cell Architecture**: 8F² Folded Bitline 1T1C Access Transistor Gate Stack

## Overview & Rationale
This Standard Operating Procedure (SOP) governs the formation of the ultra-thin gate dielectric layer (~3.5 nm thermally grown SiO₂) and subsequent Poly-1 deposition, lithography, and high-selectivity anisotropic plasma etching for 180nm gate length ($L = 180\text{ nm}$) access transistors. In 8F² DRAM cells, access transistors must withstand wordline overdrive voltages ($V_{PP} \ge 2.5\text{V to } 2.8\text{V}$) while maintaining sub-threshold/junction leakage $< 1\text{ fA/cell}$ at 85°C to preserve stored storage node charges ($C_{cell} \ge 25\text{ to } 30\text{ fF}$).

---

## Process Flow Diagram

```text
┌────────────────────────┐
│                        │
│    Pre-Gate Cleans:    │
│  RCA-1 + RCA-2 + DHF   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Dry Thermal Gate    │
│       Oxidation:       │
│   850C-900C, ~3.5 nm   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      LPCVD Poly-1      │
│  Deposition: ~150-200  │
│     nm + In-Situ P     │
│         Doping         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     DUV 248nm KrF      │
│   Lithography: L=180   │
│  nm, Pitch=360-400 nm  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Anisotropic ICP RIE:  │
│        Cl2/HBr         │
│    High-Selectivity    │
│       Poly Etch        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   In-Line Metrology:   │
│  CD-SEM, Ellipsometry  │
│      & Ig Leakage      │
│                        │
└────────────────────────┘
```

---

## Detailed Step-by-Step Procedure

### Step 1: Pre-Gate Pre-Clean & Native Oxide Strip
1. Perform RCA standard clean:
   - **RCA-1 (SC-1)**: $\text{NH}_4\text{OH} : \text{H}_2\text{O}_2 : \text{H}_2\text{O}$ (1:1:5) at 70°C for 10 minutes to remove organic surface particles.
   - **RCA-2 (SC-2)**: $\text{HCl} : \text{H}_2\text{O}_2 : \text{H}_2\text{O}$ (1:1:6) at 70°C for 10 minutes to strip ionic and metallic contaminants.
2. Dilute HF dip:
   - 0.5% DHF etch for 60 seconds to strip native oxide down to bare hydrophobic Si surface; DI water rinse until resistivity exceeds $18.2\text{ M}\Omega\cdot\text{cm}$; spin rinse dry (SRD) under $\text{N}_2$ purge.
   - Maximum queue time (Q-time) to oxidation furnace: $\le 60\text{ minutes}$.

### Step 2: Dry Thermal Gate Oxidation ($T_{ox} \approx 3.5\text{ nm}$)
1. Load wafers into a horizontal/vertical diffusion furnace under continuous $\text{N}_2$ ballast at 600°C.
2. Ramp furnace temperature to **850°C – 900°C**.
3. Conduct pure dry thermal oxidation with high-purity $\text{O}_2$ (and trace 0.5%–1.0% trans-1,2-dichloroethylene / DCE or HCl for metallic gettering) to grow **$\sim 3.5\text{ nm}$ physical $\text{SiO}_2$**.
4. In-situ anneal under pure $\text{N}_2$ ambient at 850°C for 15 minutes to reduce fixed oxide charges ($Q_{ss}$) and interface trap density ($D_{it} < 1 \times 10^{10}\text{ cm}^{-2}\text{eV}^{-1}$).
5. Ramp down to 600°C and unload in pure $\text{N}_2$ ambient. Maximum Q-time to Poly-1 deposition: $\le 120\text{ minutes}$.

### Step 3: Poly-1 Gate Deposition & In-Situ Doping
1. Load into Low-Pressure Chemical Vapor Deposition (LPCVD) reactor at 580°C – 620°C.
2. Deposit **150 nm to 200 nm** polycrystalline silicon using $\text{SiH}_4$ precursor.
3. Perform in-situ N+ phosphorus doping using $\text{PH}_3$ co-flow (or low-energy ion implantation: P⁺, $15\text{ keV}$, dose $5 \times 10^{15}\text{ cm}^{-2}$) to ensure heavy gate poly activation ($R_s \le 30\,\Omega/\Box$), eliminating poly-depletion effects under $V_{PP} = 2.5\text{V to } 2.8\text{V}$ overdrive.

### Step 4: Photolithography (248nm DUV KrF Exposure)
1. Apply organic Bottom Anti-Reflective Coating (BARC) with thickness optimized to minimize standing wave reflections.
2. Spin coat positive DUV photoresist to a nominal thickness of $\sim 350\text{ nm}$ and soft-bake at 100°C.
3. Expose wordline / gate patterns on a 248nm KrF excimer stepper/scanner using off-axis illumination (OAI) and phase-shift or binary reticle targeting:
   - Critical Dimension: **Channel length $L = 180\text{ nm}$**.
   - Active Area Transistor Width: **$W = 220\text{ nm}$**.
   - Wordline / Gate Pitch: **$360\text{ nm to } 400\text{ nm}$**.
4. Post-exposure bake (PEB) at 110°C; develop with 2.38% TMAH (Tetramethylammonium hydroxide); hard-bake at 110°C.

### Step 5: Anisotropic Poly-1 Reactive Ion Etching (RIE)
1. Etch organic BARC open using $\text{CF}_4 / \text{O}_2$ plasma.
2. Main poly etch in Inductively Coupled Plasma (ICP) RIE reactor:
   - Chemistries: $\text{Cl}_2 / \text{HBr} / \text{O}_2$ gas mixture.
   - Energetic anisotropic directional etch to pattern vertical gate sidewalls ($88^\circ - 90^\circ$).
3. Soft landing / Over-etch:
   - High selectivity chemistry ($\text{HBr} / \text{O}_2$) with $> 100:1$ selectivity to the underlying $3.5\text{ nm}$ gate oxide.
   - Endpoint detection (EPD) via optical emission spectroscopy (OES) monitoring the $288\text{ nm}$ Si line to prevent punch-through into the 180nm channel silicon active area.
4. Downstream oxygen plasma resist/BARC ash followed by wet clean (dilute EKC / SC-1 clean).

### Step 6: In-Line Metrology & Electrical Verification
1. Inspect etched gate profile and line CD across wafer with CD-SEM.
2. Measure physical thickness of unetched scribe-lane oxide pads using spectroscopic ellipsometry.
3. Perform preliminary gate leakage breakdown screening ($I_g$) and threshold voltage ($V_{th} = 0.5\text{V to } 0.7\text{V}$) qualification on test macro structures.

---

## Acceptance Criteria

| Parameter | Target Metric | Engineering Unit | Tolerance / Limit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Physical Gate Oxide Thickness ($T_{ox}$)** | **3.5** | **nm** | $\pm 0.2\text{ nm}$ ($3.3\text{ nm} - 3.7\text{ nm}$) | Spectroscopic Ellipsometry / TEM cross-section |
| **Access Transistor Channel Length ($L$)** | **180** | **nm** | $\pm 10\text{ nm}$ ($170\text{ nm} - 190\text{ nm}$) | In-line CD-SEM (3-sigma across wafer) |
| **Access Transistor Active Width ($W$)** | **220** | **nm** | $\pm 12\text{ nm}$ ($208\text{ nm} - 232\text{ nm}$) | In-line CD-SEM |
| **Wordline / Gate Pitch** | **360 – 400** | **nm** | Full pitch within $360\text{ to } 400\text{ nm}$ | CD-SEM Pitch Analysis |
| **Total Cell Leakage (Sub-threshold + Junction)** | **$< 1.0$** | **fA/cell** | Max $1.0\text{ fA/cell}$ at 85°C | In-line Parametric Test System (WAT) |
| **Access Transistor Threshold Voltage ($V_{th}$)** | **0.5 – 0.7** | **V** | NMOS enhancement baseline | In-line Parametric Test System (WAT) |

---

## Literature & Source Context Citations
1. **Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**
   - *“Gate dielectric is thermally grown silicon dioxide (SiO2) at 850°C-900°C dry oxidation with ~3.5 nm physical thickness.”*
   - *“Bitline and wordline pitch is approximately 360 nm to 400 nm.”*
   - *“The storage capacitor must maintain a minimum capacitance of 25 to 30 fF (femtofarads) per cell to ensure data retention time > 64 ms at 85°C.”*
2. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - *“Unit Cell Geometry: Access transistor channel length L = 180 nm, width W = 220 nm. Bitline contact shared between two adjacent memory cells.”*
   - *“Leakage Current Target: Sub-threshold and junction leakage must be kept below 1 fA/cell at 85°C to achieve refresh interval...”*
3. **Source: High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture**
   - *“In 180nm DRAM cells, the pass transistor is an NMOS enhancement device with threshold voltage V_th ~ 0.5V to 0.7V.”*
   - *“V_PP Overdrive Solution: The wordline driver must be supplied by an on-chip boosted high voltage: V_PP = V_DD + V_th + Delta V_overdrive >= 2.5V to 2.8V.”*

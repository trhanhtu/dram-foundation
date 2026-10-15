# Standard Operating Procedure (SOP)
## EBDW Exposure Matrix Execution & Resist Development Processing

- **Document ID:** SOP-LITH-EBDW-180-EM01
- **Process Generation:** 180nm Open-Source DRAM (Gen 3)
- **Hierarchy:** 180nm Open-Source DRAM Chip > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > Electron Beam Direct Write (EBDW) Lithography > HSQ/ZEP520A Resist Coating & PEC Modeling > Monte Carlo PSF Simulation and EBDW PEC Dose Modulation Modeling > 180nm Gate Pattern Dose Calibration & CD-SEM Linewidth Metrology Verification > EBDW Exposure Matrix Execution & Resist Development Processing
- **Action Type:** Make
- **Target Layer:** 180nm Critical Dimension Gates (Access Transistor Channel L = 180 nm, W = 220 nm; Minimum drawn poly gate length = 150 nm, minimum poly space = 210 nm)
- **Manufacturing Grid:** 0.005 µm (5 nm physical placement grid resolution)

---

### 1. Process Workflow

```text
┌──────────────────────┐
│                      │
│     Pre-Exposure     │
│      Inspection      │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│     Dose Matrix      │
│      Execution       │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│  Resist Development  │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│  DI Water Quench &   │
│      Post-Bake       │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│   CD-SEM Metrology   │
│                      │
└──────────────────────┘
```

---

### 2. Step-by-Step SOP Execution Procedure

1. **Substrate Pre-Conditioning & Film Verification**:
   - Verify post-spin coat thickness for negative tone resist (HSQ) at nominal $50\text{ nm} \pm 2\text{ nm}$ or positive tone resist (ZEP520A) at nominal $100\text{ nm} \pm 3\text{ nm}$ over the polysilicon gate stack ($150\text{ nm}$ poly-Si over $3.5\text{ nm}$ gate dielectric).
   - Ensure soft-bake thermal stabilization is completed prior to chamber load. For standard solvent desorption, bake at $115^\circ\text{C}$ for $60\text{ s}$ on a vacuum hotplate.
   - Clean backside and transfer wafer into the EBDW loadlock; pump vacuum chamber down to base operating pressure $\le 1.0 \times 10^{-6}\text{ mbar}$ ($\le 1.0 \times 10^{-4}\text{ Pa}$).

2. **Stage Alignment, Deflection Calibration & Grid Snapping**:
   - Execute automated laser interferometer stage coordinate alignment to global wafer alignment fiducials.
   - Align to active diffusion marks ensuring overlay registration within the permissible overlay budget ($\le 35\text{ nm}$).
   - Snap all layout coordinates, field boundaries, and fractured exposure shots strictly to the $0.005\ \mu\text{m}$ ($5\text{ nm}$) physical placement grid.
   - Set electron column accelerating voltage to $50\text{ keV}$ (or $100\text{ keV}$), beam current to $100\text{ pA} \pm 2\text{ pA}$, and aperture beam spot diameter to $\le 10\text{ nm}$.

3. **Dose Matrix (Exposure-Dose Array) Execution**:
   - Load the fractured DRAM 180nm access gate layout pattern containing the cell array ($L = 180\text{ nm}$, $W = 220\text{ nm}$, bitline contact pitch $\ge 340\text{ nm}$, poly spacing $\ge 210\text{ nm}$).
   - Configure an automated exposure matrix grid varying base dose ($D_0$) across columns and PEC contrast scaling across rows:
     - **For HSQ (Negative Resist):** Nominal dose range $D_0 = 350\ \mu\text{C/cm}^2$ to $650\ \mu\text{C/cm}^2$ in step increments of $25\ \mu\text{C/cm}^2$.
     - **For ZEP520A (Positive Resist):** Nominal dose range $D_0 = 80\ \mu\text{C/cm}^2$ to $160\ \mu\text{C/cm}^2$ in step increments of $5\ \mu\text{C/cm}^2$.
   - Execute writing sequence using vectorized beam deflection with dynamic beam focus and stigmation correction across each write field ($100\ \mu\text{m} \times 100\ \mu\text{m}$).

4. **Resist Development Processing**:
   - Vent loadlock with ultra-high purity $N_2$, unload wafer to cleanroom environment (Class 10 / ISO 4, temperature $21.0 \pm 0.5^\circ\text{C}$, relative humidity $45 \pm 5\%$).
   - **For HSQ Resist (Aqueous Alkaline Development):**
     - Immerse wafer into tetramethylammonium hydroxide (TMAH 25% w/w) developer solution at controlled temperature ($21.0 \pm 0.2^\circ\text{C}$) or salty developer ($1\text{ wt}\%\ \text{NaOH} + 4\text{ wt}\%\ \text{NaCl}$) for exactly $60\text{ s}$ with gentle mechanical agitation.
   - **For ZEP520A Resist (Solvent Development):**
     - Immerse in n-Amyl acetate (ZED-N50) for $60\text{ s}$ at $21.0^\circ\text{C}$, or alternatively utilize standard developer bath for $45\text{ to }60\text{ s}$.
   - Immediately transfer wafer to immersion cascade bath with high-purity Deionized (DI) water (or MIBK/IPA rinse for solvent-based development) for $60\text{ s}$ to rapidly quench development and halt chemical clearing.

5. **Post-Development Rinse, Marangoni Drying & Hard Bake**:
   - Perform overflowing cascade rinse with $18.2\ \text{M}\Omega\cdot\text{cm}$ DI water for $180\text{ s}$.
   - Dry wafer via automated Marangoni surface tension dryer or filtered ultra-pure $N_2$ blow gun directed from center to wafer edge at 15 psi to prevent resist pattern collapse.
   - Perform post-development bake on vacuum hotplate at $115^\circ\text{C}$ for $60\text{ s}$ to eliminate residual moisture and stabilize resist sidewall profiles prior to plasma etching.

6. **CD-SEM Metrology & Matrix Evaluation**:
   - Transfer wafer to in-line CD-SEM.
   - Perform automated linewidth measurements across 9 matrix dies (top, center, bottom, left, right field sites) on DRAM access transistor gate features ($L = 180\text{ nm}$) and minimum isolated/dense poly features ($150\text{ nm}$).
   - Record gate CD, Line-Edge Roughness ($3\sigma$ LER), and residual overlay registration error relative to active diffusion.

---

### 3. Machine-Measurable Acceptance Criteria Targets

```text
                       Lithography Tolerance Budgets    
                  ┌────────────────────────────────────┐
                  │░░░░░░                              │
    Grid Snap (nm)┤░░░░░░                              │
  Gate CD Dev (nm)┤███████████                         │
                  │███████████                         │
Overlay Error (nm)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                  │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                  └┬────────┬────────┬───────┬────────┬┘
                  0.0      8.8     17.5    26.2    35.0 
```

| Metric | Target Specification | Physical Unit | Measurement Tool / Inspection Method |
| :--- | :--- | :--- | :--- |
| **Critical Dimension (CD) Accuracy** | $180.0 \pm 5.0\text{ nm}$ (DRAM Access Gate); min drawn gate $\ge 150.0\text{ nm}$ | nm | Automated High-Resolution CD-SEM ($500\text{ V}$ beam voltage) |
| **Poly Gate to Active Overlay Error** | $|\Delta X|, |\Delta Y| \le 35.0$ | nm | Automated In-Line SEM / Optical Overlay Metrology System |
| **Feature Placement Grid Conformance** | Grid snapping residual $\equiv 0.0$ (Strict $5.0\text{ nm}$ integer boundary) | nm | GDSII/OASIS Fractured Stream Verification & EBDW Beam Step Generator |
| **Minimum Poly Pitch / Spacing** | Critical poly space $\ge 210.0\text{ nm}$; Metal 1 / active pitch compliance | nm | Top-down CD-SEM pitch scan across dense memory array |

---

### 4. Verified Literature References

1. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Physical placement grid resolution: $0.005\ \mu\text{m}$ ($5\text{ nm}$).
   - Minimum active diffusion width: $0.15\ \mu\text{m}$ ($150\text{ nm}$).
   - Minimum poly gate length: $0.15\ \mu\text{m}$ ($150\text{ nm}$).
   - Minimum poly gate spacing: $0.21\ \mu\text{m}$ ($210\text{ nm}$).
   - Maximum permissible overlay error between gate poly and active diffusion: $\le 35\text{ nm}$.
   - Minimum Metal 1 width: $0.14\ \mu\text{m}$ ($140\text{ nm}$); minimum Metal 1 pitch: $0.34\ \mu\text{m}$ ($340\text{ nm}$).

2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor channel length: $L = 180\text{ nm}$, width: $W = 220\text{ nm}$.
   - Memory cell layout: Folded bitline architecture with shared drain contact and stacked capacitor over bitline (COB).

3. **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**:
   - Thermal bake parameters: $115^\circ\text{C}$ for $60\text{ seconds}$ on flat aluminum hot plate.
   - Resist development & rinse discipline: $45\text{--}60\text{ seconds}$ developer exposure followed by thorough deionized (DI) water rinse.

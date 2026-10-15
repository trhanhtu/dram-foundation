# Standard Operating Procedure (SOP): EBDW Exposure Recipe Execution with Active Diffusion Overlay Alignment

- **Document ID:** SOP-LITH-EBDW-180-001
- **Domain:** DRAM Foundation VN / Photolithography & Direct Write
- **Generation:** Gen 3 (nm scale)
- **Action Type:** Make
- **Status:** Approved / Active

---

## 1. Process Overview & Objective
Execute Direct-Write Electron Beam Lithography (EBDW) with Proximity Effect Correction (PEC) on active diffusion layers for 180nm critical dimension poly gate patterning. This procedure guarantees critical dimension (CD) fidelity and overlay error suppression relative to prior active diffusion layer alignments.

```text
┌────────────────────────┐
│                        │
│    Substrate Prep &    │
│      Dehydration       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Resist Application &  │
│       Soft Bake        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Stage Vacuum Loading  │
│    & Mark Detection    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Active Diffusion    │
│  Overlay Calibration   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    EBDW PEC Recipe     │
│        Exposure        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Development &      │
│       Metrology        │
│                        │
└────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Substrate Dehydration & HMDS Priming
1. Place patterned active diffusion wafers into convection/vacuum oven.
2. Perform thermal dehydration bake at **150°C to 200°C for 30 minutes** to desorb physisorbed water molecules.
3. Transfer substrate to HMDS vapor chamber to reactively silylate hydrophilic silanol (`-Si-OH`) into hydrophobic methyl-siloxane (`-Si-O-Si(CH3)3`) bonds to maximize resist adhesion.

### Step 2: Resist Coat & Soft Bake
1. Chuck wafer onto spin coater. Dispense **2 to 3 mL** of resist (e.g., Shipley 1813 or targeted E-beam analog).
2. Execute spread cycle at **500 RPM for 5 seconds**.
3. Ramp at **10,000 RPM/s** to terminal speed of **4,000 RPM for 30 seconds** to establish a uniform film target of **1.30 µm ± 15 nm**.
4. Apply PGMEA solvent jet edge bead removal (EBR) to eliminate perimeter ridge beads.
5. Transfer wafer to flat aluminum vacuum hot plate; soft bake at **115°C for 60 seconds**.

### Step 3: Vacuum Chamber Loading & Mark Detection
1. Load wafer into the EBDW load lock chamber; pump down to operational vacuum level.
2. Initialize stage positioning and scan global fiducials and local active diffusion alignment marks.
3. Calculate translation ($\Delta X, \Delta Y$), rotation ($\theta$), and magnification/scaling factors against the active diffusion layer baseline.

### Step 4: PEC Grid Setup & Direct-Write Exposure
1. Load exposure vector database aligned to the manufacturing grid resolution of **0.005 µm (5 nm)**.
2. Activate Proximity Effect Correction (PEC) algorithms targeting minimum drawn poly gate length of **0.15 µm (150 nm)** and minimum poly gate spacing of **0.21 µm (210 nm)** over active diffusion widths ($\ge 0.15 \text{ µm}$).
3. Execute e-beam direct-write vector scan across chip dies with real-time laser interferometer stage feedback.

### Step 5: Post-Exposure Development & Inspection
1. Unload wafer to development track.
2. Immerse/puddle in **Microposit MF-319 developer for 45 to 60 seconds**.
3. Execute thorough deionized (DI) water cascade rinse for $\ge 60$ seconds, followed by high-purity spin dry with dry $N_2$.
4. Conduct critical dimension (CD-SEM) and overlay metrology.

---

## 3. Machine-Measurable Acceptance Criteria

```text
                      ┌────────────────────────────────┐
                      │░░                              │
        Grid Step (nm)┤░░                              │
                      │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
     Poly Spacing (nm)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
     Poly Gate CD (nm)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         │
                      │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         │
Max Overlay Error (nm)┤██████                          │
                      │██████                          │
                      └┬───────┬───────┬──────┬───────┬┘
                      0.0    52.5    105.0  157.5 210.0 
```

| Parameter Metric | Target Value | Physical Unit | Tolerance / Boundary | Verification Instrument |
| :--- | :--- | :--- | :--- | :--- |
| **Active-to-Poly Overlay Error** | $\le 35$ | nm | Maximum limit ($|\Delta X|, |\Delta Y| \le 35 \text{ nm}$) | Optical/SEM Overlay Tool |
| **Poly Gate Critical Dimension (CD)** | $150$ | nm ($0.15\text{ }\mu\text{m}$) | Drawn target CD | CD-SEM |
| **Minimum Poly Gate Spacing** | $210$ | nm ($0.21\text{ }\mu\text{m}$) | Minimum clearance | CD-SEM |
| **Manufacturing Placement Grid** | $5$ | nm ($0.005\text{ }\mu\text{m}$) | Physical snap grid | EBDW Pattern Generator |
| **Resist Film Thickness** | $1.30$ | $\mu\text{m}$ | $\pm 15$ nm | Spectroscopic Ellipsometry |

---

## 4. Literature & PDK Sources Citing
1. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Placement grid resolution: $0.005 \text{ }\mu\text{m}$ ($5\text{ nm}$).
   - Minimum active diffusion width: $0.15 \text{ }\mu\text{m}$ ($150\text{ nm}$).
   - Minimum poly gate length: $0.15 \text{ }\mu\text{m}$ ($150\text{ nm}$).
   - Minimum poly gate spacing: $0.21 \text{ }\mu\text{m}$ ($210\text{ nm}$).
   - Overlay error budget between gate poly and active diffusion: $\le 35\text{ nm}$.
2. **Photoresist Spin Coating Dynamics and HMDS Vapor Priming**:
   - Wafer dehydration bake: $150^\circ\text{C}-200^\circ\text{C}$ for $30\text{ minutes}$.
   - Spin recipe: Dispense $2-3\text{ mL}$, spread at $500\text{ RPM}$ for $5\text{ s}$, ramp at $10,000\text{ RPM/s}$ to $4,000\text{ RPM}$ for $30\text{ s}$.
   - Film thickness: $1.30\text{ }\mu\text{m} \pm 15\text{ nm}$.
   - Edge bead removal using PGMEA solvent jet.
3. **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**:
   - Soft bake: $115^\circ\text{C}$ for $60\text{ seconds}$ on flat aluminum hot plate.
   - Development: Microposit MF-319 for $45-60\text{ seconds}$ followed by rigorous DI water rinse.

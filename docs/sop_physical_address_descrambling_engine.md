# Standard Operating Procedure (SOP)
## Physical Address Descrambling & 2D Bit-Flip Topology Reconstruction Engine

- **Document ID:** SOP-DRAM-MET-004
- **Generation:** Gen 2 (µm) / 180nm DRAM Cell Architecture
- **Action Type:** Make
- **Discipline:** Metrology / Silicon Analytics

---

## 1. Scope & Objective
This Standard Operating Procedure establishes the protocol for mapping raw logical bit-flip fail logs (originating from retention pause audits and March test telemetry) to physical $(X, Y)$ coordinate space on the 180nm DRAM silicon die. It accounts for folded bitline routing, address multiplexer scrambles, and shared contact geometry to reconstruct accurate 2D spatial defect bitmaps.

---

## 2. Technical Context & Verified Parameters
- **Architecture**: 1T1C stacked capacitor over bitline (COB) folded bitline cell layout ($8F^2$ footprint).
- **Physical Cell Area**: $0.259\ \mu\text{m}^2$ ($8F^2$ at $F = 180\ \text{nm}$, or $0.194\ \mu\text{m}^2$ for open $6F^2$).
- **Array Pitches**: Wordline (WL) and Bitline (BL) pitch range of $360\ \text{nm}$ to $400\ \text{nm}$.
- **Access Transistor Dimensions**: Channel length $L = 180\ \text{nm}$, width $W = 220\ \text{nm}$, gate oxide thickness $\sim 3.5\ \text{nm}$ $\text{SiO}_2$.
- **Array Sub-block Density**: 256 or 512 cells per bitline with bitline contact shared between adjacent pairs.
- **Capacitance Budgets**: Storage node capacitance $C_s \ge 25\text{--}30\ \text{fF}$ (nominally $28\ \text{fF}$); parasitic bitline capacitance $C_b = 150\text{--}250\ \text{fF}$; ratio $C_b / C_s \in [5:1, 9:1]$.
- **Leakage & Retention Target**: Sub-threshold and junction leakage $< 1\ \text{fA/cell}$ at $85^\circ\text{C}$ to maintain retention time $> 64\ \text{ms}$.

---

## 3. Step-by-Step Procedure

### Step 3.1: Logical Telemetry Ingestion & Inversion Sanitization
1. Ingest raw March test failure streams containing `[Bank, Row_Addr, Col_Addr, Data_Polarity]`.
2. Apply physical data polarity descrambling: compare data pattern against the physical storage node high/low state mapping (compensating for folded bitline reference inversion across true/complement bitline pairs: $\text{BL}$ vs $\overline{\text{BL}}$).

### Step 3.2: Row & Column Address Descrambling
1. **Row Address Descramble**: Decode logical row address bus $(A_R)$ using the 180nm sub-array row-decoder scrambling matrix:
   $$Y_{\text{phy}} = \text{DescrambleRow}(A_{R0} \dots A_{Rn})$$
   Map physical wordlines at uniform pitch between $360\ \text{nm}$ and $400\ \text{nm}$.
2. **Column Address Descramble**: Map logical column address $(A_C)$ into physical folded bitline pairs:
   $$X_{\text{phy}} = \text{DescrambleCol}(A_{C0} \dots A_{Cm})$$
   Assign true bitline ($\text{BL}$) to even physical tracks and complement bitline ($\overline{\text{BL}}$) to odd physical tracks at pitch $360\text{--}400\ \text{nm}$.

### Step 3.3: 2D Spatial Topology & Shared Contact Reconstruction
1. Allocate an array block grid matching the partition architecture: 256 or 512 cells per bitline segment.
2. Group adjacent paired cells along each bitline that share a common bitline contact plug (tungsten plug to stacked capacitor node).
3. Compute exact physical coordinates:
   $$X = X_{\text{phy}} \times \text{Pitch}_{\text{BL}}, \quad Y = Y_{\text{phy}} \times \text{Pitch}_{\text{WL}}$$
   occupying $0.259\ \mu\text{m}^2$ unit cell footprint.

### Step 3.4: Bit-Flip Clustering & Defect Classification
1. Project bit-flip event coordinates onto the $(X, Y)$ physical bitmap grid.
2. Classify spatial failure patterns into:
   - **Single Bit Failures**: Isolated retention degradation ($C_s < 25\ \text{fF}$ or localized junction leakage $> 1\ \text{fA}$).
   - **Bitline-Pair / Shared Contact Faults**: Failures along shared W-plug contacts or adjacent dual cells.
   - **Wordline / Bitline Open-Shorts**: Continuous linear failure tracks across 256 or 512 cells.

---

## 4. Machine-Measurable Acceptance Criteria Target Metrics

| Metric ID | Metric Parameter | Target Value / Tolerance | Physical Unit | Measurement Method |
| :--- | :--- | :--- | :--- | :--- |
| **AC-01** | Unit Cell Footprint Grid Accuracy | $0.259 \pm 0.005$ | $\mu\text{m}^2$ | CAD GDSII Overlay Validation ($8F^2$ at $F = 180\ \text{nm}$) |
| **AC-02** | Bitline / Wordline Physical Pitch | $360 \text{ to } 400$ | $\text{nm}$ | Coordinate Reconstruction Step Pitch Verification |
| **AC-03** | Sub-Array Block Line Density | Exactly $256$ or $512$ | $\text{cells/bitline}$ | Telemetry Array Dimension Check |
| **AC-04** | Bit-Flip Retention Leakage Bound | Sub-threshold/Junction $< 1.0$ | $\text{fA/cell}$ at $85^\circ\text{C}$ | Automated Shmoo Metrology ($> 64\ \text{ms}$ retention threshold) |

---

## 5. References & Literature Context
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench* (Transistor $L = 180\ \text{nm}, W = 220\ \text{nm}$, W-plug shared contact, leakage $< 1\ \text{fA/cell}$ at $85^\circ\text{C}$, $C_s \ge 28\ \text{fF}$).
- *1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets* ($8F^2$ footprint area $0.259\ \mu\text{m}^2$, $C_s \ge 25\text{--}30\ \text{fF}$, 256/512 cells per bitline, $C_b = 150\text{--}250\ \text{fF}$, $C_b/C_s \in [5:1, 9:1]$).
- *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering* (WL/BL pitch $360\text{--}400\ \text{nm}$, retention $> 64\ \text{ms}$ at $85^\circ\text{C}$, $t_{\text{ox}} \sim 3.5\ \text{nm}\ \text{SiO}_2$).

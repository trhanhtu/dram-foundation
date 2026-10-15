# Standard Operating Procedure (SOP)
## Fail-Bit Bitmap Extraction & Variable Retention Time (VRT) Defect Analysis

- **Document ID:** SOP-DRAM-MET-007
- **Generation:** Gen 3 (nm) / 180nm CMOS Commercial MPW Tapeout & PDK Implementation
- **Action Type:** Make
- **Discipline:** Metrology / Reliability Testing & Silicon Failure Analysis

---

## 1. Scope & Objective
This Standard Operating Procedure establishes the execution methodology for extracting physical fail-bit bitmaps from automated test equipment (ATE) retention screening logs and performing Variable Retention Time (VRT) defect analysis on the 180nm open-source DRAM architecture. The procedure isolates anomalous, trap-assisted bimodal retention time fluctuations from deterministic sub-threshold and junction leakages, correlating bimodal pause-refresh degradation back to physical 2D layout coordinates.

```text
+------------------------------------------------------------------------------------+
|               DRAM ARRAY FAIL-BIT BITMAP EXTRACTION & VRT FLOW                     |
+------------------------------------------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               | 1. ATE Variable Pause-Refresh Stress & Cycling    |
               |    - Pause sweep: 10 ms to 1000 ms at 85 deg C    |
               |    - N = 100 consecutive read-pause-verify passes |
               +---------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               | 2. 2D Physical Coordinate & Bitmap Descrambling   |
               |    - Wordline / Bitline pitch: 360 nm to 400 nm   |
               |    - 8F^2 unit cell footprint: 0.259 um^2         |
               +---------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               | 3. VRT Tail-Bit Identification & Bimodal Analysis |
               |    - Track bit-flip state transitions (Good/Fail) |
               |    - Isolate trap switching (> 1 fA state jump)   |
               +---------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               | 4. Defect Characterization & Parametric Screen    |
               |    - Gate oxide / interface trap Dit correlation  |
               |    - Stacked capacitor (Cs >= 28 fF) verification |
               +---------------------------------------------------+
```

---

## 2. Technical Context & Verified Parameters
From verified local literature context and 180nm baseline design rules:
- **Unit Cell Topology**: 1T1C stacked capacitor over bitline (COB) folded bitline architecture ($8F^2$ footprint).
- **Access Transistor Dimensions**: Channel length $L = 180\ \text{nm}$, channel width $W = 220\ \text{nm}$, physical gate oxide thickness $t_{\text{ox}} = 3.5\ \text{nm}$ to $25\ \text{nm}$.
- **Access Device Static Parameters**: Linear threshold voltage $V_{\text{thn}} = +0.55\ \text{V} \pm 50\ \text{mV}$ (measured at $V_{\text{DS}} = 50\ \text{mV}$ via maximum $g_m$ extrapolation); $I_{\text{on}} \ge 500\ \mu\text{A}/\mu\text{m}$ at $V_{\text{GS}} = 1.8\ \text{V}$, $I_{\text{off}} \le 10\ \text{pA}/\mu\text{m}$ at $V_{\text{GS}} = 0\ \text{V}$ ($I_{\text{on}} / I_{\text{off}} > 10^7$).
- **Capacitor Structure & Dielectric**: Crown-shaped polysilicon or metal-insulator-metal (MIM) stacked over drain contact via tungsten plug (W-plug). Dielectric stack: ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-$k$ stack ($\kappa > 15$).
- **Capacitance Budget**: Storage node capacitance $C_s \ge 28\ \text{fF/cell}$.
- **Leakage & Retention Target**: Sub-threshold and junction leakage target $\le 1\ \text{fA/cell}$ at $85^\circ\text{C}$ to maintain baseline refresh window ($> 64\ \text{ms}$).

---

## 3. Step-by-Step Procedure

### Step 3.1: Automated Pause-Refresh Stress Sequencing on ATE
1. Mount the packaged 180nm DRAM device onto the temperature-controlled test socket calibrated at chuck temperature $T_{\text{ch}} = 85^\circ\text{C} \pm 0.5^\circ\text{C}$.
2. Initialize core and peripheral bias supplies to nominal operating conditions ($V_{\text{DD}} = 1.8\ \text{V}$, $V_{\text{PP}} = 3.0\ \text{V}$, $V_{\text{BB}} = -0.5\ \text{V}$).
3. Program a multi-pass pause-refresh sequence:
   - Write solid '1' and checkerboard background patterns into the array.
   - Execute a logarithmic pause-time retention sweep across $t_{\text{pause}} \in [10\ \text{ms}, 20\ \text{ms}, 50\ \text{ms}, 64\ \text{ms}, 100\ \text{ms}, 200\ \text{ms}, 500\ \text{ms}, 1000\ \text{ms}]$.
   - Read back array contents at standard operating speed without intermediate auto-refresh commands.
   - Record logical address `[Bank, Row, Column]` for all flipped bits.
4. Repeat the pause-refresh test loop for $N = 100$ consecutive cycles at fixed retention pause time ($t_{\text{pause}} = 64\ \text{ms}$) to observe temporal instability.

### Step 3.2: 2D Spatial Fail-Bit Bitmap Physical Descrambling
1. Ingest logical fail address logs into the physical descrambling engine.
2. Descramble logical row address $A_R$ and column address $A_C$ into physical coordinates $(X_{\text{phy}}, Y_{\text{phy}})$ accounting for folded bitline multiplexing and shared bitline tungsten contact (W-plug) pairing.
3. Scale coordinates using the array pitch:
   $$X = X_{\text{phy}} \times \text{Pitch}_{\text{BL}}, \quad Y = Y_{\text{phy}} \times \text{Pitch}_{\text{WL}}$$
   where $\text{Pitch}_{\text{BL}}$ and $\text{Pitch}_{\text{WL}}$ range from $360\ \text{nm}$ to $400\ \text{nm}$, forming the $0.259\ \mu\text{m}^2$ unit cell footprint.
4. Generate the composite 2D failure bitmap, categorizing fails into single-bit cells, paired shared-contact defects, single wordline rows, and single bitline columns.

### Step 3.3: Variable Retention Time (VRT) Defect Extraction & Classification
1. Aggregate the $N = 100$ cycle multi-pass retention bitmaps.
2. Classify bit failures into two distinct behavior regimes:
   - **Static Retention Fails (Deterministic)**: Bits failing consistently across all $N$ cycles for a given $t_{\text{pause}}$ (governed by static junction leakage, low $C_s < 28\ \text{fF}$, or elevated MOSFET $I_{\text{off}} > 10\ \text{pA}/\mu\text{m}$).
   - **Variable Retention Time (VRT) Tail Bits**: Bits exhibiting bimodal retention switching—flipping between passing (retention $> 64\ \text{ms}$) and failing (retention $< 64\ \text{ms}$) states randomly across cycles.
3. Compute the switching frequency and bimodal retention distribution for each identified VRT candidate.
4. Calculate effective leakage jump $\Delta I_{\text{leak}}$ from the retention time differential:
   $$\Delta I_{\text{leak}} = C_s \frac{\Delta V}{\Delta t_{\text{ret}}}$$
   confirming trap-assisted generation-recombination switching exceeding $1\ \text{fA/cell}$.

### Step 3.4: Metrological Defect Correlation & Root-Cause Screening
1. Correlate VRT cluster coordinates with C-V profiling and interface trap density ($D_{\text{it}}$) extracted from adjacent scribe-line Planar MOSCAP structures (thermally grown oxide $t_{\text{ox}} = 3.5\text{--}25\ \text{nm}$).
2. Perform gate-induced drain leakage (GIDL) and sub-threshold swing metrology on discrete target reference transistors ($W/L = 2.0\ \mu\text{m} / 0.18\ \mu\text{m}$) to ensure access transistor $V_{\text{thn}} = +0.55\ \text{V} \pm 50\ \text{mV}$ and $S \approx 80\text{--}90\ \text{mV/dec}$.
3. Quarantine dies displaying VRT tail-bit density exceeding allowable redundancy repair capacity.

---

## 4. Machine-Measurable Acceptance Criteria Target Metrics

| Metric ID | Metric Parameter | Target Value / Tolerance | Physical Unit | Measurement / Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **AC-01** | Nominal Cell Storage Capacitance ($C_s$) | $\ge 28.0$ | $\text{fF/cell}$ | Stacked Crown/MIM Capacitor C-V Extraction at $1\ \text{MHz}$ |
| **AC-02** | Baseline Cell Junction & Sub-threshold Leakage | $\le 1.0$ | $\text{fA/cell}$ at $85^\circ\text{C}$ | Automated ATE Refresh Retention Threshold ($t_{\text{pause}} \ge 64\ \text{ms}$) |
| **AC-03** | Access Transistor Off-State Current ($I_{\text{off}}$) | $\le 10.0$ | $\text{pA}/\mu\text{m}$ at $V_{\text{GS}} = 0\ \text{V}$, $V_{\text{DS}} = 1.8\ \text{V}$ | Discrete Reference Transistor ($W/L = 2.0\ \mu\text{m} / 0.18\ \mu\text{m}$) Parametric Metrology |
| **AC-04** | Access Transistor Linear Threshold Voltage ($V_{\text{thn}}$) | $+0.55 \pm 0.05$ ($+0.50 \text{ to } +0.60$) | $\text{V}$ | Maximum Transconductance ($g_m$) Extrapolation at $V_{\text{DS}} = 50\ \text{mV}$ |

---

## 5. References & Verified Context
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Stacked capacitor over bitline (COB) architecture ($8F^2$ and $6F^2$).
  - Access transistor channel length $L = 180\ \text{nm}$, width $W = 220\ \text{nm}$, shared W-plug contact.
  - Storage capacitance $C_s \ge 28\ \text{fF/cell}$, high-$k$ stack $\kappa > 15$.
  - Sub-threshold and junction leakage target $< 1\ \text{fA/cell}$ at $85^\circ\text{C}$.
- **Stage 3 Reality Gate: Discrete Long-Channel MOSFET & CMOS Inverter Verification**:
  - Target sub-micron transistor geometry: $W / L = 2.0\ \mu\text{m} / 0.18\ \mu\text{m}$.
  - NMOS linear threshold voltage: $V_{\text{thn}} = +0.55\ \text{V} \pm 50\ \text{mV}$ (measured at $V_{\text{DS}} = 50\ \text{mV}$ via max $g_m$).
  - Transistor on/off metrics: $I_{\text{on}} \ge 500\ \mu\text{A}/\mu\text{m}$ ($V_{\text{GS}} = 1.8\ \text{V}$), $I_{\text{off}} \le 10\ \text{pA}/\mu\text{m}$ ($V_{\text{GS}} = 0\ \text{V}$, $V_{\text{DS}} = 1.8\ \text{V}$), $I_{\text{on}} / I_{\text{off}} > 10^7$.
- **Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction**:
  - High-frequency ($1\ \text{MHz}$) and quasi-static C-V characterization on thermal oxide ($t_{\text{ox}} = 3.5\ \text{nm}$ to $25\ \text{nm}$).
  - Accumulation oxide thickness determination ($C_{\text{ox}}$) and interface trap / depletion dynamics evaluation.

# Standard Operating Procedure (SOP)
## ATE Shmoo Raw Vector Parsing & Pass/Fail Surface Extraction

- **Document ID:** SOP-DRAM-MET-014
- **Generation:** Gen 3 (180nm) / 180nm CMOS Commercial MPW Tapeout & PDK Implementation
- **Action Type:** Make
- **Discipline:** Metrology / Automated Test Equipment (ATE) JEDEC DDR Speed-Bin & HTOL Burn-in Testing

---

## 1. Scope & Objective

This Standard Operating Procedure (SOP) defines the protocol for parsing raw automated test equipment (ATE) vector logs (STIL/WGL/VCD/EVCD/ASCII datalog streams) and extracting two-dimensional (2D) and three-dimensional (3D) Pass/Fail operating boundary surfaces ($V_{DD}$ vs. Frequency $f_{CK}$ vs. Temperature $T$) for 180nm open-source DRAM chips. The procedure extracts JEDEC timing margins ($t_{RCD}$, $t_{RP}$, $t_{RAS}$, $t_{CK}$) and operating margins from post-HTOL burn-in test vectors, separating functional core failures from peripheral I/O setup/hold violations.

```text
+------------------------------------------------------------------------------------+
|            ATE SHMOO RAW VECTOR PARSING & PASS/FAIL SURFACE EXTRACTION            |
+------------------------------------------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               | 1. High-Throughput Raw Vector Parsing             |
               |    - Ingest ATE cyclized vector datalogs          |
               |    - Tokenize VDD sweep (1.2V-2.2V) & tCK/Freq    |
               |    - Isolate vector pin states (H, L, X, Z)       |
               +---------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               | 2. Matrix Reconstruction & Coordinate Mapping     |
               |    - Map 2D grid: VDD (20mV step) x Freq (2MHz)   |
               |    - 180nm cell dimensions: L=180nm, W=220nm      |
               |    - Decode fail vector cycle to fail bit address |
               +---------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               | 3. Pass/Fail Surface & Contour Extraction         |
               |    - Determine 50% pass/fail cutoffs (isocline)   |
               |    - Extract minimum VDD operating floor          |
               |    - Evaluate signal margin: Cs >= 28 fF budget   |
               +---------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               | 4. JEDEC Operating Margin & Metrology Signoff     |
               |    - Compute voltage margin: VDD_nom +/- 10%      |
               |    - Compute frequency margin: fCK_max >= target  |
               |    - Generate signoff certificate & export CSV/HDF5|
               +---------------------------------------------------+
```

---

## 2. Technical Context & Verified Parameters

From verified local literature context and 180nm baseline design specifications:
- **Unit Cell Architecture**: $8F^2$ Folded Bitline layout with Stacked Capacitor over Bitline (COB).
- **Access Transistor Dimensions**: Channel length $L = 180\ \text{nm}$, channel width $W = 220\ \text{nm}$.
- **Capacitor Structure & Budget**: Crown-shaped polysilicon or metal-insulator-metal (MIM) structure erected above drain contact via tungsten plug (W-plug). High-$\kappa$ dielectric ($\kappa > 15$, e.g., ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$). Storage capacitance $C_s \ge 28\ \text{fF/cell}$.
- **Bitline Parasitic Capacitance**: $C_b = 150\ \text{fF}$ to $250\ \text{fF}$, maintaining capacitance ratio $C_b / C_s$ between $5:1$ and $9:1$.
- **Storage Cell Retention Leakage**: Sub-threshold and junction leakage target $\le 1.0\ \text{fA/cell}$ at $85^\circ\text{C}$.
- **ATE Sweep Range**:
  - Core supply voltage: $V_{DD} = 1.20\ \text{V}$ to $2.20\ \text{V}$ (nominal $1.80\ \text{V} \pm 10\%$, step resolution $\le 20\ \text{mV}$).
  - Operating frequency: $f_{CK} = 50\ \text{MHz}$ to $250\ \text{MHz}$ (clock period $t_{CK} = 20.0\ \text{ns}$ to $4.0\ \text{ns}$, step resolution $\le 2\ \text{MHz}$ or $0.2\ \text{ns}$).
  - Thermal chuck: $T = 25^\circ\text{C}$ to $125^\circ\text{C}$ ($\pm 0.5^\circ\text{C}$ stability).

---

## 3. Equipment, Toolflow & Input Artifacts

1. **ATE Test System**: Advantest T5588 / Teradyne UltraFLEX or equivalent high-speed memory test head configured with algorithmic pattern generator (ALPG) and pin electronics (PE).
2. **Analysis Environment**: Python 3.10+ execution runtime with NumPy, SciPy, Pandas, HDF5, and Plotext/Termaid CLI visualization tools (`PYTHONIOENCODING="utf-8"`).
3. **Synthesis & Physical Design Database**: OpenROAD RTL-to-GDSII flow timing reports (`OpenROAD-flow-scripts`) providing post-routing parasitic extraction (`OpenRCX`) and STA delay corners.
4. **Input Vector Logs**: Raw ATE STIL/ASCII test log files containing per-cycle vector execution results, fail counts, pin compare vectors, and sweep header tables.

---

## 4. Step-by-Step Procedure

### Step 1: Ingestion & Lexical Parsing of ATE Raw Datalog Streams
1. Open raw ATE datalog file stream. Read ASCII header block to extract sweep parameters: start voltage $V_{DD,\min}$, stop voltage $V_{DD,\max}$, voltage step $\Delta V_{DD}$, start period $t_{CK,\min}$, stop period $t_{CK,\max}$, and period step $\Delta t_{CK}$.
2. Stream vector evaluation records line-by-line. Tokenize output vector pins:
   - Match compare tokens against expected pattern: `P` / `.` (Pass), `F` / `*` (Fail), `X` (Masked/Don't Care).
   - Ingest cycle-accurate fail address pointers: `Row[11:0]`, `Col[9:0]`, `Bank[1:0]`.
3. Validate stream integrity by verifying checksum or record count matches the defined grid dimensions:
   $$N_{\text{points}} = \left(\frac{V_{DD,\max} - V_{DD,\min}}{\Delta V_{DD}} + 1\right) \times \left(\frac{f_{CK,\max} - f_{CK,\min}}{\Delta f_{CK}} + 1\right)$$

### Step 2: Binary Matrix Reconstruction & Coordinate Normalization
1. Allocate an empty 2D binary matrix $M \in \{0, 1\}^{N_V \times N_F}$, where:
   - Index $i \in [0, N_V - 1]$ corresponds to $V_{DD}(i) = V_{DD,\min} + i \cdot \Delta V_{DD}$.
   - Index $j \in [0, N_F - 1]$ corresponds to $f(j) = f_{\min} + j \cdot \Delta f$.
2. Populate $M[i, j]$ with binary classification:
   - Set $M[i, j] = 1$ (Pass) if total fail count $\text{FC} = 0$ (or below allowable redundancy repair limit, $\le 4$ single-bit fails).
   - Set $M[i, j] = 0$ (Fail) if $\text{FC} > 0$ uncorrectable functional fails occur.
3. Isolate failure mechanisms:
   - Flag whole-column or whole-row failures as wordline/bitline open/short defects.
   - Flag voltage-dependent degradation as charge-sharing sensing failures caused by $C_s < 28\ \text{fF}$ or sense amplifier imbalance.

### Step 3: Pass/Fail Boundary Contour & Surface Extraction
1. Apply 2D marching squares or bilinear surface interpolation across matrix $M$ to isolate the $0.5$ isocline boundary curve $f_{\text{boundary}}(V_{DD})$.
2. Extract the minimum operating voltage $V_{DD,\min}(f)$ across each frequency slice.
3. Compute the maximum operating frequency $f_{\max}(V_{DD})$ across each voltage slice.
4. Fit the empirical saturation delay model to the extracted boundary:
   $$t_{pd}(V_{DD}) = \frac{k \cdot C_L \cdot V_{DD}}{(V_{DD} - V_{th})^a}$$
   where $V_{th} \approx 0.55\ \text{V}$ and $a \in [1.2, 1.4]$ for the 180nm CMOS process.
5. Check for "Shmoo holes" (isolated fail points surrounded by pass points) indicating substrate noise, supply bounce, or PLL jitter instability.

### Step 4: JEDEC Operating Margin & Yield Boundary Calculation
1. Overlay JEDEC standard DDR operating limits onto the extracted boundary surface:
   - Supply tolerance window: $V_{DD} \in [1.62\ \text{V}, 1.98\ \text{V}]$ ($1.80\ \text{V} \pm 10\%$).
   - Target speed grade: $f_{CK} = 133\ \text{MHz}$ (DDR-266) or $166\ \text{MHz}$ (DDR-333).
2. Measure Voltage Operating Margin:
   $$\text{Margin}_{V, \text{low}} = 1.62\ \text{V} - V_{DD,\min}(f_{\text{target}})$$
   $$\text{Margin}_{V, \text{high}} = V_{DD,\max}(f_{\text{target}}) - 1.98\ \text{V}$$
3. Measure Frequency Operating Margin:
   $$\text{Margin}_f = f_{\max}(V_{DD} = 1.62\ \text{V}) - f_{\text{target}}$$
4. Export the resulting boundary surface dataset to structured HDF5 and CSV metrology archive formats.

---

## 5. Acceptance Criteria Target Metrics

| Parameter / Metric | Evaluation Method | Target Spec | Physical Units | Tolerance |
| :--- | :--- | :--- | :--- | :--- |
| **Parsing Throughput & Latency** | Execution timer on 10,000-point ATE raw datalog stream | $\le 1.50$ | seconds | Maximum allowable |
| **Pass/Fail Boundary Resolution ($\Delta V_{DD}$)** | Voltage step size of extracted 2D Shmoo grid | $\le 20.0$ | $\text{mV}$ | Step accuracy |
| **Pass/Fail Boundary Resolution ($\Delta f_{CK}$)** | Frequency step size of extracted 2D Shmoo grid | $\le 2.0$ | $\text{MHz}$ | Step accuracy |
| **JEDEC DDR Speed Margin ($f_{\max} @ 1.62\ \text{V}$)** | Extracted maximum functional clock frequency at lower $V_{DD}$ rail | $\ge 146.3$ | $\text{MHz}$ | $\ge +10\%$ above DDR-266 ($133\ \text{MHz}$) |
| **Minimum Operating Core Voltage ($V_{DD,\min} @ 133\ \text{MHz}$)** | Extracted lowest functional voltage point on boundary curve | $\le 1.45$ | $\text{V}$ | Upper threshold |

---

## 6. Literature & Verification Citations

1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry $L = 180\ \text{nm}$, $W = 220\ \text{nm}$.
   - Folded bitline $8F^2$ architecture with stacked capacitor over bitline (COB).
   - Storage capacitance requirement $C_s \ge 28\ \text{fF/cell}$; leakage target $\le 1.0\ \text{fA/cell}$ at $85^\circ\text{C}$.
2. **OpenROAD Physical Design & Synthesis Toolflow**:
   - Parasitic extraction using OpenRCX and static timing analysis signoff.
   - Standard cell placement and clock tree synthesis constraints governing path delays.
3. **SkyWater 130nm / 180nm Open PDK Architecture**:
   - Digital design flow integration, cell timing liberty models, and voltage margin characterization.

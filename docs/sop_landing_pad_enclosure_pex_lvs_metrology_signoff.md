# Standard Operating Procedure (SOP)
## Landing Pad Enclosure & Parasitic Extraction LVS Metrology Review & Sign-Off

- **Document ID**: SOP-MET-180DRAM-LVS-PEX-001
- **Process Generation**: 180nm Open-Source DRAM (Gen 3)
- **Hierarchy Path**: Context: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm CMOS Commercial MPW Tapeout & PDK Implementation [Foundry Tapeout & PDK] > 8F2 Folded Bitline 1T1C Full-Custom Cell Layout & Metal-Fix Routing for Commercial MPW [Circuit Design] > 1T1C Unit Cell Layout & Shared-Contact Active Area Design [Circuit Design] > Shared Bitline Contact & Storage Node Landing Pad DRC/LVS Verification [Metrology] > Landing Pad Enclosure & Parasitic Extraction LVS Metrology Review & Sign-Off [Metrology]
- **Action Type**: Make
- **Status**: Implemented / Approved

---

### 1. Purpose & Scope
This Standard Operating Procedure (SOP) defines the physical layout verification, design rule checking (DRC) enclosure validation, parasitic resistance and capacitance (RC) extraction (PEX), and layout-versus-schematic (LVS) sign-off protocol for the 8F² folded bitline 1T1C DRAM array at the 180nm technology node. 

The procedure encompasses:
1. Physical metrology verification of active area shared bitline contacts and storage node landing pad enclosures (W-plug interfaces).
2. Parasitic extraction calibration for storage node capacitance ($C_s$), bitline parasitic capacitance ($C_b$), and mutual coupling across 256/512 cell array blocks.
3. LVS discrepancy resolution, capacitance ratio ($C_b / C_s$) sign-off, sub-femtoampere junction leakage compliance review, and electrical rule validation before GDSII tapeout freeze.

---

### 2. Metrology & Verification Architecture Flow

```text
┌───────────────────────┐
│                       │
│    GDSII Layout &     │
│        Netlist        │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Shared Contact &    │
│    Landing Pad DRC    │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│     Parasitic RC      │
│    Extraction PEX     │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  LVS Netlist Match &  │
│   C_s/C_b Metrology   │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Sign-Off Approval   │
│                       │
└───────────────────────┘
```

---

### 3. Step-by-Step Execution Procedure

#### Step 1: Layout Geometrical Enclosure & DRC Verification
1. **Load GDSII Stream & Cell View**:
   - Ingest the full-custom 8F² folded bitline array layout ($F = 180\text{ nm}$, unit cell area $= 8F^2 = 0.259\ \mu\text{m}^2$) into the physical verification engine.
   - Confirm active area dimensions for access transistor: channel length $L = 180\text{ nm}$, gate width $W = 220\text{ nm}$.
   - Confirm bitline pitch and wordline pitch are set within nominal range $360\text{ nm to } 400\text{ nm}$.
2. **Landing Pad & Shared Contact Enclosure Verification**:
   - Check shared bitline contact landing pad geometry centered between adjacent access transistors sharing the drain active region.
   - Validate tungsten plug (W-plug) contact boundary against active area (diffusion) enclosure: ensure minimum diffusion enclosure of contact $\ge 40\text{ nm}$ along both axes.
   - Check storage node landing pad (M1/contact or poly plug) boundary against the access transistor source node diffusion: verify concentricity and minimum enclosure $\ge 45\text{ nm}$.
   - Ensure contact plug diameter is exactly $180\text{ nm} \pm 5\text{ nm}$ across all array array rows and dummy boundary columns.
   - Execute DRC deck `drc_180nm_dram_feol_beol.rul` and verify 0 DRC violations.

#### Step 2: 3D Field Solver Parasitic Extraction (PEX) Configuration
1. **PEX Layer Stack Definition**:
   - Load the commercial MPW dielectric stack: thermally grown gate oxide ($t_{ox} = 3.5\text{ nm}$), inter-layer dielectric (ILD1, ILD2), and stacked capacitor dielectric ($Si_3N_4$, $Ta_2O_5$, or $Ta_2O_5 / Al_2O_3$ / ONO high-k stack, effective $\kappa > 15$, Equivalent Oxide Thickness $\text{EOT} = 3.0\text{ to } 4.0\text{ nm}$).
   - Define tungsten plug (W-plug) bulk resistivity $\rho_W = 5.6\ \mu\Omega\cdot\text{cm}$ and contact interface barrier layers ($Ti/TiN$).
2. **Netlist Parasitic Extraction Execution**:
   - Run calibrated transistor-level 3D field-solver parasitic extraction (PEX) on a full array block containing 256 or 512 cells per folded bitline pair (`BL` and `/BL`).
   - Extract distributed coupled RC networks with minimum capacitance resolution threshold set to $0.005\text{ fF}$.
   - Output extracted spice netlist `array_1t1c_extracted.sp` incorporating back-annotated parasitic capacitances and interconnect resistances.

#### Step 3: Metrology Parametric Review & Netlist Capacitance Audit
1. **Storage Node Capacitance ($C_s$) Audit**:
   - Query extracted netlist for stacked capacitor storage nodes (crown/cylinder structure over bitline, COB).
   - Ensure total extracted capacitance $C_s$ per unit cell satisfies $25\text{ fF} \le C_s \le 30\text{ fF}$ (nominal target $28\text{ fF}$).
2. **Bitline Parasitic Capacitance ($C_b$) Audit**:
   - Query total lumped and distributed parasitic capacitance on bitline tracks (`BL`, `/BL`) for an active array block of 256 or 512 cells.
   - Verify total bitline capacitance satisfies $150\text{ fF} \le C_b \le 250\text{ fF}$.
3. **Capacitance Ratio ($C_b / C_s$) Evaluation**:
   - Compute bitline-to-storage-node capacitance ratio:
     $$R = \frac{C_b}{C_s}$$
   - Verify that $R$ satisfies the design budget window of $5:1 \le R \le 9:1$.
   - Confirm $R$ does not exceed $10:1$ under any corner (preventing catastrophic degradation of sensing read signal margin $\Delta V_{BL}$).

#### Step 4: LVS Topology Matching & Electrical Rule Checking (ERC)
1. **Schematic vs. Layout Cross-Comparison**:
   - Execute LVS rule deck `lvs_180nm_dram.rul` comparing the extracted netlist against golden hierarchical schematic `schematic_dram_8f2_array.sch`.
   - Verify port matching, device pin permutations, floating nodes, and substrate taps.
   - Confirm complete 1:1 netlist equivalence: 0 unbalanced nets, 0 missing instances, 0 short circuits.
2. **Leakage & ERC Verification**:
   - Evaluate sub-threshold channel leakage and reverse-biased $n^+/p$-well junction leakage at the storage node diffusion contact: confirm total leakage current $I_{leak} < 1.0\text{ fA/cell}$ at $85^\circ\text{C}$ to maintain data retention time $> 64\text{ ms}$.
   - Verify soft-error charge integrity: ensure critical charge $Q_{crit} = C_s \times (V_{DD}/2) \ge 25\text{ fF} \times 0.9\text{ V} = 22.5\text{ fC}$ prevents alpha-particle upset.

#### Step 5: Sign-Off Committee Review & Formal Authorization
1. Generate automated LVS/PEX metrology sign-off summary report `LVS_PEX_SIGNOFF_MET_001.rpt`.
2. Inspect GDSII cell array boundary coordinates and verify dummy perimeter cell termination.
3. Sign off and lock physical database for final chip assembly and MPW tapeout submission.

---

### 4. Parametric Extraction Budgets & Metrology Profile

```text
                      DRAM 180nm Cell Extraction Budgets
                       ┌───────────────────────────────┐
                       │■■                             │
        C_b / C_s Ratio┤■■                             │
C_b (Bitline Parasitic)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
                       │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
     C_s (Storage Node)┤█████                          │
                       │█████                          │
                       └┬───────┬──────┬───────┬──────┬┘
                        0      49     98      147   196 
```

---

### 5. Machine-Measurable Acceptance Criteria

| Metric ID | Inspection Parameter | Minimum | Nominal | Maximum | Physical Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MET-AC-01** | Storage Node Capacitance ($C_s$) | $25.0$ | $28.0$ | $30.0$ | $\text{fF}$ | 3D Field Solver PEX Netlist Extraction |
| **MET-AC-02** | Bitline Parasitic Capacitance ($C_b$) | $150.0$ | $196.0$ | $250.0$ | $\text{fF}$ | Extracted Netlist per 256/512 Cell Block |
| **MET-AC-03** | Capacitance Ratio ($C_b / C_s$) | $5.0$ | $7.0$ | $9.0$ | ratio ($:1$) | PEX Netlist Calculated Ratio ($\le 10:1$ hard limit) |
| **MET-AC-04** | Storage Node Junction/Subthreshold Leakage ($T = 85^\circ\text{C}$) | — | $0.4$ | $1.0$ | $\text{fA/cell}$ | SPICE Device Model Simulation ($> 64\text{ ms}$ retention) |

---

### 6. Verified Literature & Context References
1. **Source**: *1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*
   - Folded bitline $8F^2$ footprint area: $0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$.
   - Storage Node Capacitance ($C_s$): Must be $\ge 25\text{ fF to } 30\text{ fF}$ per cell (nominally $28\text{ fF}$).
   - Bitline Parasitic Capacitance ($C_b$): $150\text{ fF to } 250\text{ fF}$ across 256 or 512 cells per bitline.
   - Capacitance Ratio ($C_b / C_s$): Maintained between $5:1$ and $9:1$; degradation threshold at $> 10:1$.
2. **Source**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
   - Access transistor geometry: channel length $L = 180\text{ nm}$, gate width $W = 220\text{ nm}$.
   - Stacked capacitor over bitline (COB) erected above drain/source contact via tungsten plug (W-plug).
   - High-k dielectric: ONO or $Ta_2O_5 / Al_2O_3$ stack providing $\kappa > 15$.
   - Leakage current target: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ to maintain refresh retention.
3. **Source**: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*
   - Storage capacitance requirement: $25\text{ to } 30\text{ fF}$ per cell for retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Dielectric EOT: $3\text{ to } 4\text{ nm}$ ($Si_3N_4$ or $Ta_2O_5$).
   - Bitline and wordline pitch: $360\text{ nm to } 400\text{ nm}$.
   - Gate oxide: thermally grown $SiO_2$ with physical thickness $t_{ox} \approx 3.5\text{ nm}$.

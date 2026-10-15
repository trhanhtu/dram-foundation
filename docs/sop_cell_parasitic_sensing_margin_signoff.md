# SOP: Cell Parasitic Model Validation and C_b/C_s Sensing Margin Sign-Off Analysis

- **Document ID**: `SOP-MET-180NM-001`
- **Revision**: 1.0.0
- **Technology Node**: 180nm CMOS Commercial MPW Tapeout (F = 180 nm)
- **Cell Architecture**: 8F² Folded Bitline 1T1C Full-Custom Unit Cell (0.259 µm²)
- **Author**: DRAM Foundation VN Multi-Agent Council (Domain Expert AI)

---

## 1. Overview & Objective

This Standard Operating Procedure (SOP) governs the extraction, validation, and sign-off analysis of cell storage node capacitance ($C_s$), bitline parasitic capacitance ($C_b$), capacitance ratio ($C_b / C_s$), and developed differential read sensing margin ($\Delta V$) for 180nm 1T1C stacked capacitor DRAM memory arrays.

```text
┌────────────────────────┐
│                        │
│    Layout & Contact    │
│      Verification      │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│      Field Solver      │
│  Parasitic Extraction  │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│  Calculate C_b / C_s   │
│         Ratio          │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│  Differential Signal   │
│   Delta_V Evaluation   │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────◇───────────┐
│  Sign-Off Margin Met?  │
└──────┬──────────┬──────┘
    Yes│          │No
       ▼          ▼
┌──────────────┐ ┌──────────────────────┐
│   Sign-Off   │ │  Layout & Metal-Fix  │
│   Approval   │ │     Optimization     │
└──────────────┘ └──────────────────────┘
```

---

## 2. Step-by-Step Procedure

### Step 1: Geometry & Boundary Setup
1. Load the GDSII/OASIS layout of the 8F² folded bitline array block (256 or 512 cells per bitline pair, cell area = $0.259\ \mu\text{m}^2$ at $F = 180\ \text{nm}$, access NMOS geometry $L = 180\ \text{nm}$, $W = 220\ \text{nm}$).
2. Validate shared bitline contacts between adjacent memory cell pairs and stacked capacitor over bitline (COB) crown/MIM tungsten plugs (W-plugs).

### Step 2: 3D Field Solver Parasitic Extraction
1. Configure dielectric stack constants: effective dielectric constant $\kappa > 15$ for the ONO / $\text{Ta}_2\text{O}_5\text{ / }\text{Al}_2\text{O}_3$ storage capacitor layer.
2. Execute deterministic 3D field solver extraction across:
   - Storage node capacitor plate and fringe parasitics to extract $C_s$.
   - Bitline conductor traces (M1/M2), adjacent line-to-line coupling, plate-to-substrate coupling, and drain diffusion junction capacitances across the full 256/512-cell column to extract total bitline capacitance $C_b$.

### Step 3: Capacitance Ratio Calculation
1. Extract net values for $C_s$ and $C_b$.
2. Compute the bitline-to-cell capacitance ratio:
   $$\text{Ratio} = \frac{C_b}{C_s}$$
3. Verify that the ratio falls strictly within the target budget of $5:1$ to $9:1$, ensuring it never exceeds the hard sign-off threshold of $10:1$.

### Step 4: Differential Sensing Margin ($\Delta V$) Calculation & SPICE Verification
1. Precharge both bitlines ($\text{BL}$ and $\overline{\text{BL}}$) to $V_{\text{DD}} / 2$.
2. Simulate wordline assertion and charge sharing from cell storage node ($V_{\text{cell}} = V_{\text{DD}}$ for Logic '1', $0\ \text{V}$ for Logic '0'):
   $$\Delta V = \left(\frac{C_s}{C_b + C_s}\right) \cdot \left|V_{\text{cell}} - \frac{V_{\text{DD}}}{2}\right| = \left(\frac{C_s}{C_b + C_s}\right) \cdot \frac{V_{\text{DD}}}{2}$$
3. Perform transient SPICE simulation of CMOS cross-coupled sense amplifier activation to verify reliable differential latching without sensing inversion or metastabilities.

---

## 3. Target Metrics & Acceptance Criteria

| Metric | Target Specification | Sign-Off Limit | Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Storage Node Capacitance ($C_s$)** | $28.0$ (nominal) | $\ge 25.0 \text{ to } 30.0$ | $\text{fF/cell}$ | 3D Field Solver Extraction |
| **Bitline Parasitic Capacitance ($C_b$)** | $150.0 \text{ to } 238.0$ | $\le 250.0$ | $\text{fF/bitline}$ | Full Column RC Extraction (256/512 cells) |
| **Capacitance Ratio ($C_b / C_s$)** | $5.0 : 1 \text{ to } 8.5 : 1$ | $\le 9.0 : 1$ (Hard Max $10.0 : 1$) | - | Ratio Analysis |
| **Read Differential Signal ($\Delta V$)** | $100.0 \text{ to } 150.0$ | $\ge 100.0$ | $\text{mV}$ | Transient Readout SPICE Simulation |

```text
                             ┌───────────────────────────┐
                             │░░░░░░░░░░░░░░             │
  Read Signal Delta_V (mV/10)┤░░░░░░░░░░░░░░             │
                             │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    │
Bitline Parasitic C_b (fF/10)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    │
        Storage Node C_s (fF)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                             │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
          C_b/C_s Ratio (x:1)┤█████████                  │
                             │█████████                  │
                             └┬──────┬─────┬──────┬─────┬┘
                              0      7    14     21    28 
```

---

## 4. Literature References

1. **Source**: *1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*
   - $8\text{F}^2$ cell footprint ($0.259\ \mu\text{m}^2$ at $F = 180\ \text{nm}$).
   - $C_s \ge 25\ \text{fF}$ to $30\ \text{fF}$ (nominal $28\ \text{fF}$).
   - $C_b = 150\ \text{fF}$ to $250\ \text{fF}$ across 256/512 cells.
   - $C_b / C_s$ operating range between $5:1$ and $9:1$; degradation limit $> 10:1$.
2. **Source**: *Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout*
   - Precharge bitline equalization at $V_{\text{DD}} / 2$.
   - Signal development formulation $\Delta V = \frac{C_s}{C_b + C_s} \cdot \left(V_{\text{cell}} - \frac{V_{\text{DD}}}{2}\right)$.
   - Read signal margin $\Delta V \approx 100\ \text{mV}$ to $150\ \text{mV}$.
3. **Source**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
   - Access transistor dimensions $L = 180\ \text{nm}$, $W = 220\ \text{nm}$.
   - High-$\kappa$ dielectric stack ($\kappa > 15$) and stacked capacitor over bitline (COB).

# SOP: Elevated-Temperature Retention Time Sort & Pause-Refresh Bitmap Metrology

- **Date**: 2026-10-15
- **Source**: DRAM Foundation VN Council (Metrology & Reliability Domain)
- **Status**: Implemented
- **Process Step**: 180nm Open-Source DRAM Chip > BEOL Multi-Layer Metallization, Wafer Sort & Packaging > Wafer Electrical Sort, Parametric Test & Die Singulation > Full-Wafer Functional DRAM Cell Array Sort & Bitmap Probing > Multi-Pattern DRAM Array Functional Sorting (March C-, Checkerboard & Retention Test) > Elevated-Temperature Retention Time Sort & Pause-Refresh Bitmap Metrology

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) defines the execution methodology for elevated-temperature ($85^\circ\text{C}$) data retention testing and pause-refresh fail-bit mapping across full-wafer 180nm 1T1C DRAM arrays. The objective is to verify storage node charge retention ($t_{\text{pause}} \ge 64\text{ ms}$), identify temperature-accelerated junction and sub-threshold leakage tails, and generate physical fail-bit bitmaps for redundancy allocation and yield binning.

---

## 2. Process Flow & Metrology Architecture

```text
┌────────────────────────┐
│                        │
│    1. Thermal Chuck    │
│   Stabilization: 85C   │
│       (+/- 0.5C)       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    2. Array Pattern    │
│    Initialization:     │
│   Solid/Checkerboard   │
│          Data          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  3. Wordline Inactive  │
│    Pause Interval:     │
│    t_pause >= 64 ms    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  4. Fast Synchronous   │
│   Readout and Sense    │
│       Amp Latch        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  5. Fail-Bit Mapping   │
│   and Variable Pause   │
│  Retention Profiling   │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Thermal Chuck Conditioning & Wafer Loading
1. Power on the automated wafer prober thermal chuck and set target temperature to $85.0^\circ\text{C}$.
2. Wait for closed-loop thermal PID stabilization within $\pm 0.5^\circ\text{C}$. Verify temperature uniformity across the 200 mm chuck surface using calibrated multi-zone RTD sensors.
3. Load the 180nm DRAM wafer onto the thermal chuck with vacuum chuck pressure $\ge 70\text{ kPa}$.
4. Align wafer notch/flat and perform probe card touchdown onto die bond pads with overdrive set between $35\,\mu\text{m}$ and $50\,\mu\text{m}$ to ensure stable contact resistance ($R_{\text{cont}} < 1\,\Omega/\text{pad}$).

### Step 2: Array Initialization & Pattern Write
1. Configure Automatic Test Equipment (ATE) supply rails:
   - Array Core Voltage: $V_{\text{DD}} = 1.8\text{ V}$.
   - Precharge Voltage: $V_{\text{BLP}} = V_{\text{DD}} / 2 = 0.9\text{ V}$.
   - Wordline Boosted Gate Voltage: $V_{\text{PP}} = 3.0\text{ V}$ to $3.3\text{ V}$.
   - Substrate Back-bias Voltage: $V_{\text{BB}} = -0.5\text{ V}$ to $-0.8\text{ V}$.
2. Execute full-array synchronous write sequence across all addresses:
   - **Pattern A (Worst-Case High Leakage)**: Solid data background (Write all '1's, storage node charged to $V_{\text{DD}}$).
   - **Pattern B (Complementary Leakage)**: Solid data background (Write all '0's, storage node discharged to $V_{\text{SS}}$).
   - **Pattern C (Adjacent-Cell Coupling & Disturb)**: Checkerboard pattern ($0101... / 1010...$) to maximize cell-to-cell lateral fringe electric field stress across adjacent $360\text{ nm}$ to $400\text{ nm}$ wordline/bitline pitches.

### Step 3: Pause Interval Execution (Refresh Clock Inactivation)
1. Inhibit all internal or ATE-driven Auto-Refresh (`CBR`) and Self-Refresh cycles.
2. Maintain all wordlines inactive at $V_{\text{SS}}$ or negative wordline low bias ($V_{\text{WL\_low}} = 0\text{ V}$ to $-0.3\text{ V}$) to isolate storage nodes ($C_s \ge 25\text{ fF}$ to $30\text{ fF}$).
3. Assert a precise static pause interval of $t_{\text{pause}} = 64.0\text{ ms}$ at $85^\circ\text{C}$.
4. For extended distribution and retention tail characterization, execute stepped pause sweeps: $t_{\text{pause}} \in \{64\text{ ms}, 128\text{ ms}, 256\text{ ms}, 512\text{ ms}, 1024\text{ ms}\}$.

### Step 4: Fast Synchronous Readout & Sense Amplifier Latching
1. Immediately upon expiration of $t_{\text{pause}}$, trigger burst synchronous burst read cycles across all row addresses at the maximum rated ATE vector speed ($100\text{ MHz} - 133\text{ MHz}$).
2. Ensure bitlines are equalized to $V_{\text{BLP}} = 0.9\text{ V}$ before wordline activation.
3. Strobe the cross-coupled CMOS sense amplifiers to latch developed cell differential voltage $\Delta V_{\text{BL}}$:
   $$\Delta V_{\text{BL}} = \frac{C_s}{C_s + C_b} \left(V_{\text{cell}} - V_{\text{BLP}}\right)$$
   Where nominal $C_s = 28\text{ fF}$ and bitline parasitic capacitance $C_b = 150\text{ fF}$ to $250\text{ fF}$ (keeping ratio $C_b / C_s$ strictly between $5:1$ and $9:1$).
4. Compare sampled digital data vectors against the reference input pattern in the ATE pattern comparator real-time buffer.

### Step 5: Fail-Bit Extraction, Physical Descrambling & Retention Bitmap Generation
1. Capture all bit comparison mismatches (1 $\rightarrow$ 0 discharges or 0 $\rightarrow$ 1 charge gains) in the ATE fail memory.
2. Pass logical coordinates $(X_{\text{logical}}, Y_{\text{logical}})$ through the physical address descrambler to map logical addresses to physical $X$-$Y$ silicon array coordinates (accounting for folded bitline $8F^2$ cell interleaved twists and wordline decoder layout).
3. Classify fail types into:
   - **Single-Bit Random Fails (Retention Tail)**: Localized access transistor junction/sub-threshold leakage or ONO/$\text{Ta}_2\text{O}_5$ pinhole leakage.
   - **Row/Column Clustered Fails**: Wordline dielectric breakdown, bitline contact shorts, or sense amplifier offset degradation.
4. Export wafer-level retention yield maps and pause-time Cumulative Distribution Functions (CDF).

---

## 4. Key Metrology Target Metrics

```text
                     Retention Test Metrology Targets   
                  ┌────────────────────────────────────┐
                  │■■                                  │
Leakage Limit (fA)┤■■                                  │
                  │████████████████████████████████████│
      t_pause (ms)┤████████████████████████████████████│
      C_s Max (fF)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   │
                  │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   │
      C_s Nom (fF)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    │
                  │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    │
      C_s Min (fF)┤░░░░░░░░░░░░░░░                     │
                  │░░░░░░░░░░░░░░░                     │
                  └┬────────┬────────┬───────┬────────┬┘
                   0       16       32      48       64 
```

---

## 5. Machine-Measurable Acceptance Criteria

| Parameter | Metric / Condition | Target Value | Unit | Action Upon Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Data Retention Pause Interval** | Standard array refresh pass threshold at Chuck Temp $= 85.0^\circ\text{C}$ | $\ge 64.0$ | $\text{ms}$ | Bin die to retention reject / repair analysis |
| **Cell Storage Capacitance ($C_s$)** | Derived from retention decay and sense amp margin (Nominal: $28\text{ fF}$) | $25.0 \text{ to } 30.0$ | $\text{fF/cell}$ | Trigger CV parametric test on PCM macro |
| **Total Cell Leakage Current** | Combined sub-threshold and junction leakage at $85^\circ\text{C}$ storage node | $\le 1.0$ | $\text{fA/cell}$ | Flag gate-oxide / junction contamination |
| **Bitline Capacitance Ratio ($C_b / C_s$)** | Ratio of parasitic bitline capacitance ($C_b = 150 - 250\text{ fF}$) to $C_s$ | $5.0 : 1 \text{ to } 9.0 : 1$ | ratio | Adjust block size or sense timing strobe |

---

## 6. Context & Literature Citations

1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$); stacked capacitor over bitline (COB) with ONO triple dielectric / $\text{Ta}_2\text{O}_5$ / $\text{Al}_2\text{O}_3$ high-k stack ($\kappa > 15$).
   - Storage capacitance minimum budget of $28\text{ fF/cell}$ and leakage current ceiling $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - 1T1C architecture with $8F^2$ or $6F^2$ cell layout; requirement of storage capacitance $C_s \in [25, 30]\text{ fF}$ ensuring retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Equivalent oxide thickness (EOT) $3 \text{ to } 4\text{ nm}$, bitline/wordline pitch $360\text{ nm} \text{ to } 400\text{ nm}$, gate dielectric $t_{\text{ox}} \approx 3.5\text{ nm}$.
3. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Folded bitline $8F^2$ layout area $= 0.259\,\mu\text{m}^2$; bitline capacitance $C_b = 150\text{ to } 250\text{ fF}$ across 256/512 cells per bitline; capacitance ratio constraint $5:1 \le C_b / C_s \le 9:1$ to preserve sense amplifier differential signal margin $\Delta V_{\text{BL}}$.

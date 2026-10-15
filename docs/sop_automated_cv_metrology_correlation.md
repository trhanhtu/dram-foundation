# SOP: Automated C-V Metrology Correlation & Sense-Margin Validation Bench

- **Date**: 2026-10-15
- **Generation**: Gen 2 (µm / 180nm)
- **Hierarchy Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > ESP32 Closed-Loop Motor Controller > Automated Parametric Retention & March C- Diagnostic Test Firmware > March C- Diagnostic Engine & Fault Mapping Algorithm Implementation > Bitmap Fault Logger, Retention Degradation Analyzer & Metrology Validation > Automated C-V Metrology Correlation & Sense-Margin Validation Bench

---

## 1. Process Overview & Flow

```text
┌────────────────────────────────────────────────────────┐
│                                                        │
│   Automated Wafer/Die Prober & Precision LCR Meter     │
│                                                        │
└───────────────────────────┬────────────────────────────┘
                            │
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                                                        │
│    Step 1: C-V Extraction of Storage Capacitance Cs    │
│            & Bitline Parasitic Capacitance Cb          │
│                                                        │
└───────────────────────────┬────────────────────────────┘
                            │
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Step 2: Capacitance Ratio (Cb / Cs) & Sense-Margin    │
│           Differential Voltage (ΔV) Computation        │
│                                                        │
└───────────────────────────┬────────────────────────────┘
                            │
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                                                        │
│  Step 3: March C- Read Margin Correlation & Validation │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Automated C-V Extraction on Test Structures
1. Position the collinear/wafer prober onto test structure pads representing the 180 nm 1T1C cell array (8F² folded bitline footprint = $0.259\ \mu\text{m}^2$).
2. Connect the high-precision LCR meter / impedance analyzer to the dedicated bitline and storage node Kelvin pads.
3. Perform capacitance-voltage (C-V) sweeps across the array block (256 or 512 cells per bitline).
4. Measure and log:
   - Storage node capacitance ($C_s$).
   - Total bitline parasitic capacitance ($C_b$ / $C_{BL}$).
5. Execute across a 9-point wafer mapping to verify measurement repeatability.

### Step 2: Parametric Ratio & Signal Development Margin Calculation
1. Extract the capacitance ratio:
   $$R = \frac{C_b}{C_s}$$
2. Verify that $C_b / C_s$ is within the design budget ($5:1$ to $9:1$). If $C_b / C_s > 10:1$, flag wafer block for severe read margin degradation risk.
3. Calculate theoretical differential sense signal voltage $\Delta V$ generated across complementary bitlines ($BL$ and $/BL$) upon access transistor activation:
   $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \times \left(V_{\text{cell}} - \frac{V_{DD}}{2}\right)$$
   *(where precharge voltage is equalized to $V_{DD} / 2$ prior to wordline activation).*

### Step 3: Closed-Loop March C- Sensing Margin Correlation
1. Apply the automated parametric March C- diagnostic sequence via firmware test bench at nominal precharge equalization ($V_{DD} / 2$).
2. Perturb precharge voltage margins or sensing strobe timing offset incrementally to measure operational read signal margin limit.
3. Correlate bit error locations identified by the Bitmap Fault Logger against locations exhibiting low $C_s$ or high $C_b / C_s$ ratio.

---

## 3. Key Metrology & Margin Budgets

```text
                Target Metrology & Margin Parameters    
            ┌──────────────────────────────────────────┐
            │░░░░░░░░░░░░░░░░░░░░░░░░░░░               │
Delta V (mV)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░               │
 Cb Nom (fF)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
            │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
 Cs Nom (fF)┤███████                                   │
            │███████                                   │
            └┬─────────┬──────────┬─────────┬─────────┬┘
             0        50         100       150      200 
```

---

## 4. Machine-Measurable Acceptance Criteria Target Metrics

1. **Storage Node Capacitance ($C_s$)**:
   - **Target**: $25\ \text{fF} \le C_s \le 30\ \text{fF}$ per cell (Nominal: $28\ \text{fF}$).
2. **Bitline Parasitic Capacitance ($C_b$ / $C_{BL}$)**:
   - **Target**: $150\ \text{fF} \le C_b \le 250\ \text{fF}$ per array block (256 or 512 cells per bitline).
3. **Capacitance Ratio ($C_b / C_s$)**:
   - **Target**: $5.0 : 1 \le \frac{C_b}{C_s} \le 9.0 : 1$ (Hard Reject Threshold: $\frac{C_b}{C_s} \le 10.0 : 1$).
4. **Differential Read Signal Margin ($\Delta V$)**:
   - **Target**: $100\ \text{mV} \le \Delta V \le 150\ \text{mV}$.
5. **Metrology Gauge R&R Repeatability**:
   - **Target**: Measurement Coefficient of Variation $CV < 1.0\%$ across 9-point wafer mapping.

---

## 5. Literature Sources Cited
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**: Storage node capacitance $C_s \ge 25\ \text{fF} - 30\ \text{fF}$ (nominally $28\ \text{fF}$), bitline capacitance $C_b = 150\ \text{fF} - 250\ \text{fF}$, capacitance ratio $C_b / C_s$ maintained between $5:1$ and $9:1$ (degrades severely $>10:1$), folded bitline footprint $8F^2 = 0.259\ \mu\text{m}^2$ at $F = 180\ \text{nm}$, 256 or 512 cells per bitline.
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**: Differential voltage signal development equation $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \times \left(V_{\text{cell}} - \frac{V_{DD}}{2}\right)$, nominal signal $\Delta V \approx 100\ \text{mV} - 150\ \text{mV}$ for $C_s = 25\ \text{fF}$ and $C_{BL} = 250\ \text{fF}$.
- **Four-Point Collinear Probe Metrology for Semiconductor Sheet Resistance**: Metrology Gauge R&R repeatability requirement $CV < 1.0\%$ across 9-point wafer mapping.

# SOP: ESP32 Variable-Interval Retention Test Pattern & March C- Generator Implementation

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Node
- **Module Hierarchy**: Architecture & Integration > ESP32 Closed-Loop Motor Controller > Automated Parametric Retention & March C- Diagnostic Test Firmware > Automated Variable-Delay Parametric Retention Metrology & Telemetry Logger > ESP32 Variable-Interval Retention Test Pattern & March C- Generator Implementation

---

## 1. Overview & Scope
This Standard Operating Procedure (SOP) specifies the firmware architecture, execution sequence, and telemetry protocols for testing 180nm 1T1C DRAM test vehicles using an ESP32-based controller. The firmware integrates:
1. **March C- Diagnostic Engine**: 6-element functional algorithm ($10N$ complexity) to weed out stuck-at faults (SAF), transition faults (TF), coupling faults (CFin, CFid), and address decoder faults (AF).
2. **Variable-Interval Retention Metrology Engine**: Static array write-pause-read sequence without refresh commands across configurable pause intervals ($t_{\text{pause}}$) to evaluate cell leakage, weak bits, and data retention time thresholds at room and elevated temperatures (85°C).

---

## 2. Theoretical Background & Physical Parameter References
All physical parameter budgets are directly grounded in verified literature for the 180nm DRAM node:
- **Unit Cell Geometry**: NMOS Access Transistor with gate length $L = 180\text{ nm}$, gate width $W = 220\text{ nm}$, bitline/wordline pitch $360\text{ nm} - 400\text{ nm}$, physical gate oxide thickness $T_{\text{ox}} \approx 3.5\text{ nm}$ (thermally grown at 850°C–900°C).
- **Cell Layout & Storage Node**: 8F² folded bitline (cell area $0.259\ \mu\text{m}^2$) or 6F² open bitline ($0.194\ \mu\text{m}^2$). Crown-type stacked capacitor over bitline (COB) utilizing ONO, $\text{Si}_3\text{N}_4$, or $\text{Ta}_2\text{O}_5$ high-$k$ dielectric ($\kappa > 15$, $\text{EOT} = 3\text{ to }4\text{ nm}$).
- **Capacitance Budgets**: 
  - Storage capacitance $C_s$: Nominally $28\text{ fF}$ (minimum $25\text{ fF} - 30\text{ fF}$).
  - Bitline parasitic capacitance $C_b$: $150\text{ fF} - 250\text{ fF}$ across 256–512 cells/bitline.
  - Bitline-to-cell capacitance ratio $C_b / C_s$: strictly $5:1$ to $9:1$ (must not exceed $10:1$).
- **Leakage & Retention Target**: Sub-threshold and junction leakage target $\le 1\text{ fA/cell}$ at 85°C to achieve target retention time $t_{\text{ret}} > 64\text{ ms}$.

---

## 3. SOP Step-by-Step Execution Procedure

### Step 1: ESP32 Diagnostic Subsystem Initialization & Bus Timing Configuration
1. Initialize the ESP32 high-speed GPIO bus interface connected to the DRAM prototype (Address bus $A[n:0]$, Data bus $DQ[m:0]$, Control lines: $\overline{\text{RAS}}$, $\overline{\text{CAS}}$, $\overline{\text{WE}}$, $\overline{\text{CS}}$, $\text{CKE}$).
2. Configure ESP32 hardware timers (High-Resolution Timer / ESP-IDF `esp_timer`) to synchronize control strobe widths respecting 180nm pad delay and settle times. Set UART/USB telemetry streaming baud rate to 921,600 baud.
3. Apply standard DRAM power-up initialization:
   - Stabilize $V_{\text{DD}}$ and $V_{\text{PP}}$ pump bias.
   - Assert $\text{CKE}$ high with continuous NOP/precharge cycles for a minimum of $200\ \mu\text{s}$.
   - Issue All-Bank Precharge (`PALL`) followed by 8 auto-refresh (`REF`) cycles.
   - Program Mode Register (MRS) for burst length (BL = 1, 4, or 8) and $\text{CAS}$ latency.

### Step 2: Full-Array March C- Fault Screening Execution
Execute the 6-pass March C- sequence across all addresses $0$ to $N-1$:
1. **Element M0** $(\Updownarrow (w0))$: Write 0 to all memory cells in ascending address order.
2. **Element M1** $(\Uparrow (r0, w1))$: Read cell (verify 0), write 1 to cell in ascending address order.
3. **Element M2** $(\Uparrow (r1, w0))$: Read cell (verify 1), write 0 to cell in ascending address order.
4. **Element M3** $(\Downarrow (r0, w1))$: Read cell (verify 0), write 1 to cell in descending address order.
5. **Element M4** $(\Downarrow (r1, w0))$: Read cell (verify 1), write 0 to cell in descending address order.
6. **Element M5** $(\Updownarrow (r0))$: Read cell (verify 0) in ascending or descending address order.
*Abort condition*: Any mismatched read bit records a fatal cell stuck-at/coupling failure. Flag address, bit position, and pass number in telemetry log.

### Step 3: Variable-Interval Retention Test Pattern Execution
After confirming functional sanity via March C-, initiate the automated parametric retention cycle:
1. **Pattern Ingestion**: Fill array with target topological data pattern:
   - Pattern A: Solid $0$ (`0x0000`)
   - Pattern B: Solid $1$ (`0xFFFF`)
   - Pattern C: Checkerboard (`0xAA55` / `0x55AA`) to evaluate maximum adjacent wordline/bitline fringing fields.
2. **Refresh Inhibition & Variable Pause ($t_{\text{pause}}$)**:
   - Disable auto-refresh controller (inhibit `REF` commands).
   - Enter controlled hardware wait state using `esp_timer_get_time()` with interval $t_{\text{pause}}$.
   - Sweep $t_{\text{pause}}$ across logarithmic test points:
     $$t_{\text{pause}} \in \{1\text{ ms}, 10\text{ ms}, 32\text{ ms}, 64\text{ ms}, 100\text{ ms}, 250\text{ ms}, 500\text{ ms}, 1000\text{ ms}\}$$
3. **Burst Read & Fault Identification**:
   - Immediately activate wordlines and perform full burst read across the array.
   - Compare read data word with written pattern buffer.
   - Record count of flipped bits ($1 \to 0$ due to capacitor discharge leakage, or $0 \to 1$ due to coupling).
   - Stream telemetry packet over serial: `[TIMESTAMP, T_PAUSE_MS, TEMP_C, TOTAL_FLIPS, FAILING_ROW_COL]`.

### Step 4: Weak-Bit Mapping & Telemetry CDF Curve Generation
1. Aggregate bit failure counts against $t_{\text{pause}}$ points to generate the Cumulative Distribution Function (CDF) of cell retention time.
2. Identify tail distribution bits (cells failing before $t_{\text{ret}} = 64\text{ ms}$ at 85°C) indicating gate oxide micro-defects or junction leakage exceeding $1\text{ fA/cell}$.

---

## 4. Machine-Measurable Acceptance Criteria Target Metrics

| Parameter / Metric | Target Value | Physical Unit | Tolerance / Limit Condition |
| :--- | :--- | :--- | :--- |
| **March C- Functional Fault Coverage** | 100 | % | Zero Stuck-at / Address decoder / Coupling faults allowed across array |
| **Nominal Storage Node Capacitance ($C_s$) Retention Threshold** | 64 | $\text{ms}$ | Minimum pause time without bit flips at $T_{\text{junction}} = 85^\circ\text{C}$ (corresponds to $C_s \ge 25 - 30\text{ fF}$) |
| **Cell Equivalent Leakage Current Target** | $\le 1.0$ | $\text{fA/cell}$ | Deduced from retention decay $\Delta V / t_{\text{pause}}$ at $85^\circ\text{C}$ |
| **Capacitance Ratio Operational Window ($C_b / C_s$)** | $5.0 : 1 \text{ to } 9.0 : 1$ | ratio | Must maintain read sensing margin; bitline parasitic $C_b = 150 - 250\text{ fF}$ with $C_s \approx 28\text{ fF}$ |

---

## 5. References & Literature Context
1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Transistor dimensions $L = 180\text{ nm}, W = 220\text{ nm}$, ONO / high-$k$ dielectric ($\kappa > 15$), $C_s \ge 28\text{ fF}$, leakage $< 1\text{ fA/cell}$ at 85°C.
2. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**: 8F² ($0.259\ \mu\text{m}^2$) and 6F² ($0.194\ \mu\text{m}^2$) layouts, $C_s = 25 - 30\text{ fF}$, $C_b = 150 - 250\text{ fF}$, $C_b / C_s = 5:1\text{ to }9:1$.
3. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: Stacked crown/cylinder capacitor with EOT $3 - 4\text{ nm}$, retention $> 64\text{ ms}$ at 85°C, pitch $360 - 400\text{ nm}$, $T_{\text{ox}} \approx 3.5\text{ nm}$.

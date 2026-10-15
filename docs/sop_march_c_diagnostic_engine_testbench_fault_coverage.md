# Standard Operating Procedure (SOP)
## March C- Diagnostic Engine Testbench Simulation & Fault Coverage Metrology

- **Document ID**: SOP-MET-DRAM180-MARCHC-001
- **Process Generation**: Gen 2 (180nm / µm)
- **Action Type**: Buy (Commercial Verification IP / EDA Simulation & Fault Modeling Toolkit)
- **Status**: Released / Operational

---

### 1. Scope & Objective
This SOP defines the step-by-step testbench simulation setup, fault injection configuration, and coverage metrology verification for the **March C- Diagnostic Engine** targeting the 180nm Open-Source DRAM Chip architecture. It verifies full test algorithm sequence execution across stacked capacitor 1T1C cells and validates detection efficiency against classic memory fault classes (Stuck-At, Transition, Address Decoder, and Coupling Faults).

---

### 2. Relevant Sources & Physical Context
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
  - Stacked capacitor (COB) with crown polysilicon / MIM structure over W-plug.
  - ONO / high-k stack dielectric ($\kappa > 15$).
  - Storage node capacitance budget $C_s \ge 28\text{ fF}$ per cell.
  - Sub-threshold and junction leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
  - Folded bitline $8F^2$ footprint ($0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$) with noise rejection.
  - Storage node capacitance $C_s = 25\text{ to }30\text{ fF}$ (nominally $28\text{ fF}$).
  - Bitline parasitic capacitance $C_b = 150\text{ to }250\text{ fF}$ across 256/512 cell array blocks.
  - Capacitance ratio constraint $C_b / C_s$ maintained between $5:1$ and $9:1$ (must not exceed $10:1$).
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - Retention time $> 64\text{ ms}$ at $85^\circ\text{C}$.
  - Bitline and wordline pitch of $360\text{ nm to }400\text{ nm}$.
  - Gate oxide physical thickness $t_{ox} \approx 3.5\text{ nm}$ grown at $850^\circ\text{C}-900^\circ\text{C}$.

---

### 3. Step-by-Step Procedure

```text
┌───────────────────────┐
│                       │
│   Setup 180nm DRAM    │
│     Array Netlist     │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│    Inject Physical    │
│     Fault Models      │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│   Execute March C-    │
│  Sequence Generator   │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│  Sense Amp Strobe &   │
│  Timing Verification  │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│    Fault Coverage     │
│       Metrology       │
│      Calculation      │
│                       │
└───────────────────────┘
```

#### Step 1: Netlist & Parasitic Model Parameterization
1. Instantiate the nominal $8F^2$ folded bitline array block (256 wordlines $\times$ 512 bitline pairs) with cell layout parameters:
   - Access NMOS: $L = 180\text{ nm}$, $W = 220\text{ nm}$, $t_{ox} = 3.5\text{ nm}$.
   - Nominal storage node capacitance: $C_s = 28.0\text{ fF}$.
   - Nominal bitline parasitic capacitance: $C_b = 200.0\text{ fF}$ ($C_b / C_s = 7.14:1$, strictly compliant with the $5:1 - 9:1$ range).
   - Cell leakage profile: $I_{leak} \le 1.0\text{ fA}$ at $85^\circ\text{C}$.
2. Couple the SPICE/Mixed-Signal Behavioral Testbench with the March C- FSM RTL engine synthesized for test generation.

#### Step 2: Fault Injection Matrix Insertion
1. Configure deterministic fault injection across cell storage nodes and wordline/bitline addresses:
   - **Stuck-At Faults (SAF)**: Inject node short to $V_{DD}$ (SA1) and node short to $V_{SS}$ (SA0).
   - **Transition Faults (TF)**: Force write transition suppression ($0 \to 1$ and $1 \to 0$ failures due to high-resistance W-plugs).
   - **Address Decoder Faults (AF)**: Emulate address line bridging and non-consecutive multi-row assertion.
   - **Coupling Faults (CFin / CFid)**: Model inter-bitline capacitive coupling across the $360\text{ nm}$ bitline pitch using bridging capacitance $C_{couple} > 0.15 \times C_b$.

#### Step 3: March C- Algorithmic Sequence Execution
1. Run the standardized 6-element March C- test sequence ($10N$ complexity):
   - Element 1: $\Updownarrow (w0)$ — Initialize all cells to '0'.
   - Element 2: $\Uparrow (r0, w1)$ — Address ascending: verify '0', write '1'.
   - Element 3: $\Uparrow (r1, w0)$ — Address ascending: verify '1', write '0'.
   - Element 4: $\Downarrow (r0, w1)$ — Address descending: verify '0', write '1'.
   - Element 5: $\Downarrow (r1, w0)$ — Address descending: verify '1', write '0'.
   - Element 6: $\Updownarrow (r0)$ — Final read verify all cells equal '0'.

#### Step 4: Sense Amplifier Strobe Timing & Signal Margin Evaluation
1. Set the sense amplifier differential strobe window:
   - Signal margin prior to latch activation: $\Delta V_{BL} = \frac{V_{DD}}{2} \cdot \frac{1}{1 + C_b / C_s}$.
   - Ensure differential strobe margin $\Delta V_{BL} \ge 120\text{ mV}$ across all read cycles.
2. Confirm the test engine captures read-compare discrepancies at cycle intervals matching the memory bus timing without missing transient strobes.

#### Step 5: Coverage Metrology and Diagnostic Log Extraction
1. Aggregate simulated fault responses against the Golden Reference log.
2. Extract Fault Detection Ratios ($FDR = \frac{\text{Detected Faults}}{\text{Total Injected Faults}} \times 100\%$) across all fault taxonomies.
3. Validate that runtime fault diagnostic mapping flags the exact row, column, and physical failure type.

---

### 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Unit | Target Specification | Validation Method |
| :--- | :--- | :--- | :--- |
| **Stuck-At & Transition Fault Coverage** | $\%$ | $100.0\%$ | Automated Fault Simulation Log Audit |
| **Address Decoder Fault Coverage (AF)** | $\%$ | $100.0\%$ | March C- Address Ascend/Descend Vector Verification |
| **Inversion & Idempotent Coupling Fault Coverage (CF)** | $\%$ | $\ge 98.0\%$ | Inter-bitline Crosstalk Injection Analysis |
| **Capacitance Ratio Compliance ($C_b / C_s$)** | Ratio | $5.0:1 \text{ to } 9.0:1$ | Testbench Extracted Parasitic Netlist Audit |
| **Read Strobe Signal Margin ($\Delta V_{BL}$)** | $\text{mV}$ | $\ge 120\text{ mV}$ | Mixed-Signal Transient Sense Strobe Measurement |

---

### 5. Fault Coverage Summary

```text
                 March C- Fault Coverage Metrology (%)  
               ┌───────────────────────────────────────┐
               │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
CFin (Coupling)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
               │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
TF (Transition)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
   AF (Address)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
               │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
 SAF (Stuck-At)┤███████████████████████████████████████│
               │███████████████████████████████████████│
               └┬─────────┬────────┬─────────┬────────┬┘
                0        25       50        75      100 
```

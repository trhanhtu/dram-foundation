# Standard Operating Procedure (SOP): March C- Algorithmic Test Vector & ATE Timing Pattern Generation

- **Document ID**: `SOP-MET-DRAM180-MARCHC-001`
- **Revision**: `v1.0.0`
- **Scope**: Metrology & Wafer Electrical Sort / Functional Array Probing
- **Process Node**: 180nm Open-Source DRAM (DRAM Foundation VN), 1T1C COB (Capacitor-Over-Bitline)
- **Cell Geometry / Target**: $L = 180\text{ nm}$, $W = 220\text{ nm}$, Cell Capacitance $C_{cell} \ge 28\text{ fF}$ (or $25\text{--}30\text{ fF}$ baseline)

---

## 1. Overview & Algorithmic Principle

The **March C-** algorithm is a standard $10N$ algorithmic memory test pattern designed to detect single-cell and multi-cell coupling defects in dense random-access memories. For the 180nm DRAM cell array, March C- specifically uncovers:
- **AF (Address Decoder Faults)**
- **SAF (Stuck-At Faults: SA0, SA1)**
- **TF (Transition Faults: Up/Down transitions)**
- **CFin (Inversion Coupling Faults)**
- **CFid (Idempotent Coupling Faults)**

The test sequence consists of 6 algorithmic elements:
$$\{\Uparrow (w0); \Uparrow (r0, w1); \Uparrow (r1, w0); \Downarrow (r0, w1); \Downarrow (r1, w0); \Updownarrow (r0)\}$$

---

## 2. ATE Operating Conditions & Electrical Timing Setup

| Parameter | Symbol | Nominal Value | Unit | Verification / Condition |
| :--- | :--- | :--- | :--- | :--- |
| **Logic Core Supply** | $V_{DD}$ | $1.8 \pm 0.1$ | $\text{V}$ | $I_{on} \ge 500\ \mu\text{A}/\mu\text{m}$, $I_{off} \le 10\ \text{pA}/\mu\text{m}$ |
| **Wordline Boosted Voltage** | $V_{PP}$ | $3.3 \pm 0.15$ | $\text{V}$ | Overdrives NMOS pass-gate ($V_{thn} = 0.55\text{ V}$) |
| **Bitline Precharge Voltage** | $V_{BLP}$ | $0.90 \pm 0.05$ | $\text{V}$ | $V_{DD} / 2$ midpoint precharge |
| **Plate Bias Voltage** | $V_{CP}$ | $0.90 \pm 0.05$ | $\text{V}$ | Cell plate bias across high-k dielectric |
| **Test Cycle Time** | $t_{CK}$ | $50.0$ | $\text{ns}$ | $20\text{ MHz}$ ATE vector rate |
| **Row Active Time** | $t_{RAS}$ | $30.0$ | $\text{ns}$ | Wordline activation window |
| **Sense Amplifier Strobe Delay** | $t_{RCD}$ | $15.0$ | $\text{ns}$ | Delay from WL fire to sense activation |
| **Data Retention Pause** | $t_{RET}$ | $64.0$ | $\text{ms}$ | Measured at wafer chuck temperature $T = 85^\circ\text{C}$ |

---

## 3. Step-by-Step Execution Procedure

### Step 1: Automated Test Equipment (ATE) Pin Electronics & Timing Initialization
1. Configure ATE drive and compare levels:
   - High-level drive: $V_{IH} = 1.8\text{ V}$
   - Low-level drive: $V_{IL} = 0.0\text{ V}$
   - Comparator threshold: $V_{REF} = 0.9\text{ V}$ ($V_{OH} = 1.2\text{ V}$, $V_{OL} = 0.6\text{ V}$)
2. Align probe-card edge pin delays to sub-100 ps skew across all row/column addresses and DQs.
3. Verify open/short continuity on pad ring before applying $V_{DD} = 1.8\text{ V}$.

### Step 2: Algorithmic Pattern Generator (ALPG) Vector Generation
Execute the $10N$ March C- sequence across all physical row addresses ($0$ to $R_{max}$) and column addresses ($0$ to $C_{max}$):
- **Element M0** $[\Uparrow (w0)]$: Step through address sequence in ascending order ($0 \to N-1$), executing a Write '0' vector at each address. Total operations: $1N$.
- **Element M1** $[\Uparrow (r0, w1)]$: Ascending address order. Read verify cell contains '0', strobe comparator; immediately execute Write '1'. Total operations: $2N$.
- **Element M2** $[\Uparrow (r1, w0)]$: Ascending address order. Read verify cell contains '1', strobe comparator; immediately execute Write '0'. Total operations: $2N$.
- **Element M3** $[\Downarrow (r0, w1)]$: Descending address order ($N-1 \to 0$). Read verify '0'; execute Write '1'. Total operations: $2N$.
- **Element M4** $[\Downarrow (r1, w0)]$: Descending address order ($N-1 \to 0$). Read verify '1'; execute Write '0'. Total operations: $2N$.
- **Element M5** $[\Updownarrow (r0)]$: Arbitrary / ascending address order. Read verify '0' across entire array. Total operations: $1N$.

### Step 3: High-Temperature Retention Strobe ($85^\circ\text{C}$)
1. Set wafer thermal chuck to $85 \pm 1^\circ\text{C}$.
2. Repeat March C- with an inserted static pause of $64\text{ ms}$ between write and read vectors without array refresh commands to screen for excessive subthreshold or junction leakage ($> 1\text{ fA/cell}$).

### Step 4: Real-Time Fail-Address Memory (AFM) Logging & Bitmap Probing
1. Capture any strobe comparison mismatch into the ATE Real-Time Bit Error Memory (BEM).
2. De-scramble topological row/column addresses into physical die coordinates (accounting for folded bitline $8F^2/6F^2$ topology and bitline twisting).
3. Classify defects into:
   - Single-bit defect (isolated cell leakage or capacitor open).
   - Wordline / Bitline paired shorts (CFin / CFid).
   - Array-block cluster failures (decoder fault).

---

## 4. Machine-Measurable Acceptance Criteria

1. **Storage Cell Capacitance**:
   - $C_{cell} \ge 28\text{ fF}$ (or nominal specification range $25\text{ to }30\text{ fF/cell}$).
2. **Cell Leakage Current**:
   - Sub-threshold and junction leakage $I_{leak} \le 1.0\text{ fA/cell}$ at $85^\circ\text{C}$.
3. **Data Retention Time**:
   - Retention time $t_{RET} \ge 64\text{ ms}$ at $85^\circ\text{C}$ chuck temperature.
4. **Access Transistor On/Off Integrity**:
   - Nominal supply $V_{DS} = 1.8\text{ V}$, $I_{on} \ge 500\ \mu\text{A}/\mu\text{m}$ (at $V_{GS} = 1.8\text{ V}$), $I_{off} \le 10\text{ pA}/\mu\text{m}$ (at $V_{GS} = 0\text{ V}$), yielding $I_{on}/I_{off} > 10^7$.
5. **Array Functional Yield**:
   - Zero unrepairable multi-cell coupling or decoder failures post-redundancy laser blowing.

---

## 5. Literature References & PDK Context

- **Source 1**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench* (COB crown/MIM capacitor, $C_{cell} \ge 28\text{ fF}$, leakage $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$, $L=180\text{ nm}$, $W=220\text{ nm}$).
- **Source 2**: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering* (1T1C $8F^2/6F^2$ layout, minimum capacitance $25\text{ to }30\text{ fF/cell}$, data retention time $> 64\text{ ms}$ at $85^\circ\text{C}$, gate dielectric $3.5\text{ nm}$).
- **Source 3**: *Stage 3 Reality Gate: Discrete Long-Channel MOSFET & CMOS Inverter Verification* ($V_{thn} = +0.55\text{ V} \pm 50\text{ mV}$, $I_{on} \ge 500\ \mu\text{A}/\mu\text{m}$, $I_{off} \le 10\text{ pA}/\mu\text{m}$, $I_{on}/I_{off} > 10^7$ at $V_{DS}=1.8\text{ V}$).

# Standard Operating Procedure (SOP): 1T1C Device Extraction & LVS Rule Deck Benchmark Validation

- **Task Title**: 1T1C Device Extraction & LVS Rule Deck Benchmark Validation
- **Node Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > Commercial Open-Source 180nm PDK Setup & Physical Verification Rule Decks > Custom DRAM 8F2 COB Cell DRC/LVS Rule Deck Adaptation and Layer Definition > 1T1C Device Extraction & LVS Rule Deck Benchmark Validation
- **Generation**: Gen 3 (nm)
- **Action Type**: Make
- **Status**: Accepted

---

## 1. Scope & Objective
Validate physical device extraction definitions and Layout Versus Schematic (LVS) comparison rules for the 180nm 1T1C DRAM bitcell (folded-bitline 8F² architecture). Ensure proper recognition of the access NMOS transistor, capacitor-over-bitline (COB) storage node capacitor ($C_s$), wordline (WL), bitline (BL), and reference plate connections without false opens, shorts, or pin mismatches.

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│  Layout GDS / Netlist  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Device Recognition &  │
│    Layer Derivation    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   1T Access FET & 1C   │
│    Node Extraction     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  LVS Comparison BL/WL  │
│      Connectivity      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Benchmark Acceptance  │
│       Evaluation       │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Execution Procedure

### Step 1: Input Netlist and GDS Boundary Preparation
1. Load schematic benchmark testbench containing:
   - 1T1C cell instance ($M_{access}$ NMOS and $C_s$ storage capacitor).
   - Complementary bitline folded pairs (`BL`, `/BL`) and Wordline (`WL`).
   - Equalization and precharge circuitry ($V_{DD}/2 = 0.9\ \text{V}$ reference line).
2. Import the layout GDSII for the $8F^2$ folded bitline cell:
   - Feature size: $F = 180\ \text{nm}$ ($0.18\ \mu\text{m}$).
   - Total physical cell footprint area: $A_{cell} = 8F^2 = 0.259\ \mu\text{m}^2$.

### Step 2: Layer Derivation & Device Recognition Rules Definition
1. Define the boolean layer combinations for access NMOS:
   - Channel region = `DIFF` AND `POLY` NOT `PPLUS` inside `NWELL_HOLE` (P-substrate/P-well).
   - Drain pin connected to `BL` contact; Source pin connected to internal Storage Node (`SN`).
   - Gate pin connected to `WL` (`POLY` / `POLY2`).
2. Define the COB capacitor extraction recognition layer:
   - `CAP_TOP` plate (connected to cell plate bias $V_{DD}/2$) over dielectric layer over `CAP_BOT` storage node plug.
   - Form device extraction statement:
     ```text
     DEVICE C(DRAM_CAP) CAP_BOT CAP_TOP [model_name=C_DRAM]
     DEVICE M(NMOS_1T) POLY DIFF DIFF PWELL [model_name=NMOS_DRAM]
     ```

### Step 3: Device Parameter Extraction & Dimension Verification
1. Extract channel width $W$ and channel length $L$ for the sub-micron access NMOS:
   - Benchmark target geometry: $W / L = 2.0\ \mu\text{m} / 0.18\ \mu\text{m}$ (or local array scaled access device geometry with nominal $L = 180\ \text{nm}$).
2. Extract storage capacitor capacitance $C_s$ based on specific dielectric constant and physical area:
   - Verify extracted $C_s \ge 25.0\ \text{fF}$ to $30.0\ \text{fF}$ (nominal target $28.0\ \text{fF}$).
3. Extract bitline parasitic capacitance $C_b$ for a 256 or 512 cell array column:
   - Baseline $C_b$ range: $150\ \text{fF}$ to $250\ \text{fF}$.

### Step 4: LVS Comparison & Topology Matching Execution
1. Execute LVS engine (e.g., KLayout `check_lvs` / Magic / Netgen):
   - Check pin matching for ports: `BL`, `/BL`, `WL`, `V_PLATE`, `V_WELL`.
   - Verify one-to-one port and device correspondence between schematic netlist and extracted layout netlist.
2. Confirm zero unwired nets, zero short circuits, and zero dangling capacitor nodes.

### Step 5: Read Margin Ratio & DC Operating Checks
1. Calculate capacitance budget ratio:
   $$\text{Ratio} = \frac{C_b}{C_s}$$
   Ensure $5:1 \le C_b/C_s \le 9:1$. Confirm ratio does not exceed the critical limit of $10:1$.
2. Verify signal development potential margin:
   $$\Delta V = \left(\frac{C_s}{C_b + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right) \ge 100\ \text{mV} \text{ to } 150\ \text{mV}$$
3. Validate discrete access NMOS DC metrics against baseline:
   - $V_{thn} = +0.55\ \text{V} \pm 50\ \text{mV}$ (measured at $V_{DS} = 50\ \text{mV}$).
   - $I_{on} \ge 500\ \mu\text{A}/\mu\text{m}$ at $V_{GS} = 1.8\ \text{V}$, $V_{DS} = 1.8\ \text{V}$.
   - $I_{off} \le 10\ \text{pA}/\mu\text{m}$ at $V_{GS} = 0\ \text{V}$, $V_{DS} = 1.8\ \text{V}$ (On/Off ratio $> 10^7$).

---

## 4. Machine-Measurable Acceptance Criteria

```text
                DRAM Storage Node Capacitance Spec (fF) 
               ┌───────────────────────────────────────┐
               │███████████████████████████████████████│
C_s (Upper Min)┤███████████████████████████████████████│
  C_s (Nominal)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   │
               │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   │
 C_s (Min Spec)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      │
               │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      │
               └┬─────────┬────────┬─────────┬────────┬┘
               0.0       7.5     15.0      22.5    30.0 
```

| Metric ID | Parameter | Minimum Spec | Nominal / Target | Maximum Spec | Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AC-01** | Physical 8F² Cell Area | $0.250$ | $0.259$ ($8 \times 0.18^2$) | $0.270$ | $\mu\text{m}^2$ | DRC / GDS Layout Boundary Extraction |
| **AC-02** | Storage Capacitance ($C_s$) | $25.0$ | $28.0$ | $30.0$ | $\text{fF}$ | LVS Extracted Device Parameter ($C$) |
| **AC-03** | Parasitic Ratio ($C_b / C_s$) | $5.0$ | $7.0$ | $9.0$ (Strict $\le 10.0$) | ratio | Array Column Extraction (256/512 cells/BL) |
| **AC-04** | Access NMOS $V_{thn}$ | $+0.50$ | $+0.55$ | $+0.60$ | $\text{V}$ | SPICE Extraction ($V_{DS} = 50\ \text{mV}$) |
| **AC-05** | NMOS $I_{on} / I_{off}$ Ratio | $10^7$ | $> 10^7$ | — | ratio | DC Sweep ($I_{on} \ge 500\ \mu\text{A}/\mu\text{m}$, $I_{off} \le 10\ \text{pA}/\mu\text{m}$) |
| **AC-06** | Readout Signal Margin ($\Delta V$) | $100$ | $120$ | $150$ | $\text{mV}$ | Folded BL Sense Development Simulation |

---

## 5. Citations & Verified Literature Context
1. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Footprint: $8F^2 = 0.259\ \mu\text{m}^2$ at $F = 180\ \text{nm}$.
   - Storage capacitance $C_s \ge 25\ \text{fF}$ to $30\ \text{fF}$ (nominal $28\ \text{fF}$).
   - Bitline capacitance $C_b = 150\ \text{fF}$ to $250\ \text{fF}$ for 256/512 cells.
   - Ratio $C_b / C_s$ within $5:1$ to $9:1$ (degrades severely if $> 10:1$).
2. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
   - Differential readout voltage $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{cell} - V_{DD}/2) \approx 100\ \text{mV} \text{ to } 150\ \text{mV}$ at $C_s = 25\ \text{fF}$, $C_{BL} = 250\ \text{fF}$.
   - Equalization to $V_{DD}/2$.
3. **Stage 3 Reality Gate: Discrete Long-Channel MOSFET & CMOS Inverter Verification**:
   - Target sub-micron transistor gate: $W / L = 2.0\ \mu\text{m} / 0.18\ \mu\text{m}$ ($180\ \text{nm}$).
   - NMOS linear threshold voltage: $V_{thn} = +0.55\ \text{V} \pm 50\ \text{mV}$ at $V_{DS} = 50\ \text{mV}$.
   - On/Off current ratio: $I_{on} \ge 500\ \mu\text{A}/\mu\text{m}$ at $V_{GS} = 1.8\ \text{V}$, $I_{off} \le 10\ \text{pA}/\mu\text{m}$ at $V_{GS} = 0\ \text{V}$ (Ratio $> 10^7$).

# SOP: PVT Corner Netlist Extraction & Precharge Equalization Testbench Setup

- **Date**: 2026-10-13
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Node Classification**: Gen 2 (µm) / Leaf Node / Action: Make
- **Hierarchy Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 1T1C DRAM Cell Topology & Layout (8F²) [DRAM Architecture] > 1T1C Access Transistor & Bitline Contact Layout DRC/LVS Design (8F²) [Circuit Design] > Layout Versus Schematic (LVS) Extraction & Parasitic Metric Sign-off [Circuit Design] > C_BL/C_s Charge-Sharing Ratio & Delta-V Metric Verification Sign-off [Metrology] > C_BL/C_s Ratio & Sense Margin Sign-off Verification across PVT & Mismatch Corners [Metrology] > PVT Corner Netlist Extraction & Precharge Equalization Testbench Setup [Circuit Design]

---

## 1. Overview & Scope
This Standard Operating Procedure (SOP) defines the execution methodology for extracting post-layout parasitic RC netlists across process, voltage, and temperature (PVT) corners and establishing an automated SPICE testbench. The testbench verifies precision bitline precharge equalization, differential signal development ($\Delta V$), and sense amplifier readiness for an 8F² folded-bitline 180nm open-source DRAM architecture.

---

## 2. Structural Metrology & Testbench Workflow

```text
┌──────────────────────┐
│                      │
│  PVT Corner Netlist  │
│      Extraction      │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│      Testbench       │
│   Instantiation &    │
│        Sizing        │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│     Precharge &      │
│     Equalization     │
│      Transient       │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│       Sign-off       │
│     Verification     │
│                      │
└──────────────────────┘
```

---

## 3. Step-by-Step Procedure

### Step 1: Multi-Corner Parasitic RC Extraction (PEX)
1. Load the DRC/LVS-clean layout database for the 8F² 1T1C DRAM array and interleaved folded bitline ($BL$, $\overline{BL}$) pitch-matched sense amplifier blocks.
2. Configure 3D field-solver parasitic extraction (PEX) with metal sheet resistance, substrate coupling, and cross-coupling capacitances between adjacent bitlines.
3. Generate back-annotated DSPF/SPEF netlists across standard process corners:
   - **TT (Typical-Typical)**: Nominal BSIM4 NMOS/PMOS models ($V_{th} \approx 0.5\text{ V to } 0.7\text{ V}$).
   - **FF (Fast-Fast)**: High drive current, minimized threshold voltage, minimum RC parasitic interconnects.
   - **SS (Slow-Slow)**: Low drive current, elevated threshold voltage, maximum RC parasitic corners.
4. Parameterize operational voltage and temperature ranges:
   - $V_{DD} = 1.8\text{ V} \pm 10\%$ ($1.62\text{ V}$ to $1.98\text{ V}$).
   - Operating temperature: $T = -40^\circ\text{C}$ to $+85^\circ\text{C}$ (worst-case retention/leakage evaluation at $85^\circ\text{C}$).

### Step 2: Precharge Equalization Network & Cell Testbench Setup
1. Instantiate the extracted folded-bitline pair with lumped post-layout bitline capacitance $C_{BL} = 250\text{ fF}$ and access transistor storage node capacitor $C_s = 25\text{ fF}$.
2. Configure the bitline precharge equalization circuit:
   - Three-transistor NMOS equalization network: one bridging equalization pass transistor shorting $BL$ and $\overline{BL}$, and two pull-up pass transistors connecting $BL$ and $\overline{BL}$ to the precision bias line $V_{BLP} = V_{DD} / 2 = 0.9\text{ V}$.
   - Connect the active-high precharge control signal line ($EQ$).
3. Instantiate the cross-coupled regenerative sense amplifier:
   - NMOS cross-coupled pull-down pair ($N$-sense amp) gated to latching node $SAN$.
   - PMOS cross-coupled pull-up pair ($P$-sense amp) gated to latching node $SAP$.
   - Baseline state during precharge: $SAN = V_{DD}/2 = 0.9\text{ V}$ and $SAP = V_{DD}/2 = 0.9\text{ V}$.

### Step 3: Wordline Boost ($V_{PP}$) & Clock Driver Configuration
1. Set up high-voltage wordline pump input rails: $V_{PP} = 2.5\text{ V to } 2.8\text{ V}$ (Dickson oscillator regulated pump level) to provide gate overdrive $\Delta V_{\text{overdrive}}$ compensating for access transistor threshold loss ($V_{DD} + V_{th} = 1.8\text{ V} + 0.6\text{ V} = 2.4\text{ V}$).
2. Configure non-overlapping two-phase clock sources ($\Phi_1, \Phi_2$) at $20\text{ MHz to } 50\text{ MHz}$ for the charge pump regulator model.
3. Configure transient sequence generator:
   - **Phase 1 (Equalization)**: Assert $EQ = V_{DD}$ ($1.8\text{ V}$) to equalize both $BL$ and $\overline{BL}$ to $V_{DD}/2 = 0.9\text{ V}$.
   - **Phase 2 (Precharge Cut-Off & WL Activation)**: De-assert $EQ \to 0\text{ V}$. Transition wordline $WL$ from $0\text{ V}$ to $V_{PP} = 2.6\text{ V to } 2.8\text{ V}$.
   - **Phase 3 (Charge Sharing)**: Dump cell charge $Q_s = C_s \cdot (V_{\text{cell}} - V_{BL})$ onto $BL$, developing differential voltage $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{\text{cell}} - V_{DD}/2)$.
   - **Phase 4 (Sensing & Latch Activation)**: Strobe $SAN$ to $0\text{ V}$ via NMOS pulldown; after a $1\text{ to } 2\text{ ns}$ delay, strobe $SAP$ to $V_{DD}$ ($1.8\text{ V}$).

### Step 4: SPICE Simulation & Dynamic Metric Extraction
1. Execute multi-corner transient analysis (`.tran 10ps 100ns`) under TT, FF, and SS corners at $T = -40^\circ\text{C}, 25^\circ\text{C}, 85^\circ\text{C}$.
2. Extract the equalization settling time $t_{\text{eq}}$ required for $|V(BL) - V(\overline{BL})| \le 1.0\text{ mV}$ prior to wordline firing.
3. Measure differential read signal $\Delta V$ immediately prior to $SAN$ activation for both stored '1' ($V_{\text{cell}} = 1.8\text{ V}$) and stored '0' ($V_{\text{cell}} = 0\text{ V}$).
4. Log and verify PVT corner margins against operational specifications.

---

## 4. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Acceptance Target Metric | Unit | Physical Context / Verification Condition |
| :--- | :--- | :--- | :--- |
| **Bitline Precharge Equalization Voltage ($V_{BL,eq}$)** | $0.90 \pm 0.01$ ($V_{DD}/2$) | $\text{V}$ | Nominal $V_{DD} = 1.8\text{ V}$, steady-state level on $BL$ and $\overline{BL}$ during $EQ = \text{HIGH}$ |
| **Differential Signal Margin ($\Delta V$)** | $100.0\text{ to } 150.0$ | $\text{mV}$ | Signal development after WL assertion for $C_s = 25\text{ fF}, C_{BL} = 250\text{ fF}$ across all PVT corners |
| **Wordline Boost Voltage ($V_{PP}$)** | $2.5\text{ to } 2.8$ | $\text{V}$ | Regulated Dickson charge pump overdrive rail ($V_{PP} \ge V_{DD} + V_{th} + \Delta V_{\text{overdrive}}$) |
| **Sensing Strobe Activation Delay ($t_{SAP - SAN}$)** | $1.0\text{ to } 2.0$ | $\text{ns}$ | Inter-latch delay between $SAN \to \text{GND}$ pull-down and $SAP \to V_{DD}$ pull-up |

---

## 5. Citations & References
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
  - Precharge equalization to $V_{DD} / 2$ using equalization transistor network prior to wordline assertion.
  - Differential signal development: $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{\text{cell}} - V_{DD}/2)$.
  - Nominal physical capacitances: cell capacitance $C_s = 25\text{ fF}$, bitline capacitance $C_{BL} = 250\text{ fF}$, yielding $\Delta V \approx 100\text{ mV to } 150\text{ mV}$.
- **Cross-Coupled Regenerative Sense Amplifier Timing & Charge Restoration**:
  - Equalization phase ties complementary lines $BL$ and $\overline{BL}$ to $V_{BLP} = V_{DD}/2$.
  - Wordline overdrive pulse transitions from $0\text{ V}$ to boosted $V_{PP}$ ($2.6\text{ V to } 2.8\text{ V}$).
  - Multi-phase latching: $SAN$ pulled to $0\text{ V}$, followed by $SAP$ pull-up to $V_{DD}$ with a $1\text{ to } 2\text{ ns}$ delay.
- **High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture**:
  - NMOS enhancement pass transistor threshold $V_{th} \approx 0.5\text{ V to } 0.7\text{ V}$ at 180nm.
  - Avoidance of 33% threshold loss ($V_{DD} - V_{th} = 1.8\text{ V} - 0.6\text{ V} = 1.2\text{ V}$) via boosted overdrive $V_{PP} \ge 2.5\text{ V to } 2.8\text{ V}$.
  - Two-phase non-overlapping clocks ($\Phi_1, \Phi_2$) at $20\text{ MHz to } 50\text{ MHz}$.

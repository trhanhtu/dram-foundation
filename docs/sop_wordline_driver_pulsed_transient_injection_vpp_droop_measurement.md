# SOP: Wordline Driver Pulsed Transient Injection & VPP Droop Measurement

- **Date**: 2026-10-13
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Node Classification**: Gen 2 (µm) / Leaf Node / Action: Make
- **Hierarchy Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > Address Decoders & Wordline VPP Voltage Pump [DRAM Circuit Design] > Transient Post-Layout Verification & VPP Slew Rate Metrology [Metrology] > Wordline VPP Slew Rate & Voltage Drop Transient Metrology Protocol [Metrology] > Wordline Driver Pulsed Transient Injection & VPP Droop Measurement [Metrology]

---

## 1. Overview & Scope
This Standard Operating Procedure (SOP) defines the protocol for pulsed transient current injection into the wordline driver network and high-precision metrology of transient $V_{PP}$ voltage droop, recovery latency, and slew rate for 180nm DRAM architectures. Wordline assertion requires dynamic charge transfer from the boosted $V_{PP}$ rail to overdrive access transistor gates ($L = 180\text{ nm}$, $W = 220\text{ nm}$), ensuring full restoration of cell charge ($C_s \ge 28\text{ fF}$) without threshold voltage loss. This procedure verifies power distribution network (PDN) integrity under peak switching conditions to protect the bitline sensing window.

---

## 2. Structural Metrology Workflow

```text
┌────────────────────────┐
│                        │
│   1. Pulse Injection   │
│    Setup & Netlist     │
│     Configuration      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  2. Transient Dynamic  │
│    Activation (VPP     │
│   Driver Assertion)    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   3. VPP Power Grid    │
│   Droop & Slew Rate    │
│        Capture         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   4. Signal Margin &   │
│  Retention Validation  │
│  (BL Sensing Window)   │
│                        │
└────────────────────────┘
```

---

## 3. Physical Array Metric Baseline

```text
                180nm DRAM Array Physical Dimensions    
             ┌─────────────────────────────────────────┐
             │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
BL Pitch (nm)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
Access W (nm)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                │
             │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                │
Access L (nm)┤█████████████████████                    │
             │█████████████████████                    │
             └┬─────────┬─────────┬─────────┬─────────┬┘
              0        90        180       270      360 
```

---

## 4. Step-by-Step Procedure

### Step 1: Netlist Assembly & Testbench Configuration
1. Import post-layout extracted DSPF/SPEF netlist of the wordline driver hierarchical tree, including the parasitic R-L-C representation of the $V_{PP}$ supply rails and wordline interconnects.
2. Configure 1T1C array cell parameters matching the 180nm cell topology:
   - Access transistor geometry: channel length $L = 180\text{ nm}$, channel width $W = 220\text{ nm}$.
   - Array bitline pitch: $360\text{ nm}$ interleaved layout.
   - Storage node capacitor: $C_s \ge 28\text{ fF}$ (stacked capacitor structure over bitline with high-$\kappa$ dielectric $\kappa > 15$).
   - Folded bitline parasitic capacitance: $C_{BL} = 250\text{ fF}$.
3. Initialize the array precharge state: bitlines equalized to $V_{DD} / 2$ prior to wordline activation.
4. Establish operating environment temperature at $T = 85^\circ\text{C}$ to evaluate worst-case sub-threshold and junction leakages.

### Step 2: Pulsed Transient Injection
1. Define address decoder trigger pulse with sub-nanosecond edge rate applied to the driver input stage.
2. Assert the high-voltage level-shifter and driver PMOS stage to switch the wordline gate from $0\text{ V}$ to boosted rail $V_{PP}$.
3. Execute synchronous multi-driver pulsed activation (simulating simultaneous wordline segment firing) to exert maximum dynamic current load $I_{peak}$ on the $V_{PP}$ power delivery mesh.

### Step 3: $V_{PP}$ Rail Droop & Wordline Slew Metrology
1. Probe local and global $V_{PP}$ node voltages during the transient switching event:
   - Extract peak droop voltage: $\Delta V_{PP\text{,droop}} = V_{PP\text{,nominal}} - V_{PP\text{,min}}$.
   - Verify transient recovery time $t_{rec}$ back to nominal $V_{PP}$ regulation envelope.
2. Measure the wordline voltage risetime ($10\%$ to $90\%$ of full $V_{PP}$) at both near-end (driver output) and far-end array termination pins to quantify RC propagation degradation under power droop.

### Step 4: Bitline Signal Development & Readout Verification
1. Verify access transistor full conduction during the wordline pulse duration:
   - Measure charge dumped onto the bitline: $Q_s = C_s \cdot (V_{\text{cell}} - V_{BL})$.
2. Calculate and measure developed differential sensing voltage:
   $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left|V_{\text{cell}} - \frac{V_{DD}}{2}\right|$$
3. Confirm that the differential signal development $\Delta V$ attains $100\text{ mV}$ to $150\text{ mV}$ prior to sense amplifier latch strobe ($SAN \rightarrow \text{GND}$, $SAP \rightarrow V_{DD}$).
4. Verify off-state access transistor sub-threshold and junction leakage current remains below $1\text{ fA/cell}$ at $85^\circ\text{C}$.

---

## 5. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Acceptance Target Metric | Physical Unit | Verification Condition / Literature Context |
| :--- | :--- | :--- | :--- |
| **Cell Storage Capacitance ($C_s$)** | $\ge 28.0$ | $\text{fF}$ | Stacked capacitor over bitline (COB), high-$\kappa$ dielectric ($\kappa > 15$) |
| **Bitline Parasitic Capacitance ($C_{BL}$)** | $\le 250.0$ | $\text{fF}$ | Extracted array column parasitic capacitance on $360\text{ nm}$ bitline pitch |
| **Differential Signal Window ($\Delta V$)** | $100.0 \text{ to } 150.0$ | $\text{mV}$ | Signal developed across $BL$ and $\overline{BL}$ prior to sense amp latching |
| **Access Transistor Geometry** | $L = 180 \pm 0$, $W = 220 \pm 0$ | $\text{nm}$ | Physical gate dimensions ($L = 180\text{ nm}$, $W = 220\text{ nm}$) |
| **Cell Junction & Sub-threshold Leakage ($I_{\text{leak}}$)** | $\le 1.0$ | $\text{fA/cell}$ | Maximum allowable cell leakage measured at $T = 85^\circ\text{C}$ |

---

## 6. Citations & References
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
  - CMOS cross-coupled latch topology with bitline equalization to $V_{DD}/2$.
  - Charge dump relation: $Q_s = C_s \cdot (V_{\text{cell}} - V_{BL})$.
  - Differential signal development: $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{\text{cell}} - V_{DD}/2)$, yielding $100\text{ mV}$ to $150\text{ mV}$ for $C_s = 25\text{ fF}$ and $C_{BL} = 250\text{ fF}$.
  - Sensing strobe sequence: $SAN$ pulls to GND, $SAP$ pulls to $V_{DD}$, restoring full rail CMOS levels.
  - Bitline array pitch: $360\text{ nm}$ pitch-matched interleaved layout.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
  - Stacked capacitor over bitline (COB) with crown polysilicon / MIM structure and W-plug contact.
  - ONO / high-$\kappa$ dielectric stack with effective dielectric constant $\kappa > 15$.
  - Minimum capacitance budget: $28\text{ fF/cell}$ for soft-error immunity and coupling noise rejection.
  - Sub-threshold and junction leakage target: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

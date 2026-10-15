# Standard Operating Procedure (SOP): HIL Sub-Nanosecond Bitline Sensing Latency Metrology & Jitter Characterization

- **Date**: 2026-10-15
- **Author**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented / Active
- **Action Type**: Buy / Metrology & Instrumentation Integration

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) governs the physical acquisition, timing metrology, and jitter characterization of bitline signal development and sense amplifier latch activation latency on 180nm open-source DRAM arrays (folded bitline architecture, $8F^2$ footprint). Utilizing an FPGA Hardware-in-the-Loop (HIL) testbench with an integrated sub-nanosecond Time-to-Digital Converter (TDC) core, this procedure measures the real-time response from wordline assertion ($V_{PP}$) through differential voltage development ($\Delta V = 100\text{ mV to }150\text{ mV}$) down to sense amplifier latch activation (SAN/SAP assertion) and bitline rail saturation.

---

## 2. Theoretical & Literature Context
Based on verified DRAM Foundation literature:
- **1T1C Memory Cell & Topology**: 180nm unit cell ($W = 220\text{ nm}$, $L = 180\text{ nm}$) with stacked capacitor (crown/MIM structure with ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-k stack, $\kappa > 15$). Cell area is $8F^2 = 0.259\ \mu\text{m}^2$.
- **Capacitance Budgets**:
  - Cell storage node capacitance: $C_s = 25\text{ fF to }30\text{ fF}$ (nominally $28\text{ fF}$).
  - Bitline parasitic capacitance: $C_{BL} = 150\text{ fF to }250\text{ fF}$ (256/512 cells per bitline).
  - Capacitance ratio: $C_{BL} / C_s$ maintained strictly between $5:1$ and $9:1$ ($< 10:1$).
- **Precharge & Signal Development**:
  - Bitlines ($BL$ and $\overline{BL}$) precharged and equalized to $V_{DD} / 2$ prior to wordline assertion.
  - Charge sharing generates differential read signal margin:
    $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \left(V_{cell} - \frac{V_{DD}}{2}\right) \approx 100\text{ mV to }150\text{ mV}$$
- **Sensing Latch Operation**: Cross-coupled CMOS inverter latch pulls SAN to $V_{SS}$ and SAP to $V_{DD}$ upon sense amplifier enable assertion.

---

## 3. Workflow & Architecture Diagram

```text
┌────────────────────────┐
│                        │
│  Precharge BL and nBL  │
│       to VDD / 2       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Wordline Assertion   │
│        WL High         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Charge Sharing Delta  │
│   V: 100 mV - 150 mV   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Sense Amplifier     │
│    Latch Activation    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   FPGA TDC Timestamp   │
│   Logging and Jitter   │
│    Characterization    │
│                        │
└────────────────────────┘
```

---

## 4. Required Equipment & Fixturing (Buy / Integration Bill-of-Materials)
1. **FPGA HIL Metrology Core Board**: High-speed FPGA board featuring low-skew dedicated carry logic chains (carry-chain TDL TDC engine) with sub-nanosecond bin resolution ($\le 25\text{ ps}$ nominal bin width) and low-jitter LVDS/high-speed differential I/O.
2. **Active RF Micro-Coaxial / Picoprobe High-Z Fixture**: Low-capacitance active differential probe head ($C_{in} < 0.2\text{ fF}$ parasitic loading to avoid distorting the $150\text{ fF to }250\text{ fF}$ bitline capacitance) with matched $50\ \Omega$ RF micro-coaxial transmission lines.
3. **Ultra-Low Phase Noise Reference Clock Generator**: Master reference clock source providing reference frequency with RMS phase jitter $< 1\text{ ps}$ RMS.
4. **Precision Sub-Femtoamp Source Measure Unit (SMU)**: For verifying cell leakage ($< 1\text{ fA/cell}$ at $85^\circ\text{C}$) and static bias levels.

---

## 5. Step-by-Step Operating Procedure

### Step 1: Pre-Measurement Fixturing & Baseline Equalization
1. Dock the low-capacitance active micro-coaxial probe tips directly onto the micro-contact test pads for true bitline ($BL$) and complement bitline ($\overline{BL}$).
2. Power on the DRAM device under test (DUT) inside a temperature-controlled thermal chamber set to nominal room temperature ($25^\circ\text{C} \pm 1^\circ\text{C}$) or high-temperature retention condition ($85^\circ\text{C} \pm 1^\circ\text{C}$).
3. Assert the equalization control gate. Confirm that both $BL$ and $\overline{BL}$ settle to $V_{DD}/2$ within $\pm 5\text{ mV}$.

### Step 2: TDC Statistical Calibration & Non-Linearity Compensation
1. Prior to active DRAM access, run the on-chip statistical code density calibration engine on the FPGA TDL TDC core across $10^6$ asynchronous calibration clock hits.
2. Calculate delay bin non-uniformity and generate the look-up table (LUT) for Differential Non-Linearity (DNL) and Integral Non-Linearity (INL) correction.
3. Lock the TDC calibrated time-scale to ensure measurement bin accuracy.

### Step 3: Write Pattern & Storage Node Charge Initialization
1. Execute a deterministic write sequence across target memory array cells (256/512 cells per bitline).
2. Write alternating checkerboard data patterns (`0xAA` / `0x55`) to evaluate worst-case bitline-to-bitline capacitive coupling.
3. De-assert the wordline ($WL \to V_{SS}$) to isolate the storage node capacitor ($C_s \ge 25\text{ fF to }30\text{ fF}$).

### Step 4: Wordline Trigger Injection & Signal Development Metrology
1. Route the Wordline Driver activation trigger signal ($WL\_ENABLE$) synchronously to the TDC start trigger channel ($T_{start}$).
2. Pulse the wordline driver to assert $WL$ to boosted level ($V_{PP}$).
3. Access transistor opens ($W = 220\text{ nm}$, $L = 180\text{ nm}$), dumping charge $Q_s = C_s (V_{cell} - V_{BL})$ onto the bitline.
4. Monitor differential signal development $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{cell} - V_{DD}/2)$. Measure the time window required to achieve $\Delta V = 100\text{ mV to }150\text{ mV}$.

### Step 5: Sense Amplifier Latch Triggering & Latency Metrology
1. Assert sense amplifier enable signals ($SAN$ to $V_{SS}$ via NMOS pull-down, $SAP$ to $V_{DD}$ via PMOS pull-up).
2. Connect the differential bitline threshold crossing comparator ($V_{diff} \ge 90\% \cdot V_{DD}$) to the TDC stop trigger channel ($T_{stop}$).
3. The FPGA TDC captures the time interval:
   $$t_{SENSE} = T_{stop} - T_{start}$$
   representing total sensing latency from wordline assertion to bitline rail saturation.

### Step 6: Jitter Characterization & Statistical Distribution Run
1. Repeat the readout cycle across $N = 100,000$ consecutive continuous acquisitions across PVT corners (Nominal, Slow-Slow, Fast-Fast).
2. Stream raw timestamp data packets into the HIL host analyzer.
3. Compute the timing histogram, extracting:
   - Mean sensing latency $\mu(t_{SENSE})$
   - Standard deviation / Random Jitter: $\sigma_{RJ}$
   - Peak-to-peak Total Jitter ($TJ = DJ + 14.069 \cdot RJ$ at $\text{BER} = 10^{-12}$)

---

## 6. Acceptance Criteria & Target Metrics

| Metric Index | Parameter Description | Acceptance Target / Tolerance | Unit | Verification Method |
| :---: | :--- | :--- | :---: | :--- |
| **AC-1** | **Bitline Differential Signal Development ($\Delta V$)** | $100.0\text{ to }150.0$ (for $C_s = 25\text{ to }30\text{ fF}$, $C_{BL} = 150\text{ to }250\text{ fF}$) | $\text{mV}$ | High-Z active probe differential voltage capture |
| **AC-2** | **TDC Timing Resolution (Least Significant Bit Bin Width)** | $\le 25.0$ | $\text{ps}$ | On-chip code density calibration engine |
| **AC-3** | **Mean Bitline Sensing Latency ($\mu(t_{SENSE})$)** | $\le 3.50$ (at $25^\circ\text{C}$, $V_{DD}$ nominal) | $\text{ns}$ | FPGA HIL TDC timestamp distribution ($N = 100,000$) |
| **AC-4** | **Bitline Sensing Latency Random Jitter ($\sigma_{RJ}$)** | $\le 45.0$ | $\text{ps RMS}$ | Gaussian fit of TDC sensing latency histogram |

---

## 7. References & Cited Context
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**: Differential sensing of cell charge $Q_s = C_s(V_{cell} - V_{BL})$; precharge to $V_{DD}/2$; differential voltage $\Delta V = (C_s / (C_{BL} + C_s))(V_{cell} - V_{DD}/2) \approx 100\text{ mV to }150\text{ mV}$ for $C_s = 25\text{ fF}$ and $C_{BL} = 250\text{ fF}$; cross-coupled CMOS inverter latch with $SAN$ and $SAP$.
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**: 1T1C cell architecture ($8F^2 = 0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$); storage node capacitance budget $C_s \ge 25\text{ fF to }30\text{ fF}$ (nominally $28\text{ fF}$); bitline parasitic capacitance $C_b = 150\text{ fF to }250\text{ fF}$ (256/512 cells); capacitance ratio $C_b / C_s$ strictly between $5:1$ and $9:1$ ($< 10:1$).
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Transistor dimensions $L = 180\text{ nm}$, $W = 220\text{ nm}$; crown/MIM stacked capacitor with ONO / high-k dielectric ($\kappa > 15$); leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- Related files:
  - [sop_tdl_tdc_synthesis.md](./docs/sop_tdl_tdc_synthesis.md)
  - [context.yaml](./docs/context.yaml)
  - [context2.yaml](./docs/context2.yaml)
  - [context3.yaml](./docs/context3.yaml)

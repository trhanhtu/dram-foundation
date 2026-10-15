# SOP: TDR Discontinuity Extraction & Eye-Diagram Signal Integrity Verification

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council)
- **Status**: Accepted
- **Generation**: Gen 3 (nm) / 180nm CMOS Commercial MPW Tapeout & PDK Implementation
- **Hierarchy Path**: `Context: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm CMOS Commercial MPW Tapeout & PDK Implementation [Foundry Tapeout & PDK] > BEOL Multi-Layer Metallization, Wafer Sort & Packaging [BEOL & Packaging] > Final Automated Test Equipment (ATE) JEDEC DDR Speed-Bin & HTOL Burn-in Testing [Reliability & Qualification] > ATE Loadboard Interface Design & JEDEC Timing Vector Pattern Generation [Circuit Design] > ATE DUT Loadboard PCB Schematic & High-Speed Impedance-Matched Layout [Circuit Design] > TDR Transmission Line Metrology & S-Parameter Signal Integrity Verification [Metrology] > TDR Discontinuity Extraction & Eye-Diagram Signal Integrity Verification [Circuit Design]`
- **Action Type**: Make

---

## 1. Overview & Rationale

In high-speed JEDEC DDR testing of the 180nm Open-Source DRAM chip, accurate signal integrity characterization on the ATE DUT loadboard interface is paramount. High-speed timing signals (differential clocks `CK`/`#CK`, data strobes `DQS`/`#DQS`, and high-speed data `DQ[15:0]`) traverse SMA/SMP launch connectors, controlled-impedance microstrip transmission lines ($Z_0 = 50.0\,\Omega$), DUT pogo-pin/socket interfaces, and package bond wires before interfacing with the on-chip DRAM I/O buffers.

Impedance mismatches and localized reactive discontinuities ($\Delta Z$, parasitic inductance $L_{\text{via}}$, and parasitic capacitance $C_{\text{pad}}$) induce reflections, signal ringing, edge degradation, and deterministic jitter. When driving fast rise-time transients through the on-chip pass transistors ($W/L = 2.0\,\mu\text{m}/0.18\,\mu\text{m}$, $V_{\text{thn}} = +0.55\text{ V} \pm 50\text{ mV}$) and cell bitline array structures ($C_s \ge 28\text{ fF}$, access transistor channel $L = 180\text{ nm}$, $W = 220\text{ nm}$), transmission line degradation erodes timing margins and shrinks the DDR data eye.

This Standard Operating Procedure (SOP) defines the physical methodology to:
1. Extract localized reactive discontinuities ($L_{\text{disc}}$, $C_{\text{disc}}$) and impedance profiles $Z(t)$ along the ATE loadboard-to-DUT signal channels via Time-Domain Reflectometry (TDR).
2. Measure eye-diagram opening (eye height $V_{\text{eye}}$, eye width $t_{\text{eye}}$) and decompose jitter into Total Jitter ($TJ$), Deterministic Jitter ($DJ$), and Random Jitter ($RJ$) under simulated and physical JEDEC DDR PRBS timing patterns.

---

## 2. Metrology & Simulation Workflow Architecture

```text
┌──────────────────────────────────────────────┐
│                                              │
│         Instrument Setup & Calibration       │
│      (TDR / Sampling Scope / SOLT Cal)       │
│                                              │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                                              │
│       TDR Step-Response Measurement          │
│       (t_rise = 20-35 ps, Z(t) Profile)      │
│                                              │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                                              │
│      Reactive Discontinuity Extraction       │
│       (Excess C_pad & L_via Integration)     │
│                                              │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                                              │
│       JEDEC DDR PRBS Pattern Injection       │
│      (Pseudo-Random Pattern, 1.8V Swing)     │
│                                              │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                                              │
│        Eye-Diagram & Jitter Metrology        │
│     (Eye Height, Eye Width, Dual-Dirac TJ)   │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Procedure

### Step 3.1: Instrument Setup, De-embedding & Baseline Calibration
1. Power on the sampling oscilloscope / TDR metrology unit (bandwidth $\ge 20\text{ GHz}$) and let temperature stabilize for at least 30 minutes in a temperature-controlled environment ($23^\circ\text{C} \pm 1^\circ\text{C}$).
2. Perform SOLT (Short-Open-Load-Thru) 2-port coaxial calibration at the instrument reference plane using a precision $3.5\text{ mm} / 2.92\text{ mm}$ calibration standard kit ($50.0\,\Omega \pm 0.1\,\Omega$).
3. Apply Automatic Fixture Removal (AFR) or 2x-Thru de-embedding file to mathematically eliminate coaxial test lead and launch cable phase delays, placing the measurement reference plane directly at the ATE DUT loadboard launch connector interface.

### Step 3.2: TDR Incident Step Configuration & Spatial Impedance Profiling
1. Configure the internal step generator to inject a fast-edge step pulse:
   - Incident step amplitude: $V_{\text{step}} = 200\text{ mV}$ to $400\text{ mV}$.
   - System filtered 10%–90% rise time: $t_r = 30\text{ ps} \pm 2\text{ ps}$ (equivalent to sub-0.18 µm high-speed I/O slew rates).
2. Measure the reflected waveform $V_{\text{refl}}(t)$ and compute the spatial reflection coefficient $\Gamma(t)$:
   $$\Gamma(t) = \frac{V_{\text{refl}}(t) - V_{\text{incident}}}{V_{\text{incident}}}$$
3. Convert $\Gamma(t)$ to the time-domain impedance profile $Z(t)$:
   $$Z(t) = Z_0 \cdot \frac{1 + \Gamma(t)}{1 - \Gamma(t)} \quad (Z_0 = 50.0\,\Omega)$$
4. Identify spatial discontinuity zones along the channel:
   - Zone 1: Launch connector (SMA/SMP) transition ($t_1 \approx 0\text{ to } 150\text{ ps}$).
   - Zone 2: Microstrip transmission line route ($Z_0 = 50.0\,\Omega$, $t_2 \approx 150\text{ to } 900\text{ ps}$).
   - Zone 3: ATE pogo-pin / socket pad transition ($t_3 \approx 900\text{ to } 1050\text{ ps}$).
   - Zone 4: Package bond wire and silicon on-chip DRAM I/O pad ($t_4 > 1050\text{ ps}$).

### Step 3.3: Quantitative Extraction of Reactive Discontinuities ($\Delta Z$, $C$, $L$)
1. Extract the characteristic impedance deviation along the uniform microstrip routing:
   $$\Delta Z = |Z_{\text{measured}} - 50.0\,\Omega|$$
2. Compute the excess shunt capacitance $C_{\text{pad}}$ at capacitive dips ($Z(t) < 50\,\Omega$) by numerical integration of the reflection coefficient $\Gamma(t)$:
   $$C_{\text{pad}} = -\frac{1}{2 Z_0} \int_{t_{\text{start}}}^{t_{\text{end}}} \Gamma(t)\,dt$$
3. Compute the excess series loop inductance $L_{\text{via}}$ at inductive peaks ($Z(t) > 50\,\Omega$) by numerical integration:
   $$L_{\text{via}} = \frac{Z_0}{2} \int_{t_{\text{start}}}^{t_{\text{end}}} \Gamma(t)\,dt$$
4. Verify that total parasitic lumped capacitance at the DUT I/O node does not exceed the budget allocated for 180nm access pass transistors and bitline sensing nodes.

### Step 3.4: JEDEC DDR Speed-Bin Pattern Excitation & Signal Eye Acquisition
1. Connect the ATE Pattern Generator / Pulse Generator configured for JEDEC DDR signaling at nominal supply $V_{DD} = 1.8\text{ V}$.
2. Program a continuous PRBS-7 / PRBS-15 pseudo-random binary sequence at target test clock/data rates (100 MHz to 200 MHz JEDEC DDR operation, 200 Mbps to 400 Mbps per pin).
3. Connect a high-bandwidth differential active probe ($C_{\text{probe}} < 0.2\text{ pF}$, bandwidth $\ge 13\text{ GHz}$) directly to the DUT test points adjacent to the DRAM package pins.
4. Set real-time sampling oscilloscope trigger to recovered clock using a JEDEC-compliant Phase-Locked Loop (PLL) software clock recovery circuit (Golden PLL loop bandwidth = data rate / 1667).
5. Accumulate persistent eye-diagram statistics over a minimum of $10^6$ continuous UI (unit intervals).

### Step 3.5: Eye Mask Validation & Dual-Dirac Jitter Decomposition
1. Measure central horizontal eye opening (Eye Width $t_{\text{eye}}$) at the reference zero-crossing threshold ($V_{\text{ref}} = V_{DD}/2 = 0.90\text{ V}$).
2. Measure central vertical eye opening (Eye Height $V_{\text{eye}}$) at $0.5\text{ UI}$ center sampling point.
3. Perform Dual-Dirac jitter decomposition to isolate:
   - Random Jitter ($RJ_{\text{rms}}$) extracted from Gaussian tail fitting.
   - Deterministic Jitter ($DJ_{\delta-\delta}$) from peak-to-peak tail separation.
   - Total Jitter ($TJ$) calculated at a Bit Error Rate target of $\text{BER} = 10^{-12}$:
     $$TJ = DJ_{\delta-\delta} + 14.069 \cdot RJ_{\text{rms}}$$
4. Overlay the standard JEDEC DDR compliance keep-out diamond mask onto the accumulated eye diagram to verify zero mask violation hits.

---

## 4. Machine-Measurable Acceptance Criteria Target Metrics

| Parameter / Metric | Evaluation Method | Target Value | Tolerance / Limit | Physical Units |
| :--- | :--- | :--- | :--- | :--- |
| **Microstrip Line Impedance ($Z_0$)** | TDR reflection step response ($t_r = 30\text{ ps}$) | $50.0$ | $\pm 2.5$ ($47.5 \text{ to } 52.5$) | $\Omega$ |
| **Excess Pad Shunt Capacitance ($C_{\text{pad}}$)** | TDR capacitive dip integral ($\Delta \Gamma(t)$) | $\le 0.45$ | Max $0.50$ | $\text{pF}$ |
| **Excess Via/Pin Loop Inductance ($L_{\text{via}}$)** | TDR inductive peak integral ($\Delta \Gamma(t)$) | $\le 0.85$ | Max $1.10$ | $\text{nH}$ |
| **Eye Height Opening ($V_{\text{eye}}$)** | Real-time scope eye diagram @ $1.8\text{ V}$ swing | $\ge 1.35$ | Min $1.25$ | $\text{V}$ |
| **Eye Width Opening ($t_{\text{eye}}$)** | Real-time scope eye diagram @ $V_{\text{ref}} = 0.90\text{ V}$ | $\ge 0.70$ | Min $0.65$ | $\text{UI}$ |
| **Total Jitter ($TJ @ \text{BER} = 10^{-12}$)** | Dual-Dirac histogram tail fitting | $\le 0.25$ | Max $0.30$ | $\text{UI}$ |

---

## 5. Verified Local Literature Citations

1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - Access transistor channel dimensions ($L = 180\text{ nm}$, $W = 220\text{ nm}$).
   - Stacked capacitor budget ($C_s \ge 28\text{ fF}$) defining the noise immunity threshold and sensitivity to interconnect reflections and bitline coupling noise.
2. **Stage 3 Reality Gate: Discrete Long-Channel MOSFET & CMOS Inverter Verification**
   - Sub-micron NMOS/PMOS device parameters ($W/L = 2.0\,\mu\text{m} / 0.18\,\mu\text{m}$, NMOS $V_{\text{thn}} = +0.55\text{ V} \pm 50\text{ mV}$, PMOS $V_{\text{thp}} = -0.60\text{ V} \pm 50\text{ mV}$).
   - Operating supply voltage $V_{DD} = 1.8\text{ V}$ ($V_{DS} = 1.8\text{ V}$) used as the benchmark signal swing and I/O buffer driver level.
3. **High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture**
   - Threshold voltage loss mechanism ($V_{DD} - V_{\text{th}} = 1.8\text{ V} - 0.6\text{ V} = 1.2\text{ V}$), underscoring the necessity of stringent edge integrity, minimum ringing, and overdrive stability across the ATE interface.

---

## 6. References & Related Files

- [sop_tdr_calibration_fixture_deembedding.md](./docs/sop_tdr_calibration_fixture_deembedding.md)
- [sop_oscilloscope_eye_diagram_jitter_metrology.md](./docs/sop_oscilloscope_eye_diagram_jitter_metrology.md)
- [sop_prbs_transient_bitline_bus_coupling.md](./docs/sop_prbs_transient_bitline_bus_coupling.md)
- [docs/context.yaml](./docs/context.yaml)

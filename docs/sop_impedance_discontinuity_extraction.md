# Standard Operating Procedure (SOP): Impedance Discontinuity Extraction & Parasitic LC Modeling

- **Date**: 2026-10-15
- **Branch**: DRAM Foundation VN > 180nm Open-Source DRAM Chip > Signal Integrity & Level Shifter Daughtercard PCB
- **Level**: Leaf SOP [Metrology / Signal Integrity]
- **Document ID**: `SOP-MET-DRAM180-TDR-001`
- **Target Topology**: 50 $\Omega$ Controlled-Impedance Microstrips, SMA/Probe Launch Transitions, Level-Shifter Interface Pads

---

## 1. Overview & Scope

This Standard Operating Procedure outlines the quantitative methodology for extracting spatial characteristic impedance profiles ($Z_0(x)$), isolating lumped impedance discontinuities (vias, pads, bond wires, and connector launches), and synthesizing equivalent lumped-element parasitic $\Pi$- or T-ladder models ($L_{\text{excess}}$, $C_{\text{excess}}$). 

Maintaining tight microstrip impedance matching ($50\ \Omega \pm 10\%$) is critical for high-speed read/write DRAM command and bitline routing interfaces between the ESP32 closed-loop controller and the 180nm test die, preventing signal reflections and distortion during differential sense-amplifier timing validation.

---

## 2. Engineering Workflow Architecture

The execution follows a strict reflection-coefficient ($\rho(t)$) time-domain reflectometry pipeline:

```text
┌────────────────────────┐
│                        │
│  Launch Step Pulse tr  │
│        <= 35ps         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      Acquire TDR       │
│  Reflection Waveform   │
│         rho t          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Locate Microstrip    │
│  Discontinuity Region  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────◇───────────┐
│                        │
│    Excess Reactance    │
│         Type?          │
│                        │
└────────────◇───────────┘
             │
             │
             ├────────────────────────────────────────────────╮Inductive Peak rho > 0
             │Capacitive Dip rho < 0                          │
             ▼                                                ▼
┌────────────────────────┐                       ┌────────────────────────┐
│                        │                       │                        │
│  Integrate Delta rho:  │                       │  Integrate Delta rho:  │
│  C_excess = -1/(2*Z0)  │                       │  L_excess = Z0/2 int   │
│    int Delta rho dt    │                       │      Delta rho dt      │
│                        │                       │                        │
└───────────┬────────────┘                       └────────────┬───────────┘
            │                                                 │
            │ ╭───────────────────────────────────────────────╯
            ▼ ▼
┌────────────────────────┐
│                        │
│  Extract Parasitic Pi  │
│  / Tee LC Equivalent   │
│        Circuit         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Synthesize SPICE    │
│      Subcircuit &      │
│   Correlate with TDR   │
│          S11           │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Instrument Setup & Calibration (OSLT / SOLT Standard)
1. Initialize the Time-Domain Reflectometer / High-Bandwidth Sampling Oscilloscope (e.g., Keysight DCA / Tektronix DSA8300) with a step generator rise time $t_r \le 35\ \text{ps}$ (10% to 90%).
2. Perform full 1-port Open-Short-Load (OSLT) calibration at the precision coaxial reference plane ($3.5\ \text{mm}$ or precision RF microprobe tip) using a certified $50.0\ \Omega$ termination standard.
3. Configure the sampling time window to capture the entire physical trace length plus terminal reflections ($T_{\text{window}} \ge 2 \times \tau_{\text{prop}} + 5\ \text{ns}$, sampling interval $\Delta t \le 1.0\ \text{ps}$).

### Step 2: Microstrip Characteristic Impedance ($Z_0$) Profiling
1. Probe the dedicated $50\ \Omega$ microstrip test coupon on the Level Shifter Daughtercard PCB.
2. Record the reflected step response $V_{\text{refl}}(t)$ and compute the reflection coefficient profile:
   $$\rho(t) = \frac{V_{\text{refl}}(t) - V_{\text{incident}}}{V_{\text{incident}}}$$
3. Convert $\rho(t)$ to instantaneous characteristic impedance $Z(t)$:
   $$Z(t) = Z_{\text{ref}} \cdot \frac{1 + \rho(t)}{1 - \rho(t)}, \quad \text{where } Z_{\text{ref}} = 50.0\ \Omega$$
4. Map propagation delay $t$ to spatial distance $x = \frac{c \cdot t}{2 \sqrt{\varepsilon_{\text{eff}}}}$. Confirm continuous uniform microstrip impedance lies within $50.0\ \Omega \pm 2.5\ \Omega$ ($5\%$).

### Step 3: Discontinuity Windowing & Excess Reactance Extraction
1. Gate the waveform boundaries $[t_1, t_2]$ strictly encompassing the local impedance anomaly (e.g., transition pad, test fixture via, or level-shifter interface bond-pad).
2. Establish baseline reference impedance $Z_0$ immediately preceding the anomaly.
3. **Capacitive Discontinuity (Negative Reflection Dip, $\Delta \rho(t) < 0$):**
   Extract lumped excess capacitance $C_{\text{excess}}$ by numerical time integration:
   $$C_{\text{excess}} = -\frac{1}{2 Z_0} \int_{t_1}^{t_2} \Delta \rho(t) \, dt = -\frac{1}{2 Z_0} \int_{t_1}^{t_2} \left( \frac{Z(t) - Z_0}{Z(t) + Z_0} \right) dt$$
4. **Inductive Discontinuity (Positive Reflection Spike, $\Delta \rho(t) > 0$):**
   Extract lumped excess inductance $L_{\text{excess}}$ by numerical time integration:
   $$L_{\text{excess}} = \frac{Z_0}{2} \int_{t_1}^{t_2} \Delta \rho(t) \, dt = \frac{Z_0}{2} \int_{t_1}^{t_2} \left( \frac{Z(t) - Z_0}{Z(t) + Z_0} \right) dt$$

### Step 4: Equivalent Circuit Synthesis & Simulation Correlation
1. Construct the lumped $\Pi$-network (for shunt-dominant pads: $C_{\text{pad1}} - L_{\text{via}} - C_{\text{pad2}}$) or T-network (for series-dominant pin headers: $L_{\text{lead1}} - C_{\text{pad}} - L_{\text{lead2}}$).
2. Export the extracted parameters into a SPICE subcircuit block representing the daughtercard interface.
3. Simulate transient step response across the identical synthetic pulse ($t_r = 35\ \text{ps}$) and overlay against measured raw TDR waveforms. Residual root-mean-square error (RMSE) must satisfy $\text{RMSE} < 3\%$.

---

## 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Acceptance Band | Physical Units | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Microstrip Line $Z_0$** | $50.0$ | $47.5 - 52.5$ ($\pm 5.0\%$) | $\Omega$ | TDR Profile flat-zone averaging |
| **Max Discontinuity Peak $|\Delta Z|$** | $\le 5.0$ | $< 5.0$ | $\Omega$ | TDR peak/valley deviation from $Z_0$ |
| **Interface Pad Excess Capacitance ($C_{\text{pad}}$)** | $\le 0.45$ | $0.10 - 0.45$ | $\text{pF}$ | Gated $\Delta \rho$ time integration |
| **Signal Via Excess Inductance ($L_{\text{via}}$)** | $\le 0.60$ | $0.20 - 0.60$ | $\text{nH}$ | Gated $\Delta \rho$ time integration |
| **SPICE Model Correlation (TDR Overlay)** | $\le 3.0$ | $< 3.0$ | $\%$ | Waveform RMS Residual Error |

```text
                       ┌───────────────────────────────┐
                       │░                              │
    Bitline C_b (Array)┤░                              │
                       │▒                              │
        Parasitic C_pad┤▒                              │
Discontinuity Tolerance┤▓▓▓▓                           │
                       │▓▓▓▓                           │
             Nominal Z0┤███████████████████████████████│
                       │███████████████████████████████│
                       └┬───────┬──────┬───────┬──────┬┘
                       0.0    12.5   25.0    37.5  50.0 
```

---

## 5. Context Literature Citations

1. **Source: 1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Parasitic capacitance budgeting principles dictating bitline line capacitance ($C_b \approx 150 - 250\ \text{fF}$ across 256/512 cell blocks) and nominal storage cell node capacitance ($C_s \ge 25 - 30\ \text{fF}$, nominally $28\ \text{fF}$), requiring external fixture parasitic capacitance ($C_{\text{pad}}$) to remain tightly modeled and bounded to prevent excessive capacitive loading during array readout characterization.
2. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry ($L = 180\ \text{nm}$, $W = 220\ \text{nm}$) and stacked capacitor over bitline (COB) architecture.
3. **Source: Transmission Line Measurement (TLM) for Specific Contact Resistivity**:
   - Extraction of series interconnect and pad parasitics utilizing standardized transmission line measurement mathematics.

# SOP: Controlled Impedance TDR Coupon Design & Signal Integrity Tolerance Verification

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN Council)
- **Status**: Accepted
- **Task Hierarchy**: `180nm Open-Source DRAM Chip (DRAM Foundation VN)` > `ESP32 Closed-Loop Motor Controller` > `Signal Integrity & Level Shifter Daughtercard PCB (50-Ohm Controlled Impedance Microstrips)` > `50-Ohm Controlled Impedance Stackup Design & Level Shifter Schematic Synthesis` > `4-Layer PCB Stackup Definition & 50-Ohm Microstrip Field Solver Modeling` > `Controlled Impedance TDR Coupon Design & Signal Integrity Tolerance Verification`

---

## 1. Overview & Purpose
This Standard Operating Procedure (SOP) defines the physical design rules, fabrication requirements, and metrological characterization for Time-Domain Reflectometry (TDR) test coupons embedded on the production panel break-away rails of the Level Shifter Daughtercard PCB. It guarantees the physical compliance of $50\,\Omega \pm 10\%$ single-ended microstrips interfacing the ESP32 closed-loop controller, level shifters, and 180nm DRAM test fixture.

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│   Coupon Edge Launch   │
│      SMA / Probe       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Lead-in Segment min   │
│          25mm          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Uniform 50-Ohm Trace  │
│     100mm to 150mm     │
│                        │
└────────────┬───────────┘
             │
             ├─────────────────────────────╮
             ▼                             ▼
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
│  Far-End Termination   │    │  TDR Fast Step Pulse   │
│         / Open         │    │       Injection        │
│                        │    │                        │
└────────────────────────┘    └────────────┬───────────┘
                                           │
             ╭─────────────────────────────╯
             ▼
┌────────────────────────┐
│                        │
│       Z0 Profile       │
│   Extraction 50 Ohm    │
│       +/- 10pct        │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step SOP Procedure

### Step 1: Panel Break-Away Coupon Physical Placement
1. Embed standard impedance test coupons along the outer perimeter (break-away tooling rails) of the 4-layer panelization frame.
2. Maintain identical layer assignment to Layer 1 (Top Signal) over Layer 2 (Solid Ground Plane Reference) replicating daughtercard microstrip stackup.
3. Keep coupon clearance $\ge 2.5\,\text{mm}$ away from V-score or mouse-bite perforation lines to avoid edge delamination or copper deformation during breakout.

### Step 2: Test Coupon Geometric Layout
1. **Trace Width ($W$) & Height ($H$):** Lay out microstrip test trace matching the 4-layer field solver synthesis ($Z_0 = 50\,\Omega$).
2. **Coupon Trace Length ($L$):** Implement a total uninterrupted coupon trace length of $100.0\,\text{mm}$ to $150.0\,\text{mm}$ (nominal $120.0\,\text{mm}$).
3. **Launch Lead-in Section:** Provide a lead-in segment of $\ge 25.0\,\text{mm}$ from the coaxial edge launcher (end-launch SMA or standard $100\,\text{mil} / 2.54\,\text{mm}$ pitch differential/ground-signal-ground micro-probe footprint) to separate launcher parasitic capacitance from the measurement window.
4. **Reference Ground Stitching:** Ensure unbroken Layer 2 GND copper under the entire coupon length. Place GND stitching vias adjacent to the probe pads with pitch $\le 1.0\,\text{mm}$.

### Step 3: TDR Calibration & System Normalization
1. Power on the sampling oscilloscope with integrated TDR differential/single-ended step generator. Allow thermal equilibration for at least 30 minutes.
2. Set incident step risetime $T_r \le 35\,\text{ps}$ (or filter to target system edge rate: $t_{r,\text{filter}} = 100\,\text{ps}$ to $200\,\text{ps}$).
3. Execute standard calibration protocol:
   - Connect calibration standards: Precision Open, Short, and $50.0\,\Omega$ Load to the launch cable end.
   - Establish reference plane at the probe/SMA launch connector interface.

### Step 4: Time-Domain Reflectometry Acquisition & Gating
1. Connect TDR head via low-loss semi-rigid coaxial test leads to the panel coupon test point.
2. Inject step voltage waveform ($V_{\text{inc}} \approx 200\,\text{mV}$ to $400\,\text{mV}$) into the microstrip trace.
3. Configure the oscilloscope measurement time gate:
   - Exclude the first $25.0\,\text{mm}$ equivalent time ($\approx 350\,\text{ps}$) corresponding to launch connector discontinuity.
   - Set the measurement evaluation window across the central $50\%$ to $80\%$ of the coupon trace (from $30.0\,\text{mm}$ to $100.0\,\text{mm}$).
4. Record reflection coefficient $\rho(t)$ and calculate continuous impedance profile:
   $$Z_0(t) = Z_{\text{ref}} \cdot \frac{1 + \rho(t)}{1 - \rho(t)}$$
   where $Z_{\text{ref}} = 50.0\,\Omega$.

---

## 4. Acceptance Criteria & Target Metrics

```text
                       TDR & DRAM Cell Key Metrics      
                ┌──────────────────────────────────────┐
                │█                                     │
     VPP Min (V)┤█                                     │
                │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 BL Cap Max (fF)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
Z0 Max Tol (Ohm)┤▓▓▓▓▓▓▓▓▓                             │
                │▓▓▓▓▓▓▓▓▓                             │
Z0 Min Tol (Ohm)┤▒▒▒▒▒▒▒▒                              │
                │▒▒▒▒▒▒▒▒                              │
    Z0 Nom (Ohm)┤████████                              │
                │████████                              │
                └┬────────┬─────────┬────────┬────────┬┘
                0.0     62.5      125.0    187.5  250.0 
```

| Metric / Parameter | Nominal Specification | Acceptance Range | Engineering Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Characteristic Impedance ($Z_0$)** | $50.0$ | $45.0 \text{ to } 55.0\ (\pm 10\%)$ | $\Omega$ | TDR Gated Profile ($30\text{--}100\,\text{mm}$) |
| **Propagation Velocity / Delay ($T_{pd}$)** | $6.8$ | $6.5 \text{ to } 7.2$ | $\text{ps/mm}$ | TDR Time Delay between physical markers |
| **Bitline Parasitic Capacitance ($C_b$)** | $150.0 \text{ to } 250.0$ | $\le 250.0$ | $\text{fF}$ | Integrated DRAM Macro Parameter Extraction |
| **DRAM VPP Charge Pump Voltage** | $2.5 \text{ to } 2.8$ | $\ge 2.5$ | $\text{V}$ | Oscilloscope / Voltmeter on test pad |

---

## 5. Literature Citations & Context Alignment
1. **[180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench]**:
   - Access transistor geometry ($L = 180\,\text{nm}$, $W = 220\,\text{nm}$), stacked capacitor $C_s \ge 28\,\text{fF}$, sub-threshold leakage $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$.
2. **[1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets]**:
   - 1T1C folded bitline ($8F^2 = 0.259\,\mu\text{m}^2$).
   - Storage capacitance $C_s \ge 25\,\text{fF} \text{ to } 30\,\text{fF}$ (nominal $28\,\text{fF}$).
   - Bitline parasitic capacitance $C_b = 150\,\text{fF} \text{ to } 250\,\text{fF}$ across 256/512 cell blocks; ratio $C_b / C_s$ maintained between $5:1$ and $9:1$.
3. **[High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture]**:
   - Enhancement NMOS pass gate $V_{th} \approx 0.5\,\text{V} \text{ to } 0.7\,\text{V}$.
   - Overdrive voltage $V_{PP} = V_{DD} + V_{th} + \Delta V_{\text{overdrive}} \ge 2.5\,\text{V} \text{ to } 2.8\,\text{V}$.
   - Dickson charge pump 4-stage topology, $C_{\text{pump}} = 20\,\text{pF} \text{ to } 50\,\text{pF}$, clocking at $20\,\text{MHz} \text{ to } 50\,\text{MHz}$.

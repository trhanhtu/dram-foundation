# SOP: High-Bandwidth Active Differential Probe & Oscilloscope Fixture Calibration

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Metrology Stack

---

## 1. Process Flowchart

```text
┌────────────────────────┐
│                        │
│    Start: Equipment    │
│        Warm-Up         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Probe Deskew &     │
│  Nulling Calibration   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Fixture De-embedding  │
│   & S-Parameter Load   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Differential Signal   │
│  Acquisition & Metric  │
│       Validation       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       Acceptance       │
│     Verification &     │
│        Sign-off        │
│                        │
└────────────────────────┘
```

---

## 2. Step-by-Step Calibration Procedure

### Step 1: Thermal Stabilization & Environmental Conditioning
1. Power on the high-bandwidth digital storage oscilloscope and active differential probe system.
2. Allow equipment to undergo thermal soak for 30 minutes in a temperature-controlled laboratory (23°C ± 2°C, 45% ± 5% RH).
3. Connect the active differential probe amplifier heads to the designated oscilloscope input channels set to 50 Ω DC termination.

### Step 2: DC Offset Nulling & Sensitivity Calibration
1. Attach the probe tip inputs (Positive `+` and Negative `-`) to the zero-volt reference calibration ground plane on the calibration fixture.
2. Execute the automated probe internal auto-zero routine on the oscilloscope to cancel DC amplifier drift and Vos offset.
3. Apply a precision DC reference voltage corresponding to the DRAM half-rail level $V_{DD}/2$ and verify differential voltage zero tracking.

### Step 3: Deskew & High-Frequency Step Response Equalization
1. Connect the differential probe tips to the fast-edge calibration fixture output (rise time $t_r \le 20\text{ ps}$).
2. Align probe channels and execute channel-to-channel deskew until timing skew differential $|\Delta t| \le 10\text{ ps}$.
3. Tune probe AC attenuation and compensation trimmer / DSP filter profile to eliminate overshoot and ring on fast pulse edges.

### Step 4: Test Fixture Characterization & De-embedding
1. Connect the 50 Ω controlled-impedance microstrip calibration standards (2x Thru, Open, Short) on the daughtercard fixture.
2. Acquire fixture S-parameters ($S_{11}$, $S_{21}$, $S_{22}$) across the frequency band.
3. Load the 2-port Touchstone de-embedding file into the oscilloscope math engine to mathematically shift the measurement reference plane directly to the DRAM sense amplifier bitline test pads (BL and /BL).

### Step 5: Differential Sensitivity Validation for DRAM Cell Signal Level
1. Configure dynamic test injection matching typical folded bitline charge dump characteristics ($C_s = 25\text{ fF}$ to $30\text{ fF}$, nominally $28\text{ fF}$, bitline parasitic $C_b = 150\text{ fF}$ to $250\text{ fF}$).
2. Verify measurement accuracy across the expected differential readout amplitude $\Delta V = 100\text{ mV}$ to $150\text{ mV}$.
3. Verify that probe loading capacitance $C_{probe} \ll C_b$ ensures negligible disturbance to the bitline capacitance budget.

---

## 3. Acceptance Criteria Target Metrics

```text
                        Acceptance Threshold Metrics    
                     ┌─────────────────────────────────┐
                     │░░░░░░░░░░░░░░░                  │
      C_b/C_s Rat Max┤░░░░░░░░░░░░░░░                  │
                     │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Fixt Return Loss (dB)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
    Diff V Error (mV)┤▓▓▓▓▓▓▓▓▓                        │
                     │▓▓▓▓▓▓▓▓▓                        │
 Deskew Residual (ps)┤█████████████████                │
                     │█████████████████                │
                     └┬───────┬───────┬───────┬───────┬┘
                      0       5      10      15      20 
```

| Parameter / Metric | Target Value | Physical Unit | Measurement Method / Verification Tool |
| :--- | :--- | :--- | :--- |
| **Residual Channel Deskew Skew** | $\le 10$ | ps | Fast-edge pulse generator & Oscilloscope Deskew Math |
| **Differential Voltage Measurement Error** | $\le 5$ | mV | DC / AC Precision Calibrator over $100\text{ mV} - 150\text{ mV}$ $\Delta V$ scale |
| **Fixture S-Parameter Return Loss ($S_{11}$)** | $\ge 20$ | dB | Vector Network Analyzer / TDR Metrology on 50 Ω Microstrip |
| **Bitline Capacitance Ratio Target ($C_b / C_s$)** | $5:1\text{ to }9:1$ (Max $10:1$) | Dimensionless ratio | TDR / S-parameter derived capacitive extraction |

---

## 4. Literature & Context Citations

1. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
   - Differential readout development: $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot (V_{cell} - V_{DD}/2)$.
   - Signal margin: Nominal $\Delta V$ spans $100\text{ mV}$ to $150\text{ mV}$ for $C_s = 25\text{ fF}$ and $C_{BL} = 250\text{ fF}$.
   - Precharge and equalization: Bitlines equalized to $V_{DD}/2$ prior to wordline assertion.

2. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Cell storage node capacitance: $C_s \ge 25\text{ fF}$ to $30\text{ fF}$ (nominally $28\text{ fF}$).
   - Bitline capacitance: $C_b$ spans $150\text{ fF}$ to $250\text{ fF}$ for 256/512 cells per bitline.
   - Capacitance budget ratio: $C_b / C_s$ maintained between $5:1$ and $9:1$; degradation threshold at $> 10:1$.
   - Geometry: Folded bitline $8F^2$ footprint ($0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$).

3. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Technology generation: $180\text{ nm}$ access transistor ($L = 180\text{ nm}$, $W = 220\text{ nm}$).
   - Stacked capacitor over bitline (COB) architecture with crown polysilicon / MIM structure.
   - Dielectric: ONO triple dielectric or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-k stack ($\kappa > 15$).
   - Storage target: Minimum $28\text{ fF}$ per cell with sub-threshold/junction leakage $< 1\text{ fA/cell}$ at 85°C.

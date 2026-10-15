# SOP: AFM Scan Parameter Optimization and Amplitude Setpoint Recipe Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Process Tier**: 180nm Open-Source DRAM Chip (Gen 3 nm) / SkyWater SKY130 Alignment
- **Task Hierarchy**: `180nm Open-Source DRAM Chip` > `CMP of ILD & W Plugs` > `Post-CMP Spectroscopic Ellipsometry & AFM Metrology` > `Tapping-Mode AFM Scan Recipe Setup and Post-CMP Wafer Surface Mapping` > `AFM Scan Parameter Optimization and Amplitude Setpoint Recipe Setup`

---

## 1. Overview & Rationale

Nanoscale surface roughness and polishing scratches post-ILD Chemical Mechanical Planarization (CMP) directly impact subsequent lithography depth of focus, dry gate oxide integrity ($T_{ox} = 3.5\text{ nm}$), and stacked capacitor bottom electrode contact landing. In tapping-mode (intermittent contact) Atomic Force Microscopy (AFM), improper cantilever drive amplitude or an unoptimized amplitude setpoint ratio ($r_{sp} = A_{sp} / A_0$) induces tip crashing, rapid tip blunting, or intermittent loss of surface tracking. 

This Standard Operating Procedure (SOP) defines the execution parameters for tuning cantilever resonance, establishing the free oscillation amplitude, locking the target amplitude setpoint ratio, and optimizing proportional-integral (PI) feedback gains across 49-point wafer map coordinates to achieve sub-Angstrom topographic tracking precision without scratching planarized dielectric surfaces.

---

## 2. Process Workflow Architecture

```text
┌───────────────────────┐
│                       │
│  Load Wafer & Align   │
│          Die          │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Cantilever Tuning &  │
│    Peak Selection     │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│     Engage Tip &      │
│  Amplitude Setpoint   │
│         Setup         │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   PID Feedback Gain   │
│     Optimization      │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Surface Mapping &   │
│       Metrology       │
│      Acquisition      │
│                       │
└───────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Wafer Loading and Coordinate Registration
1. Mount the cleaned post-CMP wafer onto the vacuum chuck of the automated tapping-mode AFM.
2. Initialize optical projection view and align wafer notch/flat to establish global coordinates.
3. Program coordinates according to an automated **49-point wafer mapping** layout across the radial extent of the wafer to capture center-to-edge CMP polish profiles.
4. Position the scan head over the initial metrology site (e.g., ILD oxide overlying $180\text{ nm}$ channel length access transistor active cell array).

### Step 2: Cantilever Resonance Auto-Tune and Free Amplitude Calibration
1. Align the four-quadrant optical deflection photodiode laser beam onto the reflective backside of the silicon cantilever tip. Center vertical and horizontal photodiode signals ($V_{A-B} \approx 0.0\text{ V}$, $V_{C-D} \approx 0.0\text{ V}$, Sum signal $> 4.0\text{ V}$).
2. Execute a frequency sweep across the $280\text{ kHz} - 350\text{ kHz}$ band to identify the fundamental flexural resonance frequency $f_0$.
3. Select an operating drive frequency shifted slightly below resonance peak:
   $$f_{drive} = f_0 - 0.5\text{ kHz}$$
   to ensure monotonic repulsive tapping regime operation.
4. Adjust piezo drive voltage until target **Free Oscillation Amplitude** $A_0 = 20.0\text{ nm}$ (rms voltage equivalent $\sim 1.0\text{ V}$ to $1.5\text{ V}$) is achieved in air.

### Step 3: Tip Engagement and Amplitude Setpoint ($A_{sp}$) Calibration
1. Set the initial amplitude setpoint ratio:
   $$r_{sp} = \frac{A_{sp}}{A_0} = 0.85$$
   (corresponding to $A_{sp} = 17.0\text{ nm}$ for $A_0 = 20.0\text{ nm}$) to avoid tip crash during automated z-approach.
2. Engage the Z-piezo motor until oscillation dampening triggers engagement lock.
3. Acquire an initial 10-line test profile across a $1.0\,\mu\text{m} \times 1.0\,\mu\text{m}$ area.
4. Fine-tune $r_{sp}$ incrementally between $0.70$ and $0.80$ ($A_{sp} = 14.0\text{ nm} - 16.0\text{ nm}$) to ensure stable repulsive intermittent contact while limiting tip indentation force to $< 5\text{ nN}$.

### Step 4: Scan Speed and Feedback Gain (P-I) Optimization
1. Set scan area to $1.0\,\mu\text{m} \times 1.0\,\mu\text{m}$ ($1000\text{ nm} \times 1000\text{ nm}$) to resolve features relative to $L = 180\text{ nm}$ and $W = 220\text{ nm}$ layout geometries. Set resolution to $512 \times 512$ data points.
2. Set scan line rate to $0.8\text{ Hz} - 1.0\text{ Hz}$ (tip velocity $\approx 1.6 - 2.0\,\mu\text{m/s}$).
3. Monitor the Trace vs. Retrace topographic height line profile in real time.
4. Increase Integral Gain ($I$-Gain) until high-frequency noise just appears on the error signal; back off by $10\% - 15\%$.
5. Adjust Proportional Gain ($P$-Gain) to minimize phase lag between Trace and Retrace traces until trace overlap correlation $> 98\%$.

### Step 5: Multi-Site Recipe Execution & Topography Mapping
1. Execute the automated 49-point wafer mapping recipe across the designated die locations.
2. At each site, capture:
   - Topography (Height channel in nm)
   - Amplitude Error channel (Dampening deviation in mV)
   - Phase channel (Material contrast between dielectric oxide and W-plug metal)
3. Apply first-order line leveling (flattening) and zero-order plane subtraction to eliminate sample tilt artifacts.
4. Extract Root-Mean-Square (RMS) surface roughness $R_q$ and maximum peak-to-valley scratch depth $R_{max}$.

---

## 4. Dimensional Scales & Metrology Context

```text
              Critical Dimensions & Metrology Scale (nm)
               ┌───────────────────────────────────────┐
               │░                                      │
 Gate Oxide Thk┤░                                      │
               │▒▒▒▒▒▒▒▒▒                              │
  Access Gate W┤▒▒▒▒▒▒▒▒▒                              │
  Access Gate L┤▓▓▓▓▓▓▓▓                               │
               │▓▓▓▓▓▓▓▓                               │
Scan Area Width┤███████████████████████████████████████│
               │███████████████████████████████████████│
               └┬─────────┬────────┬─────────┬────────┬┘
                0        250      500       750    1000 
```

---

## 5. Machine-Measurable Acceptance Criteria

| Parameter | Target Specification | Exact Physical Unit | Verification Method |
| :--- | :--- | :--- | :--- |
| **Measurement Vertical Precision** | $\le \pm 0.05$ | $\text{nm}$ (sub-Angstrom) | Replicate 10-cycle scan noise floor on planar dry oxide benchmark |
| **Trace/Retrace Topographic Profile Overlap** | $\ge 98.0$ | $\%$ | Real-time cross-correlation coefficient of forward and reverse scan lines |
| **Post-CMP Surface Roughness ($R_q$)** | $\le 0.35$ | $\text{nm}$ | Automated RMS calculation over $1.0\,\mu\text{m} \times 1.0\,\mu\text{m}$ scan window |
| **Micro-Scratch Residual Depth Threshold** | $< 3.5$ | $\text{nm}$ | Maximum peak-to-valley depth profile (must not breach gate oxide equivalent) |

---

## 6. Literature & Context Citations

1. **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**:
   - *Physical Principle & Precision*: Establishes sub-Angstrom dry gate oxide measurement precision benchmark ($\pm 0.05\text{ nm}$ for $3.5\text{ nm}$ thermal oxide) and radial non-uniformity tracking via automated **49-point wafer mapping**.
2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - *Unit Cell Dimensions*: Access transistor channel length $L = 180\text{ nm}$, active width $W = 220\text{ nm}$, stacked capacitor over bitline (COB) above drain contact via tungsten plug (W-plug). Dictates the AFM scan window of $1000\text{ nm} \times 1000\text{ nm}$ ($1.0\,\mu\text{m} \times 1.0\,\mu\text{m}$) to resolve active cell surface topography.
3. **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**:
   - *Stage Stability & Metrology Protocol*: Contextualizes mechanical stage stabilization and precision alignment tolerances transitioning from micron-scale to nanometer-scale fabrication nodes.

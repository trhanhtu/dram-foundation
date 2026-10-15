# Standard Operating Procedure (SOP): High-Density Tapping-Mode AFM Scan Execution across Post-CMP Dielectric Fields

- **Document ID:** SOP-MET-AFM-180-003
- **Process Step:** Post-CMP Dielectric Field Micro-Roughness Metrology & Power Spectral Density (PSD) Analysis
- **Node/Generation:** 180nm CMOS Open-Source DRAM (DRAM Foundation VN)
- **Hierarchy:** `180nm Open-Source DRAM Chip` > `180nm CMOS Commercial MPW Tapeout & PDK Implementation` > `Chemical Mechanical Planarization (CMP) of Inter-Layer Dielectrics & Tungsten Plugs` > `Post-CMP Ellipsometry, AFM Topography Profilometry, and Defect Metrology` > `AFM Surface Micro-Roughness and W-Plug Dishing/Erosion Profilometry` > `High-Resolution AFM Scan Recipe Optimization for Post-CMP Dielectric Micro-Roughness` > `Post-CMP Dielectric Micro-Roughness Extraction and Power Spectral Density Validation Matrix` > `High-Density Tapping-Mode AFM Scan Execution across Post-CMP Dielectric Fields`
- **Cell Architecture Context:** 1T1C Stacked Capacitor Over Bitline (COB), $8F^2$ ($0.259\,\mu\text{m}^2$) and $6F^2$ ($0.194\,\mu\text{m}^2$) cell layout, access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$, gate dielectric dry thermal $\text{SiO}_2$ thickness $3.5\text{ nm}$, cell capacitance target $28\text{ fF}$ (budget $25\text{ fF} - 30\text{ fF}$), bitline and wordline pitch $360\text{ nm} - 400\text{ nm}$.

---

## 1. Scope & Objective

This SOP establishes the physical execution procedure for high-density tapping-mode (intermittent contact) Atomic Force Microscopy (AFM) topographic scanning across planarized Inter-Layer Dielectric (ILD) oxide/nitride fields following Chemical Mechanical Planarization (CMP). The objective is to extract nanoscale surface micro-roughness ($R_q$, $R_a$), verify absence of micro-scratches, evaluate surface frequency components via 1D/2D Power Spectral Density (PSD) validation, and ensure post-CMP dielectric planarity compatible with subsequent 180nm lithography depth-of-focus and high-k stacked capacitor deposition.

---

## 2. Process Workflow Architecture

```text
┌────────────────────────┐
│                        │
│      Wafer Load &      │
│      49-Point Die      │
│       Navigation       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Cantilever Tuning &   │
│     Free Amplitude     │
│      Calibration       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Tip Engagement &    │
│        Setpoint        │
│      Optimization      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      High-Density      │
│   Tapping-Mode Scan    │
│       Execution        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Surface Topography &  │
│     PSD Metrology      │
│       Extraction       │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Substrate Loading and Wafer Map Macro-Alignment
1. Transfer the 200 mm post-CMP wafer onto the motorized, vibration-isolated AFM vacuum chuck ($10^{-6}\text{ g}$ isolation table).
2. Align wafer notch/flat and initialize optical coordinate registration.
3. Configure the metrology stage to execute an automated **49-point wafer mapping** routine to measure radial film non-uniformity across center, mid-radius, and wafer edge zones.
4. Position the optical targeting camera over the designated inter-layer dielectric (ILD) isolation fields adjacent to dense memory array tiles ($8F^2$ / $6F^2$ blocks, $360\text{ nm} - 400\text{ nm}$ pitch). Ensure the selected dielectric region is clear of macro-fill structures and metal test pads.

### Step 2: Cantilever Resonance Tuning and Free-Air Amplitude Calibration
1. Load a high-aspect-ratio, non-contact/tapping silicon probe (cantilever length $\approx 125\,\mu\text{m}$, nominal spring constant $k \approx 40\text{ N/m}$, nominal resonance frequency $f_0 \approx 300\text{ kHz}$, tip apex radius $r < 5\text{ nm}$, half-angle $< 10^\circ$).
2. Perform automated acoustic/piezo drive sweep across a $\pm 10\text{ kHz}$ window around $300\text{ kHz}$.
3. Select the operating peak frequency $\approx 500\text{ Hz}$ below natural resonance on the steeper slope to maintain linear feedback sensitivity and prevent phase bistability.
4. Drive piezo excitation to establish a free-air oscillation amplitude $A_0 = 20.0\text{ nm}$ (photodiode detector output calibrated using a certified reference step).

### Step 3: Gentle Tip Engagement & Amplitude Setpoint Optimization
1. Initiate automated tip approach sequence toward the dielectric surface.
2. Configure the feedback loop setpoint ratio ($r_{sp} = A_{sp} / A_0$) to $0.75 - 0.80$ ($A_{sp} = 15.0\text{ nm} - 16.0\text{ nm}$).
3. Verify tip lands stably in the repulsive intermittent-contact regime without damaging the probe tip apex or scratching the underlying oxide/nitride layer ($T_{ox} \sim 3.5\text{ nm}$ gate oxide equivalent sensitivity).
4. Optimize Proportional-Integral (PI) feedback gains by monitoring trace and retrace profile matching on an oscilloscope display: increase Integral Gain until trace and retrace overlap with $< 1\%$ discrepancy, without inducing high-frequency feedback ringing.

### Step 4: High-Density Tapping-Mode Scan Execution
1. Set the scan field window to $2.0\,\mu\text{m} \times 2.0\,\mu\text{m}$ (encompassing multiple periods of the $360\text{ nm} - 400\text{ nm}$ wordline/bitline pitch domain).
2. Configure the scan grid density to $512 \times 512$ pixels (or $1024 \times 1024$ pixels for ultra-fine micro-roughness inspection), achieving a lateral pixel resolution $\le 3.91\text{ nm/pixel}$.
3. Set the raster line scan rate to $1.0\text{ Hz}$ (tip linear velocity $4.0\,\mu\text{m/s}$), avoiding hydrodynamic air damping or lateral tip deflection.
4. Execute simultaneous dual-channel acquisition:
   - **Height Channel:** Measures real-space topographic z-displacement.
   - **Phase Channel:** Monitors composition variation and verifies absence of residual CMP slurry polymer or polishing debris.

### Step 5: Post-Processing, Micro-Roughness & PSD Extraction
1. Apply 1st-order polynomial line-by-line leveling and tilt flattening to remove sample tilt without distorting true high-frequency surface features.
2. Calculate Root-Mean-Square Roughness ($R_q$) and Average Roughness ($R_a$) over the $2.0\,\mu\text{m} \times 2.0\,\mu\text{m}$ scan area:
   $$R_q = \sqrt{\frac{1}{N} \sum_{i=1}^N (z_i - \bar{z})^2}$$
3. Perform 2D Fast Fourier Transform (FFT) and radially average to compute the 1D Power Spectral Density (PSD) function $P(f)$ over spatial frequencies $f \in [0.5\,\mu\text{m}^{-1}, 128\,\mu\text{m}^{-1}]$.
4. Validate that high-frequency polishing scratch peaks (chatter marks) are suppressed below background noise level and record spatial roll-off exponent.

---

## 4. Acceptance Criteria & Target Metrics

```text
                  AFM Metrology Key Parameters (nm & Hz)
                  ┌────────────────────────────────────┐
                  │●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●│
  Capacitance (fF)┤●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●│
                  │■■■■■■■■■■■■■■■■■■■■■■■■            │
Channel L (x10 nm)┤■■■■■■■■■■■■■■■■■■■■■■■■            │
                  │░░░░░░░░░░░░░░░░░░░░                │
 Setpoint Asp (nm)┤░░░░░░░░░░░░░░░░░░░░                │
  Free Amp A0 (nm)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          │
                  │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          │
Line Rate (x10 Hz)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      │
                  │▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      │
  Scan Window (um)┤████                                │
                  │████                                │
                  └┬────────┬────────┬───────┬────────┬┘
                   0        7       14      21       28 
```

| Parameter / Metric | Target Value | Acceptance Tolerance | Measurement Unit | Inspection Frequency |
| :--- | :--- | :--- | :--- | :--- |
| **Dielectric RMS Micro-Roughness ($R_q$)** | $\le 0.20$ | $\le 0.35$ | nm | Every 49-point die location |
| **Maximum Dielectric Peak-to-Valley ($R_{max}$ / $R_t$)** | $\le 1.50$ | $\le 2.50$ | nm | Per $2.0\,\mu\text{m} \times 2.0\,\mu\text{m}$ scan field |
| **Lateral Sampling Grid Resolution** | $3.91$ | $\le 4.00$ | nm/pixel | $512 \times 512$ grid over $2.0\,\mu\text{m}$ field |
| **Trace/Retrace Profile Tracking Discrepancy** | $\le 0.5$ | $\le 1.0$ | % | In-situ during scan execution |

---

## 5. Literature Citations & Physical Context

1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry: channel length $L = 180\text{ nm}$, channel width $W = 220\text{ nm}$.
   - Memory cell layout: $8F^2$ and $6F^2$ folded bitline architectures with stacked capacitor over bitline (COB).
   - Tungsten plug (W-plug) interconnects the storage capacitor crown structure to the transistor drain contact through the planarized dielectric field.
   - Storage capacitance target: $\ge 28\text{ fF}$ per cell (noise immunity requirement against alpha-particle soft errors; leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$).
2. **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**:
   - Automated 49-point wafer mapping tracking radial film non-uniformity across spin coating, oxidation, and polishing CMP runs.
   - Dry gate oxide reference thickness: $3.5\text{ nm}$ measured with sub-Angstrom precision ($\pm 0.05\text{ nm}$).
3. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - 1T1C storage capacitor maintenance requirement: $25\text{ fF}$ to $30\text{ fF}$ per cell to ensure data retention time $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Pitch dimensions: Bitline and wordline pitch spanning approximately $360\text{ nm}$ to $400\text{ nm}$.
   - Gate dielectric physical thickness: $\sim 3.5\text{ nm}$ $\text{SiO}_2$ grown via thermal dry oxidation at $850^\circ\text{C} - 900^\circ\text{C}$.

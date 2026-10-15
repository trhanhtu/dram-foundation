# Standard Operating Procedure (SOP)
## Automated Microprobe Station Calibration & Kelvin Contact Setup for TLM Test Structures

- **Document ID**: `SOP-MET-TLM-180NM-001`
- **Revision**: `1.0`
- **Generation**: Gen 3 (180nm Open-Source DRAM Chip - DRAM Foundation VN)
- **Classification**: Metrology & Thin Film Metallization Characterization

---

### 1. Scope & Objective
This SOP defines the setup, microprobe tip planarization, automated die alignment, Kelvin 4-point electrical probing, and regression extraction protocols for Transmission Line Measurement (TLM) test structures on 180nm DRAM test vehicles following Metal-1 (350 nm Al / Al-0.5% Cu) deposition and forming gas anneal (95/5 N₂/H₂ at 400°C for 30 min).

---

### 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│   Wafer Chuck Load &   │
│      Vacuum Hold       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Optical Pattern     │
│   Recognition & Die    │
│       Alignment        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  4-Point Kelvin Probe  │
│    Planarization &     │
│       Scrubbing        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Calibrated TLM     │
│  Sweeps: d=5, 10, 20,  │
│       40, 80 um        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       Regression       │
│    Extraction: R_s,    │
│    R_c, L_T, rho_c     │
│                        │
└────────────────────────┘
```

---

### 3. Step-by-Step Operating Procedure

#### Step 1: Wafer Chuck Vacuum Mounting & Pre-Flight Check
1. Place the 180nm post-metal anneal test wafer onto the automated probe station gold-plated vacuum chuck.
2. Engage chuck vacuum (> 80 kPa / 600 mmHg differential pressure) ensuring wafer flatness. Verify chuck temperature is stabilized at 25.0°C ± 0.5°C.
3. Verify microscope optics and optical pattern recognition (PR) illumination (coaxial + ring light).

#### Step 2: Probe Card / Manipulator Kelvin Arm Planarization & Contact Calibration
1. Mount 4-point Kelvin tungsten/beryllium-copper microprobes (two force arms, two sense arms) onto independent motorized micropositioners.
2. Align probe tips over an alumina contact planarization calibration substrate.
3. Lower probes to touch-down Z-height ($Z_0$). Apply a calibrated overdrive scrub of 25 µm to 35 µm to penetrate native aluminum oxide without micro-cracking the underlying dielectric.
4. Execute short-circuit zero-nulling across Kelvin pairs ($V_{\text{sense}} / I_{\text{force}}$) to null residual cable parasitics (< 0.005 Ω residual system offset).

#### Step 3: Automated Die Alignment & TLM Pad Recognition
1. Navigate probe station stage to the scribe-line or test-die TLM array.
2. Perform two-point global wafer theta correction followed by local pattern recognition targeting the TLM pad boundaries.
3. Locate the standard TLM structure consisting of rectangular contact pads with:
   - Pad Width: $W = 100\ \mu\text{m}$
   - Pad Length: $L_{\text{pad}} = 50\ \mu\text{m}$
   - Progressively increasing gap spacings: $d = 5\ \mu\text{m},\ 10\ \mu\text{m},\ 20\ \mu\text{m},\ 40\ \mu\text{m},\ 80\ \mu\text{m}$.

#### Step 4: Kelvin Probing & I-V Measurement Execution
1. For each pair of adjacent pads across gap distances $d \in \{5, 10, 20, 40, 80\}\ \mu\text{m}$:
   - Position Kelvin Force+ and Sense+ tips on Pad $N$ and Force- and Sense- tips on Pad $N+1$.
   - Force a bipolar current sweep from $-10\ \text{mA}$ to $+10\ \text{mA}$ through the Force lines.
   - Measure differential voltage $V_{\text{sense}}$ across Sense lines with high-input impedance electrometer ($Z_{\text{in}} > 10\ \text{G}\Omega$).
   - Record total resistance $R_T(d) = \Delta V / \Delta I$ from the ohmic linear slope ($R^2 > 0.999$).

#### Step 5: Regression Analysis & Parameter Extraction
1. Plot measured total resistance $R_T$ versus pad spacing $d$:
   $$R_T = 2 R_c + \left(\frac{R_s}{W}\right) d$$
2. Extract parameters:
   - **Diffusion Sheet Resistance ($R_s$)**: $\text{Slope} \times W = \text{Slope} \times 100\ \mu\text{m}$.
   - **Contact Resistance ($R_c$)**: $\frac{1}{2} \times (Y\text{-intercept at } d = 0)$.
   - **Transfer Length ($L_T$)**: $-\frac{1}{2} \times (X\text{-intercept})$.
   - **Specific Contact Resistivity ($\rho_c$)**:
     $$\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\quad [\Omega\cdot\text{cm}^2]$$

---

### 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Specification | Physical Units | Verification Method |
| :--- | :--- | :--- | :--- |
| **Metal-1 Interconnect Sheet Resistance ($R_s$)** | $R_s < 0.08$ | $\Omega/\Box$ | Four-point probe / TLM slope validation |
| **TLM Contact Pad Dimensions** | $W = 100 \pm 1$, $L_{\text{pad}} = 50 \pm 1$ | $\mu\text{m}$ | Optical pattern recognition metrology |
| **TLM Inter-Pad Spacing Progression** | $d \in \{5, 10, 20, 40, 80\} \pm 0.1$ | $\mu\text{m}$ | Metrology stage linear encoder / SEM |
| **I-V Linearity & Regression Fit ($R^2$)** | $R^2 \ge 0.999$ across all 5 gaps | Unitless | Linear least-squares fit on $R_T(d)$ |

---

### 5. Verified Literature Citations & References
1. **Transmission Line Measurement (TLM) for Specific Contact Resistivity**:
   - Pad geometry: $W = 100\ \mu\text{m}$, $L_{\text{pad}} = 50\ \mu\text{m}$.
   - Spacing progression: $d = 5\ \mu\text{m}, 10\ \mu\text{m}, 20\ \mu\text{m}, 40\ \mu\text{m}, 80\ \mu\text{m}$.
   - Resistance model: $R_T = 2 R_c + (R_s / W) d$.
   - Resistivity relation: $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\ [\Omega\cdot\text{cm}^2]$.
2. **Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects**:
   - Film: M1 Al / Al-0.5% Cu, target thickness $350\ \text{nm} \pm 5\%$.
   - Forming gas anneal: $95/5\ \text{N}_2/\text{H}_2$ at $400^\circ\text{C}$ for $30\ \text{minutes}$.
   - Metal sheet resistance specification: $R_s < 0.08\ \Omega/\Box$.
3. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Unit cell geometry: $L = 180\ \text{nm}$, $W = 220\ \text{nm}$.
   - Cell capacitance target: Minimum $28\ \text{fF/cell}$.
   - Junction leakage limit: $< 1\ \text{fA/cell}$ at $85^\circ\text{C}$.

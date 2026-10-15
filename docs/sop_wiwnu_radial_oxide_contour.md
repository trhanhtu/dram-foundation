# SOP: WIWNU Percentage Calculation & Radial Oxide Thickness Contour Mapping

- **Document ID**: SOP-MET-CMP-049
- **Technology Node**: 180nm Open-Source DRAM (Gen 3) / 180nm CMOS MPW
- **Layer / Step**: Post-CMP ILD Oxide Metrology (COB Stacked Capacitor Architecture)
- **Status**: Accepted / Industrial Release

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) defines the execution protocol for spectroscopic ellipsometry automated 49-point wafer mapping, calculation of Within-Wafer Non-Uniformity (WIWNU percentage, $1\sigma$ and range-based), and radial oxide thickness contour interpolation. This ensures post-CMP ILD (Inter-Layer Dielectric) oxide planarization meets depth-of-focus (DoF) and overlay margins before tungsten plug (W-plug) contact and bitline lithography.

---

## 2. Metrology Workflow & Execution Diagram

```text
┌─────────────────────┐
│                     │
│    Wafer Loading    │
│                     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│                     │
│    Ellipsometry     │
│     Calibration     │
│                     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│                     │
│  49-Point Map Scan  │
│                     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│                     │
│  Fresnel Ratio Fit  │
│                     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│                     │
│  Cauchy Thickness   │
│      Inversion      │
│                     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│                     │
│  WIWNU Calculation  │
│                     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│                     │
│   Radial Contour    │
│       Mapping       │
│                     │
└──────────┬──────────┘
           │
           ▼
┌──────────◇──────────┐
│                     │
│  WIWNU Target Met?  │
│                     │
└──────────◇──────────┘
           │
           ├──────────────────────────╮No
        Yes│                          │
           ▼                          ▼
┌─────────────────────┐    ┌─────────────────────┐
│                     │    │                     │
│  Pass Lot to Litho  │    │  CMP Head Pressure  │
│                     │    │        Trim         │
│                     │    │                     │
└─────────────────────┘    └─────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Tool Initialization & Baseline Calibration
1. Load standard thermal calibration wafer (dry gate oxide reference at $3.5\text{ nm} \pm 0.05\text{ nm}$).
2. Perform spectroscopic ellipsometer hardware autocalibration across spectral band $\lambda = 248\text{ nm}$ to $800\text{ nm}$ at angle of incidence $\theta_0 = 70.0^\circ$.
3. Verify baseline measurement repeatability: residual goodness of fit $R^2 > 0.999$, sub-Angstrom precision ($< 0.05\text{ nm}$ baseline drift).

### Step 2: Wafer Loading & 49-Point Polar Pattern Setup
1. Transfer post-CMP ILD production wafer from FOUP onto the vacuum chuck.
2. Align wafer notch at $0^\circ$ orientation; enforce an edge exclusion zone of $3.0\text{ mm}$ (clear aperture diameter $194\text{ mm}$ for $200\text{ mm}$ wafer).
3. Load the standardized 49-point polar coordinate map recipe:
   - **Zone 0 (Center)**: 1 point at $r = 0\text{ mm}$.
   - **Zone 1 (Inner ring)**: 8 points at $r = 25\text{ mm}$ ($\Delta\theta = 45^\circ$).
   - **Zone 2 (Mid-inner ring)**: 12 points at $r = 50\text{ mm}$ ($\Delta\theta = 30^\circ$).
   - **Zone 3 (Mid-outer ring)**: 12 points at $r = 75\text{ mm}$ ($\Delta\theta = 30^\circ$).
   - **Zone 4 (Edge ring)**: 16 points at $r = 95\text{ mm}$ ($\Delta\theta = 22.5^\circ$).

### Step 3: Spectral Acquisition & Optical Dispersion Fitting
1. Execute automated polar stage translation; measure complex reflectance ratio $\rho$ at each coordinate:
   $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
   where $r_p$ and $r_s$ are the complex Fresnel reflection coefficients.
2. Invert acquired ellipsometric angles $(\Psi_i, \Delta_i)$ into oxide thickness $T_i$ ($i = 1, \dots, 49$) utilizing the Cauchy dispersion model for SiO2 ILD:
   $$n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}, \quad k(\lambda) = 0$$
   *(Baseline parameters for densified TEOS/HDP oxide: $A_n \approx 1.457$, $B_n \approx 0.00356\ \mu\text{m}^2$)*.
3. Validate fit convergence ($MSE \le 1.50$ per site).

### Step 4: WIWNU Percentage Calculation
Calculate key statistical non-uniformity metrics over all $N = 49$ sites:
1. **Arithmetic Mean Oxide Thickness ($\bar{T}$)**:
   $$\bar{T} = \frac{1}{N} \sum_{i=1}^{N} T_i$$
2. **Sample Standard Deviation ($\sigma$)**:
   $$\sigma = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} (T_i - \bar{T})^2}$$
3. **One-Sigma Non-Uniformity ($\text{WIWNU}_{1\sigma}\%$)**:
   $$\text{WIWNU}_{1\sigma}\% = \left( \frac{\sigma}{\bar{T}} \right) \times 100\%$$
4. **Range / Half-Range Non-Uniformity ($\text{WIWNU}_{\text{range}}\%$)**:
   $$\text{WIWNU}_{\text{range}}\% = \left( \frac{T_{\max} - T_{\min}}{2\bar{T}} \right) \times 100\%$$

### Step 5: Radial Contour Mapping & Zonal Inversion
1. Compute mean concentric annular thicknesses:
   $$\bar{T}_{\text{zone}}(r_k) = \frac{1}{M_k} \sum_{j=1}^{M_k} T(r_k, \theta_j)$$
2. Generate 2D radial contour surface using bi-cubic spline interpolation over $(r, \theta)$.
3. Evaluate center-to-edge thickness delta:
   $$\Delta T_{\text{radial}} = |\bar{T}_{\text{center}} - \bar{T}_{\text{edge}}| = |\bar{T}(0) - \bar{T}(95\text{mm})|$$
4. Check for edge roll-off / edge over-polishing or center dome profiles. Feed radial delta back to CMP tool multi-zone retaining ring / membrane back-pressure controllers if out of control limit.

---

## 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Control Limit | Physical Unit | Measurement Method |
| :--- | :--- | :--- | :--- | :--- |
| **Mean Remaining ILD Thickness ($\bar{T}$)** | $650.0$ | $650.0 \pm 25.0$ | $\text{nm}$ ($6500 \pm 250\text{ \AA}$) | Spectroscopic Ellipsometry ($49$-pt map) |
| **One-Sigma Non-Uniformity ($\text{WIWNU}_{1\sigma}\%$)** | $\le 3.00$ | $\le 3.50$ | $\%$ | Statistical sample standard deviation / mean |
| **Range-Based Non-Uniformity ($\text{WIWNU}_{\text{range}}\%$)** | $\le 4.50$ | $\le 5.00$ | $\%$ | $(T_{\max} - T_{\min}) / (2\bar{T}) \times 100\%$ |
| **Radial Center-to-Edge Delta ($\Delta T_{\text{radial}}$)** | $\le 20.0$ | $\le 25.0$ | $\text{nm}$ ($200 - 250\text{ \AA}$) | Radial zonal profile $|\bar{T}(0) - \bar{T}(95\text{mm})|$ |

```text
                                                        
                     ┌─────────────────────────────────┐
                     │■■■                              │
WIWNU Max-Min (x100%)┤■■■                              │
                     │▒▒▒                              │
WIWNU 1-Sigma (x100%)┤▒▒▒                              │
     Radial Delta (A)┤▓▓                               │
                     │▓▓                               │
   Mean ILD Thick (A)┤█████████████████████████████████│
                     │█████████████████████████████████│
                     └┬───────┬───────┬───────┬───────┬┘
                      0     1625    3250    4875   6500 
```

---

## 5. Verified Source Citations
- **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**: Physical principle of polarization ratio $\rho = r_p / r_s = \tan(\Psi) \cdot \exp(i\Delta)$; Cauchy and Sellmeier optical dispersion modeling; 49-point wafer mapping protocol; precision reference for gate oxide baseline ($3.5\text{ nm} \pm 0.05\text{ nm}$).
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Stacked capacitor over bitline (COB) architecture requiring strict ILD planarization above bitline contact and tungsten plug (W-plug) interconnects.
- **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**: Physical grid resolution ($0.005\ \mu\text{m}$ / $5\text{ nm}$), contact hole dimension ($0.17\ \mu\text{m} \times 0.17\ \mu\text{m}$), DUV KrF ($\lambda = 248\text{ nm}$) exposure constraints, and overlay budget ($\le 35\text{ nm}$).

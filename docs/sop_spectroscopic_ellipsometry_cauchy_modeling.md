# Standard Operating Procedure (SOP): Spectroscopic Ellipsometer Optical Calibration & Cauchy Dispersion Modeling

- **Module**: Metrology / Chemical Mechanical Planarization (CMP) & Thin Films
- **Node**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Target Layer**: Inter-Layer Dielectric (ILD Oxide) / Post-CMP Planarization
- **Generation**: Gen 3 (nm)
- **Status**: Implemented

---

## 1. Process Workflow Architecture

```text
┌────────────────────────┐
│                        │
│   Baseline Hardware    │
│      Calibration       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Bare Si Substrate    │
│      Verification      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      Post-CMP ILD      │
│  Spectral Acquisition  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Cauchy Dispersion    │
│     Model Fitting      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Acceptance & Wafer   │
│     Mapping Output     │
│                        │
└────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Optical Hardware Alignment and Baseline Calibration
1. Power up the spectroscopic ellipsometer broadband light source and detector array. Allow thermal stabilization (minimum 30 minutes).
2. Clean and load a certified reference calibration standard (standard thermal oxide on silicon, $d \approx 100\text{ nm}$ or reference bare silicon wafer).
3. Align sample stage tilt and height (Z-position) using the optical auto-collimator quadrant photodiode to maximize reflected intensity and minimize beam walk-off.
4. Execute straight-through (transmission) or reference reflection calibration to calculate polarizer and rotating compensator offset angles.

### Step 2: Reference Substrate Optical Baseline Verification
1. Perform baseline measurement on certified bare silicon with native oxide standard.
2. Measure the complex reflectance ratio:
   $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
   where $r_p$ and $r_s$ are the complex Fresnel reflection coefficients, $\Psi$ represents the amplitude ratio, and $\Delta$ represents the phase change upon reflection.
3. Verify that native oxide thickness fits within calibration limits ($d_{\text{native}} \le 2.0\text{ nm}$ with measurement precision baseline matching $\pm 0.05\text{ nm}$ scale).

### Step 3: Post-CMP ILD Wafer Load and Multi-Angle Spectral Acquisition
1. Transfer the post-CMP 180nm DRAM wafer (planarized ILD oxide over tungsten plugs and cell access structures) onto the vacuum chuck.
2. Align wafer notch/flat and focus on the scribe line or dedicated unpatterned ILD test pads.
3. Configure the goniometer angle of incidence (AOI) to nominal Brewster-proximate angle ($\theta = 65^\circ - 75^\circ$, typically $70^\circ$).
4. Acquire spectroscopic raw spectra $\Psi(\lambda)$ and $\Delta(\lambda)$ across the operational spectrum (UV to NIR).

### Step 4: Cauchy Dispersion Layer Modeling & Regression Fitting
1. Construct the optical model:
   - **Substrate**: Crystalline Silicon (c-Si, fixed table $n, k$).
   - **Dielectric Layer**: Transparent Inter-Layer Dielectric (ILD $\text{SiO}_2$).
2. Apply the Cauchy dispersion model parameterization for transparent dielectric films ($k(\lambda) \approx 0$):
   $$n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}$$
   where $A_n \approx 1.45 - 1.46$ for thermal/CVD $\text{SiO}_2$, and $\lambda$ is in micrometers ($\mu\text{m}$).
3. Run Levenberg-Marquardt non-linear regression to simultaneously extract ILD film thickness $t_{\text{ILD}}$ and Cauchy refractive index coefficients ($A_n, B_n$).

### Step 5: Automated Wafer Mapping & Radial Uniformity Tracking
1. Initiate the automated wafer mapping recipe using either a standard 9-point or 49-point wafer mapping grid across the wafer diameter.
2. Record local ILD thickness values, film non-uniformity percentage, and mean square error (MSE) across the array.
3. Flag any site exceeding CMP planarity or erosion specifications.

---

## 3. Machine-Measurable Acceptance Criteria Target Metrics

| Parameter / Metric | Acceptance Target / Tolerance | Engineering Unit | Verification Method |
| :--- | :--- | :--- | :--- |
| **Thin Oxide Measurement Precision** | $\pm 0.05$ | $\text{nm}$ (Sub-Angstrom) | Repeated dynamic loading & spectral fit on thin oxide standard |
| **Thick Film / PR Metrology Precision** | $\pm 2$ | $\text{nm}$ | Regression fit across multi-point optical probe |
| **Wafer Mapping Grid Resolution** | $9\text{ or } 49$ | points / wafer | Automated motorized stage polar/Cartesian grid scan |
| **Optical Regression Goodness-of-Fit** | $\text{MSE} \le 1.50$ (or $R^2 \ge 0.999$) | dimensionless | Levenberg-Marquardt convergence on $\Psi(\lambda), \Delta(\lambda)$ |

---

## 4. Contextual Literature Citations

1. **Source: Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**
   - *Physical Principle & Equation*: $\rho = r_p / r_s = \tan(\Psi) \cdot \exp(i\Delta)$
   - *Dispersion Parameterization*: Cauchy or Sellmeier dispersion models for $n(\lambda)$ and $k(\lambda)$.
   - *Precision Metrics*: Dry gate oxide ($3.5\text{ nm}$) measured with sub-Angstrom precision ($\pm 0.05\text{ nm}$); thick film / photoresist ($1.3\ \mu\text{m}$) measured within $\pm 2\text{ nm}$.
   - *Mapping Protocol*: Automated 9-point or 49-point wafer mapping tracking radial film non-uniformity across spin coating and furnace runs.
2. **Source: Ellipsometry Basics**
   - *Phase and Amplitude*: Direct determination of phase change $\Delta$ and amplitude ratio $\Psi$.
3. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - *Architecture Context*: Stacked capacitor over bitline (COB) with access transistor ($L = 180\text{ nm}$, $W = 220\text{ nm}$) connected to tungsten plugs (W-plug) isolated by CMP ILD planarization.

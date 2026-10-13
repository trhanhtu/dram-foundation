# SOP: Full-Wafer Radial Non-Uniformity Contour Reconstruction & Process Tolerance Validation

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 1 (mm)
- **Action Type**: Make
- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > Buffered Oxide Etch (BOE 6:1) SiO2 Patterning [Chemical Processing] > HMDS Vapor Prime, Resist Patterning & Wet Oxide Dip-Etch Recipe Execution [Wet Chemistry] > Spectroscopic Ellipsometry & Resist Undercut Metrology Inspection [Metrology] > Automated Multi-Point Delta-Psi Film Thickness Wafer Mapping Acquisition [Metrology] > Full-Wafer Radial Non-Uniformity Contour Reconstruction & Process Tolerance Validation [Metrology]

---

## 1. Overview & Physical Principles

In the fabrication of the 180nm Open-Source DRAM cell architecture (featuring access transistors with channel length $L = 180\text{ nm}$, active diffusion width $W = 220\text{ nm}$, stacked capacitor cell layout, and manufacturing physical grid resolution of $0.005\text{ }\mu\text{m} = 5\text{ nm}$), precise dielectric and photoresist film thickness control across the full wafer radius is vital. Non-destructive spectroscopic ellipsometry measures the ratio of Fresnel reflection coefficients:
$$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$

By parameterizing refractive index $n(\lambda)$ and extinction coefficient $k(\lambda)$ using Cauchy or Sellmeier dispersion formulations, automated polarimetric multi-point spectra ($\Psi, \Delta$) are fitted to extract:
1. Thin dry gate oxide dielectric films ($3.5\text{ nm}$ nominal target) with sub-angstrom precision ($\pm 0.05\text{ nm}$).
2. Patterned/unpatterned photoresist films ($1.3\text{ }\mu\text{m}$ nominal target) with $\pm 2\text{ nm}$ precision.

Radial contour reconstruction converts discrete 9-point or 49-point wafer mapping data into 2D/radial thickness gradients:
$$\text{Non-Uniformity (\% NU)} = \frac{t_{\max} - t_{\min}}{2 \times t_{\text{mean}}} \times 100\%$$
This protocol validates process tolerances across spin coating and furnace runs, ensuring boundary layers and etch allowances do not compromise critical features such as gate oxide integrity or minimum lithographic overlay tolerances ($\le 35\text{ nm}$).

```text
┌────────────────────────────────────────────────────────┐
│  Automated Multi-Point (9-pt / 49-pt) SE Data Import   │
│  (Acquire raw Psi(λ), Delta(λ) across wafer radii)     │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Cauchy / Sellmeier Dispersion Model Inversion & Fit   │
│  (Extract tox [3.5 nm] or tresist [1.3 µm] per site)   │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Full-Wafer Radial Contour Mapping & % NU Calculation  │
│  (% NU = (t_max - t_min) / (2 * t_mean) * 100%)        │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Process Tolerance Validation & Lot Disposition        │
│  (Pass / Rework / Quarantine based on Spec Limits)     │
└────────────────────────────────────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Polarimetric Measurement Grid & Data Ingestion
1. Mount wafer onto the automated vacuum chuck of the spectroscopic ellipsometer.
2. Initialize and load polarimetric acquisition coordinates:
   - For rapid qualification: Standard 9-point radial diamond-cross pattern.
   - For full-wafer contour reconstruction: 49-point concentric radial polar grid (covering center $r = 0\text{ mm}$, intermediate radii $r = 0.25R, 0.5R, 0.75R$, and edge exclusion zone boundary $r = 0.95R$).
3. Measure ellipsometric angles $\Psi(\lambda)$ and $\Delta(\lambda)$ across the UV-visible spectral range ($250\text{ nm} \le \lambda \le 800\text{ nm}$) based on $\rho = r_p / r_s = \tan(\Psi) \exp(i\Delta)$.

### Step 2: Dispersion Model Fitting & Thickness Extraction
1. Apply the qualified optical dispersion model:
   - For dielectric $\text{SiO}_2$ layers (nominal $3.5\text{ nm}$ dry oxide): Fit Sellmeier/Cauchy dispersion $n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4}$ with extinction coefficient $k(\lambda) = 0$ in the transparent regime. Verify measurement precision within $\pm 0.05\text{ nm}$.
   - For photoresist layers (nominal $1.3\text{ }\mu\text{m}$): Fit Cauchy model with appropriate absorption tail, ensuring measurement precision within $\pm 2\text{ nm}$.
2. Record fitted physical thickness $t_i$ ($i = 1, \dots, N$, where $N = 49$ or $9$) along with mean square error (MSE). Discard and remeasure any site where $\text{MSE} > 2.5$.

### Step 3: Radial Interpolation & Contour Reconstruction
1. Map discrete thickness points $(r_i, \theta_i, t_i)$ to physical cartesian wafer coordinates $(x_i, y_i)$ on the $0.005\text{ }\mu\text{m}$ manufacturing placement grid reference frame.
2. Compute radial mean profile:
   $$\bar{t}(r) = \frac{1}{M_r}\sum_{j=1}^{M_r} t(r, \theta_j)$$
   where $M_r$ is the number of azimuthal sample sites at radius $r$.
3. Execute bi-cubic spline interpolation or radial basis function (RBF) surface fitting across the wafer radius up to the $3\text{ mm}$ edge exclusion boundary.
4. Generate 2D contour isothickome maps displaying thickness variations in increments of $0.05\text{ nm}$ (for $3.5\text{ nm}$ oxide) or $5\text{ nm}$ (for $1.3\text{ }\mu\text{m}$ resist).

### Step 4: Process Tolerance Evaluation & Statistical Disposition
1. Compute the wafer statistical non-uniformity metrics:
   - Maximum thickness $t_{\max}$, minimum thickness $t_{\min}$, arithmetic mean thickness $t_{\text{mean}}$, and standard deviation $\sigma$.
   - Radial percent non-uniformity:
     $$\% \text{NU} = \frac{t_{\max} - t_{\min}}{2 \times t_{\text{mean}}} \times 100\%$$
2. Compare radial thickness roll-off between center ($r = 0\text{ mm}$) and outer edge ($r \ge 0.9R$) to verify compliance against spin coating edge-bead or furnace thermal gradient limits.
3. Lot Disposition Decision:
   - **PASS**: All 49-point thickness values fall within process spec and $\% \text{NU} \le 1.5\%$ (oxide) or $\le 2.0\%$ (resist).
   - **FAIL / REWORK**: If resist thickness deviation exceeds $\pm 2\text{ nm}$ precision boundary or $\% \text{NU} > 2.5\%$, trigger strip and re-coat.
   - **QUARANTINE**: If dry oxide deviation exceeds $\pm 0.05\text{ nm}$ precision band or displays asymmetrical non-radial saddle contours, quarantine furnace tube for thermocouple/gas-injector recalibration.

---

## 3. Acceptance Criteria & Target Metrics

| Parameter | Metric Target / Acceptance Criteria | Physical Units | Verification Method |
| :--- | :--- | :--- | :--- |
| **Dry Gate Oxide Measurement Precision** | $\pm 0.05$ | $\text{nm}$ | Multi-point Spectroscopic Ellipsometry ($3.5\text{ nm}$ nominal target) |
| **Photoresist Film Measurement Precision** | $\pm 2$ | $\text{nm}$ | Cauchy model spectroscopic fit ($1.3\text{ }\mu\text{m}$ nominal target) |
| **Wafer Spatial Sampling Density** | Automated 9-point or 49-point wafer mapping | Points/Wafer | Ellipsometer automated polar coordinate stage mapping |
| **Radial Oxide Thickness Non-Uniformity (% NU)** | $\le 1.5\%$ (Center-to-Edge gradient across 49 points) | $\%$ | Full-wafer radial contour reconstruction formula: $\frac{t_{\max} - t_{\min}}{2 t_{\text{mean}}} \times 100\%$ |
| **Physical Feature Placement Grid Resolution** | $0.005$ | $\mu\text{m}$ ($5\text{ nm}$) | Coordinate mapping reference to PDK layout grid |

---

## 4. Cited Reference Sources

1. **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**:
   - Fundamental physical equation: $\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$ using complex Fresnel reflection coefficients $r_p, r_s$.
   - Cauchy and Sellmeier optical dispersion modeling for $n(\lambda)$ and $k(\lambda)$.
   - Dry gate oxide ($3.5\text{ nm}$) sub-angstrom measurement precision ($\pm 0.05\text{ nm}$).
   - Photoresist ($1.3\text{ }\mu\text{m}$) measurement precision within $\pm 2\text{ nm}$.
   - Automated 9-point and 49-point wafer mapping to track radial film non-uniformity across spin coating and furnace runs.
2. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Physical placement grid resolution: $0.005\text{ }\mu\text{m}$ ($5\text{ nm}$).
   - Overlay error budget $\le 35\text{ nm}$ between gate poly and active diffusion.
   - DUV ($248\text{ nm}$ KrF excimer laser, $\text{NA} = 0.65$, $k_1 = 0.40$) lithography for critical feature definition.
3. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - DRAM access transistor dimensions: Channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - Stacked capacitor over bitline architecture with high dielectric integrity requirements for retention and noise immunity.

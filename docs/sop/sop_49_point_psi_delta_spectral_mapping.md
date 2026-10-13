# SOP: 49-Point Psi/Delta Spectral Acquisition & Radial Thickness Non-Uniformity Mapping

- **Date**: 2026-10-13
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Module**: Metrology / Thermal Processing Integration
- **Node**: 180nm Open-Source DRAM (Gen 2 µm architecture)
- **Target Layer**: Pyrogenic Wet Field Oxide Isolation (Nominal 350 nm)

---

## 1. Scope & Objective
Establish a standard operating procedure for automated non-destructive spectroscopic ellipsometry across 49 polar/Cartesian sampling sites on a 200 mm production wafer. The protocol extracts spectral ellipsometric angles ($\Psi, \Delta$) across the ultraviolet-to-visible regime to extract physical film thickness ($T_{ox}$) and refractive index ($n(\lambda)$) using Cauchy dispersion modeling, qualifying within-wafer non-uniformity (WIWNU) following pyrogenic wet field oxidation.

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│  Wafer Load & Vacuum   │
│         Chuck          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Optical Calibration   │
│         Si Ref         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│        49-Point        │
│   Polar/Radial Move    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       Psi/Delta        │
│      Acquisition       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Cauchy Modeling &    │
│       Thickness        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Radial Contour Map &  │
│          SPC           │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

1. **System Initialization & Baseline Calibration**:
   - Verify tool beam alignment and analyzer angle offset using a certified reference standard (e.g., thermal oxide on Si reference).
   - Set the angle of incidence ($\theta_0$) to $70.0^\circ$ (near the Brewster angle for the $\text{SiO}_2/\text{Si}$ interface).
   - Confirm Xenon/Deuterium broadband illumination stability across $\lambda = 250\text{ nm} - 800\text{ nm}$.

2. **Automated Wafer Load & Vacuum Chucking**:
   - Robotically transfer the post-pyrogenic field oxidation wafer (frontside target: 350 nm $\text{SiO}_2$) onto the kinematic vacuum chuck.
   - Establish vacuum retention $\le -80\text{ kPa}$; verify optical wafer leveler autofocus and z-height positioning within $\pm 0.5\ \mu\text{m}$.
   - Orient notch to $0.0^\circ$ via optical edge sensor.

3. **Recipe Selection & Sampling Matrix Execution**:
   - Load automated 49-point polar/concentric radial map:
     - 1 center point ($r = 0\text{ mm}$)
     - 4 concentric rings with 3 mm edge exclusion ($r_1 = 20\text{ mm}$, $r_2 = 45\text{ mm}$, $r_3 = 70\text{ mm}$, $r_4 = 97\text{ mm}$) with angular stepping.
   - Execute sequential XY stage positioning with settling time $\ge 150\text{ ms}$ per coordinate.

4. **Spectral Acquisition ($\Psi, \Delta$)**:
   - At each of the 49 coordinates, acquire polarization reflection data to evaluate the complex ratio:
     $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
   - Collect spectra over $\lambda = 250\text{ nm} - 800\text{ nm}$ with an integration time of $500\text{ ms}$ per point.

5. **Optical Dispersion Fitting & Parameter Regression**:
   - Regress experimental $(\Psi, \Delta)$ against a two-layer physical model: $\text{Si}\ (\text{substrate}) / \text{SiO}_2\ (\text{Cauchy dielectric layer})$.
   - Cauchy parameterization:
     $$n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}, \quad k(\lambda) = 0$$
   - Fit thickness $T_{ox}$ and index $A_n$ ($n_{632.8\text{ nm}} \approx 1.457$) while monitoring Mean Squared Error ($\text{MSE} \le 2.0$).

6. **Radial Non-Uniformity & Contour SPC Mapping**:
   - Calculate within-wafer thickness metrics:
     $$\bar{T}_{ox} = \frac{1}{49}\sum_{i=1}^{49} T_{i}, \quad \text{WIWNU } (\%) = \frac{T_{\max} - T_{\min}}{2 \bar{T}_{ox}} \times 100\%$$
   - Generate 2D radial thickness contour map and post summary records into the fab SPC database.

---

## 4. Acceptance Criteria & Target Metrics

| Parameter | Target Metric | Engineering Tolerance / Spec | Verification Method |
| :--- | :--- | :--- | :--- |
| **Field Oxide Thickness ($T_{ox}$ Mean)** | 350.0 nm | $350.0\text{ nm} \pm 10.0\text{ nm}$ | 49-Point Spectroscopic Ellipsometry Average |
| **WIWNU Thickness Non-Uniformity** | $\le 1.50\%$ | Max $\le 2.00\%$ | $(T_{\max} - T_{\min}) / (2\bar{T}_{ox}) \times 100\%$ |
| **Refractive Index ($n$ at $\lambda = 632.8\text{ nm}$)** | 1.457 | $1.457 \pm 0.005$ | Cauchy Dispersion Fit |
| **Measurement Precision Repeatability** | Sub-Ångström | $\le \pm 0.05\text{ nm}$ ($1\sigma$) | 10-cycle static dynamic repeatability at center point |
| **Goodness-of-Fit (MSE)** | $\le 1.50$ | $\text{MSE} < 2.00$ | Levenberg-Marquardt Regression Fit |

---

## 5. Literature & Context Citations

- **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**:
  - Optical modeling fundamentals ($\rho = r_p / r_s = \tan(\Psi)\exp(i\Delta)$).
  - Cauchy / Sellmeier dispersion models parameterizing $n(\lambda)$ and $k(\lambda)$.
  - Sub-Ångström precision capability ($\pm 0.05\text{ nm}$) and automated 49-point wafer mapping to track radial non-uniformity across furnace and deposition runs.
- **Pyrogenic Wet Field Oxide Isolation (350 nm)**:
  - Process specification baseline defining target physical field oxide thickness of 350 nm for 180nm node isolation architecture.
- **180nm DRAM Cell Layout Topology & Architecture**:
  - Integration framework for 180nm node dielectric and isolation budgets.

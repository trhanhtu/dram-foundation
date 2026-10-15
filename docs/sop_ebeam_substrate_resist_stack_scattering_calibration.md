# Standard Operating Procedure (SOP): E-Beam Substrate-Resist Stack Definition & Scattering Cross-Section Calibration

- **Module**: Photolithography / Electron Beam Direct Write (EBDW) & Metrology
- **Node**: 180nm Open-Source DRAM (DRAM Foundation VN) / Commercial MPW Gate Definition
- **Target Layer**: Critical Dimension (CD) Access Transistor Gate Polysilicon ($L = 180\text{ nm}$, $W = 220\text{ nm}$)
- **Generation**: Gen 3 (nm)
- **Status**: Implemented / Approved for Monte Carlo PEC Execution

---

## 1. Process Workflow Architecture

```text
┌────────────────────────┐
│                        │
│    1. Substrate and    │
│    Stack Definition    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       2. Resist        │
│  Application and Bake  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     3. Elastic and     │
│  Inelastic Scattering  │
│      Calibration       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     4. Monte Carlo     │
│   Trajectory and PSF   │
│   Energy Deposition    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   5. 180nm Gate Grid   │
│  and Overlay Signoff   │
│                        │
└────────────────────────┘
```

```text
       180nm DRAM E-Beam Lithography CD and Overlay Metrics (nm)
                 ┌─────────────────────────────────────┐
                 │████████████████████████████████     │
   Gate Channel L┤████████████████████████████████     │
                 │░░░░░░░░░░░░░░░░░░░░░░░░░░░          │
Poly Length Drawn┤░░░░░░░░░░░░░░░░░░░░░░░░░░░          │
   Diff Width Min┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          │
                 │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          │
   Poly Space Min┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                 │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
Max Overlay Error┤███████                              │
                 │███████                              │
                 └┬────────┬────────┬────────┬────────┬┘
                 0.0     52.5     105.0    157.5  210.0 
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Substrate-Resist Multi-Layer Stack Parameter Definition
1. Define the physical substrate-resist material stack in the Monte Carlo simulation engine:
   - **Substrate Base**: Crystalline Silicon ($\text{Si}$, atomic number $Z = 14$, density $\rho = 2.33\text{ g/cm}^3$, semi-infinite thickness $\ge 500\ \mu\text{m}$).
   - **Gate Dielectric / Thin Oxide**: Silicon dioxide ($\text{SiO}_2$, $Z_{\text{eff}} \approx 10$, density $\rho = 2.20\text{ g/cm}^3$, physical thickness $t_{\text{ox}} = 3.5\text{ nm}$).
   - **Gate Conductor Layer**: Polycrystalline silicon film for access transistor gate ($L = 180\text{ nm}$, drawn gate length $150\text{ nm}$).
   - **High-Resolution E-Beam Resist**: HSQ / ZEP520A (or benchmark baseline Shipley 1813 positive resist, nominal thickness $1.3\ \mu\text{m}$, density $\rho \approx 1.20\text{ g/cm}^3$).

### Step 2: Resist Film Application, Thermal Conditioning & Thickness Verification
1. Spin-coat the resist film on a clean, dehydration-baked wafer chuck at 4000 RPM to yield the target film thickness ($1.3\ \mu\text{m}$).
2. Perform soft bake thermal cure at $115^\circ\text{C}$ for 60 seconds on a precision-calibrated aluminum contact hot plate to evaporate residual solvent and minimize resist pinhole density.
3. Validate film thickness uniformity across the substrate using spectroscopic ellipsometry (Cauchy dispersion fit) prior to electron exposure.

### Step 3: Elastic and Inelastic Scattering Cross-Section Calibration
1. Calibrate screened Rutherford elastic scattering differential cross-sections:
   $$\frac{d\sigma_{\text{el}}}{d\Omega} = \frac{Z^2 e^4}{16 \pi^2 \varepsilon_0^2 m_0^2 v^4 (1 - \cos\theta + 2\beta_{\text{scr}})^2}$$
   where $Z$ is the atomic number of the target atom, $e$ is elementary charge, $v$ is incident electron velocity, and $\beta_{\text{scr}}$ is the atomic electron-cloud screening parameter.
2. Calibrate inelastic energy loss rate using the modified Bethe continuous slowing down approximation (CSDA):
   $$-\frac{dE}{ds} = \frac{2\pi e^4 N_A \rho Z}{E \cdot A} \ln\left(\frac{1.166 E_m}{J}\right)$$
   where $N_A$ is Avogadro's number, $A$ is atomic weight, $\rho$ is layer mass density, $E_m$ is mean kinetic energy, and $J$ is the mean ionization potential of the material layer.

### Step 4: Monte Carlo Trajectory Ensemble Simulation & PSF Parameter Extraction
1. Launch an ensemble of $N \ge 10^5$ primary electron trajectories injected at normal incidence ($\theta_{\text{in}} = 0^\circ$) across the stack.
2. Track 3D step-length distribution $\lambda_{\text{mfp}} = 1 / (\sum N_i \sigma_i)$, elastic scattering deflection angles, and inelastic cumulative energy deposition into the resist layer grid.
3. Fit the radial absorbed energy density into the double-Gaussian Point Spread Function (PSF):
   $$f(r) = \frac{1}{\pi (1 + \eta)} \left[ \frac{1}{\alpha^2} \exp\left(-\frac{r^2}{\alpha^2}\right) + \frac{\eta}{\beta^2} \exp\left(-\frac{r^2}{\beta^2}\right) \right]$$
   where $\alpha$ is the forward scattering range, $\beta$ is the backscattering range from the high-$Z$ substrate, and $\eta$ is the backscatter-to-forward energy ratio.

### Step 5: Manufacturing Grid Quantization & 180nm Gate Overlay Signoff
1. Map the extracted energy deposition profile and dose modulation matrix onto the physical manufacturing grid resolution of $0.005\ \mu\text{m}$ ($5\text{ nm}$).
2. Validate access transistor gate geometry targeting channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$ (minimum drawn poly gate length $150\text{ nm}$, minimum poly spacing $210\text{ nm}$ / $0.21\ \mu\text{m}$, minimum active diffusion width $150\text{ nm}$ / $0.15\ \mu\text{m}$).
3. Verify that the combined electron-beam exposure positional drift and beam-deflection distortion satisfy the maximum permissible gate-to-diffusion overlay error budget $\le 35\text{ nm}$.

---

## 3. Machine-Measurable Acceptance Criteria Target Metrics

| Parameter / Metric | Acceptance Target / Tolerance | Engineering Unit | Verification Method |
| :--- | :--- | :--- | :--- |
| **Manufacturing Placement Grid Resolution** | $0.005$ ($5$) | $\mu\text{m}$ ($\text{nm}$) | EBDW beam deflection digital-to-analog converter (DAC) step pitch quantization check |
| **Access Transistor Physical Gate CD ($L$)** | $180 \pm 5$ | $\text{nm}$ | In-line CD-SEM / cross-sectional metrology (minimum drawn poly gate length: $150\text{ nm}$) |
| **Minimum Poly Gate Spacing** | $\ge 210$ ($0.21$) | $\text{nm}$ ($\mu\text{m}$) | Post-exposure CD-SEM automated pitch measurement |
| **Gate Poly to Active Diffusion Overlay Error** | $\le 35$ | $\text{nm}$ | Multi-point automated vernier / optical overlay metrology on test fiducials |

---

## 4. Contextual Literature Citations

1. **Source: SkyWater SKY130 Open PDK Design Rules & Lithography Grid**
   - *Manufacturing Grid*: Physical placement grid resolution is $0.005\ \mu\text{m}$ ($5\text{ nm}$).
   - *Critical Dimensions (CD)*: Minimum active diffusion (diff) width: $0.15\ \mu\text{m}$ ($150\text{ nm}$); minimum poly gate length: $0.15\ \mu\text{m}$ ($150\text{ nm}$); minimum poly gate spacing: $0.21\ \mu\text{m}$ ($210\text{ nm}$).
   - *Overlay Error Budget*: Maximum permissible overlay error between gate poly and active diffusion is $\le 35\text{ nm}$.
2. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - *Unit Cell Geometry*: Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - *Architecture Context*: Stacked capacitor over bitline (COB) architecture with tungsten plug (W-plug) connection.
3. **Source: Sam Zeloof Z1 Garage Semiconductor Journal (2018)**
   - *Resist Spin-Coating & Thermal Profile*: Shipley 1813 spin-coated at 4000 RPM yields $\sim 1.3\ \mu\text{m}$ thickness; soft bake at $115^\circ\text{C}$ for 60 seconds on a flat contact hot plate.

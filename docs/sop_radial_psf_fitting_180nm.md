# Standard Operating Procedure (SOP)
## Radial Energy Deposition Profile Fitting & Double-Gaussian PSF Parameter Extraction

- **Document ID:** SOP-LITH-EBDW-180-PSF01
- **Process Generation:** 180nm Open-Source DRAM (Gen 3)
- **Action Type:** Buy / Tool Parameter Extraction & Integration
- **Target Layer:** 180nm Critical Dimension Gates (Access Transistor Channel L = 180 nm, W = 220 nm)
- **Grid Resolution:** 5 nm (0.005 µm SkyWater SKY130 manufacturing grid)

---

### 1. Objective & Physical Principle
Characterize the radial energy deposition profile $E(r)$ obtained from Monte Carlo electron-solid scattering simulations and physical resist exposures (HSQ / ZEP520A over poly gate stacks on bulk Si) to extract Point Spread Function (PSF) parameters for the Proximity Effect Correction (PEC) dose-modulation engine.

The Double-Gaussian Point Spread Function is formulated as:
$$PSF(r) = \frac{1}{\pi (1 + \eta)} \left[ \frac{1}{\alpha^2} \exp\left(-\frac{r^2}{\alpha^2}\right) + \frac{\eta}{\beta^2} \exp\left(-\frac{r^2}{\beta^2}\right) \right]$$

- $\alpha$: Forward-scattering range (dominated by beam blur and electron scattering within resist).
- $\beta$: Back-scattering range (dominated by wide-angle backscatter from underlying polysilicon and bulk Si).
- $\eta$: Ratio of total backscattered energy deposition to forward-scattered energy deposition.

---

### 2. Execution Steps

1. **Stack & Resist Thickness Calibration**:
   - Verify photoresist (HSQ or ZEP520A) thickness profile across the wafer using automated 9-point or 49-point Spectroscopic Ellipsometry / Reflectometry.
   - Confirm resist thickness target within ±2 nm tolerance. Verify underlying gate dielectric (3.5 nm equivalent oxide) within ±0.05 nm.

2. **Simulation Data Parsing & Placement Grid Binning**:
   - Load radial energy deposition data $E(r, z)$ output from the Monte Carlo trajectory simulator.
   - Integrate deposition along the resist thickness axis $z$.
   - Bin radial coordinates $r$ strictly adhering to the 0.005 µm (5 nm) physical manufacturing grid up to a radial cutoff of $r_{max} \ge 3\beta$ (~30 µm).

3. **Non-Linear Least Squares (NLLS) Fitting**:
   - Apply Levenberg-Marquardt optimization minimizing weighted residual squares:
     $$\chi^2 = \sum_{i} w_i \cdot \left[ E(r_i) - PSF(r_i; \alpha, \beta, \eta) \right]^2$$
   - Weight $w_i = 1 / \sigma_i^2$ normalized by radial bin area $2\pi r_i \Delta r$.

4. **Parameter Extraction & Validation**:
   - Extract $\alpha$ (nm), $\beta$ (µm), and $\eta$ (dimensionless ratio).
   - Validate extracted forward-scattering blur against gate overlay error budget ($\le 35\text{ nm}$) and drawn CD (150 nm - 180 nm).

5. **Format & Export to PEC Dose Modulation Table**:
   - Export parameters into PEC engine matrix formatted on the 5 nm grid resolution for access transistor gate exposure ($L = 180\text{ nm}$, $W = 220\text{ nm}$).

---

### 3. Acceptance Criteria Targets

| Metric | Target Specification | Physical Unit | Measurement Method / Verification Tool |
| :--- | :--- | :--- | :--- |
| **Forward Scattering Range ($\alpha$)** | $20.0 \le \alpha \le 35.0$ | nm | Levenberg-Marquardt NLLS Fit (95% CI) |
| **Back Scattering Range ($\beta$)** | $8.0 \le \beta \le 12.0$ | µm | Long-range radial bin integration ($r \le 35\ \mu\text{m}$) |
| **Backscatter Ratio ($\eta$)** | $0.50 \le \eta \le 0.85$ | Dimensionless | NLLS Double-Gaussian energy partition ratio |
| **Curve Fit Residual ($R^2$)** | $\ge 0.9950$ (Max Dev $\le 1.8$) | Dimensionless (nm CD err) | Non-linear regression goodness-of-fit |

---

### 4. Verified Literature References
- **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**: Resist thickness verification (±2 nm precision) and thin dielectric metrology (3.5 nm oxide within ±0.05 nm), 9-point/49-point wafer mapping.
- **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**: Physical manufacturing grid of 0.005 µm (5 nm), minimum drawn poly gate length 150 nm, overlay error budget $\le 35\text{ nm}$.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: 180nm unit cell geometry with access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.

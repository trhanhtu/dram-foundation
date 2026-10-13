# Standard Operating Procedure (SOP)
## Assembly, Multi-Point Tilt Calibration, and Optical & Electrical Baseline Qualification on 3.5nm SiO2 MOS Dummies

- **Document ID**: SOP-MET-180NM-MOSCAP-001
- **Node**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Dielectric / Target**: 3.5 nm Thermal SiO2 Gate Oxide on P-type (100) Si
- **Test Structures**: Planar MOSCAP circular Al gate dots (200 µm, 500 µm, 1000 µm) with Au/Al backside contact
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)

---

### 1. Scope & Objective
Establish the precision mechanical assembly, multi-point tilt calibration, optical spectroscopic ellipsometry, and electrical high-frequency (1 MHz) / quasi-static C-V baseline qualification protocol on planar MOS dummy test coupons grown via dry thermal oxidation at 850°C–900°C.

---

### 2. Equipment, Tooling & Fixtures
1. **Precision Vacuum Chuck & Fixturing Stage**: Kinematic mechanical stage with multi-axis micrometer tilt adjustment ($\theta_x, \theta_y, z$).
2. **Spectroscopic Ellipsometer**: Variable-angle optical metrology tool capable of sub-angstrom EOT thickness mapping.
3. **C-V Metrology System & Probe Card**: High-frequency LCR meter (1 MHz testing) and quasi-static electrometer/picoammeter unit.
4. **MOS Dummy Coupons**: P-type (100) Si substrate with ~3.5 nm dry thermal SiO2 gate oxide, sputtered circular Al dots (diameters: 200 µm, 500 µm, 1000 µm), and backside Au or Al ohmic metallization.

---

### 3. Step-by-Step Procedure

```text
┌────────────────────────┐
│                        │
│  Tooling Stage Mount   │
│     & Vacuum Lock      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      Multi-Point       │
│  Auto-Collimator Tilt  │
│      Calibration       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Spectroscopic      │
│      Ellipsometry      │
│   Baseline on 3.5nm    │
│          SiO2          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Backside Contact &   │
│   Probe Card Pinning   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  High-Frequency 1 MHz  │
│   & Quasi-Static C-V   │
│     Qualification      │
│                        │
└────────────────────────┘
```

#### Step 1: Mechanical Mounting & Substrate Seating
1. Inspect the backside of the P-type (100) Si MOS dummy coupon to ensure the Au or Al ohmic contact layer is free from particulates and oxidation.
2. Place coupon onto the precision gold-plated vacuum stage chuck. Engage stage vacuum hold-down (> 70 kPa). Ensure thermal and electrical baseline continuity.

#### Step 2: Multi-Point Tilt Calibration & Optical Normalization
1. Position the optical head / auto-collimator at normal incidence across 5 distributed fiducial points (Center, North, South, East, West).
2. Adjust stage differential micrometer screws ($\theta_x, \theta_y$) until angular pitch and roll deviations across all five points are within tolerance ($\Delta \theta \le \pm 0.01^\circ$).
3. Zero optical beam path height ($z$-axis) to align the focal plane with the 3.5 nm SiO2 surface.

#### Step 3: Spectroscopic Ellipsometry Thickness Qualification
1. Measure multi-wavelength optical phase change ($\Psi, \Delta$) across the test coupon at nominal angle of incidence ($70^\circ$–$75^\circ$).
2. Fit optical constants using an established P-Si / SiO2 Cauchy or Sellmeier optical model.
3. Quantify physical oxide thickness $t_{\text{ox}}$ ensuring adherence to the target ~3.5 nm nominal gate oxide line within $\pm 0.1\text{ nm}$ uncertainty.

#### Step 4: Electrical Probing & Backside Contact Interconnect
1. Ground the gold-plated vacuum chuck connected to the wafer backside Au/Al contact.
2. Under stereomicroscope guidance, lower the micro-probe pin onto the designated Al gate dot (selecting from 200 µm, 500 µm, or 1000 µm diameter patterns).
3. Confirm contact resistance and zero mechanical penetration of the thin 3.5 nm oxide dielectric layer.

#### Step 5: High-Frequency (1 MHz) & Quasi-Static C-V Characterization
1. Apply gate voltage sweep $V_G$ from accumulation ($V_G < V_{\text{fb}}$) through depletion ($V_{\text{fb}} < V_G < V_T$) to inversion ($V_G > V_T$).
2. Record high-frequency (1 MHz) capacitance:
   - Verify accumulation capacitance saturation:
     $$C_{\text{ox}} = \frac{\epsilon_{\text{ox}} \epsilon_0 \cdot \text{Area}}{t_{\text{ox}}}$$
   - Extract physical oxide thickness $t_{\text{ox}}$ to cross-verify optical ellipsometry.
3. Record quasi-static C-V response:
   - Observe low-frequency recovery to $C_{\text{ox}}$ in the inversion region ($V_G > V_T$).
4. Compute interface trap density ($D_{\text{it}}$) from high-low frequency capacitance delta across the depletion region.

---

### 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Tolerance / Window | Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Physical Gate Oxide Thickness ($t_{\text{ox}}$)** | 3.5 | $\pm 0.1$ | nm | Spectroscopic Ellipsometry / 1 MHz Accumulation $C_{\text{ox}}$ |
| **Multi-Point Stage Angular Planarity ($\Delta \theta$)** | 0.00 | $\le \pm 0.01$ | deg ($^\circ$) | 5-Point Optical Auto-collimator / Tilt Sensor |
| **High-Frequency Testing Signal** | 1.0 | Nominal | MHz | Precision LCR Meter C-V Profiling |
| **Top Electrode Gate Dot Diameter** | 200, 500, 1000 | Nominal shadow-mask | µm | Optical Metrology / Inspection Micrometer |

---

### 5. Context Literature Citations
- **Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction**:
  - Validates MOSCAP diagnostic structure: Al circular gate dots (200 µm, 500 µm, 1000 µm) sputtered on thermally grown gate oxide (3.5 nm to 25 nm) on P-type (100) Si with Au/Al backside contact.
  - Confirms High-Frequency (1 MHz) and Quasi-Static C-V methodology, accumulation capacitance relation $C_{\text{ox}} = (\epsilon_{\text{ox}} \epsilon_0 \cdot \text{Area}) / t_{\text{ox}}$, and thickness extraction precision within $\pm 0.1\text{ nm}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - Validates gate dielectric thermal growth at 850°C–900°C dry oxidation with ~3.5 nm physical thickness and stacked capacitor high-k EOT of 3 to 4 nm.

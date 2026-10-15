# Standard Operating Procedure (SOP)
## CD-SEM Electron Optical Column Alignment & Landing Energy Beam Calibration

- **Document ID**: `SOP-MET-CDSEM-180NM-001`
- **Revision**: `v1.0`
- **Status**: Released / Effective
- **Domain**: DRAM Foundation VN — 180nm Open-Source DRAM Chip / MPW Tapeout Metrology
- **Action Type**: Make

---

### 1. Scope & Objective
This SOP defines the setup, alignment, and landing energy calibration procedure for the in-line Critical Dimension Scanning Electron Microscope (CD-SEM). It ensures non-destructive, charge-neutral, sub-nanometer repeatable dimensional inspection of 180nm access transistor gates, 150nm poly gate lengths, and 170nm contact holes.

---

### 2. Physical & Architectural Context
- **Transistor Geometry**: Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
- **PDK Rules (SKY130 / 180nm MPW)**: Minimum poly gate length $= 150\text{ nm}$ ($0.15\ \mu\text{m}$), minimum poly gate spacing $= 210\text{ nm}$ ($0.21\ \mu\text{m}$), minimum contact hole dimension $= 170\text{ nm} \times 170\text{ nm}$ ($0.17\ \mu\text{m} \times 0.17\ \mu\text{m}$).
- **Manufacturing Grid**: $0.005\ \mu\text{m}$ ($5\text{ nm}$) resolution.
- **Overlay Budget**: Gate poly to active diffusion overlay error $\le 35\text{ nm}$.

---

### 3. Step-by-Step Operating Procedure

1. **Load Lock & High Vacuum Stabilization**:
   - Transfer calibration/pattern wafer onto laser-interferometer stage.
   - Verify column vacuum chamber pressure $< 5 \times 10^{-7}\text{ Torr}$ before opening column gate valve.
2. **Gun Alignment & Field Emission Current Tuning**:
   - Power Cold Field Emission (CFE) / Schottky emitter. Set primary extraction voltage.
   - Perform electron gun tilt and gun shift centering to align emission centroid with optical axis.
3. **Condenser & Objective Aperture Centering**:
   - Select real/virtual objective aperture. Modulate lens focal current (wobbler mode).
   - Adjust X/Y mechanical and electromagnetic beam deflection coils until image translation/breathing during focus modulation is eliminated.
4. **Stigmation & Astigmatism Correction**:
   - Drive stage to a dedicated pitch calibration grid (Au-on-C or etched Si pitch standard).
   - Adjust octupole stigmators (stig-X and stig-Y) to eliminate directional elongation/blur at over-focus and under-focus.
5. **Landing Energy ($E_L$) & Stage Retardation Calibration**:
   - Apply wafer stage retarding bias ($V_{\text{stage}}$) relative to primary electron beam acceleration ($V_{\text{acc}}$) such that:
     $$E_L = e \cdot (V_{\text{acc}} - V_{\text{stage}})$$
   - Tune $E_L$ to the charge balance point ($E_2 \approx 500\text{ eV} - 800\text{ eV}$) where total secondary electron emission yield $\sigma + \delta \approx 1$.
   - Confirm surface potential stabilization across sensitive gate oxide ($3.5\text{ nm}$ physical $\text{SiO}_2$) and dielectric layers.
6. **Magnification & Scan Linearity Verification**:
   - Scan standardized reference pitch structures aligned to the $5\text{ nm}$ physical placement grid.
   - Calibrate scan generators to ensure CD measurement linearity within $\pm 0.5\%$.
7. **Automated Metrology Recipe Execution**:
   - Execute recipe to measure access gate lengths ($L = 180\text{ nm}$ and nominal $150\text{ nm}$), contact holes ($170\text{ nm}$), and gate-to-diffusion overlay ($\le 35\text{ nm}$).

---

### 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Unit | Verification Method |
| :--- | :--- | :--- | :--- |
| **Minimum Poly Gate Length CD** | $150.0 \pm 1.5$ | $\text{nm}$ | In-line 16-scan edge-detection algorithm |
| **Contact Hole Dimension ($X \times Y$)** | $170.0 \times 170.0 \pm 2.0$ | $\text{nm}$ | 2D elliptical fit algorithm |
| **Poly Gate to Active Overlay Error** | $\le 35.0$ | $\text{nm}$ | Multi-point optical/CD-SEM overlay algorithm |
| **Physical Placement Grid Alignment** | $5.0$ (snap-to-grid error $= 0.0$) | $\text{nm}$ | Stage laser interferometer coordinate mapping |

---

### 5. Context Literature Citations
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
- **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**: Manufacturing grid resolution $= 0.005\ \mu\text{m}$ ($5\text{ nm}$); minimum poly gate length $= 0.15\ \mu\text{m}$ ($150\text{ nm}$); minimum poly gate spacing $= 0.21\ \mu\text{m}$; minimum contact hole $= 0.17\ \mu\text{m} \times 0.17\ \mu\text{m}$ ($170\text{ nm}$); overlay error budget $\le 35\text{ nm}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: Physical gate oxide thickness $\approx 3.5\text{ nm}$; cell pitch $360\text{ nm} - 400\text{ nm}$.

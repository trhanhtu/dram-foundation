# Standard Operating Procedure (SOP)
## Task: MOS Capacitor Shadow Mask Dot Profilometry and Edge Taper Metrology
- **Module**: Metrology / Characterization & Process Verification
- **Platform**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Hierarchy Path**: Architecture & Integration > 180nm Dry Gate Oxide Growth (3.5 nm) > Spectroscopic Ellipsometry and C-V Oxide Thickness & Interface Metrology > MOS Capacitor Shadow Mask Metallization for Electrical Test Structures > Process Parameter Benchmarking for MOS Capacitor Shadow Mask Metallization for Electrical Test Structures > MOS Dot Profile Metrology and Forming Gas Anneal Parameter Verification > MOS Capacitor Shadow Mask Dot Profilometry and Edge Taper Metrology
- **Generation**: Gen 2 (µm) | **Action Type**: Make

---

### 1. Process Overview & Objective
Establish a standardized high-resolution surface profilometry and edge taper metrology protocol for deposited metal (Al/Ti/poly-Si) MOS capacitor top electrode dots fabricated via stencil shadow mask evaporation/sputtering. The objective is to accurately extract physical dot film thickness, step height, center plateau roughness, and penumbra edge taper width ($\Delta x$) / slope. This prevents fringe-field capacitance distortion and enables accurate area normalization for high-frequency C-V, EOT extraction (baseline $\sim 3.5\text{ nm}$ dry oxide), and interface defect state evaluation.

---

### 2. Workflow Diagram (ASCII / Unicode)

```text
┌────────────────────────┐
│                        │
│  Load Wafer and Align  │
│       Dot Array        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Stylus Profilometry   │
│       Step Scan        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Extract Peak Step    │
│    Height and Film     │
│       Thickness        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Quantify Penumbra    │
│  Edge Taper Width and  │
│         Slope          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       Acceptance       │
│  Verification and C-V  │
│          Gate          │
│                        │
└────────────────────────┘
```

---

### 3. Step-by-Step Operating Procedure

1. **Substrate Handling & Chuck Loading**:
   - Transfer the metallized test coupon/wafer (featuring shadow-mask evaporated top contact dots on $\sim 3.5\text{ nm}$ dry gate oxide) from the cleanroom transport box onto the anti-vibration vacuum chuck of the high-resolution stylus / optical profilometer.
   - Engage vacuum clamp ($> 70\text{ kPa}$) and visually orient the primary flat/notch parallel to the X-axis stage travel.

2. **Optical Navigation & Dot Array Alignment**:
   - Utilize the top-down alignment camera to locate the target Gen 2 circular dot array (nominal pad diameters $150\text{ }\mu\text{m}$ to $500\text{ }\mu\text{m}$ on a $1.0\text{ mm}$ pitch).
   - Establish orthogonal scan axes $(X, Y)$ across the central axis of the dot to ensure the stylus traverses directly across the maximum dot diameter ($D_{\max}$).

3. **Stylus Profilometry Scan Setup & Execution**:
   - Select a low-force micro-stylus tip (radius $r = 2.0\text{ }\mu\text{m}$ to $2.5\text{ }\mu\text{m}$, diamond tip) calibrated to a stylus tracking force $\le 1.0\text{ mg}$ ($9.8\text{ }\mu\text{N}$) to avoid scratching the deposited metal film or punching through the underlying ultra-thin gate oxide.
   - Program a scan length spanning $L_{\text{scan}} = D_{\text{nom}} + 200\text{ }\mu\text{m}$ (providing $100\text{ }\mu\text{m}$ baseline on bare oxide on both sides) at a traverse speed $v_{\text{scan}} \le 10\text{ }\mu\text{m/s}$ with vertical sampling resolution $\le 0.1\text{ nm}$.
   - Execute bilateral linear trace passes (orthogonal $0^\circ$ and $90^\circ$) across 5 benchmark locations (Center, North, South, East, West) on the coupon.

4. **Step Height & Top Plateau Profilometry Extraction**:
   - Level the raw profilometry trace using two linear baseline fits on the unmetallized dry gate oxide region flanking the dot.
   - Extract the nominal metal step height ($h_{\text{metal}}$) across the central flat plateau (inner $50\%$ radius of the dot).
   - Calculate plateau surface micro-roughness ($R_a$ and $R_q$) across the top plateau.

5. **Penumbra Edge Taper Metrology & Geometric Deconvolution**:
   - Quantify the deposition penumbra region at the dot perimeter induced by shadow-mask standoff gap.
   - Define the edge taper transition width $\Delta x_{10-90}$ as the lateral distance between the $10\%$ and $90\%$ normalized step height coordinates:
     $$\Delta x_{10-90} = x(0.9 \cdot h_{\text{metal}}) - x(0.1 \cdot h_{\text{metal}})$$
   - Calculate the edge taper sidewall slope $\theta_{\text{taper}} = \arctan(h_{\text{metal}} / \Delta x_{10-90})$.
   - Determine the effective electrical capacitor dot area $A_{\text{eff}}$ by integrating the radial profile to prevent systematic capacitance overestimation during C-V analysis.

6. **Defect Screening, Data Logging, & C-V Handover**:
   - Inspect profiles for shadowing asymmetry, lift-off burrs, or mask clamping leakage artifacts.
   - Record metrology parameters into the fab MES database. Pass verified coupons to the high-frequency C-V probe station for accumulation capacitance and EOT extraction.

---

### 4. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Target Value | Physical Unit | Measurement Tool / Method |
| :--- | :--- | :--- | :--- |
| **Top Metal Step Height ($h_{\text{metal}}$)** | $100.0 \pm 5.0$ | $\text{nm}$ | Calibrated stylus profilometer / optical step profiler |
| **Penumbra Edge Taper Width ($\Delta x_{10-90}$)** | $\le 12.0$ | $\mu\text{m}$ | Linear profilometric step edge deconvolution |
| **Center Plateau Roughness ($R_a$)** | $\le 2.5$ | $\text{nm}$ | Micro-stylus trace across inner 50% dot plateau |
| **Bilateral Dot Diameter Symmetry ($D_X / D_Y$)** | $1.00 \pm 0.02$ | Dimensionless ratio | Orthogonal dual-axis profilometry line scans |

---

### 5. Verified Literature Citations

- **Gate Dielectric Reference**: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*
  - *"Gate dielectric is thermally grown silicon dioxide (SiO2) at 850°C-900°C dry oxidation with ~3.5 nm physical thickness."*
  - *"In 180nm nodes, stacked capacitors (Crown or Cylinder type) utilize silicon nitride (Si3N4) or tantalum pentoxide (Ta2O5) high-k dielectrics with equivalent oxide thickness (EOT) around 3 to 4 nm."*
- **Metrology & Dielectric Modeling Precision**: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
  - *"Physical Principle: Measures the change in light polarization upon reflection from a thin film interface, quantified by angles Psi and Delta. Fundamental Equation: rho = r_p / r_s = tan(Psi) * exp(i * Delta)... Measurement Precision: Dry gate oxide (3.5 nm) measured with sub-Angstrom precision (±0.05 nm)."*
- **Capacitance & Leakage Constraints**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
  - *"Capacitance Budget: Minimum 28 fF per cell ensures noise immunity against alpha-particle soft errors and bitline coupling capacitance. Leakage Current Target: Sub-threshold and junction leakage must be kept below 1 fA/cell at 85°C to achieve refresh interval."*

# SOP: MOS Capacitor Test Chip Layout & Probe Pad Mask Preparation

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Action Type**: Make
- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm Dry Gate Oxide Growth (3.5 nm) [Thermal Processing] > Dry Thermal Oxidation Recipe Execution (850°C-900°C, 3.5 nm SiO2) [Thermal Oxidation] > Spectroscopic Ellipsometry and C-V Gate Oxide Metrology (3.5nm EOT & Dit Characterization) [Metrology] > Quality Acceptance & Metrology Protocol for Spectroscopic Ellipsometry and C-V Gate Oxide Metrology (3.5nm EOT & Dit Characterization) [Quality Assurance] > MOS Capacitor Test Structure Calibration & Ellipsometer Recipe Standardization [Metrology] > MOS Capacitor Test Chip Layout & Probe Pad Mask Preparation [Circuit Design]

---

## 1. Overview & Rationale

In the DRAM Foundation VN 180nm technology node, access transistors require a gate length $L = 180\text{ nm}$ and width $W = 220\text{ nm}$ within an $8F^2$ or $6F^2$ cell layout, with wordline/bitline pitch spanning $360\text{ nm}–400\text{ nm}$. The gate dielectric is formed by dry thermal oxidation at $850^\circ\text{C}–900^\circ\text{C}$ to yield a physical thickness of $3.5\text{ nm}$ (3.5 nm to 4.0 nm).

To accurately extract Equivalent Oxide Thickness ($\text{EOT} \approx 3.5\text{ nm}$), interface trap density ($D_{\text{it}} < 10^{10}\text{ cm}^{-2}\text{eV}^{-1}$), oxide breakdown field ($E_{\text{bd}} > 10\text{ MV/cm}$), and sub-threshold leakage, dedicated Metal-Oxide-Semiconductor (MOS) capacitor test structures and probe pads must be laid out and converted into photolithography / shadow mask data. At Gen 2 ($\mu\text{m}$) test coupon scale, probe pad geometry, guard-ring structures, and array pitch must balance stray fringing capacitance against micro-probing requirements.

```text
┌────────────────────────────────────────────────────────┐
│ MOS Capacitor Layout Generation (GDSII / OASIS)        │
│ Test Dots (100 µm - 500 µm) + Kelvin Guard Rings       │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Design Rule Check (DRC) & Optical Pattern Verification │
│ Pitch: 1000 µm, Probe Pad Clearances ≥ 80 µm × 80 µm   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Optical/Shadow Mask Data Prep & Laser Photoplotting    │
│ Cr-on-Glass / Precision Stencil Tooling & Alignment    │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ CD Metrology, Defect Inspection & Mask Sign-off        │
│ Ready for Gate Oxide Deposition & C-V Profiling        │
└────────────────────────────────────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Test Structure CAD Layout Synthesis & Sizing
1. Launch CAD tool (KLayout / OpenLane layout editor) configured with the 180nm Gen 2 ($\mu\text{m}$) design kit.
2. Instantiate graduated MOS capacitor test arrays to enable accurate area-to-perimeter capacitance separation:
   - Large area circular/square capacitors: $500\text{ }\mu\text{m} \times 500\text{ }\mu\text{m}$ and $200\text{ }\mu\text{m} \times 200\text{ }\mu\text{m}$ (for bulk accumulation capacitance $C_{\text{ox}}$ and EOT extraction).
   - Medium and perimeter-intensive test structures: $100\text{ }\mu\text{m} \times 100\text{ }\mu\text{m}$ and comb/finger patterns (for fringing capacitance de-embedding).
3. Design integrated p+ / n+ substrate guard rings with minimum $10\text{ }\mu\text{m}$ separation around test pads to suppress surface inversion channel leakage and lateral carrier drift during high-frequency (100 kHz - 1 MHz) and quasi-static C-V profiling.
4. Define standard RF / DC micro-probe pad geometries ($80\text{ }\mu\text{m} \times 80\text{ }\mu\text{m}$ minimum contact area on a $150\text{ }\mu\text{m}$ to $1000\text{ }\mu\text{m}$ pitch grid) compatible with standard probe card needles and picoprobe tips.

### Step 2: Alignment Fiduciaries & Metrology Target Placement
1. Embed standard split-field optical alignment marks (crosshair / Vernier key targets) in the peripheral scribe lanes and four coupon corners to interface with dual-camera split-field mask aligner optics.
2. Insert large-area bare oxide witness pads ($2.0\text{ mm} \times 2.0\text{ mm}$) adjacent to capacitor arrays reserved for multi-angle Spectroscopic Ellipsometry (SE) beam spot placement without metal occlusion.
3. Incorporate darkfield/brightfield CD test bars ($10\text{ }\mu\text{m}$, $20\text{ }\mu\text{m}$, $50\text{ }\mu\text{m}$) for post-lithography optical critical dimension verification.

### Step 3: Design Rule Check (DRC) & Data Fracturing
1. Run automated DRC deck against Gen 2 design rules:
   - Validate probe pad clearance $\ge 20\text{ }\mu\text{m}$ to prevent shorting during probe needle skate.
   - Validate guard-ring continuity and absence of floating polysilicon/metal islands.
2. Perform Boolean layer operations to separate top-electrode metal (Gate Metal / Al / Poly-Si), dielectric open windows, and back-side substrate contact layers.
3. Fracture layout polygons into MEBES / OASIS mask write stream files. Apply laser/e-beam proximity effect correction (PEC) and optical sizing biases ($\pm 0.05\text{ }\mu\text{m}$).

### Step 4: Mask Fabrication Preparation & Tooling Setup
1. Transfer fractured mask data to the optical mask photoplotter / laser direct imaging (LDI) system.
2. Select 5-inch or 6-inch soda-lime or quartz blank pre-coated with $100\text{ nm}$ low-reflective Chromium and positive photoresist (or calibrate laser micro-machining CNC stage for foil shadow mask tooling).
3. Initialize workpiece stage coordinate system; calibrate laser beam focus and XY interferometer stage travel accuracy.

### Step 5: Photoplotting / Mask Exposure & Wet Processing
1. Execute laser exposure recipe at calibrated optical dose ($405\text{ nm}$ laser source, dose uniformity $<\pm 2\%$).
2. Develop exposed resist in standard TMAH developer bath for $60\text{ s} \pm 2\text{ s}$ with automated agitation; rinse in $18.2\text{ M}\Omega\cdot\text{cm}$ DI water and spin dry.
3. Wet etch exposed Chromium layer in standard perchloric acid / ceric ammonium nitrate chrome etchant until clear endpoints are achieved; strip remaining photoresist.

### Step 6: Metrology, Inspection & Mask Sign-off
1. Verify Critical Dimension (CD) of capacitor dot diameters across 5 die locations using calibrated optical coordinate metrology.
2. Inspect for pinholes, bridge defects, and chrome voids under transmission darkfield microscopy (zero defects $\ge 2\text{ }\mu\text{m}$ allowed in active capacitor dot zones).
3. Pack approved mask plates in antistatic, cleanroom-grade polycarbonate canisters under continuous dry $\text{N}_2$ purge.

---

## 3. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Target Value | Physical Unit | Tolerance / Constraint | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Probe Pad Critical Dimension (CD)** | $100.0$ | $\mu\text{m}$ | $\pm 2.0\text{ }\mu\text{m}$ | Automated Optical Coordinate Measuring System |
| **Mask Pattern Feature Pitch** | $1000.0$ | $\mu\text{m}$ | $\pm 0.5\text{ }\mu\text{m}$ laser stage travel | Laser Interferometric Stage Metrology |
| **Critical Defect Density (Active Zone)** | $0$ | $\text{defects/cm}^2$ | Defect size threshold $\ge 2.0\text{ }\mu\text{m}$ | Automated Optical Mask Inspection / Darkfield Microscopy |
| **Mask In-Plane Overlay Registration Error** | $\le 0.50$ | $\mu\text{m}$ | Vector error across $100\text{ mm}$ field | Scribe-line Vernier & Optical Target Metrology |

---

## 4. Verified Literature Citations

- **Gate Dielectric Thermal Oxidation & Thickness**: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*
  - *"Gate dielectric is thermally grown silicon dioxide (SiO2) at 850°C-900°C dry oxidation with ~3.5 nm physical thickness."*
  - Stacked capacitor EOT around 3 to 4 nm; cell capacitance minimum 25 to 30 fF per cell ensuring data retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
- **Cell Geometry & Leakage Constraints**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
  - Unit cell access transistor length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
  - Capacitance budget $\ge 28\text{ fF/cell}$; sub-threshold and junction leakage target $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **Oxidation Kinetics & Breakdown Standards**: *Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace*
  - Dry oxidation linear-parabolic kinetics: $x_0^2 + A x_0 = B(t + \tau)$.
  - Dry thermal oxidation produces dense gate oxide with breakdown field $E_{\text{bd}} > 10\text{ MV/cm}$ and minimal interface trap density $D_{\text{it}} < 10^{10}\text{ cm}^{-2}\text{eV}^{-1}$, targeting $3.5\text{ nm}$ to $4.0\text{ nm}$ thickness for 180nm gate dielectric.

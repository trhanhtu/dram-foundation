# SOP: Multi-Site Sessile Drop Dispense & Contact Angle Transient Profile Capture

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 1 (mm)
- **Action Type**: Make
- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm Dry Gate Oxide Growth (3.5 nm) [Thermal Processing] > Pre-Oxidation RCA Clean and In-Situ HF Dip Surface Preparation [Wet Chemistry] > Post-Clean Contact Angle & Surface Particle/Metallic Defect Metrology [Metrology] > Goniometer Water Contact Angle Metrology for HF-Last Hydrophobicity & Surface Passivation Verification [Metrology] > Multi-Site Sessile Drop Dispense & Contact Angle Transient Profile Capture [Metrology]

---

## 1. Overview & Rationale

In the 180nm DRAM fabrication architecture, cell access transistors require a gate length $L = 180\text{ nm}$ and active width $W = 220\text{ nm}$, with bitline and wordline pitch scaled between $360\text{ nm}$ and $400\text{ nm}$. The gate dielectric consists of thermally grown silicon dioxide ($\text{SiO}_2$) with a nominal physical thickness target of $3.5\text{ nm}$, grown via dry thermal oxidation at $850^\circ\text{C}–900^\circ\text{C}$ to maintain cell leakage below $1\text{ fA/cell}$ at $85^\circ\text{C}$.

Prior to furnace loading, wafers undergo an RCA wet clean with an in-situ dilute hydrofluoric acid (DHF) dip to strip native/chemical oxides and establish full hydrogen passivation ($\text{Si-H}$ bonding). Complete hydrogen passivation renders the bare silicon surface hydrophobic. Any localized residual oxide patches, ionic contaminants, or micro-roughness degrade dry gate oxide nucleation uniformity and lead to gate dielectric breakdown degradation.

This Standard Operating Procedure (SOP) governs the automated multi-site sessile drop dispense and transient profile capture on a high-speed optical goniometer. By recording the dynamic water contact angle ($\theta(t)$) over a multi-second settling window across designated wafer monitor sites, this metrology validates uniform surface hydrophobicity and passivation integrity prior to loading wafers into the $850^\circ\text{C}–900^\circ\text{C}$ oxidation furnace.

```text
┌─────────────────────────────────────────────────────────┐
│ Post-HF Dip Wafer Ingestion & Substrate Pre-Alignment   │
│ (Vacuum Chucking, Edge Exclusion ≥ 5 mm)                │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│ Automated Multi-Site Coordinate Step & Positioning     │
│ (Center, North, South, East, West Wafer Sites)          │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│ Precision Sessile Micro-Droplet Dispense                │
│ (1.00 µL ± 0.10 µL Ultrapure 18.2 MΩ·cm DI H2O)         │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│ High-Speed Telecentric Video Capture & Baseline Fit     │
│ (Young-Laplace Fitting, Transient θ(t) from t = 0 to 5s)│
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│ Site Droplet Aspiration, N2 Purge & Lot Disposition     │
│ (Pass: θ ≥ 70.0°, Drift ≤ 0.50°/s -> Gate Oxide Queue)  │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Environmental Conditioning and Tool Calibration
1. Confirm the goniometer environmental chamber is held at $21.0^\circ\text{C} \pm 0.5^\circ\text{C}$ and relative humidity at $40\% \pm 3\%$ under Class 1 laminar flow air.
2. Verify the fluid delivery system is primed with ultrapure deionized (DI) water ($18.2\text{ M}\Omega\cdot\text{cm}$ resistivity at $25^\circ\text{C}$, passed through a point-of-use $0.05\text{ }\mu\text{m}$ filter).
3. Perform optical magnification and tilt calibration:
   - Position a certified spherical optical calibration artifact (diameter $3.000\text{ mm} \pm 0.001\text{ mm}$) in the optical field of view.
   - Adjust the telecentric lens illumination and camera focus until the sphere boundary shows sharp contrast with zero optical distortion.
   - Run the automated pixel-to-millimeter scaling routine (calibration tolerance: $\pm 0.002\text{ mm/pixel}$).

### Step 2: Wafer Loading and Multi-Site Coordinate Registration
1. Transfer the post-clean wafer from the sealed $\text{N}_2$-purged transfer pod onto the automated goniometer vacuum stage using an edge-grip robotic end-effector (edge exclusion zone: $\ge 5\text{ mm}$).
2. Perform optical notch/flat detection to align the wafer coordinates to the stage frame.
3. Load the multi-site recipe defining 5 standard metrology coordinates across the 200 mm wafer:
   - Site 1 (Center): $(X = 0\text{ mm}, Y = 0\text{ mm})$.
   - Site 2 (North): $(X = 0\text{ mm}, Y = +70\text{ mm})$.
   - Site 3 (South): $(X = 0\text{ mm}, Y = -70\text{ mm})$.
   - Site 4 (East): $(X = +70\text{ mm}, Y = 0\text{ mm})$.
   - Site 5 (West): $(X = -70\text{ mm}, Y = 0\text{ mm})$.

### Step 3: Precision Sessile Drop Dispense
1. Drive the stage to move the designated site under the dispensing tip (PTFE-coated 30-gauge stainless steel needle, OD $\approx 0.31\text{ mm}$).
2. Lower the dispensing tip to a clearance height of $1.50\text{ mm} \pm 0.10\text{ mm}$ above the silicon surface.
3. Actuate the micro-stepping syringe pump to dispense a droplet volume of $1.00\text{ }\mu\text{L} \pm 0.10\text{ }\mu\text{L}$ at a controlled dosing rate of $0.50\text{ }\mu\text{L/s}$.
4. Touch off the droplet gently to touch the silicon surface, then retract the needle tip vertically by $+3.00\text{ mm}$ at $2.0\text{ mm/s}$ without inducing mechanical vibration or droplet pinning distortion.

### Step 4: High-Speed Transient Profile Video Capture & Young-Laplace Fitting
1. Trigger the high-speed monochrome camera (frame rate $\ge 60\text{ fps}$, resolution $\ge 1280 \times 1024$) synchronously with droplet detachment ($t = 0\text{ s}$).
2. Record the continuous transient shadowgraph sequence for $5.0\text{ s}$.
3. Execute the automated edge-detection and Young-Laplace contour-fitting algorithm on each captured frame:
   - Identify the solid-liquid baseline interface.
   - Fit the droplet profile to determine the left angle ($\theta_L$) and right angle ($\theta_R$), computing the mean contact angle $\theta(t) = (\theta_L + \theta_R)/2$.
   - Extract the static settled contact angle $\theta_0$ at $t = 1.0\text{ s}$ post-deposition.
   - Calculate the transient contact angle drift rate:
     $$\left|\frac{d\theta}{dt}\right| = \frac{|\theta(5.0\text{ s}) - \theta(1.0\text{ s})|}{4.0\text{ s}}$$
4. Flag any profile asymmetry where $|\theta_L - \theta_R| > 2.0^\circ$ as a baseline anomaly or localized particulate defect.

### Step 5: Post-Measurement Droplet Aspiration and Site Purge
1. Position the vacuum aspiration micro-nozzle over the dispensed droplet and evacuate the water droplet to prevent liquid residue or drying stain formation.
2. Apply a dry, filtered $\text{N}_2$ micro-purge jet ($0.2\text{ bar}$, $2.0\text{ s}$) over the test site.
3. Index the stage to the subsequent test coordinates and repeat Steps 3 through 5 until all 5 sites are recorded.

### Step 6: Lot Disposition & Furnace Transfer Queue Execution
1. Calculate the across-wafer average contact angle $\bar{\theta}$ and contact angle range ($\Delta\theta = \theta_{\max} - \theta_{\min}$).
2. **PASS Disposition**:
   - If $\theta_0 \ge 70.0^\circ$ at all sites, $|d\theta/dt| \le 0.50^\circ/\text{s}$, and across-wafer range $\Delta\theta \le 5.0^\circ$:
   - Mark the lot as fully passivated hydrophobic silicon and release for transfer to the quartz oxidation furnace for $3.5\text{ nm}$ dry $\text{SiO}_2$ thermal growth ($850^\circ\text{C}–900^\circ\text{C}$).
   - Enforce remaining clean-to-furnace queue time $t_{\text{queue}} \le 60\text{ min}$.
3. **FAIL Disposition**:
   - If $\theta_0 < 70.0^\circ$ or $|d\theta/dt| > 0.50^\circ/\text{s}$, hold the cassette. Surface has residual hydrophilic chemical oxide or incomplete HF passivation. Route lot to wet bench for DHF re-dip.

---

## 3. Machine-Measurable Acceptance Criteria

| Metric / Parameter | Target Value | Physical Units | Tolerance / Constraint | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Initial Sessile Drop Contact Angle ($\theta_0$)** | $\ge 70.0$ | $\text{degrees } (^\circ)$ | Minimum acceptable hydrophobic threshold (nominal $75.0^\circ–85.0^\circ$) at $t = 1.0\text{ s}$ | Automated optical goniometer Young-Laplace fit |
| **Transient Contact Angle Drift Rate ($|d\theta/dt|$)** | $\le 0.50$ | $\text{degrees / second } (^\circ/\text{s})$ | Maximum allowable dynamic relaxation rate between $t = 1.0\text{ s}$ and $t = 5.0\text{ s}$ | Frame-by-frame transient video capture ($\ge 60\text{ fps}$) |
| **Across-Wafer Contact Angle Uniformity Range ($\Delta\theta$)** | $\le 5.0$ | $\text{degrees } (^\circ)$ | $\theta_{\max} - \theta_{\min}$ across 5 monitor sites (Center, N, S, E, W) | Multi-site coordinate automated map |
| **Dispense Droplet Volume Precision ($V_{\text{drop}}$)** | $1.00$ | $\mu\text{L}$ | $\pm 0.10\text{ }\mu\text{L}$ ($18.2\text{ M}\Omega\cdot\text{cm}$ DI $\text{H}_2\text{O}$ at $25^\circ\text{C}$) | Precision micro-stepping syringe pump calibration |

---

## 4. Context & Literature Citations

- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Access transistor channel dimensions ($L = 180\text{ nm}$, $W = 220\text{ nm}$).
  - Cell target leakage current $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$ and storage capacitance budget $\ge 28\text{ fF/cell}$, requiring atomic-scale gate oxide interface control.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - Gate dielectric physical thickness target of $3.5\text{ nm}$ grown via dry thermal oxidation at $850^\circ\text{C}–900^\circ\text{C}$.
  - Bitline and wordline pitch specifications ($360\text{ nm}$ to $400\text{ nm}$).
- **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
  - Physical placement grid resolution of $0.005\text{ }\mu\text{m}$ ($5\text{ nm}$) and active gate length scaling requirements ($150\text{ nm}$ poly gate length, $0.15\text{ }\mu\text{m}$ active diffusion width, overlay error $\le 35\text{ nm}$).

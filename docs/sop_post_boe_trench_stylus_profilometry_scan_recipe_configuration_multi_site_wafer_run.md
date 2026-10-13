# Standard Operating Procedure (SOP): Post-BOE Trench Stylus Profilometry Scan Recipe Configuration and Multi-Site Wafer Run

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 1 (mm)
- **Action Type**: Buy
- **Hierarchy Path**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > Buffered Oxide Etch (BOE 6:1) SiO2 Patterning [Chemical Processing] > Post-Etch Spectroscopic Ellipsometry & Profilometry Metrology Inspection [Metrology] > Stylus Profilometry Step-Height & Etch Trench Uniformity Characterization [Metrology] > Post-BOE Etch Trench Step-Height Profilometry Recipe Setup and Scan Execution [Metrology] > Post-BOE Trench Stylus Profilometry Scan Recipe Configuration and Multi-Site Wafer Run [Metrology]

---

## 1. Scope & Physical Principles

This Standard Operating Procedure (SOP) governs the recipe setup, multi-site stage coordinate programming, and automated execution of high-resolution stylus profilometry scans across 100mm patterned wafers following Buffered Oxide Etch (BOE 6:1) processing. 

In the 180nm DRAM integration flow (utilizing access transistors with channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$, and stacked capacitor topologies requiring a strict leakage limit $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ and $C_s \ge 28\text{ fF}$), wet BOE patterning opens critical isolation boundaries, scribe line test trenches, and Gen 1 (mm-scale die perimeter) $100\text{ }\mu\text{m} \times 100\text{ }\mu\text{m}$ contact/bonding pad openings. 

Accurate step-height stylus profiling validates:
1. Complete oxide clearance down to the silicon substrate without micro-trenching.
2. Wet etch selectivity and post-etch step uniformity across center, middle, and edge wafer zones.
3. Chuck mechanical parallelism and planar baseline calibration ($< 1\text{ }\mu\text{m}$ across the 100mm substrate).

```text
┌────────────────────────────────────────────────────────┐
│  Wafer Vacuum Loading & Chuck Parallelism Calibration  │
│  (Verify substrate parallelism < 1 µm across 100mm)    │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Optical Alignment & Multi-Site Scribe Grid Fiducials  │
│  (Camera with 5x/10x/20x zoom; align 100x100 µm pads)  │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Stylus Recipe Setup & Low-Force Tracking Parameters   │
│  (Program scan speed, length, diamond stylus tracking) │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Multi-Site Automated Run & Step-Height Data Logging   │
│  (Center, North, South, East, West multi-die profile)  │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Acceptance Verification & Statistical Lot Disposition │
│  (Pass / Rework / Quarantine based on step & tilt)     │
└────────────────────────────────────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Substrate Loading, Vacuum Clamping & Leveling Verification
1. Transfer the post-BOE etched and DI-water rinsed/dried 100mm wafer from the cleanroom transport carrier onto the profilometer motorized stage chuck.
2. Engage chuck vacuum holding pressure.
3. Perform stage baseline tilt verification: execute a two-point leveling sweep across the 100mm wafer chuck to establish stage parallelism within $< 1\text{ }\mu\text{m}$ across 100mm, matching the mechanical Wedge Error Compensation (WEC) reference standard.

### Step 2: Optical Navigation & Multi-Site Scribe Coordinates
1. Activate the top-down split-field/dual CMOS navigation camera system.
2. Using the optical objectives ($5\times$, $10\times$, and $20\times$), locate the primary wafer notch/flat and align the primary orientation axes $(X, Y)$.
3. Move the stage to the target metrology structures:
   - Gen 1 bond pad apertures and test trenches ($100\text{ }\mu\text{m} \times 100\text{ }\mu\text{m}$ square openings).
   - Scribe-line kerf test step-height patterns.
4. Verify optical overlay and positioning precision within $\le 0.5\text{ }\mu\text{m}$ using the $20\times$ high-resolution optical video feed.
5. Program an automated multi-site coordinate map consisting of at least 5 sites:
   - Site 1: Center ($r = 0\text{ mm}$)
   - Site 2: North ($r = 35\text{ mm}, \theta = 90^\circ$)
   - Site 3: South ($r = 35\text{ mm}, \theta = 270^\circ$)
   - Site 4: East ($r = 35\text{ mm}, \theta = 0^\circ$)
   - Site 5: West ($r = 35\text{ mm}, \theta = 180^\circ$)

### Step 3: Stylus Profilometry Scan Recipe Configuration
1. Verify the stylus sensor assembly: diamond tip radius $r_{\text{tip}} = 2.0\text{ }\mu\text{m} - 2.5\text{ }\mu\text{m}$.
2. Calibrate stylus tracking force to $\le 1.0\text{ mg}$ ($9.8\text{ }\mu\text{N}$) to ensure non-destructive contact that does not scratch underlying silicon or distort oxide step edges.
3. Configure the scan recipe parameters:
   - **Scan Length**: Set traverse span to $300\text{ }\mu\text{m}$ (providing $100\text{ }\mu\text{m}$ pre-step unetched baseline, the $100\text{ }\mu\text{m}$ etched trench bottom across the $100\text{ }\mu\text{m} \times 100\text{ }\mu\text{m}$ feature, and $100\text{ }\mu\text{m}$ post-step baseline).
   - **Scan Speed**: Set linear scan velocity $v_{\text{scan}} \le 10\text{ }\mu\text{m/s}$ to maintain continuous tracking and suppress mechanical resonance.
   - **Sampling Resolution**: Configure data acquisition rate for horizontal resolution $\le 0.05\text{ }\mu\text{m}$ and vertical step resolution $\le 0.1\text{ nm}$.
   - **Leveling Algorithm**: Apply two-point linear leveling to reference the pre-step oxide surface as $Z = 0$.

### Step 4: Multi-Site Automated Execution & Data Ingestion
1. Initiate the automated recipe run sequence across all 5 programmed wafer sites.
2. For each site, record:
   - Profile curve $Z(x)$.
   - Etch step-height $H_{\text{step}} = Z_{\text{plateau}} - Z_{\text{trench}}$.
   - Trench floor surface roughness $R_a$ and floor tilt.
3. Inspect profile for signs of incomplete oxide etching (slanted trench floor, residue spikes) or over-etch undercutting.

### Step 5: Statistical Analysis & Acceptance Verification
1. Calculate the mean step-height $\bar{H}_{\text{step}}$, standard deviation $\sigma$, and percentage non-uniformity (% NU) across the 5 sites:
   $$\% \text{NU} = \frac{H_{\max} - H_{\min}}{2 \times \bar{H}_{\text{step}}} \times 100\%$$
2. Disposition rules:
   - **PASS**: All 5 measurement sites confirm clear trench profiles, step height within target range, and stage leveling tilt $< 1\text{ }\mu\text{m}$ across the 100mm wafer.
   - **FAIL / RE-ETCH**: If step height is below nominal target indicating unetched residual oxide, transfer wafer for additional calibrated BOE dip.
   - **QUARANTINE**: If severe radial asymmetry (% NU $> 5\%$) or mechanical tilt exceeds $1.0\text{ }\mu\text{m}$, quarantine wafer and recalibrate chuck leveling and wet etch bath agitation.

---

## 3. Machine-Measurable Acceptance Criteria Target Metrics

| Parameter | Metric Target / Acceptance Criteria | Physical Units | Verification Method |
| :--- | :--- | :--- | :--- |
| **Wafer Chuck Parallelism / Leveling Tilt** | $< 1.0$ across 100mm wafer | $\mu\text{m}$ | Two-point profilometer stage sweep referencing spherical air-bearing WEC standard |
| **Optical Stage Alignment Positioning Precision** | $\le 0.5$ | $\mu\text{m}$ | Optical split-field/CMOS camera navigation with $20\times$ objective |
| **Trench Step Metrology Feature Width** | $100 \times 100$ | $\mu\text{m}$ | Scribe line / bonding pad opening window traversed with $300\text{ }\mu\text{m}$ scan length |
| **Stylus Tip Tracking Force** | $\le 1.0$ ($\le 9.8$) | $\text{mg}$ ($\mu\text{N}$) | Calibrated low-force transducer diamond stylus tip |

---

## 4. Cited Reference Sources

1. **Karl Suss MA6 Mask Aligner Standard Operating Procedure & Gap Control**:
   - Wedge Error Compensation (WEC) mechanical leveling using spherical air bearings achieving wafer chuck parallelism $< 1\text{ }\mu\text{m}$ across 100mm wafers.
   - Split-field microscope with $5\times$, $10\times$, and $20\times$ objectives paired with dual high-resolution CMOS cameras.
   - Alignment precision $\le 0.5\text{ }\mu\text{m}$ in vacuum contact mode.
2. **Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging**:
   - On-chip bonding pads: $100\text{ }\mu\text{m} \times 100\text{ }\mu\text{m}$ square contact openings.
   - Wire pull strength $\ge 4.0\text{ grams-force}$ for $25\text{ }\mu\text{m}$ wire.
3. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - 180nm technology generation DRAM cell geometry: Access transistor channel length $L = 180\text{ nm}$, active diffusion width $W = 220\text{ nm}$.
   - Stacked capacitor over bitline (COB) architecture.
   - Retention and dielectric integrity constraints: Capacitance budget $\ge 28\text{ fF/cell}$, leakage current $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

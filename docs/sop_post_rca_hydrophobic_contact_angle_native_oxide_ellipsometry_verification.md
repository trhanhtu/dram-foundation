# SOP: Post-RCA Hydrophobic Contact Angle & Native Oxide Ellipsometry Verification

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Action Type**: Make
- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm Dry Gate Oxide Growth (3.5 nm) [Thermal Processing] > Dry Thermal Oxidation Recipe Execution (850°C-900°C, 3.5 nm SiO2) [Thermal Oxidation] > RCA Clean and Pre-Oxidation Surface Conditioning (SC-1/SC-2/DHF Dip) [Wet Chemistry] > Post-Clean Surface Contact Angle and TXRF Trace Metal Metrology [Metrology] > Pre-Oxidation Clean Surface Spec Verification and Furnace Loading Disposition Report [Metrology] > Post-RCA Hydrophobic Contact Angle and Native Oxide Ellipsometry Verification [Metrology]

---

## 1. Overview & Rationale

In the 180nm open-source DRAM fabrication sequence, access transistors possess channel length $L = 180\text{ nm}$ and active width $W = 220\text{ nm}$, with bitline/wordline pitch scaled to $360\text{ nm}–400\text{ nm}$. The gate dielectric requires thermally grown silicon dioxide ($\text{SiO}_2$) with a tight physical thickness target of $3.5\text{ nm}$ (3.5 to 4.0 nm) grown by dry thermal oxidation at $850^\circ\text{C}–900^\circ\text{C}$.

Thermal oxidation follows the Deal-Grove linear-parabolic kinetic model:
$$x_0^2 + A x_0 = B(t + \tau)$$
In the thin regime ($x_0 \ll A/2$), growth kinetics are interface reaction-rate limited with linear rate constant $k_l = B/A$. Uncontrolled native oxide or chemical oxide regrowth prior to furnace loading introduces an indeterminate initial oxide offset ($\tau$) and disrupts initial dry oxidation kinetics, degrading gate dielectric breakdown strength below the required $E_{\text{bd}} > 10\text{ MV/cm}$ and elevating interface trap density above $D_{\text{it}} < 10^{10}\text{ cm}^{-2}\text{eV}^{-1}$.

This SOP defines the metrology verification protocol following the wet clean (SC-1 / SC-2 / DHF dip) sequence. It quantifies:
1. **Surface Hydrogen Passivation / Hydrophobicity**: Measured via automated sessile droplet contact angle goniometry.
2. **Residual Native Oxide Thickness**: Quantified via multi-wavelength Spectroscopic Ellipsometry (SE) across wafer test sites to ensure clean surface disposition before loading into the $850^\circ\text{C}–900^\circ\text{C}$ quartz tube oxidation furnace.

```text
┌───────────────────────────────────────────────┐
│ Post-RCA DHF Dip Wafer Lot Transfer           │
│ (Cassette in Class 1 Laminar N2 Purged Pod)   │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ Sessile Drop Contact Angle Goniometry         │
│ (DI Water Micro-Droplet Contact Angle θ ≥ 70°)│
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ Multi-Point Spectroscopic Ellipsometry        │
│ (Measure Residual Native Oxide Thickness tox) │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│ Furnace Queue Disposition & Recipe Loading    │
│ Target: 3.5 nm Dry SiO2 (850°C - 900°C)       │
└───────────────────────────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Metrology Stage Preparation & Environmental Control
1. Confirm the metrology tool enclosure environment is maintained at $21.0^\circ\text{C} \pm 0.5^\circ\text{C}$ and relative humidity $< 40\%$ to prevent accelerated native oxide regrowth.
2. Verify pure deionized water supply for goniometer dispensing ($18.2\text{ M}\Omega\cdot\text{cm}$ resistivity at $25^\circ\text{C}$, $0.05\text{ }\mu\text{m}$ filtered).
3. Initialize and calibrate the Spectroscopic Ellipsometer using a certified silicon reference wafer with thermal oxide calibration standard. Verify polarimetric angles $\Psi$ and $\Delta$ across $250\text{ nm}–800\text{ nm}$ wavelength range.

### Step 2: Wafer Transfer & Queue Time Verification
1. Receive wafer cassette transferred directly from the pre-oxidation wet bench immediately following final DHF dip and Marangoni / high-purity $\text{N}_2$ dry.
2. Verify total post-clean elapsed queue time is strictly monitored ($t_{\text{queue}} \le 60\text{ min}$) to avoid ambient native oxidation prior to quartz furnace insertion.
3. Transfer wafer onto automated vacuum chuck using edge-grip end-effector (3 mm edge exclusion).

### Step 3: Automated Sessile Drop Contact Angle Metrology
1. Align wafer to center and notch coordinates.
2. Dispense a calibrated $1.0\text{ }\mu\text{L} \pm 0.1\text{ }\mu\text{L}$ droplet of $18.2\text{ M}\Omega\cdot\text{cm}$ DI water onto designated monitor sites (center, mid-radius, edge).
3. Capture digital shadowgraph profile within $2.0\text{ s}$ of droplet deposition to prevent droplet evaporation artifacts.
4. Execute automated Young-Laplace baseline fitting algorithm to extract contact angle $\theta$.
   - Fully hydrogen-terminated hydrophobic silicon surface must exhibit contact angle $\theta \ge 70^\circ$ (typical $75^\circ–85^\circ$).
   - A hydrophilic surface ($\theta < 30^\circ$) indicates incomplete DHF oxide stripping or residual chemical oxide.
5. Aspirate droplet and dry test site under high-purity $\text{N}_2$ nozzle.

### Step 4: Multi-Point Spectroscopic Ellipsometry Verification
1. Position optical beam ($70.0^\circ \pm 0.05^\circ$ angle of incidence) over 9 standard wafer measurement sites.
2. Collect spectroscopic data ($\tan\Psi, \cos\Delta$) over spectral range $250\text{ nm}–800\text{ nm}$.
3. Fit optical constants using a two-layer model: single-crystal silicon substrate with an ultra-thin native $\text{SiO}_2$ Cauchy/Sellmeier dielectric overlayer.
4. Extract residual native oxide thickness $t_{\text{native}}$. Target for pre-oxidation bare Si is $t_{\text{native}} \le 0.4\text{ nm}$ (indicating clean bare/passivated silicon prior to the $3.5\text{ nm}$ thermal dry oxidation step).

### Step 5: Disposition & Furnace Loading Authorization
1. Compile metrology parameters into the Pre-Oxidation Metrology Report.
2. **PASS Disposition**:
   - Contact angle $\theta \ge 70^\circ$ across all monitor points.
   - Ellipsometric native oxide $t_{\text{native}} \le 0.4\text{ nm}$.
   - Authorize automated wafer lot transfer to the horizontal/vertical quartz tube furnace for the dry gate oxidation recipe ($850^\circ\text{C}–900^\circ\text{C}$, target $3.5\text{ nm} \pm 0.1\text{ nm}$ $\text{SiO}_2$).
3. **FAIL / REWORK Disposition**:
   - If contact angle $\theta < 70^\circ$ or $t_{\text{native}} > 0.6\text{ nm}$, hold cassette. Surface exhibits re-oxidation or incomplete DHF etch.
   - Route lot back for DHF touch-up dip or full RCA re-clean.

---

## 3. Machine-Measurable Acceptance Criteria

| Metric / Parameter | Target Value | Physical Units | Tolerance / Constraint | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Sessile Drop Contact Angle ($\theta$)** | $\ge 70.0$ | $\text{degrees } (^\circ)$ | Min acceptable hydrophobic threshold (nominal $75^\circ–85^\circ$) | Automated optical contact angle goniometer ($1.0\text{ }\mu\text{L}$ DI $\text{H}_2\text{O}$) |
| **Pre-Oxidation Native Oxide Thickness ($t_{\text{native}}$)** | $\le 0.40$ | $\text{nm}$ | $\pm 0.05\text{ nm}$ fit uncertainty | 9-point Spectroscopic Ellipsometry ($250–800\text{ nm}$) |
| **Clean-to-Furnace Queue Time ($t_{\text{queue}}$)** | $\le 60$ | $\text{minutes}$ | Maximum post-DHF ambient exposure before furnace load | MES automated queue timer timestamp |
| **Subsequent Gate Oxide Target Thickness** | $3.50$ | $\text{nm}$ | $3.50\text{ nm}$ to $4.00\text{ nm}$ ($850^\circ\text{C}–900^\circ\text{C}$ dry $\text{O}_2$) | Post-oxidation SE confirmation (Deal-Grove linear regime) |

---

## 4. References & Related Literature Context

- **Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace**:
  Linear-parabolic kinetic model: $x_0^2 + A x_0 = B(t + \tau)$. Thin regime ($x_0 \ll A/2$) linear rate constant $k_l = B/A$. Dry oxidation performed at $850^\circ\text{C}–900^\circ\text{C}$ (to $1000^\circ\text{C}$) in pure dry $\text{O}_2$ achieves $3.5\text{ nm}$ to $4.0\text{ nm}$ gate dielectric thickness, $E_{\text{bd}} > 10\text{ MV/cm}$, and $D_{\text{it}} < 10^{10}\text{ cm}^{-2}\text{eV}^{-1}$.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  Unit cell geometry access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$. Storage capacitor minimum capacitance budget $\ge 28\text{ fF/cell}$, sub-threshold and junction leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  $1\text{T}1\text{C}$ stacked capacitor layout with bitline/wordline pitch $360\text{ nm}–400\text{ nm}$, retention time $> 64\text{ ms}$ at $85^\circ\text{C}$ ($25–30\text{ fF/cell}$), gate dielectric thermally grown $\text{SiO}_2$ at $850^\circ\text{C}–900^\circ\text{C}$ dry oxidation with $\sim 3.5\text{ nm}$ physical thickness.
- Related SOPs:
  - [Post-RCA Surface Defect Density Inspection & Darkfield Haze Mapping](../sop_post_rca_surface_defect_density_darkfield_haze.md)
  - [Automated Sequential Wet Bench Immersion Run & Marangoni Dry Execution](../sop_wet_bench_rca_marangoni.md)

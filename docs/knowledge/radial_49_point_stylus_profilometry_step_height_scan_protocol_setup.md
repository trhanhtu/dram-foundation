# Radial 49-Point Stylus Profilometry Step-Height Scan Protocol Setup

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented

## Overview & Rationale
This Standard Operating Procedure (SOP) governs the setup, calibration, execution, and cross-correlation of automated radial 49-point stylus profilometry step-height scans for post-etch patterned $\text{SiO}_2$ dielectric trenches in the 180nm open-source DRAM fabrication sequence (post-BOE 6:1 etch). The profilometry step-height mapping correlates directly with optical thin-film spectroscopic ellipsometry data to capture radial etch non-uniformity across spin coating and furnace runs.

## Process Flowchart
```text
┌───────────────────────┐
│  Wafer Vacuum Load &  │
│    Notch Alignment    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Stylus Tip & Force   │
│      Calibration      │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    Radial 49-Point    │
│   Coordinate Recipe   │
│         Load          │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│      Multi-Point      │
│      Step-Height      │
│   Profilometry Scan   │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│     Trench Depth      │
│     Extraction &      │
│     Ellipsometry      │
│      Correlation      │
└───────────────────────┘
```

## Step-by-Step SOP Procedure
1. **Tool Initialization and Vacuum Chucking**:
   - Verify vibration isolation air table pressure and acoustic enclosure closure.
   - Load the patterned 180nm DRAM wafer onto the automated motorized translation chuck. Engage wafer vacuum hold-down ($> 70\text{ kPa}$).
   - Perform automated optical pattern recognition on the wafer notch/flat and align the DRAM unit cell scribe-line alignment marks to establish the global $(X, Y, \theta)$ coordinate frame.

2. **Stylus Tip Qualification & Force Baseline Calibration**:
   - Inspect the low-load diamond stylus tip (nominal radius $2.0\,\mu\text{m}$ to $2.5\,\mu\text{m}$).
   - Zero the optical lever / LVDT deflection transducer against an optical flat reference.
   - Set contact tracking force to $0.05\text{ mN}$ to $0.10\text{ mN}$ ($5\text{ mg}$ to $10\text{ mg}$) to eliminate photoresist scratching or film deformation while tracking patterned $1.3\,\mu\text{m}$ photoresist / $\text{SiO}_2$ steps.

3. **Radial 49-Point Grid Configuration**:
   - Load the standard concentric radial polar distribution recipe containing exactly 49 measurement sites:
     - Center site: 1 point at $(r = 0\text{ mm})$.
     - Ring 1: 8 points spaced at $45^\circ$ azimuth intervals.
     - Ring 2: 12 points spaced at $30^\circ$ azimuth intervals.
     - Ring 3: 12 points spaced at $30^\circ$ azimuth intervals.
     - Ring 4 (Edge zone): 16 points spaced at $22.5^\circ$ azimuth intervals (maintaining a $3\text{ mm}$ edge-exclusion zone).

4. **Automated Step-Height Profile Acquisition**:
   - For each of the 49 coordinates, translate stage and acquire a surface scan across the etched $\text{SiO}_2$ step transition.
   - Set trace scan length to $200\,\mu\text{m}$ at a scan speed of $10\,\mu\text{m/s}$ with a sampling frequency $\ge 500\text{ Hz}$.
   - Apply two-point tilt levelling to horizontal substrate baselines on both sides of the step. Calculate the vertical step-height ($Z_{\text{step}}$) using ISO 5436-1 standard groove depth algorithms.

5. **Spectroscopic Ellipsometry Cross-Correlation**:
   - Import the corresponding 49-point wafer map acquired via spectroscopic ellipsometry based on the polarization amplitude ratio and phase difference:
     $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
   - Co-register the physical step height $Z_{\text{step}}$ with optical thickness modeling (Cauchy/Sellmeier dispersion parameterized $n(\lambda), k(\lambda)$ for unetched oxide reference vs residual trench oxide).
   - Evaluate radial non-uniformity metrics across spin coating and furnace runs.

## Acceptance Criteria Target Metrics
| Parameter / Metric | Target Value | Physical Unit | Verification Method |
| :--- | :--- | :--- | :--- |
| Wafer Mapping Grid Density | **49** | Points / wafer | Automated radial polar recipe coordinate log |
| Photoresist Reference Thickness Precision | **$\le \pm 2$** | nm | Spectroscopic ellipsometry / profilometry delta on $1.3\,\mu\text{m}$ resist |
| Ultrathin Gate Dielectric Measurement Precision | **$\le \pm 0.05$** | nm | Multi-wavelength spectroscopic ellipsometry on $3.5\text{ nm}$ dry oxide |
| Radial Step Height Uniformity ($\sigma / \mu$) | **$\le 2.5$** | % | Statistical evaluation of 49-point step-height profile dataset |

## Cited Sources
- *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*

# Standard Operating Procedure (SOP): In-Line High-Resolution CD-SEM Profile & Plug Recess Metrology

- **Module**: Metrology & Defect Review / Post-CMP Quality Assurance
- **Node**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Status**: Implemented / Active

---

## 1. Scope & Objective
This SOP defines the in-line critical dimension scanning electron microscopy (CD-SEM) and high-resolution tilted-beam / secondary-backscattered electron profile metrology procedure for tungsten (W) contacts and storage node drain plugs following Chemical Mechanical Planarization (CMP). It ensures structural compliance before stacked capacitor (Crown / MIM) fabrication.

---

## 2. Process Flow & Operational Steps

1. **Wafer Loading & Global Optical Alignment**:
   - Transfer wafer from post-CMP dry station into the CD-SEM loadlock chamber under ultra-high vacuum ($P < 1.0 \times 10^{-4}\text{ Pa}$).
   - Perform automated pattern recognition using optical macro-alignment marks on scribe-line fiducials.

2. **E-Beam Column Setup & Charging Suppression**:
   - Set primary electron landing energy $V_{\text{acc}} = 500\text{ V} - 800\text{ V}$ with beam current $I_{\text{beam}} = 8\text{ pA} - 15\text{ pA}$ to eliminate substrate charging on inter-layer dielectric (ILD oxide).
   - Apply dynamic astigmatism correction and objective aperture alignment at $200\text{k}\times$ magnification on a calibration reference pitch.

3. **Top-Down CD-SEM Metrology**:
   - Acquire top-down secondary electron (SE) images of the shared bitline contact and drain contact W-plugs across 9 site locations (die center, edge, quadrant perimeter).
   - Extract critical dimensions: channel contact length axis ($L_{\text{target}} = 180\text{ nm}$) and contact width axis ($W_{\text{target}} = 220\text{ nm}$).
   - Verify array pitch alignment against wordline/bitline target grid ($360\text{ nm} - 400\text{ nm}$).

4. **Tilted-Beam High-Resolution Recess Profilometry**:
   - Tilt electron optical column or sample stage to $\theta = 15^\circ - 30^\circ$.
   - Quantify plug recess relative to surrounding ILD oxide via backscattered electron (BSE) edge-contrast differentiation and signal intensity derivative profiles.
   - Flag excessive dishing or over-polishing if recess violates the target threshold.

5. **Automated Defect & Residual Metal Scanning**:
   - Perform bright-field voltage-contrast (VC) inspection across array boundaries to detect un-cleared tungsten stringers, bridging shorts, or seam voids within the plug core.
   - Archive measurement data into the fab manufacturing execution system (MES) and trigger lot disposition.

---

## 3. Quantitative Acceptance Criteria

| Metric Parameter | Target Value | Tolerance / Specification Limit | Units |
| :--- | :--- | :--- | :--- |
| **Contact Plug Critical Dimension (Length Axis)** | 180 | $\pm 10$ | nm |
| **Contact Plug Critical Dimension (Width Axis)** | 220 | $\pm 12$ | nm |
| **Array Pattern Pitch (Wordline / Bitline)** | 360 – 400 | $\pm 15$ | nm |
| **Post-CMP Plug Recess Depth** | 20 – 30 | $\le 35$ (max allowable recess) | nm |

---

## 4. Context References & Citations
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$, bitline contact shared between adjacent memory cells, stacked capacitor erected above drain contact via tungsten plug (W-plug).
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: Bitline and wordline pitch approximately $360\text{ nm} - 400\text{ nm}$; 1T1C stacked capacitor integration requirements.

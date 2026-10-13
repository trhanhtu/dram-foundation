# SOP: Vernier Scale Optical Overlay Error & Critical Dimension Metrology

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Process Tier**: Metrology / Photolithography Quality Gate

---

## 1. Overview & Scope
This Standard Operating Procedure (SOP) governs the quantitative optical inspection, vernier scale misregistration evaluation, and critical dimension (CD) line/space verification following Shipley 1813 positive resist development in Microposit MF-319. It confirms alignment budget compliance for Gen 2 DRAM lithography before committing wafers to irreversible wet or dry etching steps.

```text
┌────────────────────────┐
│                        │
│    Sample Loading &    │
│   Stage Calibration    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Diffraction Line    │
│  Focusing & Objective  │
│         Setup          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Post-Dev Resist     │
│       Thickness        │
│     Reflectometry      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Optical Vernier     │
│  Overlay Reading X/Y   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Critical Dimension   │
│       Line-Space       │
│      Verification      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Disposition: Pass or  │
│      Strip/Rework      │
│                        │
└────────────────────────┘
```

---

## 2. Step-by-Step Procedure

### Step 1: Substrate Preparation & Visual Inspection
1. Transfer developed wafer (Shipley 1813 post-MF-319 45–60 s development and DI water rinse) onto the vacuum chuck of the metrology stage.
2. Verify under low-magnification macro view that no residual scumming, blistering, or unrinsed surfactant film persists across the active die fields.

### Step 2: Optical Objective Configuration & Image Calibration
1. Select a calibrated 10x Plan Achromat objective (Numerical Aperture $\text{NA} = 0.25$) on the optical microscope.
2. Focus on calibrated stage micrometer grid targets to establish pixel-to-micron aspect ratio calibration.

### Step 3: Resist Film Thickness Verification via Spectroscopic Reflectometry
1. Position optical reflectometer probe over test pads adjacent to scribe lines.
2. Fit the measured reflectance curve against Cauchy/Sellmeier dispersion parameters ($n(\lambda), k(\lambda)$) using:
   $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
3. Confirm unexposed/retained Shipley 1813 resist thickness across a standard multi-point radial map.

### Step 4: Orthogonal Vernier Scale Overlay Metrology ($X$ & $Y$)
1. Navigate microscope crosshairs to the peripheral scribe-line vernier gauge pairs (inner comb = current mask level; outer comb = substrate baseline level).
2. Measure alignment offset along the $X$-axis by identifying the coincident index bars on the vernier array.
3. Translate to the orthogonal $Y$-axis vernier gauge and repeat coincidence reading.
4. Record radial displacement vector:
   $$\delta_{\text{total}} = \sqrt{\delta_x^2 + \delta_y^2}$$

### Step 5: Critical Dimension (CD) Line-Space Metrology
1. Align image sensor reticle across minimum pitch test structures (proximity printed nominal line-space grating).
2. Quantify isolated line width and dense space pitch via intensity profile half-maximum thresholding.

### Step 6: Lot Disposition & Action Thresholds
- **PASS**: Total misregistration $\le \pm 5\,\mu\text{m}$ and CD within target resolution limits $\to$ Proceed to soft bake inspect / plasma or wet etching.
- **FAIL**: Overlay $> \pm 5\,\mu\text{m}$ or CD out of spec $\to$ Route wafer to photoresist strip (acetone / piranha) and rework lithography before any substrate etch occurs.

---

## 3. Machine-Measurable Acceptance Criteria

```text
                      Gen 2 Metrology Target Thresholds 
                     ┌─────────────────────────────────┐
                     │█████████████████████████████████│
     Gap Control (um)┤█████████████████████████████████│
                     │▓▓▓▓▓▓▓                          │
   CD Resolution (um)┤▓▓▓▓▓▓▓                          │
Resist Thickness (um)┤▒▒▒▒▒                            │
                     │▒▒▒▒▒                            │
   Overlay Error (um)┤░░░░░░░░░░░░░░░░░                │
                     │░░░░░░░░░░░░░░░░░                │
                     └┬───────┬───────┬───────┬───────┬┘
                     0.0     2.5     5.0     7.5   10.0 
```

1. **Orthogonal Vernier Overlay Alignment Tolerance**:
   - Target: $\le \pm 5\,\mu\text{m}$ (Gen 2 target, refined from Gen 1 $\pm 100\,\mu\text{m}$).
2. **Post-Exposure Resist Film Thickness & Uniformity**:
   - Target: $1.3\,\mu\text{m} \pm 0.002\,\mu\text{m}$ ($\pm 2\,\text{nm}$ measurement precision via spectroscopic reflectometry/ellipsometry optical modeling).
3. **Proximity Printing Critical Dimension (CD) Resolution**:
   - Target: $2.0\,\mu\text{m} - 3.0\,\mu\text{m}$ resolvable line/space grating (with mask aligner gap setting maintained at $10\,\mu\text{m} - 20\,\mu\text{m}$).
4. **Aligner Gap Actuator Sensitivity & Precision**:
   - Target: Closed-loop micrometer / piezo gap control sensitivity $\le 0.1\,\mu\text{m}$.

---

## 4. Literature & Context Citations
1. **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**:
   - 10x Plan Achromat objective ($\text{NA} = 0.25$) for micron-scale resolution.
   - Shipley 1813 spin-coated at 4000 RPM yielding $\sim 1.3\,\mu\text{m}$ thickness; MF-319 development for 45–60 s.
   - Gen 1 alignment tolerance ($\pm 100\,\mu\text{m}$) upgrading to Gen 2 tolerance ($\pm 5\,\mu\text{m}$).
2. **Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose**:
   - Proximity mode gap set at $10\,\mu\text{m} - 20\,\mu\text{m}$ using actuators with $0.1\,\mu\text{m}$ sensitivity.
   - Diffraction-limited proximity resolution of $\sim 2 - 3\,\mu\text{m}$.
   - UV exposure clear dose calibration of $120 - 150\,\text{mJ/cm}^2$ for $1.3\,\mu\text{m}$ Shipley 1813.
3. **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**:
   - Complex reflection ratio $\rho = r_p / r_s = \tan(\Psi) \cdot \exp(i\Delta)$ under Cauchy/Sellmeier dispersion modeling.
   - Optical measurement precision for photoresist ($1.3\,\mu\text{m}$) within $\pm 2\,\text{nm}$.

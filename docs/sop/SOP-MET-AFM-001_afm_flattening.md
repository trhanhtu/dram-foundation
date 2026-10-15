# Standard Operating Procedure (SOP): AFM Topography Raw Height Field Preprocessing and Flattening

**Process Level:** Sub-module Metrology / Post-CMP Planarization Characterization  
**Node Generation:** Gen 3 (180nm Open-Source DRAM Chip, DRAM Foundation VN)  
**Parent Process Chain:** Inter-Layer Dielectric (ILD) Oxide CMP Recipe Optimization and Polish > Post-CMP Metrology > Tapping-Mode AFM Metrology  
**Document ID:** `SOP-MET-AFM-001`  

---

## 1. Process Overview & Objective
Raw Atomic Force Microscopy (AFM) height fields obtained from tapping-mode inspection of polished Inter-Layer Dielectric (ILD) oxide over dense 180nm stacked capacitor bitline arrays contain physical scan artifacts:
1. Piezoelectric scanner bow and parabolic tilt.
2. Slow-scan axis thermal drift along the Z-baseline.
3. Line-to-line Z-offsets caused by tip-sample engagement fluctuations.

This SOP details the deterministic, artifact-free mathematical preprocessing and leveling required to isolate true nanoscale surface roughness ($S_q$, $S_a$) and detect micro-scratches without introducing false step-height flattening distortions.

---

## 2. Process Workflow Diagram

```text
┌────────────────────────┐
│                        │
│   Raw AFM Height Map   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Data Conditioning &   │
│     Spike Removal      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       Planar Bow       │
│      Correction:       │
│       Polynomial       │
│      Subtraction       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      Line-by-Line      │
│      Mean/Median       │
│       Alignment        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Feature Masking &    │
│  Zero-Plane Baseline   │
│     Normalization      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Flattened Topography  │
│      Height Field      │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Raw Data Ingestion and Point Grid Verification
- Ingest raw cantilever deflection and piezo Z-sensor channels ($512 \times 512$ or $1024 \times 1024$ points) over the designated scan area ($5\,\mu\text{m} \times 5\,\mu\text{m}$ to $20\,\mu\text{m} \times 20\,\mu\text{m}$).
- Verify physical spatial grid resolution:
  - In-plane grid step $\Delta x, \Delta y$ must match or be commensurate with the lithographic physical placement grid of $0.005\,\mu\text{m}$ ($5\,\text{nm}$) per [SkyWater SKY130 Design Rules & Lithography Grid](file:///docs/context.yaml).
  - Confirm vertical Z-piezo resolution calibrated to sub-Angstrom precision ($< 0.05\,\text{nm}$) consistent with optical metrology baselines.

### Step 2: Despiking & Singular Outlier Filtering
- Apply a $3 \times 3$ pixel spatial moving median filter exclusively to identify non-physical cantilever flight spikes (laser reflection loss / feedback lost).
- Threshold: Any pixel deviating from local median by $> 5\sigma$ (or $> 15\,\text{nm}$ step discontinuity across 1 grid step) is tagged as an outlier spike.
- Interpolate flagged pixels using 8-neighbor bilinear interpolation.

### Step 3: Global Planar Tilt and 2nd-Order Bow Correction
- Execute global background subtraction across the entire field:
  $$Z_{\text{corrected}}(x,y) = Z_{\text{raw}}(x,y) - \left(a_0 + a_1 x + a_2 y + a_3 x^2 + a_4 y^2 + a_5 xy\right)$$
- Polynomial fit order must be restricted to 1st order (plane leveling) or 2nd order (scanner tube arc bow compensation).
- **Constraint:** Do not use $\ge 3\text{rd}$ order polynomial flattening across unmasked topography to prevent synthetic waviness and depression artifacts near array edges.

### Step 4: Masked Line-by-Line Median Alignment
- Isolate structural DRAM features: Mask out unpolished topography, contact hole edges ($0.17\,\mu\text{m} \times 0.17\,\mu\text{m}$), and tungsten plug (W-plug) protrusion/recession areas using a binary exclusion mask ($M(x,y) = 0$ for pattern steps, $M(x,y) = 1$ for continuous ILD oxide).
- For each fast-scan line $y_i$, compute the median height $\tilde{Z}(y_i)$ of unmasked pixels ($M = 1$):
  $$Z_{\text{flattened}}(x, y_i) = Z_{\text{corrected}}(x, y_i) - \tilde{Z}(y_i)$$
- Removes fast-scan line hopping and slow-axis thermal offset while preventing artificial "shadow trenches" adjacent to raised DRAM capacitor crown or plug regions.

### Step 5: Mean Plane Zero-Baseline Normalization
- Set the global reference plane such that the arithmetic mean height of the baseline polished ILD oxide field equals $0.000\,\text{nm}$:
  $$\bar{Z}_{\text{ILD}} = \frac{1}{N_{\text{mask}}} \sum_{(x,y) \in M} Z_{\text{flattened}}(x,y) = 0.00\,\text{nm}$$
- Export the calibrated floating-point matrix to the downstream surface roughness extraction algorithm.

---

## 4. Acceptance Criteria & Target Metrics

```text
                                                        
                   ┌───────────────────────────────────┐
                   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
    Peak Mask Excl.┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
                   │▒▒▒▒                               │
   Line Scan Offset┤▒▒▒▒                               │
   Z-Baseline Drift┤▓▓▓                                │
                   │▓▓▓                                │
Residual Tilt Angle┤██                                 │
                   │██                                 │
                   └┬────────┬───────┬────────┬───────┬┘
                  0.00     0.24    0.47     0.71   0.95 
```

1. **Residual Macro Tilt Slope:** Residual plane angle across the unmasked baseline area must be $\le 0.02^\circ$ ($\le 0.35\,\text{mrad}$).
2. **Line-to-Line Median Discontinuity:** Inter-line step offset across adjacent fast-scan rasters must be $\le 0.08\,\text{nm}$ (3-sigma).
3. **Z-Baseline Measurement Repeatability:** Post-flattening zero-plane drift across consecutive repeat scans must be within $\pm 0.05\,\text{nm}$, conforming to sub-Angstrom precision standards established in spectroscopic dielectric metrology.
4. **Pattern Step Masking Fidelity:** Feature exclusion mask coverage on unpolished contacts ($0.17\,\mu\text{m} \times 0.17\,\mu\text{m}$) and dense bitline structures must achieve $\ge 95\%$ boundary conformity.

---

## 5. Source Citations & Literature Alignment
- **SkyWater SKY130 Open PDK Design Rules & Lithography Grid:**
  - Manufacturing physical placement grid resolution: $0.005\,\mu\text{m}$ ($5\,\text{nm}$).
  - Minimum contact hole dimension: $0.17\,\mu\text{m} \times 0.17\,\mu\text{m}$.
  - Lithography resolution budget: $\lambda = 248\,\text{nm}$ (KrF DUV), $\text{NA} = 0.65$, overlay budget $\le 35\,\text{nm}$.
- **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology:**
  - Precision standard: Sub-Angstrom precision benchmark of $\pm 0.05\,\text{nm}$ applied to baseline film leveling and metrology stability.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench:**
  - Stacked capacitor over bitline (COB) architecture with tungsten plug (W-plug) interconnects requiring topography masking during CMP dielectric polish characterization.

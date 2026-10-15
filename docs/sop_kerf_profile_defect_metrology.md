# SOP: Kerf Profile & Multi-Threshold Edge-Detection Defect Metrology Algorithm Recipe Optimization

- **Document ID**: SOP-PKG-MET-003
- **Classification**: Standard Operating Procedure (Level 4 Leaf SOP)
- **Node Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > BEOL Multi-Layer Metallization, Wafer Sort & Packaging > Wafer Backgrinding Thinning & High-Speed Diamond Saw Dicing > Post-Dicing Die Metrology, Kerf Quality Inspection & Die Pick-and-Place Sort > Automated Optical Inspection (AOI) of Kerf Width, Chipping & Crack Defect Metrology > Kerf Profile & Multi-Threshold Edge-Detection Defect Metrology Algorithm Recipe Optimization
- **Technology Generation**: Gen 3 (180nm / SkyWater SKY130 compatible)
- **Action Type**: Make

---

## 1. Scope & Objective
This SOP establishes the machine recipe calibration and algorithmic optimization procedure for automated optical inspection (AOI) of post-dicing street kerfs, die-seal ring margins, and edge chipping/cracking on 180nm DRAM MPW wafers.

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│      Wafer Load &      │
│   Fiducial Alignment   │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│    Multi-Wavelength    │
│   Brightfield / DUV    │
│          Scan          │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│  Kernel Convolution &  │
│     Gradient Edge      │
│       Extraction       │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│        Adaptive        │
│  Multi-Threshold Kerf  │
│      Segmentation      │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│   Sub-Pixel Metric &   │
│        Chipping        │
│     Quantification     │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│  Automated Binning &   │
│    PnP Feedforward     │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step SOP Procedure

### Step 1: Substrate Vacuum Clamping & Global Fiducial Pattern Alignment
1. Mount the tape-mounted, thinned wafer (post-diamond saw dicing) onto the AOI automated theta-X-Y chuck with vacuum suction >= 75 kPa.
2. Calibrate coordinate system registration using dedicated peripheral alignment fiducials matching the physical placement grid resolution of **0.005 µm (5 nm)** [Ref: SkyWater SKY130 PDK].
3. Execute theta correction ensuring angular runout along the dicing street axis is $\le \pm 0.002^\circ$.

### Step 2: Optical Train & Illumination Balancing
1. Configure illumination using high-resolution DUV / i-line dual-band optics ($\lambda_1 = 248\text{ nm}$ KrF excimer source, $\lambda_2 = 365\text{ nm}$ i-line) with numerical aperture $\text{NA} = 0.65$ to resolve micro-cracks below $R = k_1 \cdot (\lambda / \text{NA}) = 0.40 \cdot (248 / 0.65) = 152\text{ nm}$ [Ref: SkyWater SKY130 PDK].
2. Set autofocus z-axis tracking within the optical Depth of Focus window ($\text{DOF} = k_2 \cdot (\lambda / \text{NA}^2) \ge 0.5\text{ µm}$) across the diced wafer topography [Ref: SkyWater SKY130 PDK].
3. Calibrate reflection intensity baselines across bare silicon street centers and dielectric passivation boundaries using normal-incidence complex Fresnel coefficients $\rho = r_p / r_s = \tan(\Psi) \cdot \exp(i\Delta)$ [Ref: Spectroscopic Ellipsometry Literature].

### Step 3: Multi-Threshold Convolution & Dynamic Kerf Edge Detection
1. Apply a $5 \times 5$ Gaussian smoothing filter ($\sigma = 1.0$) followed by dual-kernel Sobel directional edge gradient filtering ($G = \sqrt{G_x^2 + G_y^2}$).
2. Execute **Multi-Threshold Segmentation** across 3 distinct optical zones:
   - **$T_1$ (Street Center / Tape Trench)**: Low-reflectance threshold calibrated to silicon dicing trench floor ($I < 0.25 I_{\text{max}}$).
   - **$T_2$ (Chipping & Delamination Fringe)**: Intermediate reflectance threshold detecting micro-fractures into the die-seal margin ($0.25 I_{\text{max}} \le I \le 0.65 I_{\text{max}}$).
   - **$T_3$ (Active Die & Seal Ring Passivation)**: High-reflectance threshold defining undamaged die edge boundary ($I > 0.65 I_{\text{max}}$).
3. Compute sub-pixel zero-crossing interpolation on the edge gradient profile down to the $0.005\text{ µm}$ (5 nm) manufacturing grid resolution.

### Step 4: Kerf Profile Metrology & Die Chipping Quantification
1. Measure bilateral kerf width $W_k$ at $10\text{ µm}$ intervals along each scribe channel across all horizontal and vertical dicing lanes.
2. Measure chipping protrusion distance $\Delta X_{\text{chip}}$ normal to the nominal die boundary toward the active area.
3. Verify clearance to active circuitry: ensure chipping encroachment does not intrude into the minimum active diffusion width margin ($0.15\text{ µm}$) or metal 1 pitch boundary ($0.34\text{ µm}$) [Ref: SkyWater SKY130 PDK].

### Step 5: Binning Classification & Pick-and-Place Map Generation
1. Correlate defect coordinates against the wafer KLARF map.
2. Mark die as defect/reject if:
   - Chipping intrusion $\Delta X_{\text{chip}} > 10.0\text{ µm}$ from nominal cut line.
   - Street kerf width deviation $|\Delta W_k| > 5.0\text{ µm}$ relative to saw blade nominal thickness.
   - Micro-crack length extends past seal ring into Metal 1/poly design boundaries ($\ge 0.15\text{ µm}$ gate/diffusion zones).
3. Export binning map to the Pick-and-Place (PnP) sorting sorter via SECS/GEM.

---

## 4. Machine-Measurable Acceptance Criteria Target Metrics

```text
                          ┌────────────────────────────┐
                          │░                           │
Inspection Grid Resolution┤░                           │
                          │▒▒                          │
    Edge Roughness 3-Sigma┤▒▒                          │
       Chipping Max Extent┤▓▓▓▓▓▓▓▓▓                   │
                          │▓▓▓▓▓▓▓▓▓                   │
         Dicing Kerf Width┤████████████████████████████│
                          │████████████████████████████│
                          └┬──────┬──────┬─────┬──────┬┘
                          0.0    8.8   17.5  26.2  35.0 
```

| Metric Parameter | Target Specification | Physical Units | Verification Method | Literature Reference |
| :--- | :--- | :--- | :--- | :--- |
| **Physical Inspection Grid Resolution** | $\le 0.005$ | $\mu\text{m}$ (5 nm) | Optical sub-pixel stage calibration | SkyWater SKY130 PDK Grid |
| **Minimum Resolvable Defect Feature Size** | $\le 152$ | $\text{nm}$ ($0.152\ \mu\text{m}$) | Optical resolution test target ($k_1=0.40, \lambda=248\text{ nm}, \text{NA}=0.65$) | SkyWater SKY130 Lithography / Rayleigh |
| **Depth of Focus Window (Topography)** | $\ge 0.5$ | $\mu\text{m}$ | Optical Z-scan across diced kerf trench | SkyWater SKY130 Rayleigh Criteria |
| **Chipping Encroachment Limit** | $\le 10.0$ | $\mu\text{m}$ | Multi-threshold AOI edge segmentation | Packaging & Assembly Scribe Margin |
| **Nominal Dicing Kerf Width Window** | $35.0 \pm 5.0$ | $\mu\text{m}$ | Continuous line scan profiling | Saw Dicing Process Recipe |

---

## 5. Verified Literature Citations & Context
1. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Physical placement grid resolution: $0.005\text{ µm}$ ($5\text{ nm}$).
   - Rayleigh Criteria resolution limit: $R = k_1 \cdot (\lambda / \text{NA}) = 0.40 \cdot (248\text{ nm} / 0.65) = 152\text{ nm}$.
   - Depth of focus limit: $\text{DOF} = k_2 \cdot (\lambda / \text{NA}^2) \ge 0.5\text{ µm}$.
   - CD references: Minimum active diffusion width ($0.15\text{ µm}$), minimum poly gate length ($0.15\text{ µm}$ / $150\text{ nm}$), minimum metal 1 pitch ($0.34\text{ µm}$), poly-to-active overlay error budget ($\le 35\text{ nm}$).
2. **Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology**:
   - Complex reflection ratio: $\rho = r_p / r_s = \tan(\Psi) \cdot \exp(i\Delta)$ for thin film and interface reflectance calibration across silicon and passivation boundaries.

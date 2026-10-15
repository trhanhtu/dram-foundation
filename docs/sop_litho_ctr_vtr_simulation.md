# Standard Operating Procedure (SOP): Full-Chip Aerial Image & Variable Threshold Resist (CTR/VTR) Contour Simulation

- **Document ID:** SOP-LITHO-180-008
- **Date:** 2026-10-15
- **Source:** DRAM Foundation VN Multi-Agent Council
- **Target Node:** 180nm Open-Source DRAM (SKY130 Process Extension / Gen 3)
- **Status:** Accepted

---

## 1. Overview & Objective
This SOP defines the rigorous protocol for running full-chip aerial image simulations and Constant/Variable Threshold Resist (CTR/VTR) contour extractions across post-OPC GDSII layouts. The objective is to verify printability, detect hot-spots, and guarantee that edge placement errors (EPE) satisfy strict silicon critical dimension (CD) constraints under DUV KrF lithography.

---

## 2. Process Workflow Architecture

```text
┌────────────────────────┐
│                        │
│  Post-OPC GDSII Grid   │
│       Snap: 5 nm       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   DUV Optical Setup:   │
│   248nm KrF, NA=0.65   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Full-Chip Aerial    │
│  Image TCC Simulation  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    CTR / VTR Resist    │
│        Modeling        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Full-Chip Contour &   │
│     EPE Metrology      │
│                        │
└────────────────────────┘
```

---

## 3. Physical Parameters & Simulation Protocol

### Step 1: Layout Grid Snapping & Layer Decomposition
- Import post-OPC GDSII/OASIS stream format for active diffusion (`diff`), poly gate (`poly`), and contact (`contact`).
- Ensure all polygon vertices snap strictly to the physical placement manufacturing grid resolution of **0.005 µm (5 nm)**. Reject any off-grid vertices.

### Step 2: DUV Optical Source Configuration
- **Laser Source:** Deep Ultraviolet KrF excimer laser, wavelength $\lambda = 248\text{ nm}$.
- **Numerical Aperture:** $\text{NA} = 0.65$.
- **Process Factor:** $k_1 = 0.40$, establishing the minimum resolvable half-pitch:
  $$R = k_1 \cdot \frac{\lambda}{\text{NA}} = 0.40 \cdot \frac{248\text{ nm}}{0.65} = 152.6\text{ nm} \approx 152\text{ nm}$$
- **Process Depth of Focus Requirement:** $\text{DOF} = k_2 \cdot \frac{\lambda}{\text{NA}^2} \ge 0.5\text{ µm}$.
- Compute transmission cross-coefficients (TCC) using Hopkins formulation decomposed into singular optical convolution kernels.

### Step 3: Aerial Image Simulation & Intensity Calculation
- Convolve mask transmission function $M(x, y)$ with decomposed optical kernels.
- Calculate continuous 2D aerial image intensity map $I(x, y)$ over a calculation grid matching or oversampled to $\le 5\text{ nm}$.

### Step 4: CTR / VTR Resist Threshold Modeling
- **Constant Threshold Resist (CTR):** Apply baseline nominal intensity cutoff threshold $I_{th} = I_0$ for initial 1D cutline extraction.
- **Variable Threshold Resist (VTR):** Calibrate resist development threshold as a function of optical parameters:
  $$I_{th,\text{eff}} = f(I_{\max}, I_{\min}, S_{\text{max}}, \nabla I)$$
  where $\nabla I$ is the image log-slope (ILS) at the edge, compensating for resist acid diffusion, PEB (post-exposure bake) blur, and local flare.

### Step 5: Contour Extraction & Full-Chip Optical Rule Check (ORC)
- Trace the iso-intensity contour at $I(x, y) = I_{th,\text{eff}}$ across all critical gate and diffusion boundaries.
- Sample 2D contours at 10 nm intervals along all gate channels and contact perimeters.
- Measure simulated wafer Critical Dimensions (CD) against drawn layout geometries to detect bridging, pinching, or excessive corner rounding.

---

## 4. Machine-Measurable Acceptance Criteria

```text
Critical Dimension (CD) Targets & Limits (nm)
                         ┌─────────────────────────────┐
                         │●●●●●●●●●●●●●●●●●●●●●●●●●●●●●│
         Min Metal1 Pitch┤●●●●●●●●●●●●●●●●●●●●●●●●●●●●●│
                         │□□□□□□□□□□□□□□□□□□           │
         Min Poly Spacing┤□□□□□□□□□□□□□□□□□□           │
                         │■■■■■■■■■■■■■■■              │
          Min Contact Dim┤■■■■■■■■■■■■■■■              │
Min Resolvable Half-Pitch┤██████████████               │
                         │██████████████               │
           Min Diff Width┤▓▓▓▓▓▓▓▓▓▓▓▓▓                │
                         │▓▓▓▓▓▓▓▓▓▓▓▓▓                │
        Min Poly Gate Len┤▒▒▒▒▒▒▒▒▒▒▒▒▒                │
                         │▒▒▒▒▒▒▒▒▒▒▒▒▒                │
         Min Metal1 Width┤░░░░░░░░░░░░░                │
                         │░░░░░░░░░░░░░                │
                         └┬──────┬──────┬──────┬──────┬┘
                          0     85     170    255   340 
```

| Metric ID | Parameter | Nominal / Target Spec | Tolerance / Pass Limit | Physical Unit |
| :--- | :--- | :--- | :--- | :--- |
| **AC-01** | Simulated Poly Gate Length ($L_g$) CD | $0.15\text{ µm}$ ($150\text{ nm}$) | $\ge 0.15\text{ µm}$ (Pinched contour $\ge 150\text{ nm}$) | $\text{nm}$ / $\text{µm}$ |
| **AC-02** | Active Diffusion Width ($W_{\text{diff}}$) CD | $0.15\text{ µm}$ ($150\text{ nm}$) | $\ge 0.15\text{ µm}$ across active channels | $\text{nm}$ / $\text{µm}$ |
| **AC-03** | Inter-Poly Gate Clear Spacing | $0.21\text{ µm}$ ($210\text{ nm}$) | $\ge 0.21\text{ µm}$ (Bridging margin $> 0\text{ nm}$) | $\text{nm}$ / $\text{µm}$ |
| **AC-04** | Gate Poly to Active Diffusion Overlay Margin | $\le 35\text{ nm}$ | Maximum simulated edge placement error $\le 35\text{ nm}$ | $\text{nm}$ |
| **AC-05** | Usable Depth of Focus (DOF) Window | $\ge 0.5\text{ µm}$ | CD within $\pm 10\%$ over focus variation $\ge 0.5\text{ µm}$ | $\text{µm}$ |

---

## 5. Citations & Verified Literature Context
1. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid:**
   - Physical placement grid resolution: $0.005\text{ µm}$ ($5\text{ nm}$).
   - Minimum active diffusion width: $0.15\text{ µm}$.
   - Minimum poly gate length: $0.15\text{ µm}$ ($150\text{ nm}$).
   - Minimum poly gate spacing: $0.21\text{ µm}$.
   - Minimum contact hole dimension: $0.17\text{ µm} \times 0.17\text{ µm}$.
   - Exposure: DUV $248\text{ nm}$ KrF excimer laser for critical poly and contact layers; i-line ($365\text{ nm}$) for upper metal routing layers.
   - Overlay error budget: Poly-to-diffusion overlay $\le 35\text{ nm}$.
   - Rayleigh criteria: $\lambda = 248\text{ nm}$, $\text{NA} = 0.65$, $k_1 = 0.40 \implies R = 152\text{ nm}$.
   - Depth of focus: $\text{DOF} = k_2 \cdot \frac{\lambda}{\text{NA}^2} \ge 0.5\text{ µm}$.

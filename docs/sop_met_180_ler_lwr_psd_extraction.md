# Standard Operating Procedure (SOP): Line-Edge and Line-Width Roughness (LER/LWR) Power Spectral Density Extraction

- **Document ID**: SOP-MET-180-LER-001
- **Process Step**: 180nm Open-Source DRAM Chip > EBDW Lithography for 180nm Critical Dimension Gates > Metrology > Line-Edge and Line-Width Roughness (LER/LWR) Power Spectral Density Extraction
- **Generation**: Gen 3 (nm)
- **Status**: Implemented / Active

---

## 1. Scope & Objective
This SOP defines the step-by-step metrology procedure for extracting Line-Edge Roughness (LER) and Line-Width Roughness (LWR) Power Spectral Density (PSD) profiles across 180nm polysilicon access transistor gate channels and array wordlines. The objective is to separate high-frequency electron-beam/resist stochastic noise from low-frequency CD drift, ensuring channel length integrity without causing junction leakage degradation in the 1T1C storage cell.

---

## 2. Metrology Workflow Overview

```text
┌────────────────────────┐
│                        │
│    High-Res CD-SEM     │
│   Image Acquisition    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Edge Detection &    │
│       Coordinate       │
│       Extraction       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Spatial Covariance &  │
│  FFT PSD Calculation   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Metrology Parameter   │
│     Deconvolution      │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: CD-SEM Recipe Execution & High-Resolution Image Acquisition
1. Load the patterned and etched 180nm polysilicon gate wafer onto the automated CD-SEM chamber chuck.
2. Align to the active memory array region targeting access transistor poly lines with nominal channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$, and wordline pitch of $360\text{ nm}$ to $400\text{ nm}$.
3. Set the electron beam landing energy to $300\text{ eV} - 500\text{ eV}$ with an emission probe current of $8\text{ pA} - 12\text{ pA}$ to avoid resist charging and shrinkage.
4. Capture top-down secondary electron (SE) images along line segments with an inspection field-of-view (FOV) length $\ge 2.0\text{ }\mu\text{m}$ along the gate edge at a pixel resolution corresponding to the physical grid step resolution of $5\text{ nm}$ ($0.005\text{ }\mu\text{m}$).

### Step 2: Line Edge Detection and Coordinate Digitization
1. Perform multi-threshold / maximum derivative edge detection along both the left edge $x_L(y)$ and right edge $x_R(y)$ at discretized vertical positions $y_i = i \cdot \Delta y$ where sampling step $\Delta y = 5\text{ nm}$.
2. Compute the local critical dimension line-width trace:
   $$W(y) = x_R(y) - x_L(y)$$
3. Verify baseline average critical dimension conforms to the drawn gate specification:
   $$\langle W \rangle = 180\text{ nm} \quad (\text{minimum drawn baseline: } 150\text{ nm})$$
4. Detrend long-range geometric distortions (linear tilt and parabolic wafer-level bow) using 1st/2nd-order polynomial fitting to generate zero-mean spatial fluctuation functions:
   $$\delta x_L(y) = x_L(y) - \langle x_L(y) \rangle$$
   $$\delta W(y) = W(y) - \langle W(y) \rangle$$

### Step 3: Spatial Autocovariance and Discrete FFT Power Spectral Density Extraction
1. Compute the discrete 1D Fast Fourier Transform (FFT) over the digitized spatial domain of edge fluctuation profiles:
   $$\widetilde{\delta x}(f) = \mathcal{F}\{\delta x(y)\}$$
2. Calculate the raw 1D Power Spectral Density $PSD_{\text{raw}}(f)$ over spatial frequencies $f \in [f_{\min}, f_{\max}]$ where $f_{\min} = 1/L_{\text{meas}}$ and $f_{\max} = 1/(2 \Delta y) = 1/(10\text{ nm}) = 0.1\text{ nm}^{-1}$:
   $$PSD(f) = \frac{1}{L_{\text{meas}}} \left| \widetilde{\delta x}(f) \right|^2$$
3. Average $PSD(f)$ spectra across $\ge 32$ parallel poly line scans across adjacent cell memory arrays spaced at $360\text{ nm}$ pitch to eliminate localized metrology speckle noise.

### Step 4: Palasantzas Model Fitting and Metrology Noise Deconvolution
1. Fit the averaged $PSD(f)$ to the Palasantzas roughness analytical model:
   $$PSD(f) = \frac{2 \sigma^2 \xi}{\left(1 + (2\pi f \xi)^2\right)^{\alpha + 0.5}} + N_{\text{SEM}}$$
   where:
   - $\sigma$: Root-mean-square roughness amplitude.
   - $\xi$: Correlation length.
   - $\alpha$: Hurst roughness exponent (fractal dimension $D = 2 - \alpha$).
   - $N_{\text{SEM}}$: High-frequency white noise floor introduced by CD-SEM shot noise.
2. Deconvolve $N_{\text{SEM}}$ by subtracting the high-frequency floor baseline ($f > 0.05\text{ nm}^{-1}$).
3. Extract final $3\sigma_{\text{LER}}$ and $3\sigma_{\text{LWR}} = 3 \sqrt{\sigma_{x_L}^2 + \sigma_{x_R}^2 - 2\,\text{cov}(x_L, x_R)}$.

---

## 4. Acceptance Criteria & Target Metrics

```text
                       Physical Metrology Constraints   
                     ┌─────────────────────────────────┐
                     │░░░░                             │
  Overlay Budget (nm)┤░░░░                             │
                     │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Bitline/WL Pitch (nm)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
       Grid Step (nm)┤▓                                │
                     │▓                                │
      Nominal CD (nm)┤█████████████████                │
                     │█████████████████                │
                     └┬───────┬───────┬───────┬───────┬┘
                      0      90      180     270    360 
```

| Metric | Target Specification | Physical Unit | Measurement Method |
| :--- | :--- | :--- | :--- |
| **Nominal Poly Gate CD ($\langle W \rangle$)** | $180 \pm 5.0$ (Minimum drawn gate: $\ge 150$) | $\text{nm}$ | CD-SEM averaged across array lines |
| **Total Line-Width Roughness ($3\sigma_{\text{LWR}}$)** | $\le 5.0$ (Within manufacturing grid resolution) | $\text{nm}$ | Deconvolved spatial integral $\sqrt{\int PSD(f) df}$ |
| **Total Line-Edge Roughness ($3\sigma_{\text{LER}}$)** | $\le 3.5$ | $\text{nm}$ | Palasantzas fitted model root area |
| **Max Poly Gate to Active Overlay Shift** | $\le 35$ | $\text{nm}$ | Edge position offset relative to diffusion |
| **Array Wordline / Bitline Pitch** | $360 \text{ to } 400$ | $\text{nm}$ | High-density memory array SEM spacing |

---

## 5. References & Literature Context Citations
1. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Placement grid resolution: $0.005\text{ }\mu\text{m}$ ($5\text{ nm}$).
   - Minimum drawn poly gate length: $0.15\text{ }\mu\text{m}$ ($150\text{ nm}$); minimum poly gate spacing: $0.21\text{ }\mu\text{m}$.
   - Maximum allowable overlay error between gate poly and active diffusion: $\le 35\text{ nm}$.
   - DUV 248nm KrF excimer optical criteria: $NA = 0.65$, $k_1 = 0.40$, minimum resolvable half-pitch: $152\text{ nm}$.
2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry: channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - Leakage current target: Sub-threshold and junction leakage $< 1\text{ fA/cell}$ at 85°C.
   - Storage capacitance minimum budget: $28\text{ fF/cell}$ with ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-k stack ($\kappa > 15$).
3. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - 1T1C storage cell with $8F^2$ or $6F^2$ architecture; cell retention time $> 64\text{ ms}$ at 85°C.
   - Bitline and wordline pitch: $360\text{ nm}$ to $400\text{ nm}$.
   - Thermally grown $\text{SiO}_2$ gate dielectric thickness: $\sim 3.5\text{ nm}$.

# SOP: Automated Multi-Angle Spectral Reflectance & Polarimetric Scan Acquisition Across 49 Wafer Sites

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Module**: Metrology / CMP Post-Planarization Thin Film Characterization

## Overview & Rationale
Automated multi-angle polarimetric and spectral reflectance metrology over 49 standard wafer sites evaluates post-CMP planarization profile and residual dielectric layer thickness across 180nm DRAM wafers (folded bitline, stacked capacitor over bitline architectures). Measuring polarization state shifts ($\Psi$, $\Delta$) enables non-destructive extraction of dielectric film parameters and radial film non-uniformity across CMP and furnace runs.

## Process Flowchart
```text
┌────────────────────────┐
│                        │
│   Load Wafer & Align   │
│         Notch          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Z-Height Optical    │
│       Autofocus        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  49-Site Polarimetric  │
│    Scan Acquisition    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      Fresnel Rho       │
│     Dispersion Fit     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Radial Uniformity &   │
│       Acceptance       │
│      Verification      │
│                        │
└────────────────────────┘
```

## Step-by-Step Operating Procedure

1. **Substrate Handling & Chamber Chuck Pre-Alignment**:
   - Transfer the post-CMP 180nm DRAM wafer to the spectroscopic ellipsometer vacuum chuck.
   - Run optical notch centering to align crystallographic orientation within $\pm 0.1^\circ$.
   - Activate automated pneumatic stabilization at 20°C $\pm 0.5^\circ$C.

2. **Optical Focus and Auto-Collimation**:
   - Establish beam incident spot across die scribe-line test pads (minimum clear area corresponding to bitline/wordline pitch scale ~360 nm to 400 nm).
   - Perform automated Z-height laser triangulation autofocus to ensure normal beam tracking within $\pm 0.5\,\mu\text{m}$.

3. **Multi-Angle Polarimetric & Spectral Reflectance Acquisition**:
   - Step across the 49-site polarimetric layout tracking concentric radial zones.
   - For each of the 49 sites, execute broadband spectral reflectance and polarimetric scan:
     - Record rotating analyzer/polarizer intensities across UV-visible-NIR spectrum ($\lambda = 240\,\text{nm} - 800\,\text{nm}$).
     - Acquire polarization angles $\Psi$ (Psi) and $\Delta$ (Delta) defined by the fundamental ellipsometric relation:
       $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot \exp(i\Delta)$$
       where $r_p$ and $r_s$ are the complex Fresnel reflection coefficients.

4. **Model Inversion and Dispersion Parameter Fitting**:
   - Regress measured spectra against Cauchy or Sellmeier dispersion models parameterizing refractive index $n(\lambda)$ and extinction coefficient $k(\lambda)$.
   - Extract physical film thickness ($t$) across each of the 49 sites and compute within-wafer non-uniformity (WIWNU).

## Machine-Measurable Acceptance Criteria

| Parameter | Target Metric | Engineering Unit | Tolerance | Source Reference |
| :--- | :--- | :--- | :--- | :--- |
| **Thin Dielectric / Oxide Measurement Precision** | $\pm 0.05$ | $\text{nm}$ (sub-Ångström) | Max $\pm 0.05\,\text{nm}$ | *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology* |
| **Thick Film / Resist Metrology Precision** | $\pm 2.0$ | $\text{nm}$ | Max $\pm 2.0\,\text{nm}$ | *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology* |
| **49-Site Measurement Completeness** | $100\%$ ($49/49$ sites) | sites / wafer | Exactly 49 valid sites | *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology* |
| **Residual EOT Profile Range** | $3.0 - 4.0$ | $\text{nm}$ | $[3.0, 4.0]\,\text{nm}$ nominal reference | *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering* |

## References & Related Context
- `Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology`: Fundamental equation $\rho = r_p / r_s = \tan(\Psi)\exp(i\Delta)$, Cauchy/Sellmeier models, dry gate oxide measurement precision ($\pm 0.05\,\text{nm}$), photoresist precision ($\pm 2\,\text{nm}$), 49-point wafer mapping.
- `Legacy 180nm DRAM Architecture & Cell Capacitor Engineering`: 180nm cell dimensions, dry oxide thermal thickness ~3.5 nm, EOT 3 to 4 nm, bitline/wordline pitch 360 nm to 400 nm.
- `180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench`: Access transistor $L = 180\,\text{nm}$, $W = 220\,\text{nm}$, tungsten plug (W-plug) contact, cell capacitance budget $\ge 28\,\text{fF}$.

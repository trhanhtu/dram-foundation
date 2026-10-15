# SOP: E-Beam Proximity Effect Correction (PEC) Parameter Calibration and Dose Matrix Generation

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN Council)
- **Status**: Implemented
- **Layer**: Gen 3 (nm) / EBDW Lithography for 180nm Critical Dimension Gates

## Overview & Rationale
Electron Beam Direct Write (EBDW) lithography at sub-micron and deep-submicron scales suffers from electron scattering: forward scattering causing beam broadening (short-range) and backscattering from the substrate creating long-range exposure background across adjacent dense features. Without Proximity Effect Correction (PEC), 180nm access transistor poly gates (drawn channel length $L = 180\,\text{nm}$, minimum drawn gate length down to $150\,\text{nm}$) and adjacent dense arrays (minimum poly gate spacing $0.21\,\mu\text{m}$) experience critical dimension (CD) variations, line-end pullback, and bridging.

This SOP defines the calibration of the Point Spread Function (PSF: $\alpha, \beta, \eta$) and the generation of the fractured dose-assignment matrix on a physical placement grid resolution of $0.005\,\mu\text{m}$ ($5\,\text{nm}$).

## SOP Step-by-Step Procedure

### Step 1: Physical Placement Grid Fracturing & Layout Prep
1. Ingest poly gate layout geometry for 180nm DRAM cell topology ($L = 180\,\text{nm}$, access transistor channel width $W = 220\,\text{nm}$) and SKY130 minimum poly feature ($L = 150\,\text{nm}$, spacing $= 0.21\,\mu\text{m}$).
2. Fracture polygons to the physical placement manufacturing grid resolution of strictly **$0.005\,\mu\text{m}$ ($5\,\text{nm}$)**.
3. Establish pattern density classification bins: isolated gates ($> 1.0\,\mu\text{m}$ clear field) vs. dense DRAM array gates ($0.21\,\mu\text{m}$ spacing).

### Step 2: Point Spread Function (PSF) Parameter Calibration
1. Model the energy deposition distribution $f(r)$ using the standard double-Gaussian formulation:
   $$f(r) = \frac{1}{\pi (1 + \eta)} \left[ \frac{1}{\alpha^2} \exp\left(-\frac{r^2}{\alpha^2}\right) + \frac{\eta}{\beta^2} \exp\left(-\frac{r^2}{\beta^2}\right) \right]$$
2. Expose calibration test structures (clearing dose matrix: isolated lines, line arrays of varying pitches from $0.21\,\mu\text{m}$ to $1.5\,\mu\text{m}$, and contact holes $0.17\,\mu\text{m} \times 0.17\,\mu\text{m}$).
3. Extract empirical forward scattering parameter $\alpha$, backscattering range $\beta$, and backscattering energy ratio $\eta$ by non-linear regression fit against measured resist profile data.

### Step 3: Dose Modulation Matrix Computation
1. Discretize fractured shapes into dose zones bounded by shape edges and proximity interaction zones.
2. Invert the exposure convolution integral across dense memory cells and peripheral logic gates:
   - Assign nominal base dose $D_0$ to semi-dense lines.
   - Modulate isolated gate dose ($D_{\text{iso}} > D_0$) to compensate for lack of background backscattered electrons.
   - Attenuate dense DRAM array gate dose ($D_{\text{dense}} < D_0$) to avoid line-widening and bridging across the $0.21\,\mu\text{m}$ pitch gaps.
3. Map dose assignments to discrete machine exposure dose levels quantized to $5\,\text{nm}$ beam-deflection deflection fields.

### Step 4: Overlay & Exposure Execution Verification
1. Register beam alignment marks to underlying active diffusion layer (minimum diffusion width: $0.15\,\mu\text{m}$).
2. Ensure exposure overlay budget does not exceed the maximum permissible overlay error between gate poly and active diffusion ($\le 35\,\text{nm}$).
3. Transfer dose-corrected fractured stream file to EBDW tool controller.

## Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Measurement Tool / Unit |
| :--- | :--- | :--- |
| **Minimum Poly Gate CD** | $150\,\text{nm} \pm 5\,\text{nm}$ (or $180\,\text{nm} \pm 5\,\text{nm}$ for cell gate) | CD-SEM ($\text{nm}$) |
| **Minimum Poly Spacing Clearance** | $\ge 0.21\,\mu\text{m}$ ($210\,\text{nm}$) without bridging | CD-SEM ($\mu\text{m}$) |
| **Poly-to-Active Overlay Error** | $\le 35\,\text{nm}$ | Optical/SEM Overlay Metrology ($\text{nm}$) |
| **Physical Fracturing Grid Alignment** | Strict integer multiples of $0.005\,\mu\text{m}$ ($5\,\text{nm}$) | GDSII/OASIS Stream Audit ($\text{nm}$) |

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- SkyWater SKY130 Open PDK Design Rules & Lithography Grid
- 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench

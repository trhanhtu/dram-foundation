# Standard Operating Procedure: Cross-Module Aligner Calibration Target Fabrication

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Action Type**: Make
- **Domain**: Architecture & Integration > Photolithography Tooling > Aligner Calibration Target

## Overview & Rationale
This Standard Operating Procedure (SOP) defines the manufacturing and qualification process for a high-precision cross-module aligner calibration artifact fabricated from chromium on quartz. Designed for Gen 2 (µm-scale) photolithographic tool qualification, this artifact standardizes split-field optical channel alignment, Wedge Error Compensation (WEC), and proximity/contact gap leveling across lithography modules.

---

## Process Flow Diagram

```text
┌────────────────────────┐
│   Quartz Substrate &   │
│     Cr Layer Prep      │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  Shipley 1813 Resist   │
│  Spin 4000 RPM 1.3 um  │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Soft Bake at 115C    │
│        for 60s         │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   365nm UV Exposure    │
│     120-150 mJ/cm2     │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Develop Microposit   │
│   MF-319 45-60s & DI   │
│      Water Rinse       │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Chromium Chemical    │
│   Wet Etch & Resist    │
│         Strip          │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│       Metrology        │
│      Calibration       │
│       Acceptance       │
│      Verification      │
└────────────────────────┘
```

---

## Step-by-Step SOP Procedure

### 1. Substrate Preparation & Photoresist Coating
1. Mount an optically polished quartz blank pre-coated with a thin chromium absorber film onto the spin coater chuck.
2. Dispense Shipley 1813 positive photoresist dynamically onto the center of the chromium surface.
3. Spin-coat at **4000 RPM** to establish a uniform resist film thickness of **1.3 µm**.
4. Transfer the coated quartz plate to a flat aluminum hot plate and perform a soft bake at **115°C for 60 seconds**.
5. Allow substrate to cool to ambient cleanroom temperature on a dedicated heat sink.

### 2. Optical Mask Patterning & UV Exposure
1. Position the substrate on a stable macroscopic stage under a projection aligner or primary exposure setup equipped with a 10x Plan Achromat objective (NA 0.25).
2. Measure and calibrate the UV light engine using an optical radiometer (calibrated in $\text{mW/cm}^2$) at the 365 nm (i-line) emission peak.
3. Ensure the illumination source (365nm i-line LED array or 200W Mercury short-arc lamp coupled through a fly's eye integrator lens) achieves **> 95% beam uniformity** across the exposure field.
4. Expose the calibration fiducial layout (including crosshair alignment marks, split-field dual-objective pitch grids, and proximity Vernier scales) with an optimum clear dose of **120 mJ/cm² to 150 mJ/cm²**.

### 3. Development, Chemical Etching, & Strip
1. Immerse the exposed substrate into Microposit MF-319 developer bath for **45 to 60 seconds** under gentle agitation.
2. Immediately transfer the substrate into a cascade deionized (DI) water rinse bath for at least 60 seconds to halt development completely, followed by dry nitrogen ($\text{N}_2$) blow-dry.
3. Inspect patterned photoresist fiducials under an optical microscope to confirm full clearing of exposed features without scumming.
4. Immerse the developed plate into a standard wet chemical chromium etchant to transfer the fiducial geometry into the chromium absorber layer until transparent quartz is exposed in pattern openings.
5. Strip remaining photoresist with solvent/remover bath, rinse thoroughly with DI water, and blow dry with filtered $\text{N}_2$.

### 4. Metrological Verification & Aligner Calibration Mounting
1. Load the finished chromium-on-quartz calibration artifact into the aligner mask holder (e.g., Karl Suss MA6) with vacuum clamping.
2. Verify split-field microscope parfocality across dual binocular objectives (5x, 10x, and 20x) using high-resolution dual CMOS cameras.
3. Perform Wedge Error Compensation (WEC) leveling against a reference chuck using spherical air bearings to ensure parallelism **< 1.0 µm** across a 100 mm reference span.
4. Inspect calibration fiducial feature boundaries under 20x split-field magnification to verify Gen 2 alignment positional tolerance within **±5 µm**.

---

## Machine-Measurable Acceptance Criteria

| Parameter | Nominal Value | Acceptance Range | Measurement Method / Tool |
| :--- | :--- | :--- | :--- |
| **Photoresist Film Thickness** | 1.3 µm | $1.25\ \mu\text{m} \le t \le 1.35\ \mu\text{m}$ | Contact stylus profilometer / Ellipsometer |
| **Exposure UV Dose (365 nm)** | 135 mJ/cm² | $120.0\ \text{mJ/cm}^2 \le \text{Dose} \le 150.0\ \text{mJ/cm}^2$ | Calibrated optical radiometer ($\text{mW/cm}^2 \times \text{s}$) |
| **UV Beam Uniformity** | > 95% | $\ge 95.0\%$ | Multi-point optical radiometer sensor grid across field |
| **Alignment Mark Position / Tolerance (Gen 2)** | 0.0 µm offset | $\le \pm 5.0\ \mu\text{m}$ | Split-field microscope (20x objective, dual CMOS cameras) |
| **WEC Chuck Parallelism** | < 1.0 µm | $\le 1.0\ \mu\text{m}$ across 100 mm | Spherical air bearing leveling mechanical gauge / sensor |

---

## Literature Citations
1. **Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose**: Chromium-on-quartz mask substrate, 365nm (i-line) LED array / 200W Mercury short-arc lamp coupled through fly's eye integrator lens for >95% beam uniformity across wafer, calibrated optical radiometer dose of 120–150 mJ/cm² for Shipley 1813 (1.3 µm thickness), and crosshair alignment marks.
2. **Karl Suss MA6 Mask Aligner Standard Operating Procedure & Gap Control**: Wedge Error Compensation (WEC) leveling chuck via spherical air bearings achieving parallelism < 1 µm across 100mm wafers, split-field binocular microscope with 5x, 10x, and 20x objectives paired with dual CMOS cameras, proximity mode overlay precision of ±2 to 5 µm, and vacuum contact alignment precision $\le 0.5\ \mu\text{m}$.
3. **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**: Microscopic objective (10x Plan Achromat, NA 0.25) resolution, Shipley 1813 spin-coated at 4000 RPM yielding ~1.3 µm thickness, soft bake at 115°C for 60 seconds on a flat aluminum hot plate, high-power 365nm i-line UV source, Microposit MF-319 developer for 45–60 seconds with DI water rinse, and Gen 2 alignment tolerance specification of ±5 µm.

## References & Related Files
- [docs/sop_split_field_optical_system_calibration_proximity_gap_setting.md](../sop_split_field_optical_system_calibration_proximity_gap_setting.md)
- [docs/sop_vernier_scale_optical_overlay_error_cd_metrology.md](../sop_vernier_scale_optical_overlay_error_cd_metrology.md)

# Split-Field Optical System Calibration & Proximity Gap Setting

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Domain**: Architecture & Integration > Microscopic Mask Optical Alignment > Split-Field Optical System Calibration & Proximity Gap Setting

## Overview & Rationale
Precision alignment in proximity photolithography requires rigorous mechanical parallelism compensation, sub-micron gap control, and split-field optical channel parfocality. This procedure standardizes Wedge Error Compensation (WEC) via spherical air bearings and gap positioning (10 µm to 30 µm) to eliminate mask-wafer contact defects while maintaining optical overlay precision within ±2 to 5 µm.

## Standard Operating Procedure (SOP)

### 1. Pre-Alignment & Optical Channel Parfocality Setup
1. Mount the chromium-on-quartz mask onto the mask holder with vacuum retention.
2. Initialize the dual-objective binocular split-field microscope equipped with dual high-resolution CMOS cameras.
3. Configure objective magnification: start at 5x for macro mark search, advance to 10x, and finalize at 20x for micro-alignment.
4. Align optical focus independently across both left and right split-field camera channels to ensure parfocality and sharp contrast on mask fiducial crosshairs.

### 2. Wedge Error Compensation (WEC) Parallelism Calibration
1. Load a 100mm silicon wafer onto the leveling vacuum chuck.
2. Activate the chuck spherical air bearing to enable free multi-axis mechanical tilt articulation.
3. Drive the wafer chuck upward toward the mask reference plane until mechanical leveling engagement is reached.
4. Lock the spherical air bearing mechanically to freeze the planar orientation, achieving wafer-to-mask parallelism < 1.0 µm total indicator reading (TIR) across the 100mm wafer surface.

### 3. Proximity Gap Actuation & Positioning
1. Retract the wafer chuck downward from the leveled mask reference plane using three high-precision differential micrometers or closed-loop piezo actuators with 0.1 µm resolution.
2. Set the proximity printing gap between **10 µm and 30 µm** (nominal 10–20 µm).
3. Verify that zero physical mask-to-photoresist contact occurs, protecting both mask quartz features and resist integrity from scratch defects.

### 4. Split-Field Overlay Verification & Optical Beam Uniformity Check
1. Under 20x split-field magnification, observe wafer and mask fiducial crosshair marks simultaneously across both left and right split-field CMOS channels.
2. Fine-tune stage X, Y, and Theta positioning to achieve operator overlay alignment precision within **±2 µm to ±5 µm** in proximity mode.
3. Verify UV exposure source coupling (365nm i-line LED array or 200W Mercury short-arc lamp through fly's eye integrator lens) delivers **> 95% beam uniformity** across the 100mm exposure field.

---

## Machine-Measurable Acceptance Criteria

| Parameter | Nominal Specification | Acceptance Range | Measurement Method / Tool |
| :--- | :--- | :--- | :--- |
| **WEC Parallelism / Wedge Error** | < 1.0 µm | $\le 1.0\ \mu\text{m}$ across 100mm wafer | Spherical air bearing leveling mechanical gauge |
| **Proximity Air Gap** | 10 µm – 30 µm | $10.0\ \mu\text{m} \le \text{Gap} \le 30.0\ \mu\text{m}$ | 0.1 µm differential micrometers / closed-loop piezo |
| **Proximity Overlay Alignment** | $\le \pm 2.0\ \mu\text{m}$ | $\pm 2.0\ \mu\text{m} \text{ to } \pm 5.0\ \mu\text{m}$ | 20x dual CMOS split-field fiducial crosshair metrology |
| **UV Exposure Beam Uniformity** | > 95% | $\ge 95.0\%$ | Calibrated optical radiometer multi-point sweep |

---

## Literature Citations
1. **Karl Suss MA6 Mask Aligner Standard Operating Procedure & Gap Control**: Wedge Error Compensation (< 1 µm across 100mm wafer, spherical air bearings), Split-field microscope (5x, 10x, 20x objectives, dual CMOS cameras), Proximity gap range (10 µm to 30 µm, resolution ~2.5 µm Fresnel diffraction limit), and Overlay alignment precision (±2 to 5 µm in proximity mode).
2. **Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose**: Differential micrometers and closed-loop piezo actuators (0.1 µm sensitivity), quartz-mask proximity separation (10–20 µm), 365nm i-line / 200W Hg lamp with fly's eye integrator lens achieving > 95% beam uniformity.

## References & Related Files
- [docs/sop_fiducial_overlay_crosshair_micro_positioning_proximity_gap_calibration.md](../sop_fiducial_overlay_crosshair_micro_positioning_proximity_gap_calibration.md)
- [docs/sop_fem_exposure_matrix_lithography_gap_recipe.md](../sop_fem_exposure_matrix_lithography_gap_recipe.md)
- [docs/sop_vernier_scale_optical_overlay_error_cd_metrology.md](../sop_vernier_scale_optical_overlay_error_cd_metrology.md)

# SOP: Travel Straightness, Repeatability & Optical Metrology Calibration

- **Document ID**: SOP-PREC-MET-001
- **Date**: 2026-10-13
- **Author**: Domain Expert AI (Precision Mechanics & Metrology Council, DRAM Foundation VN)
- **Generation**: Gen 1 (mm)
- **Hierarchy**: 180nm Open-Source DRAM Chip > Macroscopic Lithography Linear Stage > Travel Straightness, Repeatability & Optical Metrology Calibration
- **Action Type**: Make

---

## 1. Overview & Purpose
This Standard Operating Procedure (SOP) defines the physical setup, mechanical alignment, travel straightness verification, closed-loop positioning repeatability calibration, and optical metrology alignment for the macroscopic Gen 1 lithography linear stage. 

The stage is engineered to transport wafer substrates across exposure fields and non-destructive optical inspection sites (e.g., photoresist thickness and gate dielectric ellipsometry/reflectometry) while minimizing Abbe errors and mechanical pitch/yaw deviations.

---

## 2. Equipment, Tooling & Physical Context
- **Structural Frame**: Extruded aluminum 4040 structural profile.
- **Linear Guides**: MGN12H precision ground linear guide rails with matching carriage blocks.
- **Drive Mechanism**: C7 rolled ball screws or anti-backlash lead screws.
- **Actuation**: NEMA 17 stepper motors driven at 1/16 microstepping.
- **Vibration Isolation**: Neoprene dampers or Sorbothane isolation pads designed to attenuate vibrations > 30 Hz.
- **Feedback Sensors**: Commercial optical encoders or linear magnetic scales (1 µm native resolution).
- **Measurement Instrumentation**:
  - Precision mechanical dial test indicator (0.5 µm graduation) or laser displacement interferometer.
  - Spectroscopic ellipsometer / reflectometer head (evaluating $\Psi, \Delta$ and Fresnel coefficients $r_p, r_s$ parameterized via Cauchy / Sellmeier dispersion models).

---

## 3. Step-by-Step Procedure

### Phase 1: Vibration Isolation and Structural Rigidity Setup
1. Place the extruded aluminum 4040 base frame on high-damping **neoprene dampers or sorbothane pads** to establish mechanical isolation for environmental frequencies above **30 Hz**.
2. Torque all 4040 joint corner brackets to manufacturer spec to eliminate structural compliance and prevent dynamic tilt or Abbe lever arm amplification.

### Phase 2: MGN12H Rail Mounting and Straightness Dialing
1. Mount the **MGN12H linear guide rails** along the primary datum reference surface of the 4040 aluminum extrusion using M3 low-profile socket screws.
2. Clamp a calibrated dial test indicator to the stage datum edge.
3. Traverse the MGN12H carriage along a 100 mm reference travel segment.
4. Progressively torque mounting fasteners in an alternating sequence from center outward, adjusting rail alignment until total straightness runout is verified strictly **< 5 µm per 100 mm** of travel.

### Phase 3: Drive Mechanism & Closed-Loop Encoder Calibration
1. Couple the **NEMA 17 stepper motor** to the **C7 rolled ball screw** (or anti-backlash lead screw) using a zero-backlash flexible helical/jaw coupling.
2. Configure motor controller driver microstepping to **1/16 microstepping**.
3. Mount the optical linear encoder or linear magnetic scale parallel to the travel axis at minimal offset from the wafer chuck centerline (minimizing Abbe error).
4. Verify linear encoder readout channel synchronization to ensure **1 µm** position feedback resolution.
5. Command forward and backward stepped movements (10 mm steps across a 100 mm envelope) to verify backlash compensation and validate position repeatability.

### Phase 4: Optical Metrology Probe Integration & Wafer Mapping Alignment
1. Mount the optical reflectometer/ellipsometer probe head over the stage travel plane normal to the wafer chuck.
2. Perform baseline calibration across known dielectric thin-film reference standards:
   - Verify dry gate oxide baseline (target: 3.5 nm) within **±0.05 nm** sub-Angstrom precision.
   - Verify photoresist baseline (target: 1.3 µm) within **±2 nm** thickness measurement tolerance using Cauchy/Sellmeier optical models ($\rho = r_p / r_s = \tan(\Psi) \cdot e^{i\Delta}$).
3. Execute an automated **9-point or 49-point wafer mapping** multi-axis sweep to confirm stage positioning stability, coordinate repeat accuracy, and radial non-uniformity tracking.

---

## 4. Acceptance Criteria & Machine-Measurable Targets

| Metric | Target Specification | Measurement Method / Tool | Verification Status |
| :--- | :--- | :--- | :--- |
| **Stage Travel Straightness** | **< 5 µm / 100 mm** | Calibrated dial test indicator / laser runout along MGN12H rail | Pass / Fail |
| **Encoder Feedback Resolution** | **1 µm** | Optical encoder / linear magnetic scale counter register | Pass / Fail |
| **Vibration Cutoff Frequency** | **> 30 Hz** isolation | Accelerometer / Vibrometer on sorbothane/neoprene isolation base | Pass / Fail |
| **Photoresist Metrology Precision** | **±2 nm** (at 1.3 µm PR) | Spectroscopic reflectometry / ellipsometry Cauchy model fit | Pass / Fail |
| **Gate Dielectric Metrology Precision** | **±0.05 nm** (at 3.5 nm oxide) | Spectroscopic ellipsometry ($\Psi, \Delta$) Sellmeier/Cauchy fit | Pass / Fail |
| **Wafer Mapping Grid Scheme** | **9-point or 49-point** pattern | Automated motion sequencer scan log | Pass / Fail |

---

## 5. References & Literature Context
- *Source: Precision Linear Stage Design & Vibration Damping*: 4040 aluminum frame, MGN12H rails (< 5 µm/100mm straightness), C7 rolled ball screws/anti-backlash lead screws, NEMA 17 (1/16 microstepping), neoprene/sorbothane pads (> 30 Hz isolation), optical/magnetic encoders (1 µm resolution).
- *Source: Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*: Angles $\Psi$ and $\Delta$, $\rho = r_p / r_s = \tan(\Psi) \exp(i\Delta)$, Cauchy/Sellmeier dispersion models, dry gate oxide 3.5 nm (±0.05 nm), photoresist 1.3 µm (±2 nm), 9-point/49-point wafer mapping.
- *Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*: Gen 1 lithography substrate registration context.

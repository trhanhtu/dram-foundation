# SOP: Closed-Loop Piezo Proximity Gap Actuator Integration & Baseline Leveling

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Action Type**: Make
- **Domain**: Architecture & Integration > Microscopic Mask Optical Alignment > Split-Field Optical System Calibration & Proximity Gap Setting > Metrology

## Overview & Rationale
In proximity optical lithography for Gen 2 (µm-scale) features, non-contact gap control prevents destructive physical wear and scratch defects between the chromium-on-quartz mask and photoresist-coated wafers. To preserve high optical yield while eliminating mask degradation, closed-loop piezoelectric actuators equipped with capacitive or linear sensor feedback are integrated in a 3-point kinematic mount configuration to achieve sub-micron leveling and baseline gap adjustment.

## Step-by-Step Operating Procedure
1. **Mechanical Tri-Point Actuator Mounting**:
   - Install three closed-loop piezoelectric actuators at 120° radial intervals on the mask stage chuck or wafer chuck leveling interface.
   - Secure the base to rigid linear guide stages (e.g. MGN12H rails on 4040 aluminum extrusion) to eliminate structural compliance and minimize Abbe errors.
2. **Sensor Nulling & Zero Baseline Calibration**:
   - Engage closed-loop positioning feedback and zero-calibrate internal actuator sensors.
   - Coarsely approach the mask using the lead screw / ball screw Z-stage while tracking positioning via linear optical/magnetic encoders (1 µm resolution).
3. **Wedge Error Compensation & Planarity Leveling**:
   - Perform optical split-field fringe detection or capacitive gap sensing across the three actuator points to measure tilt/wedge error.
   - Apply differential voltage offsets across the three piezo channels with 0.1 µm actuation sensitivity until parallel tilt error across the wafer diameter is neutralized.
4. **Proximity Gap Setting & Closed-Loop Locking**:
   - Step all three actuators synchronously to set the target non-contact proximity air gap within 10 µm to 20 µm.
   - Lock PID closed-loop control to suppress drift and attenuate mechanical stage vibrations (> 30 Hz isolated via elastomer damping pads).

## Machine-Measurable Acceptance Criteria
- **Actuator Positioning Sensitivity**: $\le 0.1\ \mu\text{m}$ sensitivity per closed-loop piezo channel.
- **Proximity Air Gap Range**: Target gap maintained between $10\ \mu\text{m}$ and $20\ \mu\text{m}$.
- **Stage Positioning Resolution**: Linear scale feedback resolution within $1\ \mu\text{m}$.
- **Mechanical Vibration Cutoff**: Passive isolation pads damping external vibrations above $30\ \text{Hz}$.

## Literature References
- *Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose*
- *Precision Linear Stage Design & Vibration Damping*

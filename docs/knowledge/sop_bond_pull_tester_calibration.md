# SOP: Bond Pull Tester Calibration and Micro-Hook Alignment Setup

- **Document ID**: SOP-PKG-MET-003
- **Owner**: DRAM Foundation VN Council
- **Target Node**: 180nm Open-Source DRAM (Gen 3)
- **Standard Reference**: MIL-STD-883 Method 2011

## 1. Overview & Rationale
Standard Operating Procedure (SOP) for calibrating the micro-hook load cell and aligning the hook fixture for wire pull metrology on thermosonic gold ball bonds (25 µm Au wire) to 100 µm × 100 µm aluminum bonding pads.

## 2. Calibration & Alignment Workflow

```text
┌────────────────────┐
│                    │
│    Calibration     │
│    Verification    │
│                    │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│                    │
│    Hook Radius     │
│     Inspection     │
│                    │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│                    │
│  Stage & Fixture   │
│     Alignment      │
│                    │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│                    │
│     Micro-Hook     │
│     Engagement     │
│                    │
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│                    │
│  Pull Metrology &  │
│     Validation     │
│                    │
└────────────────────┘
```

## 3. Step-by-Step Procedure
1. **Load Cell Calibration & Tare**:
   - Power on the bond pull tester metrology station.
   - Perform load cell zero-point drift check.
   - Verify calibrated dead weights covering the testing range (target limit >= 4.0 gf) to ensure transducer accuracy within ±0.1 gf.
2. **Micro-Hook Selection & Inspection**:
   - Inspect the micro-hook tip under optical magnification (minimum 50× to 100×).
   - Ensure the inner hook bend radius is sized for 25 µm diameter wire without notches or burrs.
3. **Leadframe / Package Fixturing**:
   - Secure the DRAM die package (die mounted on leadframe via silver-filled epoxy cured at 150°C) onto the vacuum workholder stage.
   - Level the package stage to maintain an orthogonal pull angle (90° ± 5° to the substrate surface).
4. **Hook Positioning & Wire Span Engagement**:
   - Using the micromanipulator joystick, align the hook to the 25 µm Au wire span connecting the 100 µm × 100 µm Al pad to the leadframe pin.
   - Position the hook at the highest apex of the wire loop (or midpoint of the span, per MIL-STD-883 Method 2011).
   - Avoid contact with adjacent wires or pad edges.
5. **Execution & Failure Mode Metrology**:
   - Initiate vertical Z-axis pull at a controlled rate.
   - Record peak force in grams-force (gf).
   - Verify failure mode occurs in the wire span and force satisfies >= 4.0 gf.

## 4. Acceptance Criteria & Target Metrics
- **Pull Force**: >= 4.0 grams-force (gf) for 25 µm diameter Au wire.
- **Bond Pad Footprint**: 100 µm × 100 µm aluminum square.
- **Wire Diameter**: 25 µm 99.99% gold (Au) wire.
- **Failure Mode**: 100% wire-span neck/mid-span break (zero bond pad peeling or ball lift).

## 5. References & Sourced Context
- *Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging* (MIL-STD-883 Method 2011, 25 µm Au wire, 100 µm × 100 µm Al pads, pull test force >= 4.0 gf).

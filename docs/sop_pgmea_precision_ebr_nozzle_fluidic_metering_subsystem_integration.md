# SOP: PGMEA Precision EBR Nozzle & Fluidic Metering Subsystem Integration

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Target Architecture**: 180nm Open-Source DRAM Chip
- **Discipline**: Photolithography / Tool Integration

---

## 1. Overview & Operational Scope
This Standard Operating Procedure (SOP) governs the mechanical assembly, fluidic plumbing, kinematic alignment, and dispense calibration of the PGMEA (Propylene Glycol Monomethyl Ether Acetate) Edge Bead Removal (EBR) subsystem. During high-speed dynamic spin coating of Shipley 1813 photoresist, centrifugal forces and surface tension build up an elevated resist bead along the perimeter of the 100mm silicon wafer. Integrated precision EBR removes this perimeter bead prior to softbake to prevent physical clamp contamination, particle shedding, and edge focal planarity distortion.

---

## 2. Integrated Process Workflow

```text
┌───────────────────────┐
│                       │
│     1. Mechanical     │
│    Subsystem Mount    │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  2. Fluidic Metering  │
│      Integration      │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│     3. Precision      │
│       Kinematic       │
│      Calibration      │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   4. Dynamic Spin &   │
│     EBR Execution     │
│                       │
└───────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Structural Chassis & Linear Stage Mounting
1. Bolt extruded aluminum 4040 structural frame profiles securely to the spin coater granite baseplate.
2. Mount precision-ground MGN12H linear guide rails horizontally over the spin bowl rim to eliminate Abbe offset errors.
3. Install a C7 rolled ball screw (or anti-backlash lead screw) driven by a NEMA 17 stepper motor set to 1/16 microstepping.
4. Seat the base assembly on Sorbothane / neoprene damping pads to isolate environmental vibrations above 30 Hz.

### Step 2: Fluidic Metering & Solvent Plumbing
1. Plumb dedicated high-purity PTFE / PFA chemical lines from the pressurized PGMEA solvent reservoir to a precision micro-dispense solenoid valve.
2. Fasten a solvent-compatible stainless steel micro-nozzle onto the MGN12H carriage bracket, oriented at a 45° impingement angle toward the wafer bevel.
3. Route an anti-drip vacuum pullback / suck-back diaphragm valve directly upstream of the nozzle tip to eliminate residual drool after valve shutoff.

### Step 3: Kinematic Closed-Loop Calibration
1. Calibrate the linear axis using an optical linear magnetic scale with 1 µm resolution.
2. Zero the carriage datum to the wafer outer diameter (100mm substrate).
3. Program the stage trajectory to position the nozzle orifice exactly within the target perimeter exclusion zone (typically 1.0 mm to 3.0 mm from wafer edge) with a mechanical positioning tolerance within ±5 µm (Gen 2 alignment threshold).

### Step 4: Dynamic Spin & EBR Execution
1. Dehydrate 100mm silicon wafer at 150°C–200°C for 30 minutes; perform HMDS vapor prime.
2. Dispense 2–3 mL of Shipley 1813 positive resist at 500 RPM for 5 seconds (spread cycle).
3. Ramp at 10,000 RPM/s to 4,000 RPM for 30 seconds (spin cycle) to establish a 1.30 µm nominal thickness film.
4. During the terminal spin phase (or immediately prior to final dry spin), actuate the PGMEA metering valve to dispense a micro-stream of PGMEA solvent along the spinning wafer bevel.
5. Transfer the wafer to a flat aluminum hot plate and execute softbake at 115°C for 60 seconds.

---

## 4. Machine-Measurable Acceptance Criteria

```text
                     Target Acceptance Criteria Metrics 
                     ┌─────────────────────────────────┐
                     │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
        Film Var (nm)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
                     │▒▒▒▒                             │
    Resist Thick (um)┤▒▒▒▒                             │
   Pos Tolerance (um)┤▓▓▓▓▓▓▓▓▓▓▓▓                     │
                     │▓▓▓▓▓▓▓▓▓▓▓▓                     │
Straightness Dev (um)┤████████████                     │
                     │████████████                     │
                     └┬───────┬───────┬───────┬───────┬┘
                     0.0     3.8     7.5    11.2   15.0 
```

| Metric / Parameter | Target Value | Tolerance / Limit | Physical Units | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Rail Straightness Deviation** | `< 5.0` | Max 5.0 | µm / 100 mm | Dial indicator along MGN12H rail travel |
| **Stage Kinematic Positioning Tolerance** | `±5.0` | Max ±5.0 | µm | Closed-loop linear optical/magnetic scale |
| **Vibration Isolation Cutoff** | `> 30` | Min 30 | Hz | Accelerometer spectrum on 4040 frame |
| **Resist Film Thickness & Uniformity** | `1.30` | ±15 | µm (±nm) | Spectroscopic ellipsometry / reflectometry across 100mm wafer |
| **Hot Plate Softbake Temperature** | `115` | ±1.0 | °C | Calibrated surface thermocouple (60 s dwell) |

---

## 5. Context Literature Citations
- **Precision Linear Stage Design & Vibration Damping**: Extruded aluminum 4040 frames; MGN12H guide rails (< 5 µm / 100 mm straightness); C7 rolled / anti-backlash lead screw with NEMA 17 (1/16 microstepping); Neoprene/Sorbothane isolation (> 30 Hz); 1 µm resolution linear scales.
- **Photoresist Spin Coating Dynamics and HMDS Vapor Priming**: Dehydration bake (150°C–200°C for 30 min); Shipley 1813 dispense (2–3 mL @ 500 RPM for 5 s); 10,000 RPM/s ramp to 4,000 RPM for 30 s producing 1.30 µm ± 15 nm film across 100mm wafers; PGMEA edge bead removal solvent dispense to prevent clamp contamination.
- **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**: Shipley 1813 film baseline (~1.3 µm thickness @ 4,000 RPM); flat aluminum hot plate softbake at 115°C for 60 seconds; Gen 2 alignment tolerance standard of ±5 µm.

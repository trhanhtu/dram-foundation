# Commercial Quartz 5x Photomask Laser/E-Beam Patterning & Cr Etch

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for the procurement, preparation, direct-write laser/e-beam exposure, chemical development, chromium wet/dry etch, and resist strip of 5x commercial quartz reticles intended for 180nm CMOS/DRAM lithography stepper operations.

## Process Flowchart
```text
┌──────────────────────┐
│                      │
│   Quartz Substrate   │
│     Preparation      │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│     Laser E-Beam     │
│      Patterning      │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│  Resist Development  │
│        MF-319        │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│  Chromium Etch and   │
│        Strip         │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│   CD Metrology and   │
│      Inspection      │
│                      │
└──────────────────────┘
```

## Step-by-Step SOP Procedure

### 1. Substrate & Tool Baseline Verification
1. Inspect 6-inch quartz blanks pre-coated with chromium (~100 nm) and positive resist (Shipley 1813 or equivalent e-beam/laser resist) coated to **1.3 µm** thickness (spin-coat equivalent: **4000 RPM**, soft baked at **115°C for 60 seconds** on a precision flat aluminum hot plate).
2. Verify precision positioning stage mechanics: ensure extruded aluminum 4040 frame rigidity, ground MGN12H linear guide rails with travel straightness **< 5 µm / 100 mm**, and NEMA 17 drive with 1/16 microstepping and linear magnetic/optical encoder feedback offering **1 µm** positioning resolution.
3. Validate vibration isolation system (neoprene dampers or sorbothane pads isolating external vibrations **> 30 Hz**).

### 2. Laser / E-Beam Patterning & Exposure
1. Load GDSII/OASIS 5x reticle layout with optical proximity correction (OPC) features and crosshair fiducial alignment marks.
2. Direct-write beam calibration: calibrate exposure source to achieve an optimum clear dose of **120–150 mJ/cm²** (equivalent calibrated 365nm optical radiometer dose for 1.3 µm resist thickness).
3. Ensure beam illumination uniformity **> 95%** across the active exposure field.
4. Execute raster/vector exposure across the quartz plate.

### 3. Post-Exposure Bake & Development
1. Transfer substrate to temperature-controlled development bench.
2. Immerse and agitate in **Microposit MF-319 developer** for **45–60 seconds** at ambient cleanroom temperature (21°C ± 1°C).
3. Transfer immediately to overflowing deionized (DI) water bath and perform a rigorous rinse for $\ge 60$ seconds.
4. Nitrogen blow-dry gently at 20 psi filter line pressure.

### 4. Chromium Pattern Etch & Resist Strip
1. Perform visual inspection of cleared resist windows prior to etch.
2. Immerse substrate in standard chromium etchant (ceric ammonium nitrate / perchloric acid bath) or dry plasma chlorine/oxygen etch until chromium patterns are fully cleared down to the quartz optical substrate.
3. Strip remaining photoresist mask using solvent (NMP/acetone) or oxygen plasma asher.
4. Final cascade DI water rinse and spin-dry.

### 5. Final Metrology & Overlay Inspection
1. Inspect reticle fiducials and critical dimensions (CD) under high-NA optical inspection microscope.
2. Confirm overlay tolerance meets alignment targets (Gen 1 baseline $\pm 100\ \mu\text{m}$, Gen 2 alignment target $\pm 5\ \mu\text{m}$).

## Baseline Metrology Parameter Chart
```text
                             ┌─────────────────────────────┐
                             │░                            │
  Stage Acc / Resolution (um)┤░                            │
                             │▒▒                           │
Stage Straightness (um/100mm)┤▒▒                           │
             Develop Time (s)┤▓▓▓▓▓▓▓▓▓▓▓▓                 │
                             │▓▓▓▓▓▓▓▓▓▓▓▓                 │
          Clear Dose (mJ/cm2)┤█████████████████████████████│
                             │█████████████████████████████│
                             └┬──────┬──────┬──────┬───────┘
                             0.0   33.8   67.5   101.2      
```

## Machine-Measurable Acceptance Criteria Targets
1. **Resist Coating Thickness & Uniformity**: **1.3 µm** thickness (spin-coated at **4000 RPM**, soft-baked at **115°C for 60 seconds**).
2. **Optimum Clear Exposure Dose**: **120 mJ/cm² – 150 mJ/cm²** calibrated at 365nm with beam uniformity **> 95%**.
3. **Development Cleared Time Window**: **45 seconds – 60 seconds** in Microposit MF-319 developer followed by DI water rinse.
4. **Stage Motion Straightness & Positioning Resolution**: Travel straightness **< 5 µm per 100 mm**; closed-loop linear encoder resolution **1 µm**; stage vibration damping effective above **30 Hz**.
5. **Alignment & Fiducial Registration Tolerance**: Gen 1 baseline tolerance **±100 µm** ($\pm 0.1\text{ mm}$), Gen 2 reticle alignment precision **±5 µm**.

## Literature & Context Citations
- *Sam Zeloof Z1 Garage Semiconductor Journal (2018)*: Shipley 1813 spin parameters (4000 RPM, 1.3 µm), soft bake (115°C, 60 s), MF-319 develop time (45–60 s), DI rinse, and alignment tolerances (±100 µm Gen 1, ±5 µm Gen 2).
- *Precision Linear Stage Design & Vibration Damping*: MGN12H linear guide rails (< 5 µm / 100 mm straightness), 4040 frame, NEMA 17 with 1/16 microstepping, 1 µm encoder resolution, and sorbothane/neoprene vibration damping (> 30 Hz).
- *Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose*: Beam uniformity (> 95%), 365nm clear exposure dose calibration (120–150 mJ/cm² for 1.3 µm Shipley 1813), and crosshair fiducial alignment mark mechanics.

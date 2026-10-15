# Downstream Oxygen Plasma Photoresist Ashing

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
This Standard Operating Procedure (SOP) governs the complete stripping and ashing of cross-linked positive photoresist (Shipley 1813, nominal thickness ~1.3 µm) from semiconductor substrates at Gen 1 (mm scale) fabrication tolerances. By utilizing a downstream RF oxygen plasma configuration, energetic ionic bombardment and high-energy UV radiation are confined to the upstream plasma generation zone, exposing the substrate strictly to neutral, thermalized reactive atomic oxygen radicals ($O(^3P)$, $O(^1D)$). This eliminates gate dielectric charging damage and lattice sputtering while volatilizing cross-linked polymeric resist chains into gaseous byproducts ($CO_2$, $CO$, $H_2O$).

## Process Parameters & Architecture

| Parameter | Operational Setpoint | Tolerance | Unit | Function |
| :--- | :--- | :--- | :--- | :--- |
| **RF Generator Power** | 250 | ±5 | W | Primary 13.56 MHz excitation for $O_2$ dissociation |
| **Chamber Process Pressure** | 300 | ±10 | mTorr | Downstream radical transport & mean free path optimization |
| **Base Pressure (Pre-strike)** | < 20 | Max | mTorr | High-vacuum evacuation to purge atmospheric moisture/nitrogen |
| **O2 Process Gas Purity** | ≥ 99.999 | Min | % | Ultra-high purity (UHP) process gas |
| **Target Ashing Film** | Shipley 1813 (~1.3 µm) | Post-bake / cross-linked | µm | Standard positive novolac/diazoquinone resist |

## Step-by-Step Procedure

1. **Substrate Pre-Inspection & Chamber Loading**:
   - Verify wafer status under optical microscope (fiducials within Gen 1 macroscopic tolerance: ±100 µm / 0.1 mm).
   - Vent the loadlock/reaction chamber to atmospheric pressure using high-purity dry $N_2$.
   - Mount the wafer onto the temperature-controlled downstream stage chuck. Close chamber hermetically.
2. **Roughing & Base Vacuum Pumpdown**:
   - Initiate roughing pump cycle to pump down the chamber from atmosphere to base vacuum level (< 20 mTorr).
   - Ensure vacuum seal integrity with leak-up rate < 1 mTorr/min.
3. **Oxygen Gas Inflow & Pressure Stabilization**:
   - Open downstream $O_2$ mass flow controller (MFC).
   - Throttle downstream butterfly control valve until process chamber pressure stabilizes solidly at **300 mTorr**.
   - Allow 30 seconds for gas stabilization and uniform radical flow dynamics.
4. **RF Plasma Ignition & Ashing Run**:
   - Engage 13.56 MHz RF power generator set to **250 W**.
   - Confirm automatic matching network achieves forward power 250 W and reflected power < 5 W.
   - Run active downstream ashing to volatilize cross-linked positive resist into volatile exhaust components ($CO_2$, $CO$, $H_2O$).
5. **Plasma Extinction & Chamber Purge**:
   - Terminate RF power generator output (0 W).
   - Close $O_2$ mass flow controller shutoff valve.
   - Evacuate chamber down to < 20 mTorr for 30 seconds to scavenge residual volatile organic byproducts.
   - Vent chamber back to atmospheric pressure using clean, filtered $N_2$. Unload wafer.
6. **Post-Ash Metrology & Verification**:
   - Inspect wafer under brightfield/darkfield optical microscope.
   - Measure residual film thickness across wafer center and edge using spectroscopic ellipsometry or stylus profilometry.

## Machine-Measurable Acceptance Criteria

1. **Residual Photoresist Thickness**: **0.0 nm (≤ 2.0 nm residual threshold)** across all test sites measured via spectroscopic ellipsometry, confirming 100% removal of initial ~1.3 µm Shipley 1813 film.
2. **RF Delivered Power Stability**: **250 W ± 5 W** continuous forward power with reflected power maintained at **< 5 W** throughout the active strip step.
3. **Chamber Ashing Operating Pressure**: **300 mTorr ± 10 mTorr** steadily maintained by automated throttle valve feedback during plasma discharge.
4. **Substrate Dimensional Stability / Alignment Retention**: Post-strip macroscopic feature shift **< ±100 µm (±0.1 mm)**, conforming to Gen 1 lithographic alignment budget.

## Literature References & Citations
- **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**: Characterization of baseline photoresist processing: Shipley 1813 positive resist spin-coated at 4000 RPM yielding ~1.3 µm thickness, soft bake at 115°C for 60 s, Microposit MF-319 development, and Gen 1 alignment tolerance of ±100 µm (0.1 mm).
- **Karl Suss MA6 Mask Aligner Standard Operating Procedure & Gap Control**: Vacuum chamber evacuation (< 200 mbar absolute), exposure optics calibration, and baseline resist handling.
- **Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose**: Optimum clear dose (120–150 mJ/cm²) for 1.3 µm Shipley 1813 resist and crosshair fiducial alignment standards.

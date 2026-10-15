# SOP: Downstream Oxygen Plasma Photoresist Ashing

- **Date**: 2026-10-16
- **Source**: Domain Expert AI (Gemini)
- **Status**: Implemented
- **Generation**: Gen 1 (mm scale baseline, transitioning to Gen 2 um)
- **Action Type**: Make

## Overview & Rationale
Standard Operating Procedure (SOP) for stripping cross-linked, hard-baked, or post-exposure/developed positive photoresist (Shipley 1813 baseline) using RF downstream oxygen plasma strip. Downstream plasma isolates the wafer from direct ion bombardment and electric fields, utilizing neutral atomic oxygen radicals to chemically oxidize and volatilize organic resist into gaseous byproducts without substrate sputtering or thermal damage.

## Key Physical Process Parameters
- **Process Gas**: Pure Oxygen ($O_2$)
- **Process Pressure**: 300 mTorr
- **RF Plasma Power**: 250 W
- **Target Substrate Temperature**: Chamber ambient / downstream heated platen (< 120°C)
- **Target Material**: Shipley 1813 positive photoresist (~1.3 µm thickness post-spin/soft bake)

## Process Workflow
```text
┌────────────────────────┐
│                        │
│  Load & Chamber Evac   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  O2 Gas Stabilization  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  RF Plasma Ignition &  │
│   Downstream Ashing    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Chamber Purge & Vent  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Metrology Inspection  │
│                        │
└────────────────────────┘
```

## Step-by-Step Procedure
1. **Substrate Preparation & Loading**:
   - Verify previous lithography step: Shipley 1813 coated at 4000 RPM (~1.3 µm) and baked on aluminum hot plate (115°C for 60 s).
   - Load wafer onto the downstream substrate chuck situated below the plasma generation zone to prevent high-energy ion bombardment.
2. **Vacuum Evacuation**:
   - Close chamber and engage roughing pump until base pressure drops below 50 mTorr.
3. **Oxygen Flow & Pressure Stabilization**:
   - Throttle upstream mass flow controller to introduce $O_2$ process gas.
   - Adjust downstream butterfly valve / throttle control to stabilize chamber pressure at exactly **300 mTorr**.
4. **RF Plasma Ignition & Ashing**:
   - Engage RF power supply at **250 W** to ignite oxygen plasma in the upstream discharge cavity.
   - Allow downstream flux of neutral oxygen radicals ($O^\bullet$) to chemically combust organic resist into $CO$, $CO_2$, and $H_2O$ volatiles.
   - Run ashing cycle for calculated duration (nominal 3–5 minutes depending on cross-linking density).
5. **Plasma Extinction & Chamber Venting**:
   - Turn off 250 W RF power.
   - Isolate $O_2$ inlet and pump chamber down to baseline vacuum for 30 seconds to evacuate residual volatile organics.
   - Backfill/vent chamber to atmosphere with dry $N_2$.
6. **Post-Ash Inspection**:
   - Inspect wafer surface via optical microscopy / reflectometry to confirm complete organic removal without residue.

## Acceptance Criteria Target Metrics
- **Chamber Operating Pressure**: $300\text{ mTorr} \pm 15\text{ mTorr}$ (MKS capacitive manometer readout).
- **RF Generator Output Power**: $250\text{ W} \pm 5\text{ W}$ delivered forward power ($< 5\text{ W}$ reflected power).
- **Photoresist Layer Ash Target**: Residual resist thickness of **0 nm** (complete removal of nominal $1.3\text{ \mu m}$ Shipley 1813 film measured via optical reflectometry/ellipsometry).
- **Physical Alignment / Geometric Tolerance**: No distortion to underlying alignment fiducials or substrates within Gen 1 macroscopic tolerance ($\pm 100\text{ \mu m}$ / $0.1\text{ mm}$).

## Literature Citations
- **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**: Shipley 1813 spin-coated at 4000 RPM yielding ~1.3 µm thickness, soft baked at 115°C for 60 s, Gen 1 alignment tolerance at $\pm 100\text{ \mu m}$ ($0.1\text{ mm}$).
- **Karl Suss MA6 Mask Aligner Standard Operating Procedure & Gap Control**: Vacuum contact evacuation (< 200 mbar absolute) and i-line / optical dose calibration context.

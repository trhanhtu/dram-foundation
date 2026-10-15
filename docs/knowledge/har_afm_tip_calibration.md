# High-Aspect-Ratio AFM Tip Calibration and Target Array Navigation

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
In 180nm DRAM fabrication (stacked capacitor over bitline / COB architecture), tungsten plug (W-plug) CMP requires precise quantitative step-height extraction to evaluate plug recess and ILD oxide dishing without tip artifact convolution. Because bitline and wordline pitches span 360 nm to 400 nm with critical feature length $L = 180\text{ nm}$ and contact width $W = 220\text{ nm}$, standard pyramidal AFM tips fail to penetrate high-aspect-ratio (HAR) recesses due to sidewall contact limits. This SOP defines high-aspect-ratio (HAR) AFM tip qualification, blind tip estimation/calibration on reference gratings, and automated optical/piezo array navigation into the dense memory core.

## Key Details / Architecture
- **Metrology Node**: 180nm CMOS MPW DRAM array.
- **Probe Specifications**: High-aspect-ratio silicon/diamond-like carbon probe with tip shank length $\ge 2\ \mu\text{m}$, half cone angle $< 3^\circ$, and nominal apex radius $R_{\text{tip}} \le 10\text{ nm}$.
- **Target Cell Geometry**:
  - Transistor gate length: $L = 180\text{ nm}$
  - Active width: $W = 220\text{ nm}$
  - Wordline / bitline pitch: $360\text{ nm}$ to $400\text{ nm}$
- **Workflow**:
  1. Tip mounting and resonance tuning in tapping/peak-force mode.
  2. Characterization scan over sharp silicon spike calibration standard for tip geometry blind reconstruction.
  3. Global wafer alignment via optical microscope and step-and-repeat coordinate navigation to target die.
  4. Local fine-pitch alignment over dense 1T1C memory array field ($2.0\ \mu\text{m} \times 2.0\ \mu\text{m}$ scan field).
  5. High-density line-profilometry across bitline contact W-plugs.

## References & Related Files
- [docs/context.yaml](..../../context.yaml)
- [docs/context2.yaml](..../../context2.yaml)
- [docs/context3.yaml](..../../context3.yaml)

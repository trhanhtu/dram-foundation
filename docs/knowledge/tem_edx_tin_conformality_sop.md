# TEM-EDX Line-Scan Profile Extraction and Step Coverage Conformality Quantification

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Accepted

## Overview & Rationale
Standard Operating Procedure (SOP) for quantifying TiN electrode step coverage and atomic composition profiles along high-aspect-ratio (HAR) 3D stacked crown capacitors in an open-source 180nm DRAM node (8F² / 6F² folded bitline architecture).

## Key Details / Architecture
- **Specimen Architecture**: 180nm 1T1C stacked capacitor over bitline (COB), cell footprint 8F² / 6F², bitline pitch 360 nm to 400 nm, access transistor L = 180 nm, W = 220 nm. High-k capacitor dielectric: Ta2O5 / Al2O3 or ONO stack (kappa > 15, EOT 3 to 4 nm, C_cell >= 28 fF).
- **Metrology Node**: Analytical STEM-EDX (200 kV Field Emission Gun, SDD EDX spectrometer).
- **Physical Line Scan Vectors**:
  1. Top flat surface electrode ($t_{\text{top}}$)
  2. Upper sidewall ($z = 80\%$ height)
  3. Mid sidewall ($z = 50\%$ height)
  4. Lower sidewall ($z = 20\%$ height)
  5. Bottom crown trench floor ($t_{\text{bottom}}$)
- **Conformality Metric**: 
  $$\text{Conformality} = \frac{t_{\text{bottom}}}{t_{\text{top}}} \times 100\% \ge 90\%$$

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

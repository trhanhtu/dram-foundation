# Automated Sequential Wet Bench Immersion Run & Marangoni Dry Execution

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the leaf Standard Operating Procedure (SOP) for sequential SC-1 / DHF 50:1 / SC-2 chemical clean and Marangoni drying across 180nm DRAM wafer fabrication before critical capacitor or gate oxidation steps. Eliminates particle contamination, organic residues, native oxides, and metallic ions while preventing water-mark defect formation on hydrophobic silicon surfaces.

## Key Details / Architecture
- **Stage 1 (SC-1 / RCA-1)**: 5:1:1 DI H2O : NH4OH (29%) : H2O2 (30%) at 70°C–80°C for 10–15 min. Removes organic residues and light metals.
- **Intermediate Quick Dump Rinse (QDR)**: 18.2 MΩ·cm DI water dump rinse for 3 minutes.
- **Stage 2 (DHF 50:1 Oxide Strip)**: 1:50 HF:H2O at ambient (25°C) for 15–30 seconds. Strips native oxide; surface transitions from hydrophilic to hydrophobic. Safety requires calcium gluconate gel on site.
- **Intermediate Quick Dump Rinse (QDR)**: 18.2 MΩ·cm DI water dump rinse for 3 minutes.
- **Stage 3 (SC-2 / RCA-2)**: 6:1:1 DI H2O : HCl (37%) : H2O2 (30%) at 70°C–80°C for 10 minutes. Eliminates alkali ions (Na+, K+) and heavy metals (Fe, Cu, Ni).
- **Stage 4 (Marangoni Dry / N2 Final Dry)**: Slow automated pull through isopropyl alcohol (IPA) / N2 vapor boundary with surface-tension gradient drying, supplemented by high-purity N2 blow-dry.

## References & Related Files
- [Standard RCA-1 and RCA-2 Silicon Wafer Cleaning Procedure](./sop_wet_bench_rca_marangoni.md)
- [Silicon Dioxide Etching with Buffered Oxide Etch (BOE)](./sop_wet_bench_rca_marangoni.md)

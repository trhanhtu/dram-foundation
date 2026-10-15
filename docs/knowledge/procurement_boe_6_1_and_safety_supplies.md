# Procurement & Safety Specifications for Electronic-Grade BOE 6:1 (180nm DRAM Line)

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Buffered Oxide Etch (BOE 6:1) is the critical wet chemical agent used in the 180nm DRAM fabrication flow for oxide patterning, pre-diffusion cleaning, and gate oxide etching. Because BOE contains Hydrofluoric Acid (HF), procurement requires strict technical lot characterization alongside mandatory life-safety counter-measures (Calcium Gluconate Gel).

## Key Technical Specifications
- **Chemical Formulation**: 6 parts $40\%\ \text{NH}_4\text{F}$ to 1 part $49\%\ \text{HF}$.
- **Thermal $\text{SiO}_2$ Etch Rate Baseline**: $100\text{ nm/min}$ ($1000\ \text{\AA/min}$) at $25^\circ\text{C}$.
- **Surfactant / Wetting Agent**: $0.1\%$ Triton X-100 or Fluorad to prevent micro-bubble entrapment in DRAM trenches ($360\text{ nm} - 400\text{ nm}$ pitch).
- **Life Safety Antidote**: Calcium Gluconate Gel ($2.5\%$) staged in redundant, unexpired units at every transfer point to mitigate systemic calcium binding upon accidental skin exposure.

## References & Related Files
- [sop_procurement_boe_6_1_safety_supplies.md](.../../sop/sop_procurement_boe_6_1_safety_supplies.md)
- [sop_boe_6_1_sio2_patterning.md](.../../sop_boe_6_1_sio2_patterning.md)

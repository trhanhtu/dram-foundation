# Idea & Micro-Knowledge: Procurement & Qualification Protocols for RCA-1 Chemistry and Megasonics

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
In 180nm DRAM fabrication (stacked capacitor COB architecture with $L = 180\ \text{nm}$, $W = 220\ \text{nm}$ access transistors and sub-$1\ \text{fA/cell}$ leakage limits), gate oxide growth at 3.5 nm requires ultra-clean silicon surfaces devoid of organic films, light metallic contamination, and sub-micron particles. Formulating the RCA-1 (SC-1) bath requires high-purity semiconductor-grade reagents ($29\%\ \text{NH}_4\text{OH}$, $30\%\ \text{H}_2\text{O}_2$) and $18.2\ \text{M}\Omega\cdot\text{cm}$ DI water, paired with megasonic bath immersion to dislodge nanoscale contaminants without damaging gate oxide interfaces.

## Key Details / Architecture
1. **Reagent Formulation Specification**:
   - $5:1:1\ \text{DI H}_2\text{O} : \text{NH}_4\text{OH} (29\%) : \text{H}_2\text{O}_2 (30\%)$.
   - Electronic/trace metal grade ($<10\ \text{ppb}$ metal ions).
2. **Megasonic Immersion Bath Integration**:
   - PFA/quartz immersion vessel operating at $800\ \text{kHz} - 1.2\ \text{MHz}$ acoustic frequency.
   - PFA-sheathed immersion heater maintaining steady-state temperature at $70^\circ\text{C}\text{--}80^\circ\text{C}$.
   - Process time calibrated for $10\text{--}15\ \text{minutes}$.
3. **Traceability to Architecture**:
   - Cleanliness directly protects gate dielectric breakdown voltage and leakage budget of the 180nm DRAM cell.

## References & Related Files
- [sop_procurement_reagents_megasonic_immersion_bath.md](.../../sop/sop_procurement_reagents_megasonic_immersion_bath.md)
- [context.yaml](.../../context.yaml)

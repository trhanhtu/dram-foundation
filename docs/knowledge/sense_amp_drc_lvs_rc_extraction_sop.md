# Sense Amp Stripe DRC/LVS Verification & Parasitic RC Bitline Imbalance Extraction

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM

## Overview & Rationale
Detailed Standard Operating Procedure (SOP) for Design Rule Checking (DRC), Layout Versus Schematic (LVS), and Parasitic RC extraction of interleaved folded bitline CMOS sense amplifiers and equalizers at the 180nm node. Focuses on pitch matching (360 nm), cell capacitance margin, bitline capacitance matching, and differential sensing signal margin ($\Delta V$).

## Key Details & Metrics
- Pitch Matching: 360 nm interleaved layout pitch.
- Access Transistor Dimensions: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
- Storage Capacitance: $C_s \ge 28\text{ fF}$ (typical nominal $25\text{ fF}$ to $28\text{ fF}$).
- Bitline Capacitance: $C_{BL} = 250\text{ fF}$.
- Developed Signal: $\Delta V = 100\text{ mV}$ to $150\text{ mV}$.
- Leakage Limit: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- [docs/knowledge/sense_amp_drc_lvs_rc_extraction_sop.md](./sense_amp_drc_lvs_rc_extraction_sop.md)

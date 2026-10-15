# DRAM Defect Signature Classifier for Retention Leakage & Cell Access Failures

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defect classification rules for 180nm folded bitline DRAM cells to discern retention leakage faults (capacitor dielectric ONO/Ta2O5, junction breakdown) from access transistor/bitline transfer failures ($C_b/C_s$ mismatch, W-plug contact resistance, drive collapse).

## Key Metrology Budgets
- Storage Node Capacitance ($C_s$): $\ge 25\text{ to }30\text{ fF}$ (nominal $28\text{ fF}$).
- Bitline Parasitic Capacitance ($C_b$): $150\text{ to }250\text{ fF}$ per 256/512 cell array block.
- Capacitance Ratio ($C_b / C_s$): $5:1\text{ to }9:1$ (Severe degradation if $> 10:1$).
- Retention Limit ($T_{\text{ret}}$): $> 64\text{ ms}$ at $85^\circ\text{C}$.
- Total Cell Leakage ($I_{\text{leak}}$): $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/sop_dram_defect_signature_classifier.md](./docs/sop_dram_defect_signature_classifier.md)

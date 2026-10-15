# SOP: Process Parameter Benchmarking for Post-Fill LVS & Electrical Rule Check (ERC) Sign-Off

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented
- **Module**: [Metrology / Process Engineering] DRAM Foundation VN 180nm MPW Tapeout

## Overview & Rationale
After dummy metal fill synthesis across interconnect layers, parasitic capacitances and layout topologies must be re-benchmarked prior to final foundry GDSII tapeout. Post-fill Layout Versus Schematic (LVS) and Electrical Rule Checks (ERC) verify that dummy tiles do not cause accidental shorts, open circuits, well-bias violations, excessive coupling noise, or capacitive degradation that violates the strict read signal margins of the 180nm 1T1C stacked capacitor DRAM cell.

## Key Physical Verification & Benchmarking Workflow
1. **LVS Extraction & Topology Verification**: Verify NMOS access transistor dimensions ($L = 180\text{ nm}$, $W = 220\text{ nm}$) and folded bitline 8F² cell footprint ($0.259\ \mu\text{m}^2$) with zero short/open violations against schematic netlists.
2. **Post-Fill Parasitic Extraction (PEX)**: Extract full distributed RC networks including dummy fill coupling to bitlines ($C_b$) and wordlines.
3. **Capacitance Budget & Ratio Benchmarking**: Benchmark extracted bitline capacitance ($C_b$) against storage node capacitance ($C_s$). Ensure $C_b / C_s$ strictly complies with the target window to safeguard sense amplifier sensing margins.
4. **Interconnect Sheet Resistance & ERC Well Bias**: Validate Metal-1 sheet resistance ($R_s < 0.08\ \Omega/\Box$) and ensure no floating dummy fills, antenna rule breaches, or substrate/well tap isolation violations.

## Acceptance Criteria Targets
- Storage Node Capacitance ($C_s$): $\ge 25\text{ fF}$ to $30\text{ fF}$ per cell (Nominal: $28\text{ fF}$).
- Bitline-to-Storage Capacitance Ratio ($C_b / C_s$): Between $5:1$ and $9:1$ (Max allowed $< 10:1$).
- Storage Node Total Leakage ($I_{\text{leak}}$ at $85^\circ\text{C}$): $< 1.0\text{ fA/cell}$.
- Metal-1 (Al/Al-Cu) Interconnect Sheet Resistance ($R_s$): $< 0.08\ \Omega/\Box$ (350 nm ± 5% target thickness).

## References & Related Files
- `180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench`
- `1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets`
- `Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects`
- [docs/context.yaml](./docs/context.yaml)

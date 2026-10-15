# SOP: Array Macro & Periphery Hierarchical Layout Placement & Global Pin Alignment

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 3 (180nm)
- **Hierarchy**: Top-Level DRAM Core & Periphery GDSII Stream-Out and Seal Ring Integration > DRAM Core & Periphery Hierarchical GDSII Assembly and Layer Stream-Out > Array Macro & Periphery Hierarchical Layout Placement & Global Pin Alignment

## Overview & Rationale
Establishes the step-by-step physical implementation protocol for placing the dense 180nm 1T1C DRAM core array macros alongside periphery circuits (row decoders, sense amplifiers, column decoders, control logic) and ensuring exact on-pitch global pin snapping to preserve bitline/wordline integrity and keep parasitic capacitance within critical budget limits.

## Key Physical Budgets & Parameters
- **Unit Cell Layout**: Folded bitline 8F^2 footprint ($0.259\ \mu\text{m}^2$) or open bitline 6F^2 footprint ($0.194\ \mu\text{m}^2$) at feature size $F = 180\ \text{nm}$.
- **Access Transistor Dimensions**: Channel length $L = 180\ \text{nm}$, channel width $W = 220\ \text{nm}$.
- **Interconnect Pitch**: Bitline (BL) and Wordline (WL) pitch = $360\ \text{nm}$ to $400\ \text{nm}$.
- **Storage Node Capacitance ($C_s$)**: $25\ \text{fF}$ to $30\ \text{fF}$ per cell (Nominal: $28\ \text{fF}$).
- **Bitline Parasitic Capacitance ($C_b$)**: $150\ \text{fF}$ to $250\ \text{fF}$ per bitline (for array sub-blocks of 256 or 512 cells/BL).
- **Capacitance Ratio ($C_b / C_s$)**: Must remain between $5:1$ and $9:1$ (strictly $< 10:1$).
- **Sub-threshold & Junction Leakage**: $< 1\ \text{fA/cell}$ at $85^\circ\text{C}$ to maintain retention time $> 64\ \text{ms}$.

## References & Related Files
- `180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench`
- `1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets`
- `Legacy 180nm DRAM Architecture & Cell Capacitor Engineering`

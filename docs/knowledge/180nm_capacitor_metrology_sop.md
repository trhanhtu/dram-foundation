# Micro-Knowledge: 180nm DRAM Stacked Crown Capacitor Metrology Protocol

- **Date**: 2026-10-15
- **Source**: Agent (Synthesized from Verified Literature)
- **Status**: Implemented

## Overview & Rationale
Defines the standard physical metrology, high-frequency C-V, thermal leakage, and TEM lamella inspection parameters for 180nm 1T1C stacked crown capacitors (MIM or ONO/Ta2O5 dielectric stacks).

## Key Details / Architecture
- **Capacitance Requirements**: Storage capacitance $C_s \ge 25\text{ fF}$ (nominally $28\text{ fF}$ to $30\text{ fF}$) with bitline-to-cell ratio $C_b/C_s$ strictly between $5:1$ and $9:1$.
- **Leakage Floor**: $I_{\text{leak}} \le 1.0\text{ fA/cell}$ at $85^\circ\text{C}$ to satisfy $> 64\text{ ms}$ retention time at 180nm.
- **Equivalent Oxide Thickness (EOT)**: $3.0\text{ nm}$ to $4.0\text{ nm}$ with $\kappa > 15$ for $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ or ONO stacked high-k layers.
- **Physical Integration Gate**: Access NMOS geometry $L=180\text{ nm}, W=220\text{ nm}$, gate dielectric physical thickness $\sim 3.5\text{ nm}$ grown at $850^\circ\text{C}-900^\circ\text{C}$, connected via W-plug drain contact.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/knowledge/180nm_cell_topology.md)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/knowledge/legacy_180nm_dram.md)
- [1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets](./docs/knowledge/1t1c_folded_bitline_budgets.md)

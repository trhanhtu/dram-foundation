# Foundry Rule Deck Correlation & MPW Physical Sign-Off Audit

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Accepted

## Overview & Rationale
Defines the standard correlation protocol between standard commercial 180nm CMOS MPW foundry design rule decks (DRC/LVS/fill) and custom DRAM cell rules (capacitor-over-bitline crown MIM/stacked topologies, sub-threshold leakage, and boosted overdrive limits). Prevents false-positive violations while strictly enforcing cell capacitance margins and noise budgets prior to tapeout sign-off.

## Key Details / Architecture
- **Process Technology**: 180nm CMOS Logic MPW + Custom DRAM Add-On (Gen 3).
- **Cell Geometry**: 8F² folded bitline ($0.259\ \mu\text{m}^2$, $F = 180\ \text{nm}$), access transistor $L = 180\ \text{nm}$, $W = 220\ \text{nm}$.
- **Storage Capacitor**: Stacked crown MIM / Poly-Insulator-Poly with ONO / high-$k$ dielectric ($\kappa > 15$). Target $C_s \ge 28\ \text{fF}$.
- **Bitline Budget**: $C_b = 150\ \text{fF}$ to $250\ \text{fF}$ for 256/512 cells per bitline; $C_b / C_s \in [5:1, 9:1]$.
- **Leakage & Boosting**: Sub-threshold and junction leakage $< 1\ \text{fA/cell}$ at $85^\circ\text{C}$; Wordline boost $V_{PP} = 2.6\ \text{V}$ to $2.8\ \text{V}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

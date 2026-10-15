# Quality Acceptance & Metrology Protocol for Post-Fill LVS & Electrical Rule Check (ERC) Sign-Off

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented / Approved

## Overview & Rationale
Defines the sign-off verification protocol for post-dummy metal fill Layout Versus Schematic (LVS) and Electrical Rule Check (ERC) on the 180nm Open-Source DRAM Chip MPW shuttle package. Ensures dummy metal and poly fill synthesis do not cause net shorts, opens, substrate latch-up hazards, or degrade cell/bitline capacitance budgets below specified circuit margins.

## Key Details / Architecture
- **Target Cell Geometry**: Access NMOS transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$.
- **Storage Node Topology**: Stacked capacitor over bitline (COB) with ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-k stack ($\kappa > 15$).
- **Bitline Topology**: Folded bitline ($8F^2 = 0.259\ \mu\text{m}^2$, 256 or 512 cells per bitline).
- **Parasitic Extraction**: Storage node capacitance $C_s \ge 25\text{ fF}$ to $30\text{ fF}$ (nominal $28\text{ fF}$), Bitline parasitic $C_b = 150\text{ fF}$ to $250\text{ fF}$, ratio $C_b / C_s \in [5:1, 9:1]$ ($< 10:1$).
- **Pad & Packaging Checks**: $100\ \mu\text{m} \times 100\ \mu\text{m}$ aluminum pads, bonding pull strength $\ge 4.0\text{ gf}$ ($25\ \mu\text{m}$ wire, Mil-Std-883 Method 2011).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

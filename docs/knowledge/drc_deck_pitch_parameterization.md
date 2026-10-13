# DRC Deck Customization & Wordline/Bitline Pitch Rule Parameterization

- **Date**: 2026-10-13
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines physical layout parameterization and DRC deck deck customization rules for 180nm Open-Source DRAM (Folded Bitline 8F² architecture). Ensures that cell pitch scaling does not violate bitline-to-cell capacitance budgets ($C_b/C_s \le 9:1$), boosted wordline gate oxide reliability constraints ($V_{PP} \ge 2.5\,\text{V} - 2.8\,\text{V}$), or minimum sensing signal margins ($\Delta V \ge 100\,\text{mV}$).

## Key Details / Architecture
- **Technology Node**: 180nm ($F = 0.18\,\mu\text{m}$).
- **Topology**: 8F² Folded Bitline layout ($A_{\text{cell}} = 0.259\,\mu\text{m}^2$).
- **Bitline Pitch ($P_{BL}$)**: Nominal $2F = 0.36\,\mu\text{m}$ (Min metal width $0.18\,\mu\text{m}$, min spacing $0.18\,\mu\text{m}$).
- **Wordline Pitch ($P_{WL}$)**: Nominal $4F = 0.72\,\mu\text{m}$ along active line or $2F$ staggered equivalent.
- **Voltage Enclosure**: Polysilicon wordline gate spacing and oxide isolation tuned for boosted $V_{PP} \ge 2.5\,\text{V}$ to prevent dielectric breakdown while eliminating $V_{th}$ threshold loss ($1.8\,\text{V} - 0.6\,\text{V} = 1.2\,\text{V}$).
- **Capacitance Targets**: $C_s = 25 - 30\,\text{fF}$ (nominally $28\,\text{fF}$), $C_b = 150 - 250\,\text{fF}$ for 256/512 cell array blocks. $C_b/C_s$ maintained between $5:1$ and $9:1$.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

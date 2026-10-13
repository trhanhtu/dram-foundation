# Differential Sense Margin ΔV Sensitivity & PVT Corner Sign-off

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Accepted

## Overview & Rationale
Standard Operating Procedure (SOP) for metrology sign-off of differential sense margin $\Delta V$ across process, voltage, and temperature (PVT) corners in an open-source 180nm 1T1C stacked capacitor DRAM cell architecture (folded-bitline configuration).

## Key Details / Architecture
- Folded bitline precharge equalized to $V_{DD}/2$.
- Differential signal development: $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right)$.
- Process corners: TT, SS, FF. Temperature range: 25°C to 85°C.
- Leakage and retention boundary conditions: $\le 1\text{ fA/cell}$ sub-threshold/junction leakage at 85°C ensuring $> 64\text{ ms}$ data retention.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- [docs/context3.yaml](../context3.yaml)

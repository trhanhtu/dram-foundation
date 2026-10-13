# SOP: Boundary Routing, Shielding & Dummy Metal Fill Insertion

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Accepted
- **Context**: 180nm Open-Source DRAM Chip (Gen 2 µm) > Folded Bitline CMOS Sense Amplifier & Equalizer > Folded Bitline Pitch-Matched Layout & DRC/LVS Extraction > Boundary Routing, Shielding & Dummy Metal Fill Insertion

## Overview & Rationale
In high-density 180nm folded bitline DRAM arrays (8F² cell area = 0.259 µm²), pitch-matched sense amplifiers (SA) and equalizers transition at the block boundaries to array routing and peripheral control circuitry. At this boundary, asymmetric capacitive coupling, edge fringing fields, and chemical-mechanical planarization (CMP) dishing can destroy differential bitline balance. 

To maintain signal development ($\Delta V = 100\text{ mV}$ to $150\text{ mV}$), the total parasitic bitline capacitance ($C_b$) must remain within $150\text{ fF}$ to $250\text{ fF}$, preserving the strict capacitance ratio $C_b / C_s$ between $5:1$ and $9:1$ against the nominal storage node capacitance ($C_s \ge 25\text{ fF}$ to $30\text{ fF}$, nominally $28\text{ fF}$). This SOP standardizes boundary routing pitch transitions, quiet reference shielding ($V_{DD}/2$ precharge / equalization lines), and density-compliant dummy metal fill insertion.

## Key Details & Architecture
1. **Boundary Pitch Transition**: Route bitlines from the dense 8F² core array ($F = 180\text{ nm}$) to the sense amplifier pitch with strict symmetrical differential pair lengths and matched via transitions.
2. **Shielding**: Enforce quiet DC/reference shielding ($V_{DD}/2$ equalization bias or Ground planes) adjacent to exterior boundary bitlines to suppress inter-block capacitive crosstalk.
3. **Dummy Metal Fill Insertion**: Insert slotted or stepped dummy metal patches respecting exclusion keep-out zones around complementary bitline pairs (BL and /BL) to prevent parasitic capacitive loading overshoots beyond $250\text{ fF}$.
4. **Post-Fill RC Extraction & Verification**: Perform corner extraction to verify differential balance ($|\Delta C_b| \le 1.0\text{ fF}$) and prevent $C_b / C_s$ exceeding $10:1$.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- [docs/context3.yaml](../context3.yaml)

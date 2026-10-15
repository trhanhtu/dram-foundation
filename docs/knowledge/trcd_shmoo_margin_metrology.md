# tRCD Shmoo Plot Margin Metrology & JEDEC Timing Compliance Verification

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Accepted
- **Context Path**: 180nm Open-Source DRAM Chip > ESP32 Closed-Loop Motor Controller > FPGA High-Speed DRAM Memory Controller Core > FPGA Hardware-in-the-Loop Timing Metrology > Differential Bitline Sensing Delay Characterization & tRCD Timing Margin Metrology

## Overview & Rationale
Defines the standard operating procedure for characterizing row-to-column command delay ($t_{RCD}$) margin across supply voltage and ambient operating temperature windows (Shmoo plots) for 180nm folded bitline stacked-capacitor DRAM fabricated under open-source PDK guidelines.

## Physical Parameters & Architecture Constraints
- **Process Generation**: 180 nm CMOS ($L = 180\text{ nm}, W = 220\text{ nm}$).
- **Topology**: $8F^2$ Folded Bitline layout ($0.259\ \mu\text{m}^2$ cell footprint).
- **Storage Cell Node ($C_s$)**: Nominal $28\text{ fF}$ (valid window $\ge 25\text{ fF}$ to $30\text{ fF}$).
- **Bitline Parasitic Capacitance ($C_b$ / $C_{BL}$)**: $150\text{ fF}$ to $250\text{ fF}$ (256/512 cells per bitline).
- **Capacitance Ratio Target**: $C_b / C_s$ maintained between $5:1$ and $9:1$ ($< 10:1$).
- **Differential Read Signal Margin**: $\Delta V = \frac{C_s}{C_{BL} + C_s} \times (V_{cell} - V_{DD}/2) \approx 100\text{ mV}$ to $150\text{ mV}$.
- **Storage Retention Leakage**: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

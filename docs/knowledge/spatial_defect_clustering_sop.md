# Spatial Defect Clustering Classification & Yield Signature Spatial Analysis

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN Council)
- **Status**: Accepted

## Overview & Rationale
Standard Operating Procedure (SOP) and spatial metrology analysis protocol for 180nm Open-Source DRAM Chip (Gen 3). Establishes automated fail-bitmap spatial classification, de-aliasing physical layout coordinates, spatial density clustering (DBSCAN/Hough), yield signature pattern recognition, and inline feedforward dispositioning.

## Key Details & Physical Parameters
- **Unit Cell & Footprint**: 180nm gate length $L = 180\text{ nm}$, width $W = 220\text{ nm}$, 8F² folded bitline footprint ($0.259\ \mu\text{m}^2$) and 6F² open bitline footprint ($0.194\ \mu\text{m}^2$).
- **Array Wiring Pitch**: Wordline pitch $360\text{ nm}$ to $400\text{ nm}$, Bitline pitch $360\text{ nm}$ to $400\text{ nm}$.
- **Electrical Storage Constraints**: Storage node capacitance $C_s \ge 25\text{ fF}$ to $30\text{ fF}$ (nominal target $28\text{ fF}$), equivalent oxide thickness $\text{EOT} = 3\text{ to } 4\text{ nm}$ (Ta₂O₅/Al₂O₃ high-$k$ stack or ONO), bitline capacitance $C_b = 150\text{ to } 250\text{ fF}$ per 256/512-cell segment ($C_b / C_s$ kept between $5:1$ and $9:1$, threshold max $10:1$).
- **Spatial Signature Taxonomies**: Ring/Perimeter Edge, Scratch/Linear Streak, Reticle Repeater, Sub-array Column/Row Cross, and Micro-Cluster Spurious Leakage ($I_{\text{leak}} > 1\text{ fA/cell}$ at $85^\circ\text{C}$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

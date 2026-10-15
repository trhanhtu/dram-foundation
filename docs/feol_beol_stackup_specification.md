# SOP: FEOL/BEOL Layer Thickness & Material Permittivity Specification

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Chip

## Overview & Scope
Standard operating procedure defining the exact physical layer thicknesses, material compositions, and relative permittivity ($\kappa$) stackup for 3D field solver parasitic extraction (PEX) of the 180nm 1T1C $8F^2$ DRAM cell topology.

## Process Stackup & Dielectric Parameters

| Stack Level | Layer Name | Material | Physical Thickness | Relative Permittivity ($\kappa$) / EOT | Source & Process Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FEOL** | Gate Oxide ($T_{ox}$) | Thermally grown $\text{SiO}_2$ | $3.5\text{ nm}$ | $\kappa \approx 3.9$ | $850^\circ\text{C}-900^\circ\text{C}$ dry oxidation |
| **FEOL** | Access Transistor Gate | Polycide / Poly-Si | Channel $L = 180\text{ nm}$, $W = 220\text{ nm}$ | Conductor | Access transistor channel |
| **FEOL/MOL** | Contact & Inter-Poly Dielectric | Pre-Metal Dielectric ($\text{SiO}_2$/BPSG) | Pitch $360\text{ nm}-400\text{ nm}$ | $\kappa \approx 3.9-4.1$ | Shared BL contact between adjacent cells |
| **MOL** | Contact Plugs | Tungsten (W-Plug) | High aspect ratio contact | Conductor | Drain & storage node contact plugs |
| **MOL/Cap** | Storage Node Capacitor | Crown / MIM / Polycide Stack | High-k Dielectric Stack ($\text{Ta}_2\text{O}_5$ / $\text{Al}_2\text{O}_3$ or ONO) | $\kappa > 15$, $\text{EOT} = 3\text{ to }4\text{ nm}$ | Target $C_s \ge 28\text{ fF}$ (25 to 30 fF range) |
| **BEOL** | Bitline & Metal Interconnect | Metal / W Bitline & ILD Stack | Bitline pitch $360\text{ nm}-400\text{ nm}$ | ILD $\text{SiO}_2$ ($\kappa \approx 3.9$) | $C_{BL} \approx 250\text{ fF}$, $\Delta V = 100-150\text{ mV}$ |

## References
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](../)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](../)
- [Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout](../)

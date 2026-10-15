# SOP: Dielectric Film Metrology, Ellipsometry & Pin-Hole Stress Profilometry Inspection

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN)
- **Status**: Implemented
- **Module**: BEOL Inter-Metal Dielectric & Passivation Layer Deposition / Thin Film Metrology

## Overview & Rationale
Defines the standard operational flow for non-destructive spectroscopic ellipsometry and stress/pin-hole profilometry on dielectric thin films in the 180nm Open-Source DRAM node (including EOT verification, gate dielectric precision, and inter-metal dielectric film uniformity).

## Key Process Steps & Parameters
1. **Wafer Loading & Notch Alignment**: Vacuum chuck at 20°C ambient cleanroom conditions; align orientation flat/notch.
2. **Spectroscopic Ellipsometry Measurement**: Measure reflection polarization angles $\Psi$ and $\Delta$ governed by:
   $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \cdot e^{i\Delta}$$
   Optical parameters extracted using parameterized Cauchy or Sellmeier dispersion models for $n(\lambda)$ and $k(\lambda)$.
3. **Automated Wafer Mapping**: Execute 49-point wafer mapping (or 9-point rapid screening) to calculate radial non-uniformity across spin coating/furnace depositions.
4. **Stress & Pin-Hole Profilometry Scan**: Laser/stylus radius of curvature scan to calculate film stress; pin-hole leakage integrity check across array area.

## Acceptance Criteria
- Equivalent Oxide Thickness (EOT): **3 to 4 nm** (for high-k/ONO stacks; gate oxide at **3.5 nm** with measurement precision within **±0.05 nm**).
- Wafer Mapping Uniformity: **49-point** automated mapping with radial thickness standard deviation $\le 1.5\%$.
- DRAM Cell Capacitance Verification: $\ge 28\text{ fF/cell}$ (minimum baseline $25 - 30\text{ fF/cell}$).
- Cell Leakage Current: $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$ to support $> 64\text{ ms}$ refresh intervals.

## References
- Source: *Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology*
- Source: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- Source: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*

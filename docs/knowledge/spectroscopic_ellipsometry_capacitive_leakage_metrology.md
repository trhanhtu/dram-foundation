# Spectroscopic Ellipsometry Thickness Mapping & In-Line Capacitive Leakage Metrology

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented
- **Subsystem**: 180nm Open-Source DRAM Chip / Metrology & Quality Gate

## Overview & Rationale
Standard Operating Procedure (SOP) for automated non-destructive spectroscopic ellipsometry physical/optical thickness mapping and in-line capacitive/leakage verification on planar test structures and 3D crown capacitor high-k stacks ($\text{Al}_2\text{O}_3/\text{Ta}_2\text{O}_5$) prior to top-electrode encapsulation.

## Key Details / Architecture
- Optical dispersion model: Tauc-Lorentz / Cauchy optical dispersion for $\text{Ta}_2\text{O}_5$ and $\text{Al}_2\text{O}_3$ films.
- Electrical extraction: 1 MHz high-frequency accumulation capacitance ($C_{ox}$) for accurate EOT extraction ($\pm 0.1\text{ nm}$ precision) and quasi-static leakage at 85°C.
- In-line qualification limits: Target cell storage capacitance $\ge 28\text{ fF/cell}$, effective dielectric constant $\kappa > 15$, and leakage current $< 1\text{ fA/cell}$ at 85°C.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context2.yaml)
- [Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction](./docs/context3.yaml)

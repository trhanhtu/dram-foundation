# Post-CMP ILD Thickness Contour Mapping & WIWNU Statistical Uniformity Computation

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure for inline post-CMP dielectric metrology across 180nm commercial MPW tapeouts (SkyWater SKY130 compatible). The procedure quantifies remaining inter-layer dielectric (ILD) thickness, establishes 2D spatial contour topography, extracts within-wafer non-uniformity (WIWNU), and qualifies tungsten-plug (W-plug) dishing and array oxide erosion before bitline/stacked capacitor formation.

## Key Details / Architecture
- **Metrology Engine**: Non-destructive spectroscopic ellipsometry (SE) operating over broadband wavelength $\lambda \in [245\text{ nm}, 1000\text{ nm}]$ with polar angles $\Psi$ and $\Delta$.
- **Optical Dispersion Model**: Cauchy parametrization $n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4}$ with zero extinction coefficient ($k = 0$) in transparent dielectric band.
- **Sampling Grid**: 49-point polar coordinate map (SEMI standard) with 3 mm edge exclusion.
- **Topography Cross-Check**: High-resolution AFM profilometry on dense memory cell arrays (0.17 µm contact holes / shared bitline plugs).
- **Statistical Metric**: Within-Wafer Non-Uniformity computed as $\text{WIWNU}_{1\sigma} = \frac{\sigma_{t}}{\bar{t}} \times 100\% \le 3.5\%$.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/knowledge/dram_180nm_cell_topology.md)
- [Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology](./docs/knowledge/spectroscopic_ellipsometry_metrology.md)
- [SkyWater SKY130 Open PDK Design Rules & Lithography Grid](./docs/knowledge/sky130_pdk_design_rules.md)

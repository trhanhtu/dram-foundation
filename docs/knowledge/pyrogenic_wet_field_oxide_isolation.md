# Micro-Knowledge: Pyrogenic Wet Field Oxide Isolation (350 nm)

- **Date**: 2026-10-08
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented

## Overview & Rationale
For Gen 1 (mm) prototyping within the 180nm DRAM architecture context, robust dielectric isolation between adjacent active areas (memory cells and periphery circuitry) requires thick field oxide (300 nm to 500 nm, nominally 350 nm). A fused silica high-purity quartz tube furnace utilizing pyrogenic wet oxidation (Deal-Grove parabolic diffusion regime) provides rapid, uniform, low-defect oxide growth with high dielectric breakdown strength.

## Key Details / Architecture
- **Furnace Equipment**: Fused silica high-purity quartz process tube with 3-zone PID temperature control maintaining $\pm 0.5^\circ\text{C}$ over a 30 cm flat zone.
- **Oxidation Target**: 350 nm nominal field oxide thickness (within the 300 nm – 500 nm range for LOCOS / STI trench fill).
- **Process Temperature Target**: Stabilized within the flat zone under pyrogenic $\text{H}_2/\text{O}_2$ steam torch ignition.
- **Metrology**: Post-oxidation spectroscopic ellipsometry mapping across wafer batch.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace

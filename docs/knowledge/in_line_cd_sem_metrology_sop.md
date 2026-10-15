# In-Line CD-SEM Multi-Site Gate Length and Line-Edge Roughness Metrology

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the leaf metrology SOP for high-resolution Critical Dimension Scanning Electron Microscopy (CD-SEM) targeting post-litho/post-etch 180nm polysilicon access gates and wordline arrays in a 180nm DRAM process (integrating SkyWater SKY130 manufacturing grid constraints and 1T1C stacked capacitor cell topology).

## Key Details / Architecture
- **Inspection Targets**: Polysilicon gate length ($L = 180\text{ nm}$ nominal, minimum physical design rule limit $150\text{ nm}$), minimum poly spacing ($210\text{ nm}$), and gate-to-active overlay error budget ($\le 35\text{ nm}$).
- **Metrology Beam Setup**: Low landing energy ($300\text{ eV} - 500\text{ eV}$), probe current $8\text{ pA} - 15\text{ pA}$ to eliminate e-beam charging and resist shrinkage.
- **LER Quantification**: High-frequency edge roughness quantified at $3\sigma \le 10\text{ nm}$ across defined gate integration windows.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- SkyWater SKY130 Design Rules & 180nm DRAM Cell Layout Topology

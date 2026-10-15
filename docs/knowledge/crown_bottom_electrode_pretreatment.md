# Crown Bottom Electrode Surface Pre-Treatment and In-Situ Degas

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
For 180nm node open-source DRAM architecture utilizing a 3D high-aspect-ratio crown capacitor over bitline (COB), clean bottom electrode interface conditioning prior to atomic layer deposition (ALD) of high-k dielectric stacks ($\text{Al}_2\text{O}_3/\text{Ta}_2\text{O}_5$, $\kappa > 15$) is essential. Removing organic residues, native oxide, and physisorbed atmospheric moisture eliminates interfacial traps, ensuring low leakage current (< 1 fA/cell at 85°C) and tight EOT control (3 to 4 nm) to sustain cell capacitance ≥ 28 fF.

## Key Details / Architecture
- **Wet Surface Pre-Treatment**: Dilute wet clean followed by overflow UPW rinse and surface-tension-gradient (Marangoni) drying to prevent crown collapse.
- **In-Situ Degas**: High-vacuum thermal bake in loadlock/degas transfer module at base pressure $< 2 \times 10^{-6}\text{ Torr}$ with turbomolecular or cryopump before ALD $\text{Al}_2\text{O}_3$ seeding.

## References & Related Files
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](file:///docs/context.yaml)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](file:///docs/context2.yaml)
- [Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects](file:///docs/context.yaml)

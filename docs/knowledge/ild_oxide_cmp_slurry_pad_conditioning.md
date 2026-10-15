# ILD Oxide CMP Slurry Selection & Polishing Pad Conditioning Setup

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (Gemini)
- **Status**: Implemented
- **Generation**: Gen 3 (nm)
- **Node Scope**: 180nm Open-Source DRAM Chip > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > Chemical Mechanical Planarization (CMP) of Inter-Layer Dielectrics & Tungsten Plugs > Inter-Layer Dielectric (ILD) Oxide CMP Recipe Optimization and Polish > ILD Oxide CMP Downforce, Platen Speed, and Slurry Flow Recipe Optimization > ILD Oxide CMP Slurry Selection and Polishing Pad Conditioning Setup

## Overview & Rationale
In 180nm DRAM fabrication featuring Stacked Capacitor Over Bitline (COB) topologies, tungsten contact plugs (W-plugs), and Metal-1 aluminum-copper (Al-0.5% Cu) interconnects (target thickness 350 nm ± 5%), inter-layer dielectric (ILD) planarization requires strict global planarity and low defect density. The storage cell utilizes stacked capacitors (Crown/Cylinder) with 28 fF capacitance budget and EOT of 3 to 4 nm, demanding surface roughness and residual step height after oxide CMP to stay well within lithographic depth-of-focus (DoF) limits.

## Process Flow & Operational Setup
The conditioning and slurry preparation protocol ensures consistent removal rates and prevents abrasive agglomeration:

1. **Slurry Selection & Chemistry**:
   - Abrasive: Colloidal/fumed silica ($\text{SiO}_2$) nanoparticles (mean particle size: 30 nm to 50 nm).
   - Solid content: 12 wt% to 15 wt%.
   - pH: Stabilized at 10.5 to 11.0 using KOH/deionized water (DIW) diluent.
   - Flow rate: 150 to 200 mL/min dispensed near platen center.

2. **Polishing Pad Conditioning Setup**:
   - Pad type: Microporous polyurethane pad (e.g., IC1000/Suba-IV concentric grooved).
   - Diamond conditioner: 100-grit diamond disc (diam. 100 mm).
   - Conditioning sweep: In-situ conditioning with 5 to 7 psi conditioner downforce at 80 rpm conditioner head speed.
   - Pad break-in: 30-minute ex-situ pre-conditioning with continuous DIW and dilute slurry flush prior to wafer processing.

3. **Platen & Polishing Kinematics**:
   - Platen rotation speed: 65 to 75 rpm.
   - Carrier head speed: 60 to 70 rpm with synchronous counter-rotation.
   - Membrane downforce: 3.5 to 4.5 psi across inner and outer pressure zones.

## References & Related Files
- [context.yaml](./docs/context.yaml)
- 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench
- Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects
- Legacy 180nm DRAM Architecture & Cell Capacitor Engineering

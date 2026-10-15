# Ti/TiN Adhesion & Diffusion Barrier Sputter Deposition

- **Date**: 2026-10-13
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for depositing Ti/TiN adhesion and diffusion barrier bilayers prior to Al-0.5% Cu interconnect metallization in the 180nm open-source DRAM architecture (Gen 2 - µm). The Ti layer acts as an adhesion promoter and contact resistance reducer on W-plug contacts, while the reactively sputtered TiN layer prevents copper/aluminum interdiffusion and junction spiking into 180nm access transistor active areas.

## Key Details / Architecture
- **Vacuum Pump-Down**: Cryo/turbomolecular pump down to base pressure $< 2 \times 10^{-6}\text{ Torr}$ to suppress oxygen contamination.
- **Process Atmosphere**: Argon (99.999% 5N purity) at $3\text{ to }5\text{ mTorr}$ working pressure.
- **Power & Deposition**: DC Magnetron power supply operated at $1.5\text{ to }3.0\text{ kW}$ yielding calibrated deposition rate of $50\text{ to }100\text{ nm/min}$.
- **Post-Metal Anneal Integration**: Compatible with forming gas ($95\%\text{ N}_2 / 5\%\text{ H}_2$) anneal at $400^\circ\text{C}$ for 30 minutes, maintaining sheet resistance $R_s < 0.08\ \Omega/\Box$.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- Verified Local Literature Context: *Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects*
- Verified Local Literature Context: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*

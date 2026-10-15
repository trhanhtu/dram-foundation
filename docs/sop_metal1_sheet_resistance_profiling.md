# Automated Multi-Point Metal-1 Wafer Sheet Resistance Profiling

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (Gemini) - DRAM Foundation VN Multi-Agent Council
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for automated collinear four-point probe sheet resistance ($R_s$) wafer profiling following post-metal forming gas anneal for the 180nm Open-Source DRAM process.

## Key Process Parameters & Equations
- **Probe Tip Spacing**: $s = 1.0\text{ mm}$, tungsten carbide tips with radius $50 - 100\ \mu\text{m}$.
- **DC Measurement Current**: $I = 1\text{ mA to } 10\text{ mA}$.
- **Sheet Resistance Formulation**: $R_s = \frac{\pi}{\ln(2)} \cdot \frac{V}{I} = 4.5324 \cdot \frac{V}{I}\ [\Omega/\square]$.
- **Edge Correction Factor**: $F(d/s)$ applied when wafer diameter is finite ($< 40 \times s$).
- **Post-Anneal Baseline**: $R_s < 0.08\ \Omega/\square$ on 350 nm $\pm 5\%$ Al-0.5% Cu interconnect film after $400^\circ\text{C}$ forming gas anneal ($95\%\ \text{N}_2 / 5\%\ \text{H}_2$) for 30 minutes.

## References & Related Files
- [context.yaml](./docs/context.yaml)
- Source: Four-Point Collinear Probe Metrology for Semiconductor Sheet Resistance
- Source: Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects

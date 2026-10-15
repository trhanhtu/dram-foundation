# SOP: Sputter Chamber Cryopump Pump-Down & Residual Gas Baseline Qualification (< 2x10^-6 Torr)

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Subsystem**: BEOL Multi-Layer Metal Interconnect Deposition (Metal 1, Metal 2, and Passivation) > M1/M2 High-Vacuum DC Magnetron Sputter Deposition & Anneal > High-Vacuum Chamber Conditioning & Base Pressure Calibration

## Overview & Rationale
For 180nm Open-Source DRAM metallization (bitline and wordline strapping using pure Al or Al-0.5% Cu), oxygen incorporation during film growth leads to severe sheet resistance degradation, interface oxidation, and early electromigration failure. Maintaining base chamber pressure below $2 \times 10^{-6}\text{ Torr}$ via high-capacity cryopumping before admitting ultra-pure Argon (Ar 99.999%) at $3\text{ to }5\text{ mTorr}$ working pressure is mandatory to establish an ultra-clean residual gas baseline.

## Key Physical Parameters
- **Chamber Base Pressure**: $< 2 \times 10^{-6}\text{ Torr}$ (prevents oxygen incorporation into Al matrix).
- **Process Gas Purity & Pressure**: Argon ($99.999\%$ / 5N purity), regulated to $3\text{ to }5\text{ mTorr}$ working pressure.
- **Target Material & Power**: $99.999\%$ (5N) Aluminum target, DC magnetron power supply operated at $1.5\text{ to }3.0\text{ kW}$.
- **Deposition Rate & Target Thickness**: Calibrated deposition rate of $50\text{ to }100\text{ nm/min}$; target film thickness of $350\text{ nm} \pm 5\%$.
- **Post-Anneal Sheet Resistance Target**: $R_s < 0.08\ \Omega/\Box$ after forming gas anneal ($\text{N}_2/\text{H}_2\ 95/5$ at $400^\circ\text{C}$ for $30\text{ min}$).

## References & Related Files
- [Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects](../../Physical%20Vapor%20Deposition%20(PVD)%20Sputtering%20of%20Aluminum%20Metallization%20Interconnects.md)

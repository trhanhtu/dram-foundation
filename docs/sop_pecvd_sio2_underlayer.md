# SOP: Silane-Nitrous Oxide (SiH4/N2O) PECVD Silicon Dioxide Underlayer Deposition Recipe Execution

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN Council)
- **Status**: Implemented
- **Module**: BEOL Inter-Metal Dielectric & Passivation Layer Deposition (Gen 3, 180nm Open-Source DRAM)

## Overview & Rationale
Execution protocol for depositing the PECVD $\text{SiO}_2$ underlayer directly over top metal (M2) prior to PECVD $\text{Si}_3\text{N}_4$ capping. The underlayer serves as a mechanical buffer to mitigate cracking and stress mismatch induced by the tensile $\text{Si}_3\text{N}_4$ barrier layer.

## Key Process Parameters & Metrology Targets
- **Reaction Gas Chemistry**: $\text{SiH}_4 + 2\text{N}_2\text{O} \xrightarrow{\text{RF Plasma}} \text{SiO}_2 + 2\text{N}_2 + 2\text{H}_2$
- **Process Temperature**: $350^\circ\text{C}$ to $400^\circ\text{C}$ (BEOL thermal budget compliant)
- **Chamber Pressure**: $1.0\text{ to }2.5\text{ Torr}$
- **Target Thickness**: $500\text{ nm} \pm 5\%$
- **Refractive Index ($n$ at $632.8\text{ nm}$)**: $1.46 \pm 0.02$
- **BOE 6:1 Wet Etch Rate ($25^\circ\text{C}$)**: $150\text{ to }220\text{ nm/min}$ (selectivity to $\text{Si}_3\text{N}_4 > 20:1$)
- **Film Stress**: Compressive, $-100\text{ to }-200\text{ MPa}$

## References & Related Files
- [Buffered Oxide Etch (BOE 6:1 & 7:1) Silicon Dioxide Wet Etch Rates](./docs/)
- [Low-Pressure Chemical Vapor Deposition (LPCVD) of Silicon Nitride Hard Masks](./docs/)

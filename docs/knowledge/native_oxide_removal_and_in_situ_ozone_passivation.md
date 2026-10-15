# Native Oxide Removal & In-Situ Ozone Passivation Run Execution

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Accepted
- **Context Path**: 180nm Open-Source DRAM Chip > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > 3D High-Aspect-Ratio Crown Capacitor ALD Dielectric & Metal Electrode Deposition > ALD Al2O3/Ta2O5 High-k Dielectric Stack Recipe Optimization & Deposition > ALD Precursor Metering & Substrate In-Situ Ozone Pre-Clean Recipe Calibration > In-Situ Ozone Surface Pre-Clean & Native Oxide Passivation Recipe Calibration > Native Oxide Removal & In-Situ Ozone Passivation Run Execution

## Overview & Rationale
For 180nm 1T1C stacked crown capacitors (cell footprint $8F^2$ or $6F^2$, access transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$), uncontrolled native oxide growth ($SiO_x$) at the bottom electrode interface introduces parasitic low-$k$ capacitance, increases Equivalent Oxide Thickness (EOT), and degrades retention.
This SOP specifies the wet ex-situ RCA clean/dilute HF strip and subsequent in-situ ALD ozone pre-clean/passivation run execution prior to high-$k$ ($Al_2O_3 / Ta_2O_5$) deposition.

## Key Process Parameters & Workflow
- **RCA-1 (SC-1)**: $5:1:1\text{ }DI\text{ }H_2O : NH_4OH (29\%) : H_2O_2 (30\%)$ at $70^\circ\text{C}-80^\circ\text{C}$ for $10-15\text{ min}$.
- **Intermediate DI Water Rinse**: $18.2\text{ M}\Omega\cdot\text{cm}$ dump rinse for $3\text{ min}$.
- **HF Strip**: $1:50\text{ }HF:H_2O$ dip for $15-30\text{ s}$ (surface transition to hydrophobic).
- **RCA-2 (SC-2)**: $6:1:1\text{ }DI\text{ }H_2O : HCl (37\%) : H_2O_2 (30\%)$ at $70^\circ\text{C}-80^\circ\text{C}$ for $10\text{ min}$.
- **Drying & Transfer**: High-purity $N_2$ blow dry; queue time $< 30\text{ min}$ to ALD loadlock.
- **In-Situ Ozone Passivation**: Substrate pre-clean in ALD chamber prior to precursor pulse priming.

## Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

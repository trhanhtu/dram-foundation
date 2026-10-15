# Crown Electrode Surface Preparation & In-Situ Ozone Hydroxylation Calibration

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
For high-aspect-ratio 3D crown storage capacitors in 180nm open-source DRAM (8F² / 6F² folded bitline architectures), uniform nucleation of high-k dielectric stacks ($\text{Al}_2\text{O}_3/\text{Ta}_2\text{O}_5$) requires complete particle removal, native oxide stripping, ionic decontamination, and dense in-situ surface hydroxylation (-OH termination). This standard operating procedure ensures robust capacitance ($C_{cell} \ge 28\text{ fF/cell}$), low leakage current ($\le 1.0\text{ fA/cell}$ at 85°C), and tight equivalent oxide thickness ($EOT \approx 3.0 - 4.0\text{ nm}$).

## Key Details / Architecture
1. **Ex-Situ RCA-1 (SC-1)**:
   - Solution: $5:\!1:\!1$ ratio ($\text{DI H}_2\text{O} : \text{NH}_4\text{OH } [29\%] : \text{H}_2\text{O}_2 [30\%]$).
   - Bath temperature: $70^\circ\text{C} - 80^\circ\text{C}$ for $10 - 15\text{ minutes}$.
   - Function: Strips organic contaminants and light trace metals.
2. **Intermediate DI Dump Rinse**:
   - Ultra-pure deionized water ($18.2\text{ M}\Omega\cdot\text{cm}$) for $3\text{ minutes}$.
3. **Dilute Hydrofluoric Dip (DHF)**:
   - Ratio: $1:50\text{ HF}:\text{H}_2\text{O}$ for $15 - 30\text{ seconds}$.
   - Function: Complete native oxide strip; transitions 3D crown surface from hydrophilic to hydrophobic (H-terminated Si).
4. **Ex-Situ RCA-2 (SC-2)**:
   - Solution: $6:\!1:\!1$ ratio ($\text{DI H}_2\text{O} : \text{HCl } [37\%] : \text{H}_2\text{O}_2 [30\%]$).
   - Bath temperature: $70^\circ\text{C} - 80^\circ\text{C}$ for $10\text{ minutes}$.
   - Function: Desorbs alkali ions ($\text{Na}^+, \text{K}^+$) and heavy transition metals ($\text{Fe}, \text{Cu}, \text{Ni}$).
5. **Drying & Vacuum Transfer**:
   - High-purity filtered $\text{N}_2$ blow-dry; rapid loadlock pump-down to suppress uncontrolled ambient re-oxidation.
6. **In-Situ ALD Ozone Pre-Clean & Hydroxylation Calibration**:
   - Reactor loadlock/chamber stabilization prior to trimethylaluminum (TMA) / $\text{Ta}(\text{OC}_2\text{H}_5)_5$ exposure.
   - Controlled $\text{O}_3$ exposure providing hydroxyl functionalization without excessive sub-interfacial parasitic $\text{SiO}_x$ regrowth.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [Standard RCA-1 and RCA-2 Silicon Wafer Cleaning Procedure](./docs/context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context.yaml)

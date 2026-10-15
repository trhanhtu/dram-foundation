# Cyclic ALD Ta2O5 Thin-Film Deposition with Periodic In-Situ N2O Plasma Radical Annealing

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Council)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for cyclic atomic layer deposition (ALD) of $\text{Ta}_2\text{O}_5$ high-$\kappa$ dielectric thin films integrated with periodic in-situ $\text{N}_2\text{O}$ plasma radical annealing. Formulated for the 180nm Open-Source DRAM node (3D high-aspect-ratio Crown/Cylinder stacked capacitor topology over bitline, 1T1C cell architecture).

Periodic in-situ radical oxidation/annealing eliminates carbon/halide contamination, passivates oxygen vacancies, suppresses junction leakage below 1 fA/cell at 85°C, and achieves target Equivalent Oxide Thickness (EOT) of 3 to 4 nm with $\kappa > 15$.

## Key Details / Architecture
- **Process Steps**:
  1. Pre-Deposition Chamber Conditioning & Loadlock Transfer.
  2. Cyclic ALD $\text{Ta}_2\text{O}_5$ Deposition (precursor pulse, purge, oxidant pulse, purge).
  3. Periodic In-Situ $\text{N}_2\text{O}$ Plasma Radical Annealing (every $N$ cycles).
  4. Post-Deposition Cooling and in-line metrology.
- **Acceptance Criteria**:
  - Cell Capacitance: $\ge 28\text{ fF/cell}$ (ensuring data retention $> 64\text{ ms}$ at 85°C).
  - Equivalent Oxide Thickness (EOT): $3\text{ to }4\text{ nm}$.
  - Effective Dielectric Constant: $\kappa > 15$.
  - Junction/Sub-threshold Leakage Current: $< 1\text{ fA/cell}$ at 85°C.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- Source: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- Source: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*

# Micro-Knowledge: High-Speed ALD Pulse Valve & Fast MFC Calibration for DRAM Crown Capacitors

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
For 180nm DRAM nodes utilizing 3D high-aspect-ratio crown capacitor stacks (such as Al2O3/Ta2O5 MIM/MIS capacitors), precise precursor dosing is critical. Digital high-speed ALD diaphragm valves and fast-response Mass Flow Controllers (MFCs) must deliver repeatable precursor and purge gas pulses to guarantee conformal step coverage, an equivalent oxide thickness (EOT) of 3 to 4 nm, and prevent precursor condensation or CVD-mode parasitic reactions.

## Key Calibration Architecture & Target Specs
- **Dielectric Stack**: Al2O3/Ta2O5 or ONO high-k dielectric stack providing dielectric constant $\kappa > 15$.
- **Target Capacitance**: Minimum 25 to 30 fF/cell (target $\ge 28\text{ fF}$) for noise immunity and retention $> 64\text{ ms}$ at 85°C.
- **Leakage Target**: Leakage current kept below $1\text{ fA/cell}$ at 85°C.
- **Equivalent Oxide Thickness (EOT)**: $3\text{ to }4\text{ nm}$.
- **Fast Pulse Valve & MFC Actuation**: Precursor injection pulse durations typically 50–200 ms with MFC settling times $< 100\text{ ms}$ and manifold base vacuum $< 2 \times 10^{-6}\text{ Torr}$ prior to precursor introduction.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context2.yaml)

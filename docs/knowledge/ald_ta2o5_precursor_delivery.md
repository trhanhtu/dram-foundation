# Micro-Knowledge: ALD Ta(OC2H5)5 Delivery Setup & Substrate Pre-Heating for 180nm Crown Capacitors

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
For high-aspect-ratio 3D Crown DRAM storage capacitors (8F² / 6F² COB cell architectures) at the 180nm node, achieving a stable capacitance > 28 fF/cell with low leakage (< 1 fA/cell at 85°C) and equivalent oxide thickness (EOT) of 3 to 4 nm requires high-k dielectrics such as Ta2O5 (dielectric constant κ > 15). Reliable deposition requires precise delivery of the low-volatility liquid precursor tantalum pentaethoxide, Ta(OC2H5)5 (PET), without premature condensation in gas delivery manifolds or cold-spot thermal fluctuations across the high-aspect-ratio 3D crown patterned substrate.

## Key Details / Architecture
1. **Precursor Delivery System (Ta(OC2H5)5)**:
   - Precursor: Liquid Tantalum Pentaethoxide, Ta(OC2H5)5 (PET).
   - Bubbler Heating: Stabilized at 120°C - 130°C to achieve adequate vapor pressure.
   - Gas Delivery Lines & Injection Valves: Maintained at +10°C to +15°C above bubbler temperature (140°C - 145°C) to prevent precursor condensation and valve clogging.
   - Carrier Gas: High-purity N2 or Ar (99.999%) calibrated at 50 - 100 sccm.
2. **Crown Substrate Pre-Heating**:
   - Substrate Chuck Temperature: Pre-heated and thermally soaked at 300°C - 350°C (ALD temperature window for Ta(OC2H5)5).
   - Pre-heating Duration: Minimum 10 minutes thermal soak to eliminate thermal gradients within high-aspect-ratio crown microstructures.
3. **Integration Targets**:
   - EOT target: 3.0 to 4.0 nm.
   - Effective dielectric constant κ: > 15.
   - Storage capacitance: ≥ 28 fF/cell (minimum legacy envelope: 25 to 30 fF/cell).
   - Junction/dielectric leakage: < 1 fA/cell at 85°C.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- `180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench`
- `Legacy 180nm DRAM Architecture & Cell Capacitor Engineering`

# High-Aspect-Ratio Crown Cross-Sectional FIB Sample Preparation

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Defines the Focused Ion Beam (FIB) dual-beam (FIB-SEM) sample preparation protocol tailored for 180nm node high-aspect-ratio (HAR) stacked crown capacitor arrays. Focuses on preserving conformal ALD/CVD TiN top metal electrodes, high-k dielectrics (Ta2O5 / Al2O3 or ONO), and underlying tungsten (W) contact plugs without curtaining, mechanical collapsing, or Ga+ amorphization.

## Key Details / Architecture
- Dual-beam Gas Injection System (GIS) Pt capping: e-beam gentle buffer (1 kV, 0.4 nA) followed by Ga+ ion beam deposition (30 kV, 80 pA to 2.5 µm).
- Bulk trenching and coarse milling at 30 kV (7 nA down to 1 nA) aligned to the memory array 360 nm–400 nm bitline/wordline pitch.
- In-situ micro-manipulator (Omniprobe) needle attachment and lift-out to Cu/Mo TEM grid.
- Low-energy fine polish stages (5 kV at 40 pA, final 2 kV at 20 pA) mitigating curtaining and limiting sidewall amorphous damage to <= 2.0 nm.

## References & Related Files
- [context.yaml](../context.yaml)
- [context2.yaml](../context2.yaml)
- [context3.yaml](../context3.yaml)

# Cross-Sectional SEM Resist Undercut & BOE Etch Bias Profile Verification

- **Date**: 2026-10-12
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Actionable standard operating procedure for cross-sectional Scanning Electron Microscopy (SEM) verification of photoresist undercut profiles, isotropic wet etch lateral bias, and dimensional fidelity following Buffered Oxide Etch (BOE 6:1) SiO2 patterning on 180nm DRAM cell arrays.

## Key Details / Architecture
- **Etch Process**: BOE 6:1 (6 parts 40% NH4F : 1 part 49% HF) with 0.1% wetting agent.
- **Reference Etch Rate**: ~100 nm/min (1000 Å/min) at 25°C.
- **Surface Preparation**: HMDS vapor prime at 120°C prior to resist coating to suppress lateral lifting and excessive undercut.
- **Target Dimensions**: Gate SiO2 physical thickness ~3.5 nm, transistor channel length L = 180 nm, pitch = 360 nm to 400 nm.
- **Metrology**: Cross-sectional high-resolution SEM profile inspection and lateral bias measurement across cleaved sample dies.

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)

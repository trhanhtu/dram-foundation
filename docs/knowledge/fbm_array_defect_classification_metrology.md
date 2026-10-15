# Fail Bitmapping (FBM) Array Defect Classification & Root-Cause Metrology

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council - Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure for post-EDS Fail Bitmapping (FBM) topological defect classification and in-line root-cause physical metrology on the 180nm Open-Source DRAM array. Translates logical March C- fail logs into physical (X, Y) coordinates across 8F² folded bitline architectures, distinguishing between single-cell retention/leakage faults, bitline/wordline line opens/shorts, and capacitor dielectric breakdown.

## Key Details / Architecture
- **Logical-to-Physical De-scrambling**: Maps tester cycle coordinates to array matrix locations ($W = 220\text{ nm}, L = 180\text{ nm}$).
- **Defect Spatial Categorization**: Single-bit isolated faults, bitline column pairs, wordline row lines, and cluster blocks.
- **Parametric Cross-Verification**: Correlates bitline capacitance ($C_b \in [150, 250]\text{ fF}$), storage capacitance ($C_s \ge 28\text{ fF}$, nominal $\ge 25\text{ fF}$), capacitance ratio ($C_b/C_s \in [5:1, 9:1]$), NMOS access transistor $V_{thn} = +0.55\text{ V} \pm 50\text{ mV}$, and on/off current ratio $I_{on}/I_{off} > 10^7$.
- **Failure Metrology**: FIB cross-sectioning and in-line SEM of tungsten contacts (W-plugs) and ONO / $\text{Ta}_2\text{O}_5$ capacitor stacks.

## References & Related Files
- [docs/context.yaml](..../../context.yaml)
- [docs/context2.yaml](..../../context2.yaml)
- [docs/context3.yaml](..../../context3.yaml)

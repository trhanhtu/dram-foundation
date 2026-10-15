# CD-SEM Automated Measurement Recipe Programming and Pattern Recognition Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN Council)
- **Status**: Accepted
- **Generation**: Gen 3 (nm) / 180nm Open-Source DRAM Node

## Overview & Rationale
Defines the standard recipe automation for CD-SEM inline metrology of Electron Beam Direct Write (EBDW) / DUV patterned 180nm polysilicon access transistor gates on DRAM cell arrays (8F² / 6F² folded bitline architectures). Ensures high-fidelity pattern recognition (PR), sub-nanometer edge detection repeatability, automated stig/focus calibration, and automated LER/LWR statistical extraction.

## Key Details / Architecture
- **Global & Die Alignment**: Primary notch/flat macro-alignment followed by dual-die micro-alignment using corner scribe-line verniers.
- **Pattern Recognition (PR)**: Multi-hierarchy normalized cross-correlation (NCC) template matching on memory array border topologies with a correlation score threshold > 0.85.
- **Beam Settings**: Low landing energy ($V_{acc} = 500\text{--}800\text{ V}$, beam current $I_p \le 8\text{ pA}$) to eliminate resist charging and feature shrinkage during measurement.
- **Metrology Algorithm**: Maximum slope thresholding on secondary electron (SE) line profiles averaged across orthogonal scan vectors over the 220 nm access transistor channel width.

## References & Related Files
- [SkyWater SKY130 Open PDK Design Rules & Lithography Grid](./docs/context.yaml)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [Sam Zeloof Z1 Garage Semiconductor Journal (2018)](./docs/context.yaml)

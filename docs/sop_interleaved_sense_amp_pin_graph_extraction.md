# SOP: Interleaved Sense Amp & Array Pin Connectivity Graph Extraction

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Chip

## Overview & Rationale
Standard Operating Procedure for extracting geometric recognition and pin connectivity graphs between the folded-bitline DRAM cell array (8F² architecture) and interleaved sense amplifier (SA) banks. Pitch-matching constraints require alternating top/bottom interleaved SA layouts, necessitating accurate topological extraction and node mapping.

## Key Details & Acceptance Criteria
- Pitch alignment verification: 360 nm array bitline pitch.
- Extracted parasitic bitline capacitance boundary: ~250 fF.
- Storage node target: >= 28 fF.
- Leakage current target: <= 1 fA/cell at 85°C.

## References & Related Files
- [docs/context.yaml](./context.yaml)
- Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout
- 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench

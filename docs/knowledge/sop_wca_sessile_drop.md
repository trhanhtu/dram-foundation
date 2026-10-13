# Multi-Point Sessile Drop Dosing Recipe & Automated Image Capture Protocol Setup

- **Date**: 2026-10-13
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Automated sessile drop water contact angle (WCA) metrology protocol for 100mm wafers post-clean and post-HMDS priming in the DRAM Foundation VN 180nm process line. Ensures cross-wafer surface energy uniformity before photoresist spin coating to prevent peel-off during acid wet etching.

## Key Details / Architecture
- **Stage Alignment & Repeatability**: Gen 2 macroscopic positioning stage holding within ±5 µm tolerance.
- **Surface Preparation Baseline**: Dehydration bake at 150°C - 200°C for 30 minutes; HMDS vapor silylation converting hydrophilic silanols to methyl-siloxane bonds.
- **Metrology Verification**: 5-point wafer map (Center, North, South, East, West) measuring DI droplet sessile profiles using telecentric optical imaging.

## References & Related Files
- [Photoresist Spin Coating Dynamics and HMDS Vapor Priming](./sop_wca_sessile_drop.md)
- [Sam Zeloof Z1 Garage Semiconductor Journal (2018)](./sop_wca_sessile_drop.md)

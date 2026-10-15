# Epoxy Molding Compound (EMC) Pellet Conditioning & Mold Chase Preheating

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) governing the thermal acclimation, high-frequency dielectric preheating of Epoxy Molding Compound (EMC) pellets, and multi-zone PID preheating of mold chase dies for TSOP-54 / 54-ball FBGA encapsulation on 180nm DRAM prototypes.

## Key Details / Architecture
- **Stage 1 (Acclimation)**: Controlled ambient warm-up from 5°C cold storage inside sealed bags until condensation risk is eliminated.
- **Stage 2 (Dielectric Preheating)**: High-frequency RF preheating (80°C - 95°C) to reduce pellet viscosity and optimize transfer flow while preventing premature cross-linking.
- **Stage 3 (PID Mold Chase Preheating)**: Multi-zone cartridge heating holding mold platens at 175°C ± 3°C with balanced clamping pressure.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- Context source: Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging
- Context source: Three-Zone Quartz Tube Thermal Dynamics and PID Temperature Regulation

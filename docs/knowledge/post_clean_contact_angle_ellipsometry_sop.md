# Post-Clean Contact Angle Dewetting & Interfacial Oxide Metrology SOP

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) governing the inspection and verification gate following Dilute HF / Ozone wet clean stripping on 180nm high-aspect-ratio crown capacitor cavities. Interfacial native oxide ($SiO_2$) removal prior to ALD TiN bottom/top electrode and high-$\kappa$ dielectric ($Ta_2O_5 / Al_2O_3$ or ONO) deposition is mandatory to preserve equivalent oxide thickness (EOT $3.0 - 4.0\text{ nm}$) and target cell capacitance ($\ge 25 - 28\text{ fF/cell}$).

## Key Details / Architecture
- **Stage 1 (Surface Wetting Verification)**: Automated sessile droplet contact angle goniometry measuring pure DIW contact angle on sacrificial planar scribe-line monitor pads ($\theta \ge 70^\circ$, typical hydrophobic H-terminated Si is $75^\circ - 85^\circ$).
- **Stage 2 (Interfacial Oxide Film Metrology)**: Spectroscopic ellipsometry at $\lambda = 250 - 850\text{ nm}$ across 9 to 13 site wafer maps confirming residual native oxide thickness $t_{ox} \le 0.2\text{ nm}$ ($< 2.0\text{ \AA}$) with spatial uniformity $3\sigma < 0.1\text{ nm}$.
- **Stage 3 (Queue Time Enforcement)**: $Q\text{-time} \le 120\text{ minutes}$ from DHF clean exit to vacuum chamber loadlock pumping (< $1\times 10^{-6}\text{ Torr}$) to prevent atmospheric re-oxidation.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

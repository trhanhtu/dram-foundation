# Tapping-Mode AFM Silicon Cantilever Tip Procurement and Resonance Calibration

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
For nanoscale post-CMP surface characterization of inter-layer dielectrics (ILD) and tungsten contact plug CMP in 180nm DRAM (such as 360–400 nm pitch wordline/bitline regions and 3.5 nm oxide-equivalent topologies), tapping-mode (intermittent contact) atomic force microscopy (AFM) requires strictly specified silicon cantilevers. Proper procurement parameters, acoustic isolation, thermal tune resonance sweep, and drive frequency offset selection are critical to avoid tip blunting while preserving sub-nanometer surface roughness sensitivity.

## Key Details / Architecture
- **Cantilever Type**: Monolithic n-type antimony-doped silicon probes (reflective Al backside coating).
- **Nominal Tip Radius**: $R_{\text{tip}} \le 10\text{ nm}$ (typically $7\text{--}8\text{ nm}$).
- **Nominal Spring Constant ($k$)**: $20\text{--}75\text{ N/m}$ (nominal $40\text{--}48\text{ N/m}$).
- **Resonance Frequency Range ($f_0$)**: $280\text{--}350\text{ kHz}$ (nominal $\approx 300\text{ kHz}$).
- **Laser Sum Signal Threshold**: $> 5.0\text{ V}$ (target $6.0\text{--}7.5\text{ V}$ on 4-quadrant photodiode).
- **Drive Frequency Offset**: $-0.5\text{ to } -1.0\text{ kHz}$ below the natural resonance peak $f_0$ to operate reliably in the repulsive tapping regime.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/knowledge/sop_afm_cantilever_procurement_calibration.md](./docs/knowledge/sop_afm_cantilever_procurement_calibration.md)

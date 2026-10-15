# Multi-Site Post-CMP Wafer Surface Roughness and Micro-Scratch Topography Mapping

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the in-line atomic force microscopy (AFM) standard operating procedure for multi-site topographic profiling across post-CMP planarized inter-layer dielectric (ILD) and tungsten-plug (W-plug) memory arrays in a 180nm commercial MPW tapeout. Ensures surface micro-roughness ($R_q, R_a$) and polish micro-scratch trench depths remain well below the critical lithographic depth-of-focus and physical manufacturing grid resolution ($0.005\ \mu\text{m} = 5\ \text{nm}$) defined by the SkyWater SKY130 / 180nm CMOS technology rules.

## Key Details / Architecture
- **Metrology Mode**: Tapping-mode (intermittent contact) AFM utilizing ultra-sharp high-aspect silicon cantilevers (tip radius $r_{\text{tip}} < 10\ \text{nm}$, nominal resonance frequency $\sim 300\ \text{kHz}$, spring constant $k \approx 40\ \text{N/m}$).
- **Multi-Site Scheme**: 9-point/13-point full-wafer map sampling dense stacked capacitor over bitline ($8F^2$ / $6F^2$) memory cell arrays, peripheral contact/metal zones, and open ILD regions.
- **Scratch Disqualifiers**: Single-pass scratches exceeding the physical placement grid resolution ($5\ \text{nm}$) or approaching the overlay budget ($\le 35\ \text{nm}$) require immediate CMP slurry filtration and pad conditioning audit.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

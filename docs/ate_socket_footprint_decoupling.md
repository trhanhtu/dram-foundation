# ATE DUT Pogo-Pin Socket Footprint & Multi-Rail Decoupling BOM Selection

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Defines the standard engineering procedure and decoupling BOM criteria for 180nm open-source DRAM prototypes mounted in ceramic QFN/DIP packages on high-speed ATE loadboards. Ensures signal and power integrity across core ($V_{DD} = 1.8\,\text{V}$), boosted wordline overdrive ($V_{PP} = 2.6\,\text{V} - 2.8\,\text{V}$), and bitline equalization reference ($V_{BLP} = V_{DD}/2 = 0.9\,\text{V}$).

## Key Details / Architecture
- Socket interface: High-frequency Kelvin pogo-pin socket with dual-point contact resistance $R_{pin} \le 30\,\text{m}\Omega$ and contact force $\ge 25\,\text{gf}$.
- Multi-rail decoupling matrix targeting target impedance from 100 kHz to 500 MHz with reverse-geometry 0402/0201 low-ESL ceramic capacitors.
- Direct alignment with Mil-Std-883 bonding and die attach integrity ($R_{th} \le 5^\circ\text{C/W}$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

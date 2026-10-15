# ATE High-Precision Pin Electronics Deskew and TDR Channel Timing Calibration

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Council)
- **Status**: Implemented

## Overview & Rationale
High-speed automated testing of 180nm DRAM chips (folded bitline topology, nominal operating voltage $V_{DD} = 1.8\text{ V}$) requires calibrating pin electronics (PE) drivers, comparators, and pogo-pin/load-board transmission lines. Sub-nanosecond JEDEC speed-bin timing parameters ($t_{CK}$, $t_{RCD}$, $t_{RP}$) demand that channel timing skew across all address, clock, and bidirectional data ($DQ/DQS$) channels be deskewed to the sub-25 ps regime using Time-Domain Reflectometry (TDR) and internal programmable delay lines.

## Key Details / Architecture
- **TDR Reference Plane Definition**: Pulse launched into open-circuit/short-circuit calibration fixture at device socket contact tips.
- **Flight Time & Impedance Matching**: Round-trip reflection time extracted to align pin-electronics timing zero-plane directly at the DRAM package pad boundary.
- **Vernier / Programmable Delay Line Calibration**: Per-channel fine-tuning step sizes of $\le 5\text{ ps}$ per LSB.
- **I/O Level Realignment**: Driver output high/low levels aligned to nominal core/IO voltages: $V_{IH} = 1.8\text{ V}$, $V_{IL} = 0.0\text{ V}$, linear reference point $V_{DS} = 50\text{ mV}$.

## References & Related Files
- [docs/context.yaml](.../context.yaml)
- [docs/context2.yaml](.../context2.yaml)
- [docs/context3.yaml](.../context3.yaml)

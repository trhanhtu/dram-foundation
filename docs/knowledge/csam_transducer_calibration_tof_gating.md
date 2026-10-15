# High-Frequency Transducer Calibration & Acoustic Time-of-Flight Gating Setup

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Accepted

## Overview & Rationale
Defines the calibration, immersion acoustic coupling, RF time-of-flight (ToF) gating, and phase inversion screening methodology for Scanning Acoustic Microscopy (CSAM). It is tailored for screening die-attach interface integrity and delamination in TSOP-54 / 54-ball FBGA packages encapsulating 180nm DRAM dies.

## Key Details / Architecture
- **Transducer**: 50 MHz to 100 MHz ultra-high-frequency (UHF) focused acoustic transducer.
- **Coupling Medium**: Degassed deionized (DI) water at 25°C.
- **ToF Gating**: Microsecond/nanosecond interval gating on the A-scan echo matching the die back-surface / die-attach epoxy interface.
- **Echo Polarity**:
  - Positive echo: Bonded solid-to-solid interface (Silicon to Ablebond 84-1LMIS silver-filled epoxy).
  - Negative/phase-inverted echo: High reflection coefficient ($R \approx -1.0$) characteristic of delamination or air void.
- **Screening Limit**: Die-attach void area < 5% total interface area; wire sweep & wire pull integrity >= 4.0 grams-force per Mil-Std-883 Method 2011.

## References & Related Files
- [Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging](./docs/context.yaml)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context2.yaml)
- [Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects](./docs/context3.yaml)

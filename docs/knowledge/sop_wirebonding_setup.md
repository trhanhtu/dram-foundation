# SOP: Capillary Selection, 25um Au Wire Sourcing & Leadframe Stage Heating Setup

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (Gemini)
- **Status**: Accepted
- **Node Context**: 180nm Open-Source DRAM Chip > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > BEOL Multi-Layer Metallization, Wafer Sort & Packaging > Epoxy Die Attach & Ultrasonic Ball Wirebonding to Leadframe > Thermosonic Gold Ball Wirebonding to Leadframe Pins > Capillary Selection, 25um Au Wire Sourcing & Leadframe Stage Heating Setup
- **Generation**: Gen 3 (nm)
- **Action Type**: Make

## Overview & Rationale
This Standard Operating Procedure (SOP) defines the operational protocol for setting up thermosonic ball wirebonding on 180nm DRAM dies mounted to leadframes. It covers capillary selection, 25 µm gold (99.99% Au) wire sourcing and feed path inspection, stage heating calibration (150°C), and thermosonic transducer parameters (60 kHz, 50–100 mW, 20–30 ms) to connect 100 µm × 100 µm aluminum bonding pads to external leadframe pins complying with Mil-Std-883 Method 2011.

## Acceptance Criteria Targets
1. **Bond Wire Material & Diameter**: 25 µm diameter, 99.99% purity Au wire.
2. **Workholder Stage Temperature**: 150°C steady-state thermal interface.
3. **Ultrasonic Transducer Profile**: 60 kHz resonance frequency, 50–100 mW power pulse, 20–30 ms duration.
4. **Mechanical Wire Pull Strength**: >= 4.0 gf (grams-force) per Mil-Std-883 Method 2011, with rupture occurring strictly in wire span.

## References & Related Files
- [Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging](./docs/context.yaml)
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context.yaml)

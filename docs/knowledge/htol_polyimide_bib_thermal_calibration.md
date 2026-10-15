# High-Density Polyimide BIB Socket Array & Multi-Zone Thermal Couple Calibration Harness

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN Council)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) for assembling, instrumenting, and calibrating a high-density polyimide Burn-in Board (BIB) socket array and multi-zone thermocouple harness for 180nm open-source DRAM continuous 125°C dynamic HTOL qualification.

## Key Technical Specifications & Criteria
- **Substrate Material**: High-Tg Polyimide (glass transition > 250°C, continuous rating > 125°C).
- **Package Under Test**: Packaged 180nm DRAM dies with 100 µm x 100 µm bonding pads, 25 µm wire bonds (Mil-Std-883 pull strength >= 4.0 gf), die-attach thermal resistance $R_{th} \le 5^\circ\text{C/W}$, acoustic void area < 5%.
- **Chamber Temperature**: 125°C continuous accelerated burn-in stress.
- **Thermal Uniformity**: Multi-zone thermocouple PID mapping within $\pm 0.5^\circ\text{C}$ across load, center, and source socket grid locations.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/context.yaml)
- [Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging](./docs/context.yaml)
- [Three-Zone Quartz Tube Thermal Dynamics and PID Temperature Regulation](./docs/context.yaml)

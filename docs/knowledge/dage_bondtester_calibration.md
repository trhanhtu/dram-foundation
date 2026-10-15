# Dage BondTester Fixturing & Shear Tool Standoff Calibration SOP

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented
- **Generation**: Gen 3 (180nm DRAM MPW)

## Overview & Rationale
Standard Operating Procedure (SOP) for fixturing leadframes / package substrates and calibrating the shear tool standoff height on a Dage BondTester. This metrology validation step ensures compliance with MIL-STD-883 Method 2011 ball shear and wire pull verification for 180nm open-source DRAM dice.

## Physical System Context
- **Substrate / Leadframe**: DRAM die attached using silver-filled conductive epoxy (Ablebond 84-1LMIS cured at 150°C for 60 min, R_th <= 5°C/W, void area < 5%).
- **Bond Pads**: 100 µm x 100 µm aluminum squares (PVD sputtering Al-0.5% Cu or pure Al, 350 nm ± 5% thickness).
- **Interconnect**: Thermosonic Gold Ball Bond (25 µm diameter 99.99% Au wire bonded at 150°C, 60 kHz transducer pulse).

## Calibration Protocol
1. Mechanical clamping and vacuum fixture verification.
2. Optical coplanarity measurement.
3. Touch-down Z-zeroing contact sensing.
4. Setting precise vertical standoff height to prevent pad dragging while testing ball shear strength.

## References & Related Files
- [docs/context.yaml](..../../context.yaml)
- [docs/context2.yaml](..../../context2.yaml)
- [docs/context3.yaml](..../../context3.yaml)

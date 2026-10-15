# Micro-Knowledge: ATE Loadboard PDN Target Impedance AC Simulation & DRC Sign-off

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Defines target impedance constraints ($Z_{target} \le 85\text{ m}\Omega$) and multi-frequency AC simulation sign-off procedures for the 180nm DRAM ATE loadboard across $V_{DD}$ (1.8 V), $V_{PP}$ (2.5 V to 2.8 V), and $V_{BLP}$ ($V_{DD}/2 = 0.9\text{ V}$) power rails.

## Key Details / Architecture
- **Frequency Bands**:
  - DC to 100 kHz: Regulated by ATE DPS / VRM.
  - 100 kHz to 10 MHz: Decoupled via bulk tantalum/polymer capacitors.
  - 10 MHz to 50 MHz: Tuned ceramic MLCCs (0402/0603) matching charge pump oscillator frequencies (20 MHz to 50 MHz).
  - 50 MHz to 200 MHz: On-socket low-ESL ceramic arrays absorbing sense amplifier restorative spikes ($t_{SAN-SAP} = 1\text{ to }2\text{ ns}$).
- **DRC & Current Density Constraints**: Maximum current density $\le 30\text{ mA/}\mu\text{m}^2$ for copper traces to prevent electromigration under continuous HTOL burn-in stress.

## References & Related Files
- [`docs/context.yaml`](./docs/context.yaml)
- [`docs/context2.yaml`](./docs/context2.yaml)

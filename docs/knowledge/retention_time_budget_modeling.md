# Retention Time Budget & 64ms Refresh Interval Statistical Sensitivity Modeling

- **Date**: 2026-10-12
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Captures the statistical sensitivity modeling protocol for evaluating DRAM retention budgets across process-voltage-temperature (PVT) corners in 180nm 1T1C COB architectures. Ensures retention time limits exceed the standard 64 ms refresh interval at elevated junction temperatures (85°C).

## Key Details / Architecture
- **Cell Capacitance**: $C_s \ge 28\text{ fF}$ (nominal range 25 to 30 fF) ensuring differential bitline sensing $\Delta V \ge 100\text{ mV}$ with bitline capacitance $C_{BL} \approx 250\text{ fF}$.
- **Leakage Target**: Total cell leakage (junction + subthreshold + dielectric) $I_{\text{leak}} < 1.0\text{ fA/cell}$ at $85^\circ\text{C}$.
- **Statistical Sensitivity**: Monte Carlo modeling ($N \ge 10,000$) evaluates worst-case tail retention distributions ($t_{\text{ret}} = Q_{\text{usable}} / I_{\text{leak}} \ge 64\text{ ms}$).

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](../context.yaml)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](../context2.yaml)
- [Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout](../context3.yaml)

# Micro-Knowledge: Differential Sense Amplifier Latch Trigger Timing & Waveform Metrology

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI, DRAM Foundation VN Council)
- **Status**: Implemented

## Overview & Rationale
In high-speed 180nm folded-bitline DRAM arrays, sensing margin and tRCD latency verification rely on precise multi-phase latch activation sequences ($SAN$ pulldown followed by $SAP$ pullup). Because signal development $\Delta V = \frac{C_s}{C_{BL} + C_s}(V_{cell} - V_{DD}/2)$ yields only 100 mV to 150 mV across folded bitline pairs ($C_{BL}/C_s$ maintained between 5:1 and 9:1), premature or asymmetric activation leads to sense amp decision inversion or destructive readout.

## Key Details & Architecture
1. **Precharge & Equalization**: Equalization network ties $BL$ and $/BL$ to precision $V_{BLP} = V_{DD}/2$.
2. **Access Gate Overdrive**: Wordline ($WL$) asserted from $0\text{ V}$ to boosted $V_{PP}$ ($2.6\text{ V}$ to $2.8\text{ V}$) to prevent $V_{th}$ threshold drop during full charge transfer from $C_s \ge 25\text{ fF}-30\text{ fF}$ into $C_{BL} \approx 150\text{ fF}-250\text{ fF}$.
3. **Regenerative Latch Sequencing**:
   - Phase 1: N-Sense Amp activation pulling common node $SAN$ from $V_{DD}/2$ rapidly to $\text{GND}$ via NMOS pulldown switch.
   - Phase 2: P-Sense Amp activation pulling common node $SAP$ to $V_{DD}$ after a calibrated $1\text{ ns}$ to $2\text{ ns}$ delay via PMOS pullup switch.
4. **Metrology Instrumentation**: Low-capacitive active differential probing on FPGA testbench coupled with HIL trigger metrology to verify $t_{RCD}$ margin without loading parasitic bitline capacitance.

## References & Related Files
- [Cross-Coupled Regenerative Sense Amplifier Timing & Charge Restoration](./docs/sop_sense_amplifier_latch_metrology.md)
- [Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout](./docs/sop_sense_amplifier_latch_metrology.md)
- [1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets](./docs/sop_sense_amplifier_latch_metrology.md)

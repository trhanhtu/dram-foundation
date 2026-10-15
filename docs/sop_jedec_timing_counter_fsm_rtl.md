# SOP: JEDEC Timing Counter & FSM Architecture RTL Encoding

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Accepted
- **Generation**: Gen 2 (180nm CMOS)
- **Context**: `180nm Open-Source DRAM Chip (DRAM Foundation VN) > ESP32 Closed-Loop Motor Controller > FPGA High-Speed DRAM Memory Controller Core > JEDEC Timing & Refresh Protocol State Machine Architecture Modeling > Verilog RTL State Machine Implementation of Command & Refresh Sequencer > JEDEC Timing Counter & FSM Architecture RTL Encoding`

---

## 1. Executive Summary & Literature Grounding
This Standard Operating Procedure (SOP) governs the digital RTL synthesis, state encoding, and timing counter design for the DRAM command and refresh engine targeting the 180nm open-source DRAM architecture. Timing parameters and refresh intervals directly map to the analog physics of the cell:
- **Sense Amplifier Operational Phasing**: Equalization to $V_{BLP} = V_{DD}/2$, Wordline boost to $V_{PP} = 2.6\,\text{V} - 2.8\,\text{V}$ overdriving access gate $(L = 180\,\text{nm}, W = 220\,\text{nm})$, N-sense amplification ($SAN$ pulled to GND), followed by P-sense amplification ($SAP$ pulled to $V_{DD}$) after a fixed $1\,\text{ns} - 2\,\text{ns}$ delay.
- **Capacitive Signal Sharing**: Cell capacitance $C_s \ge 28\,\text{fF}$ (stacked capacitor ONO/high-k $\kappa > 15$) and bitline capacitance $C_{BL} = 250\,\text{fF}$ yielding a read differential voltage $\Delta V = \frac{C_s}{C_{BL} + C_s} (V_{cell} - V_{DD}/2) \approx 100\,\text{mV} - 150\,\text{mV}$.
- **Retention & Leakage**: Sub-threshold and junction leakage kept below $1\,\text{fA/cell}$ at $85^\circ\text{C}$ establishing JEDEC auto-refresh counter periods.

---

## 2. References & Literature Context Citations
1. **Cross-Coupled Regenerative Sense Amplifier Timing & Charge Restoration**: Equalization ($V_{BLP} = V_{DD}/2$), WL overdrive ($V_{PP} = 2.6\,\text{V} - 2.8\,\text{V}$), $SAN$ NMOS pulldown, and $SAP$ PMOS pullup delay ($1\,\text{ns} - 2\,\text{ns}$).
2. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**: Cell capacitance $C_s = 25\,\text{fF} - 28\,\text{fF}$, bitline capacitance $C_{BL} = 250\,\text{fF}$, signal delta $\Delta V = 100\,\text{mV} - 150\,\text{mV}$.
3. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: 180nm channel length ($L = 180\,\text{nm}, W = 220\,\text{nm}$), stacked capacitor budget $\ge 28\,\text{fF}$, dielectric $\kappa > 15$, and leakage target $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$.

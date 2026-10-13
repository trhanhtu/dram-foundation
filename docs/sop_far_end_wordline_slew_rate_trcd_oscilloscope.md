# SOP: Far-End Wordline Slew Rate & Activation Delay tRCD Oscilloscope Characterization

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Proposed
- **Generation**: Gen 2 (µm / 180nm Open-Source DRAM Chip)
- **Subsystem**: Address Decoders & Wordline VPP Voltage Pump > Hierarchical Row/Column Address Predecoder & Wordline Driver Sizing > Distributed RC Wordline Slew Rate & Activation Delay Transient Metrology > Far-End Wordline Slew Rate & Activation Delay tRCD Oscilloscope Characterization

## Overview & Rationale
In the 180nm Open-Source DRAM architecture, wordlines span across dense memory sub-arrays with an aggressive pitch of $360\,\text{nm} - 400\,\text{nm}$. Each access transistor features channel dimensions of $L = 180\,\text{nm}$, $W = 220\,\text{nm}$, and a thermally grown $\text{SiO}_2$ gate oxide of $3.5\,\text{nm}$ (fabricated via dry oxidation at $850^\circ\text{C} - 900^\circ\text{C}$). Due to distributed polysilicon sheet resistance and parasitic gate-channel capacitances across hundreds of cells, the wordline voltage pulse experiences signal attenuation, edge degradation, and propagation skew along the line. 

This SOP defines the metrology procedure for direct high-bandwidth oscilloscope probing and transient characterization of the far-end wordline slew rate ($10\% - 90\%$ rise time) and row-to-column activation delay ($t_{RCD}$). Physical measurement of the far-end transient response ensures that sufficient gate overdrive ($V_{PP}$) reaches the furthest cell to transfer stored charge ($C_s = 25\,\text{fF} - 30\,\text{fF}$, minimum $28\,\text{fF}$) onto the folded bitline ($C_{BL} = 250\,\text{fF}$), developing the required $\Delta V = 100\,\text{mV} - 150\,\text{mV}$ differential signal within the timing margin prior to sense amplifier latching.

## Architectural Flow
```text
┌────────────────────────────────────────────────────────┐
│ 180nm DRAM Array Under Test & Oscilloscope Test Fixture│
│ (Sub-array Row with Pitch 360-400 nm, L=180 nm, W=220nm)│
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Micro-Probing & High-Bandwidth Active Probe Attachment │
│ - Near-End (Wordline Driver Output)                   │
│ - Far-End (Terminus Micro-Pad across Distributed Line) │
│ - Bitline Sense Amplifier SAN/SAP Activation Nodes     │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Row Activation Triggering & Transient Waveform Capture │
│ - Issue ACT Command at Thermal Chuck Condition (85°C)  │
│ - Synchronous Oscilloscope Trigger on Command / Wordline│
│ - Multi-Channel High-Speed Real-Time Digitization      │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Slew Rate, Propagation Delay & tRCD Analysis           │
│ - Far-End 10%-90% Slew Rate Metrology                  │
│ - Near-End to Far-End Wordline Delay Delta t_WL        │
│ - Delta V Bitline Signal Development & Latch Timing    │
└────────────────────────────────────────────────────────┘
```

## Step-by-Step SOP Procedure
1. **Test Vehicle & Wafer Chuck Setup**:
   - Mount the 180nm DRAM test coupon/wafer onto a low-noise, temperature-controlled analytical probe station chuck.
   - Establish baseline thermal test conditions at $85^\circ\text{C}$ to capture worst-case sub-threshold leakage, junction leakage ($< 1\,\text{fA/cell}$ target), and elevated polysilicon/interconnect resistivity.
   - Verify power supply rails: core voltage $V_{DD}$, bitline precharge reference ($V_{DD}/2$), and boosted wordline high-voltage supply ($V_{PP}$).

2. **Low-Capacitive Micro-Probe Station Landing**:
   - Under high-magnification optical microscopy, land active high-impedance FET micro-probes ($C_{probe} < 0.2\,\text{fF}$ loading equivalent or low-capacitance active differential probe heads) onto dedicated test structures:
     - **Channel 1 (CH1)**: Row Address Strobe / ACT command trigger input.
     - **Channel 2 (CH2)**: Wordline driver local output (Near-End $WL_{near}$).
     - **Channel 3 (CH3)**: Array boundary wordline termination monitor pad (Far-End $WL_{far}$, positioned across the entire $360\,\text{nm} - 400\,\text{nm}$ pitch array).
     - **Channel 4 (CH4)**: Bitline sense amplifier differential node or sensing strobe ($\text{SAN}/\text{SAP}$).

3. **Oscilloscope Calibration & Deskew**:
   - Power on the real-time digital storage oscilloscope (minimum bandwidth $\ge 4\,\text{GHz}$, sampling rate $\ge 20\,\text{GS/s}$).
   - Perform hardware propagation deskew across all active channels using a fast sub-nanosecond rise-time calibration edge source to eliminate cable and probe propagation offsets.
   - Set vertical resolution to $200\,\text{mV/div}$ or $500\,\text{mV/div}$ with 50 $\Omega$ / high-Z matching according to probe specifications.

4. **Transient Wordline Slew Rate & Far-End Rise Time Measurement**:
   - Drive periodic Row Activation (ACT) commands from the pattern generator or test controller.
   - Trigger the oscilloscope on the rising edge of the internal ACT command clock.
   - Capture the simultaneous rising waveforms at $WL_{near}$ and $WL_{far}$.
   - Compute the far-end wordline slew rate by extracting the $10\%$ to $90\%$ voltage transition duration ($t_{rise, far}$) as the pulse transitions from $0\,\text{V}$ to the target $V_{PP}$ plateau.
   - Quantify transmission line propagation skew: $\Delta t_{WL} = t_{50\%}(WL_{far}) - t_{50\%}(WL_{near})$.

5. **Activation Delay ($t_{RCD}$) & Signal Development Validation**:
   - Measure the elapsed duration from the $50\%$ point of the external ACT command clock to the $50\%$ rising point of $WL_{far}$.
   - Monitor the differential bitline readout voltage development $\Delta V = \frac{C_s}{C_{BL} + C_s} \cdot (V_{cell} - V_{DD}/2)$ on the access cell.
   - With nominal bitline parasitic capacitance $C_{BL} = 250\,\text{fF}$ and storage cell capacitance $C_s = 25\,\text{fF} - 30\,\text{fF}$ (minimum $28\,\text{fF}$), verify that the far-end wordline reaches full conduction threshold in time to establish the required $\Delta V = 100\,\text{mV} - 150\,\text{mV}$ before the sense amplifier strobe ($\text{SAN}$ pulling to ground) latches.
   - Log $t_{RCD}$ across multiple row addresses to identify row decoder path variations.

6. **Data Logging & Statistical Reporting**:
   - Record waveform traces, $10\% - 90\%$ slew rate, propagation delay, and $t_{RCD}$ across 1,000 continuous cycles.
   - Export transient ASCII/CSV datasets to the DRAM engineering metrology database for correlation against 3D distributed RC extraction models.

## Acceptance Criteria Targets
1. **Far-End Wordline Slew Rate & Rise Time**: The far-end wordline $10\%$ to $90\%$ voltage rise time ($t_{rise, far}$) to $V_{PP}$ must not exceed the target threshold, ensuring rapid channel inversion for access transistors with gate length $L = 180\,\text{nm}$, width $W = 220\,\text{nm}$, and $t_{ox} = 3.5\,\text{nm}$ $\text{SiO}_2$.
2. **Readout Differential Signal Margin under Far-End Timing**: Far-end wordline turn-on must allow complete cell charge transfer prior to sense amplifier activation, achieving a differential bitline signal $\Delta V$ strictly within $100\,\text{mV}$ to $150\,\text{mV}$ given cell capacitance $C_s = 25\,\text{fF} - 30\,\text{fF}$ (minimum $28\,\text{fF}$) and bitline capacitance $C_{BL} = 250\,\text{fF}$.
3. **Array Layout Pitch & Physical Structure Consistency**: Physical metrology and micro-probing validated across the standard sub-array row layout pitch of $360\,\text{nm}$ to $400\,\text{nm}$.
4. **Thermal Stability & Retention Environmental Target**: Metrology characterization executed on a temperature-controlled chuck at $85^\circ\text{C}$ with access cell junction leakage verified $< 1\,\text{fA/cell}$ to guarantee retention time $> 64\,\text{ms}$.

## References & Literature Sources
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**: Differential signal development formula $\Delta V = \frac{C_s}{C_{BL} + C_s} \cdot (V_{cell} - V_{DD}/2)$, cell capacitance $C_s = 25\,\text{fF}$, bitline capacitance $C_{BL} = 250\,\text{fF}$, differential target $\Delta V = 100\,\text{mV} - 150\,\text{mV}$, sense amplifier precharge to $V_{DD}/2$, and SAN/SAP activation timing.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry with access transistor length $L = 180\,\text{nm}$ and width $W = 220\,\text{nm}$, minimum cell capacitance budget of $28\,\text{fF/cell}$, and junction/sub-threshold leakage target $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: 1T1C stacked capacitor architecture ($8F^2 / 6F^2$), cell capacitance range $25\,\text{fF} - 30\,\text{fF}$, data retention time $> 64\,\text{ms}$ at $85^\circ\text{C}$, wordline and bitline pitch of $360\,\text{nm} - 400\,\text{nm}$, and gate oxide physical thickness $\sim 3.5\,\text{nm}$ $\text{SiO}_2$ grown via $850^\circ\text{C} - 900^\circ\text{C}$ dry oxidation.

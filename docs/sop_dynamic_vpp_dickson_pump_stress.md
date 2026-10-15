# Standard Operating Procedure (SOP): Dynamic V_PP Dickson Pump Stress & In-Situ Overdrive Degradation Logging

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Module Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > BEOL Multi-Layer Metallization, Wafer Sort & Packaging > Final Automated Test Equipment (ATE) JEDEC DDR Speed-Bin & HTOL Burn-in Testing > HTOL Dynamic Thermal-Voltage Accelerated Burn-in Stress Execution > HTOL Burn-in Board Socketing & Dynamic Stress Pattern Programming with V_PP Overdrive Cycling > In-Chamber Dynamic Signal Integrity & Wordline Boost Leakage In-Situ Monitoring > Dynamic V_PP Dickson Pump Stress & In-Situ Overdrive Degradation Logging

## 1. Overview & Scope
This Standard Operating Procedure (SOP) governs the dynamic stress acceleration, overdrive degradation qualification, and in-situ parametric monitoring of the 4-stage on-chip Dickson charge pump driving the wordline high-voltage booster rail ($V_{PP}$) on the 180nm DRAM process. Stress is performed on packaged units socketed inside dynamic High-Temperature Operating Life (HTOL) burn-in chambers under continuous clocking and wordline toggle workloads.

## 2. Process Flow
```
┌────────────────────────┐
│  HTOL Burn-in Chamber  │
│     & Socket Setup     │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│      Dickson Pump      │
│  Clocking: Phi1/Phi2   │
│        20-50MHz        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Overdrive Cycling:   │
│  V_PP Stress at 2.5V   │
│         - 2.8V         │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│    In-Situ Wordline    │
│  Boost & Dynamic V_PP  │
│        Logging         │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│       Acceptance       │
│  Screening: Retention  │
│   & Leakage Analysis   │
└────────────────────────┘
```

## 3. Step-by-Step Procedure
1. **Chamber Thermal Stabilization & Environmental Control**:
   - Install packaged 180nm DRAM test devices into the HTOL Burn-in Board (BIB) sockets.
   - Establish baseline chamber thermal monitoring at $85^\circ\text{C}$ across all device zones using calibrated sensors.
2. **Dickson Oscillator & Non-Overlapping Phase Clocks Setup**:
   - Program the internal oscillator / external ATE test clock generator to supply non-overlapping two-phase clocking ($\Phi_1, \Phi_2$) to the 4-stage Dickson charge pump at frequencies between $20\text{ MHz}$ and $50\text{ MHz}$.
   - Ensure flying pump capacitances ($C_{\text{pump}}$) between $20\text{ pF}$ and $50\text{ pF}$ per stage are actively shuttling charge per clock phase.
3. **Dynamic $V_{PP}$ Overdrive Voltage Cycling**:
   - Bias nominal core supply $V_{DD} = 1.8\text{ V}$.
   - Regulate dynamic overdrive target to generate boosted wordline voltage $V_{PP} = V_{DD} + V_{th} + \Delta V_{\text{overdrive}}$ in the range of $2.5\text{ V}$ to $2.8\text{ V}$ (accounting for pass gate access transistor $V_{th} \sim 0.5\text{ V}\text{--}0.7\text{ V}$).
   - Toggle memory cell wordlines ($L = 180\text{ nm}, W = 220\text{ nm}$) continuously to induce maximum AC Hot Carrier Injection (HCI) and Bias Temperature Instability (BTI) stress across the access transistor gate dielectric and pump pass gates.
4. **In-Situ Metrology & Degradation Telemetry Logging**:
   - Continuously record the feedback comparator trip threshold, pump charging latency, steady-state $V_{PP}$ boost ripple, and regulator shut-off margins.
   - Monitor storage node write levels ($V_{SN}$) to ensure the written level does not degrade towards the non-boosted drop ($V_{DD} - V_{th} = 1.8\text{ V} - 0.6\text{ V} = 1.2\text{ V}$).
   - Conduct periodic post-stress in-situ retention scans to evaluate cell sub-threshold/junction leakage against the $1\text{ fA/cell}$ threshold at $85^\circ\text{C}$.

## 4. Machine-Measurable Acceptance Criteria
| Metric / Parameter | Target Value / Limit | Physical Unit | Measurement Condition |
| :--- | :--- | :--- | :--- |
| Wordline Boosted Voltage ($V_{PP}$) | $2.5 \le V_{PP} \le 2.8$ | $\text{V}$ | Dynamic load under active $\Phi_1, \Phi_2$ switching |
| Dickson Clock Frequency Range | $20 \text{ to } 50$ | $\text{MHz}$ | Non-overlapping two-phase clock $\Phi_1, \Phi_2$ |
| Flying Pump Capacitance ($C_{\text{pump}}$) | $20 \text{ to } 50$ | $\text{pF}$ | Per-stage Dickson flying capacitor budget |
| DRAM Cell Sub-Threshold & Junction Leakage | $< 1.0$ | $\text{fA/cell}$ | Tested in-situ at $85^\circ\text{C}$ across $L = 180\text{ nm}, W = 220\text{ nm}$ access transistors |
| Unit Cell Storage Capacitance | $\ge 28.0$ | $\text{fF}$ | Stacked MIM/ONO crown capacitor |

## 5. References & Literature Context
- *High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture* (NMOS $V_{th} \sim 0.5\text{ V}\text{--}0.7\text{ V}$; $V_{DD}=1.8\text{ V}$; $V_{PP} \ge 2.5\text{ V}\text{--}2.8\text{ V}$; 4-stage pump; $C_{\text{pump}} = 20\text{--}50\text{ pF}$; $\Phi_1, \Phi_2$ at $20\text{--}50\text{ MHz}$; dynamic feedback comparator regulator).
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench* (Transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$; Stacked ONO/MIM capacitor $C_{\text{cell}} \ge 28\text{ fF}$; Sub-threshold/junction leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$).

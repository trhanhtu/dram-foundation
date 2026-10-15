# Standard Operating Procedure (SOP)
## PRBS Pattern Transient Simulation & Bitline-to-Bus Coupling Analysis

- **Module**: Circuit Design & Signal Integrity Verification
- **Technology Node**: 180 nm Open-Source CMOS DRAM (Gen 2 µm)
- **Context Path**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > ESP32 Closed-Loop Motor Controller [Electronics & Firmware] > Signal Integrity & Level Shifter Daughtercard PCB (50-Ohm Controlled Impedance Microstrips) [PCB & Hardware] > 50-Ohm Controlled Impedance Stackup Design & Level Shifter Schematic Synthesis [Circuit Design] > High-Speed Bus Signal Integrity Transient & Eye-Diagram Verification [Metrology] > PRBS Pattern Transient Simulation & Bitline-to-Bus Coupling Analysis [Circuit Design]
- **Target Channel Impedance**: $50\,\Omega$ controlled impedance microstrip bus
- **Core Operating Voltages**: Core $V_{DD} = 1.8\,\text{V}$, Wordline Boosted $V_{PP} \ge 2.5\,\text{V}\text{--}2.8\,\text{V}$, Bitline Precharge $V_{BL} = V_{DD} / 2 = 0.9\,\text{V}$

---

### 1. Step-by-Step Simulation & Analysis Procedure

#### Step 1: Subcircuit Netlist Assembly & Transistor Level Modeling
- Load the SPICE/Spectre subcircuits for the 180 nm folded bitline 1T1C memory array:
  - Access transistor: NMOS enhancement mode with channel length $L = 180\,\text{nm}$, channel width $W = 220\,\text{nm}$, and threshold voltage $V_{th} = 0.5\,\text{V}\text{--}0.7\,\text{V}$.
  - Storage capacitor: MIM / stacked capacitor modeled at $C_s = 25\,\text{fF}\text{--}28\,\text{fF}$.
  - Bitline parasitic capacitance: $C_{BL} = 250\,\text{fF}$ per complementary pair ($BL$ and $\overline{BL}$).
  - Wordline overdrive supply: $V_{PP} = 2.5\,\text{V}\text{--}2.8\,\text{V}$ (driven by the 4-stage Dickson charge pump oscillator operating at $20\,\text{MHz}\text{--}50\,\text{MHz}$).
  - Sense amplifier: CMOS cross-coupled latch with equalization network precharged to $V_{DD}/2 = 0.9\,\text{V}$.

#### Step 2: PCB Microstrip Bus & Level Shifter Distributed Interconnect Coupling
- Instantiate the transmission line model for the daughtercard PCB $50\,\Omega$ microstrip bus interconnect between the DRAM peripheral I/O and the ESP32 controller interface.
- Couple the extracted bitline-to-I/O pad parasitic mutual capacitance ($C_m$) and cross-talk inductances ($L_m$) representing the layout routing transitions from array core to peripheral data bus lines.
- Terminate the high-speed data bus with matched $50\,\Omega$ characteristic impedance terminations to prevent standing-wave reflections.

#### Step 3: PRBS Pattern Generation & Transient Stimulus Configuration
- Configure an autonomous pseudo-random binary sequence generator (PRBS-7 or PRBS-9) at the high-speed bus inputs:
  - Operating data bit rate synchronized to the memory bus cycle.
  - Driver swing voltage set to peripheral interface logic levels ($1.8\,\text{V}$ core I/O stepping through level-shifter daughtercard).
  - Rise/fall transition times ($t_r, t_f$) set according to 180 nm I/O buffer slew rate constraints.
- Concurrently apply non-overlapping two-phase clocking ($\Phi_1, \Phi_2$ at $20\,\text{MHz}\text{--}50\,\text{MHz}$) to the $V_{PP}$ charge pump circuitry with flying capacitor models ($C_{pump} = 20\,\text{pF}\text{--}50\,\text{pF}$).

#### Step 4: Transient Read/Write Sensing & Coupling Simulation Execution
- Run SPICE transient simulation (`.tran`) over a minimum of 1024 PRBS bit intervals across operating temperature corners up to $85^\circ\text{C}$:
  - Precharge phase: Assert bitline equalization transistor network to set $V_{BL} = \overline{V_{BL}} = V_{DD}/2 = 0.9\,\text{V}$.
  - Charge sharing phase: Pulse wordline to $V_{PP} \ge 2.5\,\text{V}$ to develop differential voltage:
    $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \times \left(V_{cell} - \frac{V_{DD}}{2}\right) \approx 100\,\text{mV}\text{--}150\,\text{mV}$$
  - Sensing phase: Enable sense amplifier latch signals ($SAN$ pulling low, $SAP$ pulling high) during simultaneous pseudo-random data bus transitions.

#### Step 5: Eye-Diagram, Jitter, & Signal Margin Metrology
- Extract eye-diagram parameters from the high-speed $50\,\Omega$ bus node: eye height, eye width, deterministic jitter (DJ), and total jitter (TJ).
- Measure bitline differential sense margin degradation: monitor peak coupling noise voltage injected from switching bus lines onto $BL / \overline{BL}$.
- Verify that sub-threshold and junction leakage remain below $1\,\text{fA/cell}$ at $85^\circ\text{C}$ to maintain cell retention during bus switching activity.

---

### 2. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Units | Tolerance / Boundary | Measurable Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Bitline Read Differential Signal ($\Delta V$)** | `100 to 150` | $\text{mV}$ | Minimum developed sensing window ($C_s = 25\text{--}28\,\text{fF}$, $C_{BL} = 250\,\text{fF}$) | SPICE Transient Waveform Measurement at SA Strobe |
| **Wordline Boost Voltage ($V_{PP}$)** | `2.5 to 2.8` | $\text{V}$ | Minimum overdrive level ($\ge V_{DD} + V_{th} + \Delta V_{overdrive}$) | Dynamic Node Voltage Extraction on Wordline Driver |
| **Bus Characteristic Impedance ($Z_0$)** | `50.0` | $\Omega$ | $\pm 10\%$ ($45\,\Omega\text{--}55\,\Omega$) | TDR / S-Parameter Transient Interconnect Extraction |
| **Cell Leakage Current (@ 85°C)** | $\le 1.0$ | $\text{fA/cell}$ | Maximum allowable threshold (sub-threshold + junction) | DC Operating Point / High-Temp Leakage SPICE Test |

---

### 3. Citations & References

- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*: Access transistor channel length $L = 180\,\text{nm}$, width $W = 220\,\text{nm}$; storage capacitance budget $\ge 28\,\text{fF/cell}$ (dielectric stack with $\kappa > 15$); cell sub-threshold and junction leakage current $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$.
- *High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture*: Pass transistor $V_{th} \sim 0.5\,\text{V}\text{--}0.7\,\text{V}$; nominal $V_{DD} = 1.8\,\text{V}$; boosted wordline overdrive voltage $V_{PP} = V_{DD} + V_{th} + \Delta V_{overdrive} \ge 2.5\,\text{V}\text{--}2.8\,\text{V}$; 4-stage charge pump with flying capacitors $C_{pump} = 20\,\text{pF}\text{--}50\,\text{pF}$ driven by two-phase non-overlapping clocks ($\Phi_1, \Phi_2$) at $20\,\text{MHz}\text{--}50\,\text{MHz}$.
- *Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout*: Folded bitline architecture; precharge equalization to $V_{DD}/2 = 0.9\,\text{V}$; nominal cell capacitance $C_s = 25\,\text{fF}$, bitline capacitance $C_{BL} = 250\,\text{fF}$; differential sensing signal $\Delta V \approx 100\,\text{mV}\text{--}150\,\text{mV}$; CMOS cross-coupled latch sensing with $SAN$ and $SAP$.

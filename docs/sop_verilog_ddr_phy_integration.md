# SOP: Verilog DDR PHY IP Block Integration & Differential I/O Pin Placement

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Proposed
- **Action Type**: Make
- **Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > ESP32 Closed-Loop Motor Controller [Electronics & Firmware] > FPGA High-Speed DRAM Memory Controller Core (Verilog DDR PHY & JEDEC State Machine) [Digital Logic & FPGA] > Verilog DDR PHY IP Block Integration & Differential I/O Pin Placement [Circuit Design]

## Overview & Rationale
This Standard Operating Procedure (SOP) governs the structural integration and differential I/O pin placement for the high-speed Verilog DDR PHY IP block interfacing with the 180nm open-source DRAM architecture. It specifies signal timing constraints, differential pair pin assignment (CK/CK#, DQS/DQS#), voltage rails, and equalization dynamics matching the physical 180nm stacked capacitor bitline architecture.

## Step-by-Step Procedure
1. **Verilog DDR PHY IP Core Parameterization**:
   - Instantiate the DDR PHY top-level Verilog module (`ddr_phy_top.v`) connecting the memory controller state machine to the high-speed I/O bank primitives.
   - Configure serializer/deserializer (SERDES) gear ratios (2:1 or 4:1) and internal phase-locked loop (PLL) / DLL clocks for 90-degree phase shift on DQS write strobes.
2. **Differential Clock (CK/CK#) and Strobe (DQS/DQS#) Pin Placement**:
   - Assign complementary clock pairs `CK_P` / `CK_N` and data strobe pairs `DQS_P` / `DQS_N` strictly to dedicated differential hardware pin pairs in adjacent FPGA/ASIC I/O banks.
   - Constrain standard single-ended address and command lines (A[0:13], BA[0:2], RAS#, CAS#, WE#) to the same bank to prevent inter-bank propagation skew.
3. **I/O Standard and Termination Definition**:
   - Define I/O standard constraints in physical UCF/XDC/SDC files (e.g., SSTL-18 / differential SSTL-18) with a 1.8V nominal $V_{DD}$ rail.
   - Set reference voltage pin $V_{REF} = V_{DD} / 2 = 0.90\text{ V}$ and bitline precharge / termination voltage $V_{BLP} = V_{DD} / 2 = 0.90\text{ V}$.
4. **Skew Minimization & Length Matching**:
   - Enforce board and package trace length matching: intra-pair skew between complementary differential legs $\le 1\text{ ps}$ (within $0.15\text{ mm}$ trace delta).
   - Match DQ data line lengths to their associated DQS strobe group within $\pm 5\text{ ps}$ ($\pm 0.75\text{ mm}$) to maintain valid window sampling margin over the 100 mV to 150 mV signal differential sensing range.
5. **Physical Subsystem Interface Timing Verification**:
   - Verify wordline gate overdrive level compatibility ($V_{PP} = 2.6\text{ V}$ to $2.8\text{ V}$) to ensure complete $V_{DD}$ charge restoration across cell access transistors without threshold loss ($V_{DD} + V_{th}$).
   - Set N-sense amplifier latch assertion ($SAN \to \text{GND}$) followed by P-sense amplifier ($SAP \to V_{DD}$) with a calibrated 1.0 ns to 2.0 ns inter-activation delay.

## Machine-Measurable Acceptance Criteria
1. **Differential Sense Voltage Development ($\Delta V$)**:
   - Target: $100\text{ mV} \le \Delta V \le 150\text{ mV}$ developed across folded bitline pair $(BL - \overline{BL})$ for $C_s = 25\text{ fF}$ to $28\text{ fF}$ and $C_{BL} = 250\text{ fF}$.
2. **Access Gate Wordline Overdrive Voltage ($V_{PP}$)**:
   - Target: $2.6\text{ V} \le V_{PP} \le 2.8\text{ V}$ to eliminate access transistor threshold degradation during cell readout and restore phases.
3. **Stacked Cell Storage Capacitance ($C_s$)**:
   - Target: $C_s \ge 28\text{ fF/cell}$ with effective dielectric constant $\kappa > 15$ and sub-threshold/junction leakage current $I_{leak} \le 1.0\text{ fA/cell}$ at $85^\circ\text{C}$.
4. **Cross-Coupled Sense Latch Activation Skew ($t_{delay(SAN \to SAP)}$)**:
   - Target: $1.0\text{ ns} \le t_{delay(SAN \to SAP)} \le 2.0\text{ ns}$ between NMOS pull-down ($SAN \to 0\text{ V}$) and PMOS pull-up ($SAP \to V_{DD}$).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- Source: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- Source: *Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout*
- Source: *Cross-Coupled Regenerative Sense Amplifier Timing & Charge Restoration*

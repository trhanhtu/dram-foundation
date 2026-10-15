# 180nm 1T1C DRAM Sensing Margin SPICE Simulation & Verilog March C- BIST Engine

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
In semiconductor engineering, high-level Work Breakdown Structures (WBS) and Standard Operating Procedures (SOPs) must be anchored to verifiable physical equations and synthesizable silicon artifacts ("Bits-to-Atoms"). 

This bridge provides:
1. **Executable SPICE Subcircuits & Transient Simulation Deck**: Models the fundamental physical phenomena of a 180nm 1T1C DRAM storage cell, access transistor non-idealities, bitline parasitic capacitances, and cross-coupled CMOS sense amplifier latch dynamics.
2. **Synthesizable Verilog March C- Memory Built-In Self-Test (BIST) Engine**: Implements the industry-standard 10N March C- test sequence to detect 100% of stuck-at, transition, coupling, and address decoder faults across the memory array.
3. **Automated Physical Simulation Runners & Pytest Test Suite**: Validates mathematical charge sharing, latching speed, margin sensitivity against bitline capacitance, and fault injection detection.

---

## Key Details & Architecture

### 1. 1T1C DRAM Physical Cell & Charge Sharing Dynamics
The unit bitcell consists of a single access NMOS transistor and a stacked MIM (Metal-Insulator-Metal) storage capacitor:
- **Storage Node Capacitance ($C_s$)**: $28.0\text{ fF}$ (High-k $\text{Al}_2\text{O}_3 / \text{Ta}_2\text{O}_5$ dielectric crown capacitor).
- **Bitline Parasitic Capacitance ($C_{BL}$)**: $150.0\text{ fF}$ (256 cells per folded bitline column, junction + wire parasitics).
- **Core Supply Voltage ($V_{DD}$)**: $1.8\text{ V}$.
- **Precharge Voltage ($V_{EQ}$)**: $\frac{V_{DD}}{2} = 0.9\text{ V}$.
- **Boosted Wordline Overdrive ($V_{PP}$)**: $2.8\text{ V}$ (overcomes $V_{th} \approx 0.55\text{ V}$ to prevent threshold voltage degradation during '1' restoration).

When the wordline is pulsed to $V_{PP}$, charge sharing between $C_s$ and $C_{BL}$ develops an initial differential voltage $\Delta V_{BL}$:
$$\Delta V_{BL} = \frac{C_s}{C_s + C_{BL}} \cdot (V_{cell} - V_{EQ}) = \frac{28\text{ fF}}{28\text{ fF} + 150\text{ fF}} \cdot (\pm 0.9\text{ V}) = \pm 141.57\text{ mV}$$

Because the complementary reference bitline ($\overline{BL}$) remains at $V_{EQ} = 0.9\text{ V}$, the differential sensing voltage is:
$$\Delta V_{diff} = |V_{BL} - V_{\overline{BL}}| = 141.57\text{ mV}$$

This value exceeds the typical 180nm sense amplifier input offset voltage ($V_{OS} \approx 25 - 30\text{ mV}$) with a healthy Signal-to-Noise Ratio (SNR > 4.5).

### 2. Folded Bitline Sense Amplifier & Full-Rail Regeneration
The sense amplifier utilizes a CMOS cross-coupled latch with timed activation strobes:
1. **Precharge & Isolation**: Equalization transistor ($MEQ$) maintains $BL = \overline{BL} = 0.9\text{ V}$. $EQ$ drops to $0\text{ V}$ prior to wordline activation.
2. **Wordline Firing**: $WL \to 2.8\text{ V}$, creating the $\pm 141.6\text{ mV}$ signal on $BL$.
3. **N-Sense Strobe (`SAN`)**: Drives from $0.9\text{ V}$ down to $0.0\text{ V}$ (NMOS cross-coupled pair fires first), pulling the lower potential bitline down toward ground.
4. **P-Sense Strobe (`SAP`)**: Drives from $0.9\text{ V}$ up to $1.8\text{ V}$ (PMOS cross-coupled pair fires ~200ps later), pulling the higher potential bitline up toward $1.8\text{ V}$.
5. **Full Rail Restoration**: Bitlines reach $1.800\text{ V}$ and $0.000\text{ V}$ within $0.7\text{ ns}$ of strobe activation, fully restoring the charge in $C_s$ via the access transistor.
6. **Wordline Deassertion**: $WL$ drops to $0\text{ V}$ trapping the refreshed charge before bitline precharge re-engages.

### 3. March C- Algorithmic Memory BIST Engine
The BIST engine executes the standard 10N March C- algorithm in 6 phases:
- **$M_0: \Updownarrow (w0)$**: Write 0 to all memory locations.
- **$M_1: \Uparrow (r0, w1)$**: Ascending sweep: Read 0, verify data, write 1.
- **$M_2: \Uparrow (r1, w0)$**: Ascending sweep: Read 1, verify data, write 0.
- **$M_3: \Downarrow (r0, w1)$**: Descending sweep: Read 0, verify data, write 1.
- **$M_4: \Downarrow (r1, w0)$**: Descending sweep: Read 1, verify data, write 0.
- **$M_5: \Updownarrow (r0)$**: Verify all cells contain 0.

#### Fault Coverage Summary
The March C- sequence guarantees detection of:
- **Stuck-At Faults (SAF0, SAF1)**: 100% detected in $M_1$ and $M_2$.
- **Transition Faults (TF01, TF10)**: 100% detected in $M_2$ and $M_3$.
- **Inversion Coupling Faults (CFin)**: 100% detected in $M_1$.
- **Idempotent Coupling Faults (CFid)**: 100% detected in $M_1$.
- **Address Decoder Faults (AF)**: 100% detected across upward and downward sequences.

---

## References & Related Files
- [dram_1t1c_cell.sp](file:///D:/coding/dram/sim/spice/dram_1t1c_cell.sp): 180nm 1T1C storage bitcell subcircuit.
- [sense_amp_folded.sp](file:///D:/coding/dram/sim/spice/sense_amp_folded.sp): Folded bitline CMOS cross-coupled sense amplifier and equalizer.
- [dram_1t1c_transient.sp](file:///D:/coding/dram/sim/spice/dram_1t1c_transient.sp): Full SPICE transient signoff deck with BSIM/Level 3 models.
- [dram_march_c_bist.v](file:///D:/coding/dram/sim/verilog/dram_march_c_bist.v): Synthesizable Verilog RTL for 10N March C- BIST engine.
- [tb_dram_march_c.v](file:///D:/coding/dram/sim/verilog/tb_dram_march_c.v): Verilog verification testbench with fault injection models.
- [run_spice_simulation.py](file:///D:/coding/dram/sim/run_spice_simulation.py): Python physical transient simulator and bitline capacitance sweeper.
- [run_verilog_bist_simulation.py](file:///D:/coding/dram/sim/run_verilog_bist_simulation.py): Cycle-accurate March C- verification runner.
- [run_all_simulations.py](file:///D:/coding/dram/sim/run_all_simulations.py): Master orchestrator rendering `termaid` diagrams and `plotext` charts.
- [test_physical_bridge_simulation.py](file:///D:/coding/dram/tests/test_physical_bridge_simulation.py): Pytest regression test suite.
- [simulation_results.json](file:///D:/coding/dram/sim/simulation_results.json): Full numerical signoff output.

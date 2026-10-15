# Standard Operating Procedure (SOP): Post-Layout Gate-Level Dynamic Simulation & Full-Chip VCD Dump

- **Date**: 2026-10-15
- **Generation**: Gen 3 (180nm DRAM Chip Architecture & Integration)
- **Domain**: Circuit Design / Foundational Verification / Metrology Interface
- **Status**: Implemented

## 1. Overview & Scope
This Standard Operating Procedure (SOP) governs the dynamic gate-level timing simulation (GLS) with Standard Delay Format (SDF) back-annotation and subsequent Value Change Dump (VCD) signal capture for the 180nm DRAM chip tapeout. The generated VCD dump serves as the baseline for JEDEC DDR functional vector generation, VCD-to-STIL translation, and Automated Test Equipment (ATE) channel calibration.

---

## 2. Process Flow Architecture
```text
┌──────────────────────────────────────────────┐
│ Post-Layout Extraction (SPEF / GDS Parasitics)│
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│      SDF Generation & Back-Annotation        │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│    Gate-Level Dynamic Timing Simulation      │
│      (JEDEC DDR Functional Vectors)          │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│  Full-Chip VCD Dump & Vector Integrity Check │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│     VCD-to-STIL Translation for ATE Sort     │
└──────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Post-Layout Parasitic Back-Annotation & SDF Compilation
1. Export post-layout parasitic extraction (`.spef`) containing all parasitic metal resistances, bitline/wordline cross-coupling, and device capacitive loads adhering to the minimum manufacturing grid of `0.005 µm` (`5 nm`) and minimum Metal 1 pitch of `0.34 µm`.
2. Generate Standard Delay Format (`.sdf`) timing models across all operating corners (Typical, Slow-Slow at 85°C, Fast-Fast) using extracted parameters:
   - Target sub-micron transistor geometry: Channel length $L = 0.18\ \mu\text{m}$ ($180\text{ nm}$), width $W = 2.0\ \mu\text{m}$, down to memory access transistor geometry $L = 180\text{ nm}$, $W = 220\text{ nm}$.
   - Reference baseline NMOS threshold voltage: $V_{\text{thn}} = +0.55\text{ V} \pm 50\text{ mV}$; PMOS: $V_{\text{thp}} = -0.60\text{ V} \pm 50\text{ mV}$.
   - Ensure bitline parasitic coupling and cell node models preserve the required minimum storage capacitance budget of $\ge 28\text{ fF}$ per cell.
3. Compile the structural post-synthesis / post-layout gate netlist with gate-level timing primitives and annotate delays via `$sdf_annotate("chip_postlayout.sdf", top_tb.dut, , "sdf.log", "MAXIMUM")`.

### Step 2: Dynamic Testbench Initialization & Operating Boundary Setup
1. Configure dynamic testbench power supply nets to the operating nominal potential: $V_{\text{DD}} = 1.8\text{ V}$ ($V_{\text{DS}} = 1.8\text{ V}$ domain).
2. Configure timing resolution in the simulator header:
   ```verilog
   `timescale 1ps / 1ps
   ```
3. Initialize the core power rail and reset sequences:
   - Maintain active power stabilization time and issue standard JEDEC DDR initialization sequences (Precharge All, Mode Register Set, Extended Mode Register Set).
   - Verify zero setup/hold timing violations on command, bank address, and row/column strobe signals.

### Step 3: Execution of JEDEC Functional Cycle Stimulus
1. Apply the full JEDEC functional pattern vector set:
   - Row Activation (`ACTIVATE`) on active wordlines across memory subarrays.
   - Read and Write bursts with CAS latency verification.
   - Auto-Refresh (`REFRESH`) bursts verifying cell retention windows consistent with sub-threshold/junction leakage targets $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. Enable continuous runtime timing checks (`+notimingchecks` must **NOT** be used; dynamic timing checks remain strictly active).

### Step 4: Full-Chip VCD Signal Capture & Dumping
1. Direct the simulator to capture and log signal activities across all top-level pin interfaces and internal probe nets:
   ```verilog
   initial begin
       $dumpfile("dram_fullchip_postlayout.vcd");
       $dumpvars(0, top_tb.dut);
   end
   ```
2. Monitor VCD generation integrity to ensure no undefined states (`X` or `Z`) propagate on the bidirectional DQ data bus during valid read strobe (`DQS`) phases.
3. Flush and close the VCD dump file buffer upon pattern completion via `$dumpflush` and `$finish`.

---

## 4. Machine-Measurable Acceptance Criteria

| Target Metric | Parameter Target Value | Reference Tolerance / Condition | Units |
| :--- | :--- | :--- | :--- |
| **Minimum Unit Cell Storage Capacitance** | **$\ge 28$** | Noise immunity limit (alpha-particle soft error & coupling) | $\text{fF/cell}$ |
| **Cell Transistor Leakage Current** | **$\le 1$** | Sub-threshold & junction leakage at $85^\circ\text{C}$ | $\text{fA/cell}$ |
| **Device On/Off Current Ratio ($I_{\text{on}} / I_{\text{off}}$)** | **$> 10^7$** | Measured at $V_{\text{DS}} = 1.8\text{ V}$, $I_{\text{on}} \ge 500\ \mu\text{A}/\mu\text{m}$, $I_{\text{off}} \le 10\text{ pA}/\mu\text{m}$ | Dimensionless |
| **Physical Placement Grid Alignment** | **$0.005$** | Foundry manufacturing grid resolution | $\mu\text{m}$ |
| **Target Sub-Micron Channel Gate Length** | **$0.18$** ($180$) | Physical gate length for sub-micron validation | $\mu\text{m}$ ($\text{nm}$) |

---

## 5. Verified Local Literature Citations
1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$).
   - Capacitance budget minimum $28\text{ fF/cell}$ ensuring noise immunity.
   - Storage node leakage budget $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. **Stage 3 Reality Gate: Discrete Long-Channel MOSFET & CMOS Inverter Verification**:
   - Discrete transistor dimensions ($W/L = 2.0\ \mu\text{m} / 0.18\ \mu\text{m}$).
   - Threshold voltages: $V_{\text{thn}} = +0.55\text{ V} \pm 50\text{ mV}$, $V_{\text{thp}} = -0.60\text{ V} \pm 50\text{ mV}$.
   - $I_{\text{on}} / I_{\text{off}} > 10^7$ at $V_{\text{DS}} = 1.8\text{ V}$ ($I_{\text{on}} \ge 500\ \mu\text{A}/\mu\text{m}$, $I_{\text{off}} \le 10\text{ pA}/\mu\text{m}$).
3. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Manufacturing placement grid resolution $= 0.005\ \mu\text{m}$ ($5\text{ nm}$).
   - Contact hole dimension $= 0.17\ \mu\text{m} \times 0.17\ \mu\text{m}$, Metal 1 pitch $= 0.34\ \mu\text{m}$.

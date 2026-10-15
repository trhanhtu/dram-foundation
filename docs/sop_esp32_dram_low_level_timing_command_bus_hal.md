# SOP: ESP32 DRAM Low-Level Timing & Command Bus HAL Implementation

- **Date**: 2026-10-15
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Node Classification**: Gen 2 (µm) / Leaf Node / Action: Make
- **Hierarchy Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > ESP32 Closed-Loop Motor Controller [Electronics & Firmware] > Automated Parametric Retention & March C- Diagnostic Test Firmware [Firmware & Software] > ESP32 DRAM Low-Level Timing & Command Bus HAL Implementation [Firmware & Software]

---

## 1. Overview & Scope
This Standard Operating Procedure (SOP) defines the engineering execution workflow for designing, calibrating, and verifying the Hardware Abstraction Layer (HAL) on an ESP32 host controller driving a custom 180nm open-source 1T1C DRAM chip. The HAL manages low-level bus sequencing—multiplexed row/column addresses, command strobes (/RAS, /CAS, /WE), and bitline precharge/refresh intervals—matched to 180nm access transistor physical characteristics ($L = 180\text{ nm}$, $W = 220\text{ nm}$), folded bitline sensing physics ($\Delta V \ge 100\text{--}150\text{ mV}$, $C_{BL} \le 250\text{ fF}$, $C_s \ge 25\text{--}28\text{ fF}$), and maximum retention limits ($\ge 64\text{ ms}$ at $85^\circ\text{C}$).

---

## 2. Bus Architecture & Control Flow

```text
┌────────────────────────────────────────────────────────┐
│           ESP32 Host Controller (GPIO HAL)             │
│   Dedicated GPIO Out / Direct Register Bit-Banging     │
└───────────┬───────────────────────────────┬────────────┘
            │ Address Bus (Row / Col Mux)   │ Strobes (/RAS, /CAS, /WE)
            ▼                               ▼
┌────────────────────────────────────────────────────────┐
│         180nm DRAM Array Front-End Interface           │
│   Row Predecoder & Wordline Driver Sizing (W=220nm)    │
└───────────────────────────┬────────────────────────────┘
                            │ Wordline Assert
                            ▼
┌────────────────────────────────────────────────────────┐
│        1T1C Folded Bitline Sensing Subsystem           │
│   Cs = 25-28 fF, CBL = 250 fF, Veq = VDD/2             │
│   Delta V = (Cs / (CBL + Cs)) * (Vcell - VDD/2)        │
│   Sense Amp Latch Strobe (SAN/SAP) -> Refresh / Write  │
└────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Procedure

### Step 1: GPIO Pin Assignment & Fast Register HAL Setup
1. Configure dedicated ESP32 GPIOs for address bus lines ($A[0:N]$), bidirectional data lines ($DQ[0:M]$), and control strobe signals:
   - $\overline{\text{RAS}}$ (Row Address Strobe)
   - $\overline{\text{CAS}}$ (Column Address Strobe)
   - $\overline{\text{WE}}$ (Write Enable)
2. Bypass high-latency driver APIs and map HAL primitives directly to ESP32 fast GPIO register sets (`GPIO.out_w1ts` / `GPIO.out_w1tc`) to achieve sub-microsecond deterministic pulse widths.
3. Configure GPIO slew-rate control and pull-up/pull-down terminations to match the 360 nm to 400 nm bitline and wordline pitch routing constraints.

### Step 2: Bus Timing Parameter Configuration
1. Initialize the timing parameter matrix in the HAL driver based on 180nm physical cell constraints:
   - **$t_{RAS}$ (Active-to-Precharge Delay)**: Set minimum row activation time to ensure full charge redistribution from storage cell ($C_s \ge 25\text{--}28\text{ fF}$) onto the bitline ($C_{BL} \le 250\text{ fF}$) and allow sense amplifier cross-coupled latch restoration.
   - **$t_{RCD}$ ($\overline{\text{RAS}}$-to-$\overline{\text{CAS}}$ Delay)**: Enforce delay between row latch and column access strobe to permit differential signal development ($\Delta V = 100\text{--}150\text{ mV}$) across bitlines ($BL$ and $\overline{BL}$) before column multiplexing.
   - **$t_{RP}$ (Row Precharge Time)**: Set bitline precharge duration to guarantee bitline equalization network restores $BL$ and $\overline{BL}$ to exact $V_{DD}/2$.
   - **$t_{RC}$ (Row Cycle Time)**: Calculate $t_{RC} = t_{RAS} + t_{RP}$ as the foundational repetitive cycle baseline.

### Step 3: Low-Level Command Sequence Implementation
1. **Row Activation / Read Command Sequence**:
   - Drive target row address onto the bus.
   - Assert $\overline{\text{RAS}}$ low, latching row address and triggering wordline activation of the $L = 180\text{ nm}$, $W = 220\text{ nm}$ access transistors.
   - Wait $t_{RCD}$ duration while charge dump $Q_s = C_s \cdot (V_{\text{cell}} - V_{BL})$ develops differential voltage $\Delta V$ on the bitline.
   - Drive target column address and assert $\overline{\text{CAS}}$ low with $\overline{\text{WE}}$ high to latch sense-amplifier output into $DQ$ buffer.
2. **Row Write Command Sequence**:
   - Apply row address and assert $\overline{\text{RAS}}$ low.
   - Wait $t_{RCD}$, assert data on $DQ$ pins, drive column address, and assert both $\overline{\text{CAS}}$ and $\overline{\text{WE}}$ low to overwrite cell capacitance to full $V_{DD}$ (logic 1) or $V_{SS}$ (logic 0).
3. **Precharge & Equalization Command Sequence**:
   - De-assert $\overline{\text{RAS}}$ high and wait minimum $t_{RP}$ to equalize folded bitline pairs back to $V_{DD} / 2$ via the equalization transistor network.

### Step 4: Distributed Auto-Refresh Timer Engine
1. Configure an ESP32 high-resolution hardware timer (`esp_timer`) to orchestrate distributed auto-refresh cycles.
2. Set cumulative refresh interval window to $\le 64\text{ ms}$ at $85^\circ\text{C}$ to combat cumulative sub-threshold and junction leakage currents targeting $\le 1.0\text{ fA/cell}$.
3. Schedule incremental row refresh bursts evenly across the $64\text{ ms}$ timeframe ($t_{REFI} = 64\text{ ms} / N_{\text{rows}}$) to avoid motor-control loop starvation.

---

## 4. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Acceptance Target Metric | Unit | Physical Context / Verification Condition |
| :--- | :--- | :--- | :--- |
| **Cell Capacitance Handled ($C_s$)** | $\ge 25.0 \text{ to } 28.0$ | $\text{fF}$ | Stacked crown/cylinder capacitor ($Ta_2O_5 / Al_2O_3$ or ONO stack, $\kappa > 15$, $\text{EOT} = 3\text{--}4\text{ nm}$) |
| **Bitline Parasitic Capacitance Limit ($C_{BL}$)** | $\le 250.0$ | $\text{fF}$ | Folded bitline array capacitance supported during signal development |
| **Differential Signal Window ($\Delta V$)** | $\ge 100.0 \text{ to } 150.0$ | $\text{mV}$ | Signal development window prior to sense amplifier latch strobe ($\Delta V = [C_s / (C_{BL} + C_s)] \cdot |V_{\text{cell}} - V_{DD}/2|$) |
| **Maximum Retention Refresh Window ($t_{REF}$)** | $\ge 64.0$ | $\text{ms}$ | Full array refresh interval window at $T = 85^\circ\text{C}$ with leakage $\le 1.0\text{ fA/cell}$ |

---

## 5. Citations & References
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Access transistor channel dimensions: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
  - Capacitance budget: Minimum $28\text{ fF/cell}$ ($\kappa > 15$, ONO or $Ta_2O_5 / Al_2O_3$ stack).
  - Sub-threshold and junction leakage target: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
  - Folded bitline precharge equalization to $V_{DD}/2$.
  - Charge dump relationship: $Q_s = C_s \cdot (V_{\text{cell}} - V_{BL})$.
  - Differential signal development: $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{\text{cell}} - V_{DD}/2)$ yielding $100\text{ mV}$ to $150\text{ mV}$ for $C_s = 25\text{ fF}$ and $C_{BL} = 250\text{ fF}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - Cell storage capacitance range: $25\text{ to } 30\text{ fF}$ per cell.
  - Data retention requirement: $> 64\text{ ms}$ at $85^\circ\text{C}$.
  - EOT: $3\text{ to } 4\text{ nm}$; Bitline/wordline pitch: $360\text{ nm to } 400\text{ nm}$.

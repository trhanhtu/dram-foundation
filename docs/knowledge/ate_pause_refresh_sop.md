# SOP: ATE Pause-Refresh Test Pattern & Thermal-Chamber Recipe Configuration

- **Date**: 2026-10-15
- **Technology Node**: 180nm CMOS DRAM (Open-Source DRAM Chip / DRAM Foundation VN)
- **Cell Architecture**: 1T1C Stacked Capacitor over Bitline (COB), 8F² / 6F² Folded Bitline Topology
- **Status**: Accepted

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) defines the execution recipe for automated test equipment (ATE) pause-refresh screening and fail-bit mapping across packaged 180nm DRAM chips inside a regulated thermal environmental chamber. The procedure screens for single-cell charge retention capability, storage capacitor degradation, and sub-threshold/junction leakage at high temperatures following dynamic HTOL stress.

---

## 2. ATE & Chamber Execution Workflow

```text
┌────────────────────────┐
│                        │
│   Step 1: Test Head    │
│        Docking         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Step 2: Thermal Soak  │
│          85C           │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Step 3: Pattern     │
│        Preload         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Step 4: Pause      │
│      Inhibit 64ms      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Step 5: Burst      │
│        Readout         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Step 6: Fail-Bit    │
│        Mapping         │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Device Docking & Pin Verification
1. Dock the packaged 180nm DRAM device (or wafer-level probe card) into the high-frequency ATE socket.
2. Verify pin continuity and contact impedance on wordline and bitline interfaces (designed for pitch $\approx 360\text{ nm}$ to $400\text{ nm}$).
3. Configure the access transistor channel operating bias conditions ($L = 180\text{ nm}$, $W = 220\text{ nm}$, gate dielectric physical thickness $t_{ox} \approx 3.5\text{ nm}$).

### Step 2: Thermal-Chamber Recipe Soak
1. Set the thermal environmental chamber recipe setpoint to **$85^\circ\text{C}$**.
2. Allow a thermal soak time of $\ge 15\text{ minutes}$ to achieve thermal equilibrium across the socket and silicon substrate.

### Step 3: Test Pattern Pre-load (Solid '1', Solid '0', and Checkerboard)
1. Issue an array-wide write sequence across all addresses using:
   - Pattern A: Solid '1' (charges storage nodes to evaluate dielectric and junction leakage to substrate).
   - Pattern B: Solid '0' (discharges storage nodes to evaluate sub-threshold pull-up / bitline disturbances).
   - Pattern C: Checkerboard / Physical inverse-checkerboard (evaluates bitline coupling and adjacent cell capacitive cross-talk).

### Step 4: Pause-Refresh Inhibit (Retention Interval Hold)
1. Inhibit all JEDEC standard auto-refresh (`REF`) and self-refresh cycles.
2. Program the ATE master clock sequencer to pause dynamic operations for an interval of:
   $$t_{\text{pause}} = 64\text{ ms}$$
3. Maintain steady-state supply voltages and thermal chamber temperature at $85^\circ\text{C}$ throughout the pause window.

### Step 5: Burst Readout & Real-Time Comparator Capture
1. Immediately upon expiration of $t_{\text{pause}} = 64\text{ ms}$, initiate high-speed burst read cycles across all wordline and bitline rows.
2. Strobe comparator channels against expected patterns to identify logic state flips ('1' $\to$ '0' or '0' $\to$ '1').

### Step 6: Fail-Bit Mapping & Spatial Clustering Analysis
1. Stream inverted bit addresses to the ATE fail-bit map (FBM) logger.
2. Classify bit failures into single-cell retention leaks (weak stacked capacitor / defective W-plug contact), wordline shorts, or bitline coupling defects.

---

## 4. Acceptance Criteria & Target Metrics

```text
                        Retention Screening Targets     
                   ┌───────────────────────────────────┐
                   │░░                                 │
 Leakage Limit (fA)┤░░                                 │
Retention Time (ms)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
                   │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
   Capacitance (fF)┤████████████████                   │
                   │████████████████                   │
                   └┬────────┬───────┬────────┬───────┬┘
                    0       16      32       48      64 
```

| Metric Parameter | Machine Target Value | Physical Unit | Measurement Condition |
| :--- | :--- | :--- | :--- |
| **Minimum Retention Time ($t_{\text{ret}}$)** | $\ge 64$ | $\text{ms}$ | At $85^\circ\text{C}$ chamber soak temperature |
| **Unit Storage Capacitance ($C_{\text{cell}}$)** | $\ge 25 \text{ to } 30$ (min. 28) | $\text{fF}$ | High-frequency C-V / Charge-sharing margin |
| **Cell Leakage Current ($I_{\text{leak}}$)** | $< 1.0$ | $\text{fA/cell}$ | Sub-threshold + junction leakage at $85^\circ\text{C}$ |
| **Access Gate Dielectric Physical Thickness ($t_{ox}$)** | $3.5 \pm 0.1$ | $\text{nm}$ | High-frequency C-V saturation extraction |

---

## 5. Literature References
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/knowledge/ate_pause_refresh_sop.md): Access transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$, stacked crown/MIM capacitor with minimum $28\text{ fF/cell}$ budget, leakage current $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/knowledge/ate_pause_refresh_sop.md): 1T1C $8\text{F}^2 / 6\text{F}^2$ architecture, storage capacitance $25\text{ to }30\text{ fF/cell}$, data retention time $> 64\text{ ms}$ at $85^\circ\text{C}$, gate oxide thickness $\approx 3.5\text{ nm}$, bitline/wordline pitch $360\text{ nm to } 400\text{ nm}$.
- [Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction](./docs/knowledge/ate_pause_refresh_sop.md): Oxide thickness $t_{ox}$ extraction precision $\pm 0.1\text{ nm}$ across accumulation region.

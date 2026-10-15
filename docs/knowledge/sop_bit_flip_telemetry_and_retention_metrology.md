# Standard Operating Procedure (SOP)
## Bit-Flip Error Telemetry Log Verification & Array Retention Boundary Metrology

**Document ID:** `SOP-MET-180NM-DRAM-001`  
**Node Generation:** Gen 2 (180 nm / 0.18 µm)  
**Process/Action Type:** Make / Metrology & Electrical Test  
**Module:** Metrology & Automated Shmoo Engine  

---

### 1. Process Overview & Objective
This procedure defines the test protocol for verifying bit-flip error telemetry logs and characterizing retention boundaries across an open-source 180nm 1T1C stacked-capacitor DRAM array (folded bitline architecture). It validates cell data retention margins under variable pause times and supply voltages ($V_{DD}$) using the ESP32 closed-loop test controller and March C- test sequence firmware.

```text
┌────────────────────────┐
│                        │
│    Initialize ESP32    │
│   March C- Sequence    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Execute Pause      │
│     Interval Step      │
│        t_pause         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Stream Telemetry &   │
│      Log Failures      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Compute Retention    │
│  Boundary & Shmoo Map  │
│                        │
└────────────────────────┘
```

---

### 2. Physical Design & Environmental Parameters
- **Access Transistor Channel:** Length $L = 180\text{ nm}$, Width $W = 220\text{ nm}$.
- **Gate Dielectric:** Thermally grown $\text{SiO}_2$ physical thickness $\sim 3.5\text{ nm}$ (dry oxidation at $850^\circ\text{C}\text{--}900^\circ\text{C}$).
- **Cell Architecture & Footprint:** 1T1C stacked capacitor over bitline (COB), $8F^2$ folded bitline topology (cell area $= 0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$).
- **Capacitor Structure & Dielectric:** Crown or Cylinder type stacked capacitor (polysilicon/MIM structure with W-plug drain contact); $\text{Si}_3\text{N}_4$, ONO, or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-$k$ stack ($\kappa > 15$, Equivalent Oxide Thickness $\text{EOT} \approx 3\text{ nm to } 4\text{ nm}$).
- **Interconnect Pitch:** Wordline and bitline pitch $= 360\text{ nm to } 400\text{ nm}$.
- **Array Size per BL:** 256 or 512 cells per bitline.
- **Operating Temperature:** Standard qualification baseline at $85^\circ\text{C}$.

---

### 3. Step-by-Step Metrology & Telemetry Verification Procedure

#### Step 1: Baseline Hardware & Environmental Setup
1. Mount the packaged 180nm DRAM DUT into the ESP32 test fixture interface.
2. Establish thermal chamber stability at $85^\circ\text{C} \pm 0.5^\circ\text{C}$.
3. Configure the programmable power supply rails: nominal $V_{DD}$ core, wordline boost rail $V_{PP}$, and bitline precharge voltage $V_{BLP} = V_{DD} / 2$.

#### Step 2: Telemetry Pipeline & Handshake Synchronization
1. Establish SPI/UART telemetry link between the DRAM test board and the host receiver at the designated telemetry baud rate.
2. Execute a hardware loopback self-test to verify UART packet framing, error-detection CRC integrity, and timestamp resolution ($< 1\ \mu\text{s}$).

#### Step 3: March C- Pattern Sequence Execution with Variable Pause
1. Program the ESP32 pattern register to execute March C- operations across all row/column addresses:
   - $\{\updownarrow (w0); \Uparrow (r0, w1); \Uparrow (r1, w0); \Downarrow (r0, w1); \Downarrow (r1, w0); \updownarrow (r0)\}$.
2. Insert a programmable retention delay interval ($t_{\text{pause}}$) between the write and read phases of the pattern.
3. Step $t_{\text{pause}}$ incrementally from $1\text{ ms}$ up to $256\text{ ms}$ in parametric intervals (e.g., $1\text{ ms}$, $10\text{ ms}$, $32\text{ ms}$, $64\text{ ms}$, $128\text{ ms}$, $256\text{ ms}$).

#### Step 4: Shmoo Grid Voltage Stepping & Bit-Flip Capture
1. Sweep $V_{DD}$ in discrete increments of $50\text{ mV}$ over the operational range across the retention time steps.
2. Capture bit-flip events: on every read mismatch ($r0 \ne 0$ or $r1 \ne 1$), the ESP32 telemetry engine logs `[Timestamp, Row_Addr, Col_Addr, Expected_Bit, Read_Bit, VDD, t_pause]`.
3. Ingest streaming telemetry into the automated Shmoo engine, generating pass/fail binary matrices across the $(V_{DD}, t_{\text{pause}})$ parameter plane.

#### Step 5: Boundary Extraction & Retention Derating Analysis
1. Define the retention boundary time ($t_{\text{ret\_boundary}}$) as the longest pause duration at which zero bit-flip errors occur across all tested addresses at $85^\circ\text{C}$.
2. Check for localized bit-line leakage clusters and single-cell retention anomalies against the sub-threshold leakage budget ($< 1\text{ fA/cell}$).

---

### 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value & Tolerance | Physical Unit | Measurement Condition |
| :--- | :--- | :--- | :--- |
| **Storage Node Capacitance ($C_s$)** | $\ge 25\text{ to } 30$ (nominal $28$) | $\text{fF/cell}$ | Stacked Crown/Cylinder capacitor metrology |
| **Bitline Parasitic Capacitance ($C_b$)** | $150 \text{ to } 250$ | $\text{fF}$ | Block array of 256 or 512 cells per bitline |
| **Capacitance Ratio ($C_b / C_s$)** | $5:1 \text{ to } 9:1$ ($< 10:1$) | Dimensionless | Folded bitline array read margin constraint |
| **Array Data Retention Time ($t_{\text{ret}}$)** | $> 64$ | $\text{ms}$ | At $T = 85^\circ\text{C}$, 0 bit errors under March C- |
| **Cell Leakage Current ($I_{\text{leak}}$)** | $< 1.0$ | $\text{fA/cell}$ | Junction & sub-threshold leakage at $85^\circ\text{C}$ |

```text
                    Array Metrology Parameters          
          ┌────────────────────────────────────────────┐
          │░░░░░░░░                                    │
  Ret Time┤░░░░░░░░                                    │
          │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
     Pitch┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
C_b Target┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    │
          │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    │
C_s Target┤████                                        │
          │████                                        │
          └┬──────────┬──────────┬─────────┬──────────┬┘
           0         95         190       285       380 
```

---

### 5. Verified Local Literature Citations
1. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - Transistor dimensions $L = 180\text{ nm}$, $W = 220\text{ nm}$.
   - Crown-shaped polysilicon or MIM stacked structure via tungsten plug (W-plug).
   - ONO triple dielectric or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-$k$ stack ($\kappa > 15$).
   - Storage capacitance minimum of $28\text{ fF/cell}$ and leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. **Source: 1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**
   - Folded bitline cell footprint $8F^2$ ($0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$).
   - Storage node capacitance $C_s \ge 25\text{ fF to } 30\text{ fF}$ per cell (nominally $28\text{ fF}$).
   - Bitline capacitance $C_b = 150\text{ fF to } 250\text{ fF}$ across 256/512 cells per bitline.
   - Capacitance ratio constraint $C_b / C_s$ maintained between $5:1$ and $9:1$ ($< 10:1$).
3. **Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**
   - Retention requirement $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Gate oxide physical thickness $\sim 3.5\text{ nm}$ grown at $850^\circ\text{C}\text{--}900^\circ\text{C}$ dry oxidation.
   - High-$k$ dielectric EOT around $3\text{ nm to } 4\text{ nm}$.
   - Bitline and wordline pitch $= 360\text{ nm to } 400\text{ nm}$.

# SOP: Hierarchical Row/Column Address Predecoder & Wordline Driver Sizing

- **Date**: 2026-10-13
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Node Classification**: Gen 2 (µm) / Leaf Node / Action: Make
- **Hierarchy Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > Address Decoders & Wordline VPP Voltage Pump [DRAM Circuit Design] > Hierarchical Row/Column Address Predecoder & Wordline Driver Sizing [Circuit Design]

---

## 1. Executive Summary & Circuit Architecture Scope

This Standard Operating Procedure (SOP) defines the circuit design and transistor sizing procedure for the hierarchical address predecoding network, level-shifting stages, and distributed sub-wordline drivers (SWD) for the 180nm open-source DRAM architecture. 

In 180nm DRAM cells, access NMOS transistors exhibit threshold voltages $V_{th} = 0.5\text{ V to } 0.6\text{ V}$ (up to $0.7\text{ V}$ under body effect). If driven solely by nominal core supply $V_{DD} = 1.8\text{ V}$, the maximum voltage written into the cell storage node capacitor ($C_s \ge 28\text{ fF}$) is limited to $V_{DD} - V_{th} = 1.2\text{ V}$, causing a 33% stored charge loss. To prevent retention degradation and maintain read sensing margin across bitline parasitic capacitances ($C_b = 150\text{ fF to } 250\text{ fF}$ with $C_b / C_s \le 9:1$), wordline drivers must be sized to operate at boosted high voltage $V_{PP} = 2.5\text{ V to } 2.8\text{ V}$ ($V_{DD} + V_{th} + \Delta V_{overdrive}$).

---

## 2. Structural Circuit Sizing Workflow

```text
┌────────────────────────┐
│                        │
│       1. Address       │
│    Predecoder Stage    │
│         Sizing         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  2. Level Shifter VDD  │
│         to VPP         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    3. Sub-Wordline     │
│   Driver SWD Sizing    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  4. Wordline Slew and  │
│    RC Verification     │
│                        │
└────────────────────────┘
```

---

## 3. Physical Cell & Array Design Budget Baseline

```text
                 Baseline Physical and Electrical Budget
                 ┌─────────────────────────────────────┐
                 │●                                    │
     VDD Core (V)┤●                                    │
                 │■                                    │
VPP Overdrive (V)┤■                                    │
                 │░░░░░░                               │
      Cs Nom (fF)┤░░░░░░                               │
  Cb/Cs Ratio Max┤▒▒                                   │
                 │▒▒                                   │
    Access L (nm)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       │
                 │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       │
    Access W (nm)┤█████████████████████████████████████│
                 │█████████████████████████████████████│
                 └┬────────┬────────┬────────┬────────┬┘
                  0       55       110      165     220 
```

---

## 4. Step-by-Step Circuit Sizing Procedure

### Step 1: Row/Column Address Predecoder Sizing ($V_{DD} = 1.8\text{ V}$ Core Domain)
1. **Tree Decomposition**: Partition incoming row address bits into 2-to-4 and 3-to-8 predecoded signal groups (e.g., $RA[0:1] \rightarrow PXR<0:3>$, $RA[2:4] \rightarrow PYR<0:7>$).
2. **Logic Gate Fan-out Optimization**:
   - Implement static CMOS NAND2/NAND3 predecoder logic sized to drive the long global predecode lines traversing the array periphery.
   - Set minimum gate length $L = 180\text{ nm}$ across all predecoder stages.
   - Size PMOS pull-up width $W_p = 2.0\text{ µm to } 3.6\text{ µm}$ and NMOS pull-down width $W_n = 1.2\text{ µm to } 2.4\text{ µm}$ maintaining an effective stage effort $h \approx 3.0 \text{ to } 3.6$.
3. **Column Predecoder Staging**: Match column predecoder sizing to column select lines ($CSL$), driving transfer gates with propagation delays matched within $\pm 0.2\text{ ns}$ of row activation phases.

### Step 2: High-Voltage Level Shifter Interfacing ($1.8\text{ V } V_{DD} \rightarrow 2.5\text{ V to } 2.8\text{ V } V_{PP}$)
1. **Topology Selection**: Implement a cross-coupled PMOS latch level shifter with dual NMOS pulldown legs.
2. **Breakdown & Gate Oxide Protection**:
   - Utilize thick-oxide or high-voltage extended-drain transistors rated for $> 3.3\text{ V}$ breakdown to handle the $V_{PP} = 2.5\text{ V to } 2.8\text{ V}$ rail without dielectric breakdown.
3. **Transistor Aspect Ratio Sizing**:
   - Set cross-coupled high-voltage PMOS latch transistors to $W/L = 1.5\text{ µm} / 0.35\text{ µm}$.
   - Size input pulldown NMOS devices driven by $1.8\text{ V}$ core signals to $W/L = 3.0\text{ µm} / 0.18\text{ µm}$ to ensure positive switching margin against high-voltage PMOS contention under worst-case corner conditions ($V_{DD,min} = 1.62\text{ V}$, $V_{PP,max} = 2.8\text{ V}$).

### Step 3: Sub-Wordline Driver (SWD) Sizing & Layout Pitch-Matching
1. **Hierarchical SWD Architecture**: Configure Main Wordline ($MWL$) and Sub-Wordline ($SWL$) hierarchy. Each $MWL$ enables a block of 4 or 8 sub-wordlines decoded via sub-wordline select signals ($FX / FXB$).
2. **Pitch-Matching to Array Grid**:
   - DRAM access transistor dimensions: Channel length $L = 180\text{ nm}$, channel width $W = 220\text{ nm}$ in an $8F^2$ folded bitline cell footprint ($0.259\text{ µm}^2$).
   - Distribute SWD drivers symmetrically across pitch boundaries to match the $2F$ wordline pitch ($360\text{ nm}$).
3. **SWD Output Transistor Dimensions**:
   - **Pull-up Device**: Sized to drive wordline to full $V_{PP} \ge 2.5\text{ V}$. PMOS/NMOS boost driver width $W_{pu} = 2.4\text{ µm to } 3.2\text{ µm}$ ($L = 0.35\text{ µm}$ high-voltage).
   - **Pull-down Device**: High-speed NMOS pulldown width $W_{pd} = 1.8\text{ µm to } 2.4\text{ µm}$ ($L = 180\text{ nm}$) to guarantee rapid wordline deactivation and prevent multi-row leakage conduction during precharge.
   - **Holding Transistor**: Auxiliary NMOS pulldown ($W = 0.5\text{ µm}$, $L = 180\text{ nm}$) to hold deactivated wordlines clamped to $V_{SS}$ against capacitive coupling noise from adjacent transitioning bitlines.

### Step 4: Wordline Capacitive Load & RC Delay Modeling
1. **Lumped Distributed RC Extraction**:
   - Wordline capacitive load includes gate capacitance of 256 or 512 access transistors ($W = 220\text{ nm}, L = 180\text{ nm}$) plus metal/polycide interconnect routing capacitance:
     $$C_{WL,total} = N_{cells} \cdot C_{gate} + C_{wire} \approx 256 \times (0.45\text{ fF}) + 65\text{ fF} \approx 180\text{ fF}$$
2. **Transient SPICE Simulation**: Run transient analysis simulating wordline activation from $0\text{ V}$ to $V_{PP} = 2.5\text{ V - } 2.8\text{ V}$ under nominal and slow PVT corners. Validate that the far-end wordline slew rate enables access transistor channel saturation within target $t_{RCD}$ windows.

---

## 5. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Specification | Exact Physical Units | Verification Method |
| :--- | :--- | :--- | :--- |
| **Wordline Boost Voltage ($V_{PP}$)** | $2.5 \le V_{PP} \le 2.8$ | $\text{V}$ | Transient SPICE / Post-layout Simulation |
| **Bitline-to-Cell Capacitance Ratio ($C_b / C_s$)** | $5.0 \le C_b / C_s \le 9.0$ ($C_s \ge 28\text{ fF}$, $C_b = 150 - 250\text{ fF}$) | Ratio (dimensionless) | Extracted Netlist Metrology / LVS |
| **Wordline Far-End Rise Time ($t_{rise, 10\%-90\%}$)** | $\le 2.2$ | $\text{ns}$ | Distributed RC SPICE transient analysis |
| **Access Transistor Channel Geometry** | $L = 180 \pm 5$, $W = 220 \pm 8$ | $\text{nm}$ | DRC / GDS Layout Metrology |

---

## 6. Literature & Context Citations

- **High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture**:
  - Validates NMOS access transistor threshold voltage loss ($V_{th} \sim 0.5\text{ V to } 0.7\text{ V}$) requiring overdrive high voltage $V_{PP} = V_{DD} + V_{th} + \Delta V_{overdrive} \ge 2.5\text{ V to } 2.8\text{ V}$ supplied by Dickson charge pump topology.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Establishes unit cell geometry for access transistor channel length $L = 180\text{ nm}$ and width $W = 220\text{ nm}$, stacked capacitor over bitline (COB) architecture, and minimum storage capacitance $C_s \ge 28\text{ fF}$ per cell.
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
  - Establishes folded bitline cell area ($8F^2 = 0.259\text{ µm}^2$ at $F = 180\text{ nm}$), storage node capacitance budget $C_s \ge 25\text{ fF to } 30\text{ fF}$ (nominal $28\text{ fF}$), array bitline parasitic capacitance $C_b = 150\text{ fF to } 250\text{ fF}$ (256/512 cells per bitline), and strict capacitance ratio limit $5:1 \le C_b / C_s \le 9:1$.

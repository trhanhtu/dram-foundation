# Standard Operating Procedure (SOP)
## 1T1C Storage Node Floating Check and Plate Voltage Bias Connectivity Verification

**Generation**: Gen 2 (180nm Open-Source DRAM Chip - DRAM Foundation VN)  
**Discipline**: Metrology / Physical Verification & LVS Equivalence  
**Target Unit**: 180nm 1T1C DRAM Cell Bitline & Wordline Matrix Hierarchy  
**Action Type**: Make  

---

### 1. Workflow Architecture & Verification Flow

The execution workflow verifies electrical continuity and topological isolation for both electrodes of the 1T1C stacked capacitor: the isolated Storage Node (SN) and the globally shared Top Plate ($V_{PL}$ / Plate Line).

```text
┌────────────────────────┐
│                        │
│    Layout GDSII and    │
│        Netlist         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   1T1C Connectivity    │
│         Trace          │
│                        │
└────────────┬───────────┘
             │
             ├─────────────────────────────╮
             ▼                             ▼
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
│      Storage Node      │    │   Plate Voltage VPL    │
│     Floating Check     │    │    Bias Mesh Trace     │
│                        │    │                        │
└───────────┬────────────┘    └────────────┬───────────┘
            │                              │
            │ ╭────────────────────────────╯
            ▼ ▼
┌────────────◇───────────┐
│                        │
│  Floating SN or Plate  │
│         Open?          │
│                        │
└────────────◇───────────┘
             │
             │
             ├─────────────────────────────╮No
          Yes│                             │
             ▼                             ▼
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
│  Flag LVS Error: Open  │    │   LVS Clean: Storage   │
│   SN or Disconnected   │    │  Node Continuous and   │
│          VPL           │    │       VPL Biased       │
│                        │    │                        │
└────────────────────────┘    └────────────────────────┘
```

---

### 2. Physical & Critical Dimension Parameters

Key geometric parameters extracted from physical verification rules:

```text
                180nm DRAM 1T1C Geometric Targets (nm)  
              ┌────────────────────────────────────────┐
              │■                                       │
EOT Dielectric┤■                                       │
              │░                                       │
      Gate Tox┤░                                       │
   WL/BL Pitch┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
              │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
      Access W┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                │
              │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                │
      Access L┤███████████████████                     │
              │███████████████████                     │
              └┬─────────┬─────────┬────────┬─────────┬┘
               0        95        190      285      380 
```

---

### 3. Step-by-Step Operating Procedure

#### Step 1: Pre-Execution Environment & Layer Definition Setup
1. Load the 180nm physical verification rule deck (`sky180` / custom 180nm DRAM open-source extension deck) into the LVS verification engine (Netgen / Magic / KLayout / Pegasus / Calibre).
2. Validate layer mapping definitions:
   - Access Transistor: Active/Diffusion (`DIFF`), Polysilicon Wordline (`POLY`), Contact (`CONT`).
   - Bitline: Metal1 / Tungsten Bitline (`BL`).
   - Storage Node Contact: Tungsten Plug (`W-plug` / `SNC`).
   - Capacitor Storage Node: Bottom Electrode (`SN_POLY` / `SN_METAL`).
   - Capacitor Dielectric: `CAP_DIEL` (ONO stack or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-$k$).
   - Plate Node: Top Plate Continuous Mesh (`PLATE` / Metal / Poly).

#### Step 2: Access Transistor to Storage Node Contact Continuity Trace
1. Perform extraction of the access transistor: channel length $L = 180\text{ nm}$ and width $W = 220\text{ nm}$.
2. Trace connectivity from the drain diffusion region of each 1T1C access transistor to the storage node contact plug (`W-plug`).
3. Verify via transition: Ensure that `W-plug` forms an uninterrupted ohmic contact with the crown-shaped or MIM storage bottom electrode.
4. Flag any dangling contacts or misaligned contacts where the overlap margin falls below design rule thresholds, resulting in open circuits.

#### Step 3: Storage Node Floating & Antenna Check (Isolation Verification)
1. **Topology Isolation Rule**: The Storage Node (`SN`) is strictly an internal memory node. It must connect to **exactly two terminals**:
   - Terminal 1: Drain of the access transistor ($W/L = 220\text{ nm} / 180\text{ nm}$).
   - Terminal 2: Bottom electrode of the storage capacitor ($C_s \ge 25\text{ fF}$).
2. Execute automated rule checking for floating storage nodes:
   - Identify nodes attached to a capacitor bottom electrode that fail to reach an active diffusion node (Unconnected/Floating SN).
   - Identify nodes where diffusion connects to a `W-plug` with no capacitor electrode extracted (Missing Capacitor).
   - Identify accidental cross-bridge shorts between storage nodes of adjacent memory cells along the wordline or bitline pitch ($360\text{ nm} - 400\text{ nm}$).
3. Verify that zero storage nodes are left electrically floating or unintentionally tied to substrate/ground.

#### Step 4: Plate Voltage ($V_{PL}$) Mesh & Connectivity Trace
1. Trace the common top plate layer (`PLATE`) across the entire memory array block.
2. In folded bitline stacked capacitor architectures (COB), the top plate forms a contiguous planar sheet covering all memory cells.
3. Trace continuity from the array top plate to the designated plate voltage generator pad / internal bias net ($V_{PL} = V_{DD}/2 = 0.9\text{ V}$ for $1.8\text{ V}$ nominal core).
4. Check for mesh fragmentation: Ensure no slots, slit etch borders, or routing blockages isolate any local capacitor top electrodes from the master plate power ring.
5. Report any isolated plate "islands" or high-resistance necking points.

#### Step 5: Post-Extraction Equivalence Report Generation
1. Compare the extracted netlist against the golden schematic netlist:
   - Validate 1:1 pairing of each 1T1C cell instance ($M_{access}$ and $C_{storage}$).
   - Confirm storage node net label equivalence.
   - Confirm common plate node binding across all cell instances to the schematic `VPL` net.
2. Generate the detailed LVS comparison report and error log.

---

### 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value / Tolerance | Physical Unit | Measurement Method | Reference Source |
| :--- | :--- | :--- | :--- | :--- |
| **Storage Node (SN) Floating Count** | **0** (Zero floating SN errors allowed across matrix) | Nodes / Violations | Automated LVS Graph Trace / Electrical Rule Check (ERC) | Netlist Comparison & 1T1C Node Connectivity Validation |
| **Storage Cell Capacitance ($C_s$)** | **25 to 30** (Minimum $\ge 25$, target $28$) | $\text{fF/cell}$ | Field solver / 3D Parasitic Extraction (PEX) | 180nm DRAM Cell Layout Topology; Legacy 180nm DRAM Architecture |
| **Top Plate ($V_{PL}$) Connectivity & Continuity** | **100%** (0 isolated plate islands; 0 open circuits to $V_{DD}/2$ bias net) | % / Open Nodes | Point-to-Point Resistance & LVS Net Equivalence Check | Folded Bitline Sense Amplifier Circuit Design |
| **Access Transistor Channel Geometry** | $L = 180 \pm 5$, $W = 220 \pm 5$ | $\text{nm}$ | Automated Optical / LVS Layout Parameter Extraction (LPE) | 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench |

---

### 5. Verified Literature Citations

1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry: Channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - Stacked capacitor topology: Crown-shaped polysilicon or metal-insulator-metal (MIM) structure erected above drain contact via tungsten plug (W-plug).
   - Dielectric: ONO triple dielectric or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-$k$ stack ($\kappa > 15$).
   - Capacitance budget: Minimum $28\text{ fF}$ per cell.
   - Leakage target: Sub-threshold and junction leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

2. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - Architecture: 1-Transistor 1-Capacitor (1T1C) architecture ($8F^2$ or $6F^2$).
   - Storage capacitance: $25\text{ to }30\text{ fF}$ per cell for retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Dielectrics: $\text{Si}_3\text{N}_4$ or $\text{Ta}_2\text{O}_5$ with Equivalent Oxide Thickness (EOT) of $3\text{ to }4\text{ nm}$.
   - Bitline and wordline pitch: $360\text{ nm to }400\text{ nm}$.
   - Gate dielectric: Thermally grown $\text{SiO}_2$ at $850^\circ\text{C} - 900^\circ\text{C}$ dry oxidation with $\sim 3.5\text{ nm}$ physical thickness.

3. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
   - Precharge operation: Bitlines equalized to $V_{DD} / 2$ prior to wordline assertion.
   - Signal development: $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{cell} - V_{DD}/2)$, yielding $100\text{ mV to }150\text{ mV}$ for $C_s = 25\text{ fF}$ and $C_{BL} = 250\text{ fF}$.
   - Plate bias verification: Plate node reference must remain stable at $V_{DD}/2$ to prevent cell dielectric stress.

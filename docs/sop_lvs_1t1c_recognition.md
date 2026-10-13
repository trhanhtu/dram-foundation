# Standard Operating Procedure (SOP)
## LVS Rule Deck Setup and 1T1C Primitive Device Recognition Definition

- **Node Generation**: 180nm Open-Source DRAM (Gen 2 - µm)
- **Hierarchy Path**: `[Architecture & Integration] > 180nm 1T1C DRAM Cell Bitline & Wordline Matrix Layout [Circuit Design] > DRC/LVS Verification & Parasitic Extraction for Bitline/Wordline Matrix [Metrology] > LVS Netlist Comparison & 1T1C Node Connectivity Validation [Metrology] > LVS Rule Deck Setup and 1T1C Primitive Device Recognition Definition [Metrology]`
- **Action Type**: Make
- **Status**: Released / Operational

---

### 1. Purpose & Scope
This Standard Operating Procedure (SOP) defines the operational workflow for configuring the Layout-Versus-Schematic (LVS) verification rule deck, declaring geometric Boolean layer derivations, and formulating extraction definitions for the 1-Transistor 1-Capacitor (1T1C) DRAM memory cell primitive devices (access MOSFET and stacked storage capacitor) in a 180nm process.

---

### 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│  GDSII / OASIS Layout  │
│         Input          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Boolean Layer      │
│      Derivations       │
│                        │
└────────────┬───────────┘
             │
             ├─────────────────────────────╮
             ▼                             ▼
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
│    Primitive Device    │    │    Primitive Device    │
│    Recognition: 1T     │    │    Recognition: 1C     │
│       Access FET       │    │      Storage Cap       │
│                        │    │                        │
└───────────┬────────────┘    └────────────┬───────────┘
            │                              │
            │ ╭────────────────────────────╯
            ▼ ▼
┌────────────────────────┐
│                        │
│       Electrical       │
│      Connectivity      │
│    Extraction & Pin    │
│        Mapping         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      LVS Netlist       │
│     Comparison vs      │
│     Schematic CDL      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  LVS Clean Report: 0   │
│      Discrepancy       │
│                        │
└────────────────────────┘
```

---

### 3. Step-by-Step Operating Procedure

1. **Rule Deck Environment Initialization & Layer Mapping**:
   - Ingest primary design layers from GDSII/OASIS (`ACTIVE`, `POLY_WL`, `NPLUS_IMPLANT`, `PPLUS_IMPLANT`, `CONT_W`, `METAL1_BL`, `CAP_BOTTOM_NODE`, `CAP_TOP_PLATE`, `SUBSTRATE`).
   - Define conductive connectivity and contact routing:
     - `CONNECT ACTIVE NPLUS_IMPLANT BY DIFF_CONT`
     - `CONNECT NPLUS_IMPLANT METAL1_BL BY CONT_W`
     - `CONNECT NPLUS_IMPLANT CAP_BOTTOM_NODE BY CONT_W`

2. **1T Access MOSFET Primitive Recognition**:
   - Derive the access channel via Boolean intersection:
     `DRAM_CHANNEL = (ACTIVE AND POLY_WL) AND NPLUS_IMPLANT`
   - Define source/drain diffusion regions:
     `DRAM_SD = (ACTIVE AND NPLUS_IMPLANT) NOT POLY_WL`
   - Formulate the 1T NMOS access primitive extraction statement:
     - Terminals: Gate (`POLY_WL`), Source (`DRAM_SD` connected to shared bitline contact), Drain (`DRAM_SD` connected to storage node plug), Bulk (`P_SUBSTRATE`).
     - Geometric extraction parameters: Nominal Channel Length $L = 180\text{ nm}$, Channel Width $W = 220\text{ nm}$.

3. **1C Stacked Storage Capacitor Primitive Recognition**:
   - Derive the capacitor active dielectric overlap area:
     `DRAM_CAP_AREA = CAP_BOTTOM_NODE AND CAP_TOP_PLATE`
   - Map terminal pins:
     - Positive terminal (`SN` / Storage Node): Connected to Access Transistor Drain diffusion via tungsten plug (`W-plug`).
     - Plate terminal (`CP` / Cell Plate): Connected to common cell plate biased to $V_{\text{plate}} = V_{\text{DD}} / 2$.
   - Formulate capacitor device statement:
     - Primitive name: `CAP_1T1C`
     - Terminal extraction: `SN`, `CP`
     - Capacitance extraction formula based on high-k dielectric stack (EOT = $3.0\text{ nm}$ to $4.0\text{ nm}$ or ONO/Ta2O5/Al2O3 equivalent).

4. **Connectivity Graph & Folded Bitline Topology Extraction**:
   - Map complementary folded bitline pairs (`BL` and `/BL`) routed on `METAL1_BL` to ensure proper pairing into the sense amplifier network.
   - Establish soft-check validation to confirm bitline contact is strictly shared between two adjacent 1T1C memory cells.

5. **LVS Netlist Comparison Execution**:
   - Execute layout extraction engine to generate extracted SPICE netlist.
   - Run comparison against reference schematic CDL netlist.
   - Inspect discrepancy tables: flag any open circuits, shorts, parameter mismatches (L/W tolerance $> 2\%$), or floating cell plate/storage nodes.

---

### 4. Acceptance Criteria & Target Metrics

```text
                ┌──────────────────────────────────────┐
                │░░░░                                  │
    Cell Cs (fF)┤░░░░                                  │
                │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
WL/BL Pitch (nm)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
   Access W (nm)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                │
                │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                │
   Access L (nm)┤███████████████████                   │
                │███████████████████                   │
                └┬────────┬─────────┬────────┬────────┬┘
                 0       95        190      285     380 
```

| Metric / Parameter | Target Value | Physical Unit | Tolerance / Limit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Access Transistor Channel Length ($L$)** | `180` | `nm` | $\pm 0$ (exact extraction grid) | LVS Primitive Parameter Comparison |
| **Access Transistor Channel Width ($W$)** | `220` | `nm` | $\pm 0$ (exact extraction grid) | LVS Primitive Parameter Comparison |
| **Bitline & Wordline Pitch** | `360 to 400` | `nm` | $[360, 400]\text{ nm}$ | DRC / LVS Spatial Pitch Gauge |
| **Storage Cell Capacitance ($C_s$)** | `25 to 30` (min `28`) | `fF` | $\ge 25\text{ fF}$ (min $28\text{ fF}$ target) | LVS / Parasitic Extraction Netlist |
| **LVS Netlist Discrepancies** | `0` | `count` | $0$ (Unmatched nets, instances, or ports) | LVS Run Comparison Report |

---

### 5. Context Literature Citations
1. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - Access transistor channel dimensions: Channel Length $L = 180\text{ nm}$, Width $W = 220\text{ nm}$.
   - Shared bitline contact topology between two adjacent memory cells.
   - Stacked capacitor over bitline (COB) architecture erected above drain contact via tungsten plug (`W-plug`).
   - Storage capacitance minimum budget of $28\text{ fF}$ per cell (dielectric constant $\kappa > 15$, sub-threshold & junction leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$).
2. **Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**
   - 1T1C storage capacitor target: $25\text{ to }30\text{ fF}$ maintaining retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Stacked capacitor dielectric equivalent oxide thickness (EOT): $3\text{ to }4\text{ nm}$.
   - Bitline and wordline pitch: $360\text{ nm to }400\text{ nm}$.
   - Gate dielectric physical thickness: $\sim 3.5\text{ nm}$ grown at $850^\circ\text{C} - 900^\circ\text{C}$.
3. **Source: Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**
   - Folded bitline topology with complementary bitlines `BL` and `/BL` precharged to $V_{\text{DD}} / 2$.
   - Signal development: Typical cell capacitance $C_s = 25\text{ fF}$ and bitline capacitance $C_{\text{BL}} = 250\text{ fF}$, delivering differential read signal $\Delta V \approx 100\text{ mV to }150\text{ mV}$.

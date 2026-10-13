# Standard Operating Procedure (SOP)
## Hierarchical Netlist Extraction and Layout-Versus-Schematic (LVS) Equivalence Run
**Generation**: Gen 2 (180nm Open-Source DRAM Chip - DRAM Foundation VN)  
**Discipline**: Metrology / Physical Verification & Circuit Equivalence  
**Target Unit**: 1T1C DRAM Bitline & Wordline Matrix Hierarchy  

---

### 1. Workflow Architecture & Execution Flow

```text
┌────────────────────────┐
│                        │
│     GDSII / OASIS      │
│    Physical Layout     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Hierarchical Device   │
│    & Pin Extraction    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Schematic SPICE     │
│  Netlist Flattening /  │
│     Preprocessing      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Subcircuit & Array   │
│     Symmetry Graph     │
│        Matching        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  LVS Parameter & Node  │
│      Equivalence       │
│       Validation       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────◇───────────┐
│                        │
│      Mismatch or       │
│      Discrepancy?      │
│                        │
└────────────◇───────────┘
             │
             │
             ├─────────────────────────────╮No
          Yes│                             │
             ▼                             ▼
┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │
│  Pin / Net / Property  │    │    1T1C Matrix LVS     │
│   Discrepancy Report   │    │     Clean Sign-Off     │
│                        │    │                        │
└────────────────────────┘    └────────────────────────┘
```

---

### 2. Physical & Metric Extraction Target Distribution

```text
              ┌────────────────────────────────────────┐
              │■■■■■■■■■■■■■■■■■■■■■■■■■■■■■           │
    L Nom (nm)┤■■■■■■■■■■■■■■■■■■■■■■■■■■■■■           │
              │███████████████████████████████████     │
    W Nom (nm)┤███████████████████████████████████     │
   BL Cap (fF)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
              │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
Cs Budget (fF)┤▒▒▒▒▒                                   │
              │▒▒▒▒▒                                   │
   Cs Min (fF)┤░░░░░                                   │
              │░░░░░                                   │
              └┬─────────┬─────────┬────────┬─────────┬┘
              0.0      62.5      125.0    187.5   250.0 
```

---

### 3. Step-by-Step Procedure

1. **Environment Setup & Rule Deck Configuration**:
   - Initialize the hierarchical verification tool deck with 180nm CMOS/DRAM tech layers.
   - Configure recognition layer operations for stacked capacitor over bitline (COB), tungsten plug (W-plug) contacts, access transistor active regions, gate oxide, and complementary bitline metal layers.

2. **Hierarchical Netlist Extraction (Layout to Extracted Netlist)**:
   - Extract primitive devices from physical geometries:
     - 1T Access Transistors: Recognize poly gate crossing active diffusion, measuring channel length ($L = 180\text{ nm}$) and channel width ($W = 220\text{ nm}$).
     - 1C Stacked Capacitors: Extract crown/cylinder capacitor nodes over tungsten plugs; map high-$k$ dielectric surface areas to extracted cell capacitance $C_s$.
     - Bitline & Wordline Matrix: Extract connectivity preserving shared contact architectures between adjacent paired memory cells.
   - Retain subcircuit modular hierarchy (`X_CELL_1T1C`, `X_BL_SENSE_AMP`, `X_MAT_ARRAY`) to prevent tool memory exhaustion during array graph matching.

3. **Schematic Netlist Preprocessing & Normalization**:
   - Parse schematic SPICE netlist representing folded-bitline DRAM architecture with complementary pairs (`BL`, `/BL`) and shared bitline contact ports.
   - Filter parasitic dummy devices and annotate tolerance bounds for extracted geometric parameters.

4. **Isomorphism & Graph Equivalence Run**:
   - Execute topological bipartite graph matching comparing layout pins/nodes against schematic ports.
   - Resolve matrix symmetry ambiguities by auto-pinning array boundary terminations and precharge equalization lines.

5. **Electrical Parameter & Property Verification**:
   - Validate extracted access transistor dimensions ($W, L$) against schematic properties within defined tool tolerances ($\le \pm 2\%$).
   - Verify extracted storage capacitor node capacitance against nominal budget ($C_s \ge 25\text{ fF}$ to $28\text{ fF}$).

6. **Error Analysis, Discrepancy Reporting & Sign-off**:
   - Generate summary report confirming zero shorts, zero opens, zero pin mismatches, and zero property discrepancies across the entire bitline/wordline matrix.

---

### 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Tolerance / Limit | Exact Physical Unit |
| :--- | :--- | :--- | :--- |
| **Access Transistor Gate Length ($L$)** | `180` | $\pm 0.0$ (CAD snap / grid exact) | $\text{nm}$ |
| **Access Transistor Channel Width ($W$)** | `220` | $\pm 0.0$ (CAD snap / grid exact) | $\text{nm}$ |
| **Storage Node Extracted Cell Capacitance ($C_s$)** | `28.0` | $\ge 25.0$ | $\text{fF}$ |
| **LVS Netlist Comparison Discrepancies** | `0` | $0$ (Unmatched nets, ports, instances) | $\text{count / error}$ |
| **Equivalent Oxide Thickness (EOT) Property** | `3.5` | $3.0\text{ to }4.0$ | $\text{nm}$ |

---

### 5. Literature References
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**: Differential sensing signals, precharge equalization, cell capacitance budget $C_s = 25\text{ fF}$, and bitline capacitance $C_{BL} = 250\text{ fF}$.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry with $L = 180\text{ nm}$, $W = 220\text{ nm}$, stacked capacitor over bitline (COB) architecture via tungsten plug (W-plug), and minimum $C_s = 28\text{ fF}$ budget.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: 1T1C folded bitline cell layout ($8F^2/6F^2$), cell storage capacitance requirement of $25\text{ to }30\text{ fF}$, EOT of $3\text{ to }4\text{ nm}$, and gate dielectric thickness of $\sim 3.5\text{ nm}$.

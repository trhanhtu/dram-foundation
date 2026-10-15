# Standard Operating Procedure (SOP): Process Parameter Benchmarking for Full-Chip Physical Sign-Off DRC, LVS, and Metal Density Fill Verification

- **Document ID**: `SOP-DRAM-SGN-180-001`
- **Revision**: `v1.0.0`
- **Node / Generation**: `180nm CMOS DRAM (Gen 3)`
- **Council**: DRAM Foundation VN Multi-Agent Council
- **Domain**: Metrology & Process Engineering / Physical Sign-Off

---

## 1. Scope & Objective
Establish a formal, industrial-grade sign-off procedure for benchmarking full-chip physical parameters (Design Rule Checking [DRC], Layout Versus Schematic [LVS], and CMP Metal Density Fill) for the 180nm Open-Source DRAM tapeout package (Core array, periphery, and seal ring integration).

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│  Stream-In GDSII and   │
│       Seal Ring        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  DRC and Pitch Checks  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     LVS and Device     │
│       Extraction       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Metal Density Fill   │
│         Check          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Foundry Sign-Off    │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Execution Procedure

### Step 1: Full-Chip GDSII Stream-In & Seal Ring Boundary Verification
- Stream in the merged top-level layout GDSII incorporating the 180nm DRAM core macro, sense amplifier banks, wordline drivers, address decoders, periphery I/O pads, and peripheral scribe/seal ring structures.
- Confirm boundary enclosure and seal ring continuity across all metallization layers without notch or gap violations.

### Step 2: Critical Physical DRC & Lithography Pitch Benchmarking
- Execute foundry-calibrated physical DRC rule decks on the entire hierarchy.
- **Access Transistor Dimension Verification**: Verify access NMOS gate channel length $L = 180\text{ nm}$ and gate channel width $W = 220\text{ nm}$.
- **Cell Pitch Verification**: Benchmark wordline (WL) and bitline (BL) pitches against the physical lithography limit of $360\text{ nm}$ to $400\text{ nm}$.
- **Array Footprint Verification**: Validate unit cell bounding box compliance with the $8F^2$ folded bitline topology ($0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$) or $6F^2$ open bitline topology ($0.194\ \mu\text{m}^2$).

### Step 3: LVS Extraction & Cell Device Parameter Benchmarking
- Extract the layout netlist using foundry LVS rule decks incorporating parasitic resistance and capacitance (PEX/RC extraction).
- **Capacitance Extraction ($C_s$ and $C_b$)**:
  - Extract stacked capacitor storage node capacitance $C_s$ per cell (Crown/Cylinder MIM or polysilicon with Si3N4, Ta2O5, or ONO stack).
  - Extract parasitic bitline capacitance $C_b$ for the standard array sub-block (256 or 512 cells per bitline).
- **Capacitance Ratio Benchmarking**: Benchmark $C_b / C_s$ ratio against the read margin requirement ($5:1$ to $9:1$, strictly below $10:1$).
- **Leakage Extraction**: Correlate junction and sub-threshold leakage target ($\le 1\text{ fA/cell}$ at $85^\circ\text{C}$).

### Step 4: CMP Dummy Metal Fill & Density Window Verification
- Run automated dummy metal fill routines across all interconnect layers (Metal 1 through Top Metal) to ensure post-CMP planarity.
- Verify metal density windows across stepping bounding boxes against foundry minimum and maximum density rules.
- Confirm that dummy metal fill maintains minimum required clearance away from active storage nodes, bitline contacts, and high-impedance sense amplifier nodes to prevent parasitic coupling spikes.

### Step 5: Final Sign-Off Clean Reporting
- Compile machine-generated DRC, LVS, and CMP density reports. Ensure clean status (`0 violations`) prior to tapeout shuttle stream-out.

---

## 4. Machine-Measurable Acceptance Criteria

```text
             Key Physical Sign-Off Benchmarks (fF / nm) 
             ┌─────────────────────────────────────────┐
             │░░░░░░░░░░░░░░░░░░░░                     │
L_gate Target┤░░░░░░░░░░░░░░░░░░░░                     │
             │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
 Pitch Target┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
   C_b Target┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   │
             │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   │
   C_s Target┤████                                     │
             │████                                     │
             └┬─────────┬─────────┬─────────┬─────────┬┘
              0        95        190       285      380 
```

| Metric / Parameter | Sign-Off Target Value / Range | Exact Physical Unit | Verification Stage |
| :--- | :--- | :--- | :--- |
| **Storage Node Capacitance ($C_s$)** | $25.0 \le C_s \le 30.0$ (Nominal: $28.0$) | $\text{fF/cell}$ | LVS / PEX Sign-Off |
| **Parasitic Bitline Capacitance ($C_b$)** | $150.0 \le C_b \le 250.0$ (for 256/512 cell array blocks) | $\text{fF}$ | LVS / PEX Sign-Off |
| **Capacitance Ratio ($C_b / C_s$)** | $5.0 : 1 \le C_b / C_s \le 9.0 : 1$ (Maximum threshold: $< 10.0 : 1$) | Unitless ratio | LVS / Margin Analysis |
| **Access Transistor Channel Geometry** | Length $L = 180$, Width $W = 220$ | $\text{nm}$ | Physical DRC Sign-Off |
| **Bitline & Wordline Lithographic Pitch** | $360.0 \le \text{Pitch} \le 400.0$ | $\text{nm}$ | Physical DRC Sign-Off |
| **Sub-threshold & Junction Cell Leakage** | $\le 1.0$ (at $85^\circ\text{C}$ for $> 64\text{ ms}$ retention) | $\text{fA/cell}$ | Device Characterization |

---

## 5. Literature Sources Cited
1. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - $8F^2$ folded bitline footprint ($0.259\ \mu\text{m}^2$) and $6F^2$ open bitline footprint ($0.194\ \mu\text{m}^2$ at $F = 180\text{ nm}$).
   - $C_s \ge 25\text{ fF}$ to $30\text{ fF/cell}$ (nominal $28\text{ fF}$).
   - $C_b = 150\text{ fF}$ to $250\text{ fF}$ (256/512 cells/BL).
   - $C_b / C_s$ ratio between $5:1$ and $9:1$, threshold $< 10:1$.
2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
   - Crown/cylinder stacked capacitor over bitline (COB) with ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-k stack ($\kappa > 15$).
   - Storage capacitance minimum $28\text{ fF/cell}$.
   - Leakage current target $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$.
3. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - Data retention time $> 64\text{ ms}$ at $85^\circ\text{C}$ with $C_s = 25$ to $30\text{ fF}$.
   - Wordline and bitline pitch: $360\text{ nm}$ to $400\text{ nm}$.
   - Dielectric EOT: $3$ to $4\text{ nm}$ ($\text{Si}_3\text{N}_4$ / $\text{Ta}_2\text{O}_5$), gate oxide $\text{SiO}_2$ physical thickness $\sim 3.5\text{ nm}$.

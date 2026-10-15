# Standard Operating Procedure (SOP)
## Quality Acceptance & Metrology Protocol for Full-Chip Physical Sign-Off DRC, LVS, and Metal Density Fill Verification

- **Document ID**: SOP-QA-180DRAM-DRC-LVS-001
- **Process Generation**: 180nm Open-Source DRAM (Gen 3)
- **Hierarchy Path**: Top-Level DRAM Core & Periphery GDSII Stream-Out and Seal Ring Integration > Full-Chip Physical Sign-Off DRC, LVS, and Metal Density Fill Verification > Quality Acceptance & Metrology Protocol

---

### 1. Purpose & Scope
This protocol governs the physical sign-off quality acceptance and metrology verification for the full-chip 180nm DRAM tapeout package. It specifies exact dimensional checks, device extraction rules, and metal fill planarization requirements across the DRAM core (8F² / 6F² folded bitline array blocks), periphery CMOS logic, pad ring, and foundry seal ring boundary.

---

### 2. Physical Sign-Off Workflow

```text
┌───────────────────────┐
│   GDSII Stream-In &   │
│       Seal Ring       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│     Full-Chip DRC     │
│     Verification      │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   LVS Extraction &    │
│    Netlist Compare    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Dummy Metal Fill &   │
│     Density Check     │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Sign-Off Acceptance  │
│       Approval        │
└───────────────────────┘
```

---

### 3. Step-by-Step Execution Procedure

1. **GDSII Stream-In & Chip Boundary Validation**:
   - Stream in the finalized full-chip GDSII hierarchy comprising the DRAM core, periphery sense amplifiers/decoders, I/O pads, and chip seal ring.
   - Confirm cell boundary, alignment of shared bitline contacts between adjacent 1T1C cells, and seal ring continuity around the perimeter.

2. **Full-Chip Design Rule Checking (DRC)**:
   - Run hierarchical DRC deck validating base layers:
     - Access NMOS gate channel length: $L = 180\text{ nm}$ nominal.
     - Access NMOS transistor width: $W = 220\text{ nm}$.
     - Gate oxide dielectric thickness: $t_{ox} = 3.5\text{ nm}$ (thermally grown $\text{SiO}_2$ dry oxidation at $850^\circ\text{C}\text{--}900^\circ\text{C}$).
     - Bitline and wordline wiring pitch: $360\text{ nm to } 400\text{ nm}$.
     - Unit cell area constraints: $\le 0.259\ \mu\text{m}^2$ for $8F^2$ folded bitline layout (or $0.194\ \mu\text{m}^2$ for $6F^2$).
   - Verify design rules for capacitor over bitline (COB) stacked capacitor layers (Crown/Cylinder polysilicon or MIM structures over tungsten plug).

3. **Layout Versus Schematic (LVS) & Device Extraction**:
   - Perform layout extraction with parasitic capacitance and resistance extraction enabled.
   - Match schematic pins, hierarchy, and 1T1C storage cell arrays against extracted connectivity.
   - Extract storage node capacitance $C_s$ and bitline total capacitance $C_b$ for array blocks (256 or 512 cells per bitline).
   - Ensure soft-error and leakage margin limits: access transistor sub-threshold and junction leakage target $\le 1\text{ fA/cell at } 85^\circ\text{C}$ to maintain refresh retention intervals $> 64\text{ ms}$.

4. **Automated Dummy Metal Density Fill & CMP Verification**:
   - Run automated fill generation for intermediate and top metal interconnect layers.
   - Validate global and local windowed metal density rules across the core array, periphery CMOS, and seal ring transitions to prevent dishing or erosion during Chemical Mechanical Planarization (CMP).
   - Re-run sign-off DRC and LVS checks post-fill to ensure dummy metal blocks introduce zero layout-vs-schematic shorts, zero opens, and zero DRC spacing violations.

5. **Sign-Off Metrology Sign-Off Review**:
   - Export physical verification sign-off summary report. All DRC and LVS violations must show zero errors before GDSII tapeout freeze.

---

### 4. Machine-Measurable Acceptance Criteria

```text
               ┌───────────────────────────────────────┐
               │░                                      │
   Gate Ox (nm)┤░                                      │
               │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
 W/L Pitch (nm)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
 EOT Limit (nm)┤▓                                      │
               │▓                                      │
C_s Target (fF)┤████                                   │
               │████                                   │
               └┬─────────┬────────┬─────────┬────────┬┘
                0        95       190       285     380 
```

| Parameter / Metrology Target | Acceptance Metric Target Value | Unit | Verification Method |
| :--- | :--- | :--- | :--- |
| **Cell Storage Capacitance ($C_s$)** | $\ge 25\text{ to } 30$ (Nominal: $28$) | $\text{fF}$ | LVS / Parasitic Extraction Deck |
| **Capacitance Ratio ($C_b / C_s$)** | $5:1\text{ to } 9:1$ (Strict Max: $< 10:1$) | Dimensionless | 256/512-cell Bitline Net Extraction |
| **Bitline & Wordline Pitch** | $360\text{ to } 400$ | $\text{nm}$ | Physical Sign-Off DRC Spacing/Pitch Check |
| **Dielectric EOT (Capacitor Stack)** | $3.0\text{ to } 4.0$ ($\kappa > 15$, ONO / $\text{Ta}_2\text{O}_5$ / $\text{Al}_2\text{O}_3$) | $\text{nm}$ | Stacked Capacitor Metrology & LVS Parameter Check |
| **Access Transistor Gate Geometry** | Length $L = 180$, Width $W = 220$; $t_{ox} = 3.5$ | $\text{nm}$ | Sign-Off DRC / LVS Extraction |
| **Full-Chip DRC / LVS Violation Count** | $0$ errors, $0$ unapproved waivers | Count | Automated Sign-Off Tool Exit Code |

---

### 5. Context Literature Citations
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$), shared bitline contact, stacked capacitor over bitline (COB) crown/MIM topology with W-plug, ONO/$\text{Ta}_2\text{O}_5$/$\text{Al}_2\text{O}_3$ dielectric ($\kappa > 15$), minimum capacitance budget $\ge 28\text{ fF}$, leakage current target $\le 1\text{ fA/cell at } 85^\circ\text{C}$.
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**: $8F^2$ folded bitline footprint ($0.259\ \mu\text{m}^2$) and $6F^2$ footprint ($0.194\ \mu\text{m}^2$); storage capacitance budget $C_s \ge 25\text{ to } 30\text{ fF}$; bitline parasitic capacitance $C_b = 150\text{ to } 250\text{ fF}$ across 256/512 cells; capacitance ratio $C_b / C_s$ window of $5:1\text{ to } 9:1$ (hard degradation above $10:1$).
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: Stacked capacitor equivalent oxide thickness (EOT) of $3\text{ to } 4\text{ nm}$; retention interval $> 64\text{ ms at } 85^\circ\text{C}$; bitline/wordline pitch of $360\text{ nm to } 400\text{ nm}$; thermally grown dry $\text{SiO}_2$ gate dielectric of $3.5\text{ nm}$.

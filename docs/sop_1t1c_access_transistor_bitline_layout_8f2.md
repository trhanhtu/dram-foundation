# Standard Operating Procedure (SOP)
## 1T1C Access Transistor & Bitline Contact Layout DRC/LVS Design (8F²)

- **Module**: DRAM Architecture & Circuit Design
- **Technology Node**: 180 nm Open-Source CMOS DRAM (Gen 2 µm)
- **Cell Architecture**: 1T1C Folded Bitline Stacked Capacitor over Bitline (COB)
- **Target Cell Area**: $8F^2 = 8 \times (0.180\,\mu\text{m})^2 = 0.259\,\mu\text{m}^2$

---

### 1. Step-by-Step Layout DRC/LVS Procedure

#### Step 1: Active Area (OD/RX) Definition & Unit Cell Boundary
- Draw active area diffusion islands along the bitline axis.
- Configure access transistor active channel width $W = 220\,\text{nm}$.
- Define unit cell boundary pitch along wordline and bitline directions to match $2F \times 4F = 360\,\text{nm} \times 720\,\text{nm}$ (total area $0.259\,\mu\text{m}^2$ for folded bitline $8F^2$).

#### Step 2: Gate Polysilicon (PC) Wordline Routing & Gate Oxide Definition
- Pattern poly wordlines crossing the active channel perpendicularly.
- Set physical gate channel length $L = 180\,\text{nm}$.
- Maintain wordline pitch within $360\,\text{nm}$ to $400\,\text{nm}$ ($2F$ pitch spacing).
- Associate physical gate dielectric stack corresponding to thermally grown $\text{SiO}_2$ at $850^\circ\text{C}\text{--}900^\circ\text{C}$ dry oxidation with $\sim 3.5\,\text{nm}$ physical thickness.

#### Step 3: Shared Bitline Contact (BLC) & Storage Node Contact (SNC) Placement
- Construct a shared bitline contact (BLC) centrally between two adjacent access transistors to optimize silicon density in the $8F^2$ pair.
- Implement contact plug using tungsten metallization (W-plug).
- Route the bitline metal pitch at $360\,\text{nm}$ to $400\,\text{nm}$.
- Position the storage node contacts (SNC / W-plug) at the opposing source/drain junctions for subsequent stacked capacitor over bitline (COB) connection.

#### Step 4: Storage Node Capacitor Landing Pad & Dielectric Definition
- Route landing pads for stacked capacitor structure (Crown or Cylinder polysilicon/MIM) over bitline.
- Dielectric model targets ONO triple layer or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-k stack ($\kappa > 15$, EOT $\sim 3\text{--}4\,\text{nm}$).
- Ensure physical geometry yields minimum target storage capacitance $C_s \ge 28\,\text{fF}$.

#### Step 5: DRC & LVS Clean Sign-Off Execution
- Execute Design Rule Checking (DRC) targeting minimum spacing and width rules:
  - Gate Length $L = 180\,\text{nm}$
  - Active Width $W = 220\,\text{nm}$
  - Wordline and Bitline pitch within $360\,\text{nm} \text{--} 400\,\text{nm}$
- Perform Layout Versus Schematic (LVS) extracting:
  - 1T NMOS transistor matching schematic ($W=220\,\text{nm}, L=180\,\text{nm}$)
  - Shared bitline node connectivity
  - Storage node capacitance matching $C_s \ge 28\,\text{fF}$ per cell

---

### 2. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Units | Tolerance / Boundary | Measurable Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Unit Cell Silicon Area** | `0.259` | $\mu\text{m}^2$ | Max allowable ($8F^2$ at $F = 180\,\text{nm}$) | GDSII Unit Cell Boundary DRC Check |
| **Access Transistor Channel Geometry** | $L = 180$, $W = 220$ | $\text{nm}$ | Exact nominal target ($\pm 0\,\text{nm}$ grid) | Automated DRC / LVS Parameter Extraction |
| **Wordline & Bitline Pitch** | `360 to 400` | $\text{nm}$ | Range ($2F$ pitch minimum $360\,\text{nm}$) | DRC Pitch Rule Verification |
| **Storage Node Capacitance ($C_s$)** | $\ge 28.0$ | $\text{fF/cell}$ | Minimum limit ($25\text{--}30\,\text{fF}$ budget) | Post-Layout PEX Extraction / LVS Check |
| **Cell Leakage Current (@ 85°C)** | $\le 1.0$ | $\text{fA/cell}$ | Max limit (sub-threshold + junction) | SPICE Corner Simulation on Extracted Netlist |

---

### 3. Citations & References
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*: Access transistor $L = 180\,\text{nm}$, $W = 220\,\text{nm}$; shared bitline contact; tungsten plug (W-plug); stacked crown/MIM capacitor; high-k $\kappa > 15$; $C_s \ge 28\,\text{fF/cell}$; cell leakage $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$.
- *1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*: Folded bitline $8F^2$ footprint ($0.259\,\mu\text{m}^2$ at $F = 180\,\text{nm}$); $C_s \ge 25\text{--}30\,\text{fF}$ per cell (nominally $28\,\text{fF}$); $C_b/C_s$ ratio between $5:1$ and $9:1$.
- *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*: Bitline and wordline pitch $360\,\text{nm} \text{--} 400\,\text{nm}$; gate oxide physical thickness $\sim 3.5\,\text{nm}$ ($850^\circ\text{C}\text{--}900^\circ\text{C}$ dry oxidation); EOT $3\text{--}4\,\text{nm}$.

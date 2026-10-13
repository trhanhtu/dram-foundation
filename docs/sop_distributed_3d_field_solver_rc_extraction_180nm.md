# Standard Operating Procedure (SOP)
## Distributed 3D Field Solver RC Extraction for Folded Bitline and Poly/Silicide Wordline Array

- **Document ID:** SOP-DRAM-180NM-RC-EXTRACT-001
- **Node / Generation:** Gen 2 (180 nm / 0.18 µm)
- **Action Type:** Make
- **Context:** 180nm Open-Source DRAM Chip (DRAM Foundation VN) > 180nm 1T1C DRAM Cell Bitline & Wordline Matrix Layout > DRC/LVS Verification & Parasitic Extraction for Bitline/Wordline Matrix > PEX Extraction & Wordline/Bitline Parasitic RC Modeling > Distributed 3D Field Solver RC Extraction for Folded Bitline and Poly/Silicide Wordline Array

---

### 1. Purpose & Scope
This SOP defines the distributed 3D electrostatic and electro-quasistatic field solver procedure for rigorous parasitic resistance-capacitance ($RC$) extraction of 180 nm 1T1C folded bitline ($BL$/$\overline{BL}$) matrices and polycide/silicide wordlines ($WL$). It addresses intra-cell/inter-cell capacitive coupling across stacked capacitor over bitline (COB) structures, tungsten contact plugs ($W$-plugs), and dense periodic arrays.

---

### 2. Verified Literature Citations & Physical Baselines
All physical dimensions, capacitance budgets, and electrical thresholds directly derive from verified 180 nm local literature:
- **[180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench]**:
  - Access transistor channel dimensions: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
  - Storage capacitor budget: $C_s \ge 28\text{ fF/cell}$ (Crown/MIM capacitor with high-$k$ stack $\kappa > 15$).
  - Target leakage budget: Sub-threshold and junction leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
  - Shared bitline contact via tungsten plug ($W$-plug) between adjacent memory cells in $8F^2 / 6F^2$ topology.
- **[Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout]**:
  - Nominal total bitline parasitic capacitance budget: $C_{BL} \approx 250\text{ fF}$.
  - Signal development: $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right) \approx 100\text{ mV to } 150\text{ mV}$ (for $C_s = 25\text{ fF}$, $C_{BL} = 250\text{ fF}$).
- **[Legacy 180nm DRAM Architecture & Cell Capacitor Engineering]**:
  - Array pitch: Bitline and wordline pitch = $360\text{ nm to } 400\text{ nm}$.
  - Gate dielectric: Thermally grown $\text{SiO}_2$ ($3.5\text{ nm}$ physical thickness, dry oxidation at $850^\circ\text{C}\text{--}900^\circ\text{C}$).
  - Storage node retention baseline: Retention time $> 64\text{ ms}$ at $85^\circ\text{C}$ with $C_s = 25\text{ to } 30\text{ fF}$.

---

### 3. Procedural Execution Workflow

```text
┌────────────────────────┐
│                        │
│   Start: 180nm GDSII   │
│         Import         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Boundary & Stitch    │
│      Domain Setup      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  3D Mesh Generation &  │
│    Dielectric Stack    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      Distributed       │
│    Laplace/Poisson     │
│      Field Solve       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Multi-Conductor RC   │
│    Matrix Synthesis    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Acceptance Criteria   │
│         & LVS          │
│    Back-Annotation     │
│                        │
└────────────────────────┘
```

#### Step 1: Geometry & Process Technology File (ITF/ICT) Ingestion
1. Ingest clean GDSII/OASIS layout data of the folded bitline array, poly/silicide wordlines, $W$-plugs, and stacked crown capacitors.
2. Load calibrated 180 nm process technology files specifying:
   - Poly/silicide wordline thickness, resistivity, and pitch ($360\text{ nm to } 400\text{ nm}$).
   - Bitline metal/silicide layer geometry, shared bitline contact tungsten plug ($W$-plug) profile.
   - Stacked capacitor dielectric stack ($\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3 / \text{ONO}$) with dielectric permittivity $\kappa > 15$, and $\text{SiO}_2$ gate dielectric ($3.5\text{ nm}$).

#### Step 2: Distributed Domain Decomposition & Boundary Conditions
1. Partition the $N \times M$ memory core layout into tessellated sub-domains with a minimum 3-pitch halo overlap ($1.08\text{ µm to } 1.20\text{ µm}$) along $X$ and $Y$ boundaries to eliminate edge fringing artifacts.
2. Apply Neumann boundary conditions ($\nabla V \cdot \hat{n} = 0$) on outer insulating simulation boundaries and Dirichlet potential conditions on grounded substrate/well taps ($V_{sub} = 0\text{ V}$).
3. Configure MPI/distributed worker nodes across computing clusters for concurrent domain field calculations.

#### Step 3: Adaptive 3D Mesh Generation
1. Generate conformal 3D tetrahedral/hexahedral adaptive meshes across critical high-gradient regions:
   - High-density refinement along the $360\text{--}400\text{ nm}$ bitline-to-bitline and wordline-to-wordline spacing.
   - Conformal surface discretization around cylindrical/crown capacitor sidewalls and $W$-plug interfaces.
2. Enforce energy error tolerance $< 0.1\%$ between successive adaptive h-refinement mesh iterations.

#### Step 4: Distributed 3D Poisson & Laplace Electrostatic Extraction
1. Solve 3D Laplace equation $\nabla \cdot (\epsilon(\mathbf{r}) \nabla \phi(\mathbf{r})) = 0$ for multi-conductor capacitance matrix:
   - Excite one net (e.g., active bitline $BL$) to unit voltage ($1.0\text{ V}$) while maintaining adjacent conductors ($\overline{BL}$, adjacent $BL_{i\pm1}$, crossing $WL_j$, and capacitor storage nodes) at $0\text{ V}$.
   - Compute integrated surface charge $Q_k = \oint_{S_k} \epsilon \mathbf{E} \cdot d\mathbf{A}$ on all neighboring conductors.
2. Solve continuity equations $\nabla \cdot (\sigma(\mathbf{r}) \nabla V(\mathbf{r})) = 0$ along poly/silicide wordlines and bitline conductors to extract distributed resistance networks.

#### Step 5: Multi-Conductor Parasitic Matrix Synthesis & SPICE Back-Annotation
1. Consolidate sub-domain matrices via domain decomposition boundary stitching.
2. Formulate reduced-order distributed $\Pi$ or T-ladder $RC$ networks representing line resistance, ground capacitance, and cross-coupling capacitance ($C_{c, BL-BL}$, $C_{c, BL-WL}$).
3. Output annotated standard parasitic format (DSPF/SPEF) for timing, signal integrity, and sense amplifier readout margin verification.

---

### 4. Machine-Measurable Acceptance Criteria

```text
                  180nm DRAM Extracted Metric Baselines 
                 ┌─────────────────────────────────────┐
                 │░░░░░░░░░░                           │
  Retention @ 85C┤░░░░░░░░░░                           │
                 │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒              │
  Delta V Readout┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒              │
C_s Min Retention┤▓▓▓▓▓                                │
                 │▓▓▓▓▓                                │
      C_BL Budget┤█████████████████████████████████████│
                 │█████████████████████████████████████│
                 └┬────────┬────────┬────────┬────────┬┘
                 0.0     62.5     125.0    187.5  250.0 
```

| Parameter | Acceptance Metric Target | Physical Unit | Measurement Method & Reference Verification |
| :--- | :--- | :--- | :--- |
| **Total Bitline Parasitic Capacitance ($C_{BL}$)** | $\le 250.0$ | $\text{fF}$ | Integrated 3D field solver matrix extraction over full array column length (`C_BL <= 250 fF`). |
| **Storage Node Cell Capacitance ($C_s$)** | $\ge 28.0$ (Nominal range: $25.0\text{--}30.0$) | $\text{fF/cell}$ | Conformal 3D Poisson extraction across crown capacitor dielectric stack ($\kappa > 15$). |
| **Sense Amplifier Readout Differential ($\Delta V$)** | $100.0\text{ to } 150.0$ | $\text{mV}$ | Derived via $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right)$ under $C_s \ge 25\text{ fF}, C_{BL} \le 250\text{ fF}$. |
| **Cell Retention Limit at Thermal Stress** | $> 64.0$ at $85$ | $\text{ms}$ at $^\circ\text{C}$ | Electro-thermal leakage integration ($\le 1.0\text{ fA/cell}$ sub-threshold & junction leakage). |

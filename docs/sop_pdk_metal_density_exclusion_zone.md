# Standard Operating Procedure (SOP)
## Title: PDK Metal Density Rule Parameterization & Fill Exclusion Zone Definition

- **Node / Context**: 180nm CMOS Commercial MPW Tapeout (180nm Open-Source DRAM Chip, DRAM Foundation VN)
- **Module**: Full-Chip Physical Verification (DRC/LVS/ERC/Antenna) & Dummy Metal Fill Synthesis
- **Action Type**: Make
- **Status**: Accepted / Active

---

### 1. Scope & Objective
This SOP defines the exact procedural execution for parameterizing interconnect metal layer density rules, generating layout exclusion keep-out zones, and synthesizing floating/grounded dummy metal fill for 180nm DRAM tapeout sign-off. Compliance prevents CMP (Chemical Mechanical Planarization) dishing/erosion across memory array boundaries and avoids parasitic capacitive degradation on bitline/wordline interconnects.

---

### 2. Verified Technical Parameters & Literature Citations

Based on the 180nm DRAM process and interconnect specifications:
1. **Interconnect Layer Stack & Deposition**:
   - Bitline and wordline strapping utilize **Al-0.5% Cu** or pure Aluminum deposited via planar DC magnetron sputtering (*Source: Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects*).
   - Metal-1 nominal target thickness: **$350\text{ nm} \pm 5\%$** ($332.5\text{ nm}$ to $367.5\text{ nm}$).
   - Sheet resistance post-forming gas anneal ($400^\circ\text{C}$, $30\text{ min}$, $\text{N}_2/\text{H}_2\ 95/5$): **$R_s < 0.08\ \Omega/\Box$**.
2. **DRAM Array Architecture**:
   - Access transistor geometry: channel length **$L = 180\text{ nm}$**, width **$W = 220\text{ nm}$** (*Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*).
   - Cell storage capacitance budget: minimum **$28\text{ fF/cell}$**; leakage limit $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
   - Array bitline pitch and sensitive analog sense amplifiers dictate strict exclusion zones to avoid coupling.
3. **Contact / Test Structure Metrology**:
   - Transmission Line Measurement (TLM) verification structures (pads $W = 100\ \mu\text{m}$, $L_{\text{pad}} = 50\ \mu\text{m}$, gaps $5, 10, 20, 40, 80\ \mu\text{m}$) require dedicated keep-out zones (*Source: Transmission Line Measurement (TLM) for Specific Contact Resistivity*).

---

### 3. Step-by-Step Operating Procedure

```text
┌───────────────────────┐
│                       │
│     PDK Rule Deck     │
│      Extraction       │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Density Window &    │
│    Stepping Setup     │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Exclusion Zone Mask  │
│      Generation       │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Dummy Metal Fill    │
│       Synthesis       │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│    Full-Chip DRC &    │
│   Density Sign-Off    │
│                       │
└───────────────────────┘
```

#### Step 1: PDK Density Rule Deck Parameterization
1. Configure DRC/fill synthesis rule deck with the foundry 180nm metal density constraints:
   - Floating dummy fill shape: Square tiles of dimensions **$1.0\ \mu\text{m} \times 1.0\ \mu\text{m}$** (or staggered rectangular shapes **$1.2\ \mu\text{m} \times 0.6\ \mu\text{m}$**).
   - Minimum spacing between dummy tiles: **$0.6\ \mu\text{m}$**.
   - Minimum spacing from dummy tiles to signal/power routing lines ($350\text{ nm}$ thick Metal-1): **$0.8\ \mu\text{m}$**.
2. Configure moving evaluation window:
   - Window size: **$100\ \mu\text{m} \times 100\ \mu\text{m}$**.
   - Step displacement: **$50\ \mu\text{m}$** ($50\%$ window overlap).
   - Target global metal density bounds: **$20\%$ minimum** to **$70\%$ maximum**.

#### Step 2: Fill Exclusion Zone (FEZ / Keep-Out) Definition
1. **DRAM Storage Cell & Bitline Array Keep-Out**:
   - Generate boundary marker layer `FEZ_M1_ARRAY` surrounding the stacked capacitor array ($W=220\text{ nm}, L=180\text{ nm}$ active transistor cells).
   - Apply a minimum exclusion halo of **$3.0\ \mu\text{m}$** outwards from the array perimeter to prevent capacitive imbalance on edge bitlines ($28\text{ fF}$ cell budget protection).
2. **Analog Sense Amplifier & Reference Generator Keep-Out**:
   - Draw `FEZ_SENSEAMP` around all differential sense-amplifier pairs with a **$2.0\ \mu\text{m}$** halo.
3. **Metrology & TLM Test Structure Keep-Out**:
   - Apply keep-out layer `FEZ_TLM` covering all TLM pad arrays ($100\ \mu\text{m} \times 50\ \mu\text{m}$ pads with $5\text{--}80\ \mu\text{m}$ pitch) extending **$5.0\ \mu\text{m}$** past the outer boundary to preserve sheet resistance ($R_s$) and contact resistance ($R_c$) measurement accuracy.
4. **Inductor / RF / High-Speed Clock Exclusion**:
   - Establish dedicated exclusion rings extending **$15.0\ \mu\text{m}$** beyond any critical low-jitter distribution nets.

#### Step 3: Automated Metal Fill Synthesis & Boolean Insertion
1. Execute synthesis engine taking primary GDSII/OASIS design layers, subtracting active routing and dilated exclusion zones:
   $$\text{Fillable\_Region} = \text{Die\_Area} \setminus \left( \bigcup \text{Metal\_Routing\_Dilated}_{0.8\mu m} \cup \bigcup \text{FEZ\_Layers} \right)$$
2. Populate the eligible regions with pattern-shifted, offset grid dummy fill tiles.
3. Merge synthesized fill tiles into auxiliary GDSII layer (e.g., `M1_DUMMY` GDS datatype 1).

#### Step 4: Full-Chip Sign-Off Physical Verification (DRC Density Check)
1. Run sign-off DRC across the composite layout (`M1` + `M1_DUMMY`).
2. Verify that every $100\ \mu\text{m} \times 100\ \mu\text{m}$ window satisfies the density criteria without minimum space violations.

---

### 4. Density Target & Constraint Distribution

```text
                   ┌───────────────────────────────────┐
                   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          │
Fill Window Overlap┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          │
  Array Max Allowed┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
                   │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
 Min Density Target┤░░░░░░░░░░░                        │
                   │░░░░░░░░░░░                        │
                   └┬────────┬───────┬────────┬───────┬┘
                   0.0     17.5    35.0     52.5   70.0 
```

---

### 5. Machine-Measurable Acceptance Criteria

| Metric ID | Parameter Description | Evaluation Window / Scope | Acceptance Target | Tolerance / Boundary | Physical Units |
|---|---|---|---|---|---|
| **AC-MET-01** | Windowed Metal-1 Area Density | $100\ \mu\text{m} \times 100\ \mu\text{m}$ window ($50\ \mu\text{m}$ step) | $20.0 \le D_{M1} \le 70.0$ | No window $<20.0\%$ or $>70.0\%$ | $\%$ |
| **AC-MET-02** | Metal-1 Sputtered Film Thickness | Ellipsometry / Profilometry across wafer | $350.0$ | $\pm 5.0\%$ ($332.5 - 367.5$) | $\text{nm}$ |
| **AC-MET-03** | Post-Anneal Metal-1 Sheet Resistance | 4-point probe / TLM structure ($400^\circ\text{C}$ anneal) | $< 0.080$ | Max upper bound $0.080$ | $\Omega/\Box$ |
| **AC-MET-04** | Exclusion Zone Clearance Violation Count | Full-chip DRC (`FEZ` vs `DUMMY_M1`) | $0$ | Exactly $0$ violations | errors / count |

---

### 6. Referenced Literature
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Transistor dimensions ($L = 180\text{ nm}$, $W = 220\text{ nm}$), cell budget ($28\text{ fF/cell}$), stacked capacitor bitline coupling protection.
- **Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects**: Al-0.5% Cu interconnect, Metal-1 thickness ($350\text{ nm} \pm 5\%$), sheet resistance target ($R_s < 0.08\ \Omega/\Box$).
- **Transmission Line Measurement (TLM) for Specific Contact Resistivity**: Pad geometries ($100\ \mu\text{m} \times 50\ \mu\text{m}$, pitch $5\text{--}80\ \mu\text{m}$) and exclusion justification.

# SOP: 180nm 1T1C DRAM Cell Bitline & Wordline Matrix Layout

- **Date**: 2026-10-09
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Accepted
- **Context**: 180nm Open-Source DRAM Chip (Gen 2 µm) > Architecture & Integration > Circuit Design

---

## 1. Process Overview & Architecture

This Standard Operating Procedure (SOP) governs the layout generation and geometric rule verification for an industrial 180nm 1T1C DRAM memory cell array using an $8F^2$ or $6F^2$ folded-bitline architecture with a stacked Capacitor-Over-Bitline (COB) crown/MIM topology.

```text
┌────────────────────────┐
│                        │
│  Step 1: Active Area   │
│   & Gate Definition    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Step 2: Shared     │
│   Bitline Contact &    │
│        Routing         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Step 3: Storage Node  │
│    Contact & W-Plug    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Step 4: Crown / MIM   │
│     Capacitor Over     │
│        Bitline         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Step 5: Extraction &  │
│  DRC/LVS Verification  │
│                        │
└────────────────────────┘
```

---

## 2. Step-by-Step Procedure

1. **Active Diffusion & Wordline (Gate) Definition**:
   - Layout the access transistor active region (OD) with gate channel length $L = 180\text{ nm}$ and transistor active width $W = 220\text{ nm}$.
   - Route polysilicon wordlines (WL) orthogonally across the active diffusions at a target pitch of $360\text{ nm}$ to $400\text{ nm}$.
   - Model the thermally grown gate dielectric ($\text{SiO}_2$) targeting a physical thickness of $\sim 3.5\text{ nm}$ (thermally grown at $850^\circ\text{C}$–$900^\circ\text{C}$).

2. **Shared Bitline Contact & Bitline Metal Routing**:
   - Place a single, shared bitline contact (CB) centered between two adjacent access transistors to minimize unit cell area in the $8F^2$ / $6F^2$ folded-bitline matrix.
   - Route metal bitlines (BL and $\overline{\text{BL}}$) perpendicular to the wordlines at a pitch of $360\text{ nm}$ to $400\text{ nm}$.
   - Constrain bitline routing Parasitic Extraction (PEX) to ensure total bitline parasitic capacitance $C_{\text{BL}} \approx 250\text{ fF}$.

3. **Storage Node Contact & Tungsten Plug Formation**:
   - Construct the storage node contact (SN) over the outer drain diffusions of the dual-cell pair.
   - Define vertical tungsten interconnect plugs (W-plug) landing on the drain region to bridge contact between the substrate and the capacitor floor above the bitline level (Capacitor-Over-Bitline scheme).

4. **Stacked Capacitor (Crown / MIM) Over Bitline (COB)**:
   - Instantiate crown-shaped polysilicon or metal-insulator-metal (MIM) 3D capacitor structures vertically stacked over the bitline level.
   - Assign dielectric stack models using ONO (Oxide-Nitride-Oxide), $\text{Si}_3\text{N}_4$, or $\text{Ta}_2\text{O}_5$ / $\text{Al}_2\text{O}_3$ high-$k$ dielectric stacks ($\kappa > 15$, Equivalent Oxide Thickness $\text{EOT} \approx 3\text{ to } 4\text{ nm}$).
   - Adjust capacitor height/depth profile to ensure storage capacitance $C_s \ge 28\text{ fF}$ (acceptable range $25\text{ fF}$ to $30\text{ fF}$).

5. **Parasitic Extraction (PEX) & Differential Readout Verification**:
   - Run full-chip Design Rule Check (DRC) and Layout Versus Schematic (LVS) matrix verification across cell array boundaries.
   - Perform PEX and simulate dynamic signal development: verify differential voltage $\Delta V = \frac{C_s}{C_{\text{BL}} + C_s} \times \left(V_{\text{cell}} - \frac{V_{\text{DD}}}{2}\right)$ yields $100\text{ mV}$ to $150\text{ mV}$ into the cross-coupled sense amplifier.

---

## 3. Machine-Measurable Acceptance Criteria

```text
                    Physical Key Target Tolerances      
              ┌────────────────────────────────────────┐
              │░                                       │
 Leakage Limit┤░                                       │
              │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            │
Retention Temp┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            │
   V_sig Level┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
              │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
    C_s Target┤██████████                              │
              │██████████                              │
              └┬─────────┬─────────┬────────┬─────────┬┘
              0.0      31.2      62.5     93.8    125.0 
```

| Parameter / Metric | Target Value | Allowable Range / Limit | Physical Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Access Transistor Channel Dimensions** | $L = 180\text{ nm}$, $W = 220\text{ nm}$ | $\pm 5\%$ tolerance | $\text{nm}$ | Automated DRC / CD-SEM |
| **Bitline & Wordline Pitch** | $380\text{ nm}$ | $360\text{ nm}$ to $400\text{ nm}$ | $\text{nm}$ | Litho DRC / PEX extraction |
| **Storage Cell Capacitance ($C_s$)** | $28\text{ fF}$ | $25\text{ fF}$ to $30\text{ fF}$ (min $28\text{ fF}$ target) | $\text{fF}$ | FastCap / 3D Field Solver PEX |
| **Cell Leakage Current** | $< 1.0\text{ fA/cell}$ | $\le 1.0\text{ fA/cell}$ at $85^\circ\text{C}$ | $\text{fA/cell}$ | SPICE Junction/Subthreshold Sim |
| **Bitline Differential Signal ($\Delta V$)** | $125\text{ mV}$ | $100\text{ mV}$ to $150\text{ mV}$ | $\text{mV}$ | Transient SPICE with $C_{\text{BL}} = 250\text{ fF}$ |
| **Data Retention Time** | $> 64\text{ ms}$ | $\ge 64\text{ ms}$ at $85^\circ\text{C}$ | $\text{ms}$ | Transient Refresh Interval Test |
| **Capacitor Dielectric EOT** | $3.5\text{ nm}$ | $3.0\text{ nm}$ to $4.0\text{ nm}$ ($\kappa > 15$) | $\text{nm}$ | TEM cross-section / Ellipsometry |

---

## 4. Cited Literature Sources

1. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - Transistor dimensions: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
   - Stacked Crown/MIM Capacitor Over Bitline (COB) with W-plug drain contact.
   - High-$k$ dielectric stack ($\kappa > 15$, ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$).
   - Storage capacitance minimum of $28\text{ fF/cell}$ for soft error/coupling noise immunity.
   - Leakage target: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

2. **Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**
   - $8F^2$ or $6F^2$ 1T1C cell architecture; retention time $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - $C_s$ operating budget: $25\text{ to } 30\text{ fF}$.
   - Dielectric Equivalent Oxide Thickness (EOT): $3\text{ to } 4\text{ nm}$.
   - Wordline and bitline pitch: $360\text{ nm}\text{ to } 400\text{ nm}$.
   - Gate oxide physical thickness: $\sim 3.5\text{ nm}$ thermally grown at $850^\circ\text{C}\text{–}900^\circ\text{C}$ dry oxidation.

3. **Source: Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**
   - Folded bitline CMOS cross-coupled latch sensing scheme.
   - Signal development differential voltage $\Delta V = \left(\frac{C_s}{C_{\text{BL}} + C_s}\right) \times \left(V_{\text{cell}} - \frac{V_{\text{DD}}}{2}\right)$.
   - Signal range: $100\text{ mV}\text{ to } 150\text{ mV}$ for $C_s = 25\text{ fF}$ and $C_{\text{BL}} = 250\text{ fF}$.

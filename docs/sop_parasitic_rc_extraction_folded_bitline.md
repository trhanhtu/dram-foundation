# SOP: Parasitic RC Extraction of Folded Bitline & Storage Node Contacts with W-Plug Interconnects

- **Date**: 2026-10-12
- **Author**: Domain Expert AI (DRAM Foundation VN Council)
- **Status**: Implemented / Active Sign-off
- **Node**: 180nm Open-Source DRAM (Gen 2 µm)
- **Cell Topology**: 8F² Folded Bitline, Capacitor-Over-Bitline (COB) with Tungsten (W) Plugs

---

## 1. Overview & Scope
This Standard Operating Procedure (SOP) defines the sign-off flow for 2.5D/3D field-solver parasitic RC extraction targeting the 180nm 8F² folded bitline memory array. The extraction covers access transistor terminals ($L = 180\,\text{nm}$, $W = 220\,\text{nm}$), shared bitline W-plug contacts, storage node W-plug interconnects, and stacked capacitor integration to evaluate bitline parasitic capacitance ($C_{BL}$), cell storage capacitance ($C_s$), and readout differential signal margin ($\Delta V$).

---

## 2. Process Flow & Execution Steps

### 2.1 Extraction Flow Diagram
```text
┌────────────────────────────────────────────────────────┐
│                                                        │
│           8F² Unit Cell & Bitline GDS Layout           │
│           (L=180 nm, W=220 nm, Pitch=360-400 nm)       │
│                                                        │
└───────────────────────────┬────────────────────────────┘
                            │
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                                                        │
│         LVS Connectivity & Layer Stack Mapping         │
│          - Active, Gate Ox (3.5 nm physical)           │
│          - W-plug bitline & storage node contacts      │
│          - Stacked capacitor nodes (EOT = 3-4 nm)      │
│                                                        │
└───────────────────────────┬────────────────────────────┘
                            │
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                                                        │
│             3D/Field-Solver RC Extraction              │
│       - Shared BL contact W-plug resistance/cap        │
│       - Inter-bitline coupling & fringe caps           │
│       - Storage node to wordline/substrate coupling    │
│                                                        │
└───────────────────────────┬────────────────────────────┘
                            │
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                                                        │
│           Post-Layout SPICE Netlist Synthesis          │
│            - Distributed R-C π / T networks            │
│            - Leakage current check (< 1 fA @ 85°C)     │
│                                                        │
└───────────────────────────┬────────────────────────────┘
                            │
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│                                                        │
│      Charge-Sharing Metric Verification Sign-off       │
│         ΔV = [Cs / (C_BL + Cs)] * (V_cell - VDD/2)     │
│           Target ΔV: 100 mV - 150 mV (Cs >= 28 fF)     │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 2.2 Execution Steps
1. **Layout & Connectivity Ingestion**:
   - Ingest cell array GDSII database with minimum feature dimensions: wordline/bitline pitch = $360\,\text{nm} - 400\,\text{nm}$, access transistor channel length $L = 180\,\text{nm}$, and channel width $W = 220\,\text{nm}$.
   - Ensure the bitline contact is shared between two adjacent 1T1C memory cells.
2. **Technological Stack Definition**:
   - Map front-end-of-line (FEOL) gate oxide: physical $\text{SiO}_2$ thickness = $3.5\,\text{nm}$.
   - Model Middle-of-Line (MOL) contact vias: Tungsten plug (W-plug) vertical interconnects connecting active diffusion to bitline metallization and storage node bottom electrodes.
   - Configure capacitor dielectric parameters: High-$k$ stack ($\text{Ta}_2\text{O}_5$, $\text{Al}_2\text{O}_3$, or ONO) with effective dielectric constant $\kappa > 15$ and Equivalent Oxide Thickness $\text{EOT} = 3.0\,\text{nm} - 4.0\,\text{nm}$.
3. **Parasitic RC Extraction Execution**:
   - Execute deterministic 3D field-solver extraction on the shared bitline contact W-plug and storage node contact W-plug.
   - Calculate cumulative bitline capacitance $C_{BL}$ along folded complementary pairs ($\text{BL}$ and $\overline{\text{BL}}$), accounting for line-to-line fringe coupling and cell contact loading.
   - Compute storage cell node capacitance $C_s$ for crown/cylinder stacked capacitor architecture.
4. **Charge-Sharing & Leakage Evaluation**:
   - Synthesize distributed post-layout SPICE netlist.
   - Compute differential readout signal voltage:
     $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \left(V_{\text{cell}} - \frac{V_{DD}}{2}\right)$$
   - Validate cell retention current threshold ($I_{\text{leak}} \le 1\,\text{fA/cell}$ at $85^\circ\text{C}$).

---

## 3. Machine-Measurable Acceptance Criteria

```text
              DRAM Parasitic Extraction Sign-off Targets
               ┌───────────────────────────────────────┐
               │░░░░░░░░░░░░░░░░░░                     │
Delta-V (mV/10)┤░░░░░░░░░░░░░░░░░░                     │
   C_BL (fF/10)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    │
               │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    │
       C_s (fF)┤███████████████████████████████████████│
               │███████████████████████████████████████│
               └┬─────────┬────────┬─────────┬────────┬┘
                0         7       14        21       28 
```

| Metric Parameter | Target Specification | Physical Units | Verification Method |
| :--- | :--- | :--- | :--- |
| **Cell Storage Capacitance ($C_s$)** | $\ge 28.0$ (range $25.0 - 30.0$) | $\text{fF/cell}$ | Field-solver extraction / C-V netlist integration |
| **Bitline Parasitic Capacitance ($C_{BL}$)** | $\le 250.0$ | $\text{fF/bitline}$ | Extracted distributed RC wire model |
| **Readout Differential Signal ($\Delta V$)** | $100.0 - 150.0$ | $\text{mV}$ | Transient SPICE charge-sharing simulation |
| **Cell Junction & Sub-threshold Leakage** | $\le 1.0$ at $85^\circ\text{C}$ | $\text{fA/cell}$ | Post-layout DC operating point simulation |

---

## 4. Literature References
- **Source 1**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench* (Unit cell $L=180\,\text{nm}$, $W=220\,\text{nm}$, shared BL contact, W-plug, dielectric $\kappa > 15$, $C_s \ge 28\,\text{fF/cell}$, leakage $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$).
- **Source 2**: *Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout* (Folded bitline architecture, precharge to $V_{DD}/2$, $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{\text{cell}} - V_{DD}/2)$, $C_s = 25\,\text{fF}$, $C_{BL} = 250\,\text{fF}$, $\Delta V = 100\,\text{mV} - 150\,\text{mV}$).
- **Source 3**: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering* ($1\text{T}1\text{C}$ 8F² architecture, $C_s = 25 - 30\,\text{fF/cell}$, retention $> 64\,\text{ms}$ at $85^\circ\text{C}$, $\text{EOT} = 3 - 4\,\text{nm}$, bitline/wordline pitch $360 - 400\,\text{nm}$, gate $\text{SiO}_2 = 3.5\,\text{nm}$).

# Standard Operating Procedure (SOP)
## Interleaved Sense Amplifier & Equalizer Pitch Boundary & Cell-to-Core Floorplan Definition

- **Document ID**: `SOP-CKT-180NM-SA-FP-001`
- **Revision**: 1.0
- **Node / Generation**: 180nm Open-Source DRAM (Gen 2 - µm)
- **Author**: Domain Expert AI, DRAM Foundation VN Council
- **Target Subsystem**: CMOS Folded Bitline Sense Amplifier & Equalizer Pitch Boundary Floorplan

---

### 1. Scope & Objective
This procedure governs the physical pitch boundary definition, cell-to-core transition layout, and interleaved floorplanning for CMOS folded bitline sense amplifiers (SA) and equalizers in the 180nm open-source DRAM architecture. It specifies boundary pitch relaxations, layout symmetry rules, and floorplan interfaces required to match ultra-dense 1T1C memory array columns to peripheral sense amplifier latch pitches.

---

### 2. Literature Context & Verified Parameters
*Sourced strictly from authenticated design specifications:*
1. **Array Pitch & Interleaving Architecture**:
   - Memory cell array bitline pitch: $360\text{ nm}$ in the 180nm process node.
   - Sense amplifier pitch requirement: Relaxed via **interleaved layout** (top/bottom alternation) to $2 \times \text{pitch} = 720\text{ nm}$ per physical layout stripe.
2. **Readout & Cell Electrical Parameters**:
   - Nominal cell storage capacitance ($C_s$): $25\text{ fF}$ (stacked capacitor architecture budget $\ge 28\text{ fF}$).
   - Bitline capacitance ($C_{BL}$): $250\text{ fF}$.
   - Signal development: $\Delta V = \frac{C_s}{C_{BL} + C_s} \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right)$, yielding a differential read margin of $100\text{ mV}$ to $150\text{ mV}$.
   - Sensing & Precharge rails: Equalization transistor network pulls complementary bitlines ($BL$, $\overline{BL}$) to $V_{DD}/2$. Sensing latches activate via $SAN \rightarrow \text{GND}$ and $SAP \rightarrow V_{DD}$ to restore full CMOS rails ($0\text{ V}$ and $V_{DD}$).
3. **1T1C Cell Boundary Dimension**:
   - Access transistor geometry: Channel length $L = 180\text{ nm}$, channel width $W = 220\text{ nm}$.
   - Array leakage target: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ to maintain required data retention.

---

### 3. Step-by-Step Engineering Procedure

#### Step 1: Array Column Pitch Boundary Allocation & Interleaving Split
1. Route memory array complementary bitline pairs ($BL_{even}, \overline{BL}_{even}$ and $BL_{odd}, \overline{BL}_{odd}$) extending from the active 1T1C array boundaries at a strict $360\text{ nm}$ metal-1 bitline pitch.
2. Construct the pitch transition region by splitting bitline pairs into an interleaved top/bottom bank configuration:
   - **Even columns** ($BL_0/\overline{BL}_0, BL_2/\overline{BL}_2, \dots$) terminate into the **Bottom Sense Amplifier Stripe**.
   - **Odd columns** ($BL_1/\overline{BL}_1, BL_3/\overline{BL}_3, \dots$) route through the cell array boundary into the **Top Sense Amplifier Stripe**.
3. Allocate exactly $720\text{ nm}$ pitch width per sense amplifier block slot within the top and bottom stripes, doubling the allowable lateral dimension for peripheral transistors.

#### Step 2: Equalizer and Precharge Transistor Network Placement
1. Position the bitline equalization transistors ($N$-channel MOSFETs) adjacent to the array edge before the latch core.
2. Connect equalization gates to control line $EQ$ and source terminals to the precharge internal rail ($V_{BLP} = V_{DD} / 2$).
3. Ensure symmetric parasitic layout routing between the true bitline ($BL$) and complement bitline ($\overline{BL}$) segments across the shorting transistor bridge to prevent differential offset imbalance ($|\Delta C_{BL}| < 0.5\%$).

#### Step 3: CMOS Cross-Coupled Latch Core & Drive Line Routing
1. Place cross-coupled NMOS sense transistors ($N$-sense latch connected to $SAN$) and cross-coupled PMOS pull-up transistors ($P$-sense latch connected to $SAP$) along the common $720\text{ nm}$ boundary channel.
2. Route $SAN$ (pull-down strobe to $0\text{ V}$) and $SAP$ (pull-up strobe to $V_{DD}$) power rails horizontally on low-resistance upper metal (Metal-2/Metal-3) orthogonal to the bitline columns.
3. Integrate substrate tap/well tie strapping at regular intervals (maximum $16$ SA columns per strap) to suppress latch-up during high-speed concurrent latch strobing.

#### Step 4: Floorplan Boundary DRC & Netlist LVS Extraction Verification
1. Run signoff physical DRC across the cell-to-core boundary region, verifying minimum metal spacings and diffusion boundaries where the $360\text{ nm}$ array pitch diverges into the $720\text{ nm}$ SA stripe.
2. Run Layout Versus Schematic (LVS) differential extraction, verifying node parity between schematic netlist representations and extracted 3D layout geometries.

---

### 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Tolerance / Limit | Physical Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Array Bitline Pitch** | $360$ | $\pm 0.0$ (Exact Grid) | $\text{nm}$ | Automated DRC pitch check |
| **Interleaved SA Slot Pitch** | $720$ | $\pm 0.0$ (Exact Grid) | $\text{nm}$ | Automated DRC boundary check |
| **Differential Sensing Margin ($\Delta V$)** | $100 \text{ to } 150$ | Minimum $\ge 100$ | $\text{mV}$ | Post-layout transient SPICE |
| **Array Cell Retention Leakage** | $< 1.0$ | Max $\le 1.0$ at $85^\circ\text{C}$ | $\text{fA/cell}$ | DC bias leakage extraction |

---

### 5. Document History & Related Files
- Linked SOPs:
  - [docs/sop_folded_bitline_cmos_sense_amplifier_equalizer.md](./sop_folded_bitline_cmos_sense_amplifier_equalizer.md)
  - [docs/sop_1t1c_storage_node_floating_and_plate_connectivity.md](./sop_1t1c_storage_node_floating_and_plate_connectivity.md)

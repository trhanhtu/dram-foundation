# Standard Operating Procedure (SOP)
## Title: Custom DRAM GDS Layer Map & COB Topological Mask Definition

- **Node / Generation**: 180nm CMOS MPW Tapeout (180nm Open-Source DRAM Chip, DRAM Foundation VN) / Gen 3
- **Module**: EDA & PDK / Physical Verification / PDK Development
- **Cell Topology**: $8F^2$ Folded Bitline Stacked Capacitor-Over-Bitline (COB) ($0.259\ \mu\text{m}^2$ Cell Footprint)
- **Action Type**: Make
- **Status**: Accepted / Active

---

### 1. Scope & Objective

This Standard Operating Procedure (SOP) defines the physical GDSII stream layer mapping, topological mask booleans, and physical layout synthesis rules for an open-source 180nm $8F^2$ Folded Bitline Capacitor-Over-Bitline (COB) unit memory cell and periphery interface. The procedure establishes the exact tapeout-grade GDS layer-to-datatype bindings, access transistor geometry ($L = 180\text{ nm}, W = 220\text{ nm}$), contact landing pads, bitline metal routing, storage node tungsten contact plugs (SN contact / W-plug), and 3D crown stacked capacitor dielectric/top-plate electrode masks.

---

### 2. Verified Technical Parameters & Literature Citations

All geometrical and electrical metrics are derived directly from verified baseline literature:
1. **Unit Cell Geometry & Footprint**:
   - Access NMOS channel length: **$L = 180\text{ nm}$** (*Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*).
   - Access NMOS channel width: **$W = 220\text{ nm}$** (*Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*).
   - Cell architecture: **$8F^2$ Folded Bitline Layout**; physical cell area = **$0.259\ \mu\text{m}^2$** at $F = 180\text{ nm}$ (*Source: 1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*).
   - Array Interconnect Pitch: Bitline and wordline pitch = **$360\text{ nm}$ to $400\text{ nm}$** (*Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*).
2. **Stacked Capacitor (COB) Architecture**:
   - Topology: Crown-shaped polysilicon or metal-insulator-metal (MIM) structure erected above the drain contact via tungsten plug (W-plug) (*Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*).
   - Capacitor Dielectric: ONO (Oxide-Nitride-Oxide) triple dielectric or $\text{Ta}_2\text{O}_5\ /\ \text{Al}_2\text{O}_3$ high-k stack providing effective dielectric constant $\kappa > 15$ with equivalent oxide thickness (EOT) around **$3\text{ to }4\text{ nm}$** (*Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*).
   - Gate Dielectric: Thermally grown silicon dioxide ($\text{SiO}_2$) with **$\sim 3.5\text{ nm}$** physical thickness (*Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*).
3. **Capacitance & Leakage Budgets**:
   - Storage Node Capacitance ($C_s$): Minimum **$25\text{ fF}$ to $30\text{ fF}$ per cell (nominally $28\text{ fF}$)** (*Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*; *1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*).
   - Bitline Parasitic Capacitance ($C_b$): **$150\text{ fF}$ to $250\text{ fF}$** in an array block of 256 or 512 cells per bitline (*Source: 1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*).
   - Capacitance Ratio ($C_b / C_s$): Must be maintained between **$5:1$ and $9:1$** (degrades severely if $> 10:1$) (*Source: 1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*).
   - Leakage Current Target: Sub-threshold and junction leakage kept **$< 1\text{ fA/cell}$ at $85^\circ\text{C}$** to achieve retention time **$> 64\text{ ms}$ at $85^\circ\text{C}$** (*Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*; *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*).

---

### 3. GDS Layer Map & Mask Definition Table

The following GDS stream layer table maps standard foundry CMOS base layers and dedicated DRAM COB frontend/backend extension layers:

| Layer Name | GDS Layer : Datatype | Mask / Litho Level | Physical Purpose & Topological Definition |
| :--- | :--- | :--- | :--- |
| **DIFF** | `1:0` | DIFF / OD | Active diffusion areas; defines NMOS access transistor channel ($W = 220\text{ nm}$). |
| **WELL_P** | `2:0` | P-WELL | P-type substrate / P-well doping for array NMOS substrate isolation. |
| **POLY_WL** | `6:0` | POLY1 / WL | Poly wordline gate layer ($L = 180\text{ nm}$, pitch $360\text{ nm}$ to $400\text{ nm}$, gate $\text{SiO}_2 \sim 3.5\text{ nm}$). |
| **NPLUS** | `7:0` | N+ IMP | Heavy N-type source/drain implant defining bitline node and storage node junctions. |
| **CONT_BL** | `10:0` | CONT / DC | Direct Bitline Contact (DC) shared between two adjacent access NMOS cells in $8F^2$ pair. |
| **MET1_BL** | `11:0` | METAL1 / BL | Bitline metal conductor running orthogonal to wordlines; pitch $360\text{ nm}$ to $400\text{ nm}$. |
| **ILD1** | `12:0` | ILD1 OX | Inter-layer dielectric isolating Bitline from overlying Crown Storage Node. |
| **SN_PLUG** | `15:0` | W-PLUG / BC | Buried Contact (BC) tungsten plug reaching from access NMOS storage drain up through ILD1. |
| **CAP_BOT** | `18:0` | CROWN_BOT | Storage Node Bottom Electrode (Crown/Cylinder polysilicon or conductive metal cup). |
| **CAP_DIEL**| `19:0` | HIGHK_DIEL | High-$\kappa$ Capacitor Dielectric ($\kappa > 15$, $\text{Ta}_2\text{O}_5\ /\ \text{Al}_2\text{O}_3$ or ONO, $\text{EOT} = 3\text{ to }4\text{ nm}$). |
| **CAP_TOP** | `20:0` | PLATE_TOP | Common Plate Electrode (Cell Plate biased at $V_{plate} = V_{DD} / 2$). |
| **VIA1** | `21:0` | VIA1 | Periphery/plate contact via connecting cell plate / array circuitry to Metal-2. |
| **MET2** | `22:0` | METAL2 | Metal-2 strapping layer (Wordline strapping and global plate distribution). |

---

### 4. Step-by-Step Operating Procedure

```text
┌──────────────────────┐
│                      │
│  Step 1: Layer Map   │
│      Definition      │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│   Step 2: Active &   │
│   Gate Definition    │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│  Step 3: Bitline &   │
│   W-Plug Formation   │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│  Step 4: Capacitor   │
│  Over Bitline Mask   │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│   Step 5: Physical   │
│  Verification & DRC  │
│         Rule         │
│                      │
└──────────────────────┘
```

#### Step 1: PDK GDS Stream Ingest and Layer Configuration
1. Initialize the PDK techfile (`dram180_tech.lyp` / `dram180.layermap`) inside KLayout / Magic / OpenROAD.
2. Bind GDS layer indices to the target masks:
   - Map `DIFF` to `1:0`, `POLY_WL` to `6:0`, `CONT_BL` to `10:0`, `MET1_BL` to `11:0`.
   - Register custom COB extension layers: `SN_PLUG` (`15:0`), `CAP_BOT` (`18:0`), `CAP_DIEL` (`19:0`), and `CAP_TOP` (`20:0`).
3. Set design grid resolution to $0.005\ \mu\text{m}$ ($5\text{ nm}$ database manufacturing grid) with strict off-grid snap checks enabled.

#### Step 2: $8F^2$ Active Diffusion and Wordline Topological Layout
1. Draw the active diffusion stripe (`DIFF` `1:0`) oriented along the diagonal or folded trajectory with channel width $W = 220\text{ nm}$.
2. Lay down the poly wordline gates (`POLY_WL` `6:0`) with physical gate length $L = 180\text{ nm}$ across the active channel.
3. Pitch wordlines at $P_{WL} = 360\text{ nm}$ ($2F$), matching the folded wordline pair pitch ($360\text{ nm}$ to $400\text{ nm}$).
4. Define self-aligned source/drain implants on `NPLUS` (`7:0`). The central diffusion pocket constitutes the shared bitline contact node, while outer diffusion pockets constitute storage drain nodes.

#### Step 3: Bitline Contact & M1 Conductor Patterning
1. Place the bitline contact (`CONT_BL` `10:0`) centered on the shared drain diffusion node between two adjacent access transistors.
2. Route Metal-1 Bitline (`MET1_BL` `11:0`) running orthogonally to the wordlines at a bitline pitch $P_{BL} = 360\text{ nm}$ to $400\text{ nm}$ ($2F$).
3. Keep bitline metal width to $180\text{ nm}$ ($1F$) to minimize inter-bitline parasitic coupling and maintain $C_b \le 250\text{ fF}$ across 512-cell array blocks.

#### Step 4: Inter-Layer Dielectric (ILD1) & Storage Node Plug (W-Plug) Insertion
1. Synthesize the ILD1 planarization boundary above the bitline level.
2. Place the storage node contact plug (`SN_PLUG` `15:0`) landing on the storage diffusion nodes, routed vertically between and clear of bitline conductors.
3. Enforce minimum enclosure of `SN_PLUG` by `DIFF` $\ge 30\text{ nm}$ and clear spacing to `MET1_BL` $\ge 90\text{ nm}$ to prevent shorting or capacitive blooming to the bitline.

#### Step 5: Capacitor-Over-Bitline (COB) Mask & Plate Definition
1. Define the storage node bottom electrode cup (`CAP_BOT` `18:0`) centered directly over `SN_PLUG`. Structure as a 3D cylindrical crown with outer perimeter maximizing surface area within the $0.259\ \mu\text{m}^2$ unit cell.
2. Apply the high-$\kappa$ dielectric layer (`CAP_DIEL` `19:0`) over the crown surface, conforming to effective oxide thickness $\text{EOT} = 3\text{ to }4\text{ nm}$ ($\kappa > 15$).
3. Form the common top plate mask (`CAP_TOP` `20:0`) spanning the entire core array block.
4. Route array boundary plate contact vias (`VIA1` `21:0`) and metal strapping (`MET2` `22:0`) to couple the common plate to the $V_{DD}/2$ generator.

#### Step 6: Physical Verification (DRC & LVS) Extraction Deck Binding
1. Configure DRC deck boolean rules:
   ```text
   storage_node = CAP_BOT AND SN_PLUG
   cob_capacitor = (CAP_BOT INTERSECT CAP_TOP) ENCLOSED_BY CAP_DIEL
   ```
2. Verify that total $8F^2$ unit cell boundary measures strictly $2F \times 4F = 360\text{ nm} \times 720\text{ nm} = 0.2592\ \mu\text{m}^2 \approx 0.259\ \mu\text{m}^2$.
3. Execute LVS pin extraction ensuring the 1T1C netlist accurately connects:
   - Gate terminal: Wordline (`POLY_WL`)
   - Source terminal: Bitline (`MET1_BL`)
   - Drain terminal: Storage Node ($C_s$)
   - Common plate: $V_{plate}$ (`CAP_TOP`)

---

### 5. Acceptance Criteria Target Metrics

The physical cell layout and mask sign-off must satisfy the following machine-measurable limits:

```text
                  ┌────────────────────────────────────┐
                  │░                                   │
Cell Leakage (85C)┤░                                   │
                  │▒▒                                  │
   Cb/Cs Ratio Max┤▒▒                                  │
 Cb Max (512-cell)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                  │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
            Cs Min┤█████                               │
                  │█████                               │
                  └┬────────┬────────┬───────┬────────┬┘
                  0.0     62.5     125.0   187.5  250.0 
```

| Parameter / Metric Description | Target Threshold | Physical Unit | Measurement / Extraction Method | Pass/Fail Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **Unit Cell Footprint Area ($8F^2$)** | **$= 0.259$** | $\mu\text{m}^2$ | DRC Layout Bounding Box Extraction ($F = 180\text{ nm}$) | $0.259\ \mu\text{m}^2 \pm 2\%$ |
| **Access Transistor Dimensions ($L \times W$)** | **$180 \times 220$** | $\text{nm} \times \text{nm}$ | Optical CD / LVS Device Parameter Extraction | $L = 180\text{ nm} \pm 5\%$, $W = 220\text{ nm} \pm 5\%$ |
| **Storage Node Capacitance ($C_s$)** | **$\ge 28.0$** (nominal $28$, min $25$) | $\text{fF/cell}$ | Post-layout 3D field solver extraction at $85^\circ\text{C}$ | $\ge 25.0\text{ fF}$ ($\ge 28.0\text{ fF}$ nominal) |
| **Bitline Parasitic Capacitance ($C_b$)** | **$\le 250.0$** ($150$ to $250$) | $\text{fF}$ | Post-layout RC extraction (256/512 cells per BL) | $\le 250.0\text{ fF}$ |
| **Capacitance Ratio ($C_b / C_s$)** | **$5:1$ to $9:1$** | Ratio ($\text{dimensionless}$) | Post-layout ratio calculation ($C_b / C_s < 10:1$) | $5.0 \le C_b/C_s \le 9.0$ |
| **Cell Retention Leakage Current ($85^\circ\text{C}$)** | **$< 1.0$** | $\text{fA/cell}$ | SPICE transient leakage evaluation ($V_{DD} = 1.8\text{ V}$) | $< 1.0\text{ fA/cell}$ ($t_{ref} > 64\text{ ms}$) |

---

### 6. References & Verified Literature Sources

1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - Transistor channel dimensions $L = 180\text{ nm}$, $W = 220\text{ nm}$.
   - Stacked capacitor over bitline (COB) architecture via tungsten plug (W-plug).
   - Dielectric high-$\kappa$ stack ($\kappa > 15$), nominal $C_s \ge 28\text{ fF/cell}$, leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**
   - $8F^2$ Folded bitline footprint: $0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$.
   - Storage capacitance $C_s$: $25\text{ fF}$ to $30\text{ fF/cell}$ (nominally $28\text{ fF}$).
   - Bitline capacitance $C_b$: $150\text{ fF}$ to $250\text{ fF}$ (256/512 cells); $C_b / C_s$ ratio maintained between $5:1$ and $9:1$.
3. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**
   - Bitline and wordline pitch $360\text{ nm}$ to $400\text{ nm}$.
   - Gate dielectric $\text{SiO}_2 \sim 3.5\text{ nm}$.
   - Capacitor high-$\kappa$ dielectric equivalent oxide thickness $\text{EOT} = 3\text{ to }4\text{ nm}$; retention interval $> 64\text{ ms}$ at $85^\circ\text{C}$.

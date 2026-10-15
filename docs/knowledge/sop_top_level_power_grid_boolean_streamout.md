# SOP: Top-Level Power Grid Stitching, Custom DRAM Layer Boolean Mask Operations & Stream-Out

- **Document ID**: SOP-DRAM-180NM-GDS-001
- **Domain**: Circuit Design & Physical Layout Integration
- **Generation**: Gen 3 (180nm)
- **Node**: 180nm CMOS Open-Source DRAM (DRAM Foundation VN)

## 1. Scope & Objective
This Standard Operating Procedure governs the final assembly, top-level power rail stitching, boolean mask synthesis for proprietary DRAM stacked capacitor layers (COB / MIM), physical rule checking, and GDSII stream-out for tapeout submission to commercial 180nm MPW shuttles.

## 2. Process Flow
1. Hierarchical placement alignment of DRAM Core Mat and Periphery Blocks.
2. Inter-block power grid stitching across `$V_{DD}$`, `$V_{PP}$`, `$V_{BLP}$`, and `GND`.
3. Custom DRAM mask layer boolean synthesis (Crown/Cylinder capacitor cavity, storage node contact, plate line).
4. Physical verification (DRC, LVS, Antenna) and boundary stream-out.

## 3. Physical Parameters & Target Metrics
- Cell Architecture: 1T1C Stacked Capacitor over Bitline (COB), $8F^2$ or $6F^2$ topology.
- Minimum Capacitor Value: 25 fF to 30 fF per cell (minimum 28 fF for soft-error immunity).
- Access Transistor Dimension: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
- Bitline / Wordline Pitch: $360\text{ nm}$ to $400\text{ nm}$.
- Wordline Overdrive Boost ($V_{PP}$): $2.6\text{ V}$ to $2.8\text{ V}$.
- Bitline Precharge ($V_{BLP}$): $V_{DD} / 2$.
- Retention Time: $> 64\text{ ms}$ at $85^\circ\text{C}$ with leakage $< 1\text{ fA/cell}$.
- Equivalent Oxide Thickness (EOT): $3\text{ nm}$ to $4\text{ nm}$ ($\text{Ta}_2\text{O}_5$ / $\text{Si}_3\text{N}_4$ / ONO).
- Gate Oxide Thickness: $\sim 3.5\text{ nm}$ dry oxidation $\text{SiO}_2$.

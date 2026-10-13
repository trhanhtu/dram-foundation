# SOP: COB Stacked Capacitor & Tungsten Bitline Contact Integration Routing

- **Date**: 2026-10-13
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented
- **Generation**: Gen 2 (µm / 180nm Open-Source DRAM Chip)
- **Action Type**: Make

## Overview & Rationale
Defines the physical implementation, layout integration, and routing rules for Capacitor-Over-Bitline (COB) architecture in a 180nm 1T1C DRAM cell. COB places the crown/cylinder storage capacitor above the bitline level, reducing bitline parasitic capacitance ($C_b$) while providing adequate aspect ratio and surface area for storage node capacitance ($C_s$) to ensure noise immunity and refresh retention.

## Structural Integration Flow
```text
┌────────────────────────┐
│   Access Transistor    │
│     Active & Gate:     │
│    L=180nm, W=220nm    │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│    Bitline Contact     │
│   Shared Formation:    │
│       W-Plug Via       │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│    Bitline Routing:    │
│   Pitch 360nm-400nm,   │
│     C_b 150-250fF      │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   ILD & Storage Node   │
│     W-Plug Contact     │
│       Formation        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│     Crown MIM/Poly     │
│   Stacked Capacitor:   │
│  Ta2O5/ONO, EOT 3-4nm  │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│    Plate Line Node     │
│     Integration &      │
│     C_b/C_s Ratio      │
│      Verification      │
└────────────────────────┘
```

## Step-by-Step Procedure
1. **Access Transistor Layout & Channel Sizing**:
   - Layout the 1T1C access NMOS transistor with gate channel length $L = 180\text{ nm}$ and active width $W = 220\text{ nm}$.
   - Gate oxide physical thickness: $\sim 3.5\text{ nm}$ thermally grown $\text{SiO}_2$ ($850^\circ\text{C}-900^\circ\text{C}$ dry oxidation).
   - Enforce unit cell footprint: $8F^2$ ($0.259\ \mu\text{m}^2$) for folded bitline configuration (or $6F^2$ / $0.194\ \mu\text{m}^2$ for open bitline layout).
2. **Bitline Contact (BLC) W-Plug Integration**:
   - Etch and fill shared bitline contact via between two adjacent memory cells along the active line.
   - Deposit and planarize tungsten contact plug (W-plug) landing directly on the common drain junction.
3. **Bitline (BL) Metallization & Routing**:
   - Pattern bitlines below capacitor level (COB topology) with routing pitch of $360\text{ nm}$ to $400\text{ nm}$.
   - Wordline (WL) pitch aligned at $360\text{ nm}$ to $400\text{ nm}$.
   - Target total parasitic capacitance per bitline ($C_b$) between $150\text{ fF}$ and $250\text{ fF}$ across subarray blocks of 256 or 512 cells per bitline.
4. **Storage Node Contact (SNC) W-Plug Integration**:
   - Deposit inter-layer dielectric (ILD) over bitlines and planarize via CMP.
   - Form high-aspect-ratio vertical tungsten contact plugs (W-plug) connecting access transistor source/drain storage nodes through the bitline wiring grid up to the capacitor base.
5. **Crown Stacked Capacitor Fabrication**:
   - Erect Crown-shaped polysilicon or metal-insulator-metal (MIM) bottom electrode storage node above the bitline level.
   - Deposit high-$\kappa$ dielectric layer: $\text{Ta}_2\text{O}_5$ / $\text{Al}_2\text{O}_3$ stack ($\kappa > 15$) or ONO ($\text{SiO}_2$/$\text{Si}_3\text{N}_4$/$\text{SiO}_2$) with Equivalent Oxide Thickness (EOT) of $3\text{ nm}$ to $4\text{ nm}$.
   - Deposit common plate top electrode enclosing the crown structures.

## Acceptance Criteria
- Storage Node Capacitance ($C_s$): Nominally $28\text{ fF}$ ($\ge 25\text{ fF}$ to $30\text{ fF}$ per cell).
- Capacitance Ratio ($C_b / C_s$): Between $5:1$ and $9:1$ (must not exceed $10:1$).
- Cell Leakage Current: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- Retention Time: $> 64\text{ ms}$ at $85^\circ\text{C}$.

## Literature References
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*
- *1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*

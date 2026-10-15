# SOP: Foundry GDSII Stream-Out & Quality Sign-Off for ALD Chamber Conditioning and TiCl4/NH3 Precursor Line Saturation Prep

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Node**: 180nm Open-Source DRAM (Gen 3)
- **Module**: Thin Film Deposition / Tapeout Signoff

## 1. Overview & Objectives
This Standard Operating Procedure (SOP) governs the tapeout sign-off, layout verification, chamber vacuum conditioning, and precursor saturation preparation for ALD TiN top electrode deposition on 180nm crown capacitor 1T1C cells.

## 2. Process Flow
```text
┌────────────────────────┐
│                        │
│   GDSII Stream-Out &   │
│  DRC/LVS Verification  │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│      ALD Chamber       │
│     Conditioning &     │
│        Bakeout         │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│      TiCl4 / NH3       │
│     Precursor Line     │
│       Saturation       │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│   Quality Sign-Off &   │
│       Leak Check       │
│                        │
└────────────────────────┘
```

## 3. Step-by-Step Procedure
1. **GDSII Stream-Out & DRC/LVS Verification**:
   - Stream out layout GDSII for the 180nm 1T1C cell array (`8F^2` or `6F^2` topology).
   - Ensure access transistor gate channel length `L = 180 nm`, active width `W = 220 nm`, and wordline/bitline pitch within `360 nm to 400 nm`.
   - Complete 100% clean DRC/LVS sign-off before committing masks for crown capacitor electrode ALD patterns.
2. **ALD Vacuum Chamber Conditioning & Pump-Down**:
   - Pump down the ALD reaction chamber using turbomolecular or cryopump until base pressure drops below `2x10^-6 Torr`.
   - Maintain chamber wall bakeout jacket at baseline temperature to desorb moisture and background ambient species.
3. **TiCl4 & NH3 Precursor Line Saturation & Carrier Flow Prep**:
   - Establish high-purity inert carrier/purge gas flow (Ar 99.999%).
   - Charge and pulse `TiCl4` vapor draw lines and `NH3` delivery lines across manifold bypass valves to ensure precursor saturation, elimination of line cold spots, and steady partial pressures.
4. **Tool Quality Sign-Off**:
   - Confirm residual gas analysis (RGA) and baseline pressure stability prior to committing wafer batches for top metal electrode deposition.

## 4. Key Acceptance Criteria
- **Storage Cell Capacitance**: `>= 28 fF/cell` (target `25 - 30 fF/cell`).
- **Data Retention Time**: `> 64 ms at 85°C`.
- **Sub-threshold & Junction Leakage**: `< 1 fA/cell at 85°C`.
- **Chamber Base Pressure**: `< 2x10^-6 Torr`.
- **Wordline / Bitline Pitch**: `360 nm - 400 nm`.

## 5. References & Literature Context
- *Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects*
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*

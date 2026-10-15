# Spare Redundancy Column & Decoder Metal-Fix Jumper Placement

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
This Standard Operating Procedure (SOP) defines the engineering execution for placing spare redundancy column routing and metal-fix jumpers within an 8F² folded bitline DRAM array on a 180nm commercial MPW platform. It enables fast post-silicon yield recovery and metal-only ECO mask revisions without modifying frontend active/poly silicon layers.

## Process Flowchart
```text
┌────────────────────────┐
│                        │
│   Identify Defective   │
│         Column         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Metal-Fix Jumper ECO  │
│         Route          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Decoder Re-mapping &  │
│   Redundancy Enable    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Physical DRC/LVS    │
│      Verification      │
│                        │
└────────────────────────┘
```

## Physical Parameters & Acceptance Metrics
```text
                 Spare Redundancy Cell Physical Targets 
                ┌──────────────────────────────────────┐
                │░                                     │
Max Leakage (fA)┤░                                     │
                │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Pass Gate W (nm)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Pass Gate L (nm)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       │
                │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       │
 Cap Budget (fF)┤██████                                │
                │██████                                │
                └┬────────┬─────────┬────────┬────────┬┘
                 0       55        110      165     220 
```

## Step-by-Step Procedure
1. **Array Boundary & Spare Column Slot Allocation**:
   - Establish dedicated 8F² spare column pairs at the array edge using identical access transistor dimensions ($L = 180\,\text{nm}$, $W = 220\,\text{nm}$) and stacked capacitor architectures over bitline (COB).
2. **Metal Layer Jumper Routing**:
   - Route metal-fix strap interconnects on upper interconnect layers to bypass defective primary column select lines (CSL).
   - Maintain contact through tungsten plugs (W-plugs) to preserve drain contact interfaces without disturbing the capacitor crown.
3. **Column Decoder Re-mapping via Metal-Fix Options**:
   - Configure jumper bridges to route address match lines from primary address decoders directly to the spare column sense-amplifier blocks.
4. **Physical Verification**:
   - Perform full-chip Design Rule Check (DRC) and Layout Versus Schematic (LVS) validation ensuring all jumper contacts follow MPW design rules.

## Acceptance Criteria Target Metrics
- **Access Transistor Physical Geometry**: Channel length $L = 180\,\text{nm}$, width $W = 220\,\text{nm}$.
- **Storage Cell Capacitance Budget**: $C_{\text{cell}} \ge 28\,\text{fF}$.
- **Sub-threshold & Junction Leakage Current**: $I_{\text{leak}} < 1\,\text{fA/cell}$ at $85^\circ\text{C}$.
- **Dielectric Constant Target**: High-$\kappa$ dielectric layer $\kappa > 15$ (ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ stack).

## References & Literature Sourcing
- [Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench]
- [docs/context.yaml](./docs/context.yaml)

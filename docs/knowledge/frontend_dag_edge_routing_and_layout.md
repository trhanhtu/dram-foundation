# Frontend DAG Architecture: Multi-Port Routing, Z-Index Layering & Topological Layout

- **Date**: 2026-10-09
- **Source**: User & Frontend Architect Subagent
- **Status**: Implemented & Verified

## Overview & Rationale
A comprehensive frontend review diagnosed why previous iterations suffered from:
1. **Edge Pointers Rendered Behind Cards**: Caused by DOM tree ordering (SVG edge layer sitting below positioned card elements without explicit z-index), complete lack of `markerEnd: { type: 'arrowclosed' }`, and a CSS `translateY(-2px)` hover transform that detached nodes from stationary SVG endpoints.
2. **Chaotic 180° Bezier Loop-Arounds ("Spaghettification")**: Caused by stacking nodes vertically in a single column while only offering horizontal handles (`Position.Left` and `Position.Right`). Intra-discipline prerequisite edges were forced to exit to the right, turn 180° backwards, and sweep behind adjacent cards to enter on the left.
3. **Missing Apex Master Coordinates**: `module_dram_root` was omitted from layout coordinates, defaulting to `(0, 0)` and stacking directly on top of `MCU-01`. Cross-module edges flew backwards diagonally across the entire canvas.

---

## Architectural Redesign Implemented

### 1. 4-Port Multi-Handle Architecture
Nodes now feature explicit multi-port connection points with perimeter offsets (`!-top-1.5`, `!-bottom-1.5`, `!-left-1.5`, `!-right-1.5`) and hover glows:
- `id: "target-top"`: Incoming sequential prerequisites from above.
- `id: "target-left"`: Incoming cross-discipline dependencies from the left.
- `id: "source-bottom"`: Outgoing sequential prerequisites downwards.
- `id: "source-right"`: Outgoing cross-discipline dependencies to the right.

### 2. Intelligent Edge Routing Engine
In [`data-engine.js`](.../../.../../data-engine.js):
- **Intra-Module Sequences**: Assigned `source-bottom` $\rightarrow$ `target-top` with `type: 'smoothstep'`. Produces direct vertical lines with zero hairpin turns.
- **Inter-Module Sequences**: Assigned `source-right` $\rightarrow$ `target-left` with `type: 'smoothstep'`. Routes along clean 100px bus channels between containers.
- **Inter-Tier Handover**: (e.g. Optics Row 0 $\rightarrow$ DRAM Cell Row 1) assigned `source-bottom` $\rightarrow$ `target-top`.

### 3. Z-Index Stacking Hierarchy
- **Container Shells**: `z-index: 0`
- **SVG Edge Layer**: `z-index: 2` (renders cleanly above discipline container backgrounds)
- **Work Package Cards**: `z-index: 10`
- **Port Handles**: `z-index: 20`
- **Hover Transform Removed**: Replaced with CSS `box-shadow` glow to prevent physical edge detachment.

### 4. 4-Column Topological Layout Matrix
Containers and cards are arranged in an ordered 4-column flow:
- **Col 0**: `MCU-01` (Row 0), `CHEM-04` (Row 1)
- **Col 1**: `LITHO-02` (Row 0), `FURN-05` (Row 1)
- **Col 2**: `OPTICS-03` (Row 0), `DRAM-06` (Row 1)
- **Col 3**: `ROOT-00` Apex Master DRAM at `(x: 1500, y: 440)` cleanly terminating all three process streams from the left.

## References & Related Files
- [`index.html`](.../../.../../index.html)
- [`data-engine.js`](.../../.../../data-engine.js)
- [`sandbox/index.html`](.../../.../../sandbox/index.html)
- [`sandbox/data-engine.js`](.../../.../../sandbox/data-engine.js)
- [`workflow/server.py`](.../../..../../.../../workflow/server.py)

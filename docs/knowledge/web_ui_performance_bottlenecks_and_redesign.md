# Web UI Performance Bottlenecks and Architectural Redesign

- **Date**: 2026-10-13
- **Source**: User & Agent
- **Status**: Proposed

## Overview & Rationale

As the DRAM Foundation VN autonomous crawler expanded the knowledge base to **1,003 Work Packages** across 6 disciplines and 1 master integration graph (1,000 directed edges), the current web visualizer (`index.html`) became sluggish and unwieldy. 

This directly triggers the anti-pattern identified in [docs/context2.yaml](.../../context2.yaml):
> `spaghetti_graph`: 1,000 nodes appearing simultaneously overwhelms DOM rendering, causes layout recalculation thrashing, and creates cognitive overload.

## Root Cause Analysis

1. **DOM Tree Explosion**:
   - React Flow creates distinct HTML DOM elements for every node, handle (4 per node = 4,000 handles), label, badge, and SVG path (1,000 edges).
   - The browser must layout and manage ~15,000 DOM elements on a single canvas.
2. **State Churn on Zoom/Pan (`onMove`)**:
   - Every zoom threshold trigger (`0.7` and `1.3`) or zoom delta >= 0.2 executes `setNodes(prev => prev.map(...))` across all 1,003 nodes, triggering full React reconciliation across the entire graph.
   - `onlyRenderVisibleElements` is not enabled, forcing off-screen nodes to remain in the DOM.
3. **Flat Default View (`selectedModule = 'all'`)**:
   - The initial load mounts all 7 modules simultaneously instead of strictly enforcing a Macro-first drill-down architecture.
4. **CDN Parsing Latency**:
   - Dynamic CDN loads for `reactflow`, `react`, and `cdn.tailwindcss.com` incur high startup latency and memory overhead.

## Proposed Architectural Solutions

### 1. Macro-First Hub-and-Spoke Navigation (Hierarchical Drill-Down)
- **Level 1 (Default Landing)**: Render only the **7 Core Discipline Clusters** with status bars, metrics, and inter-discipline dependency arrows. Zero child nodes mounted initially.
- **Level 2 (Discipline Subgraph)**: Clicking a discipline loads only its isolated subgraph (e.g. Litho: 13 nodes, Optics: 31 nodes, Furnace: 351 nodes).
- **Benefits**: 70% to 99% DOM element reduction; strict adherence to `context2.yaml` Just-in-Time Generation.

### 2. Dual-Mode WBS Explorer: Fast Filterable Table + Mini Neighborhood Canvas
- **Primary Pane**: Virtualized/Paginated table with instant search (<10ms), filtering by Discipline, Generation (Gen 1 mm / Gen 2 µm), Action (Make / Buy), and Status (`done`, `in_progress`, `red_flag`).
- **Secondary Canvas (Neighborhood Ego-Graph)**: When a node is selected, render only its direct prerequisite chain and child dependents (3 to 6 nodes) on a silky-smooth canvas.
- **Inspector Drawer**: Display markdown SOP, RAG citations, and AI Council actions without page lag.

### 3. Immediate Canvas Optimizations (Quick-Win Patch)
- Set `onlyRenderVisibleElements={true}` on `<ReactFlow />`.
- Decouple zoom LOD styling from React state updates (use pure CSS container zoom levels).
- Change default initial view from `'all'` to the macro discipline overview.

## References & Related Files
- [index.html](.../../.../../index.html)
- [data-engine.js](.../../.../../data-engine.js)
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)
- [scripts/run_server.py](.../../.../../scripts/run_server.py)

# React Flow Sub-Graph Drill-Down & Edge Filtering Patterns

- **Date**: 2026-10-07
- **Source**: Agent (Reviewer 2 / Adversarial Critic)
- **Status**: Accepted

## Overview & Rationale
When rendering large modular Directed Acyclic Graphs (DAGs) across multiple engineering disciplines in React Flow (such as semiconductor fabrication WBS with 6+ sub-modules), drill-down filtering allows users to isolate and focus on a single sub-module. However, cross-module dependencies (edges whose source is in Module A and target is in Module B) introduce edge filtering boundary conditions that can cause visual dangling or React Flow console warnings if not handled properly.

## Key Details / Architecture

### 1. The Dangling Edge Problem
In a naive sub-graph filter:
```javascript
// Problematic: OR condition includes edges where only one node is visible
filteredEdges = allEdges.filter(e => activeNodeIds.has(e.source) || activeNodeIds.has(e.target));
```
When `selectedModule` is filtered to Module B:
- If an edge connects `node_A` (in Module A) to `node_B` (in Module B), `node_A` is not in `filteredNodes`.
- React Flow attempts to render the edge between `node_A` and `node_B`, cannot locate the DOM handle for `node_A`, and logs warnings.

### 2. Recommended Patterns

#### Pattern A: Strict Intra-Sub-Graph Filtering (Clean View)
```javascript
// Clean: Only render edges whose source AND target are present in active nodes
filteredEdges = allEdges.filter(e => activeNodeIds.has(e.source) && activeNodeIds.has(e.target));
```
This isolates the sub-graph cleanly, removing cross-discipline visual clutter while in drill-down mode.

#### Pattern B: Boundary Stub Nodes (Context-Preserving)
For edges crossing discipline boundaries, generate virtual "External Prerequisite" stub nodes on the left/top of the sub-graph container:
- Virtual stubs represent the cross-module dependency without rendering the full external graph.
- Clicking the stub triggers navigation to the source discipline module.

### 3. Parent Group Containers and Event Passing
In React Flow 11+:
- Parent nodes (`type: 'disciplineGroup'`) must be listed before child nodes in the `nodes` array.
- Parent containers must specify `pointer-events-none` on the outer shell and `pointer-events-auto` on interactive header elements, allowing direct click and drag interactions with child work package nodes.
- Child nodes specify `parentNode: groupId` and `extent: 'parent'`, locking relative movement within the parent bounding box.

## References & Related Files
- [index.html](.../../.../../index.html)
- [sandbox/index.html](.../../.../../sandbox/index.html)
- [data-engine.js](.../../.../../data-engine.js)
- [workflow/server.py](.../../..../../.../../workflow/server.py)

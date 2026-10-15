# Reingold-Tilford Tree Layout & 3-Ary Branching Mechanics

- **Date**: 2026-10-12
- **Source**: User & Agent Synthesis
- **Status**: Implemented & Verified

## Overview & Rationale
When visualizing the WBS (Work Breakdown Structure) graph, the canvas previously rendered all nodes within each discipline as a single vertical column (`x: 40`), with sequential daisy-chain edges (`C1 -> C2 -> C3 -> Parent`). This made a true 3-ary tree appear as a single straight line.

To reflect genuine hierarchical decomposition, the frontend engine and crawler workflow have been upgraded to:
1. **Left-to-Right Reingold-Tilford Layout**: Nodes fan out along the X-axis by tree depth (`x = 40 + depth * 380`), with parents vertically centered between their children (`y = (min_child + max_child) / 2`).
2. **Direct Branching Edges**: Sub-tasks connect directly to their parent milestone (`C_i -> P`), giving an immediate visual fan-in / fan-out structure.
3. **Dynamic Canvas Bounds & Collision Avoidance**: Discipline groups calculate their bounding boxes dynamically from their subtrees and are placed in non-overlapping columns and rows.

## Architecture Details

### 1. Reingold-Tilford Subtree Placement (`data-engine.js` & `sandbox/data-engine.js`)
- **Depth Offset**:
  ```javascript
  const x = PADDING_LEFT + depth * COL_WIDTH; // COL_WIDTH = 380px
  ```
- **Leaf & Parent Positioning**:
  - Leaf nodes allocate row increments: `y = PADDING_TOP + leafCounter++ * ROW_HEIGHT` (`ROW_HEIGHT = 180px`).
  - Internal parent nodes are centered: `y = (childYs[0] + childYs[childYs.length - 1]) / 2`.
- **Dynamic Group Sizing**:
  ```javascript
  const groupWidth = Math.max(480, PADDING_LEFT * 2 + (maxDepth + 1) * COL_WIDTH);
  const groupHeight = Math.max(280, Math.round(maxY + 220));
  ```

### 2. Multi-Directional Edge Routing
`CustomNode` in `index.html` equips handles on all 4 boundaries:
- Targets: `target-top`, `target-bottom`, `target-left`, `target-right`
- Sources: `source-top`, `source-bottom`, `source-left`, `source-right`

Edge connections dynamically choose handles based on geometric angle ($\Delta x$ vs $\Delta y$), eliminating twisted or backwards edge loops.

### 3. Tree Branch Prerequisite Edges (`workflow/crawler_engine.py`)
When System-2 divides a work package into 3 sub-tasks, it proposes 3 direct prerequisite edges pointing to the parent milestone:
```python
for c_id in child_ids:
    edges.append({
        "id": f"edge-{c_id}-to-{p_id}",
        "source": c_id,
        "target": p_id,
        "relationship_type": "prerequisite",
        "label": "Sub-task Prerequisite"
    })
```

## References & Related Files
- [`data-engine.js`](.../../.../../data-engine.js)
- [`sandbox/data-engine.js`](.../../.../../sandbox/data-engine.js)
- [`index.html`](.../../.../../index.html)
- [`sandbox/index.html`](.../../.../../sandbox/index.html)
- [`workflow/crawler_engine.py`](.../../..../../.../../workflow/crawler_engine.py)

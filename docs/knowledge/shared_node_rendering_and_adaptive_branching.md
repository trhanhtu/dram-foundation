# Shared Node Rendering & Adaptive Branching Mechanics

- **Date**: 2026-10-12
- **Source**: User & Agent Discussion
- **Status**: Implemented & Documented

## 1. Branching Strategy: Static N=3 vs Hard Jobs (10–50 Branches)

### Why Flat 10–50 Fan-Out is an Anti-Pattern
1. **Cognitive & Canvas Overload**: Spawning 50 sibling cards under one parent node creates an unnavigable 9,000px vertical stack in React Flow.
2. **LLM Context Degradation**: Prompting Gemini to output 50 detailed, non-overlapping semiconductor engineering tasks in a single JSON response results in token starvation, truncation, and shallow descriptions.
3. **Violates Work Breakdown Structure (WBS) & Miller's Law ($7 \pm 2$)**: Real-world complex tasks are not 50 flat parallel tasks; they naturally group into subsystems, milestones, and phases.

### Recommended Strategy: Hierarchical Multi-Level Decomposition vs Dynamic Branching
- **Hierarchical Tree Decomposition**:
  $$\text{Parent (400h)} \xrightarrow{5} \text{Subsystems (80h)} \xrightarrow{3} \text{Modules (26h)} \xrightarrow{3} \text{Work Packages (9h)} = 45\text{ leaves}$$
- **Adaptive Branch Factor ($N$) Formula**:
  $$N = \text{clamp}\left(\left\lceil \frac{\text{estimated\_hours}}{40} \right\rceil, 2, 7\right)$$
  - $\le 40$h: No split, generate SOP directly ($N=0$).
  - $40$–$120$h: Split into $N=2$ to $3$ tasks.
  - $120$–$300$h: Split into $N=4$ to $5$ subsystems.
  - $>300$h: Split into $N=5$ to $7$ major milestones (recurse hierarchically).

---

## 2. Rendering Shared Nodes in Current Architecture

### Two Types of Shared Nodes
1. **Convergence / Multi-Parent DAG Nodes**: Nodes with multiple incoming dependencies ($\text{in\_degree} > 1$). Example: `node-deal-grove-dry-ox` receives inputs from its 3 sub-tasks, `node-furnace-build`, and `node-rca-clean-process` (across disciplines).
2. **Shared Provider Prerequisite Nodes**: Nodes with multiple outgoing dependencies ($\text{out\_degree} > 1$). Example: `node-rca-clean-process` provides clean wafers to both `node-boe-oxide-etch` (Wet Chem) and `node-deal-grove-dry-ox` (Thermal Oxidation).

### Current Rendering Pipeline (`data-engine.js`)
1. **Discipline Ownership**: Every node belongs to one primary module file (`module_file`), anchoring its spatial coordinates $(x, y)$ inside its discipline container.
2. **Inter-Module Bridge Edges**: The SQLite database stores DAG edges across any two nodes. React Flow renders animated `smoothstep` bezier curves across discipline boundaries.
3. **Intelligent Dynamic Port Routing**: Handles connect automatically via Euclidean vector logic ($\Delta x$ vs $\Delta y$):
   - Target to the right $\implies$ `source-right` $\to$ `target-left`.
   - Target to the left $\implies$ `source-left` $\to$ `target-right`.
   - Vertical $\implies$ `source-bottom` $\to$ `target-top`.

### Scalability Roadmap for Shared Nodes
- **Proxy / Ghost Badges**: For nodes shared across $>3$ disciplines, render a lightweight "Reference Proxy" card inside the consumer module to prevent edge spaghetti.
- **Hover Highlighting**: Dim non-connected edges and highlight connected paths upon hovering any shared node.

## References & Related Files
- [`data-engine.js`](.../../.../../data-engine.js)
- [`workflow/crawler_engine.py`](.../../..../../.../../workflow/crawler_engine.py)
- [`index.html`](.../../.../../index.html)

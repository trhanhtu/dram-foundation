# DRAM Foundation VN - Strategic Philosophy & Mindset

- **Date**: 2026-10-07
- **Source**: User
- **Status**: Accepted

## 1. 5W1H Strategic Framework
- **Who**:
  - **Human**: Solo Systems Architect (Chief Engineer, controls framework, makes final decisions).
  - **AI**: Multi-Agent Council (Local Technicians, automates research, validation, and leaf SOP generation).
  - **Target Audience**: Vietnamese engineers, students, and research institutes.
- **What**: An open-source R&D map decomposing legacy DRAM fabrication (e.g., 180nm) into 1,000+ feasible sub-problems. It is a **Technology Reverse-Engineering & Mastery** program, not an immediate commercial factory build.
- **Where**:
  - **Physical**: Vietnam constraints (local supply chain, budget, machining capabilities).
  - **Digital**: Local-first architecture (SQLite/KùzuDB, Local LLM/Laya, React Flow).
- **When**:
  - **Short-Term**: 3-node sandbox immediately to eliminate Blueprint Vertigo.
  - **Long-Term**: Multi-year Generational Roadmap (Gen 1 mm $\rightarrow$ Gen 2 $\mu$m $\rightarrow$ Gen 3 nm).
- **Why**: Demystify semiconductor manufacturing and make core R&D modules approachable and measurable.
- **How**: WBS DAG, TRL evaluation, and anti-hallucination Multi-Agent Council.

---

## 2. Core Philosophies
1. **Architect vs. Technician**:
   - Human is the Architect; AI is the Technician.
   - AI is strictly prohibited from unilaterally redrawing the global skeleton. AI only generates detailed SOPs and parameters within bounded, authorized nodes.
2. **Pragmatism over Purity (Make or Buy)**:
   - Avoid reinventing the wheel. Utilize Commercial Off-The-Shelf (COTS) components (e.g., ESP32, standard motors, used optical lenses) for utility layers.
   - Concentrate R&D on proprietary algorithms, alignment jigs, and custom tooling.
3. **Bottom-Up Execution**:
   - Top-down architecture, but bottom-up execution.
   - Prove the UI and data pipelines with the first 3 nodes before scaling out 1,000 nodes.
4. **Just-In-Time Generation (Lazy Loading for AI)**:
   - Prevent token exhaustion and DOM freezes by spawning branches only when the user zooms into or expands a specific node (Semantic Zooming / Nested Graphs).

---

## 3. Anti-Patterns & Defensive Measures

| Anti-Pattern | Symptom | Defensive Measure / Cure |
| :--- | :--- | :--- |
| **Hallucination** | AI invents incorrect chemical concentrations, melt temperatures, or physical parameters. | Enforce VectorDB RAG verification and require explicit citations for every quantitative parameter. |
| **Analysis Paralysis** | Over-decomposing work packages down to trivial micro-actions (< 8 hours). | **8–80 Hour Rule**: When a task scope falls under 8 hours, stop graph spawning and write a leaf Markdown SOP instead. |
| **Spaghetti Graph** | 1,000 unorganized nodes freeze the browser or obscure execution paths. | Strict Directed Acyclic Graph (DAG) enforcement and **Nested Graphs** (drill-down into parent nodes). |

---

## References & Related Files
- [docs/context2.yaml](../context2.yaml)
- [docs/context.yaml](../context.yaml)
- [docs/knowledge/system_architecture.md](./system_architecture.md)
- [AGENTS.md](../../AGENTS.md)

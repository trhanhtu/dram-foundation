# DRAM Foundation VN - Systems Architecture & AI Council

- **Date**: 2026-10-07
- **Source**: User
- **Status**: Accepted

## 1. Overview & Vision
- **Objective**: Build core technology foundations for simple DRAM chip manufacturing (e.g., 180nm) for Vietnam using Systems Engineering, Work Breakdown Structure (WBS), and Directed Acyclic Graph (DAG) task decomposition.
- **Strategy**: Bottom-Up Implementation (starting with a 3-node prototype) paired with Top-Down Architecture.

---

## 2. Multi-Agent Council
To prevent hallucination, each node in the DAG must be reviewed by the specialized AI Council before database commitment:

1. **Domain Expert** (`Gemini` via Local VectorDB): Verifies physical/chemical specifications and writes leaf-level SOPs.
2. **Systems Engineer** (`Nimble` decision model): Validates edge pointers, prerequisites, and graph topological integrity.
3. **Project Manager** (`Laya` decision model): Enforces the 8-80 hour rule. Decides whether to spawn child nodes or terminate at a leaf SOP.
4. **Supply Chain Expert** (Decision/Generative): Classifies tasks as **Make** (in-house R&D) vs. **Buy** (Commercial Off-The-Shelf - COTS).

---

## 3. Core Principles
1. **Breadth-First Search (BFS)**: Map tier-1 and tier-2 high-level skeleton before deep-diving into granular leaf nodes.
2. **Context Travel Up**: Sub-agents query recursively up to the root node for global context prior to processing leaf tasks.
3. **Generational Roadmap (TRL)**: Technology Readiness Level progression without skipping: Gen 1 (mm) -> Gen 2 (µm) -> Gen 3 (nm).
4. **Make or Buy**:
   - Buy (COTS): Microcontrollers, motors, off-the-shelf instrumentation.
   - Make (R&D): Core algorithms, mechanical jigs, lithography fixtures.
5. **Human-in-the-Loop**: Trigger a breakpoint / red-flag review if agents debate for more than 3 rounds or exceed token budget ceilings.

---

## 4. Tech Stack & Initial Milestone
- **Frontend**: Vite + React, React Flow (Semantic Zooming, Nested Graphs).
- **Data Store**: Static JSON (`nodes.json`, `edges.json`) for prototype -> SQLite / KùzuDB for production.
- **AI Orchestration**: LangGraph / CrewAI, ChromaDB + LlamaIndex / GraphRAG.
- **Next Step**: Initial Bootstrap Sandbox (Static HTML/JS + React Flow loading 3 sample nodes across Gen 1 and Gen 2).

---

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [AGENTS.md](../../AGENTS.md)

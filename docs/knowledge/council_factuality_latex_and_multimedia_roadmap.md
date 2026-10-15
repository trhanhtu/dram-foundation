# AI Council Strictness, KaTeX Math, Language Standardization, and Media Roadmap

- **Date**: 2026-10-13
- **Source**: User & Agent Discussion
- **Status**: Implemented / In Progress

## 1. KaTeX LaTeX Math Typography
- **Problem**: Mathematical formulas, units, and chemical reactions (e.g. `$400\text{nm}$`, `$C_s \ge 28\text{fF}$`, `$\text{DI H}_2\text{O}$`) rendered as raw `$ ... $` strings because standard markdown parsers do not evaluate LaTeX math syntax.
- **Resolution**: Integrated KaTeX CDN (`katex.min.js`, `katex.min.css`, `auto-render.min.js`) into [index.html](.../../.../../index.html) and [sandbox/index.html](.../../.../../sandbox/index.html). Post-render hook evaluates math across SOP markdown, parameter chips, and primary metric targets.

## 2. AI Council Strictness & Factuality Audit
- **Systems Engineer**: 100% deterministic & strict. Programmatically enforces Kahn's DAG acyclicity, topological sort order, and validates pointer integrity. Disallows cycles and dangling prerequisite pointers.
- **Laya PM**: Programmatic 8-80h scope bounding and ModernBERT Make/Buy classification. Arrests runaway graph decomposition for tasks < 8 hours.
- **Domain Expert (Gemini System 2)**:
  - Backed by ChromaDB vector store (currently 26 empirical semiconductor chunks).
  - **Core Baseline Nodes (50-80 tasks)**: Highly actionable, industrial fab parameters (Deal-Grove oxidation rates, RCA chemical ratios, BOE etch rates, folded bitline sense amplifier tolerances).
  - **Deep Crawler Branches**: Susceptible to generic boilerplate when literature coverage is sparse. To reach 100% industrial rigor across all 1,000+ nodes, ChromaDB must be continually ingested with peer-reviewed papers, open PDKs (SkyWater 130nm / FreePDK45), and equipment manuals.

## 3. Language Standardization Strategy
- **Technical SSOT (Single Source of Truth)**: English is enforced as the sole language for all work packages, node IDs, SOP procedures, database schemas, and parameters to ensure compatibility with international semiconductor standards.
- **Architectural Philosophy**: Strategic 5W1H and foundation rules (e.g. [docs/context2.yaml](.../../context2.yaml)) maintain bilingual summaries for local Vietnamese engineering teams while maintaining English for technical execution.

## 4. Multimedia & Verification Artifacts (PoW) Roadmap
- **Mermaid Dynamic Rendering**: Integrated `mermaid.js` into web visualizer to automatically render process flowcharts and sequence timing diagrams inside SOP drawers.
- **Physical Proof of Work**: Move beyond placeholder repos (`dram-vn/...`) to link real open-source hardware repositories, open micrographs, and lab demo videos.

## References
- [index.html](.../../.../../index.html)
- [workflow/council/domain_expert.py](.../../..../../.../../workflow/council/domain_expert.py)
- [workflow/council/orchestrator.py](.../../..../../.../../workflow/council/orchestrator.py)
- [workflow/vector_store.py](.../../..../../.../../workflow/vector_store.py)

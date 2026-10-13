# DRAM Foundation VN - Workflow Pipeline Implementation

- **Date**: 2026-10-08
- **Source**: Agent
- **Status**: Implemented & Tested

---

## 1. Objective & Workflow Overview
The automated workflow pipeline bridges the gap between raw semiconductor intelligence and the modular WBS DAG:
1. **Knowledge Ingestion Pipeline**: Crawls URLs, parses technical PDFs, and indexes semiconductor literature into local ChromaDB with ONNX embeddings.
2. **AI Council Orchestrator**: Executes a multi-stage review committee on any proposed work package before committing to modular JSON files.

---

## 2. Multi-Agent Council Review Sequence

```text
┌──────────────────────────────────────────────┐
│  Candidate Node Proposal                     │
│  (ID, Title, Description, Generation)        │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  Stage 1: Systems Engineer Agent             │
│  • NetworkX DAG topological sorting          │
│  • Cycle detection & duplicate prevention    │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  Stage 2: Laya Project Manager & Supply Chain│
│  • Non-autoregressive CPU decision model     │
│  • 8-80 Hour Rule: spawn vs write_sop        │
│  • Make vs Buy (COTS) classification         │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  Stage 3: Domain Expert Agent (Gemini + RAG) │
│  • ChromaDB semantic literature retrieval    │
│  • Leaf SOP procedure generation             │
│  • Measurable acceptance metrics & citations │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  Stage 4: Council Verdict & Modular Export   │
│  • Schema-compliant DRAMNode payload         │
│  • Export ready for GitHub Graph PR review   │
└──────────────────────────────────────────────┘
```

---

## 3. Workflow CLI Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `python -m workflow.cli status` | Displays ChromaDB document counts, active nodes, edges, and DAG health | `python -m workflow.cli status` |
| `python -m workflow.cli crawl --seed` | Ingests baseline semiconductor papers and literature into ChromaDB | `python -m workflow.cli crawl --seed` |
| `python -m workflow.cli crawl --url <URL>` | Crawls and indexes a public web page into ChromaDB | `python -m workflow.cli crawl --url https://...` |
| `python -m workflow.cli crawl --pdf <PATH>` | Extracts and indexes a local technical PDF file | `python -m workflow.cli crawl --pdf docs/paper.pdf` |
| `python -m workflow.cli review` | Runs the 4-stage AI Council review on a candidate node | `python -m workflow.cli review --id node-spin --title "Spin Coater" --desc "4000 RPM"` |

---

## References & Related Files
- [workflow/cli.py](../../workflow/cli.py)
- [workflow/vector_store.py](../../workflow/vector_store.py)
- [workflow/crawler.py](../../workflow/crawler.py)
- [workflow/council/systems_engineer.py](../../workflow/council/systems_engineer.py)
- [workflow/council/laya_pm.py](../../workflow/council/laya_pm.py)
- [workflow/council/domain_expert.py](../../workflow/council/domain_expert.py)
- [workflow/council/orchestrator.py](../../workflow/council/orchestrator.py)

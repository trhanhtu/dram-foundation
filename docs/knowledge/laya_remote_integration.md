# Laya Decision Model Remote Integration & Benchmark

- **Date**: 2026-10-08
- **Source**: User & Agent
- **Status**: Implemented

## Overview & Rationale
The DRAM Foundation VN uses Laya (a non-autoregressive ModernBERT decision engine) for ultra-fast, zero-token-cost System-1 decision routing (Make vs. Buy COTS classification, 8-80h scope sizing, safety hazard scoring, and generation classification).
To optimize inference on distributed lab workstations, Laya is deployed on a dedicated Mac mini daemon (`http://localhost:8000`), co-located with local Ollama (`http://localhost:11434`), while Gemini remains the exclusive model for generative SOP synthesis and literature RAG.

## Key Details / Architecture

### 1. Wire Contract & Protocol Specifications
- **Daemon Route**: `POST /v1/systemone` and `POST /v1/systemone/batch`
- **Schema Requirements**:
  - `state`: String representation of the node/task under review.
  - `questions`: Dictionary of questions, where each question key contains a specification dict:
    - `type`: `"choice"` | `"score"` | `"noul"`
    - `instructions`: Explicit prompt instruction (e.g. `"Is this component COTS (Buy) or custom R&D (Make)?"`). *Note: must be `instructions`, not `question`.*
    - `criteria`: List of allowable enum options or dictionary mapping choices.
- **Client Integration**:
  - Uses `laya.mcp.remote.RemoteRouter(base_url, timeout=60)` for transparent RPC invocation.
  - Seamless dual-mode fallback: if `LAYA_BASE_URL` is unreachable or unset, [`workflow/council/laya_pm.py`](.../../..../../.../../workflow/council/laya_pm.py) automatically falls back to local CPU `Router(preload=False)` and regex heuristics.

### 2. Multi-Head Routing & Throughput
- **Multi-Head Capability**: Evaluates multiple orthogonal dimensions (e.g., Action Type, Work Breakdown Scope, and Target Generation) in a single neural forward pass (~1.0s).
- **Batch Processing**: Parallel batch evaluation via `/v1/systemone/batch` processes 8 work packages in 3.27s (~409 ms/item, ~2.44 items/sec on CPU).

### 3. Co-located Infrastructure
- **Mac mini host (`127.0.0.1`)**:
  - Port 8000: `laya-serve` v0.1.0 with preloaded `english` model (`7b928d828b7b0e022f929d9bd2e44165aa270148`).
  - Port 11434: `ollama` serving `qwen3.5:latest` and `gemma4:latest`.

## References & Related Files
- [`.env`](.../../.../../.env)
- [`.env.example`](.../../.../../.env.example)
- [`workflow/council/laya_pm.py`](.../../..../../.../../workflow/council/laya_pm.py)
- [`laya_benchmark_report.json`](.../../.../../laya_benchmark_report.json)
- [`laya_openapi.json`](.../../.../../laya_openapi.json)
- [`tests/test_laya_pm.py`](.../../..../../.../../tests/test_laya_pm.py)

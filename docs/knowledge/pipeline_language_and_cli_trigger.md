# Architecture Decision: Pipeline Language Selection (Python) & Antigravity CLI Integration

- **Date**: 2026-10-08
- **Source**: Agent & User Architecture Consultation
- **Status**: Accepted

## Overview & Rationale
When deciding between **Python** and **TypeScript** for orchestrating the DRAM Foundation VN autonomous pipeline (connecting Laya System-1 routing with Antigravity-CLI System-2 deep synthesis), **Python** is selected as the exclusive language for the backend pipeline.

TypeScript remains dedicated exclusively to the React Flow frontend web visualizer (`src/`), while the entire data engine, vector store, AI council, and CLI orchestration pipeline remain 100% unified in Python.

## Architectural Trade-Off Analysis

| Evaluation Metric | Python (Selected) | TypeScript (Rejected for Pipeline) |
| :--- | :--- | :--- |
| **Laya Model Support** | Native Python SDK (`laya`, `RemoteRouter`). Zero serialization overhead. | No native TS SDK. Requires manual REST payload construction or Python child-process bridge. |
| **Antigravity CLI Triggering** | Direct via `subprocess` / `asyncio` (`agy -p ... --output-format json`) or `google-antigravity` SDK. | Via `child_process.spawn` or `execa`. Similar subprocess effort, but separated from data layer. |
| **Data Engine & Vector DB** | Direct in-memory access to ChromaDB (`SemiconductorVectorStore`) and DAG JSON state. | Requires spinning up local HTTP bridge server for every single node read/write. |
| **Test Automation** | 100% test coverage with existing `pytest` test suite (135 tests). | Requires dual test runners (Jest/Vitest + Pytest) and mock fixtures across two languages. |
| **Runtime Overhead** | Zero runtime translation tax. Single Python 3.10 virtual environment. | Dual-runtime overhead (Node.js/Bun + Python), `package.json`, `node_modules` clutter. |

---

## Antigravity CLI Model Configuration

Per workspace guidelines (`RULE[workspace:AGENTS.md]`), all generative tasks must exclusively use Gemini.

### Supported Gemini Models in `agy`
- `gemini-3.8-flash-high` (Default recommendation for fast, high-quality SOP synthesis)
- `gemini-3.8-flash-medium`
- `gemini-3.8-flash-low`
- `gemini-3.1-pro-high` (Recommended for complex multi-physics modeling and litho calculations)
- `gemini-3.1-pro-low`

CLI Flags:
- `--model <name>`: Model for the CLI session (e.g. `--model gemini-3.8-flash-high`).
- `--effort <level>`: Reasoning effort (`low`, `medium`, `high`, `xhigh`, `max`).

---

## Multi-Agent Session Topology: 1 Session vs. Multiple Sessions

### 1. Paradigm 1: Single Session with Child Subagents (`invoke_subagent`)
- **Mechanism**: A master orchestrator agent spawns subagents within the same conversation tree. Subagents communicate via `send_message`.
- **Best Use Case**: **Interactive Council Consensus**. Used when multiple disciplines (Lithography, Metallurgy, Optics) must debate, cross-examine constraints, and reach a unified consensus in real-time.
- **Limitation**: When crawling dozens of leaf nodes, dumping every child turn into one session bloats the context window and creates a single point of failure.

### 2. Paradigm 2: Multiple Independent Sessions via Python Pool (RECOMMENDED for Pipeline)
- **Mechanism**: Python pipeline supervisor (`crawler_engine.py`) traverses the DAG and invokes independent `agy` processes per work package (`max_workers=4` or `asyncio.Semaphore(4)`).
- **Best Use Case**: **Autonomous WBS Traversal & Leaf SOP Generation (50+ nodes)**.
- **Key Advantages**:
  1. **100% Clean Context**: Each work package gets a pristine context window without token bleed from previous nodes.
  2. **Process-Level Isolation & Fault Tolerance**: If Node 14 encounters an issue or rate limit, Node 14 is retried with backoff while Nodes 1–13 remain safely committed to disk.
  3. **Adaptive Model Sizing**: Assign `gemini-3.1-pro-high` to complex physics modules and `gemini-3.8-flash-high` to standard leaf SOPs.

---

## Programmatic Code Patterns

### Pattern 1: Synchronous JSON Subprocess (`agy --output-format json`)
```python
import json
import subprocess
from typing import Dict, Any, Optional

def invoke_antigravity(
    prompt: str,
    model: str = "gemini-3.8-flash-high",
    effort: str = "high",
    json_schema: Optional[str] = None,
    skip_permissions: bool = True
) -> Dict[str, Any]:
    cmd = [
        "agy",
        "-p", prompt,
        "--model", model,
        "--effort", effort,
        "--output-format", "json"
    ]
    if skip_permissions:
        cmd.append("--dangerously-skip-permissions")
    if json_schema:
        cmd.extend(["--json-schema", json_schema])
    
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)
```

### Pattern 2: Asynchronous Real-Time Event Streaming (`--output-format stream-json`)
```python
import asyncio
import json
from typing import AsyncGenerator, Dict, Any

async def stream_antigravity(
    prompt: str,
    model: str = "gemini-3.8-flash-high",
    effort: str = "high"
) -> AsyncGenerator[Dict[str, Any], None]:
    cmd = [
        "agy",
        "-p", prompt,
        "--model", model,
        "--effort", effort,
        "--output-format", "stream-json",
        "--dangerously-skip-permissions"
    ]
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    async for line in proc.stdout:
        line_str = line.decode("utf-8").strip()
        if line_str:
            yield json.loads(line_str)
    await proc.wait()
```

## References & Related Files
- [`workflow/council/laya_pm.py`](../../workflow/council/laya_pm.py)
- [`workflow/crawler_engine.py`](../../workflow/crawler_engine.py)
- [`docs/knowledge/laya_remote_integration.md`](./laya_remote_integration.md)

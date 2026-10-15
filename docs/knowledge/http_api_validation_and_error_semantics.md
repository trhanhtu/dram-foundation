# FastAPI Parameter Validation and HTTP Error Semantics

- **Date**: 2026-10-07
- **Source**: Agent
- **Status**: Proposed

## Overview & Rationale
In local bridge and service architectures (such as `workflow/server.py`), client errors (malformed payloads, missing required dictionary keys, out-of-bounds parameters) must never crash the service or bubble up as unhandled `500 Internal Server Error`. 
Internal server errors mislead monitoring systems into signaling system failures, while obscuring actionable client payload flaws.

This document formalizes the two-tier architectural defense pattern:
1. **Declarative Schema Constraints**: Leverage Pydantic `Field(..., ge=..., le=...)` at the HTTP ingress point to automatically enforce boundary conditions and generate OpenAPI contracts (returning HTTP 422).
2. **Exception Hierarchy Mapping**: Map business logic and validation exceptions (`KeyError`, `ValueError`) to client errors (`HTTP 400 Bad Request`), reserving `HTTP 500 Internal Server Error` strictly for unanticipated operational or infrastructural failures (e.g., hardware fault, filesystem corruption).

## Key Details / Architecture

### 1. Vector Search Boundary Enforcement (VULN-03)
Under ChromaDB, passing `n_results=0` or negative numbers triggers an internal `TypeError` ("cannot be negative, or zero"). Additionally, unbounded large numbers (e.g., `n_results=1,000,000`) induce unnecessary memory pressure.
- **Remediation**:
  Define explicit bounds in Pydantic:
  ```python
  class SearchRequest(BaseModel):
      query: str = Field(..., description="Semantic search query")
      n_results: int = Field(default=5, ge=1, le=100, description="Number of literature chunks to return (1-100)")
  ```
- **Defense-in-depth**:
  In the endpoint handler `search_knowledge`, catch `(TypeError, ValueError)` and return `HTTP 400 Bad Request` if internal vector store queries reject parameter variations.

### 2. Node Payload Validation & Exception Hierarchy (VULN-04)
In Python's exception hierarchy, `KeyError` inherits from `LookupError`, not `ValueError`. Consequently:
```python
try:
    ...
except ValueError:
    raise HTTPException(status_code=400)
except Exception:
    raise HTTPException(status_code=500)
```
When client payloads lack an `'id'` field (e.g., `{"node": {}}`), downstream dictionary indexing raises `KeyError`, completely skipping `except ValueError` and triggering `HTTP 500`.

- **Remediation**:
  1. **Pre-check at Gateway**: Validate that `req.node` contains a non-empty string `'id'` before dispatching to council orchestrators.
  2. **Exception Tuple Handling**: Expand the handler to catch `except (ValueError, KeyError) as ve:` to translate missing keys and invalid values to `HTTP 400 Bad Request`.
  3. **Informative Error Messages**: Return explicit messages (e.g., `"Invalid node payload: Node must contain a valid, non-empty 'id'"`) instead of leaking raw exception internals.

## References & Related Files
- [workflow/server.py](.../../..../../.../../workflow/server.py)
- [workflow/council/orchestrator.py](.../../..../../.../../workflow/council/orchestrator.py)
- [workflow/vector_store.py](.../../..../../.../../workflow/vector_store.py)
- [tests/test_adversarial_backend.py](.../../..../../.../../tests/test_adversarial_backend.py)

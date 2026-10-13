# DRAM Foundation VN: E2E Test Suite Infrastructure & Architecture Specification

## 1. Test Architecture & Methodology

The **DRAM Foundation VN** test infrastructure is engineered as an opaque-box, multi-tiered verification framework designed to validate every layer of the Semiconductor Knowledge OS:
- **FastAPI Bridge Server** REST API contracts.
- **ChromaDB Vector Store** offline RAG retrieval and literature persistence.
- **Multi-Discipline WBS** (6 domains) schema conformity and Kahn DAG acyclicity.
- **AI Multi-Agent Council** (Systems Engineer, Laya ModernBERT PM, Gemini Domain Expert) review and commit workflows.
- **Physical Semiconductor Fabrication Line** physics, chemical hazards, and electrical readout signal flows.

### Structural Flow Diagram

```text
┌────────────────────────┐    ┌────────────────────────┐    ┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │    │                        │    │                        │
│    Tier 1: Feature     │    │   Tier 2: Boundary &   │    │  Tier 3: Cross-Module  │    │      Tier 4: Fab       │
│        Coverage        │    │         Corner         │    │      Interactions      │    │       Workflows        │
│                        │    │                        │    │                        │    │                        │
└─────────┬──────────────┘    └────────────┬───────────┘    └────────────┬───────────┘    └────────────┬───────────┘
          │                                │                             │                             │
          │                                │                             │                             │
          │   ╭────────────────────────────┼─────────────────────────────╯                             │
          │   │                            │                                                           │
          │ ╭─┼─┬───────────┬──────────────╯                                                           │
          ▼ ▼ ▼ ▼           │                                                                          │
┌────────────────────────┐  ╰──────────────────────────────────────────────────────────────────────────╯
│                        │
│      Client REST       │
│       TestClient       │
│                        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│                        │
│     FastAPI Bridge     │
│         Server         │
│                        │
└────────────┬───────────┘  ╭──────────────────────────────────────────────────────────────────────────╮
             │              │                                                                          │
             ├──────────────┴──────────────╮                                                           │
             ├─────────────────────────────┼─────────────────────────────╮                             │
             │                             │                             │                             │
             ▼                             ▼                             ▼                             ▼
┌────────────────────────┐    ┌────────────────────────┐    ┌────────────────────────┐    ┌────────────────────────┐
│                        │    │                        │    │                        │    │                        │
│  Systems Engineer DAG  │    │  Laya PM 8-80h Model   │    │  ChromaDB RAG Corpus   │    │    Modular WBS JSON    │
│       Validator        │    │                        │    │                        │    │          SSOT          │
│                        │    │                        │    │                        │    │                        │
└────────────────────────┘    └────────────────────────┘    └────────────────────────┘    └────────────────────────┘
```

---

## 2. Four-Tier Testing Pyramid

```text
                  ┌────────────────────────────────────┐
                  │■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■│
     Baseline Unit┤■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■│
                  │███████████                         │
 Tier 4 (Fab Flow)┤███████████                         │
Tier 3 (Cross-Mod)┤▓▓▓▓▓▓▓▓                            │
                  │▓▓▓▓▓▓▓▓                            │
 Tier 2 (Boundary)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    │
                  │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    │
  Tier 1 (Feature)┤░░░░░░░░░░░░░░░░░░░░░░░░░           │
                  │░░░░░░░░░░░░░░░░░░░░░░░░░           │
                  └┬────────┬────────┬───────┬────────┬┘
                  0.0      7.2     14.5    21.8    29.0 
```

### Tier 1: Feature Coverage (20 Tests)
Covers all core system features across primary operational paths:
1. **FastAPI REST Endpoints**: `/api/status`, `/api/graph`, `/api/manifest`, `/api/modules`, `/api/search`, `/api/crawl`, `/api/council/review`, and `/api/council/commit`.
2. **ChromaDB Vector Store**: Client initialization, persistent collection verification, semantic retrieval scoring, document upserting, batch ingestion, and crawler word chunking.
3. **WBS 6-Discipline Schemas & DAG**: All 6 discipline files present, schema conformity against `node.schema.json` and `edge.schema.json`, Kahn DAG acyclicity, and topological precedence invariants.

### Tier 2: Boundary & Corner Cases (26 Tests)
Stresses the system under extreme, invalid, and edge-case operational conditions:
1. **Search & Crawler Boundaries**: Empty string queries, whitespace-only queries, oversized `n_results` limits, sub-30-character text filtration, and extreme chunk boundaries.
2. **Schema Enum Violations**: Rejection of invalid generation enums, unapproved action types (`Steal`), illegal lifecycle statuses (`demolished`), negative effort estimates, and missing required attributes.
3. **Graph Topology Corner Cases**: Rejection of direct 2-node cycles (A → B → A), multi-hop 3-node cycles (A → B → C → A), duplicate node IDs, self-loops (A → A), and dangling edges pointing to non-existent source or target IDs.
4. **API Errors & Resource Boundaries**: 404 on non-existent modules, 404 on invalid target commit files, 400 on duplicate node commits, and Laya ModernBERT effort clamping at minimum 8 hours and maximum 80 hours.

### Tier 3: Cross-Feature Interactions (6 Tests)
Validates multi-subsystem cascading workflows:
1. **Search → Review → Commit → Manifest → Graph Reload Pipeline**: Queries vector store for literature, synthesizes candidate node via AI Council, atomically commits node to disk, verifies manifest node count updates, reloads unified DAG, and verifies `/api/status` reflects incremented count.
2. **Multi-Discipline DAG Precedence Chains**:
   - Drive & Litho Chain: `MCU COTS` (Mod 1) → `Litho Stage` (Mod 2) → `Optical Aligner` (Mod 3) → `DRAM Cell Layout` (Mod 6).
   - Chemistry & Thermal Chain: `Wet Bench Safety` (Mod 4) → `RCA Clean Line` (Mod 4) → `Quartz Furnace Build` (Mod 5) & `Deal-Grove Dry Oxidation` (Mod 5).
3. **Cross-Module Edge Integrity**: Verifies zero dangling inter-module edges across all 6 files.
4. **Corpus Re-Ingestion Idempotency**: Confirms running `/api/crawl` seed re-indexing does not alter or corrupt DAG node/edge states.

### Tier 4: Real-World Semiconductor Fabrication Workflows (8 Tests)
Directly tests realistic semiconductor foundry workflows and physical verification protocols:
1. **Wafer Fab End-to-End Sequence**: Wafer surface prep (RCA-1/2) → quartz tube furnace calibration → Deal-Grove dry gate oxidation (3.5 nm) → microscopic optical alignment (±5 µm) → 1T1C DRAM storage cell layout (C_s ≥ 28 fF, 8F² footprint).
2. **Interactive User Work Package Lifecycle**: Simulates human engineer proposing an RTA dopant activation work package via `/api/council/review`, obtaining unanimous council approval, committing via `/api/council/commit`, and querying live DAG via `/api/graph`.
3. **Chemical Safety & Equipment Interlocks**: Verifies that hazardous chemical (HF, Piranha) and high-temperature (1000°C) operations have verified facility prerequisites (exhaust fume hood ≥ 0.5 m/s, calibrated Type S thermocouples).
4. **DRAM Readout Circuit Signal Chain**: Verifies physical signal flow: 1T1C storage cell → CMOS folded bitline sense amplifier (ΔV > 120 mV) → wordline address decoders & Dickson VPP charge pump (2.8V).
5. **Bits-to-Atoms Proof-of-Work Verification**: Verifies completed nodes contain verifiable repos, lab videos, and machine-measurable engineering targets.
6. **Technology Readiness Level (TRL) Directional Guard**: Prevents "Quantum Leap Syndrome"; ensures macroscopic Gen 1 precedes microscopic Gen 2 without reverse dependencies.
7. **8-80 Hour Decomposition Rule**: Enforces that all work packages in the OS fall within 8 to 80 hours.
8. **AI Council Interception of Unphysical Loops**: Ensures invalid cycles are blocked at the review stage before committing to disk.

---

## 3. Test Isolation & Idempotence Strategy

To ensure zero disk corruption and complete test independence:
- **`isolated_wbs_state` Pytest Fixture**: Snapshots `data/manifest.json` and all files in `data/modules/*.json` before executing any test that performs commits. In the fixture's `finally` block, it restores the exact original files to disk.
- **In-Memory & Dedicated Temp Stores**: Vector store unit tests use temporary isolated directories (`tmp_path`) to prevent polluting the 22-chunk persistent knowledge corpus.
- **Opaque-Box Testing**: REST API endpoints are tested using Starlette/FastAPI `TestClient(app)`, issuing genuine HTTP requests and asserting on response payloads, status codes, and database states.

---

## 4. Test Suite Execution Matrix

| Test File | Tier Focus | Tests Count | Execution Target | Status |
| :--- | :--- | :---: | :--- | :---: |
| `tests/test_crawler.py` | Baseline Crawler | 2 | Chunking logic & seed docs | **PASS** |
| `tests/test_dag.py` | Baseline DAG | 8 | Modular graph & Kahn sorting | **PASS** |
| `tests/test_laya_pm.py` | Baseline Laya PM | 3 | Make/Buy & 8-80h rule | **PASS** |
| `tests/test_server_api.py` | Baseline FastAPI | 10 | REST API endpoints | **PASS** |
| `tests/test_vector_store.py` | Baseline ChromaDB | 6 | Vector store queries & upserts | **PASS** |
| `tests/test_e2e_comprehensive.py` | Tier 1, Tier 2, Tier 3 | 52 | Full feature, boundary, and cross-module interactions | **PASS** |
| `tests/test_semiconductor_workflows.py` | Tier 4 | 8 | End-to-end fab line & user lifecycle | **PASS** |
| **Total Test Suite** | **All 4 Tiers** | **89** | **Complete System Verification** | **100% PASS** |

---

## 5. Running the Test Suite

```bash
# Run entire test suite
pytest -v

# Run comprehensive E2E tests only (Tiers 1, 2, 3)
pytest tests/test_e2e_comprehensive.py -v

# Run semiconductor fab workflows only (Tier 4)
pytest tests/test_semiconductor_workflows.py -v
```

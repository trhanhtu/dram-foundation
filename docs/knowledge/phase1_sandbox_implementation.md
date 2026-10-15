# DRAM Foundation VN - Phase 1: Micro-Sandbox Implementation

- **Date**: 2026-10-07
- **Source**: Agent
- **Status**: Implemented & Verified

---

## 1. Objective & Purpose
As mandated by [docs/context.yaml](.../../context.yaml) (`initial_bootstrap_task`) and [docs/context2.yaml](.../../context2.yaml) (*Bottom-Up Execution*), Phase 1 was executed immediately to eliminate **Blueprint Vertigo** without getting lost in abstraction.

---

## 2. Technical Stack & Design Decisions
- **Zero-Build Standalone HTML**: Uses browser-native ESM import maps (`react`, `react-dom/client`, `reactflow@11.11.4` via `esm.sh`) and Tailwind CSS CDN.
- **Offline / Local Execution**: Servable via simple local HTTP server (`python -m http.server 3000`) or [start_sandbox.bat](.../../.../../start_sandbox.bat).
- **Zero AI Branching**: Node topologies and details are purely deterministic to validate UI responsiveness, pan, zoom, and inspection capabilities before introducing autonomous agents.

---

## 3. The 3 Baseline Nodes

```text
[node-mcu-cots] ────────► [node-gen1-mm] ────────► [node-gen2-um]
  ESP32 Stepper             Macroscopic Litho       Microscopic Mask
  Controller                Stage (±0.1 mm)         Aligner (±5 µm)
  • Buy (COTS)              • Make (R&D)            • Make (R&D)
  • Status: Done            • Status: Done          • Status: In_Progress
```

1. **`node-mcu-cots`** (ESP32 Closed-Loop Motor Controller):
   - Category: Electronics & Firmware.
   - Action: `Buy` (COTS).
   - Philosophy: Avoid reinventing microcontroller boards at Gen 1.
2. **`node-gen1-mm`** (Macroscopic Linear Lithography Stage):
   - Category: Precision Mechanics.
   - Action: `Make` (In-house R&D).
   - Metrics: Positioning tolerance $\pm 0.1\text{ mm}$ verified by caliper.
   - Proof of Work: Physical video demonstration and CAD repository links.
3. **`node-gen2-um`** (Microscopic Mask Optical Alignment):
   - Category: Optics & Precision Alignment.
   - Action: `Make` (In-house R&D).
   - Metrics: Alignment precision $\pm 5.0\text{ }\mu\text{m}$, 365nm UV LED source.
   - Status: `In_Progress`.

---

## 4. UI & Inspection Drawer Features
- **Semantic Glow & Badges**: Clean distinction between `Make (R&D)` (Emerald) and `Buy (COTS)` (Cyan).
- **Detailed Drawer**: Clicking any node opens a panel showing Acceptance Target Metrics, Leaf SOP, Proof-of-Work verification badges, and RAG literature citations.
- **Controls & Navigation**: Integrated MiniMap, Zoom In/Out, Fit View, and Background Grid.

---

## References & Related Files
- [sandbox/index.html](.../../.../../sandbox/index.html)
- [index.html](.../../.../../index.html)
- [start_sandbox.bat](.../../.../../start_sandbox.bat)
- [docs/plan_n_days.md](.../../plan_n_days.md)

# SOP: Residual Overlay Error Budget Decomposition & EBDW Stepper Correction Verification (<=35nm)

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN Council)
- **Status**: Accepted
- **Generation**: Gen 3 (180nm Open-Source DRAM Chip MPW Tapeout)

## Overview & Rationale
In the 180nm open-source DRAM architecture (DRAM Foundation VN), precise overlay between the polysilicon gate layer and active diffusion (`diff`) is critical to avoid source/drain asymmetric overlaps, threshold voltage shifts, channel length shortening below minimum design rule ($L = 150\text{ nm}$ drawn / $180\text{ nm}$ nominal access transistor), and degradation of cell storage retention. This Standard Operating Procedure defines the decomposition of total measured overlay errors across wafer vector maps and the verification of residual uncorrectable errors after Electron Beam Direct Write (EBDW) stage correction within the permissible $\le 35\text{ nm}$ budget.

## Literature & Baseline References
1. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Placement Grid: $0.005\ \mu\text{m}$ ($5\text{ nm}$).
   - Active diffusion minimum width: $0.15\ \mu\text{m}$ ($150\text{ nm}$).
   - Gate Poly minimum length: $0.15\ \mu\text{m}$ ($150\text{ nm}$ drawn); spacing: $0.21\ \mu\text{m}$.
   - Permissible gate poly-to-active overlay budget: $\le 35\text{ nm}$.
2. **180nm DRAM Cell Layout Topology (Stacked Capacitor vs Deep Trench)**:
   - Access transistor geometry: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
   - Folded bitline $8F^2$ / $6F^2$ stacked capacitor over bitline (COB).

## Workflow Execution Flow
```text
┌───────────────────────┐
│   Active Diffusion    │
│    Layer Alignment    │
│         Marks         │
└───────────┬───────────┘
            ▼
┌───────────────────────┐
│    EBDW Stage Grid    │
│   Coarse Alignment    │
└───────────┬───────────┘
            ▼
┌───────────────────────┐
│    Poly Gate EBDW     │
│       Exposure        │
│     L=150nm-180nm     │
└───────────┬───────────┘
            ▼
┌───────────────────────┐
│  Critical Dimension   │
│     SEM & Overlay     │
│       Metrology       │
└───────────┬───────────┘
            ▼
┌───────────────────────┐
│      Vector Map       │
│    Decomposition &    │
│  Residual Extraction  │
└───────────┬───────────┘
            ▼
┌───────────────────────┐
│     Verification:     │
│  Residual Overlay <=  │
│         35nm          │
└───────────────────────┘
```

## Step-by-Step Procedure
1. **Substrate & Alignment Target Registration**:
   - Register wafer alignment marks from the prior Active Diffusion (`diff`) lithography layer with minimum active feature width $0.15\ \mu\text{m}$ ($150\text{ nm}$).
   - Load wafer onto EBDW laser interferometer stage calibrated to the foundry physical placement grid of $0.005\ \mu\text{m}$ ($5\text{ nm}$).
2. **First-Order Systematic Global Offset Modeling**:
   - Execute optical/SEM multi-point alignment across standard peripheral scribe-line targets.
   - Decompose gross wafer vector map into translation offsets $(T_x, T_y)$, wafer expansion/scaling $(S_x, S_y)$, and orthogonal wafer rotation $(\Theta_x, \Theta_y)$.
3. **EBDW Stepper Feedback Correction Application**:
   - Apply linear feedforward correction coefficients to the EBDW deflector and stage motion control system.
   - Restrict grid snapping and correction increments strictly to integer multiples of the $5\text{ nm}$ ($0.005\ \mu\text{m}$) design grid.
4. **Poly Gate Pattern Exposure**:
   - Pattern critical poly gates at nominal DRAM access transistor length $L = 180\text{ nm}$ (minimum physical limit $150\text{ nm}$) and active width $W = 220\text{ nm}$, maintaining poly pitch spacing $\ge 0.21\ \mu\text{m}$.
5. **CD-SEM Metrology & Overlay Vector Extraction**:
   - Perform automated top-down CD-SEM overlay metrology across die array centers and cell edges measuring relative displacement $(\Delta X, \Delta Y)$ between poly gate edge and active diffusion boundary.
6. **Residual Error Budget Decomposition & Gating**:
   - Subtract systematic modeled components (translation, magnification, rotation) from measured vector field to yield residual overlay vectors:
     $$\vec{\Delta}_{\text{residual}} = \vec{\Delta}_{\text{measured}} - \vec{\Delta}_{\text{systematic}}$$
   - Calculate wafer-level $3\sigma$ residual overlay error:
     $$\text{Residual Overlay} = |\mu_{\text{residual}}| + 3\sigma_{\text{residual}}$$
   - Verify that $\text{Residual Overlay} \le 35\text{ nm}$.

## Acceptance Criteria
- **Maximum Poly-to-Active Residual Overlay Error**: $\le 35\text{ nm}$ ($|\mu| + 3\sigma$ vector magnitude across all measured sites).
- **Physical Placement Grid Quantization**: Residual correction quantization step $= 0.005\ \mu\text{m}$ ($5\text{ nm}$).
- **Critical Dimension Gate Length Compliance**: Drawn minimum gate length $L \ge 0.15\ \mu\text{m}$ ($150\text{ nm}$), DRAM nominal access gate length $L = 180\text{ nm} \pm 10\%$.
- **Minimum Poly Gate Isolation Spacing**: $\ge 0.21\ \mu\text{m}$ ($210\text{ nm}$) without bridge defects.

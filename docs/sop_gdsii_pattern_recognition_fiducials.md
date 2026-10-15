# SOP: GDSII Pattern Recognition Template Generation & Fiducial Coordinate Extraction for Gate Array

- **Document ID:** SOP-MET-GDS-003
- **Version:** 1.0.0
- **Classification:** DRAM Foundation VN - Standard Operating Procedure
- **Target Generation:** Gen 3 (180nm Open-Source DRAM Node)
- **Status:** Approved / Active

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) defines the protocol for parsing top-level GDSII stream data, isolating critical gate/diffusion layers, extracting high-precision alignment fiducials, and synthesizing multi-tier synthetic Pattern Recognition (PR) templates for automated Critical Dimension Scanning Electron Microscope (CD-SEM) navigation across the DRAM cell array.

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│   Load GDSII Stream    │
│          File          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Filter Active & Poly  │
│         Layers         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Extract Global/Die   │
│       Fiducials        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Generate Multi-FOV   │
│      PR Templates      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Export Automated    │
│     CD-SEM Recipe      │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Layout Ingestion & Grid Snapping
1. Ingest the top-level tapeout GDSII stream file into the offline metrology recipe preparation environment.
2. Verify all polygon coordinates align with the manufacturing placement grid of **0.005 µm (5 nm)**. Flag any off-grid vertices.

### Step 2: Layer Extraction & Boolean Partitioning
1. Isolate the target active diffusion (`diff`) layer and polysilicon gate (`poly`) layer.
2. Confirm unit cell access transistor design bounds:
   - Drawn gate channel length: **$L = 180\text{ nm}$** (foundry minimum design rule: **$150\text{ nm}$**).
   - Transistor width: **$W = 220\text{ nm}$**.
   - Wordline / Poly gate spacing: $\ge \mathbf{210\text{ nm}}$.
   - Cell topology: Folded bitline ($8F^2$ or $6F^2$) with wordline/bitline array pitch of **$360\text{ nm}$ to $400\text{ nm}$**.

### Step 3: Fiducial Coordinate Extraction
1. Extract die-corner global alignment marks (crosses/box-in-box) with absolute $(X, Y)$ coordinate precision snapped to the **$5\text{ nm}$** physical grid.
2. Extract local array kerf and cell-block corner fiducials situated within **$< 50\ \mu\text{m}$** vector displacement of the target gate array measurement sites.
3. Validate that the fiducial coordinate delta accommodates the maximum permissible poly-to-diffusion overlay error budget of **$\le 35\text{ nm}$**.

### Step 4: Synthetic Pattern Recognition (PR) Template Generation
1. Synthesize multi-field-of-view (FOV) raster templates from layout geometry:
   - **Macro Alignment Template:** $15\ \mu\text{m} \times 15\ \mu\text{m}$ FOV covering array boundary transitions.
   - **Micro Navigation Template:** $3\ \mu\text{m} \times 3\ \mu\text{m}$ FOV resolving individual wordline gates ($L = 180\text{ nm}$, pitch $\approx 360\text{--}400\text{ nm}$).
2. Convolve sharp layout edges with a Gaussian electron-beam profile matching CD-SEM landing potential to simulate edge blooming and contrast gradients.
3. Define the measurement Region of Interest (ROI) box centered over the $W = 220\text{ nm} \times L = 180\text{ nm}$ access transistor channel.

### Step 5: Recipe Compilation & Verification
1. Export navigation coordinates, fiducial vectors, and PR bitmap templates into the CD-SEM automated recipe format.
2. Run an offline simulated pattern matching run; ensure normalized cross-correlation (NCC) scores exceed threshold targets before releasing recipe to the cleanroom tool.

---

## 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Unit | Target / Specification | Verification Method |
| :--- | :--- | :--- | :--- |
| **Physical Placement Grid Alignment** | nm | Exactly **5 nm** (0.005 µm) | Automated GDSII off-grid vertex parser |
| **Drawn Gate Metrology Target (L)** | nm | **180 nm** ($\pm 0.0$ layout grid offset) | Pattern template edge-to-edge verification |
| **Minimum Gate Spacing Rule** | nm | $\ge \mathbf{210\text{ nm}}$ | Layout DRC / Template design spacing check |
| **Poly-to-Active Overlay Allocation** | nm | $\le \mathbf{35\text{ nm}}$ | Fiducial vector bounding box margin check |

---

## 5. Literature References
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$), folded bitline ($8F^2/6F^2$) configuration, bitline contact sharing, and array architecture.
- **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**: Manufacturing placement grid of **$0.005\ \mu\text{m}$ ($5\text{ nm}$)**; minimum poly gate length of **$150\text{ nm}$**; minimum poly gate spacing of **$0.21\ \mu\text{m}$ ($210\text{ nm}$)**; overlay error budget $\le \mathbf{35\text{ nm}}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: 1T1C array layout rules; wordline and bitline pitches of **$360\text{ nm}$ to $400\text{ nm}$**.

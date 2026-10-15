# Standard Operating Procedure (SOP)
## DUV 248nm Optical System Pupil Function & 4D TCC Matrix Discretization

- **Date**: 2026-10-15
- **Generation**: Gen 3 (nm) / 180nm Open-Source DRAM Node
- **Module**: Photolithography & OPC Simulation Engine
- **Status**: Implemented

---

### 1. Architectural Overview & Workflow

```text
┌────────────────────────┐
│                        │
│  DUV KrF Laser 248nm   │
│     & Illumination     │
│        Source J        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Entrance Pupil     │
│     Discretization     │
│        NA=0.65         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     4D Hopkins TCC     │
│  Tensor Sampling f1,   │
│       g1, f2, g2       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│          SVD           │
│  Eigen-Decomposition   │
│    & Optical Kernel    │
│       Truncation       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Simulated Aerial    │
│     Image Grid 5nm     │
│  Placement Validation  │
│                        │
└────────────────────────┘
```

---

### 2. Step-by-Step SOP Procedure

1. **Optical Wavefront & Source Initialization**:
   - Configure exposure wavelength $\lambda = 248\text{ nm}$ (KrF excimer laser source).
   - Set numerical aperture $\text{NA} = 0.65$.
   - Define effective spatial frequency cutoff $f_c = \frac{\text{NA}}{\lambda} = \frac{0.65}{248\text{ nm}} \approx 0.002621\text{ nm}^{-1}$ ($2.621\times 10^6\text{ m}^{-1}$).
   - Set the partial coherence source intensity distribution $J(f', g')$ normalized such that $\iint J(f', g') \, df' dg' = 1$.

2. **Pupil Function Discretization ($P(f, g)$)**:
   - Discretize the 2D pupil plane frequency coordinates $(f, g)$ over a uniform frequency mesh sampled to maintain spatial domain grid fidelity compliant with the minimum manufacturing placement grid of $0.005\ \mu\text{m}$ ($5\text{ nm}$).
   - Establish coherent pupil cutoff boundary:
     $$P(f, g) = \begin{cases} 1, & \sqrt{f^2 + g^2} \le \frac{\text{NA}}{\lambda} = 0.002621\text{ nm}^{-1} \\ 0, & \text{otherwise} \end{cases}$$
   - Incorporate wavefront phase error / defocus terms into $P(f, g)$ bounded by process window depth of focus ($\text{DOF} \ge 0.5\ \mu\text{m}$).

3. **4D Transmission Cross-Coefficient (TCC) Matrix Formulation**:
   - Construct the 4D Hopkins TCC tensor over pupil spatial frequency coordinate pairs $(f_1, g_1)$ and $(f_2, g_2)$:
     $$\text{TCC}(f_1, g_1; f_2, g_2) = \iint J(f', g') P(f' + f_1, g' + g_1) P^*(f' + f_2, g' + g_2) \, df' dg'$$
   - Evaluate overlapping support integrals between shifted pupil functions centered at $(f_1, g_1)$ and $(f_2, g_2)$ weighted by illumination source $J(f', g')$.

4. **Hermitian Matrix SVD Decomposition & Kernel Truncation (SOCS)**:
   - Reorder the 4D TCC tensor into a 2D Hermitian matrix $\mathbf{T}_{(f_1, g_1), (f_2, g_2)}$.
   - Compute Singular Value Decomposition (SVD) / Eigen-decomposition:
     $$\mathbf{T} = \sum_{k=1}^N \mu_k \mathbf{\Phi}_k \mathbf{\Phi}_k^*$$
   - Truncate the expansion to dominant eigenvalues $\mu_k$ capturing $>98\%$ total optical system energy for fast forward aerial image convolution.

5. **Forward Aerial Image & Mask CD Grid Verification**:
   - Convolve 2D decomposed spatial mask spectrum with top truncated optical kernels.
   - Verify that simulated aerial image contours at minimum poly gate length ($150\text{ nm}$ / $0.15\ \mu\text{m}$) and minimum poly spacing ($0.21\ \mu\text{m}$) resolve with zero sub-5nm discretization grid artifacts.

---

### 3. Machine-Measurable Acceptance Criteria

```text
                   Critical Lithography Physical Bounds 
                   ┌───────────────────────────────────┐
                   │▒▒                                 │
  Min Mfg Grid (nm)┤▒▒                                 │
 Overlay Limit (nm)┤▓▓▓▓▓▓▓▓▓                          │
                   │▓▓▓▓▓▓▓▓▓                          │
Half-Pitch Res (nm)┤███████████████████████████████████│
                   │███████████████████████████████████│
                   └┬────────┬───────┬────────┬───────┬┘
                   0.0     38.1    76.3     114.4 152.6 
```

| Metric Parameter | Target Specification | Exact Physical Units | Verification Method |
| :--- | :--- | :--- | :--- |
| **Pupil Cutoff Frequency ($f_c$)** | $0.002621$ (or $2.621 \times 10^6$) | $\text{nm}^{-1}$ ($\text{m}^{-1}$) | Numerical validation of $P(f, g)$ aperture radius ($\text{NA}/\lambda$) |
| **Minimum Rayleigh Half-Pitch Resolution ($R$)** | $\le 152$ | $\text{nm}$ | Aerial image intensity slice calculation at $k_1 = 0.40, \text{NA} = 0.65$ |
| **Physical Manufacturing Grid Snapping** | Exactly $0.005$ ($5$) | $\mu\text{m}$ ($\text{nm}$) | Coordinate quantization check on discretized spatial transformation mesh |
| **Depth of Focus Process Window ($\text{DOF}$)** | $\ge 0.5$ | $\mu\text{m}$ | Defocus phase aberration margin across wafer topography window |
| **Gate Poly to Active Diffusion Overlay Error Budget** | $\le 35$ | $\text{nm}$ | Shift vector delta validation against PDK layer overlay budget |

---

### 4. Verified Literature Context & Source Citations
- **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
  - Exposure source: DUV 248nm KrF excimer laser.
  - Rayleigh resolution: $R = k_1 \cdot (\lambda / \text{NA}) = 0.40 \cdot (248\text{ nm} / 0.65) \approx 152\text{ nm}$ half-pitch.
  - Numerical Aperture ($\text{NA}$): $0.65$.
  - Depth of Focus ($\text{DOF}$): $k_2 \cdot (\lambda / \text{NA}^2) \ge 0.5\ \mu\text{m}$.
  - Manufacturing Grid resolution: $0.005\ \mu\text{m}$ ($5\text{ nm}$).
  - Maximum permissible overlay error between gate poly and active diffusion: $\le 35\text{ nm}$.
  - Critical Dimensions (CD): Minimum active diffusion width $= 0.15\ \mu\text{m}$; minimum poly gate length $= 0.15\ \mu\text{m}$ ($150\text{ nm}$); minimum poly gate spacing $= 0.21\ \mu\text{m}$; contact hole $= 0.17\ \mu\text{m} \times 0.17\ \mu\text{m}$.

# SOP: Kelvin Test Structure Layout & 3D TCAD Contact Mesh Generation

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Node
- **Module**: Circuit Design / Metrology & TCAD

---

## 1. Process Overview & Objective
This Standard Operating Procedure (SOP) defines the end-to-end flow for laying out a four-terminal (Kelvin) test structure and synthesizing an adaptive 3D TCAD mesh across the storage node contact (SNC) / tungsten plug (W-plug) interface in a 180nm Crown-Type Capacitor-Over-Bitline (COB) 8F² DRAM cell. 

The primary goal is the extraction of true interfacial contact resistance ($R_c$), specific contact resistivity ($\rho_c$), and verification of 3D current crowding effects without parasitic trace/pad series resistance confounding.

```text
┌────────────────────────┐
│                        │
│   Layout Definition:   │
│   Kelvin 4-Terminal    │
│       Structure        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     GDSII / OASIS      │
│    Hierarchy Export    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   3D TCAD Boundary &   │
│  Material Deposition   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Adaptive Mesh      │
│  Generation: Contact   │
│  Interface Refinement  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Electromigration &   │
│    Current Crowding    │
│       Simulation       │
│                        │
└────────────────────────┘
```

---

## 2. Layout & Geometric Specifications (180nm Open-Source DRAM)

1. **Access Transistor & Cell Dimensions**:
   - Access transistor physical channel length: $L = 180\text{ nm}$ [Source: 180nm DRAM Cell Layout Topology].
   - Channel active width: $W = 220\text{ nm}$ [Source: 180nm DRAM Cell Layout Topology].
   - Critical interconnect pitch: Bitline and Wordline pitch = $360\text{ nm}$ to $400\text{ nm}$ [Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering].
   - Contact Via (W-Plug / SNC): $180\text{ nm} \times 180\text{ nm}$ square cross-section at the drain diffusion node.

2. **Kelvin Four-Terminal Arm Configuration**:
   - Force (+) and Sense (+) arms routed to the bottom active silicon/polysilicon terminal.
   - Force (-) and Sense (-) arms routed to the top metal / tungsten interconnect line.
   - Test Pad Geometry: Identical rectangular probing pads with width $W_{\text{pad}} = 100\ \mu\text{m}$ and length $L_{\text{pad}} = 50\ \mu\text{m}$ [Source: Transmission Line Measurement (TLM) for Specific Contact Resistivity].
   - Pad Enclosure & Overlap: Minimum $10\ \mu\text{m}$ enclosure around via connections; metal trace tapers down linearly to sub-micron Kelvin bridge terminals over a run length of $5\ \mu\text{m}$ to $10\ \mu\text{m}$ to minimize series lead parasitic resistance.

---

## 3. Step-by-Step 3D TCAD Contact Mesh Generation Procedure

### Step 1: Layout Import and Domain Truncation
- Import the localized Kelvin via GDSII / OASIS cell into the 3D TCAD solid modeler.
- Define a cropped 3D simulation bounding box:
  - $X \in [-1.0\ \mu\text{m}, +1.0\ \mu\text{m}]$
  - $Y \in [-1.0\ \mu\text{m}, +1.0\ \mu\text{m}]$
  - $Z$: From bulk silicon substrate ($Z = -0.5\ \mu\text{m}$) through tungsten plug ($Z = +0.6\ \mu\text{m}$) to metal cap layer ($Z = +1.0\ \mu\text{m}$).

### Step 2: 3D Material Emulation & Layer Stacking
- **Substrate / Diffusion**: Active silicon doped n-type (arsenic/phosphorus drain node, active area $W = 220\text{ nm}$, $L = 180\text{ nm}$).
- **Contact Barrier / Adhesion**: Sputtered $\text{Ti}/\text{TiN}$ barrier layer ($10\text{ nm} / 15\text{ nm}$) lining the contact hole bottom.
- **Plug Filling**: Chemical Vapor Deposition (CVD) Tungsten ($\text{W}$) plug ($180\text{ nm}$ diameter/width).
- **Dielectric Overlayer**: Inter-layer dielectric (ILD) $\text{SiO}_2$ and surrounding capacitor integration stack.

### Step 3: Adaptive Mesh Construction & Edge Refinement
- **Far-field Coarse Mesh**: Bulk substrate and outer metal arms meshed with maximum tetrahedral edge length $h_{\max} = 100\text{ nm}$.
- **Transition Mesh (ILD & Conductor Body)**: Geometric growth ratio $r = 1.25$ transitioning from coarse regions toward the contact aperture.
- **Contact Interface Refinement (Crowding Zone)**:
  - Refine the $\text{W-plug} / \text{TiSi}_2 / \text{Si}$ junction ($Z = -10\text{ nm}$ to $+20\text{ nm}$):
    - Maximum in-plane mesh pitch ($X, Y$): $\Delta x, \Delta y \le 5\text{ nm}$.
    - Vertical normal mesh pitch ($Z$): $\Delta z \le 1.0\text{ nm}$.
  - Place localized corner refinement boxes around the 4 outer peripheral corners of the $180\text{ nm} \times 180\text{ nm}$ via edge where the electric field gradient $\nabla E$ peaks due to 3D current crowding.

### Step 4: Distributed Resistivity & Physics Boundary Setup
- Apply Distributed Contact Resistance boundary physics at the semiconductor-metal interface:
  - Input specific contact resistivity $\rho_c$ derived from baseline TLM metrics.
  - Implement Fermi-Dirac carrier statistics, high-field mobility saturation, and thermodynamic heat dissipation models.
- Set Force terminal to $I_{\text{force}} = 10\ \mu\text{A}$ to $100\ \mu\text{A}$; measure drop across Sense(+) and Sense(-) terminals to compute $R_{\text{Kelvin}} = \frac{V_{\text{sense}}}{I_{\text{force}}}$.

---

## 4. Machine-Measurable Acceptance Criteria

| Metric | Target Specification | Physical Units | Tolerance / Criteria |
| :--- | :--- | :--- | :--- |
| **Contact Via Critical Dimension (CD)** | `180` | $\text{nm}$ | $\pm 5\%$ ($171\text{ nm} - 189\text{ nm}$) |
| **Critical Layer Pitch (BL/WL Pitch)** | `360` to `400` | $\text{nm}$ | Layout DRC zero violation |
| **Contact Interface Refinement Grid Size ($\Delta z$)** | $\le 1.0$ | $\text{nm}$ | Across the entire $\text{TiSi}_2/\text{Si}$ interface ($30\text{ nm}$ window) |
| **Mesh Quality Index (Minimum Tetrahedral Angle)** | $\ge 18.0$ | $\text{degrees}$ | No inverted or sliver elements ($\alpha_{\min} \ge 18^\circ$) |

```text
                                                        
                ┌──────────────────────────────────────┐
                │░░░░                                  │
Capacitance (fF)┤░░░░                                  │
                │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
WL/BL Pitch (nm)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Pad Overlap (um)┤▓▓                                    │
                │▓▓                                    │
   Via Mesh (nm)┤██                                    │
                │██                                    │
                └┬────────┬─────────┬────────┬────────┬┘
                 0       90        180      270     360 
```

---

## 5. Verified Context Citations
1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$; stacked capacitor over bitline (COB) topology with tungsten plug (W-plug).
2. **Transmission Line Measurement (TLM) for Specific Contact Resistivity**:
   - Test pad dimensions: width $W = 100\ \mu\text{m}$, length $L_{\text{pad}} = 50\ \mu\text{m}$; contact resistance $R_c$, transfer length $L_T$, and specific contact resistivity $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\ [\Omega\cdot\text{cm}^2]$.
3. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - Bitline and wordline pitch approximately $360\text{ nm}$ to $400\text{ nm}$; minimum storage capacitance budget $25\text{ fF}$ to $30\text{ fF}$ per cell.

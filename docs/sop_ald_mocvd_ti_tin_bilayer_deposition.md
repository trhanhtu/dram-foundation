# SOP: ALD/MOCVD Ti/TiN Bi-Layer Conformal Deposition & Thermal Nitridation Recipe Emulation

- **Date**: 2026-10-12
- **Author**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Accepted
- **Technology Node**: 180nm Open-Source DRAM (8F² / 6F² Stacked COB Topology)

## 1. Scope & Objective
This Standard Operating Procedure (SOP) defines the emulation recipe and execution sequence for depositing the conformal Titanium/Titanium Nitride (Ti/TiN) contact adhesion and diffusion barrier bi-layer. This bi-layer lines the high-aspect-ratio Storage Node Contact (SNC) trench and bitline contact vias prior to Tungsten plug (W-plug) fill and crown-type capacitor erection in 180nm DRAM cells.

## 2. Process Workflow

```text
┌────────────────────────┐
│                        │
│    1. Pre-Clean and    │
│   High Vacuum Degas    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  2. ALD Ti Conformal   │
│     Adhesion Layer     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│      3. MOCVD TiN      │
│   Diffusion Barrier    │
│         Layer          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       4. Thermal       │
│  Nitridation and 400C  │
│         Anneal         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    5. Metrology and    │
│   W-Plug Integration   │
│                        │
└────────────────────────┘
```

## 3. Step-by-Step Procedure

### Step 1: Pre-Clean, Load Lock, and High-Vacuum Degas
1. Subject patterned wafers (post-SNC reactive ion etching) to dilute HF native oxide strip followed by ultrapure DI rinse and Marangoni dry.
2. Transfer wafers into the multi-chamber cluster tool via load-lock.
3. Pump down the degas and deposition chambers using turbomolecular/cryopump subsystems until reaching a base pressure strictly **< 2 × 10⁻⁶ Torr** to eliminate ambient moisture and prevent unwanted oxygen incorporation into the contact interface.
4. Perform an in-situ substrate degas and preheat stage conditioning to achieve thermal equilibrium across the 180nm cell array.

### Step 2: Atomic Layer Deposition (ALD) of Conformal Ti Adhesion Layer
1. Establish substrate chuck temperature within the calibrated thermal window.
2. Introduce metal-organic or halide titanium precursor (e.g., TiCl₄ or TDMAT equivalent) with high-purity carrier gas (Ar 99.999%).
3. Execute self-limiting surface saturation exposure to coat the bottom and vertical sidewalls of the high-aspect ratio SNC trench (bitline and wordline pitch ~360 nm to 400 nm).
4. Purge excess unreacted precursor with ultra-dry N₂ / Ar.
5. Introduce reducing co-reactant (plasma-assisted H₂ or radical flux) to reduce precursor to metallic Ti, forming a low-contact-resistance ohmic interface with the underlying silicon source/drain diffusion regions of the access transistor (channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$).
6. Repeat cycles to achieve the target conformal Ti seed thickness.

### Step 3: MOCVD TiN Diffusion Barrier Deposition
1. Transfer wafer under high vacuum to the MOCVD chamber without vacuum break.
2. Introduce nitrogen-bearing metal-organic precursor chemistry (e.g., TDMAT / TDEAT with NH₃ co-reactant) with working chamber pressure dynamically throttled.
3. Deposit continuous stoichiometric TiN film to seal micro-voids, prevent fluorine attack during subsequent WF₆/W-plug chemical vapor deposition, and ensure adequate step coverage across high aspect ratio contact trenches.

### Step 4: In-Situ Thermal Nitridation & Forming Gas Anneal
1. Transfer substrate to the rapid thermal nitridation (RTN) station.
2. Expose the Ti/TiN bi-layer to an activated nitrogen/ammonia ambient to densify the film, eliminate residual carbon/halide impurities, and passivate grain boundaries against metal diffusion.
3. Conduct post-metallization forming gas anneal using $95\%\text{ N}_2 / 5\%\text{ H}_2$ gas mixture maintained at **400°C for 30 minutes** to repair interface states, ensure complete thermal nitridation, and stabilize sheet resistance.

### Step 5: Post-Deposition Metrology & Hand-Off
1. Verify film sheet resistance across array and test monitor pads.
2. Perform spectroscopic ellipsometry and X-ray reflectivity (XRR) to verify bi-layer thickness uniformity and density.
3. Transfer wafer to downstream Tungsten (W-plug) chemical vapor deposition module for storage node contact plug fill.

---

## 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Tolerance / Criteria | Verification Method |
| :--- | :--- | :--- | :--- |
| **Vacuum Chamber Base Pressure** | $< 2 \times 10^{-6}\text{ Torr}$ | Maximum threshold before deposition initiation | Calibrated Ionization / Cold-Cathode Gauge |
| **Post-Metal Anneal Conditions** | $400^\circ\text{C}$ for $30\text{ min}$ | Forming gas mixture: $95\%\text{ N}_2 / 5\%\text{ H}_2$ | Multi-zone thermocouple array & mass flow controller |
| **Interconnect Metallization Sheet Resistance ($R_s$)** | $R_s < 0.08\ \Omega/\Box$ | Upper limit post-anneal | 4-point collinear probe (FPP) |
| **Array Geometry Alignment** | $360\text{ nm} - 400\text{ nm}$ | Bitline/wordline pitch conformance ($L=180\text{ nm}$, $W=220\text{ nm}$) | In-line CD-SEM / cross-sectional STEM |

---

## 5. References & Literature Context
- *Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects*: Chamber base pressure $< 2 \times 10^{-6}\text{ Torr}$; forming gas $\text{N}_2/\text{H}_2\ 95/5$ anneal at $400^\circ\text{C}$ for $30\text{ minutes}$; sheet resistance target $R_s < 0.08\ \Omega/\Box$; Ar 99.999% purity.
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*: Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$; stacked capacitor over bitline (COB) with W-plug via; minimum capacitance 28 fF/cell; cell leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*: Bitline and wordline pitch $360\text{ nm} - 400\text{ nm}$; 1T1C $8\text{F}^2 / 6\text{F}^2$ architecture; high-k dielectric stack retention $> 64\text{ ms}$ at $85^\circ\text{C}$.

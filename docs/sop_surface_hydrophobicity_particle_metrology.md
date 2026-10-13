# Standard Operating Procedure (SOP)
## Surface Hydrophobicity and Post-Clean Particle Defect Metrology

- **Document ID:** SOP-DRAM180-WET-MET-004
- **Node / Technology:** 180nm Open-Source DRAM (DRAM Foundation VN)
- **Line Module:** High-K Gate Dielectric & Thin Film Thermal Oxidation Line / RCA Clean Conditioning
- **Classification:** Metrology / Quality Control Leaf SOP

---

### 1. Scope & Purpose
This procedure defines the machine-automated and manual inspection protocols for evaluating post-RCA surface conditioning, chemical passivation (H-termination vs. native oxide removal), and surface particle defect counts prior to critical gate oxidation (3.5 nm to 4.0 nm physical SiO2) on 180nm DRAM access transistor channels ($L = 180\text{ nm}, W = 220\text{ nm}$).

---

### 2. Workflow Architecture

```text
┌────────────────────────┐
│   Pre-Clean HF Dip /   │
│   SC-1 / SC-2 Rinse    │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  Sessile Drop Contact  │
│    Angle Goniometry    │
└────────────┬───────────┘
             │
             ▼
┌────────────◇───────────┐
│     Hydrophobicity     │
│   Check: θ > 75 deg    │
└────────────◇───────────┘
             │
             ├──────────────────────────────╮ [Fail: Residual Oxide / Hydrophilic]
        Pass │                              ▼
             │                 ┌────────────────────────┐
             │                 │  Rework: Native Oxide  │
             │                 │   Re-etch / Surface    │
             │                 │         Strip          │
             ▼                 └────────────────────────┘
┌────────────────────────┐
│     Laser Surface      │
│  Particle Scanning /   │
│     DLS Metrology      │
└────────────┬───────────┘
             │
             ▼
┌────────────◇───────────┐
│   LPD Particle Count   │
│    <= 10 at 0.18 um    │
└────────────◇───────────┘
             │
             ├──────────────────────────────╮ [Fail: Particulate Contamination]
        Pass │                              ▼
             │                 ┌────────────────────────┐
             │                 │  Megasonic DIW Rinse   │
             │                 │       & Re-scan        │
             ▼                 └────────────────────────┘
┌────────────────────────┐
│  Release to 850-900°C  │
│   Dry Gate Oxidation   │
└────────────────────────┘
```

---

### 3. Step-by-Step Operating Procedure

#### Step 1: Pre-Inspection Environmental & Wafer Handling
1. Unload 200mm product wafer carrier from the RCA clean station drying module (spin-rinse dry / Marangoni dry) within Class 1 cleanroom conditions.
2. Ensure wafer queue time between final dilute HF dip / rinse and dry oxidation tube furnace loading is strictly $< 4$ hours to prevent uncontrolled native oxide regrowth.

#### Step 2: Surface Hydrophobicity & H-Termination Verification (Goniometry)
1. Mount the control wafer onto the stage of an automated optical goniometer.
2. Dispense a calibrated sessile droplet ($1.0\ \mu\text{L} \pm 0.1\ \mu\text{L}$) of ultra-pure deionized water (UPW, resistivity $\ge 18.2\ \text{M}\Omega\cdot\text{cm}$) at 5 test sites (Center, North, South, East, West, with $5\text{ mm}$ edge exclusion).
3. Measure static water contact angle ($\theta$) using automated Young-Laplace optical edge-fitting.
4. **Pass Criteria**: $\theta \ge 75^\circ$, confirming uniform Si-H termination and complete removal of native silicon oxide. If $\theta < 75^\circ$, flag for pre-gate oxide re-clean.

#### Step 3: Post-Clean Particle & Light Point Defect (LPD) Scanning
1. Transfer wafer into the automated Darkfield Laser Surface Particle Scanner (wavelength $\lambda = 405\text{ nm}$ or $488\text{ nm}$).
2. Execute full-surface defect scanning calibrated against NIST-traceable polystyrene latex (PSL) spheres.
3. Quantify Light Point Defects (LPD) in the critical gate access channel defect bin: $\ge 180\text{ nm}$ ($0.18\ \mu\text{m}$).
4. Generate spatial defect density map; flag localized clusters or streak contamination.

#### Step 4: Lot Disposition & Gate Oxide Queue Hand-off
1. Verify acceptance metric compliance (Section 4).
2. If verified, transition lot into nitrogen-purged FOUP/SMIF pod for loading into the quartz tube furnace running dry oxidation at $850^\circ\text{C}-900^\circ\text{C}$.

---

### 4. Acceptance Criteria & Target Metrics

```text
Acceptance Criteria Target Thresholds
                          ┌────────────────────────────┐
                          │░░░░░                       │
Defect Density (cts/wafer)┤░░░░░                       │
                          │▒▒▒▒▒                       │
   Breakdown Field (MV/cm)┤▒▒▒▒▒                       │
        Ox Target EOT (nm)┤▓▓                          │
                          │▓▓                          │
       Contact Angle (deg)┤████████████████████████████│
                          │████████████████████████████│
                          └┬──────┬──────┬─────┬──────┬┘
                          0.0   18.8   37.5  56.2  75.0 
```

| Metric Parameter | Target Threshold | Measuring Technique / Tool | Physical Rationale & Downstream Impact |
| :--- | :--- | :--- | :--- |
| **Water Contact Angle ($\theta$)** | $\ge 75.0^\circ$ | Automated Sessile Drop Goniometry (UPW) | Assures complete oxide strip and robust Si-H passivation prior to thermal oxidation. |
| **Post-Clean Critical Particle Count** | $\le 10\text{ counts/wafer}$ ($\text{size} \ge 180\text{ nm}$) | Darkfield Laser Surface Scattering / Metrology | Prevents gate dielectric pinholes and localized breakdown in $L=180\text{ nm}, W=220\text{ nm}$ access gates. |
| **Pre-Oxide Residual Native Oxide** | $< 0.3\text{ nm}$ equivalent thickness | Spectroscopic Ellipsometry | Guarantees strict physical thickness targeting for $3.5\text{ nm}-4.0\text{ nm}$ gate oxide. |
| **Dielectric Breakdown Expectation** | $E_{\text{bd}} > 10.0\text{ MV/cm}$ | MOS Capacitor C-V / I-V Breakdown Testing | Direct consequence of particle-free interface ($D_{\text{it}} < 10^{10}\text{ cm}^{-2}\text{eV}^{-1}$). |

---

### 5. Citations & Verified Literature Context
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Transistor dimensions $L = 180\text{ nm}$, $W = 220\text{ nm}$; sub-threshold leakage limit $< 1\text{ fA/cell}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: Gate dielectric grown thermally via dry oxidation at $850^\circ\text{C}-900^\circ\text{C}$ targeting $\sim 3.5\text{ nm}$ physical thickness.
- **Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace**: Dry oxidation at $900^\circ\text{C}-1000^\circ\text{C}$ in pure dry $\text{O}_2$ producing gate dielectric with $E_{\text{bd}} > 10\text{ MV/cm}$, interface trap density $D_{\text{it}} < 10^{10}\text{ cm}^{-2}\text{eV}^{-1}$, and target gate dielectric thickness of $3.5\text{ nm}-4.0\text{ nm}$.

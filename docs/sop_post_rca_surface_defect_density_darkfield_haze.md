# SOP: Post-RCA Surface Defect Density Inspection & Darkfield Haze Mapping

- **Date**: 2026-10-12
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm)
- **Action Type**: Buy (Automated Darkfield Laser Surface Inspection & Haze Metrology Tooling)
- **Hierarchy**: 180nm Open-Source DRAM Chip > Standard RCA-1 & RCA-2 Wafer Cleaning Line > Post-Clean Particle & Hydrophobic Contact Angle Metrology > Post-RCA Surface Defect Density & Hydrophobic Passivation Mapping > Post-RCA Surface Defect Density Inspection & Darkfield Haze Mapping

---

## 1. Overview & Rationale
This Standard Operating Procedure (SOP) governs automated surface defect inspection, particle size classification, and full-wafer darkfield haze mapping following the standard RCA-1/RCA-2 wet clean sequence. 

In 180nm 1T1C DRAM architectures with stacked capacitor over bitline (COB) topologies, access transistors have gate length $L = 180\text{ nm}$ and width $W = 220\text{ nm}$, gate dielectric physical thickness of $\sim 3.5\text{ nm}$ (grown at $850^\circ\text{C}–900^\circ\text{C}$), and bitline/wordline pitch between $360\text{ nm}$ and $400\text{ nm}$. Particulate contamination or chemical micro-roughness (measured as optical haze) from ammonium hydroxide etching or unrinsed ionic residues can induce catastrophic gate oxide pinholes, shorten retention times ($> 64\text{ ms}$ target at $85^\circ\text{C}$), or violate the leakage budget of $< 1\text{ fA/cell}$.

```text
┌─────────────────────┐
│                     │
│   Wafer Loading &   │
│      Alignment      │
│                     │
└──────────┬──────────┘
           │
           │
           ▼
┌─────────────────────┐
│                     │
│   Laser Darkfield   │
│    Surface Scan     │
│                     │
└──────────┬──────────┘
           │
           │
           ▼
┌─────────────────────┐
│                     │
│   Particle Defect   │
│  Sizing & Counting  │
│                     │
└──────────┬──────────┘
           │
           │
           ▼
┌─────────────────────┐
│                     │
│  Surface Darkfield  │
│    Haze Mapping     │
│                     │
└──────────┬──────────┘
           │
           │
           ▼
┌─────────────────────┐
│                     │
│  Acceptance Gate:   │
│    Pass / Rework    │
│                     │
└─────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Tool Verification & Background Calibration
1. Verify the inspection tool chamber is purged with high-purity dry nitrogen ($N_2$) and the HEPA/ULPA filtration mini-environment meets ISO Class 1 cleanliness.
2. Load a certified Polystyrene Latex (PSL) calibration wafer (standard particle spheres calibrated at $180\text{ nm}$ and $360\text{ nm}$).
3. Perform optical detector auto-gain calibration and background optical noise check to ensure laser spot repeatability within $\pm 1.0\%$.

### Step 2: Post-RCA Wafer Transfer & Alignment
1. Receive wafer lot immediately following RCA-1 ($70^\circ\text{C}–80^\circ\text{C}$, 10–15 min), $18.2\text{ M}\Omega\cdot\text{cm}$ DI water rinse (3 min), 1:50 HF native oxide strip ($15–30\text{ s}$), RCA-2 ($70^\circ\text{C}–80^\circ\text{C}$, 10 min), and high-purity $N_2$ blow-dry.
2. Load wafer onto the vacuum chuck under robotic end-effector control with edge-grip handling to avoid contact within the active die area.
3. Perform non-contact optical notch/flat pre-alignment.

### Step 3: Dual-Channel Laser Darkfield Scanning
1. Initiate spiral or raster darkfield surface scan utilizing oblique laser illumination (e.g., solid-state laser at short wavelength).
2. Direct collected scattered light simultaneously to:
   - **Narrow/Wide Angle Darkfield Collectors**: To capture localized Rayleigh and Mie scattering from discrete surface particles.
   - **Integrating Sphere / Low-Angle Background Sensor**: To record low-frequency diffuse scattered light across the wafer for surface haze calculation.
3. Maintain edge exclusion boundary at $3\text{ mm}$ to eliminate bevel handling artifacts.

### Step 4: Defect Binning & Haze Map Generation
1. Classify discrete defect signals into bins:
   - Critical dimension threshold: $\ge 180\text{ nm}$ (matching access transistor gate length $L = 180\text{ nm}$).
   - Killer bridge/short threshold: $\ge 360\text{ nm}$ (matching minimal wordline/bitline pitch).
2. Generate full-wafer 2D haze intensity map expressed in parts-per-million (ppm), reflecting surface microroughness induced by SC-1 etching.

### Step 5: Lot Disposition & Routing
1. Evaluate wafer against Acceptance Criteria.
2. **Pass**: Route wafer directly to thermal oxidation furnace for dry gate oxidation ($850^\circ\text{C}–900^\circ\text{C}$, $\sim 3.5\text{ nm}$ $\text{SiO}_2$) or high-$k$ dielectric deposition.
3. **Fail (Defect Density Exceeded)**: Flag for re-cleaning via RCA-1/QDR line.
4. **Fail (Haze / Micro-roughness Exceeded)**: Hold lot for wet bench chemical bath concentration inspection (excessive $\text{NH}_4\text{OH}$ etch rate).

---

## 3. Acceptance Criteria Target Metrics

| Parameter / Metric | Target Value | Physical Units | Tolerance / Constraint | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Minimum Defect Sizing Sensitivity** | $\le 180$ | $\text{nm}$ | $\pm 5\%$ PSL equivalent size | Calibration check with $180\text{ nm}$ PSL reference standard |
| **Surface Defect Density ($\ge 180\text{ nm}$)** | $\le 0.10$ | $\text{defects/cm}^2$ | Max allowable across wafer surface | Automated darkfield defect counter ($3\text{ mm}$ edge exclusion) |
| **Critical Pitch Killer Defect Count ($\ge 360\text{ nm}$)** | $0$ | $\text{defects/wafer}$ | Strict zero-tolerance for defects $\ge$ pitch ($360–400\text{ nm}$) | Darkfield defect binning map |
| **Background Darkfield Haze Level** | $\le 0.15$ | $\text{ppm}$ | Full-wafer average; non-uniformity $\le 5.0\%$ ($3\sigma$) | Integrating collector haze channel |
| **Pre-Clean Resistivity Confirmation** | $18.2$ | $\text{M}\Omega\cdot\text{cm}$ | $\ge 18.0\text{ M}\Omega\cdot\text{cm}$ at $25^\circ\text{C}$ | In-line DI rinse dump resistivity sensor |

---

## 4. References & Related Literature Context
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Transistor dimensions ($L = 180\text{ nm}$, $W = 220\text{ nm}$), stacked capacitor W-plug contact, ONO/$\text{Ta}_2\text{O}_5$/$\text{Al}_2\text{O}_3$ high-$k$ stack ($\kappa > 15$, capacitance budget $\ge 28\text{ fF/cell}$), and leakage limit ($< 1\text{ fA/cell}$ at $85^\circ\text{C}$).
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: $1\text{T}1\text{C}$ architecture, $8F^2/6F^2$ cell layout, bitline/wordline pitch ($360\text{ nm}–400\text{ nm}$), capacitor capacitance ($25–30\text{ fF/cell}$ for $> 64\text{ ms}$ retention at $85^\circ\text{C}$), and gate dielectric thermal dry oxidation at $850^\circ\text{C}–900^\circ\text{C}$ ($\sim 3.5\text{ nm}$ physical thickness).
- **Standard RCA-1 and RCA-2 Silicon Wafer Cleaning Procedure**: SC-1 ($5:1:1\text{ DI } \text{H}_2\text{O}:\text{NH}_4\text{OH}:\text{H}_2\text{O}_2$ at $70^\circ\text{C}–80^\circ\text{C}$, $10–15\text{ min}$), intermediate $18.2\text{ M}\Omega\cdot\text{cm}$ DI water rinse ($3\text{ min}$), DHF $1:50\text{ HF}:\text{H}_2\text{O}$ dip ($15–30\text{ s}$), SC-2 ($6:1:1\text{ DI } \text{H}_2\text{O}:\text{HCl}:\text{H}_2\text{O}_2$ at $70^\circ\text{C}–80^\circ\text{C}$, $10\text{ min}$), and high-purity $N_2$ blow-dry.

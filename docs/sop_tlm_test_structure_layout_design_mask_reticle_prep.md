# Standard Operating Procedure (SOP): TLM Test Structure Layout Design & Mask Reticle Preparation

- **Document ID:** SOP-MET-TLM-001
- **Process Generation:** Gen 3 (180nm Open-Source DRAM Chip / BEOL Metallization & Metrology)
- **Action Type:** Make
- **Domain:** Circuit Design / Layout & Reticle Preparation

---

## 1. Overview & Scope

This Standard Operating Procedure defines the exact methodology for layout design, Design Rule Checking (DRC), and mask reticle preparation of Transmission Line Measurement (TLM) test vehicle structures. The test structures are integrated into scribe-line drop-in areas or dedicated test reticles for the 180nm DRAM process to extract specific contact resistivity ($\rho_c$), contact resistance ($R_c$), diffusion sheet resistance ($R_s$), and transfer length ($L_T$) between BEOL metallization (Metal 1) and active doped silicon diffusion regions.

---

## 2. Process Workflow & Visual Layout Architecture

```text
┌───────────────────────┐
│                       │
│   Layout Definition   │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  GDSII DRC & Reticle  │
│         Prep          │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Mask Fabrication    │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│     Kelvin Probe      │
│      Measurement      │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Regression & rho_c   │
│      Extraction       │
│                       │
└───────────────────────┘
```

### TLM Structure Gap Geometry (Pad Spacing Metric)

```text
                   TLM Pad Spacing Gaps (um)            
      ┌────────────────────────────────────────────────┐
      │■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■│
d=80um┤■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■│
      │█████████████████████████                       │
d=40um┤█████████████████████████                       │
      │▓▓▓▓▓▓▓▓▓▓▓▓▓                                   │
d=20um┤▓▓▓▓▓▓▓▓▓▓▓▓▓                                   │
      │▒▒▒▒▒▒▒                                         │
d=10um┤▒▒▒▒▒▒▒                                         │
      │░░░░                                            │
 d=5um┤░░░░                                            │
      │░░░░                                            │
      └┬───────────┬───────────┬──────────┬───────────┬┘
       0          20          40         60          80 
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Active Diffusion Stripe Definition
1. Open CAD layout editor (e.g., KLayout / Magic) configured with the 180nm PDK tech file.
2. Define a continuous active diffusion channel (DIFF/OD layer) running horizontally.
   - Channel Width ($W$): Exactly $100\,\mu\text{m}$.
   - Channel Length: Sized to accommodate all 6 contact pads and the intervening spaces ($L_{total} = (6 \times 50\,\mu\text{m}) + (5 + 10 + 20 + 40 + 80\,\mu\text{m}) = 300\,\mu\text{m} + 155\,\mu\text{m} = 455\,\mu\text{m}$).
   - Set isolation boundaries via STI (Shallow Trench Isolation) with minimum PDK enclosure margin $\ge 1.0\,\mu\text{m}$.

### Step 2: Contact Pad Geometry & Array Placement
1. Draw identical rectangular contact pads on the Metal 1 layer:
   - Pad Width ($W$): $100\,\mu\text{m}$ (aligned identically to the diffusion width to prevent current fringing).
   - Pad Length ($L_{pad}$): $50\,\mu\text{m}$.
2. Array 6 identical contact pads linearly along the diffusion stripe with progressively increasing edge-to-edge separation distances ($d$):
   - Gap 1: $d_1 = 5\,\mu\text{m}$
   - Gap 2: $d_2 = 10\,\mu\text{m}$
   - Gap 3: $d_3 = 20\,\mu\text{m}$
   - Gap 4: $d_4 = 40\,\mu\text{m}$
   - Gap 5: $d_5 = 80\,\mu\text{m}$
3. Populate contact cut (W-plug / CONT layer) arrays across each contact pad interface:
   - High-density matrix of minimum-size contacts ($0.22\,\mu\text{m} \times 0.22\,\mu\text{m}$ with standard pitch) ensuring uniform current distribution across $W = 100\,\mu\text{m}$.

### Step 3: Probe Pad & Kelvin Sensing Routing
1. For each of the 6 contact regions, route dual micro-probe landing pads (Force and Sense) to enable 4-point Kelvin electrical characterization:
   - Probe landing pad dimensions: $100\,\mu\text{m} \times 100\,\mu\text{m}$ Al squares (compatible with both micro-probe needles and subsequent wire bonding verification).
   - Route using top metallization or Metal 2 with low parasitic resistance interconnect tracks ($W_{track} \ge 10\,\mu\text{m}$).

### Step 4: DRC/LVS Verification & Optical Proximity Reticle Preparation
1. Run DRC (Design Rule Check) against 180nm BEOL rules:
   - Confirm Metal 1 minimum spacing and enclosure of contacts.
   - Verify no floating diffusion or antenna rule violations.
2. Generate GDSII/OASIS stream format with grid snap set to $0.005\,\mu\text{m}$ ($5\,\text{nm}$).
3. Perform reticle layout assembly:
   - Place test cell within scribe lines or primary MPW test drop-in zone.
   - Apply Optical Proximity Correction (OPC) and sub-resolution assist features (SRAF) to pad corners to prevent corner rounding on mask chrome plates.
   - Inspect reticle mask data using optical/electron-beam mask data inspection verification tools.

### Step 5: Test Execution & Parameter Extraction Math
1. Perform 4-point DC current injection ($I_{force} = 1.0\,\text{mA}$) and measure voltage drop ($V_{sense}$) across adjacent pad pairs ($d = 5, 10, 20, 40, 80\,\mu\text{m}$).
2. Calculate total measured resistance for each gap:
   $$R_T = \frac{V_{sense}}{I_{force}} = 2 R_c + \left(\frac{R_s}{W}\right) d$$
3. Perform linear least-squares regression of $R_T$ versus $d$:
   - **Slope ($m$):** $m = \frac{R_s}{W} \implies R_s = m \times W$
   - **Y-intercept ($b$ at $d=0$):** $b = 2 R_c \implies R_c = \frac{b}{2}$
   - **X-intercept ($-2 L_T$):** $L_T = -\frac{b}{2m}$
   - **Specific Contact Resistivity ($\rho_c$):**
     $$\rho_c = R_c \times W \times L_T = R_s \times L_T^2 \quad [\Omega \cdot \text{cm}^2]$$

---

## 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Tolerance / Limit | Exact Physical Unit | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Contact Pad Width ($W$)** | `100.0` | $\pm 0.05$ | $\mu\text{m}$ | CD-SEM metrology / Optical layout DRC |
| **Contact Pad Length ($L_{pad}$)** | `50.0` | $\pm 0.05$ | $\mu\text{m}$ | CD-SEM metrology / Optical layout DRC |
| **Spacing Gap Progression ($d$)** | `[5, 10, 20, 40, 80]` | $\pm 0.02$ | $\mu\text{m}$ | Critical Dimension SEM (CD-SEM) |
| **Linear Regression Correlation ($R^2$)** | $\ge 0.998$ | Min $0.995$ | Unitless ($R^2$) | Linear regression fit ($R_T$ vs $d$) |
| **Specific Contact Resistivity ($\rho_c$)** | $\le 1.0 \times 10^{-6}$ | Process Spec | $\Omega \cdot \text{cm}^2$ | TLM Extraction Calculation |

---

## 5. References & Literature Context

- **Source:** *Transmission Line Measurement (TLM) for Specific Contact Resistivity*
  - Defines contact pad dimensions ($W = 100\,\mu\text{m}$, $L_{pad} = 50\,\mu\text{m}$), gap intervals ($d = 5, 10, 20, 40, 80\,\mu\text{m}$), and regression parameter relations:
    $$R_T = 2 R_c + (R_s / W) \cdot d, \quad \rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2 \, [\Omega \cdot \text{cm}^2]$$
- **Source:** *Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging*
  - Defines bonding pad dimensions ($100\,\mu\text{m} \times 100\,\mu\text{m}$ Al pads).
- **Source:** *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
  - Establishes 180nm design rules and baseline BEOL contact integration boundaries.

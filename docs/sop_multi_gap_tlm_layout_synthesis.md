# Standard Operating Procedure (SOP): Multi-Gap TLM Test Structure & Probe Pad Array Layout Synthesis

- **Task Hierarchy**: `180nm Open-Source DRAM Chip` > `BEOL Multi-Layer Metallization, Wafer Sort & Packaging` > `Electrical Die Sort (EDS) & Micro-Cantilever Probe Card Automated Testing` > `Die Pad Frame & TLM Array Interface Layout Optimization` > `Multi-Gap TLM Test Structure & Probe Pad Array Layout Synthesis`
- **Target Node**: 180nm CMOS DRAM Process (Gen 3)
- **Action Type**: Make / Physical Layout Synthesis
- **Date**: 2026-10-15
- **Status**: Implemented

---

## 1. Objective & Scope
This Standard Operating Procedure (SOP) defines the physical layout synthesis, geometry parameters, design rule checks (DRC), and parameter extraction methodology for fabricating a Multi-Gap Transmission Line Measurement (TLM) test vehicle. The synthesized structure allows Electrical Die Sort (EDS) micro-cantilever probe cards to directly extract diffusion sheet resistance ($R_s$), contact resistance ($R_c$), transfer length ($L_T$), and specific contact resistivity ($\rho_c$) across doped silicon diffusion and metal interconnect interfaces.

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│     Step 1: Active     │
│    Diffusion Stripe    │
│       Definition       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Step 2: Contact     │
│       Opening &        │
│     Metallization      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Step 3: Probe Pad    │
│   Array Integration    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Step 4: Layout     │
│  Verification DRC/LVS  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Step 5: EDS 4-Wire   │
│       Resistance       │
│       Extraction       │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Layout Synthesis Procedure

### Step 1: Active Diffusion Layer Definition
1. Draw a continuous rectangular active diffusion stripe on the baseline substrate/well with a fixed layout width:
   $$W = 100\,\mu\text{m}$$
2. Set the longitudinal length of the diffusion stripe to accommodate six contact pads plus all spacing gaps and end-enclosures:
   $$\text{Length}_{\text{diffusion}} = (6 \times L_{\text{pad}}) + \sum d_i + 2 \times L_{\text{enc}} = (6 \times 50\,\mu\text{m}) + (5 + 10 + 20 + 40 + 80)\,\mu\text{m} + 2 \times 5\,\mu\text{m} = 465\,\mu\text{m}$$

### Step 2: Contact Opening & Metallization Placement
1. Synthesize 6 identical rectangular contact pads directly atop the diffusion stripe with dimensions:
   - Contact pad width: $W = 100\,\mu\text{m}$
   - Contact pad length: $L_{\text{pad}} = 50\,\mu\text{m}$
2. Place the pads linearly along the active diffusion stripe with progressively increasing inter-pad gaps ($d$):
   - Gap 1: $d_1 = 5\,\mu\text{m}$
   - Gap 2: $d_2 = 10\,\mu\text{m}$
   - Gap 3: $d_3 = 20\,\mu\text{m}$
   - Gap 4: $d_4 = 40\,\mu\text{m}$
   - Gap 5: $d_5 = 80\,\mu\text{m}$

```text
                   TLM Inter-Pad Spacings d (um)        
           ┌───────────────────────────────────────────┐
           │■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■│
Gap d=80 um┤■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■│
           │██████████████████████                     │
Gap d=40 um┤██████████████████████                     │
Gap d=20 um┤▓▓▓▓▓▓▓▓▓▓▓▓                               │
           │▓▓▓▓▓▓▓▓▓▓▓▓                               │
Gap d=10 um┤▒▒▒▒▒▒                                     │
           │▒▒▒▒▒▒                                     │
 Gap d=5 um┤░░░░                                       │
           │░░░░                                       │
           └┬──────────┬─────────┬──────────┬─────────┬┘
            0         20        40         60        80 
```

### Step 3: Probe Pad Array Interface Routing
1. Connect each of the 6 contact regions to standard micro-cantilever probe pads on top-level metallization (Metal 1 / Metal 2 / Top Metal) using low-resistance interconnect routing and redundant via arrays.
2. Maintain identical routing trace geometry for all 6 pads to eliminate differential parasitics during 4-point Kelvin probe testing.

### Step 4: Physical Verification (DRC & LVS)
1. Run Design Rule Checking (DRC) to ensure metal spacing, contact enclosure inside diffusion, and minimum density rules meet the 180nm PDK specifications.
2. Execute Layout Versus Schematic (LVS) verifying 6 distinct probe terminals contacting the active diffusion segment.

### Step 5: Test Execution & Parameter Extraction
1. Measure the total resistance $R_T$ between every pair of adjacent pads using 4-wire Kelvin sensing:
   $$R_T = 2 \cdot R_c + \left(\frac{R_s}{W}\right) \cdot d$$
2. Perform linear regression of $R_T$ versus pad spacing $d$:
   - **Slope**: $\text{Slope} = \frac{R_s}{W} \implies R_s = \text{Slope} \times W$
   - **Y-intercept**: $\text{Intercept}_Y = 2 \cdot R_c \implies R_c = \frac{\text{Intercept}_Y}{2}$
   - **X-intercept**: $\text{Intercept}_X = -2 \cdot L_T \implies L_T = -\frac{\text{Intercept}_X}{2}$
   - **Specific Contact Resistivity**: $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2 \quad [\Omega\cdot\text{cm}^2]$

---

## 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Physical Unit | Measurement & Extraction Method |
| :--- | :--- | :--- | :--- |
| **Contact Pad Width ($W$)** | $100.0 \pm 0.1$ | $\mu\text{m}$ | Optical / CD-SEM metrology on synthesized mask layout |
| **Contact Pad Length ($L_{\text{pad}}$)** | $50.0 \pm 0.1$ | $\mu\text{m}$ | Optical / CD-SEM metrology on synthesized mask layout |
| **Inter-Pad Spacing Progression ($d$)** | $[5, 10, 20, 40, 80] \pm 0.05$ | $\mu\text{m}$ | High-resolution in-line SEM / layout DRC spacing check |
| **Specific Contact Resistivity ($\rho_c$) Extraction** | Extracted via $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2$ | $\Omega\cdot\text{cm}^2$ | Linear regression of $R_T$ vs $d$ across 5 gap intervals |

---

## 5. Literature & Context Citations
1. **Transmission Line Measurement (TLM) for Specific Contact Resistivity**:
   - Contact pad dimensions: width $W = 100\,\mu\text{m}$, length $L_{\text{pad}} = 50\,\mu\text{m}$.
   - Progressively increasing gaps: $d = 5\,\mu\text{m}, 10\,\mu\text{m}, 20\,\mu\text{m}, 40\,\mu\text{m}, 80\,\mu\text{m}$.
   - Model formulation: $R_T = 2 \cdot R_c + (R_s / W) \cdot d$.
   - Parameter extraction formulas: $\text{Slope} = R_s / W$, Y-intercept $= 2 \cdot R_c$, X-intercept $= -2 \cdot L_T$, $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2$ in $\Omega\cdot\text{cm}^2$.

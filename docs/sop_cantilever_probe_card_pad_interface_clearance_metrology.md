# Standard Operating Procedure (SOP): Cantilever Probe Card Pad Interface Clearance & Metrology Inspection Verification

- **Task Hierarchy**: `180nm Open-Source DRAM Chip` > `BEOL Multi-Layer Metallization, Wafer Sort & Packaging` > `Electrical Die Sort (EDS) & Micro-Cantilever Probe Card Automated Testing` > `Custom Micro-Cantilever Probe Card Design & Pad Interface Layout` > `Die Pad Frame & TLM Array Interface Layout Optimization` > `Cantilever Probe Card Pad Interface Clearance & Metrology Inspection Verification`
- **Target Node**: 180nm CMOS DRAM Process (Gen 3)
- **Action Type**: Make / Metrology & Verification
- **Date**: 2026-10-15
- **Status**: Implemented

---

## 1. Objective & Scope
This Standard Operating Procedure (SOP) specifies the physical metrology, touchdown clearance verification, and contact inspection protocol for custom micro-cantilever probe cards interfacing with die pad frames and Transmission Line Measurement (TLM) test structures on 180nm CMOS DRAM wafers. This procedure ensures scrub mark centering, prevents probe-to-passivation edge clipping across multi-gap TLM pads, verifies tip planarity and scrub length, and qualifies contact integrity prior to automated wafer sort and parameter extraction.

---

## 2. Process Flow Architecture

```text
┌────────────────────────┐
│                        │
│  1. Wafer Alignment &  │
│     Pad Coordinate     │
│        Mapping         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  2. Micro-Cantilever   │
│  Probe Card Planarity  │
│      & Alignment       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     3. Z-Overdrive     │
│  Touchdown Execution   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    4. Scrub Mark &     │
│   Clearance Optical    │
│       Metrology        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   5. TLM Electrical    │
│     Verification &     │
│       Resistance       │
│       Extraction       │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Wafer Alignment & TLM Pad Coordinate Calibration
1. Load the 180nm DRAM wafer onto the automated prober chuck.
2. Perform global theta and pattern-recognition fine alignment using fiducial marks on the die peripheral frame.
3. Establish origin $(X_0, Y_0)$ on the TLM test structure contact pad array featuring pad dimensions:
   - Contact pad width: $W = 100\,\mu\text{m}$
   - Contact pad length: $L_{\text{pad}} = 50\,\mu\text{m}$
   - Successive inter-pad spacing gaps: $d_1 = 5\,\mu\text{m}$, $d_2 = 10\,\mu\text{m}$, $d_3 = 20\,\mu\text{m}$, $d_4 = 40\,\mu\text{m}$, and $d_5 = 80\,\mu\text{m}$.

```text
             TLM Pad Geometry & Pitch Dimensions (um)   
           ┌───────────────────────────────────────────┐
           │◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆        │
Gap d5 (um)┤◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆        │
           │●●●●●●●●●●●●●●●●●●                         │
Gap d4 (um)┤●●●●●●●●●●●●●●●●●●                         │
           │■■■■■■■■■                                  │
Gap d3 (um)┤■■■■■■■■■                                  │
Gap d2 (um)┤█████                                      │
           │█████                                      │
Gap d1 (um)┤▓▓▓                                        │
           │▓▓▓                                        │
 W_pad (um)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
           │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
 L_pad (um)┤░░░░░░░░░░░░░░░░░░░░░░                     │
           │░░░░░░░░░░░░░░░░░░░░░░                     │
           └┬──────────┬─────────┬──────────┬─────────┬┘
            0         25        50         75       100 
```

### Step 2: Cantilever Probe Card Planarity & Visual Alignment
1. Mount the custom micro-cantilever probe card onto the prober test head interface.
2. Using the bottom-looking optics, verify cantilever probe tip planarity across all tips (target: $\le 10\,\mu\text{m}$ vertical tip-to-tip coplanarity variance).
3. Align the needle probe tips with the center of each $100\,\mu\text{m} \times 50\,\mu\text{m}$ aluminum/copper top metal pad.
4. Verify edge clearance: Maintain an initial nominal offset $\ge 15\,\mu\text{m}$ from the passivation opening edge along the longitudinal axis ($L_{\text{pad}} = 50\,\mu\text{m}$) and $\ge 25\,\mu\text{m}$ along the transverse axis ($W = 100\,\mu\text{m}$).

### Step 3: Controlled Z-Overdrive Touchdown
1. Set initial electrical contact search velocity to $100\,\mu\text{m}/\text{s}$ until first contact touch sense is registered.
2. Apply controlled vertical Z-overdrive of $50\,\mu\text{m}$ to $75\,\mu\text{m}$ to induce lateral tip scrubbing through native surface aluminum oxide.
3. Ensure cantilever scrub direction runs strictly along the pad length axis ($L_{\text{pad}} = 50\,\mu\text{m}$), parallel to the active diffusion stripe.

### Step 4: Optical Metrology & Scrub Mark Clearance Inspection
1. Retract prober chuck in Z and translate high-resolution automated inspection camera ($50\times / 100\times$ optical magnification) over the contacted pads.
2. Measure scrub mark dimensions:
   - Scrub mark length ($L_{\text{scrub}}$): must measure between $10\,\mu\text{m}$ and $20\,\mu\text{m}$.
   - Scrub mark width ($W_{\text{scrub}}$): nominal $3\,\mu\text{m}$ to $6\,\mu\text{m}$.
3. Verify edge clearance and margin:
   - Residual clearance between scrub mark perimeter and passivation boundary: $\ge 10\,\mu\text{m}$.
   - Zero scrub mark breakout beyond metal pad boundary into the inter-pad gaps ($d = 5\,\mu\text{m}$ to $80\,\mu\text{m}$).
4. Inspect passivation integrity: Confirm zero cracking, micro-delamination, or particulate bridging across the inter-pad gaps.

### Step 5: TLM Contact Integrity & Resistance Verification
1. Perform 4-wire Kelvin resistance measurement ($R_T$) across adjacent pad pairs separated by spacing gaps $d_1 = 5\,\mu\text{m}$, $d_2 = 10\,\mu\text{m}$, $d_3 = 20\,\mu\text{m}$, $d_4 = 40\,\mu\text{m}$, and $d_5 = 80\,\mu\text{m}$.
2. Construct linear regression:
   $$R_T = 2 \cdot R_c + \left(\frac{R_s}{W}\right) \cdot d$$
   where $W = 100\,\mu\text{m}$.
3. Extract physical TLM metrics:
   - Slope yields $R_s / W$ (providing sheet resistance $R_s$).
   - Y-intercept at $d = 0$ yields contact resistance $2 \cdot R_c$.
   - X-intercept yields transfer length $-2 \cdot L_T$.
   - Calculate specific contact resistivity: $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2$ $[\Omega \cdot \text{cm}^2]$.

---

## 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Target Value | Tolerance / Limit | Exact Physical Unit | Measurement Method |
| :--- | :--- | :--- | :--- | :--- |
| **Probe Tip Scrub Mark Length ($L_{\text{scrub}}$)** | $15.0$ | $10.0$ to $20.0$ | $\mu\text{m}$ | Automated Optical Metrology (AOI) |
| **Passivation Boundary Edge Clearance** | $\ge 10.0$ | $\text{Min } 8.0$ | $\mu\text{m}$ | Automated Optical Metrology (AOI) |
| **Cantilever Tip Coplanarity Variance** | $\le 8.0$ | $\text{Max } 10.0$ | $\mu\text{m}$ | Prober Optical Non-Contact Profilometry |
| **TLM Regression Linearity ($R^2$)** | $\ge 0.995$ | $\text{Min } 0.990$ | Dimensionless | 4-Wire DC Resistance Fit ($d=5\text{--}80\,\mu\text{m}$) |

---

## 5. Verified Context References
- **Transmission Line Measurement (TLM) for Specific Contact Resistivity**:
  - Rectangular contact pads: $W = 100\,\mu\text{m}$, $L_{\text{pad}} = 50\,\mu\text{m}$.
  - Progressively increasing gaps: $d = 5\,\mu\text{m}, 10\,\mu\text{m}, 20\,\mu\text{m}, 40\,\mu\text{m}, 80\,\mu\text{m}$.
  - Resistance formulation and parameter extraction: $R_T = 2 \cdot R_c + (R_s / W) \cdot d$, with slope $= R_s / W$, Y-intercept $= 2 \cdot R_c$, X-intercept $= -2 \cdot L_T$, and $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2$ $[\Omega \cdot \text{cm}^2]$.
- **180nm DRAM Cell Layout Topology & Capacitor Engineering**:
  - Access transistor geometry $L = 180\,\text{nm}$, $W = 220\,\text{nm}$.
  - Storage capacitor retention target $> 64\,\text{ms}$ at $85^\circ\text{C}$ with $C_{\text{cell}} \ge 25\text{--}30\,\text{fF}$.

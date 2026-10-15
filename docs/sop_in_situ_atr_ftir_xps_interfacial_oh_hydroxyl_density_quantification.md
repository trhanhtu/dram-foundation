# SOP: In-Situ ATR-FTIR & XPS Interfacial -OH Hydroxyl Density Quantification

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Generation**: Gen 3 (nm)
- **Action Type**: Make
- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm CMOS Commercial MPW Tapeout & PDK Implementation [Foundry Tapeout & PDK] > 3D High-Aspect-Ratio Crown Capacitor ALD Dielectric & Metal Electrode Deposition [Nanofabrication] > ALD Al2O3/Ta2O5 High-k Dielectric Stack Recipe Optimization & Deposition [Thin Film Deposition] > ALD Precursor Metering & Substrate In-Situ Ozone Pre-Clean Recipe Calibration [Thin Film Deposition] > Pre-ALD Interfacial Hydroxyl Density & Surface Cleanliness Metrology [Metrology] > In-Situ ATR-FTIR & XPS Interfacial -OH Hydroxyl Density Quantification [Metrology]

---

## 1. Overview & Rationale

In the 180nm open-source DRAM architecture (DRAM Foundation VN), memory cells transition toward $8F^2$ and $6F^2$ folded bitline topologies using a Stacked Capacitor Over Bitline (COB) architecture. The storage node consists of a 3D crown-shaped metal-insulator-metal (MIM) or polysilicon capacitor erected above the drain contact through a tungsten plug (W-plug). To achieve the required capacitance budget of $C_{\text{cell}} \ge 25\text{ to }30\text{ fF}$ (ensuring refresh retention time $> 64\text{ ms}$ at $85^\circ\text{C}$ and leakage current $< 1\text{ fA/cell}$ against alpha-particle soft errors), the storage node employs an atomic layer deposition (ALD) high-$\kappa$ dielectric stack consisting of $\text{Al}_2\text{O}_3 / \text{Ta}_2\text{O}_5$ providing an effective dielectric constant $\kappa > 15$ with an equivalent oxide thickness (EOT) around $3\text{ to }4\text{ nm}$.

ALD of metal oxides (such as $\text{Al}_2\text{O}_3$ from trimethylaluminum [TMA] and $\text{Ta}_2\text{O}_5$ from tantalum ethoxide or halide precursors) is strictly self-terminating and critically dependent upon the initial density of surface reactive hydroxyl ($-\text{OH}$) functional groups. Insufficient or non-uniform interfacial hydroxyl termination ($< 10^{14}\text{ sites/cm}^2$) leads to severe ALD nucleation incubation delays, island growth, pinhole defects, and elevated dielectric leakage current exceeding $1\text{ fA/cell}$. Conversely, adventitious carbon contamination ($> 3\text{ at}\%$) inhibits precursor chemisorption and induces defect states that degrade the $\kappa > 15$ performance.

This Standard Operating Procedure (SOP) governs the in-situ metrology protocol combining Attenuated Total Reflection Fourier-Transform Infrared Spectroscopy (ATR-FTIR) and X-ray Photoelectron Spectroscopy (XPS) within a cluster-connected ultra-high vacuum (UHV) analysis module. This enables direct quantitative tracking of surface $-\text{OH}$ density and carbon contamination following in-situ ozone ($\text{O}_3$) pre-clean prior to high-$\kappa$ dielectric deposition.

```text
┌────────────────────────┐
│                        │
│  Wafer Ingestion from  │
│    Post-Ozone Clean    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    In-Situ Transfer    │
│    Chamber Base P <    │
│       2e-6 Torr        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   ATR-FTIR Spectrum    │
│      Acquisition       │
│     3000-3800 cm-1     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Peak Deconvolution &  │
│      Isolated -OH      │
│   Integral 3740 cm-1   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Monochromatic Al-Ka   │
│  XPS Core-Level Scan   │
│       O1s & C1s        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  O1s Deconvolution &   │
│    Hydroxyl Density    │
│     Quantification     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│       Pass/Fail        │
│  Disposition for ALD   │
│      Al2O3/Ta2O5       │
│    Dielectric Stack    │
│                        │
└────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Vacuum Chamber Preparation & In-Situ Transfer
1. Confirm the cluster transfer module and analysis chambers are pumped down to a high-vacuum base pressure below $2.0 \times 10^{-6}\text{ Torr}$ via turbomolecular and cryopump systems to eliminate ambient moisture and hydrocarbon re-contamination.
2. Maintain high-purity nitrogen ($\text{N}_2 \ge 99.999\%$) buffer flow in isolation valves if transferring under inert purge.
3. Transfer the 200mm test/monitor wafer directly from the ozone pre-clean chamber into the in-situ metrology analysis stage using the automated robotic transfer arm. Avoid ambient air exposure.

### Step 2: In-Situ ATR-FTIR Spectroscopic Measurement
1. Dock the wafer surface against the infrared internal reflection element (Ge or ZnSe ATR crystal prism) using pneumatic micro-force control ($15 \pm 2\text{ N}$) to establish reproducible evanescent optical coupling without mechanical fracture of 3D crown capacitor structures.
2. Purge the FTIR spectrometer optical path with dry nitrogen gas ($\text{H}_2\text{O} < 1\text{ ppm}$, $\text{CO}_2 < 1\text{ ppm}$) at a flow rate of $10\text{ slm}$.
3. Acquire background interferogram across the $600\text{ cm}^{-1}$ to $4000\text{ cm}^{-1}$ mid-infrared spectral range at $4\text{ cm}^{-1}$ spectral resolution over 128 co-added scans.
4. Collect sample absorption spectrum focusing on the stretching vibrational band of surface hydroxyl species:
   - Isolated silanol/metal-hydroxyl groups ($\nu_{-\text{OH},\text{ isolated}}$) centered at $3740\text{ cm}^{-1}$ to $3745\text{ cm}^{-1}$.
   - Hydrogen-bonded hydroxyl network ($\nu_{-\text{OH},\text{ bonded}}$) spanning $3200\text{ cm}^{-1}$ to $3600\text{ cm}^{-1}$.
5. Perform linear baseline subtraction between $3000\text{ cm}^{-1}$ and $3800\text{ cm}^{-1}$ and integrate the absorbance peak area ($A_{-\text{OH}}$).

### Step 3: In-Situ XPS Core-Level Surface Analysis
1. Transfer wafer onto the XPS analysis stage under ultra-high vacuum ($P \le 5.0 \times 10^{-9}\text{ Torr}$).
2. Power up the monochromatic $\text{Al } K_\alpha$ X-ray source ($h\nu = 1486.6\text{ eV}$) operating at $15\text{ kV}$ and $150\text{ W}$ ($10\text{ mA}$ emission). Set beam spot diameter to $400\text{ }\mu\text{m}$.
3. Calibrate binding energy scale against the adventitious carbon $\text{C } 1s$ peak at $284.8\text{ eV}$ or metallic substrate core level.
4. Record high-resolution core-level spectra with pass energy $20\text{ eV}$ and step size $0.05\text{ eV}$:
   - **$\text{O } 1s$ Region**: $526\text{ eV} - 536\text{ eV}$ (15 sweeps).
   - **$\text{C } 1s$ Region**: $280\text{ eV} - 292\text{ eV}$ (10 sweeps).
   - **Substrate Metal/Si Region**: ($\text{Si } 2p$ at $99–104\text{ eV}$, $\text{Ti } 2p$, or $\text{Ta } 4f$) to normalize sampling volume.
5. Deconvolve the $\text{O } 1s$ spectral envelope using Shirley background subtraction and Voigt (Gaussian-Lorentzian 70:30) peak fitting:
   - Lattice oxide oxygen peak ($\text{M}-\text{O}-\text{M}$ or $\text{Si}-\text{O}-\text{Si}$) at $530.2 \pm 0.3\text{ eV}$.
   - Interfacial surface hydroxyl peak ($\text{M}-\text{OH}$ / $\text{Si}-\text{OH}$) shifted to $531.8 \pm 0.3\text{ eV}$.
   - Physisorbed molecular water / organic oxygen ($\text{C}-\text{O}$) at $533.0 \pm 0.4\text{ eV}$.

### Step 4: Hydroxyl Density Calculation & Contamination Verification
1. Calculate the fractional hydroxyl coverage ($\chi_{-\text{OH}}$) from the deconvolved $\text{O } 1s$ peak area:
   $$\chi_{-\text{OH}} = \frac{I_{\text{OH}}}{I_{\text{lattice}} + I_{\text{OH}}}$$
2. Convert into absolute areal hydroxyl site density ($\sigma_{-\text{OH}}$) using the known substrate surface atomic packing density and inelastic mean free path ($\lambda_{\text{IMFP}} \approx 2.1\text{ nm}$ for $\text{O } 1s$ photoelectrons):
   $$\sigma_{-\text{OH}} = \rho_{\text{surf}} \cdot \chi_{-\text{OH}} \cdot \left[1 - \exp\left(-\frac{d}{\lambda_{\text{IMFP}} \cos\theta}\right)\right]^{-1}$$
3. Correlate XPS-derived $\sigma_{-\text{OH}}$ with the integrated FTIR peak area at $3740\text{ cm}^{-1}$ ($A_{-\text{OH}}$) using the modified Beer-Lambert extinction coefficient calibration curve.
4. Quantify surface carbon concentration from $\text{C } 1s$ core peak intensity using relative sensitivity factors ($S_C = 0.296$, $S_O = 0.711$).

### Step 5: Disposition & ALD Gate Signoff
1. Verify calculated $-\text{OH}$ density against the threshold requirement: $\sigma_{-\text{OH}} \ge 4.5 \times 10^{14}\text{ sites/cm}^2$ (equivalent to $\ge 15\%$ of total $\text{O } 1s$ peak area).
2. Verify total adventitious carbon contamination: $\text{C}_{\text{contam}} \le 2.0\text{ at}\%$.
3. **PASS Disposition**:
   - Transfer wafer immediately to the ALD deposition reactor without vacuum break.
   - Execute recipe for $\text{Al}_2\text{O}_3 / \text{Ta}_2\text{O}_5$ high-$\kappa$ dielectric deposition targeting $\kappa > 15$ and EOT $3\text{ to }4\text{ nm}$.
4. **FAIL / REWORK Disposition**:
   - If $\sigma_{-\text{OH}} < 4.0 \times 10^{14}\text{ sites/cm}^2$ or $\text{C}_{\text{contam}} > 2.0\text{ at}\%$, hold lot.
   - Return wafer to the in-situ ozone pre-clean chamber for 120 seconds cycle optimization at $300^\circ\text{C}$ to burn off organic residue and re-functionalize surface hydroxyl species.

---

## 3. Machine-Measurable Acceptance Criteria

| Metric / Parameter | Target Value | Physical Units | Tolerance / Constraint | Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **Interfacial Hydroxyl Surface Density ($\sigma_{-\text{OH}}$)** | $\ge 4.5 \times 10^{14}$ | $\text{sites/cm}^2$ | Min acceptable threshold ($\ge 15.0\text{ to }22.0\%$ of $\text{O } 1s$ peak) | In-situ XPS $\text{O } 1s$ deconvolution & FTIR cross-calibration |
| **Surface Carbon Contamination Level** | $\le 2.0$ | $\text{at}\%$ | Max allowable limit ($< 1.5\text{ at}\%$ nominal) | Monochromatic XPS $\text{C } 1s$ survey & high-resolution scan |
| **ATR-FTIR Isolated Silanol Peak Area ($A_{-\text{OH}}$)** | $\ge 0.035$ | $\text{a.u. } (\text{absorbance}\cdot\text{cm}^{-1})$ | Peak centered at $3740 \pm 5\text{ cm}^{-1}$ ($4\text{ cm}^{-1}$ resolution) | In-situ evanescent wave ATR-FTIR spectrometry |
| **Cluster Transfer Chamber Base Pressure** | $< 2.0 \times 10^{-6}$ | $\text{Torr}$ | Maximum base vacuum before transfer | Penning / Bayard-Alpert ion gauge |

```text
                     Acceptance Criteria Target Metrics 
                    ┌──────────────────────────────────┐
                    │░░░                               │
    C1s Contam (at%)┤░░░                               │
                    │▒                                 │
   ATR-FTIR 3740cm-1┤▒                                 │
    O1s -OH Sub-peak┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                    │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
-OH Density (x10^14)┤██████████                        │
                    │██████████                        │
                    └┬───────┬────────┬───────┬───────┬┘
                    0.0     4.6      9.2    13.9   18.5 
```

---

## 4. Source Citations & Context Alignment

1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry $L = 180\text{ nm}$, $W = 220\text{ nm}$, stacked capacitor over bitline (COB) crown-shaped polysilicon or metal-insulator-metal (MIM) structure erected above drain contact via tungsten plug (W-plug).
   - Dielectric requirements: $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-$\kappa$ dielectric stack providing effective dielectric constant $\kappa > 15$, minimum cell capacitance $28\text{ fF/cell}$, and junction leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - 1T1C architecture, $8F^2$ or $6F^2$ cell layout, $25\text{ to }30\text{ fF}$ storage capacitance ensuring data retention time $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - High-$\kappa$ dielectric equivalent oxide thickness (EOT) around $3\text{ to }4\text{ nm}$ on stacked crown capacitors.
3. **Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects**:
   - Vacuum chamber base pressure criteria: must pump down below $2.0 \times 10^{-6}\text{ Torr}$ using turbomolecular or cryopump to prevent oxygen and atmospheric contamination.

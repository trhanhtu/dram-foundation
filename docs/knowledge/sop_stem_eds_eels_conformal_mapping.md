# SOP: STEM-EDS/EELS Nanoscale Conformal Profile Mapping & Top-to-Bottom Thickness Ratio Extraction

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Accepted
- **Generation**: Gen 3 (nm)
- **Action Type**: Make
- **Context Path**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > 180nm CMOS Commercial MPW Tapeout & PDK Implementation > 3D High-Aspect-Ratio Crown Capacitor ALD Dielectric & Metal Electrode Deposition > ALD Al2O3/Ta2O5 High-k Dielectric Stack Recipe Optimization & Deposition > Spectroscopic Ellipsometry, Crown Sidewall Step Coverage & C-V/I-V Leakage Qualification > Cross-Sectional HR-SEM/TEM Crown Sidewall Step Coverage and Conformal Profile Analysis > STEM-EDS/EELS Nanoscale Conformal Profile Mapping & Top-to-Bottom Thickness Ratio Extraction

---

## 1. Overview & Rationale
For 180nm 1T1C stacked crown capacitors (8F² and 6F² topologies), conformal deposition of the high-k dielectric stack (e.g., $\text{Al}_2\text{O}_3/\text{Ta}_2\text{O}_5$ or ONO) over high-aspect-ratio (HAR) 3D crown sidewalls is critical to maintaining minimum capacitance ($\ge 25 - 28\text{ fF/cell}$), minimizing leakage ($< 1\text{ fA/cell}$ at 85°C), and preventing early dielectric breakdown.
This leaf Standard Operating Procedure (SOP) specifies the exact analytical protocol to prepare cross-sectional lamellae via Dual-Beam Focused Ion Beam (FIB) and extract high-precision thickness, chemical interface profiles, and step-coverage ratios along the crown capacitor's top, middle sidewall, and bottom cup via Scanning Transmission Electron Microscopy paired with Energy-Dispersive X-ray Spectroscopy (STEM-EDS) and Electron Energy-Loss Spectroscopy (STEM-EELS).

---

## 2. Metrology Workflow & Execution Steps

### 2.1 FIB Site-Specific Lamella Preparation & Thinning
1. **Protective Capping**:
   - Deposit in-situ electron-beam Pt/C protection layer ($1.0\text{ kV}$, $0.5\text{ nA}$, thickness $\sim 200\text{ nm}$) over selected 180nm crown capacitor array (pitch: $360\text{ nm} - 400\text{ nm}$).
   - Follow with ion-beam Pt cap ($30\text{ kV}$, $80\text{ pA} \to 0.23\text{ nA}$, target thickness $1.5 - 2.0\ \mu\text{m}$).
2. **Rough Trenching & Lift-out**:
   - Bulk trench milling at $30\text{ kV}$, $7 - 15\text{ nA}$ Gallium ($Ga^+$) beam.
   - Omniprobe in-situ needle attachment via Pt deposition; cut bottom and side tabs. Transfer lamella to Mo or Cu TEM half-grid.
3. **Progressive Fine Thinning & Polish**:
   - Thinning at $30\text{ kV}$, stepping beam current down from $0.43\text{ nA} \to 80\text{ pA} \to 40\text{ pA}$.
   - Amorphous damage reduction polish: $5\text{ kV}$, $20\text{ pA}$ followed by final flash polish at $2\text{ kV}$ ($15\text{ pA}$, $\pm 7^\circ$ tilt) until final specimen thickness $t \le 40 - 50\text{ nm}$ across the bottom cup and W-plug interface.

### 2.2 STEM Alignment & HAADF Z-Contrast Imaging
1. **Instrument Setup**:
   - Accelerating Voltage: $200\text{ kV}$ (cold FEG).
   - Probe convergence semi-angle $\alpha = 15 - 21\text{ mrad}$.
   - High-Angle Annular Dark-Field (HAADF) detector collection semi-angle range: $\beta = 50 - 200\text{ mrad}$ for clean Rutherford atomic-number ($Z^2$) contrast.
   - Beam probe size: $\le 0.15\text{ nm}$ (sub-ångström / probe-corrected).
2. **Reference Cross-Section Imaging**:
   - Align zone axis parallel to capacitor crown sidewalls.
   - Record calibrated HAADF reference micrographs across three regions:
     - **Region A (Top)**: Rim/lip of crown capacitor.
     - **Region B (Mid)**: Sidewall midpoint.
     - **Region C (Bottom)**: Cup corner and base directly above the tungsten plug (W-plug).

### 2.3 STEM-EDS Spectrum Imaging & Quantitative Line Profile Extraction
1. **Acquisition Parameters**:
   - Detector: Four-quadrant windowless SDD ($\ge 0.9\text{ sr}$ solid angle).
   - Probe current: $150 - 300\text{ pA}$ (optimized to prevent beam-induced local damage/migration while retaining high count rates $> 50{,}000\text{ cps}$).
   - Pixel dwell time: $20 - 50\ \mu\text{s/pixel}$ with drift correction (spatial drift check interval every 15 frames).
2. **Elemental Line Scanning**:
   - Perform perpendicular line scans across the dielectric stack at Top, Mid, and Bottom locations:
     - Characteristic X-ray peaks monitored: $\text{Ta-M}\alpha$ ($1.71\text{ keV}$), $\text{Al-K}\alpha$ ($1.48\text{ keV}$), $\text{O-K}\alpha$ ($0.525\text{ keV}$), and adjacent electrode markers ($\text{Ti-K}\alpha$ $4.51\text{ keV}$, $\text{N-K}\alpha$ $0.392\text{ keV}$, $\text{W-M}\alpha$ $1.77\text{ keV}$, $\text{Si-K}\alpha$ $1.74\text{ keV}$).
   - Extract the full-width at half-maximum (FWHM) physical thickness $T_{\text{top}}$, $T_{\text{mid}}$, and $T_{\text{bottom}}$ of the high-k stack.

### 2.4 High-Resolution STEM-EELS Core-Loss & Low-Loss Profiling
1. **Spectrometer Calibration**:
   - Energy dispersion: $0.1 - 0.25\text{ eV/channel}$.
   - Energy resolution: $\le 0.8\text{ eV}$ measured across zero-loss peak (ZLP).
2. **Fine-Interface Mapping**:
   - Measure low-loss spectrum to extract local specimen relative thickness ($t/\lambda$). Reject lamella regions where $t/\lambda > 0.8$ due to multiple inelastic scattering artifacts.
   - Core-loss mapping across:
     - $\text{Ta-N}_{4,5}$ edge ($33\text{ eV}$), $\text{Al-L}_{2,3}$ edge ($73\text{ eV}$), $\text{Si-L}_{2,3}$ edge ($99\text{ eV}$), and $\text{O-K}$ edge ($532\text{ eV}$).
   - Differentiate physical thickness from interfacial sub-oxide intermixing ($SiO_x / AlO_x$ intermixing layer thickness $< 0.6\text{ nm}$).

### 2.5 Top-to-Bottom Thickness Ratio & Step Coverage Calculation
1. **Ratio Formulation**:
   $$\text{Conformality Ratio (Top-to-Bottom)} = \frac{T_{\text{bottom}}}{T_{\text{top}}}$$
   $$\text{Step Coverage (\%)} = \frac{T_{\text{bottom}}}{T_{\text{top}}} \times 100\%$$
   $$\text{Sidewall Conformality (\%)} = \frac{T_{\text{mid}}}{T_{\text{top}}} \times 100\%$$
2. Log metrics directly into foundry SPC (Statistical Process Control) database.

---

## 3. Machine-Measurable Acceptance Criteria Target Metrics

| Parameter / Metric | Target Value | Tolerance / Limit | Measurement Method | Context Reference Target |
| :--- | :--- | :--- | :--- | :--- |
| **Top-to-Bottom Thickness Ratio ($T_{\text{bottom}} / T_{\text{top}}$)** | **$\ge 0.95$ (95%)** | $\ge 0.90$ minimum | STEM-EDS / EELS line scan calibrated FWHM | Conformal high-k profile across crown HAR structure |
| **Equivalent Oxide Thickness (EOT)** | **$3.5\text{ nm}$** | $3.0\text{ nm} - 4.0\text{ nm}$ | High-k physical thickness converted via effective $\kappa > 15$ | *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering* ($3 - 4\text{ nm}$ EOT) |
| **Storage Capacitance Target ($C_s$)** | **$\ge 28\text{ fF/cell}$** | Min $25\text{ fF/cell}$ | Correlated physical area $\times$ EOT extraction ($C-V$) | *180nm DRAM Cell Layout Topology* ($\ge 28\text{ fF/cell}$, Ret. $> 64\text{ ms}$) |
| **Dielectric Leakage Floor ($I_{\text{leak}}$ at 85°C)** | **$< 1.0\text{ fA/cell}$** | Max $1.0\text{ fA/cell}$ | In-line $I-V$ leakage qualification correlated | *180nm DRAM Cell Layout Topology* ($< 1\text{ fA/cell}$ at 85°C) |
| **Crown Sidewall Interfacial Intermixing Layer** | **$\le 0.5\text{ nm}$** | Max $0.8\text{ nm}$ | Core-loss EELS O-K & Al-L edge onset gradient | Avoid EOT degradation & leakage path |

---

## 4. Verified Literature Context Citations
1. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$, bitline contact shared).
   - Crown-shaped stacked capacitor over bitline (COB) erected above drain via tungsten plug (W-plug).
   - High-k dielectric stack ($\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ or ONO) providing effective $\kappa > 15$.
   - Capacitance budget: Minimum $28\text{ fF/cell}$; leakage current $< 1\text{ fA/cell}$ at 85°C.
2. **Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - 1T1C architecture with $8F^2$ or $6F^2$ layout; minimum capacitance $25 - 30\text{ fF/cell}$ for data retention $> 64\text{ ms}$ at 85°C.
   - Stacked capacitor (Crown or Cylinder) utilizing $\text{Ta}_2\text{O}_5$ high-k dielectric with Equivalent Oxide Thickness (EOT) of $3 - 4\text{ nm}$.
   - Bitline and wordline pitch of $360\text{ nm} - 400\text{ nm}$.

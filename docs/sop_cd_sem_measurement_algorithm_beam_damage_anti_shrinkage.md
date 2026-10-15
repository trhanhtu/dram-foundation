# Standard Operating Procedure (SOP): In-Line CD Measurement Algorithm Validation & Beam-Damage Anti-Shrinkage Optimization

- **SOP ID**: `SOP-MET-EBDW-CDSEM-002`
- **Revision**: `v1.0.0`
- **Date**: 2026-10-15
- **Status**: Released / Operational
- **Applicability**: 180nm Open-Source DRAM (DRAM Foundation VN) / EBDW Gate Array Metrology
- **Context Level**: Metrology > Automated In-Line CD-SEM & LER Characterization > In-Line CD Measurement Algorithm Validation & Beam-Damage Anti-Shrinkage Optimization

---

## 1. Overview & Scope

This Standard Operating Procedure (SOP) defines the operational workflow for calibrating, validating, and locking the in-line automated Critical Dimension Scanning Electron Microscope (CD-SEM) waveform line extraction algorithm, and optimizing beam-induced thermal/hydrocarbon deposition shrinkage on 180nm gate array features.

In dense DRAM access transistor arrays ($L = 180\text{ nm}$, poly gate pitch $P = 360\text{ nm} - 400\text{ nm}$), prolonged high-energy electron beam exposure induces critical dimension distortion, including electron beam-induced carbon deposition, resist shrinkage during post-develop inspection (ADI), and thermal charging artifacts. This SOP guarantees repeatable sub-nanometer CD extraction while maintaining beam shrinkage below allowable tolerance.

---

## 2. Theoretical & Literature Context Citations

All geometrical and lithographic specifications strictly adhere to the project literature context:
1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor physical channel length $L = 180\text{ nm}$.
   - Access transistor active width $W = 220\text{ nm}$.
   - Gate pitch (wordline/bitline array pitch): $360\text{ nm} - 400\text{ nm}$.
2. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Physical placement grid resolution: $0.005\ \mu\text{m}$ ($5\text{ nm}$).
   - Minimum poly gate length: $0.15\ \mu\text{m}$ ($150\text{ nm}$).
   - Minimum poly gate spacing: $0.21\ \mu\text{m}$ ($210\text{ nm}$).
   - Maximum allowable overlay error: $\le 35\text{ nm}$.
3. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - Bitline and wordline pitch target: $360\text{ nm} - 400\text{ nm}$.
   - Thermally grown $\text{SiO}_2$ gate dielectric physical thickness: $\sim 3.5\text{ nm}$.

---

## 3. Equipment & Metrology Setup

| Parameter | Specification | Notes / Controls |
| :--- | :--- | :--- |
| **Tool Type** | In-Line Cold-Field Emission CD-SEM | Ultra-high vacuum automated wafer handler |
| **Accelerating Voltage ($V_{\text{acc}}$)** | $500\text{ V} - 800\text{ V}$ | Low landing energy to avoid gate oxide breakdown ($T_{\text{ox}} \sim 3.5\text{ nm}$) |
| **Beam Extraction Current ($I_{\text{p}}$)** | $5.0\text{ pA} - 8.0\text{ pA}$ | Suppresses thermal heating & resist/poly shrinkage |
| **Working Distance (WD)** | $2.5\text{ mm} - 3.5\text{ mm}$ | Optimized for immersion objective lens |
| **Vacuum Chamber Pressure** | $\le 1.0 \times 10^{-7}\text{ Torr}$ | Cryo-baffle trapping active to prevent hydrocarbon cracking |
| **Field of View (FOV)** | $1.2\ \mu\text{m} \times 1.2\ \mu\text{m}$ to $2.0\ \mu\text{m} \times 2.0\ \mu\text{m}$ | Encompasses $\ge 3$ full pitches of DRAM gate arrays |
| **Image Resolution** | $1024 \times 1024\text{ pixels}$ | Sampling pixel size $\le 1.5\text{ nm/pixel}$ |

---

## 4. Step-by-Step Operating Procedure

### Step 1: Automated Pattern Recognition & Navigation Lock
1. Load 200mm/300mm wafer into CD-SEM loadlock chamber; pump down to baseline pressure $< 5 \times 10^{-6}\text{ Torr}$.
2. Execute global wafer alignment using optical pattern recognition targets to correct translational ($X, Y \le 5\ \mu\text{m}$) and rotational ($\theta \le 0.05^\circ$) errors.
3. Drive stage to target DRAM macro array coordinates using the pre-programmed navigation recipe.
4. Perform local fine alignment on the array periphery fiducial at low magnification ($5,000\times$) before shifting to measurement site ($150,000\times$).

### Step 2: Line Profile Waveform Extraction & Algorithm Configuration
1. Position the measurement box centered symmetrically across the $180\text{ nm}$ polysilicon gate line.
2. Acquire the Secondary Electron (SE) line profile across the feature width with a minimum integration length along the gate edge of $200\text{ nm}$ (within active width $W = 220\text{ nm}$).
3. Configure the line-edge detection algorithm:
   - **Algorithm Model**: Normalized Secondary Electron Peak-to-Threshold (Derivative/Maximum Slope Threshold).
   - **Threshold Cutoff**: Lock at **$50.0\%$** of peak-to-baseline intensity height for both Left Edge ($LE_{50}$) and Right Edge ($RE_{50}$).
   - **Derivative Smoothing Filter**: Apply a 5-point Gaussian kernel smoothing window to suppress random shot noise without smearing line-edge definition.
   - **CD Computation**:
     $$\text{CD} = RE_{50} - LE_{50}$$
4. Validate pitch calibration by measuring the center-to-center distance between adjacent poly lines to confirm compliance with the $360\text{ nm} - 400\text{ nm}$ design rule ($L = 180\text{ nm}$, space $\ge 210\text{ nm}$).

### Step 3: Beam-Damage Anti-Shrinkage Dose Optimization
1. Select dedicated sacrificial DRAM array test sites (minimum 5 sites across wafer: Center, Top, Bottom, Left, Right).
2. Measure initial baseline CD at Scan $N=1$ using standard frame integration (16 frames averaging, pixel dwell time $t_{\text{dwell}} = 100\text{ ns}$).
3. Perform an endurance multi-scan sequence: acquire $N = 1, 3, 5, 8, 10, 15$ successive image captures on the exact same coordinate without moving the stage.
4. Calculate shrinkage rate:
   $$\Delta \text{CD}(N) = |\text{CD}_N - \text{CD}_1|$$
5. If $\Delta \text{CD}(10) > 1.5\text{ nm}$, implement Anti-Shrinkage Controls:
   - Reduce beam dwell time $t_{\text{dwell}}$ to $50\text{ ns}$.
   - Reduce frame integration from 16 to 8 frames, enabling spatial Kalman filter averaging.
   - Activate auto-defocus offset jump: perform autofocus and auto-stigmation on a dummy patch offset $2.0\ \mu\text{m}$ away along the gate direction prior to beam snap-shot exposure.

### Step 4: Line-Edge Roughness (LER) & Gate Profile Validation
1. Extract line edges along the gate length ($L_{\text{box}} = 200\text{ nm}$).
2. Compute $3\sigma$ Line-Edge Roughness ($\text{LER}_{3\sigma}$) and Line-Width Roughness ($\text{LWR}_{3\sigma}$):
   $$\text{LWR}_{3\sigma} = 3 \times \sqrt{\frac{1}{M}\sum_{i=1}^M (\text{CD}_i - \overline{\text{CD}})^2}$$
3. Verify that measured gate spacing conforms to the SkyWater SKY130 minimum poly spacing rule ($\ge 210\text{ nm}$).

---

## 5. Process Flow Diagram

```text
┌────────────────────────┐
│                        │
│      Beam Dose &       │
│  Accelerating Voltage  │
│  Setup: 500V - 800V,   │
│       Ip <= 8 pA       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Secondary Electron   │
│   Peak-Threshold Alg   │
│   Validation at 50%    │
│       Threshold        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Array Gate CD &     │
│  Spacing Extraction:   │
│       L=180 nm,        │
│    Pitch=360-400 nm    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Multi-Scan Beam     │
│    Damage Test: 10     │
│   Consecutive Scans    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Anti-Shrinkage Dose   │
│     Optimization:      │
│  Cumulative Drift <=   │
│         1.5 nm         │
│                        │
└────────────────────────┘
```

---

## 6. Beam Damage Trend Analysis

Monochrome zebra-stripe analysis of gate critical dimension stability under repeated electron beam exposure:

```text
                Gate Poly CD vs Multiple Beam Scans (nm)
                ┌──────────────────────────────────────┐
                │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
       15th Scan┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
                │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
       10th Scan┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        5th Scan┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
1st Scan (Fresh)┤██████████████████████████████████████│
                │██████████████████████████████████████│
                └┬────────┬─────────┬────────┬────────┬┘
                 0       45        90       135     180 
```

---

## 7. Machine-Measurable Acceptance Criteria

| Metric ID | Parameter Description | Target Specification | Physical Units | Verification Tool & Method |
| :--- | :--- | :--- | :--- | :--- |
| **AC-MET-01** | Nominal Gate Critical Dimension (CD) Mean | $180.0 \pm 5.0$ | $\text{nm}$ | In-Line CD-SEM $50\%$ peak-threshold algorithm |
| **AC-MET-02** | CD Repeatability Precision ($3\sigma$) | $\le 1.2$ | $\text{nm}$ | 20 dynamic wafer load/unload unload repeat measurements |
| **AC-MET-03** | 10-Scan Beam-Induced CD Shrinkage ($\Delta \text{CD}_{10}$) | $\le 1.5$ | $\text{nm}$ | Single-location 10 continuous scans differential measurement |
| **AC-MET-04** | Line-Width Roughness ($3\sigma\ \text{LWR}$) | $\le 4.5$ | $\text{nm}$ | High-frequency edge variation analysis over $200\text{ nm}$ slice |

---

## 8. Micro-Knowledge & Documentation Tracking

- **Document Path**: [docs/sop_cd_sem_measurement_algorithm_beam_damage_anti_shrinkage.md](./docs/sop_cd_sem_measurement_algorithm_beam_damage_anti_shrinkage.md)
- **Status**: Operational SOP
- **Council Approval**: DRAM Foundation VN Metrology Council

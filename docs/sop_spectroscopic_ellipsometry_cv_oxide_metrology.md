# SOP: Spectroscopic Ellipsometry and C-V Oxide Thickness & Interface Metrology

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Node**: 180nm Open-Source DRAM (Gen 1)
- **Classification**: Standard Operating Procedure (Leaf SOP) / Metrology

---

## 1. Overview & Process Objectives
In classic 180nm DRAM architectures (1T1C cell with 8F² folded bitline topology, access transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$), thermally grown gate oxide ($\text{SiO}_2$) serves as the primary dielectric isolating the wordline/access gate from the substrate channel. Process integration requires an ultra-thin dry thermal gate oxide target of **3.5 nm physical thickness** grown at 850°C–900°C. 

Accurate non-destructive extraction of physical thickness ($t_{ox}$), refractive index ($n$), equivalent oxide thickness ($\text{EOT}$), interface trap density ($D_{it}$), and flatband voltage shift ($\Delta V_{fb}$) is performed via correlated **Spectroscopic Ellipsometry (SE)** and **Capacitance-Voltage (C-V) MOSCAP Metrology**.

---

## 2. Process Flow & Structural Diagram

```text
┌────────────────────────┐
│                        │
│   Oxide Growth 3.5nm   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Spectroscopic      │
│    Ellipsometry SE     │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  MOSCAP Fabrication /  │
│       Dot Array        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    High-Frequency &    │
│    Quasi-Static C-V    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     EOT, Dit & Vfb     │
│       Extraction       │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Pre-Measurement Inspection & Reference Baseline
1. Transfer the 150mm/200mm p-type Si (100) wafer (boron-doped, resistivity $1 - 10\ \Omega\cdot\text{cm}$) to the class 10 cleanroom metrology bay under Class 1 laminar flow.
2. Initialize the automated rotating-compensator Spectroscopic Ellipsometer (RC2/VASE):
   - Spectral range: $\lambda = 193\text{ nm}$ to $1000\text{ nm}$.
   - Angle of incidence (AOI): Multi-angle sweep at $65.0^\circ$, $70.0^\circ$, and $75.0^\circ$ (spanning Brewster's angle for $\text{Si}/\text{SiO}_2$ at $\sim 75.6^\circ$).
3. Load a certified Si reference wafer with native oxide stripped (<0.2 nm) to calibrate the baseline polarizer/analyzer angles, spectrometer wavelength dispersion, and detector gain.

### Step 2: 49-Point Polar Spectroscopic Ellipsometry Mapping
1. Load the production/monitor wafer onto the automated vacuum chuck ($10^{-2}\text{ Torr}$ holddown, tilt level within $\pm 0.005^\circ$).
2. Execute a 49-point polar concentric scan pattern covering center ($R = 0\text{ mm}$), inner ring ($R = 0.33 R_{max}$), middle ring ($R = 0.67 R_{max}$), and edge ring ($R = 0.90 R_{max}$ with 5 mm edge exclusion).
3. Acquire polarization parameters $\Psi(\lambda)$ and $\Delta(\lambda)$ across $193 - 1000\text{ nm}$ with integration time $\tau = 1.5\text{ s}$ per site.
4. Optical Dispersion Modeling:
   - Apply a two-layer optical model: Substrate: $\text{c-Si}$ (tabulated Herzinger dispersion); Ambient: Air; Overlayer: $\text{SiO}_2$ modeled via Cauchy dispersion:
     $$n(\lambda) = A_n + \frac{B_n}{\lambda^2} + \frac{C_n}{\lambda^4}, \quad k(\lambda) \approx 0$$
     Nominal parameters: $A_n = 1.457$, $B_n = 0.0035\ \mu\text{m}^2$, $C_n = 0.0001\ \mu\text{m}^4$.
   - Extract physical thickness $t_{ox\_SE}$ and refractive index at $632.8\text{ nm}$. Minimize Mean Squared Error (MSE < 1.50).

### Step 3: Test MOSCAP Metallization (Shadow Mask / Dot Array)
1. For electrical C-V validation, load the oxide monitor wafer into an e-beam or thermal evaporator with an array shadow mask (dot diameter $\phi = 200\ \mu\text{m}$ to $500\ \mu\text{m}$, dot area $A_{gate} = 3.142 \times 10^{-4}\text{ cm}^2$ to $1.963 \times 10^{-3}\text{ cm}^2$).
2. Evaporate pure aluminum (99.999% Al) front gate electrodes:
   - Deposition rate: $0.2\text{ nm/s}$ at base pressure $< 2.0 \times 10^{-6}\text{ Torr}$; total thickness $= 300\text{ nm} \pm 10\text{ nm}$.
3. Backside native oxide strip using BOE 6:1 swab followed by backside Al blanket contact evaporation ($200\text{ nm}$).
4. Form gas anneal (FGA) at $400^\circ\text{C}$ in $95\%\ \text{N}_2 / 5\%\ \text{H}_2$ for 30 minutes in a quartz tube furnace to passivate dangling bonds and establish ohmic contact.

### Step 4: High-Frequency (HF) & Quasi-Static (QS) C-V Metrology
1. Mount the wafer onto the shielded temperature-controlled probe station ($T = 25.0^\circ\text{C} \pm 0.5^\circ\text{C}$, dark enclosure).
2. Connect Low-Noise Triaxial cables to an LCR meter (Keysight E4980A or Keithley 4200-SCS):
   - **High-Frequency C-V**: Test frequency $f = 100\text{ kHz}$ and $1\text{ MHz}$, AC oscillation level $V_{ac} = 15\text{ mV}_{\text{rms}}$, DC gate bias sweep from accumulation ($-2.5\text{ V}$) through depletion to inversion ($+2.0\text{ V}$) at a ramp rate of $50\text{ mV/s}$.
   - **Quasi-Static C-V / Low-Frequency C-V**: Sweep DC bias from $-2.5\text{ V}$ to $+2.0\text{ V}$ at ramp rate $10\text{ mV/s}$ recording displacement current $I_{disp}$ to determine low-frequency capacitance $C_{LF} = I_{disp} / (dV/dt)$.

### Step 5: Parameter Extraction (EOT, Dit, and Vfb)
1. **Accumulation Capacitance ($C_{acc}$)**: Extract maximum capacitance in strong accumulation at $V_G = -2.5\text{ V}$, correcting for substrate series resistance $R_s$ and quantum-mechanical band-bending/poly-depletion effects via Hauser C-V fitting.
2. **Equivalent Oxide Thickness (EOT)**:
   $$\text{EOT} = \frac{\kappa_{\text{SiO}_2} \cdot \varepsilon_0 \cdot A_{gate}}{C_{acc\_corr}} = \frac{3.9 \times (8.854 \times 10^{-14}\ \text{F/cm}) \times A_{gate}}{C_{acc\_corr}}$$
3. **Interface Trap Density ($D_{it}$)** via High-Low Frequency (Castagné-Vapaille) method:
   $$D_{it} = \frac{C_{ox}}{q \cdot A_{gate}} \left( \frac{C_{LF} / C_{ox}}{1 - C_{LF} / C_{ox}} - \frac{C_{HF} / C_{ox}}{1 - C_{HF} / C_{ox}} \right) \quad [\text{cm}^{-2}\text{eV}^{-1}]$$
4. **Flatband Voltage ($V_{fb}$)**: Extract flatband capacitance $C_{fb}$ using Debye length $\lambda_D$:
   $$C_{fb} = \frac{C_{ox} \cdot C_{s,fb}}{C_{ox} + C_{s,fb}}, \quad C_{s,fb} = \frac{\varepsilon_{Si} A_{gate}}{\lambda_D}$$
   Determine $V_{fb}$ from the HF C-V curve and compute flatband voltage shift $\Delta V_{fb} = |V_{fb\_meas} - V_{fb\_ideal}|$.

---

## 4. Machine-Measurable Acceptance Criteria

```text
                                                        
                   ┌───────────────────────────────────┐
                   │░                                  │
Vfb Flatband Offset┤░                                  │
                   │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Dit Interface Traps┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
  Radial Uniformity┤▓▓                                 │
                   │▓▓                                 │
      EOT Thickness┤█████████████████████████          │
                   │█████████████████████████          │
                   └┬────────┬───────┬────────┬───────┬┘
                   0.0      1.2     2.5      3.8    5.0 
```

| Parameter Metric | Target Value | Allowable Tolerance | Physical Unit | Measurement Tool / Method |
| :--- | :--- | :--- | :--- | :--- |
| **Physical Gate Oxide Thickness ($t_{ox}$)** | **3.50** | $\pm 0.15$ ($3.35 - 3.65$) | **nm** | Multi-Angle Spectroscopic Ellipsometry (193–1000 nm, Cauchy fit, MSE < 1.50) |
| **Equivalent Oxide Thickness (EOT)** | **3.50** | $\pm 0.20$ ($3.30 - 3.70$) | **nm** | HF C-V Accumulation Extraction ($100\text{ kHz} / 1\text{ MHz}$, Hauser model) |
| **Across-Wafer Thickness Non-Uniformity ($1\sigma$)** | **$\le 0.12$** | Maximum 0.15 | **nm** | 49-point polar concentric wafer map (5 mm edge exclusion) |
| **Interface Trap Density ($D_{it}$ at midgap)** | **$\le 5.0 \times 10^{10}$** | Maximum $1.0 \times 10^{11}$ | **$\text{cm}^{-2}\text{eV}^{-1}$** | High-Low (HF/LF) C-V differential method post-FGA |
| **Flatband Voltage Shift ($\Delta V_{fb}$)** | **$\le 0.05$** | Maximum 0.08 | **V** | High-Frequency C-V flatband capacitance matching ($100\text{ kHz}$) |

---

## 5. Literature & Context Citations

1. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - Gate dielectric is thermally grown silicon dioxide ($\text{SiO}_2$) at 850°C–900°C dry oxidation with $\sim 3.5\text{ nm}$ physical thickness.
   - Storage capacitor must maintain minimum capacitance $25 - 30\text{ fF}$ per cell to ensure data retention time $> 64\text{ ms}$ at 85°C.
2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Unit cell geometry: Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - Sub-threshold and junction leakage kept below $1\text{ fA/cell}$ at 85°C, demanding tight gate oxide thickness and low interface state density ($D_{it}$) to avoid channel off-state leakage.
3. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Folded bitline 8F² architecture requires strict access transistor threshold voltage matching ($\Delta V_{th} < 20\text{ mV}$) driven by flatband voltage control ($\Delta V_{fb} \le 0.05\text{ V}$) and across-wafer oxide uniformity ($1\sigma \le 0.12\text{ nm}$).

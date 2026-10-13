# Standard Operating Procedure (SOP)
## MOSCAP Test Structure Probe Card Alignment and Open/Short Parasitic Calibration

- **Task ID / Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > 180nm Dry Gate Oxide Growth (3.5 nm) [Thermal Processing] > Spectroscopic Ellipsometry and C-V Oxide Thickness & Interface Metrology [Metrology] > High-Frequency and Quasi-Static C-V Interface Trap Density (Dit) Extraction [Metrology] > High-Frequency (1 MHz) and Quasi-Static C-V Dual-Sweep Acquisition [Metrology] > MOSCAP Test Structure Probe Card Alignment and Open/Short Parasitic Calibration [Metrology]
- **Generation**: Gen 1 (mm)
- **Action Type**: Make
- **Status**: Released / Operational

---

### 1. Objective & Scope
This SOP establishes the machine-level setup, mechanical alignment, and RF/impedance de-embedding calibration (Open/Short parasitic compensation) for probing planar MOS capacitor (MOSCAP) test structures. The test vehicle consists of circular aluminum gate dots (diameters: 200 µm, 500 µm, 1000 µm) sputtered on 3.5 nm thermally grown dry gate oxide ($SiO_2$) on P-type (100) Si with Au/Al backside ohmic contact. Proper parasitic calibration ensures error-free acquisition of 1 MHz High-Frequency and Quasi-Static C-V curves to resolve physical oxide thickness $t_{ox}$ within $\pm 0.1\text{ nm}$ precision.

---

### 2. Operational Workflow Diagram

```text
┌──────────────────────┐
│                      │
│  Probe Card / Chuck  │
│       Loading        │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│       Optical        │
│   Planarization &    │
│      Alignment       │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│    Open Parasitic    │
│     Calibration      │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│   Short Parasitic    │
│     Calibration      │
│                      │
└───────────┬──────────┘
            │
            │
            ▼
┌──────────────────────┐
│                      │
│      Acceptance      │
│    Verification &    │
│   Dual-Sweep Ready   │
│                      │
└──────────────────────┘
```

---

### 3. Step-by-Step Operating Procedure

#### Step 1: Substrate Chuck Vacuum & Backside Ohmic Grounding
1. Mount the P-type (100) wafer (featuring backside Au or Al metallization) onto the gold-plated vacuum chuck.
2. Engage chuck vacuum (> 75 kPa); verify vacuum lock and electrical continuity between chuck and wafer backside (substrate contact resistance $< 1.0\ \Omega$).

#### Step 2: Optical Alignment and Planarization
1. Under 10× to 50× optical magnification, locate the circular Al gate dot array (200 µm, 500 µm, and 1000 µm test structures).
2. Align probe card / coaxial micropositioner needle tips (BeCu or W tips, radius 10–25 µm) over the target dot center.
3. Perform Z-height touchdown planarization: sense initial physical touch, then apply a controlled vertical overdrive of **25 µm to 40 µm** (target: **35 µm**) to scrub native aluminum oxide without puncturing the underlying 3.5 nm dry gate oxide.

#### Step 3: Open Circuit Parasitic Calibration (Admittance De-embedding)
1. Elevate probe needle tips exactly **250 µm** vertically above the substrate surface in air (or over an isolated quartz open calibration block).
2. Ensure test fixture triaxial/coaxial cabling and environmental light-tight shield (dark box) are closed.
3. Trigger the LCR / C-V meter (operating at test frequency $f = 1.0\text{ MHz}$, AC oscillation level $V_{ac} = 15\text{ mV}$ to $30\text{ mV}$ RMS):
   - Measure open admittance: $Y_{open} = G_{open} + j \omega C_{open}$.
   - Store $C_{open}$ and $G_{open}$ correction arrays in the instrument calibration registry.

#### Step 4: Short Circuit Parasitic Calibration (Impedance De-embedding)
1. Lower probe tips onto an Al shorting substrate calibration pad (or contiguous metallized area on the calibration substrate).
2. Apply standard contact overdrive (35 µm).
3. Trigger the meter short correction routine at $f = 1.0\text{ MHz}$:
   - Measure short series impedance: $Z_{short} = R_{short} + j \omega L_{short}$.
   - Store residual series resistance $R_{short}$ and inductance $L_{short}$ in instrument firmware.
4. Activate real-time de-embedding network:
   $$Z_{DUT} = \frac{Z_{meas} - Z_{short}}{1 - (Z_{meas} - Z_{short}) Y_{open}}$$

---

### 4. Machine-Measurable Acceptance Criteria

```text
Calibration Target Windows & Tolerances:
                       ┌───────────────────────────────┐
                       │░                              │
   Oxide Precision (nm)┤░                              │
                       │▒▒▒▒▒▒▒▒▒▒▒▒▒▒                 │
 Contact Overdrive (um)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒                 │
Short Residual R (mOhm)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                       │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
   Open Residual C (fF)┤███████                        │
                       │███████                        │
                       └┬───────┬──────┬───────┬──────┬┘
                        0      20     40      60     80 
```

| Parameter / Metric | Unit | Target / Specification | Verification Method |
| :--- | :--- | :--- | :--- |
| **Residual Open Stray Capacitance ($C_{open}$)** | fF | **$< 20\text{ fF}$** (typically $< 15\text{ fF}$) | 1 MHz open de-embedded sweep at 250 µm elevation |
| **Residual Short Series Resistance ($R_{short}$)** | $\text{m}\Omega$ | **$< 100\ \text{m}\Omega$** (typically $\le 80\ \text{m}\Omega$) | 1 MHz short measurement on Au/Al reference pad |
| **Needle Touchdown Overdrive** | µm | **$35 \pm 5\ \text{µm}$** | Motorized Z-stage micrometer / visual scrub witness mark |
| **Accumulation Thickness Resolution ($t_{ox}$)** | nm | **$3.5\text{ nm} \pm 0.1\text{ nm}$** | Extraction via $C_{ox} = \frac{\varepsilon_{ox}\varepsilon_0 \cdot \text{Area}}{t_{ox}}$ across 200/500/1000 µm dots |

---

### 5. Context Literature Citations
1. **Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction**:
   - Aluminum circular gate dots (diameter 200 µm, 500 µm, 1000 µm) sputtered on thermally grown gate oxide (3.5 nm to 25 nm) on P-type (100) Si; backside substrate Au/Al ohmic contact layer.
   - High-Frequency (1 MHz) accumulation saturation capacitance $C_{ox} = (\varepsilon_{ox}\varepsilon_0 \cdot \text{Area}) / t_{ox}$ yielding physical oxide thickness $t_{ox}$ with $\pm 0.1\text{ nm}$ precision.
2. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - Gate dielectric thermally grown $SiO_2$ at 850°C–900°C dry oxidation with ~3.5 nm physical thickness.

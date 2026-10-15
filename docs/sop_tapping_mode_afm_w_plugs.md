# Standard Operating Procedure (SOP): Tapping-Mode Scan Execution Over Dense Bitline and Storage Node W-Plugs

- **Document ID:** SOP-MET-AFM-180-001
- **Process Step:** Post-CMP Plug Recess Profilometry and Residual Metal Defect Metrology
- **Node/Generation:** 180nm CMOS Open-Source DRAM (DRAM Foundation VN)
- **Cell Architecture:** 1T1C Folded Bitline (8F²: 0.259 µm² / 6F²: 0.194 µm²), Stacked Capacitor Over Bitline (COB)

---

## 1. Scope & Objective
This Standard Operating Procedure defines the precise tapping-mode Atomic Force Microscopy (AFM) profilometry over dense array Tungsten (W) bitline contacts and storage node contact plugs post-tungsten chemical-mechanical planarization (W-CMP) clearing. It validates plug recess depths, array dishing, and dielectric erosion to prevent open/short contacts prior to crown capacitor erection and bitline metallization.

---

## 2. Process Workflow

```text
┌────────────────────────┐
│                        │
│      Wafer Load &      │
│   Pre-Scan Alignment   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Tip Engagement &    │
│    Resonance Tuning    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Tapping-Mode Scan    │
│       Execution        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Topography & Recess   │
│  Metrology Extraction  │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Substrate Load and Optical Site Navigation
1. Load the 200 mm post-W-CMP wafer onto the vibration-isolated, vacuum-clamped AFM chuck.
2. Align to global wafer notch/flat and navigate the motorized stage to the dense memory array test macro.
3. Position optical navigation on the dense 8F² (0.259 µm² footprint) or 6F² (0.194 µm² footprint) array field, locating bitline and wordline grid pitches spanning 360 nm to 400 nm.

### Step 2: Cantilever Calibration and Auto-Tuning
1. Utilize high-aspect-ratio (HAR) silicon AFM probes with tip apex radius $r < 5\text{ nm}$ and tip half-angle $< 10^\circ$ to resolve high aspect ratio 180 nm contact openings.
2. Perform sweep of cantilever resonance frequency in air (nominal $f_0 \approx 300\text{ kHz}$, spring constant $k \approx 40\text{ N/m}$).
3. Set free-air oscillation amplitude $A_0 = 20.0\text{ nm}$.
4. Engage feedback loop with a tapping setpoint ratio ($A_{sp} / A_0$) between $0.75$ and $0.80$ to minimize tip wear and sample lateral shear.

### Step 3: High-Resolution Tapping-Mode Scan Execution
1. Set scan field window to $2.0\,\mu\text{m} \times 2.0\,\mu\text{m}$ across minimum 5 consecutive bitline/wordline pitches ($360\text{ nm} - 400\text{ nm}$ pitch).
2. Set scan grid density to $512 \times 512$ pixels (lateral sampling resolution $\approx 3.9\text{ nm/pixel}$, ensuring $>45$ pixels across each 180 nm plug diameter).
3. Execute raster scan at line scan rate of $1.0\text{ Hz}$ ($4.0\,\mu\text{m/s}$ tip velocity) along the orthogonal axis to the bitline running direction (fast axis).
4. Maintain proportional/integral (P/I) feedback gain optimized to eliminate error tracking lag while suppressing tip ringing.

### Step 4: Metrology Profile Extraction & Defect Flagging
1. Apply 1st-order line-by-line planarization flattening across the Inter-Layer Dielectric (ILD) field reference plane.
2. Extract cross-sectional depth profiles through the centers of access transistor drain/source W-plugs (channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$).
3. Measure individual W-plug recess depth relative to surrounding ILD surface.
4. Calculate array-level CMP dishing across the dense array block.

---

## 4. Acceptance Criteria & Target Metrics

| Parameter | Target Specification | Tolerance / Upper Limit | Measurement Unit |
| :--- | :--- | :--- | :--- |
| **W-Plug Recess Depth** | 15.0 | 5.0 to 25.0 | nm |
| **Dense Array W-CMP Dishing** | $\le 15.0$ | $\le 25.0$ | nm |
| **Contact Pitch Fidelity** | 360.0 to 400.0 | $\pm 5.0$ | nm |
| **Array RMS Roughness ($R_q$)** | $\le 0.35$ | $\le 0.50$ | nm |

```text
                  AFM Metrology Key Parameters (nm & Hz)
                   ┌───────────────────────────────────┐
                   │██                                 │
     Scan Line Rate┤██                                 │
                   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       │
 Tip Res. Amplitude┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       │
   Max Dishing Spec┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
                   │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Recess Depth Target┤░░░░░░░░░░░░░░░░░░░░░              │
                   │░░░░░░░░░░░░░░░░░░░░░              │
                   └┬────────┬───────┬────────┬───────┬┘
                   0.0      6.2    12.5     18.8   25.0 
```

---

## 5. Literature Citations & Physical Context
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry defines access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$. Bitline contact shared between two adjacent memory cells. Stacked capacitor erected above drain contact via tungsten plug (W-plug).
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: Bitline and wordline pitch is approximately $360\text{ nm}$ to $400\text{ nm}$. Storage capacitor target $C_s \ge 25\text{ fF}$ to $30\text{ fF}$ per cell.
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**: 8F² folded bitline footprint ($0.259\,\mu\text{m}^2$) and 6F² open bitline footprint ($0.194\,\mu\text{m}^2$) at $F = 180\text{ nm}$. Storage node capacitance $C_s \ge 25\text{ fF} - 30\text{ fF}$ (nominally $28\text{ fF}$).

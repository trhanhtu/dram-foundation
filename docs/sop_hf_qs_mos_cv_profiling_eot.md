# SOP: High-Frequency & Quasi-Static MOS C-V Profiling & EOT Extraction

- **Document ID**: SOP-MET-MOSCV-002
- **Node**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Module**: Metrology & Thin Film Dielectric Characterization
- **Structure**: Planar MOSCAP Test Vehicle (Circular Gate Dots on P-type (100) Si)
- **Status**: Released

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) governs high-frequency (HF, 1 MHz) and quasi-static (QS) capacitance-voltage ($C$-$V$) profiling on test planar MOS capacitors (MOSCAP) fabricated within the 180nm front-end line. The metrology sequence quantifies oxide capacitance in strong accumulation ($C_{ox}$), verifies low-frequency inversion response, and precisely extracts the Equivalent Oxide Thickness (EOT) with $\pm 0.1\text{ nm}$ resolution.

---

## 2. Test Structure & Tooling Architecture

- **Substrate**: P-type (100) Silicon with Au or Al backside ohmic contact.
- **Top Gate Dots**: Sputtered Aluminum circular dots with nominal diameters of $200\ \mu\text{m}$, $500\ \mu\text{m}$, or $1000\ \mu\text{m}$.
- **Metrology Tooling**: LCR meter / Impedance analyzer (1 MHz AC signal, $V_{ac} = 15\text{--}30\text{ mV}$) combined with Quasi-Static electrometer / SMU ramp generator ($dV/dt = 10\text{--}100\text{ mV/s}$) mounted on a shielded, dark probe station chuck.

```text
┌────────────────────────┐
│                        │
│  Start: MOSCAP Wafer   │
│        Loading         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Backside Ohmic     │
│     Contact Check      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   HF 1 MHz C-V Sweep   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Quasi-Static C-V    │
│          Ramp          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Cox Saturation & EOT  │
│       Extraction       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Acceptance Gate     │
│        Decision        │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Execution

### Step 1: Wafer Loading & Chuck Grounding
1. Mount the wafer onto the vacuum chuck inside the light-tight Faraday cage enclosure.
2. Verify substrate contact resistance across the Au/Al backside layer ($R_{series} < 10\ \Omega$).
3. Lower the tungsten/beryllium-copper probe tip onto a chosen Aluminum circular dot ($200\ \mu\text{m}$, $500\ \mu\text{m}$, or $1000\ \mu\text{m}$ diameter) with controlled micro-stepping to prevent dielectric puncture.

### Step 2: High-Frequency (1 MHz) C-V Sweep
1. Configure the AC oscillation level to $v_{ac} = 20\text{ mV}$ RMS at $f = 1\text{ MHz}$.
2. Perform DC bias sweep from inversion to strong accumulation ($V_G = +2.0\text{ V} \rightarrow -2.5\text{ V}$ for P-type substrate) at a sweep rate of $50\text{ mV/s}$.
3. In strong accumulation ($V_G < V_{fb}$), verify saturation of capacitance at maximum $C_{ox}$:
   $$C_{ox} = \frac{\varepsilon_{ox} \cdot \varepsilon_0 \cdot \text{Area}}{t_{ox}}$$
4. Confirm depletion shelf minimum ($V_{fb} < V_G < V_T$) where high-frequency inversion capacitance remains flat and unrecovered due to minority carrier lifetime limitation.

### Step 3: Quasi-Static C-V Profiling
1. Set the electrometer to linear ramp mode with displacement current sensing:
   $$I_{QS} = C_{QS}(V) \cdot \frac{dV}{dt}$$
2. Ramp gate voltage at $dV/dt = 20\text{ mV/s}$ from $-2.5\text{ V}$ to $+2.0\text{ V}$ under dark, equilibrium conditions.
3. Verify that in strong inversion ($V_G > V_T$), quasi-static capacitance $C_{QS}$ recovers back toward $C_{ox}$ due to thermal generation-recombination matching the ramp rate.

### Step 4: Extraction & Correction Formulation
1. Extract saturated accumulation capacitance $C_{max} \equiv C_{ox}$ at $V_G = -2.5\text{ V}$.
2. Extract physical/equivalent oxide thickness:
   $$\text{EOT} = \frac{\varepsilon_{SiO2} \cdot \varepsilon_0 \cdot \pi (d/2)^2}{C_{ox}}$$
   where $\varepsilon_{SiO2} = 3.9$, $\varepsilon_0 = 8.854 \times 10^{-14}\text{ F/cm}$, and $d \in \{200\ \mu\text{m}, 500\ \mu\text{m}, 1000\ \mu\text{m}\}$.
3. Compare HF and QS curves to evaluate interface trap density ($D_{it}$) and ensure profile validity.

---

## 4. Machine-Measurable Acceptance Criteria

```text
                        Target Acceptance Limits        
                 ┌─────────────────────────────────────┐
                 │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
Min Cap (fF/cell)┤░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
  EOT High-k (nm)┤▒▒▒▒▒▒                               │
                 │▒▒▒▒▒▒                               │
 EOT Gate Ox (nm)┤██████                               │
                 │██████                               │
                 └┬────────┬────────┬────────┬────────┬┘
                  0        7       14       21       28 
```

| Metric / Parameter | Target Value | Tolerance / Range | Unit | Diagnostic Method |
| :--- | :--- | :--- | :--- | :--- |
| **Thermally Grown Gate Oxide Thickness ($t_{ox}$ / EOT)** | `3.5` | `± 0.1` | `nm` | Extracted from HF 1 MHz $C_{ox}$ saturation |
| **Stacked Capacitor High-k Dielectric EOT** | `3.5` | `3.0 to 4.0` | `nm` | Extracted from high-k test structures ($\kappa > 15$) |
| **Cell Storage Capacitance ($C_{cell}$)** | `≥ 28.0` | `25.0 to 30.0` min | `fF/cell` | Integrated capacitance budget |
| **Sub-threshold & Junction Leakage Current** | `< 1.0` | Upper limit at 85°C | `fA/cell` | Static current metrology |

---

## 5. Literature Citations
- **Source 1**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench* (Unit geometry $L = 180\text{ nm}$, $W = 220\text{ nm}$; high-k stack $\kappa > 15$; min capacitance budget $28\text{ fF/cell}$; leakage target $< 1\text{ fA/cell}$ at 85°C).
- **Source 2**: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering* (Stacked capacitor EOT $3\text{ to }4\text{ nm}$; retention baseline $> 64\text{ ms}$; cell capacitance $25\text{ to }30\text{ fF}$; gate oxide dry oxidation ~3.5 nm).
- **Source 3**: *Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction* (Aluminum gate dots $200\ \mu\text{m}$, $500\ \mu\text{m}$, $1000\ \mu\text{m}$ on P-type (100) Si; Au/Al backside contact; 1 MHz HF & Quasi-Static sweep regions; $C_{ox}$ saturation extraction yielding $t_{ox}$ with $\pm 0.1\text{ nm}$ precision).

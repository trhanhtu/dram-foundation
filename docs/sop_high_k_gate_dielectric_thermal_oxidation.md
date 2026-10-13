# Standard Operating Procedure (SOP): High-K Gate Dielectric & Thin Film Thermal Oxidation Line

- **Document ID**: SOP-FAB-FEOL-180-OX01
- **Node / Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > Front-End Fabrication
- **Generation**: Gen 2 (µm) / 180nm Node
- **Action Type**: Make
- **Status**: Released / Operational

---

## 1. Process Overview & Flow

```text
┌─────────────────────┐
│    RCA Clean and    │
│   Pre-Gate HF Dip   │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   Dry O2 Thermal    │
│    Oxidation at     │
│      850C-900C      │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  High-K Dielectric  │
│     Deposition      │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  Ellipsometry and   │
│ Breakdown Metrology │
└─────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Pre-Oxidation Surface Preparation (RCA Clean & HF Dip)
1. Clean 180nm silicon substrate wafers through standard RCA-1 (organic strip: $NH_4OH:H_2O_2:H_2O$) and RCA-2 (metallic clean: $HCl:H_2O_2:H_2O$) baths.
2. Perform a diluted HF (1%–2%) dip to strip native chemical oxide and achieve a hydrophobic hydrogen-terminated silicon surface immediately prior to furnace loading.
3. Rinse in ultra-pure deionized (DI) water ($18.2\text{ M}\Omega\cdot\text{cm}$) and spin-dry in an inert $N_2$ atmosphere.

### Step 2: Quartz Tube Furnace Idle & Ramp-Up
1. Idle the quartz furnace tube in high-purity dry $N_2$ purge gas flow at $650^\circ\text{C}$ to prevent thermal shock and ambient air backflow.
2. Load wafer boat into the flat thermal zone of the quartz process tube.
3. Ramp furnace temperature under continuous $N_2$ purge to the dry oxidation target range of **$850^\circ\text{C}$ to $900^\circ\text{C}$** at a controlled ramp rate ($\le 10^\circ\text{C}/\text{min}$).

### Step 3: Deal-Grove Linear-Regime Thin Thermal Oxidation
1. Stabilize quartz tube temperature within **$850^\circ\text{C}$ to $900^\circ\text{C}$** ($\pm 0.5^\circ\text{C}$ flat zone profile).
2. Switch gas purge to ultra-dry process $O_2$ (carrier grade $\ge 99.999\%$).
3. Maintain dry oxidation dwell in the linear reaction-rate-limited regime ($x_0 \ll A/2$, rate constant $k_l = B/A$) to grow dense $SiO_2$ gate oxide target of **$3.5\text{ nm}$ to $4.0\text{ nm}$** physical thickness.
4. Switch atmosphere back to pure dry $N_2$ for post-oxidation anneal (10–15 min at $850^\circ\text{C}$–$900^\circ\text{C}$) to passivate interface traps ($D_{it} < 10^{10}\text{ cm}^{-2}\text{ eV}^{-1}$).
5. Ramp furnace down to $650^\circ\text{C}$ under $N_2$ and un-boat wafers.

### Step 4: High-K Dielectric Integration
1. For capacitor cell integration, transfer wafers to the high-k thin film deposition chamber.
2. Deposit high-k dielectric stack ($Ta_2O_5$ / $Al_2O_3$ or $ONO$ / $Si_3N_4$) targeting an Equivalent Oxide Thickness (EOT) of **$3\text{ nm}$ to $4\text{ nm}$** and an effective dielectric constant $\kappa > 15$.
3. Execute post-deposition in-situ densification anneal.

### Step 5: Inline Physical and Electrical Metrology
1. Measure film physical thickness across 9 test sites per wafer using multi-angle spectroscopic ellipsometry.
2. Conduct C-V and I-V test structure probe:
   - Verify dielectric breakdown field $E_{bd} > 10\text{ MV/cm}$.
   - Verify cell capacitance $\ge 28\text{ fF/cell}$ (within the $25\text{ to }30\text{ fF}$ capacitance budget).
   - Verify cell leakage $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$.

---

## 3. Acceptance Criteria & Target Metrics

```text
                  Dielectric Process Target Metrics     
             ┌─────────────────────────────────────────┐
             │░░░░░                                    │
     EOT (nm)┤░░░░░                                    │
             │▒▒▒▒▒▒                                   │
Gate Tox (nm)┤▒▒▒▒▒▒                                   │
Cap/Cell (fF)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
             │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
 E_bd (MV/cm)┤███████████████                          │
             │███████████████                          │
             └┬─────────┬─────────┬─────────┬─────────┬┘
              0         7        14        21        28 
```

| Parameter / Metric | Target Value | Physical Unit | Measurement Method / Tool | Verification Tolerance |
| :--- | :--- | :--- | :--- | :--- |
| **Furnace Dry Oxidation Temperature** | `850 to 900` | $^\circ\text{C}$ | Multi-zone thermocouple array | $\pm 0.5^\circ\text{C}$ |
| **Thermally Grown Gate Oxide Thickness ($T_{ox}$)** | `3.5 to 4.0` | $\text{nm}$ | Spectroscopic Ellipsometry | $\pm 0.1\text{ nm}$ |
| **Equivalent Oxide Thickness (EOT)** | `3.0 to 4.0` | $\text{nm}$ | High-Frequency C-V Metrology | $\pm 0.2\text{ nm}$ |
| **Dielectric Breakdown Field Strength ($E_{bd}$)** | `> 10` | $\text{MV/cm}$ | Ramp-voltage I-V dielectric breakdown | Lower specification limit |
| **Storage Node Unit Cell Capacitance** | `25 to 30` (Min `28`) | $\text{fF/cell}$ | Automated parametric tester C-V ($85^\circ\text{C}$) | $\ge 28\text{ fF}$ nominal |
| **Dielectric Junction / Sub-threshold Leakage** | `< 1` | $\text{fA/cell}$ ($85^\circ\text{C}$) | Picoammeter parametric wafer probe | Upper specification limit |

---

## 4. Literature & Context Citations

1. **Source: Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace**:
   - Linear-parabolic kinetic model ($x_0^2 + A x_0 = B(t + \tau)$) in the interface reaction-rate-limited regime ($k_l = B/A$).
   - Dry oxidation parameter window: $900^\circ\text{C} - 1000^\circ\text{C}$ (and $850^\circ\text{C} - 900^\circ\text{C}$) in pure dry $O_2$.
   - Dielectric breakdown target $E_{bd} > 10\text{ MV/cm}$, interface trap density $D_{it} < 10^{10}\text{ cm}^{-2}\text{ eV}^{-1}$, and gate dielectric physical thickness of $3.5\text{ nm to }4.0\text{ nm}$.
2. **Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - Gate dielectric thermally grown $SiO_2$ at $850^\circ\text{C} - 900^\circ\text{C}$ dry oxidation with $\sim 3.5\text{ nm}$ physical thickness.
   - Stacked capacitor dielectric ($Si_3N_4$ or $Ta_2O_5$) with Equivalent Oxide Thickness (EOT) around $3\text{ to }4\text{ nm}$.
   - Minimum cell storage capacitance of $25\text{ to }30\text{ fF/cell}$ for $> 64\text{ ms}$ retention at $85^\circ\text{C}$.
3. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry $L = 180\text{ nm}$, $W = 220\text{ nm}$.
   - High-k dielectric stack ($Ta_2O_5 / Al_2O_3$ or ONO) with $\kappa > 15$.
   - Capacitance budget: Minimum $28\text{ fF/cell}$; leakage current target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

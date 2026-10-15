# Standard Operating Procedure (SOP)
## Post-Anneal Interface Trap Density ($D_{it}$) & Al-Si Contact Resistance Metrology

- **Date**: 2026-10-15
- **Generation**: Gen 3 (180nm Open-Source DRAM Chip - DRAM Foundation VN)
- **Node Context**: 180nm CMOS Commercial MPW Tapeout & PDK Implementation > BEOL Multi-Layer Metallization > Post-Anneal Metrology
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented

---

## 1. Process Overview & Workflow

Post-metal forming gas anneal ($N_2/H_2$ 95/5 at 400°C for 30 minutes) serves two critical metallurgical and electrical functions:
1. Passivates silicon/gate-dielectric dangling bonds with atomic hydrogen, driving the interface trap density ($D_{it}$) to target levels.
2. Forms a low-barrier, ohmic Al-Si contact interface while preserving interconnect film properties.

```text
┌────────────────────────┐
│   Wafer Unload from    │
│  Forming Gas Furnace   │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│        Quench &        │
│    Stabilization to    │
│          25°C          │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│     4-Point Probe      │
│     Metal-1 Sheet      │
│       Resistance       │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│     Quasi-Static &     │
│   High-Frequency C-V   │
│       Metrology        │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│   Kelvin Structure &   │
│      TLM Contact       │
│  Resistance Metrology  │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  Statistical Process   │
│     Verification &     │
│        Binning         │
└────────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Wafer Loading & Temperature Stabilization
1. Transfer post-forming gas annealed 180nm wafer lot from the nitrogen purge cooling station to the automated metrology station.
2. Ensure wafer stage temperature stabilizes at $25.0 \pm 0.5^\circ\text{C}$ in a cleanroom ambient ($<45\%$ RH).
3. Align wafer notch to index position $0^\circ$ on the vacuum chuck.

### Step 2: In-Line 4-Point Probe Metal-1 Sheet Resistance ($R_s$)
1. Position the standard 4-point probe head (tungsten carbide tips, 1.0 mm tip spacing, 100g probe loading) over 49-point wafer mapping sites.
2. Apply forward and reverse current $I = 10.0\text{ mA}$ through outer probes (1 and 4).
3. Measure potential drop $V_{23}$ between inner probes (2 and 3).
4. Calculate sheet resistance:
   $$R_s = \frac{\pi}{\ln(2)} \cdot \frac{V_{23}}{I} \cdot F_{\text{geom}}$$
5. Verify sheet resistance against the target $R_s < 0.08\ \Omega/\Box$.

### Step 3: High-Frequency / Quasi-Static C-V Metrology for Interface Trap Density ($D_{it}$)
1. Direct the automated probe card to MOS capacitor PCM (Process Control Monitor) test structures on scribe lines ($A = 100\ \mu\text{m} \times 100\ \mu\text{m}$, gate dielectric $t_{ox} = 3.5\text{ to }4.0\text{ nm}$).
2. Execute High-Frequency Capacitance-Voltage measurement:
   - AC small signal: $f = 1.0\text{ MHz}$, $V_{ac} = 15\text{ mV}$.
   - DC gate bias sweep: $-2.5\text{ V} \to +2.5\text{ V}$ at step size $20\text{ mV}$.
3. Execute Quasi-Static Capacitance-Voltage (QSCV) measurement:
   - Ramp rate: $dV/dt = 50\text{ mV/s}$.
   - Measure displacement current $I_{qs}$ to extract $C_{qs} = I_{qs} / (dV/dt)$.
4. Extract interface trap density across the bandgap using High-Low Frequency method:
   $$D_{it} = \frac{C_{ox}}{q} \left( \frac{C_{qs}/C_{ox}}{1 - C_{qs}/C_{ox}} - \frac{C_{hf}/C_{ox}}{1 - C_{hf}/C_{ox}} \right)$$
5. Confirm minimum mid-gap $D_{it} < 1.0 \times 10^{10}\ \text{cm}^{-2}\text{eV}^{-1}$.

### Step 4: Al-Si Contact Resistance Metrology (Kelvin & TLM Structures)
1. Index probe tips to four-terminal Kelvin test structures (Al contact to n+ / p+ active diffusion, contact area $0.22\ \mu\text{m} \times 0.22\ \mu\text{m}$).
2. Force current $I = 100\ \mu\text{A}$ through contact line; sense voltage drop $V_k$ across active tap.
3. Compute specific contact resistance:
   $$R_c = \frac{V_k}{I} \cdot A_{\text{contact}}$$
4. Traverse to Transfer Length Method (TLM) pad arrays (pad widths $W = 10\ \mu\text{m}$, inter-contact spacings $L = 0.5, 1.0, 2.0, 4.0, 8.0\ \mu\text{m}$).
5. Measure total resistance $R_{\text{total}}$ vs. contact spacing $L$; extract contact resistance $R_c$ from the y-intercept ($2R_c$) and transfer length $L_T$ from the x-intercept ($-2L_T$).

---

## 3. Acceptance Criteria Target Metrics

| Parameter | Metrology Target | Unit | Physical Mechanism / Impact |
| :--- | :--- | :--- | :--- |
| **Metal-1 Sheet Resistance ($R_s$)** | $< 0.08$ | $\Omega/\Box$ | Ensures grain coalescence & Al-Cu electrical conductivity at $350\text{ nm}$ nominal thickness. |
| **Interface Trap Density ($D_{it}$)** | $< 1.0 \times 10^{10}$ | $\text{cm}^{-2}\text{eV}^{-1}$ | Measures hydrogen passivation of dangling bonds at $3.5\text{--}4.0\text{ nm}$ gate oxide interface. |
| **Gate Oxide Breakdown Field ($E_{bd}$)** | $> 10.0$ | $\text{MV/cm}$ | Validates dielectric breakdown integrity following thermal stress of forming gas anneal. |
| **Specific Contact Resistivity ($\rho_c$)** | $< 5.0 \times 10^{-7}$ | $\Omega\cdot\text{cm}^2$ | Confirms barrier thinning and native oxide reduction at Al-Si interface. |

```text
                            Metrology Acceptance Targets
                             ┌─────────────────────────┐
                             │■■■■■■■■■■■■■■■■■■■■■■■■■│
            Al-Si Rc (Ohm-um)┤■■■■■■■■■■■■■■■■■■■■■■■■■│
Gate Dit (x10^10 cm^-2 eV^-1)┤█████████                │
                             │█████████                │
            Al M1 Rs (Ohm/sq)┤▒▒                       │
                             │▒▒                       │
                             └┬─────┬─────┬─────┬─────┬┘
                            0.00  0.70  1.40  2.10 2.80 
```

---

## 4. Literature & Context Citations

1. **Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects**:
   - Forming gas anneal conditions: $N_2/H_2$ 95/5 at $400^\circ\text{C}$ for 30 minutes.
   - Metal-1 nominal thickness: $350\text{ nm} \pm 5\%$.
   - Post-anneal sheet resistance specification: $R_s < 0.08\ \Omega/\Box$.
2. **Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace**:
   - Gate oxide physical thickness: $3.5\text{ to }4.0\text{ nm}$.
   - Gate dielectric breakdown electric field: $E_{bd} > 10\text{ MV/cm}$.
   - Interface trap density target: $D_{it} < 10^{10}\ \text{cm}^{-2}\text{eV}^{-1}$.

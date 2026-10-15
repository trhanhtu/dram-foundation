# SOP: ALD Chamber Conditioning and TiCl4/NH3 Precursor Pulse Calibration

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Process Tier**: 180nm Open-Source DRAM Chip (Gen 3 nm) / 3D Crown Capacitor Conformal TiN Top Metal Electrode Deposition

## Overview & Rationale
In the 180nm DRAM cell architecture with 8F² / 6F² stacked crown capacitors over bitline (COB), conformal titanium nitride (TiN) acts as the top metal electrode capping the high-k capacitor dielectric (such as Ta₂O₅, Al₂O₃, or ONO stacks). Achieving uniform step coverage, low resistivity, and stoichiometric TiN across deep 3D high-aspect-ratio crown structures requires thermal Atomic Layer Deposition (ALD) driven by alternating pulses of titanium tetrachloride ($\text{TiCl}_4$) and ammonia ($\text{NH}_3$).

Prior to production deposition, ALD chamber wall conditioning and precursor pulse/purge time calibration must be performed. Conditioning passivates internal stainless steel / quartz reactor surfaces to establish steady-state chemical equilibrium and eliminate base-pressure contaminant outgassing. Precise precursor pulse-dose and purge calibration ensures saturation within the self-limiting ALD regime without precursor condensation or gas-phase parasitic CVD reactions, guaranteeing low leakage (< 1 fA/cell) and high capacitance retention (> 25 to 30 fF/cell).

## Conditioning & Pulse Calibration Workflow

```text
┌──────────────────────────────────────────────┐
│                                              │
│   Chamber Bakeout & Base Vacuum Pump-Down    │
│            (< 2.0e-6 Torr Check)             │
│                                              │
└──────────────────────┬───────────────────────┘
                       │
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                                              │
│    Thermal Wall & Stage Temperature Soak     │
│             (T_stage: 380°C - 420°C)         │
│                                              │
└──────────────────────┬───────────────────────┘
                       │
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                                              │
│     Chamber Wall Passivation Conditioning    │
│        (50 Dummy Cyclic ALD TiN Pulses)      │
│                                              │
└──────────────────────┬───────────────────────┘
                       │
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                                              │
│    Precursor Pulse & Purge Dose Saturation   │
│     Calibration (TiCl4 & NH3 Fast Valves)    │
│                                              │
└──────────────────────┬───────────────────────┘
                       │
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                                              │
│   GPC Growth & Uniformity Test Verification  │
│         (Ellipsometry / 4-Point Probe)       │
│                                              │
└──────────────────────────────────────────────┘
```

## Step-by-Step Procedure

### 1. Chamber Evacuation and Base Vacuum Verification
1. Verify all precursor isolation valves (pneumatic ALD AL-valves) for $\text{TiCl}_4$ and anhydrous $\text{NH}_3$ are in the closed interlock state.
2. Engage the dry roots blower backed by the turbomolecular pump (TMP) / cryopump train.
3. Pump down the reaction chamber to verify ultimate base vacuum level. Ensure base pressure pumps down below $2.0 \times 10^{-6}\text{ Torr}$ to eliminate ambient moisture ($\text{H}_2\text{O}$) and atmospheric oxygen ($\text{O}_2$) outgassing.
4. Perform an automated vacuum rate-of-rise (ROR) leak check: isolate the pumping foreline valve for 60 seconds. Confirm chamber leak-back rate is $< 0.5\text{ mTorr/min}$.

### 2. Reactor Thermal Stabilization & Gas Flow Balancing
1. Energize multi-zone heater controllers: set reactor outer wall heating jacket to $150^\circ\text{C} \pm 2^\circ\text{C}$ (to prevent $\text{TiCl}_4$ and reaction byproduct $\text{NH}_4\text{Cl}$ cold-spot condensation) and delivery gas line jackets to $120^\circ\text{C} \pm 2^\circ\text{C}$.
2. Set substrate stage / pedestal heater to the thermal ALD process temperature between $380^\circ\text{C}$ and $420^\circ\text{C}$ (setpoint: $400^\circ\text{C} \pm 1.0^\circ\text{C}$). Allow a 30-minute thermal soak until thermocouple readouts stabilize within $\pm 0.5^\circ\text{C}$.
3. Initiate continuous ultra-high-purity (UHP 99.999% / 5N) carrier and purge gas flows:
   - Nitrogen ($\text{N}_2$) or Argon ($\text{Ar}$) carrier line A ($\text{TiCl}_4$ manifold): $100\text{ sccm}$.
   - Nitrogen ($\text{N}_2$) or Argon ($\text{Ar}$) carrier line B ($\text{NH}_3$ manifold): $100\text{ sccm}$.
   - Continuous bottom ballast/exhaust purge flow: $50\text{ sccm}$.
4. Throttle the downstream dry-pump pendulum throttle valve to establish a steady dynamic process operating pressure of $0.8\text{ Torr}$ to $1.2\text{ Torr}$.

### 3. Precursor Delivery Line Preparation & Chamber Conditioning
1. Maintain the $\text{TiCl}_4$ liquid precursor bubbler source cabinet at $25^\circ\text{C} \pm 0.5^\circ\text{C}$ via recirculating bath (yielding equilibrium vapor pressure $\approx 10\text{ Torr}$).
2. Supply electronic-grade anhydrous $\text{NH}_3$ (99.999%) through a dedicated point-of-use (POU) purifier at an inlet delivery pressure of $15\text{ psig} \pm 1\text{ psig}$.
3. Load a conditioning dummy silicon wafer (200mm bare monitor substrate) onto the heated chuck via the load-lock transfer robot.
4. Run a 50-cycle pre-conditioning recipe to coat and passivate all active reactor surfaces:
   - Sequence: $\text{TiCl}_4\text{ pulse } (0.20\text{ s}) \rightarrow \text{Purge } (3.0\text{ s}) \rightarrow \text{NH}_3\text{ pulse } (0.30\text{ s}) \rightarrow \text{Purge } (3.0\text{ s})$.
5. Verify chamber residual gas analyzer (RGA) or downstream foreline pressure traces show consistent, symmetric transient pressure spikes across each cycle.

### 4. TiCl4 / NH3 Precursor Pulse & Purge Time Calibration
1. Load a freshly prepared test coupon or monitor wafer with a pre-measured thermal native oxide/high-k test stack.
2. **TiCl₄ Pulse Time Optimization**:
   - Fix $\text{NH}_3$ pulse at $0.30\text{ s}$ and purge times at $4.0\text{ s}$.
   - Vary $\text{TiCl}_4$ high-speed ALD valve pulse width across four test runs: $0.05\text{ s}$, $0.10\text{ s}$, $0.20\text{ s}$, and $0.35\text{ s}$ for 100 cycles each.
   - Measure deposited TiN thickness via spectroscopic ellipsometry to identify the ALD chemisorption saturation knee point. Confirm saturated pulse width at $0.15\text{ s} - 0.20\text{ s}$ where growth per cycle (GPC) plateaus.
3. **NH₃ Pulse Time Optimization**:
   - Set calibrated $\text{TiCl}_4$ pulse to $0.20\text{ s}$.
   - Vary $\text{NH}_3$ co-reactant pulse width across four test runs: $0.10\text{ s}$, $0.20\text{ s}$, $0.30\text{ s}$, and $0.50\text{ s}$.
   - Determine full surface nitridation saturation point, establishing standard operational pulse duration at $0.25\text{ s} - 0.30\text{ s}$.
4. **Purge Interlock Optimization**:
   - Systematically decrease inert purge duration from $5.0\text{ s}$ down to $1.5\text{ s}$.
   - Ensure inter-precursor purge duration ($> 2.5\text{ s}$, nominal $3.0\text{ s}$) completely sweeps out physisorbed species and unreacted $\text{HCl}$ / $\text{NH}_4\text{Cl}$ byproducts, preventing gas-phase parasitic CVD reactions and particle formation.

## Acceptance Criteria

| Parameter | Target Specification | Measurement Method / Tool | Pass/Fail Interlock |
| :--- | :--- | :--- | :--- |
| **Chamber Base Vacuum** | $< 2.0 \times 10^{-6}\text{ Torr}$ | Penning / Bayard-Alpert Ion Gauge | Abort recipe if base pressure $> 2.0 \times 10^{-6}\text{ Torr}$ |
| **Growth Per Cycle (GPC)** | $0.022\text{ nm/cycle} \pm 0.003\text{ nm/cycle}$ ($0.22\text{ Å/cycle} \pm 0.03\text{ Å/cycle}$) | Spectroscopic Ellipsometry (multi-angle 45-site map) | Out of saturation limit if $\Delta\text{GPC} > \pm 0.003\text{ nm/cycle}$ |
| **Within-Wafer Film Uniformity (WIWNU)** | $< 2.5\%\text{ (1}\sigma\text{)}$ across 200mm wafer ($3\text{mm}$ edge exclusion) | 49-point automated spectroscopic ellipsometry | Recalibrate gas manifold purge balance if $\sigma > 2.5\%$ |
| **TiN Film Resistivity ($\rho$)** | $< 180\ \mu\Omega\cdot\text{cm}$ (equivalent to $R_s < 90\ \Omega/\text{sq}$ for $20\text{ nm}$ film) | In-line 4-Point Resistivity Probe (4PP) | Reject if residual chlorine ($\text{Cl}$) incorporation spikes resistivity $\ge 200\ \mu\Omega\cdot\text{cm}$ |

## Context Citations & Technical References
1. **Source: 180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**
   - High-aspect-ratio crown-shaped metal-insulator-metal (MIM) capacitor structure erected above drain contacts via tungsten plugs (W-plugs); capacitor budget requiring $> 28\text{ fF/cell}$ and leakage current $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ requires atomically conformal, pinhole-free TiN top metal electrode capping.
2. **Source: Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**
   - 1T1C stacked capacitor (Crown / Cylinder type) cell layout targeting $25\text{ to }30\text{ fF/cell}$ storage capacitance with high-k dielectrics ($3\text{ to }4\text{ nm}$ EOT); necessitates self-limiting cyclic deposition to avoid thermal degradation or excessive equivalent oxide thickness variation.
3. **Source: Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects**
   - Vacuum chamber base pressure criteria baseline ($< 2.0 \times 10^{-6}\text{ Torr}$) utilizing turbomolecular or cryogenic high-vacuum pumping systems to prevent oxygen incorporation and background contamination.

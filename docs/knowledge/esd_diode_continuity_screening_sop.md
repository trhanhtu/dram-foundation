# ESD Protection Diode Forward-Bias Continuity & Open/Short Contact Screening SOP

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented
- **Generation**: Gen 3 (180nm CMOS Commercial MPW Tapeout & PDK Implementation)

## Overview & Rationale
During Electrical Die Sort (EDS) on 180nm DRAM wafers, verifying probe needle-to-pad physical contact and integrity of on-chip electrostatic discharge (ESD) protection networks is the essential prerequisite before applying operating core potentials (e.g. nominal $V_{DD} = 1.8\text{ V}$, boosted wordline pump $V_{PP} \ge 2.5\text{ V}\text{ to }2.8\text{ V}$). An open needle or defective ESD diode can cause misclassification, latch-up, or false functional test aborts.

Screening evaluates the forward-biased substrate/ESD clamping p-n diodes across every pin relative to $V_{SS}$ and $V_{DD}$.

## Screening Execution Flow
```text
┌────────────────────────┐
│   Start: Wafer Chuck   │
│    Loaded & Aligned    │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│      Ground VSS /      │
│    Substrate Common    │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  Force Test Current:   │
│   IF = -100 uA to -1   │
│           mA           │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  Measure Voltage Drop  │
│       VF on Pad        │
└────────────┬───────────┘
             │
             ▼
┌────────────◇───────────┐
│    Evaluate Voltage    │
│         Window         │
└────────────◇───────────┘
             │
             ├────────────────────────────────────────────────╮
             │                                                │
  VF < -0.2 V│                                                │ -0.9 V <= VF <= -0.5 V
             ├────────────────────────────────────────────────┼────────────────────────────────────────────────╮
             ▼                                                ▼                                                ▼ VF > -0.9 V / Clamp
┌────────────────────────┐                       ┌────────────────────────┐                       ┌────────────────────────┐
│  FAIL: Short to GND /  │                       │    PASS: Intact ESD    │                       │  FAIL: Open Contact /  │
│      Low-R Bridge      │                       │     Diode & Probe      │                       │     Lifted Needle      │
└────────────────────────┘                       └────────────┬───────────┘                       └────────────────────────┘
                                                              │
             ╭────────────────────────────────────────────────╯
             ▼
┌────────────────────────┐
│  Proceed to VDD Clamp  │
│       Test / DC        │
│      Parametrics       │
└────────────────────────┘
```

## Screening Voltage Limits
```text
                     ┌─────────────────────────────────┐
                     │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Open (> -0.9V/Vclamp)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
         Nominal Pass┤████████████████                 │
                     │████████████████                 │
      Short (< -0.2V)┤░░░░░                            │
                     │░░░░░                            │
                     └┬───────┬───────┬───────┬───────┬┘
                    0.00    0.38    0.75    1.12   1.50 
```

## Step-by-Step Procedure
1. **Chuck Loading & Vacuum Hold**: Load 180nm DRAM wafer onto temperature-controlled thermal chuck (baseline sort temperature at $25^\circ\text{C}$ or $85^\circ\text{C}$).
2. **Micro-Cantilever Alignment**: Align cantilever probe needles to bond pad center coordinates with contact overdrive set between $35\,\mu\text{m}$ to $50\,\mu\text{m}$ to pierce aluminum oxide passivation.
3. **Tester Ground Configuration**: Tie all tester ground channels, die $V_{SS}$, and p-substrate return pins to common system ground ($0.0\text{ V}$).
4. **Current Force (Negative Bias - Substrate Diode)**: Using automated parametric measurement unit (PMU / SMU), force forward test current $I_F = -100\,\mu\text{A}$ (per-pin parametric test) or $-1.0\text{ mA}$ into each test pad with compliance voltage clamp set to $-1.5\text{ V}$.
5. **Voltage Measurement & Evaluation**:
   - Measure resulting forward voltage drop $V_F$ within $1.5\text{ ms}$ settling time.
   - If $|V_F| < 0.2\text{ V}$: Flag bin as **SHORT** (metallization bridge, damaged dielectric, or blown ESD clamp).
   - If $0.5\text{ V} \le |V_F| \le 0.9\text{ V}$: Bin status **PASS** (normal silicon p-n diode forward conduction).
   - If $|V_F| \ge 1.4\text{ V}$ (voltage clamp triggered): Flag bin as **OPEN** (probe needle lifted, particulate contamination, or open via/contact).
6. **Positive Bias ($V_{DD}$ Rail ESD Diode)**: Connect $V_{DD}$ rail to tester ground, float other pins, and force $+100\,\mu\text{A}$ to measure the upper clamping diode ($V_F \in [0.5\text{ V}, 0.9\text{ V}]$).
7. **Release & Gate Functional Tests**: Upon $100\%$ pad pass across all DQ, Addr, Command, and Power pins, gate subsequent high-voltage charge pump ($V_{PP} \ge 2.5\text{ V}\text{ to }2.8\text{ V}$ Dickson pump) and core cell parametric screening.

## Acceptance Criteria
- **Forward Voltage Continuity Window ($V_{F,\text{ESD}}$)**: $-0.90\text{ V} \le V_F \le -0.50\text{ V}$ at forced current $I_F = -100\,\mu\text{A}$ (nominal silicon p-n forward barrier voltage).
- **Contact Resistance / Short Threshold**: Measured $|V_F| \ge 0.20\text{ V}$ at $I_F = -100\,\mu\text{A}$ (contact resistance $R_{\text{contact}} + R_{\text{path}} > 2.0\text{ k}\Omega$ to exclude direct metal short to $V_{SS}$).
- **Compliance Clamping Open Threshold**: Measured $|V_F| < 1.40\text{ V}$ under tester voltage compliance of $1.50\text{ V}$ at $I_F = -100\,\mu\text{A}$ (ruling out floating/open probe needle contacts).
- **Leakage Isolation Before Core Stress**: Reverse bias leakage current $I_{\text{leak}} < 1.0\,\mu\text{A}$ at applied reverse test potential $V_{\text{rev}} = 1.8\text{ V}$ ($V_{DD}$ operating rail).

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- `180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench`
- `Legacy 180nm DRAM Architecture & Cell Capacitor Engineering`
- `High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture`

# Standard Operating Procedure: Wafer-Level DC Parametric Extraction & Multi-Site SMU Measurement Execution

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council)
- **Status**: Implemented
- **Process Generation**: Gen 3 (180nm CMOS DRAM)
- **Equipment & Tooling**: Semi-Automated / Automated Wafer Prober with Micro-Cantilever Probe Card & Multi-Site Source Measure Unit (SMU) Matrix

## Overview & Rationale
This Standard Operating Procedure (SOP) governs the electrical screening and DC parametric parameter extraction (threshold voltage $V_{th}$, drive current $I_{on}$, subthreshold leakage $I_{off}$, junction leakage, and on-chip boosted wordline $V_{PP}$ rail screening) across discrete test structures and memory array cells prior to functional bitmapping.

## Operational Workflow

```text
┌───────────────────────┐
│                       │
│     Step 1: Wafer     │
│  Alignment & Prober   │
│        Docking        │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Step 2: Linear Vth   │
│   Extraction via gm   │
│          Max          │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Step 3: Ion/Ioff    │
│  Saturation Leakage   │
│       Screening       │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Step 4: Multi-Site   │
│  Array Leakage & VPP  │
│  Boost Verification   │
│                       │
└───────────────────────┘
```

## Step-by-Step Execution Procedure

1. **Step 1: Wafer Alignment & Prober Docking**
   - Load the 180nm processed wafer onto the temperature-controlled chuck set to $85^\circ\text{C}$ (for thermal retention/leakage validation) or $25^\circ\text{C}$ baseline.
   - Perform optical pattern recognition alignment on wafer fiducials.
   - Align micro-cantilever probe tips to the EDS test pad groups (discrete test structures: $W/L = 20\,\mu\text{m}/5\,\mu\text{m}$, $W/L = 10\,\mu\text{m}/1.0\,\mu\text{m}$, and sub-micron target $W/L = 2.0\,\mu\text{m}/0.18\,\mu\text{m}$; and memory array test pads: access transistor $W = 220\,\text{nm}, L = 180\,\text{nm}$).
   - Set contact overdrive depth to $40\,\mu\text{m} \pm 5\,\mu\text{m}$ to ensure low-resistance scrub marks.

2. **Step 2: Linear Threshold Voltage ($V_{th}$) Extraction via $g_m$ Extrapolation**
   - Connect SMU Channel 1 to Drain ($V_{DS}$), Channel 2 to Gate ($V_{GS}$), Channel 3 to Source ($V_S = 0\,\text{V}$), and Channel 4 to Body/Bulk ($V_B = 0\,\text{V}$).
   - Bias linear drain voltage: $V_{DS} = 50\,\text{mV}$.
   - Sweep gate voltage $V_{GS}$ from $0\,\text{V}$ to $1.8\,\text{V}$ in $10\,\text{mV}$ steps.
   - Compute transconductance $g_m = \frac{\partial I_{DS}}{\partial V_{GS}}$.
   - Locate $g_{m,\max}$ and extrapolate linear tangent to the $I_{DS} = 0$ intercept:
     $$V_{th} = V_{GS}(g_{m,\max}) - \frac{I_{DS}(g_{m,\max})}{g_{m,\max}} - \frac{V_{DS}}{2}$$
   - Verify NMOS target is within $+0.55\,\text{V} \pm 50\,\text{mV}$ and PMOS target is within $-0.60\,\text{V} \pm 50\,\text{mV}$.

3. **Step 3: Drive Current ($I_{on}$) and Subthreshold Off Current ($I_{off}$) Screening**
   - Maintain $V_{DS} = 1.8\,\text{V}$ (saturation supply rail).
   - Measure saturation on-current $I_{on}$ at $V_{GS} = 1.8\,\text{V}$.
   - Measure subthreshold leakage current $I_{off}$ at $V_{GS} = 0.0\,\text{V}$.
   - Calculate On/Off Current ratio: $\frac{I_{on}}{I_{off}}$.

4. **Step 4: Memory Cell Array Retention Leakage & $V_{PP}$ Boost Rail Verification**
   - Switch matrix SMU to array test pads (access NMOS $W = 220\,\text{nm}, L = 180\,\text{nm}$, bitline contact, and stacked capacitor node with minimum $28\,\text{fF}$ target capacitance).
   - At chuck temperature $85^\circ\text{C}$, measure combined subthreshold and junction leakage into the storage node capacitor node; verify leakage $\le 1\,\text{fA/cell}$.
   - Route SMU voltage sensing channel to the high-voltage wordline charge pump ($V_{PP}$) monitor pad; power $V_{DD} = 1.8\,\text{V}$, enable Dickson oscillator ($20\,\text{MHz}$ to $50\,\text{MHz}$, 4-stage pump with $C_{pump} = 20\,\text{pF}$ to $50\,\text{pF}$ flying caps).
   - Verify regulated boosted rail $V_{PP} \ge 2.5\,\text{V} \text{ to } 2.8\,\text{V}$ ($V_{PP} = V_{DD} + V_{th} + \Delta V_{overdrive}$).

## Acceptance Criteria & Targets

| Metric | Target Value & Tolerance | Test Conditions | Physical Units |
| :--- | :--- | :--- | :--- |
| **NMOS Linear Threshold Voltage ($V_{thn}$)** | $+0.55 \pm 0.05$ | $V_{DS} = 50\,\text{mV}$, via $g_m$ extrapolation, $W/L = 2.0/0.18\,\mu\text{m}$ | $\text{V}$ |
| **PMOS Linear Threshold Voltage ($V_{thp}$)** | $-0.60 \pm 0.05$ | $V_{DS} = -50\,\text{mV}$, via $g_m$ extrapolation | $\text{V}$ |
| **Transistor Drive Current ($I_{on}$)** | $\ge 500$ | $V_{DS} = 1.8\,\text{V}, V_{GS} = 1.8\,\text{V}$ | $\mu\text{A}/\mu\text{m}$ |
| **Subthreshold Off-Current ($I_{off}$)** | $\le 10$ | $V_{DS} = 1.8\,\text{V}, V_{GS} = 0\,\text{V}$ | $\text{pA}/\mu\text{m}$ |
| **Drive On/Off Current Ratio** | $> 10^7$ | $I_{on}(V_{GS}=1.8\,\text{V}) / I_{off}(V_{GS}=0\,\text{V})$ | Dimensionless |
| **Cell Retention Storage Leakage** | $\le 1.0$ | Subthreshold & junction leakage at $T = 85^\circ\text{C}$ | $\text{fA/cell}$ |
| **Regulated Boosted Wordline ($V_{PP}$)** | $2.5 \text{ to } 2.8$ | $V_{DD} = 1.8\,\text{V}$, Dickson pump enabled | $\text{V}$ |

## Metric Visual Comparison

```text
                    Normalized DC Parametric Metrics    
                 ┌─────────────────────────────────────┐
                 │██████████████                       │
    VPP Boost (V)┤██████████████                       │
                 │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
  Log10(Ion/Ioff)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
Vthp Target (|V|)┤▒▒▒▒                                 │
                 │▒▒▒▒                                 │
  Vthn Target (V)┤░░░░                                 │
                 │░░░░                                 │
                 └┬────────┬────────┬────────┬────────┬┘
                 0.0      1.8      3.5      5.2     7.0 
```

## Literature References & Citations
- **Source 1**: *Stage 3 Reality Gate: Discrete Long-Channel MOSFET & CMOS Inverter Verification*
  - Transistor geometries ($20\,\mu\text{m}/5\,\mu\text{m}$, $10\,\mu\text{m}/1\,\mu\text{m}$, $2.0\,\mu\text{m}/0.18\,\mu\text{m}$).
  - Linear $V_{th}$ extraction at $V_{DS} = 50\,\text{mV}$ via maximum $g_m$ extrapolation ($V_{thn} = +0.55\,\text{V} \pm 50\,\text{mV}$, $V_{thp} = -0.60\,\text{V} \pm 50\,\text{mV}$).
  - $I_{on} \ge 500\,\mu\text{A}/\mu\text{m}$, $I_{off} \le 10\,\text{pA}/\mu\text{m}$ at $V_{DS} = 1.8\,\text{V}$, $I_{on}/I_{off} > 10^7$.
- **Source 2**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
  - Access transistor channel length $L = 180\,\text{nm}$, width $W = 220\,\text{nm}$.
  - Storage node capacitance budget $\ge 28\,\text{fF}$.
  - Leakage current target $\le 1\,\text{fA/cell}$ at $85^\circ\text{C}$ for refresh interval preservation.
- **Source 3**: *High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture*
  - Access NMOS threshold voltage $V_{th} \sim 0.5\,\text{V} \text{ to } 0.7\,\text{V}$.
  - Boosted high voltage requirement: $V_{PP} = V_{DD} + V_{th} + \Delta V_{overdrive} \ge 2.5\,\text{V} \text{ to } 2.8\,\text{V}$.
  - 4-stage Dickson pump topology ($C_{pump} = 20\,\text{pF} \text{ to } 50\,\text{pF}$, $\Phi_1, \Phi_2$ at $20\,\text{MHz} \text{ to } 50\,\text{MHz}$).

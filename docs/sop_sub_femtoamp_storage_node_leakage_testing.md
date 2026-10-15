# SOP: Sub-Femtoamp Storage Node & Junction Leakage Thermal Acceptance Testing

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Process Generation**: 180nm Open-Source DRAM (Gen 3)
- **Lifecycle Stage**: Wafer Electrical Sort, Parametric Test & Die Singulation > Cell Leakage & Storage Capacitor C-V Parametric Acceptance Testing

## Overview & Rationale
At the 180nm DRAM node (folded bitline 8F² / 6F² stacked crown/cylinder cell topology with access transistor $L = 180\text{ nm}$, $W = 220\text{ nm}$), storage node data retention requires strictly suppressing leakage paths under elevated junction temperatures ($85^\circ\text{C}$). The critical leakage contributors consist of:
1. Access transistor sub-threshold leakage ($I_\text{sub}$).
2. Storage node n+/p-well reverse junction leakage ($I_\text{junc}$).
3. Dielectric leakage across the stacked storage capacitor (ONO or $\text{Ta}_2\text{O}_5$/$\text{Al}_2\text{O}_3$ high-k stack).

To preserve data retention beyond $> 64\text{ ms}$ at $85^\circ\text{C}$ with a nominal cell capacitance budget $\ge 28\text{ fF}$ (or $25\text{ to }30\text{ fF}$), total leakage per cell must not exceed $1\text{ fA/cell}$.

## Tooling & Environmental Setup
- **Wafer Prober**: Triaxial guarded thermal chuck prober enclosed in an EMI/light-tight Faraday enclosure.
- **Parametric Analyzer**: Sub-femtoamp electrometer / High-Resolution SMU (HRSMU) with low-current remote preamplifier.
- **Test Structures**: Dedicated PCM addressable array (e.g., $10^3$ to $10^4$ cell storage nodes tied in parallel to multiply current above instrument floor) and single-cell diagnostic Kelvin pads.

---

## Step-by-Step Execution Procedure

1. **Thermal Chuck Stabilization**:
   - Mount the 180nm DRAM wafer onto the prober chuck.
   - Ramp chuck temperature to **$85^\circ\text{C} \pm 0.5^\circ\text{C}$** and hold for at least 15 minutes thermal soak to achieve complete thermal equilibrium across the wafer.
2. **Triaxial Guarding & Offset Nulling**:
   - Connect triaxial driven guards directly up to the probe tips contacting the PCM bitline, wordline, and plate line test pads.
   - Execute zero-offset compensation and open-probe cable capacitance cancellation on the electrometer / SMU.
3. **Array Bias Configuration**:
   - Apply cell plate bias $V_\text{plate} = V_\text{DD}/2$.
   - Bias substrate / p-well tap to $V_\text{BB}$ (substrate back-bias).
   - Bias wordline (gate) to off-state voltage $V_\text{WL} = V_\text{SS}$ (or negative back-bias).
4. **Precharge & Node Charging**:
   - Turn access transistor ON momentarily by pulsing $V_\text{WL}$ high to charge the storage node capacitor to $V_\text{DD}$ via the bitline.
   - De-assert wordline back to off-state ($V_\text{WL\_OFF}$), isolating the storage node.
5. **Sub-Femtoamp Direct Current & Charge Decay Integration**:
   - **Method A (Direct Array Integration)**: For parallel PCM test array (e.g., $N = 10,000$ cells), measure steady-state drain-to-substrate/bitline leakage current using HRSMU integration time $\ge 10\text{ PLC}$ (Power Line Cycles). Calculate $I_\text{cell} = I_\text{total} / N$.
   - **Method B (Quasi-Static Retention Hold Profiling)**: Float the precharged storage node and sample the voltage decay $\Delta V$ after retention hold time $t_\text{hold} = 64\text{ ms}$. Extract leakage using:
     $$I_\text{leak} = C_\text{cell} \cdot \frac{\Delta V}{t_\text{hold}}$$
     where $C_\text{cell} \ge 28\text{ fF}$.
6. **Pass/Fail Decision & Wafer Mapping**:
   - Flag any die with normalized leakage exceeding the acceptance threshold as retention fails.

---

## Machine-Measurable Acceptance Criteria

| Parameter | Target Specification | Physical Unit | Evaluation Conditions |
|---|---|---|---|
| Total Storage Node Leakage ($I_\text{sub} + I_\text{junc}$) | $\le 1.0$ | $\text{fA/cell}$ | $T = 85^\circ\text{C}$, $V_\text{cell} = V_\text{DD}$, $V_\text{WL} = \text{OFF}$ |
| Minimum Storage Cell Capacitance ($C_\text{cell}$) | $\ge 28.0$ (Range: $25 - 30$) | $\text{fF/cell}$ | Stacked Crown/Cylinder, ONO / $\text{Ta}_2\text{O}_5$ |
| Cell Retention Time ($t_\text{ret}$) | $> 64$ | $\text{ms}$ | Full array retention hold at $85^\circ\text{C}$ |
| Gate Dielectric Physical Thickness ($t_\text{ox}$) | $3.5 \pm 0.1$ | $\text{nm}$ | High-Frequency C-V Accumulation extraction |

---

## Verified Context Citations
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry $L = 180\text{ nm}$, $W = 220\text{ nm}$; Stacked capacitor with ONO or $\text{Ta}_2\text{O}_5$ / $\text{Al}_2\text{O}_3$ high-k stack ($\kappa > 15$); Capacitance budget minimum $28\text{ fF/cell}$; Leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: 1T1C stacked capacitor maintaining $25\text{ to }30\text{ fF/cell}$ to guarantee retention time $> 64\text{ ms}$ at $85^\circ\text{C}$; Gate oxide physical thickness $\sim 3.5\text{ nm}$ from dry oxidation at $850^\circ\text{C}-900^\circ\text{C}$.
- **Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction**: High-frequency C-V accumulation region saturation yields physical oxide thickness $t_\text{ox}$ with $\pm 0.1\text{ nm}$ precision.

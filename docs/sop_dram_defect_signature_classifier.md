# SOP: DRAM Defect Signature Classifier for Retention Leakage & Cell Access Failures

**Document ID:** `SOP-MET-180NM-DEF-001`  
**Generation:** Gen 2 (µm) / 180nm Open-Source DRAM Node  
**Discipline:** Metrology / Automated Shmoo Pass/Fail Defect Pipeline  

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) defines the physical screening parameters, algorithmic decision boundaries, and telemetry export requirements for classifying DRAM bit failures into **Retention Leakage Defects** vs. **Cell Access Failures** on 180nm 1T1C stacked-capacitor folded-bitline arrays.

---

## 2. Metrology Workflow & Execution Pipeline

```text
┌─────────────────────┐
│                     │
│    Ingest Shmoo     │
│   Telemetry Grid    │
│                     │
└──────────┬──────────┘
           │
           │
           ▼
┌─────────────────────┐
│                     │
│  Evaluate Boundary  │
│      Contours       │
│                     │
└──────────┬──────────┘
           │
           │
           ▼
┌──────────◇──────────┐
│                     │
│  Defect Signature   │
│        Check        │
│                     │
└──────────◇──────────┘
           │
           │
           ├────────────────────────────────────────────────────────╮Cb/Cs Ratio > 10:1 or Access Fail
           │T_ret < 64ms at 85C                                     │
           ▼                                                        ▼
┌─────────────────────┐                                  ┌─────────────────────┐
│                     │                                  │                     │
│   Flag Retention    │                                  │  Flag Cell Access   │
│       Leakage       │                                  │       Failure       │
│                     │                                  │                     │
└─────────┬───────────┘                                  └──────────┬──────────┘
          │                                                         │
          │ ╭───────────────────────────────────────────────────────╯
          ▼ ▼
┌─────────────────────┐
│                     │
│  Export Metrology   │
│       Report        │
│                     │
└─────────────────────┘
```

---

## 3. Step-by-Step Procedure

1. **Ingest Shmoo Telemetry Matrix**: Load the calibrated $V_{\text{DD}}$ versus Retention Time ($T_{\text{ret}}$) 2D shmoo bitmap captured across the 256/512 cell array blocks under elevated junction temperature ($85^\circ\text{C}$).
2. **Normalize Cell Geometry & Parasitic Ratio**:
   - Establish baseline NMOS access transistor dimensions ($L = 180\text{ nm}$, $W = 220\text{ nm}$, gate dielectric $\text{SiO}_2$ physical thickness $\sim 3.5\text{ nm}$).
   - Set nominal stacked storage node capacitance budget $C_s = 28\text{ fF}$ (allowed operational range $25\text{ fF}$ to $30\text{ fF}$) with bitline parasitic load $C_b = 150\text{ fF}$ to $250\text{ fF}$.
   - Verify baseline transfer ratio falls within nominal bounds:
     $$5:1 \le \frac{C_b}{C_s} \le 9:1$$
3. **Classify Retention Leakage Signatures**:
   - Evaluate cell bit-flips across pause time intervals.
   - If cell fails data state holding prior to $64\text{ ms}$ at $85^\circ\text{C}$, verify whether the defect is voltage-independent or temperature-accelerated.
   - If retention failure occurs while access margins at standard $V_{\text{DD}}$ are intact, tag bit as **Retention Leakage Defect** (indicative of storage capacitor ONO / $\text{Ta}_2\text{O}_5$ dielectric pinholes or junction leakage exceeding $1\text{ fA/cell}$).
4. **Classify Cell Access Failure Signatures**:
   - Inspect bit failures at nominal retention times ($< 64\text{ ms}$) where wordline activation fails to deliver adequate bitline split ($\Delta V_{\text{BL}}$) due to excessive transfer ratios ($\frac{C_b}{C_s} > 10:1$).
   - Identify bits failing at aggressive $V_{\text{DD}}$ drop boundaries regardless of pause time; tag bit as **Cell Access Failure** (indicative of tungsten plug contact degradation, high bitline capacitance coupling, or sub-threshold NMOS drive collapse).
5. **Telemetry Vector Export**: Stream structured defect tags into the metrology aggregation database, logging coordinates `[Row, Col, Block]`, defect category (`RETENTION_LEAKAGE` or `CELL_ACCESS`), and measured operating margins.

---

## 4. Machine-Measurable Acceptance Criteria

```text
                      180nm DRAM Metrology Budgets      
                ┌──────────────────────────────────────┐
                │░                                     │
I_leak (fA/cell)┤░                                     │
                │▒▒▒▒▒▒▒▒▒▒▒▒▒                         │
 T_ret @85C (ms)┤▒▒▒▒▒▒▒▒▒▒▒▒▒                         │
C_b Bitline (fF)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
  C_s Stack (fF)┤██████                                │
                │██████                                │
                └┬────────┬─────────┬────────┬────────┬┘
                 0       50        100      150     200 
```

| Metric ID | Parameter | Nominal / Target Budget | Unit | Failure Threshold / Action Boundary |
| :--- | :--- | :--- | :--- | :--- |
| **MAC-01** | Storage Node Capacitance ($C_s$) | $28.0$ (Budget: $25.0 - 30.0$) | $\text{fF/cell}$ | Classify degraded capacitance if $C_s < 25.0\text{ fF}$ |
| **MAC-02** | Cell Retention Time ($T_{\text{ret}}$ @ $85^\circ\text{C}$) | $> 64.0$ | $\text{ms}$ | Classify **Retention Leakage** if $T_{\text{ret}} < 64.0\text{ ms}$ at $85^\circ\text{C}$ |
| **MAC-03** | Total Cell Leakage Current ($I_{\text{leak}}$ @ $85^\circ\text{C}$) | $< 1.0$ | $\text{fA/cell}$ | Flag dielectric / junction leakage breakdown if $I_{\text{leak}} \ge 1.0\text{ fA/cell}$ |
| **MAC-04** | Bitline-to-Storage Capacitance Ratio ($C_b / C_s$) | $5.0 : 1 - 9.0 : 1$ ($C_b = 150 - 250\text{ fF}$) | Ratio (dimensionless) | Classify **Cell Access Failure** if $\frac{C_b}{C_s} > 10.0 : 1$ |

---

## 5. Verified Context Citations
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry $L = 180\text{ nm}$, $W = 220\text{ nm}$; ONO triple dielectric / $\text{Ta}_2\text{O}_5$ high-k stack ($\kappa > 15$); minimum capacitance budget $28\text{ fF/cell}$; leakage current target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**: 1T1C architecture, $8\text{F}^2$ folded bitline cell area ($0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$); storage node capacitance $C_s \ge 25\text{ fF}$ to $30\text{ fF}$ (nominally $28\text{ fF}$); bitline parasitic $C_b = 150\text{ fF}$ to $250\text{ fF}$ across 256/512 cell array blocks; $C_b / C_s$ transfer ratio between $5:1$ and $9:1$, severe read margin degradation when $C_b / C_s > 10:1$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: Stacked crown/cylinder capacitor; data retention time $> 64\text{ ms}$ at $85^\circ\text{C}$; gate dielectric thermal $\text{SiO}_2$ physical thickness $\sim 3.5\text{ nm}$; bitline and wordline pitch $360\text{ nm}$ to $400\text{ nm}$.

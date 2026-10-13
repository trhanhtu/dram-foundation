# Standard Operating Procedure (SOP)
## Three-Transistor VDD/2 Bitline Equalizer & Precharge Switch Sizing

- **Technology Node**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Hierarchy**: [Architecture & Integration] > Folded Bitline CMOS Sense Amplifier & Equalizer > CMOS Cross-Coupled Latch & VDD/2 Equalizer Schematic Sizing > Three-Transistor VDD/2 Bitline Equalizer & Precharge Switch Sizing
- **Generation**: Gen 2 (µm)
- **Action Type**: Make
- **Status**: Accepted

---

### 1. Architectural Overview & Equalizer Topology

The three-transistor (3T) bitline equalizer network is placed across each complementary bitline pair ($BL$ and $\overline{BL}$) in the folded bitline architecture:
1. **Equalization Transistor ($M_{EQ}$)**: Shunts complementary bitlines directly ($BL \leftrightarrow \overline{BL}$) to enable rapid charge-sharing differential nulling without drawing instantaneous current from the $V_{BLP}$ precharge supply.
2. **Precharge Pull-in Transistors ($M_{PR1}, M_{PR2}$)**: Connects $BL$ and $\overline{BL}$ respectively to the intermediate reference rail $V_{BLP} = V_{DD} / 2 = 0.90\text{ V}$ to clamp the common-mode voltage and replenish any residual sub-threshold or junction leakage.
3. **Control Gate**: All three gates are driven by the equalization control signal $BLEQ$ ($0\text{ V} \rightarrow V_{DD} = 1.8\text{ V}$).

```text
┌───────────────────────┐
│                       │
│   BLEQ Assert High    │
│                       │
└───────────┬───────────┘
            │
            ├────────────────────────────╮
            ▼                            ▼
┌───────────────────────┐    ┌───────────────────────┐
│                       │    │                       │
│  M_EQ Bridges BL and  │    │    M_PR1 and M_PR2    │
│          BLB          │    │    Connect to VBLP    │
│                       │    │                       │
└──────────┬────────────┘    └───────────┬───────────┘
           │                             │
           │ ╭───────────────────────────╯
           ▼ ▼
┌───────────────────────┐
│                       │
│  Rapid Differential   │
│     Equalization      │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Bitlines Settle to   │
│     VDD/2 (0.9V)      │
│                       │
└───────────────────────┘
```

---

### 2. Physical & Electrical Constraints Context

From verified literature:
- Nominal Supply Voltage: $V_{DD} = 1.8\text{ V}$
- Precharge Reference Voltage: $V_{BLP} = V_{DD} / 2 = 0.9\text{ V}$
- Access Transistor Threshold: $V_{th} \approx 0.5\text{ V} - 0.7\text{ V}$ (Nominal access transistor dimensions: $L = 180\text{ nm}$, $W = 220\text{ nm}$)
- Storage Cell Capacitance: $C_s = 25\text{ fF}$ (Minimum cell target: $\ge 28\text{ fF}$)
- Lumped Bitline Capacitance: $C_{BL} = 250\text{ fF}$
- Minimum Differential Readout Window: $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right)\left(V_{cell} - \frac{V_{DD}}{2}\right) \approx 100\text{ mV} - 150\text{ mV}$

```text
                 Critical Equalizer Electrical Baseline 
                ┌──────────────────────────────────────┐
                │████████████████                      │
Delta V min (mV)┤████████████████                      │
                │░░                                    │
 V_BLP (x100 mV)┤░░                                    │
  V_DD (x100 mV)┤▒▒▒▒                                  │
                │▒▒▒▒                                  │
        C_s (fF)┤▓▓▓▓▓                                 │
                │▓▓▓▓▓                                 │
       C_BL (fF)┤██████████████████████████████████████│
                │██████████████████████████████████████│
                └┬────────┬─────────┬────────┬────────┬┘
                0.0     62.5      125.0    187.5  250.0 
```

---

### 3. Step-by-Step SOP Procedure

1. **Step 1: Set Technology Node Channel Length Bounds**
   - Configure all 3 equalizer NMOS switches ($M_{EQ}, M_{PR1}, M_{PR2}$) to minimum channel length $L_{min} = 180\text{ nm}$ ($0.18\text{ }\mu\text{m}$) to minimize channel on-resistance $R_{on}$ and reduce parasitic gate-drain overlap capacitance $C_{gd}/C_{gs}$ injected into the sensitive bitlines.

2. **Step 2: Size Shunt Equalizer Switch ($M_{EQ}$)**
   - Target an on-resistance $R_{on,EQ}$ sufficiently low to equalize the differential voltage from full rail swing ($1.8\text{ V}$ vs $0\text{ V}$) across $C_{BL} = 250\text{ fF}$ within precharge time $t_{RP} \le 5\text{ ns}$.
   - Effective load during differential equalization is the series loop: $\tau_{EQ} \approx R_{on,EQ} \cdot \left(\frac{C_{BL}}{2}\right)$.
   - Size $W_{EQ} = 1.00\text{ }\mu\text{m} - 1.20\text{ }\mu\text{m}$ ($L = 0.18\text{ }\mu\text{m}$), establishing $W/L \approx 5.5 - 6.7$, ensuring $R_{on,EQ} < 1.2\text{ k}\Omega$ at $V_{GS} = 1.8\text{ V}, V_{DS} \approx 0.9\text{ V}$.

3. **Step 3: Size Precharge Centering Switches ($M_{PR1}, M_{PR2}$)**
   - Precharge switches $M_{PR1}$ and $M_{PR2}$ bias both lines to $V_{BLP} = 0.90\text{ V}$. Because $M_{EQ}$ executes $>90\%$ of the initial charge equalization, $M_{PR1,2}$ primarily serve common-mode centering and static leakage compensation.
   - Size $W_{PR1} = W_{PR2} = 0.50\text{ }\mu\text{m} - 0.60\text{ }\mu\text{m}$ ($L = 0.18\text{ }\mu\text{m}$).
   - Enforce symmetric, matched layout placement between $M_{PR1}$ and $M_{PR2}$ to eliminate differential threshold voltage mismatch ($\Delta V_{th} < 2\text{ mV}$) and gate-feedthrough charge skew.

4. **Step 4: Transient Equalization Verification**
   - Apply precharge pulse $BLEQ = 1.8\text{ V}$ following full sense amplification where $BL = 1.8\text{ V}$ and $\overline{BL} = 0\text{ V}$.
   - Monitor differential decay $|V_{BL} - V_{\overline{BL}}|$ and settlement toward $V_{DD}/2 = 0.900\text{ V}$.

---

### 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Physical Unit | Measurement Condition |
| :--- | :--- | :--- | :--- |
| **Bitline Precharge Settle Time ($t_{RP}$)** | $\le 4.5$ | $\text{ns}$ | Time from $BLEQ \ge 0.9\text{ V}$ until $\|V_{BL} - V_{\overline{BL}}\| \le 5\text{ mV}$ with $C_{BL} = 250\text{ fF}$ |
| **Equalization Offset Residual Voltage** | $\le 2.0$ | $\text{mV}$ | Common-mode deviation $\|V_{BL} - 0.900\text{ V}\|$ after $5\text{ ns}$ |
| **Feedthrough Charge Injection Skew ($\Delta Q_{inj}$)** | $\le 0.15$ | $\text{fC}$ | Differential net charge injected between $BL$ and $\overline{BL}$ upon $BLEQ$ falling edge |
| **Maximum Standby Equalizer Leakage ($I_{leak}$)** | $\le 1.0$ | $\text{fA/cell}$ | Measured per unit cell bitline junction/gate at $T = 85^\circ\text{C}$, $V_{BL} = 0.9\text{ V}$ |

---

### 5. Literature Citations

- *Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout*: Folded bitline topology, equalization network at $V_{DD}/2$, bitline capacitance $C_{BL} = 250\text{ fF}$, storage node capacitance $C_s = 25\text{ fF}$, developed differential read signal $\Delta V \approx 100\text{ mV} - 150\text{ mV}$.
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*: 180nm technology node rules ($L = 180\text{ nm}$, $W = 220\text{ nm}$ for access device), minimum storage capacitance target $\ge 28\text{ fF}$, retention leakage budget $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- *High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture*: Baseline power rail definition $V_{DD} = 1.8\text{ V}$, threshold parameters $V_{th} \approx 0.5\text{ V} - 0.7\text{ V}$, overdrive conditions.

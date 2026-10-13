# Standard Operating Procedure (SOP): Folded Bitline CMOS Sense Amplifier & Equalizer Design & Verification

- **Document ID**: SOP-DES-SA-180-01
- **Node / Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > Folded Bitline CMOS Sense Amplifier & Equalizer [DRAM Circuit Design]
- **Generation**: Gen 2 (µm) / 180nm Node
- **Action Type**: Make
- **Status**: Released / Operational

---

## 1. Process & Sensing Sequence Flow

```text
┌──────────────────────┐
│    1. Precharge &    │
│ Equalize Bitlines to │
│        VDD/2         │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│ 2. Assert Wordline & │
│   Dump Cell Charge   │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│      3. Signal       │
│ Development Delta V  │
│      100-150mV       │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│  4. Activate Sense   │
│    Latch SAN/SAP     │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│     5. Full-Rail     │
│    Restoration &     │
│       Refresh        │
└───────────┬──────────┘
            ▼
┌──────────────────────┐
│ 6. Deassert Wordline │
│      & Equalize      │
└──────────────────────┘
```

---

## 2. Step-by-Step Operating Procedure

### Step 1: Precharge and Equalization Configuration
1. Instantiate the equalization network across the complementary folded bitline pair ($BL$ and $\overline{BL}$) using minimum-pitch NMOS equalizing transistors laid out within the $360\text{ nm}$ to $400\text{ nm}$ bitline pitch.
2. Assert the equalization control gate ($EQ$) to short $BL$ and $\overline{BL}$ directly together while biasing both rails to the half-rail precharge generator supply:
   $$V_{PRE} = \frac{V_{DD}}{2}$$
3. Prior to wordline selection, deassert $EQ$ to float $BL$ and $\overline{BL}$ at identical reference potentials ($V_{DD}/2$), suppressing common-mode noise across the folded layout topology.

### Step 2: Access Transistor Wordline Assertion & Charge Sharing
1. Drive the selected wordline ($WL$) high to turn on the 1T1C unit access transistor (channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$).
2. Discharge or charge the storage capacitor ($C_s \ge 28\text{ fF}$, nominal budget $25\text{ fF}$ to $30\text{ fF}$) onto the active bitline rail ($C_{BL} = 250\text{ fF}$) through the shared tungsten plug (W-plug) bitline contact.
3. Allow charge redistribution governed by:
   $$Q_s = C_s \cdot (V_{cell} - V_{BL})$$

### Step 3: Differential Signal Development ($\Delta V$)
1. Maintain the complementary bitline ($\overline{BL}$) isolated as an unperturbed folded reference rail held at $V_{DD}/2$.
2. Allow transient charge sharing to settle across the active bitline, establishing the differential sensing signal:
   $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right)$$
3. Ensure differential amplitude $\Delta V$ develops to a minimum of **$100\text{ mV}$ to $150\text{ mV}$** before firing the sense amplifier latching strobes.

### Step 4: Strobe Activation & Differential Latching (SAN & SAP)
1. Trigger the NMOS pull-down latch strobe ($SAN$), pulling the lower-potential bitline toward ground ($V_{SS} = 0\text{ V}$).
2. With controlled delay to prevent shoot-through crowbar currents, trigger the PMOS pull-up latch strobe ($SAP$), driving the higher-potential bitline to full power rail ($V_{DD}$).
3. Exploit regenerative positive feedback of the CMOS cross-coupled inverter pair to amplify the $100\text{ mV} - 150\text{ mV}$ signal to full CMOS logic levels ($0\text{ V}$ and $V_{DD}$).

### Step 5: Cell Refresh, Restore, and Cycle Close
1. While the wordline remains asserted, use the amplified full-rail bitline level ($0\text{ V}$ or $V_{DD}$) to recharge and restore full initial charge back into the storage node capacitor $C_s$.
2. Verify restore completion to maintain cell retention target ($> 64\text{ ms}$ at $85^\circ\text{C}$ against total sub-threshold/junction leakage $< 1\text{ fA/cell}$).
3. Deassert wordline ($WL \rightarrow 0\text{ V}$), locking stored charge into the cell capacitor.
4. Re-engage $EQ$ high, shorting $BL$ and $\overline{BL}$ back to $V_{DD}/2$ in readiness for the subsequent access cycle.

---

## 3. Acceptance Criteria & Target Metrics

```text
       Sense Amplifier & Equalizer Target Metrics       
                ┌──────────────────────────────────────┐
                │██████████████████████████████████████│
   BL Pitch (nm)┤██████████████████████████████████████│
                │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             │
BL Cap C_BL (fF)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓             │
Cell Cap Cs (fF)┤▒▒▒▒                                  │
                │▒▒▒▒                                  │
    Delta V (mV)┤░░░░░░░░░░░░░                         │
                │░░░░░░░░░░░░░                         │
                └┬────────┬─────────┬────────┬────────┬┘
                 0       95        190      285     380 
```

| Parameter / Metric | Target Value | Physical Unit | Measurement / Verification Method | Verification Tolerance / Bound |
| :--- | :--- | :--- | :--- | :--- |
| **Developed Differential Signal ($\Delta V$)** | `100 to 150` | $\text{mV}$ | Transient SPICE differential node probe ($V_{BL} - V_{\overline{BL}}$) | Lower limit $\ge 100\text{ mV}$ |
| **Bitline Parasitic Capacitance ($C_{BL}$)** | `250` | $\text{fF}$ | RC extraction metrology on folded line layout | Nominal design budget ($\pm 5\%$) |
| **Cell Storage Node Capacitance ($C_s$)** | `25 to 30` (Min `28`) | $\text{fF}$ | Automated C-V parametric bridge probe ($85^\circ\text{C}$) | $\ge 28\text{ fF}$ nominal |
| **Bitline Layout Pitch** | `360 to 400` | $\text{nm}$ | In-line CD-SEM metrology / DRC layout rule check | Design rule bound |
| **Precharge / Equalization Voltage** | $V_{DD} / 2$ | $\text{V}$ | Equalizer center-tap voltage monitor | $\pm 1.5\%$ tracking to $V_{DD}/2$ |
| **Cell Retention Time** | `> 64` | $\text{ms}$ ($85^\circ\text{C}$) | Automated memory tester retention pause scan | Minimum specification limit |

---

## 4. Literature & Context Citations

1. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
   - CMOS cross-coupled inverter latch connected between complementary bitlines $BL$ and $\overline{BL}$ in folded-bitline topology.
   - Precharge operation: Bitlines equalized to $V_{DD} / 2$ via equalization transistor network prior to wordline assertion.
   - Signal development: Access transistor dumping cell charge $Q_s = C_s \cdot (V_{cell} - V_{BL})$ onto bitline.
   - Differential voltage formula: $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right)$.
   - Parametric values: $C_s = 25\text{ fF}$, $C_{BL} = 250\text{ fF}$, developed signal $\Delta V \approx 100\text{ mV}$ to $150\text{ mV}$.
   - Sensing activation: Strobe signal $SAN$ pulls to ground, $SAP$ pulls to $V_{DD}$.

2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - 180nm folded bitline architecture ($8F^2$ / $6F^2$) with stacked capacitor over bitline (COB).
   - Access transistor dimensions: $L = 180\text{ nm}$, $W = 220\text{ nm}$.
   - Shared bitline contact via tungsten plug (W-plug).
   - Unit cell capacitance budget: Minimum $28\text{ fF/cell}$ for soft-error and bitline coupling noise margin.
   - Cell sub-threshold and junction leakage: $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.

3. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - 1T1C storage capacitor target: $25\text{ to }30\text{ fF/cell}$.
   - Data retention time: $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Bitline and wordline pitch: $360\text{ nm}$ to $400\text{ nm}$.

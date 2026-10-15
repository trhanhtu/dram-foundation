# Standard Operating Procedure (SOP): High-Bandwidth Real-Time Oscilloscope Eye-Diagram & Jitter Metrology

- **Date**: 2026-10-15
- **Generation**: Gen 2 (180nm / µm)
- **Hierarchy Path**: `180nm Open-Source DRAM Chip (DRAM Foundation VN)` > `ESP32 Closed-Loop Motor Controller` > `Signal Integrity & Level Shifter Daughtercard PCB (50-Ohm Controlled Impedance Microstrips)` > `50-Ohm Controlled Impedance Stackup Design & Level Shifter Schematic Synthesis` > `High-Speed Bus Signal Integrity Transient & Eye-Diagram Verification` > `High-Bandwidth Real-Time Oscilloscope Eye-Diagram & Jitter Metrology`
- **Action Type**: Make
- **Status**: Implemented

---

## 1. Overview & Rationale
This leaf Standard Operating Procedure specifies the metrology workflow to capture, reconstruct, and decompose high-speed differential signals, eye diagrams, and jitter profiles for the DRAM Foundation VN 180nm open-source DRAM architecture. Operating at 180nm technology with folded bitline topology (8F² cell area = 0.259 µm²), storage cell capacitance $C_s \ge 28\text{ fF}$, and bitline parasitic capacitance $C_b = 150\text{ fF}$ to $250\text{ fF}$, readout differential voltage $\Delta V$ developed across complementary bitlines (BL and /BL) is strictly bounded between $100\text{ mV}$ and $150\text{ mV}$. High-bandwidth real-time oscilloscopic verification validates transmission line matching (50 Ω single-ended / 100 Ω differential) and verifies signal integrity through the level shifter daughtercard.

---

## 2. Metrology Workflow & Execution Diagram

```text
┌───────────────────────┐
│                       │
│     Oscilloscope      │
│     Calibration &     │
│     De-embedding      │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│  Active Differential  │
│    Probe Fixturing    │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│  Real-Time Transient  │
│     & Eye-Diagram     │
│      Acquisition      │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│   Dual-Dirac Jitter   │
│     Decomposition     │
│       TJ/DJ/RJ        │
│                       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│                       │
│      Acceptance       │
│  Verification & Mask  │
│        Testing        │
│                       │
└───────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

### Step 1: Instrument Calibration & S-Parameter De-Embedding
1. Power on real-time oscilloscope ($\ge 4\text{ GHz}$ analog bandwidth, $\ge 20\text{ GSa/s}$ sample rate) and warm up for $\ge 30\text{ minutes}$.
2. Run deskew and DC offset self-calibration across differential measurement channels with active differential probes ($Z_{in} > 50\text{ k}\Omega \parallel 0.3\text{ pF}$).
3. Load touchstone 2-port / 4-port S-parameter files (`.s2p` / `.s4p`) of the measurement coax cables, PCB breakout traces, and level shifter daughtercard test fixture into the oscilloscope DSP de-embedding engine to strip fixturing insertion loss and group delay distortion.

### Step 2: Test Fixturing & Probing 50-Ohm Controlled Microstrips
1. Connect differential high-impedance active probe tips directly across the complementary bitline / data bus breakout test points on the 50 Ω controlled impedance microstrip traces.
2. Confirm probe ground lead inductance is minimized ($< 2\text{ mm}$ coaxial ground spring tips) to avoid resonant ringing on edges.
3. Configure channel termination to $50\ \Omega$ DC coupling where specified by the level shifter interface, or $1\text{ M}\Omega$ differential high-Z mode when probing unbuffered folded bitlines.

### Step 3: Triggering & Real-Time Waveform Capture
1. Establish hardware pattern trigger on the DRAM Wordline activation signal or high-speed synchronous bus clock.
2. Set timebase to display continuous bursts of $\ge 10^6$ unit intervals (UI) with deep memory acquisition depth.
3. Verify precharge voltage baseline stabilizes at precisely $V_{DD} / 2$ prior to wordline assertion using the sense amplifier precharge equalization network.
4. Measure the transient charge dump signal development:
   $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right)$$
   verifying differential amplitude swing lands inside the expected $100\text{ mV}$ to $150\text{ mV}$ window.

### Step 4: Eye Diagram Construction & Mask Alignment
1. Activate software Continuous Time Linear Equalization (CTLE) and Phase-Locked Loop (PLL) Golden Clock Recovery (1st-order or 2nd-order loop filter, nominal tracking bandwidth).
2. Fold transient waveform segments into a persistent real-time eye diagram overlaying $> 10^6$ unit intervals.
3. Construct hexagonal/diamond keep-out mask scaled to the DRAM interface specifications and position center at $V_{DD}/2$.
4. Run automated mask violation counts across the entire acquired burst buffer.

### Step 5: Dual-Dirac Jitter Decomposition & Reporting
1. Compute Time Interval Error (TIE) jitter track across all rising and falling edges.
2. Apply Dual-Dirac jitter model decomposition to separate Total Jitter ($TJ$ at Bit Error Rate $\text{BER} = 10^{-12}$), Deterministic Jitter ($DJ$), and Random Jitter ($RJ_{rms}$):
   $$TJ(\text{BER}) = DJ + 2 \cdot Q(\text{BER}) \cdot RJ_{rms}$$
   where $Q(10^{-12}) \approx 7.034$.
3. Measure Deterministic Jitter components: Periodic Jitter ($PJ$), Duty Cycle Distortion ($DCD$), and Intersymbol Interference ($ISI$).
4. Export raw `.csv` waveform tables, eye metrics, and de-embedded jitter figures to the test repository.

---

## 4. Machine-Measurable Acceptance Criteria

```text
                         ┌─────────────────────────────┐
                         │░░░░░░░░░░░░░░░              │
   Target Eye Height (mV)┤░░░░░░░░░░░░░░░              │
                         │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Bitline Parasitic Cb (fF)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
     Storage Node Cs (fF)┤▓▓▓▓▓                        │
                         │▓▓▓▓▓                        │
  Sense Diff Delta V (mV)┤███████████████████          │
                         │███████████████████          │
                         └┬──────┬──────┬──────┬──────┬┘
                          0     50     100    150   200 
```

| Parameter / Metric | Nominal / Target Budget | Machine-Measurable Acceptance Range | Physical Unit | Measurement Method |
| :--- | :--- | :--- | :--- | :--- |
| **Differential Signal Swing ($\Delta V$)** | $125\text{ mV}$ | **$100\text{ mV} \le \Delta V \le 150\text{ mV}$** | $\text{mV}$ (millivolts) | Real-time differential peak voltage amplitude at sense amp activation |
| **Eye Opening Height ($V_{eye}$)** | $\ge 100\text{ mV}$ | **$\ge 100\text{ mV}$** at inner mask boundary ($\text{BER} = 10^{-12}$) | $\text{mV}$ (millivolts) | Vertical opening measured at 50% UI horizontal eye center |
| **Eye Width & Total Jitter ($TJ$)** | $TJ \le 0.30\text{ UI}$ | **Eye Width $\ge 0.70\text{ UI}$** ($TJ \le 0.30\text{ UI}$ at $\text{BER} = 10^{-12}$) | $\text{UI}$ (Unit Intervals) / $\text{ps}$ | Dual-Dirac TIE jitter decomposition ($DJ + 14.069 \cdot RJ_{rms}$) |
| **Bitline Precharge Balance Offset** | $0\text{ mV}$ offset from $V_{DD}/2$ | **$|V_{BL} - V_{/BL}| \le 5\text{ mV}$** prior to wordline assertion | $\text{mV}$ (millivolts) | Mean differential DC voltage across precharge equalization phase |

---

## 5. Verified Local Literature Citations
This procedure directly derives physical budgets and electrical constraints from local verified literature:
1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$).
   - Capacitance budget: Minimum $C_s \ge 28\text{ fF}$ per cell (ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-$\kappa$ dielectric) to maintain soft-error immunity.
   - Leakage current target: Sub-threshold and junction leakage $< 1\text{ fA/cell}$ at $85^\circ\text{C}$.
2. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Folded bitline $8F^2$ footprint (cell area $= 0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$) providing common-mode noise rejection.
   - Storage Node Capacitance budget: $C_s \ge 25\text{ fF}$ to $30\text{ fF}$ per cell (nominally $28\text{ fF}$).
   - Bitline Parasitic Capacitance: $C_b = 150\text{ fF}$ to $250\text{ fF}$ for blocks of 256 or 512 cells per bitline.
   - Capacitance ratio constraint: $C_b / C_s$ bounded between $5:1$ and $9:1$ ($< 10:1$ to prevent severe read margin degradation).
3. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
   - CMOS cross-coupled inverter latch between complementary bitlines $BL$ and $/BL$.
   - Bitline precharge and equalization to $V_{DD} / 2$.
   - Signal development equation: $\Delta V = (C_s / (C_{BL} + C_s)) \cdot (V_{cell} - V_{DD}/2)$, yielding differential readout signal $\Delta V = 100\text{ mV}$ to $150\text{ mV}$ for $C_s = 25\text{ fF}$ and $C_{BL} = 250\text{ fF}$.

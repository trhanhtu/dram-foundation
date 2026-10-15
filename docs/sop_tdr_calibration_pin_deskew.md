# SOP: TDR Calibration & Pin Electronics Timing Deskew Characterization

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 3 (180nm Commercial MPW / 1T1C DRAM)
- **Hierarchy Context**: Architecture & Integration > Foundry Tapeout & PDK > BEOL & Packaging > Reliability & Qualification > Metrology > 2D VDD-Frequency Shmoo Plotting & Operating Margin Metrology > ATE Shmoo Test Pattern Vector Generation & Pin Timing Deskew Calibration > TDR Calibration & Pin Electronics Timing Deskew Characterization

---

## 1. Executive Summary & Purpose
This Standard Operating Procedure (SOP) defines the physical calibration and deskew methodology for Automated Test Equipment (ATE) pin electronics and Device Under Test (DUT) loadboard test fixtures. Precision Time-Domain Reflectometry (TDR) and active timing deskew eliminate channel-to-channel trace propagation mismatch, pogo pin socket parasitics, and pin electronics driver timing skew before executing high-frequency JEDEC DDR speed-binning and VDD-frequency Shmoo characterization on 180nm DRAM silicon.

---

## 2. Engineering Context & Equipment Architecture

```text
┌────────────────────────┐
│                        │
│   ATE Channel Driver   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Direct Fixture Trace  │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     DUT Loadboard      │
│      Contact Pad       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Pogo Pin / Socket    │
│        Boundary        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Reflection Edge     │
│       Metrology        │
│                        │
└────────────────────────┘
```

- **ATE Architecture**: Multi-channel Digital Pin Electronics with integrated TDR step generator (25 ps edge rate, 50 $\Omega$ source termination), high-speed pin comparator, and per-pin Programmable Delay Lines (PDL).
- **Physical Environment**: Controlled metrology thermal chamber at $25^\circ\text{C} \pm 0.5^\circ\text{C}$ ambient; burn-in HTOL stress test correlation at $85^\circ\text{C}$ ambient.
- **Fixture Topology**: Controlled-impedance microstrip/stripline loadboard ($Z_0 = 50\,\Omega \pm 1.5\,\Omega$) mated via high-frequency elastomer or pogo-pin socket to 180nm open-source packaged DRAM DUTs.

---

## 3. Step-by-Step Operating Procedure

### Phase 1: Hardware Fixture Inspection & TDR Reference Baseline
1. Mount the Golden Standard Open/Short/Load (OSL) calibration substrate directly onto the ATE test head pogo-pin socket interface.
2. Initialize ATE Pin Electronics calibration software. Verify system baseline instrument internal calibration within the last 24 hours.
3. Configure the ATE TDR driver to pulse a fast incident step ($V_\text{step} = 500\text{ mV}$, rise time $t_r \le 35\text{ ps}$, $Z_0 = 50.0\,\Omega$).
4. Acquire incident and reflected waveforms across all DRAM pin channels (DQ[15:0], DQS, /CAS, /RAS, /WE, ADDR[12:0], CLK, /CS).
5. Identify the primary reflection discontinuity point ($t_\text{fixture\_contact}$) corresponding to the pogo pin socket contact tip. Verify fixture trace impedance across all channels conforms to $50\,\Omega \pm 2.0\,\Omega$.

### Phase 2: Propagation Delay Extraction ($T_\text{flight}$) & Deskew Table Generation
1. Measure round-trip time-of-flight ($2 \times T_\text{flight, pin}$) from the pin electronics driver node to the open socket pad contact for channel $i \in [1, N]$.
2. Calculate one-way electrical delay:
   $$T_{\text{flight}, i} = \frac{t_{\text{reflection}, i} - t_{\text{incident}, i}}{2}$$
3. Designate the differential reference clock channel (`CLK/CLK#`) as the master temporal baseline ($T_{\text{ref}}$).
4. Compute delta skew offset for each pin:
   $$\Delta T_{\text{skew}, i} = T_{\text{ref}} - T_{\text{flight}, i}$$
5. Program the ATE channel hardware vernier / programmable delay lines (PDL) with $-\Delta T_{\text{skew}, i}$ values.

### Phase 3: Active Loopback & Verification at DUT Contact Tip
1. Install the calibrated Short/Loopback calibration dummy DUT into the test socket.
2. Drive simultaneous edge patterns across all data pins (DQ/DQS) and control/address lines at $1.8\text{ V}$ SSTL_18 / LVTTL logic levels.
3. Measure edge coincidence across all pin electronics receivers at the socket tip using high-bandwidth equivalent-time sampling.
4. Execute an automated iterative fine-deskew convergence loop until channel-to-channel edge alignment reaches steady state.
5. Export and lock the calibrated timing calibration matrix file (`pin_deskew_180nm_cal.dat`).

---

## 4. Machine-Measurable Acceptance Criteria

```text
                       Deskew & Calibration Metrics     
                   ┌───────────────────────────────────┐
                   │░░░░░░                             │
  Edge Jitter (RMS)┤░░░░░░                             │
TDR Impedance Error┤▒▒▒                                │
                   │▒▒▒                                │
   Channel P2P Skew┤███████████████████████████████████│
                   │███████████████████████████████████│
                   └┬────────┬───────┬────────┬───────┬┘
                   0.0      4.6     9.2     13.9   18.5 
```

| Metric Parameter | Target Value | Hard Limit / Tolerance | Measurement Unit | Inspection Tool |
| :--- | :--- | :--- | :--- | :--- |
| **Pin-to-Pin Timing Skew** | $\le 15.0$ | $\le 20.0$ | ps (peak-to-peak) | ATE High-Speed Sampling Comparator |
| **TDR Characteristic Impedance ($Z_0$)** | $50.0$ | $\pm 1.5$ | $\Omega$ | TDR Reflection Edge Metrology Module |
| **Pin Driver Edge Jitter ($J_\text{RMS}$)** | $\le 2.5$ | $\le 3.0$ | ps (RMS) | Real-time Sampling Oscilloscope / ATE |
| **Edge Alignment Residual Error** | $\le 5.0$ | $\le 8.0$ | ps | Differential TDR Cross-Correlation |

---

## 5. Verified Technical References

1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - Minimum cell storage capacitance $28\text{ fF}$ ensuring noise immunity against coupling and alpha-particle soft errors.
   - Leakage current target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ for retention interval compliance.
2. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - 1T1C stacked capacitor architecture ($8F^2 / 6F^2$) requiring $25 \text{ to } 30\text{ fF}$ storage capacitance for data retention $> 64\text{ ms}$ at $85^\circ\text{C}$.
   - Bitline and wordline pitch of $360\text{ nm to } 400\text{ nm}$; gate dielectric dry oxidation thickness $\sim 3.5\text{ nm}$.
3. **SkyWater SKY130 Open PDK Design Rules & Lithography Grid**:
   - Placement grid resolution: $0.005\,\mu\text{m}$ ($5\text{ nm}$).
   - Critical dimensions: minimum poly gate length $0.15\,\mu\text{m}$ ($150\text{ nm}$), active diffusion width $0.15\,\mu\text{m}$, Metal 1 minimum width $0.14\,\mu\text{m}$, Metal 1 pitch $0.34\,\mu\text{m}$.
   - Overlay error budget $\le 35\text{ nm}$.

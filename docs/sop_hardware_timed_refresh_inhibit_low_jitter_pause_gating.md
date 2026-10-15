# SOP: Hardware-Timed Refresh Inhibit & Low-Jitter Pause Gating Implementation

- **Date**: 2026-10-15
- **Author**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Node Classification**: Gen 2 (µm) / Leaf Node / Action: Make
- **Hierarchy Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > ESP32 Closed-Loop Motor Controller [Electronics & Firmware] > Automated VDD vs Retention Time Shmoo Plot Telemetry Engine [Firmware & Software] > Variable Retention Pause & March Pattern Bit-Flip Audit Firmware [Firmware & Software] > Hardware-Timed VDD Stepping & Refresh Inhibit Pause Engine Implementation [Circuit Design] > Hardware-Timed Refresh Inhibit & Low-Jitter Pause Gating Implementation [Circuit Design]

---

## 1. Overview & Scope
This Standard Operating Procedure (SOP) defines the physical circuit implementation and hardware gating methodology for executing hardware-timed refresh inhibit and low-jitter pause intervals during retention characterization and automated $V_{DD}$ vs. retention time Shmoo plotting. 

In a 180nm 1T1C folded bitline DRAM array ($8F^2$ cell area = $0.259\ \mu\text{m}^2$, cell capacitance $C_s \ge 25\ \text{fF}$ to $30\ \text{fF}$, bitline capacitance $C_{BL} = 150\ \text{fF}$ to $250\ \text{fF}$), charge retention on storage node capacitors leaks across junction and gate interfaces over time. To precisely characterize retention boundaries down to single-bit failure thresholds, the periodic DRAM refresh controller must be cleanly inhibited without introducing asynchronous glitches or partial sense/restore cycles. This procedure details synchronous command boundary gating, hardware counter timers, and jitter-minimized pause assertion logic.

---

## 2. Structural Control & Gating Flow

```text
┌───────────────────────────────────────┐
│                                       │
│   1. Synchronous Boundary Detect      │
│      (Wait for t_RAS / t_RP Idle)     │
│                                       │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│                                       │
│   2. Glitch-Free Clock/Pulse Gating   │
│      (Deassert Auto-Refresh Trigger)  │
│                                       │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│                                       │
│   3. Hardware Counter-Timed Pause     │
│      (Precise Retention Window t_PAUSE)│
│                                       │
└───────────────────┬───────────────────┘
                    │
                    ▼
┌───────────────────────────────────────┐
│                                       │
│   4. Deterministic Gating Release     │
│      & Burst Audit Resumption         │
│                                       │
└───────────────────────────────────────┘
```

---

## 3. Step-by-Step Implementation Procedure

### Step 1: Synchronous Inhibit Gating at Precharge Boundary
1. Implement a dual-stage synchronizer and state machine arbiter in the refresh command generator that samples the `REFRESH_INHIBIT_REQ` signal against the primary DRAM controller clock.
2. Inhibit assertion must be locked out until the completion of active row restoration:
   - Ensure the equalization phase ($EQ$ asserted high) is active where bitlines $BL$ and $\overline{BL}$ are equilibrated to $V_{DD} / 2$ ($V_{BLP}$).
   - Verify that all wordlines ($WL$) are completely deasserted to $0\ \text{V}$ (isolated from boosted $V_{PP} = 2.6\ \text{V}$ to $2.8\ \text{V}$) to prevent wordline truncation during charge transfer.
3. Assert internal clock-gating latch `REF_GATE_EN` on the falling edge of the clock prior to the scheduled auto-refresh command pulse, preventing partial refresh commands.

### Step 2: Hardware-Timed High-Resolution Pause Engine
1. Route a dedicated synchronous hardware timer (clocked by a stabilized crystal/PLL reference) to decrement the programmed retention pause interval $t_{\text{PAUSE}}$.
2. Maintain array wordline decoders in a quiescent unselected state ($WL = 0\ \text{V}$) throughout the pause period.
3. Maintain sense amplifier latch control signals in unpowered standby ($SAN = V_{DD}/2$, $SAP = V_{DD}/2$) with precharge transistors held on, holding $BL$ and $\overline{BL}$ stable at $V_{DD}/2$.
4. Ensure power supply stepping rails ($V_{DD}$) remain within programmed test setpoints without exceeding $dV_{DD}/dt$ transients that induce capacitive coupling displacement currents into floating storage nodes.

### Step 3: Low-Jitter Resume & Audit Strobe Synchronization
1. Upon expiration of the hardware timer down-counter, release the `REF_GATE_EN` gating latch strictly aligned to the positive clock edge.
2. Direct the controller immediately into a read-verify or March pattern audit sweep (e.g., March C-) to read out bitline differential voltages:
   $$\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{\text{cell}} - \frac{V_{DD}}{2}\right)$$
3. Verify that the sense amplifier differential activation timing satisfies the baseline specification:
   - $SAN$ pulls to GND to initiate N-sense amplification.
   - $SAP$ pulls to $V_{DD}$ after a calibrated $1\ \text{ns}$ to $2\ \text{ns}$ delay for PMOS restoration.
4. Record retention failure bitmask telemetry across array row/column addresses.

---

## 4. Acceptance Criteria & Target Metrology

| Metric Parameter | Specification Target | Verification Method & Conditions |
| :--- | :--- | :--- |
| **Pause Gating Edge Jitter ($t_{\text{jitter}}$)** | $\le 50\ \text{ps RMS}$ (or $\le 200\ \text{ps peak-to-peak}$) | Real-time high-bandwidth oscilloscope measurement on gating strobe trigger relative to clock edge. |
| **Refresh Glitch Suppression Margin** | $0\ \text{V}$ runt pulse / $100\%$ glitch-free | Logic analyzer / high-speed DSO capture on refresh command bus during asynchronous assertion of inhibit request. |
| **Pre-Gating Array Quiescent State** | $WL = 0\ \text{V}$, $V_{BL} = V_{\overline{BL}} = V_{DD}/2 \pm 15\ \text{mV}$ | Analog active micro-probing of sense amp precharge nodes prior to timer start. |
| **Post-Pause Sense Activation Delay ($\Delta t_{SAN\text{-}SAP}$)** | $1.0\ \text{ns} \le \Delta t \le 2.0\ \text{ns}$ | SPICE transient verification & oscillographic timing verification during first post-inhibit readout cycle. |

---

## 5. Literature Citations & Physical Constraints

1. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
   - Signal development: $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{\text{cell}} - \frac{V_{DD}}{2}\right)$. For nominal $C_s = 25\ \text{fF}$ and $C_{BL} = 250\ \text{fF}$, nominal developed $\Delta V$ is $100\ \text{mV}$ to $150\ \text{mV}$.
   - Precharge operation: Bitlines equalized to $V_{DD}/2$ prior to sensing.
2. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Folded bitline $8F^2$ cell layout ($0.259\ \mu\text{m}^2$ at $F = 180\ \text{nm}$).
   - Cell storage capacitance $C_s \ge 25\ \text{fF}$ to $30\ \text{fF}$; bitline parasitic capacitance $C_b = 150\ \text{fF}$ to $250\ \text{fF}$ with capacitance ratio $C_b / C_s$ bounded between $5:1$ and $9:1$.
3. **Cross-Coupled Regenerative Sense Amplifier Timing & Charge Restoration**:
   - Wordline assert overdrive using boosted $V_{PP} = 2.6\ \text{V}$ to $2.8\ \text{V}$.
   - Two-stage regenerative sensing sequence: $SAN$ pulldown to GND followed by $SAP$ pullup to $V_{DD}$ after $1\ \text{ns}$ to $2\ \text{ns}$ delay.

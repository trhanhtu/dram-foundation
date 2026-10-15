# Interactive In-Browser SPICE Transient Waveform & March C- BIST Visualizer

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Bridging the abstract 2,020-node semiconductor WBS graph to atomic physical reality requires intuitive, interactive visual tools that allow engineers, researchers, and community contributors to experiment with silicon behaviors directly in their browser without requiring local EDA tool installations (Cadence Spectre, Synopsys PrimeSim, or Ngspice binaries).

This feature integrates a real-time **SPICE Transient Sensing Margin Analyzer** and an animated **March C- Memory BIST Lab** into the 360° Metadata Explorer of both the development interface ([index.html](file:///D:/coding/dram/index.html)) and the standalone static distribution ([dist/index.html](file:///D:/coding/dram/dist/index.html)).

---

## Key Details & Architecture

### 1. In-Browser SPICE Transient Waveform Engine
- **Mathematical Modeling**:
  - Solves the continuous differential charge sharing equation:
    $$\Delta V_{BL} = \frac{C_s}{C_s + C_{BL}} \cdot (V_{cell} - V_{EQ})$$
  - Simulates dynamic cross-coupled CMOS sense amplifier regeneration using an analytical S-curve sigmoid model parameterized by bitline capacitance ($C_{BL}$), storage capacitance ($C_s$), and transconductance ($g_m$):
    $$\tau_{latch} = 0.67\text{ ns} \cdot \left(\frac{C_{BL}}{150\text{ fF}}\right) \cdot \left(\frac{28.0\text{ fF}}{C_s}\right)^{0.3}$$
- **HiDPI Multi-Signal Canvas Rendering**:
  - Dynamically renders 6 concurrent voltage signals across an 8.0ns sensing lifecycle:
    - $V(BL)$ True Bitline (Cyan `#06b6d4`, 2.5px)
    - $V(\overline{BL})$ Complementary Reference Bitline (Indigo Dashed `#818cf8`, 2.0px)
    - $V(SN)$ Storage Node Cell Potential (Emerald `#10b981`, 1.5px)
    - $V(WL)$ Boosted Wordline Overdrive to $V_{PP} = 2.8\text{ V}$ (Purple `#c084fc`, 1.5px)
    - $SAN$ N-Sense Strobe pulling to $0.0\text{ V}$ (Amber `#f59e0b`, 1.2px)
    - $SAP$ P-Sense Strobe pulling to $1.8\text{ V}$ (Rose `#f43f5e`, 1.2px)
- **Interactive Controls & Inspection**:
  - Real-time sliders for $C_{BL} \in [80, 300]\text{ fF}$ and $C_s \in [15, 45]\text{ fF}$.
  - Toggle between Data '1' ($1.8\text{ V}$) and Data '0' ($0.0\text{ V}$).
  - Live metric cards: Sensing Margin ($\Delta V$), SNR over $30\text{ mV}$ offset, Restored Voltage, and Latch Delay ($t_{LATCH}$).
  - Cursor tracking tooltip with microsecond precision showing $(t, V_{BL}, V_{\overline{BL}}, \Delta V)$.

### 2. March C- Memory BIST Lab (10N Complexity)
- **64-Cell (8x8) Silicon Matrix Grid**:
  - Visualizes an 8x8 DRAM cell array with hex address labels (`0x00` through `0x3F`).
  - Color-coded cell states:
    - Value 0: Deep navy (`#0f172a`)
    - Value 1: Cyan (`#0e7490`)
    - Active Accessed Cell: Pulsing amber outline with scale transform (`scale-105`)
    - Mismatch / Fault Cell: Pulsing crimson red (`#dc2626`)
- **FSM Algorithm Sequencer**:
  - Executes the 640 operations of the 10N March C- test sequence:
    1. $M_0: \Updownarrow (w0)$ (64 writes)
    2. $M_1: \Uparrow (r0, w1)$ (128 operations: ascending read 0, write 1)
    3. $M_2: \Uparrow (r1, w0)$ (128 operations: ascending read 1, write 0)
    4. $M_3: \Downarrow (r0, w1)$ (128 operations: descending read 0, write 1)
    5. $M_4: \Downarrow (r1, w0)$ (128 operations: descending read 1, write 0)
    6. $M_5: \Updownarrow (r0)$ (64 operations: final zero verify)
- **Dynamic Fault Injection Suite**:
  - **Stuck-At-0 (SAF0)** at address `0x15`: Caught in Phase $M_2$.
  - **Stuck-At-1 (SAF1)** at address `0x2A`: Caught in Phase $M_1$.
  - **Transition Fault (TF01)** at address `0x1F`: Caught in Phase $M_2$.
  - **Inversion Coupling Fault (CFin)**: Transition at aggressor `0x20` flips victim `0x21`: Caught in Phase $M_1$.
- **Playback Controls**:
  - Run, Pause, Single-Step, and Reset.
  - Multi-speed clock rate (Fast 20ms, Medium 80ms, Slow 250ms).
  - Telemetry console showing cycle count, active address, and error messages.

---

## References & Related Files
- [index.html](file:///D:/coding/dram/index.html): Full interactive Web Explorer.
- [dist/index.html](file:///D:/coding/dram/dist/index.html): Clean static production deployment.
- [verify_ui_dom.py](file:///D:/coding/dram/scripts/verify_ui_dom.py): 45/45 DOM ID verification script.
- [test_physical_bridge_simulation.py](file:///D:/coding/dram/tests/test_physical_bridge_simulation.py): Pytest regression suite covering SPICE math and Web UI DOM elements.
- [dram_1t1c_sensing_spice_and_march_c_bist.md](file:///D:/coding/dram/docs/knowledge/dram_1t1c_sensing_spice_and_march_c_bist.md): Physical bridge architectural documentation.

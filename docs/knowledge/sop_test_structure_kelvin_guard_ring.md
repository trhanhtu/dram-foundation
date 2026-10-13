# SOP: Test Structure Kelvin Array & Guard-Ring Pad Design for Sub-fA Probing

- **Document ID**: SOP-DRAM180-MET-004
- **Date**: 2026-10-12
- **Node**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Generation**: Gen 2 (µm)
- **Hierarchy**: [Architecture & Integration] > [Circuit Design] > [Metrology] > Test Structure Kelvin Array & Guard-Ring Pad Design

---

## 1. Overview & Objective
Design and lay out dedicated 4-terminal Kelvin test pads and concentric driven guard-ring structures to enable precise electrical extraction of 180nm 1T1C storage cell retention leakage (< 1.0 fA/cell) and storage capacitance ($C_s \approx 25\text{ to }30\text{ fF}$) without parasitic cable, pad, or junction leakage distortion.

---

## 2. Process Flow Architecture

```text
┌───────────────────────┐
│                       │
│  Kelvin Force/Sense   │
│         Core          │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Active Driven Guard  │
│         Ring          │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Shield Metal Moat &  │
│     Substrate Tap     │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Sub-fA Electrometer  │
│        Probing        │
│                       │
└───────────────────────┘
```

---

## 3. Step-by-Step Procedure

1. **Kelvin 4-Terminal Pad Layout Partitioning**:
   - Establish dedicated `Force` and `Sense` pad pairs for both Wordline (WL) access gate and Bitline (BL) contact terminals to eliminate probe contact resistance ($R_{\text{probe}}$) and metallization series drop.
   - Size individual probing pads to standard pitch with minimum top-metal thickness suitable for low-impact cantilever or triaxial probe touchdown.

2. **Driven Guard-Ring Enclosure Implementation**:
   - Route an inner continuous concentric guard ring enclosing the high-impedance Device-Under-Test (DUT) pad (connected to the cell storage node / tungsten bitline contact via access transistor).
   - Bias the guard ring using an active unity-gain buffer matching the DUT potential ($V_{\text{guard}} \approx V_{\text{DUT}}$), forcing zero potential gradient across dielectric isolation gaps and eliminating lateral surface leakage.

3. **Multi-Layer Interconnect Shielding & Substrate Tapping**:
   - Surround the Kelvin guard ring with a grounded outer shield metal moat tied to substrate p-well taps through dense contact arrays.
   - Maintain ground routing on lower intermediate metal layers beneath high-impedance routing traces to shield vertical capacitive coupling against adjacent clock and wordline toggle lines.

4. **Integration with Cell Matrix & Array Isolation**:
   - Terminate the test structure into single-cell and parallelized $1024 \times 1024$ Kelvin array configurations to cross-verify single-cell sub-fA leakage and aggregate cell capacitance ($C_s \ge 25\text{ fF/cell}$).
   - Insert dummy polysilicon gate stripes and dummy active diffusions at array boundaries to match optical proximity effect (OPE) matching the 360 nm to 400 nm bitline/wordline pitch.

5. **Electrometer Triaxial Metrology Calibration**:
   - Connect triaxial cable shields directly to the active guard ring pads.
   - Execute open/short de-embedding protocols at 85°C to calibrate triaxial leakage floor below 0.1 fA before running long-integration I-V ramps.

---

## 4. Machine-Measurable Acceptance Criteria

| Parameter | Target Metric | Exact Physical Unit | Verification Method |
|---|---|---|---|
| Cell Leakage Floor | $< 1.0$ | $\text{fA/cell}$ | Electrometer I-V integration at 85°C |
| Cell Storage Capacitance ($C_s$) | $25.0 \text{ to } 30.0$ | $\text{fF/cell}$ | Kelvin LCR meter / CV profiling at 100 kHz |
| Bitline / Wordline Pitch Compliance | $360 \text{ to } 400$ | $\text{nm}$ | In-line CD-SEM / GDSII DRC verification |
| Gate Dielectric Physical Thickness | $3.5 \pm 0.2$ | $\text{nm}$ | Spectroscopic Ellipsometry / TEM cross-section |

---

## 5. References & Verified Literature Citations

- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Cell geometry: Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
  - Storage capacitance budget: minimum 28 fF per cell ($> 15$ high-k stack).
  - Target cell leakage: $< 1\text{ fA/cell}$ at 85°C.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - Storage capacitor retention requirement: 25 to 30 fF per cell ensuring retention $> 64\text{ ms}$ at 85°C.
  - Interconnect pitch: Bitline and wordline pitch of 360 nm to 400 nm.
  - Gate oxide: Thermally grown $\text{SiO}_2$ at 850°C–900°C with $\sim 3.5\text{ nm}$ physical thickness.
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
  - Signal margin development: Cell capacitance $C_s = 25\text{ fF}$, bitline capacitance $C_{\text{BL}} = 250\text{ fF}$, readout differential $\Delta V = 100\text{ mV to } 150\text{ mV}$.

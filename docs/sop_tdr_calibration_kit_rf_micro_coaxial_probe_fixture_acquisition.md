# Standard Operating Procedure (SOP)
## TDR Calibration Kit & RF Micro-Coaxial Probe Fixture Acquisition

- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > ESP32 Closed-Loop Motor Controller [Electronics & Firmware] > Signal Integrity & Level Shifter Daughtercard PCB (50-Ohm Controlled Impedance Microstrips) [PCB & Hardware] > Microstrip TDR Impedance Metrology & Signal Integrity Eye-Diagram Validation [Metrology] > TDR Calibration Kit & RF Micro-Coaxial Probe Fixture Acquisition [Metrology]
- **Action Type**: Buy
- **Generation**: Gen 2 (µm)

---

### 1. Scope & Objective
Establish the procurement, RF specification validation, incoming inspection, and baseline acceptance protocol for acquiring high-frequency Time-Domain Reflectometry (TDR) calibration standards (SOLT: Short-Open-Load-Through) and RF micro-coaxial probe fixtures (GS/GSG micro-probing tips). This acquisition supports impedance metrology and signal integrity eye-diagram validation across 50-Ohm controlled-impedance microstrip interconnect lines on the ESP32 level shifter daughtercard PCB and test interfaces interfacing 180nm DRAM test vehicles.

---

### 2. Step-by-Step Procurement & Acquisition Procedure

1. **RF Metrology Requirement & Form-Factor Specification Definition**
   - Define characteristic impedance standard: $Z_0 = 50.0\text{ }\Omega$ nominal.
   - Establish probe fixture pitch compatibility matching test pads and TLM contact structures: probe pitch range compatible with pad widths $W = 100\text{ }\mu\text{m}$ and pad lengths $L_{\text{pad}} = 50\text{ }\mu\text{m}$ with spacing gaps $d = 5\text{ }\mu\text{m}, 10\text{ }\mu\text{m}, 20\text{ }\mu\text{m}, 40\text{ }\mu\text{m}, \text{and } 80\text{ }\mu\text{m}$.
   - Select micro-coaxial probe tip geometry: Ground-Signal (GS) or Ground-Signal-Ground (GSG) configuration with low-loss semi-rigid/flexible RF coaxial cabling terminated in SMA / 2.92mm (K) connectors rated for TDR step rise times $< 35\text{ ps}$.

2. **Supplier Evaluation & RF Spec Sheet Verification**
   - Solicit RF calibration kits providing precision open, short, and matched $50.0\text{ }\Omega$ termination loads certified with traceable return loss ($S_{11} \le -20\text{ dB}$) across the operating bandwidth.
   - Mandate differential micrometer / piezo-actuator stage fixture compatibility possessing displacement resolution and position sensitivity down to $0.1\text{ }\mu\text{m}$ for repeatable micro-contact touchdown without damaging microstrip metallization.
   - Verify probe tip parasitics do not exceed the minimum cell capacitance budget headroom ($28\text{ fF}$) by requiring probe tip stray capacitance $< 0.1\text{ pF}$ (sub-50 fF nominal).

3. **Commercial Procurement & Traceability Sign-Off**
   - Issue Purchase Order (PO) specifying calibration kit serial numbers, individual S-parameter coefficient definition files, and micro-coaxial probe fixture compliance certificates.
   - Ensure delivery packaging includes anti-static ESD-shielded enclosures, desiccated storage cases, and mechanical tip protective covers.

4. **Physical Receipt & Mechanical Stage-Fit Metrology**
   - Unbox in clean bench environment; perform optical microscopic inspection of probe tips (using 10x Plan Achromat objective lens, NA 0.25). Inspect for bent tines, mechanical wear, or tip contamination.
   - Mount RF micro-coaxial probe onto the 3-axis micromanipulator; verify micrometer travel sensitivity ($\le 0.1\text{ }\mu\text{m}$) across progressive pad gap pitches ($5\text{ to }80\text{ }\mu\text{m}$).

5. **SOLT Calibration & TDR Baseline Impedance Acceptance Test**
   - Connect the calibration standards to the TDR oscilloscope / Vector Network Analyzer (VNA).
   - Execute Short-Open-Load-Through (SOLT) or Short-Open-Load (SOL) calibration routine.
   - Touch down probe tips onto the precision $50\text{ }\Omega$ calibration load; confirm measured characteristic impedance remains within $50.0 \pm 1.0\text{ }\Omega$ and reflection coefficient return loss $\le -20\text{ dB}$ across the target frequency band.

---

### 3. Machine-Measurable Acceptance Criteria Target Metrics

| Metric | Target Value | Physical Unit | Measurement Method & Instrument |
| :--- | :--- | :--- | :--- |
| **Nominal Calibration Load Characteristic Impedance ($Z_0$)** | `50.0 ± 1.0` | `Ω` | TDR / VNA Reflection Metrology ($S_{11}$) |
| **Load Return Loss ($S_{11}$) Calibration Metric** | `≤ -20` | `dB` | High-bandwidth Vector Network Analyzer / TDR module |
| **Micro-Manipulator Gap & Pitch Displacement Sensitivity** | `≤ 0.1` | `µm` | Closed-loop piezo actuator / differential micrometer dial |
| **Compatible Interconnect Measurement Gap Range ($d$)** | `5 to 80` | `µm` | Calibrated optical reticle inspection across progressive TLM gaps |
| **Probe Tip Residual Parasitic Capacitance Loading** | `< 0.1` | `pF` | High-frequency LCR / VNA capacitive extraction |

---

### 4. Verified Literature Citations

- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - *Context applied*: "Capacitance Budget: Minimum 28 fF per cell ensures noise immunity against alpha-particle soft errors and bitline coupling capacitance. Unit Cell Geometry: Access transistor channel length L = 180 nm, width W = 220 nm."
- **Transmission Line Measurement (TLM) for Specific Contact Resistivity**:
  - *Context applied*: "Structure Dimensions: - Identical rectangular contact pads (width W = 100 um, length L_pad = 50 um) spaced at progressively increasing gaps: d = 5 um, 10 um, 20 um, 40 um, 80 um. Measurement & Calculation: - Total measured resistance R_T between two adjacent pads is: R_T = 2 * R_c + (R_s / W) * d."
- **Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose**:
  - *Context applied*: "Gap Setting: Controlled using three high-precision differential micrometers or closed-loop piezo actuators with 0.1 micron sensitivity. UV Exposure Optics: 365nm (i-line) LED array or 200W Mercury short-arc lamp coupled through fly's eye integrator lens for >95% beam uniformity across wafer."

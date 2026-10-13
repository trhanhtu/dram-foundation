# Standard Operating Procedure (SOP)
## Picoprobe Micro-Contact Setup & Low-Capacitance Fixture Preparation

- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > Address Decoders & Wordline VPP Voltage Pump [DRAM Circuit Design] > Transient Post-Layout Verification & VPP Slew Rate Metrology [Metrology] > Wordline VPP Slew Rate & Voltage Drop Transient Metrology Protocol [Metrology] > Picoprobe Micro-Contact Setup & Low-Capacitance Fixture Preparation [Metrology]
- **Action Type**: Make
- **Generation**: Gen 2 (µm)

---

### 1. Scope & Objective
Establish the physical assembly, micro-positioning, and probe calibration protocol for high-impedance, ultra-low-capacitance active Picoprobes (FET-input microprobes) and low-capacitance test fixtures. This procedure ensures accurate transient measurement of wordline pumped voltage ($V_{PP}$) slew rates and transient voltage drops across 180nm DRAM address decoders without excessive capacitive loading on high-impedance internal nodes.

---

### 2. Step-by-Step Operating Procedure

1. **Vibration-Isolated Macroscopic Stage & Environment Preparation**
   - Mount the micro-probing workstation on a pneumatic vibration-isolation optical breadboard table to eliminate mechanical drift and transient tip displacement.
   - Ground the chuck, probe head body, and chassis to a common earth star point to eliminate ground-loop induced AC ripple and electrostatic discharge (ESD).

2. **Low-Capacitance Fixture & Active Picoprobe Mechanical Mounting**
   - Secure the active FET Picoprobe (input capacitance $< 0.1\text{ pF}$, nominal sub-50 fF tip load) into a high-precision 3-axis micro-manipulator stage.
   - Connect the ultra-short, coaxial/triaxial ground lead directly to the nearest on-chip ground test point adjacent to the wordline driver to minimize ground-loop parasitic inductance ($< 2\text{ nH}$).
   - Fasten the device-under-test (DUT) wafer or die carrier onto the low-capacitance fixture vacuum chuck.

3. **Optical Inspection & Gen 2 Micro-Positioning Alignment**
   - Position the stereo microscope with a high-magnification objective lens (e.g. 10x Plan Achromat, NA 0.25) above the target wordline $V_{PP}$ driver and address decoder tap points.
   - Adjust micro-manipulator $X-Y$ vernier micrometers to align the tungsten probe tip (tip radius $< 1\text{ }\mu\text{m}$) directly over the top metal test pad or decapped wordline contact pad.
   - Ensure positioning alignment meets Gen 2 micro-contact alignment tolerance ($\pm 5\text{ }\mu\text{m}$).

4. **Z-Axis Controlled Descent & Micro-Contact Touchdown**
   - Slowly lower the $Z$-axis micrometer under continuous optical focus tracking until the probe tip touches the pad surface.
   - Apply a micro-overtravel contact force strictly between $10\text{ to }30\text{ mN}$ (tip scrub deflection $\le 2\text{ }\mu\text{m}$) to reliably break through native surface oxide without punching through thin top-metal interconnects.
   - Verify contact continuity with a low-voltage DC four-point check or pre-bias test before activating active $V_{PP}$ transient drives.

5. **Transient Slew Rate Metrology & Capacitive Loading Calibration**
   - Power up the Picoprobe active buffer power supply module and calibrate zero-offset into a high-bandwidth digital oscilloscope (50 $\Omega$ termination input).
   - Trigger the wordline driver and $V_{PP}$ charge pump circuitry.
   - Acquire transient waveform profiles; verify that fixture and probe loading does not perturb the measured node capacitance by more than the allowable capacitive budget (referencing the minimum cell storage capacitance budget of $25\text{ to }30\text{ fF}$).
   - Inspect recorded signals for ringing or reflection artifacts and confirm calibrated slew rate accuracy.

---

### 3. Machine-Measurable Acceptance Criteria Target Metrics

| Metric | Target Value | Physical Unit | Measurement Method & Instrument |
| :--- | :--- | :--- | :--- |
| **Micro-Contact Alignment Tolerance (Gen 2)** | `±5` | `µm` | Optical alignment stage scale / calibrated microscope reticle (10x Plan Achromat, NA 0.25) |
| **Picoprobe Active Tip Loading Capacitance** | `< 0.1` (nominal `< 0.05`) | `pF` | High-frequency vector network analyzer (VNA) / LCR bridge fixture characterization |
| **Micro-Contact Tip Scrub Overtravel Force** | `10 to 30` | `mN` | Micromanipulator strain-gauge load sensor / calibrated cantilever deflection |
| **Ground Loop Lead Parasitic Inductance** | `< 2.0` | `nH` | S-parameter return loss ($S_{11}$) reflection time-domain reflectometry (TDR) |
| **Probe Tip Positioning Travel Resolution** | `< 0.5` | `µm` | Differential micrometer drive / piezo-actuated stage encoder |

---

### 4. Verified Literature Citations

- **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**:
  - *Context applied*: "Using a modified microscope objective (10x Plan Achromat, NA 0.25) allows micron-scale feature resolution... Alignment tolerance at Gen 1 is ±100 microns (0.1 mm), improving to ±5 microns in Gen 2."
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - *Context applied*: "Capacitance Budget: Minimum 28 fF per cell ensures noise immunity against alpha-particle soft errors and bitline coupling capacitance. Unit Cell Geometry: Access transistor channel length L = 180 nm, width W = 220 nm."
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - *Context applied*: "The storage capacitor must maintain a minimum capacitance of 25 to 30 fF (femtofarads) per cell to ensure data retention time > 64 ms at 85°C... Bitline and wordline pitch is approximately 360 nm to 400 nm."

# Standard Operating Procedure (SOP)
## MOSCAP Aluminum Pad Scrub Depth and Overtravel Optimization

- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm Dry Gate Oxide Growth (3.5 nm) [Thermal Processing] > Spectroscopic Ellipsometry and C-V Oxide Thickness & Interface Metrology [Metrology] > High-Frequency and Quasi-Static C-V Interface Trap Density (Dit) Extraction [Metrology] > MOSCAP Test Structure Probe Setup and Contact Verification [Metrology] > Tungsten/Beryllium-Copper Microprobe Tip Alignment and Pad Scrub Optimization [Metrology] > MOSCAP Aluminum Pad Scrub Depth and Overtravel Optimization [Metrology]
- **Action Type**: Make
- **Generation**: Gen 2 (µm)

---

### 1. Scope & Objective
Establish a reproducible, non-destructive mechanical micro-probing procedure for aluminum (Al-0.5%Cu) top metal test pads situated directly over ultra-thin 3.5 nm dry gate oxide MOSCAP test structures. This SOP optimizes cantilever needle scrub length and $Z$-axis overtravel to break native aluminum oxide ($Al_2O_3$, ~3–5 nm) without causing dielectric punch-through, mechanical micro-cracking, or false leakage elevation in high-frequency (100 kHz – 1 MHz) and quasi-static C-V / $D_{it}$ extractions.

---

### 2. Step-by-Step Operating Procedure

1. **Environmental & Chuck Preparation**
   - Mount the processed wafer or coupon onto the vacuum chuck of the analytical probe station mounted on a pneumatic vibration-isolation table.
   - Verify ambient temperature stability ($23.0 \pm 0.5^\circ\text{C}$) and laminar nitrogen purge flow inside the dark Faraday enclosure shield to avoid electrostatic coupling and photo-carrier generation during subsequent C-V metrology.
   - Establish low-impedance common ground connections across chuck, shield, and coaxial/triaxial cable shields.

2. **Probe Alignment & Planarity Leveling**
   - Install pre-inspected Tungsten (W) or Beryllium-Copper (BeCu) cantilever probes (nominal tip radius $R_{tip} = 12.5\text{ to }25\text{ }\mu\text{m}$) into the micro-positioner.
   - Under stereo microscope illumination (10x Plan Achromat objective lens), align the probe tips across the pad matrix. Ensure tip-to-pad positional alignment tolerance is within Gen 2 limits ($\pm 5\text{ }\mu\text{m}$).
   - Adjust the probe holder planarity tilt so that multi-finger contacts land co-planar within $\le 2\text{ }\mu\text{m}$ across all test pads.

3. **Touchdown Detection ($Z_0$ Reference)**
   - Advance the motorized/micrometer $Z$-axis stage downward toward the aluminum pad in $1\text{ }\mu\text{m}$ increments.
   - Monitor electrical touchdown via high-resolution contact sense or optical focus change. The exact mechanical contact point where initial electrical resistance drops below $10\text{ k}\Omega$ marks the zero-overtravel reference ($Z_0$).

4. **Calibrated Overtravel ($Z_{OT}$) Scrub Drive**
   - Drive the $Z$-axis downward by a calibrated overtravel distance of $25\text{ }\mu\text{m} \pm 5\text{ }\mu\text{m}$ ($0.025\text{ mm}$).
   - Allow the cantilever probe spring beam to deflect forward, executing a horizontal scrub displacement of $8\text{ to }15\text{ }\mu\text{m}$ across the aluminum pad surface.
   - Ensure the probe tip breaks the native surface oxide without exceeding a maximum penetration depth of $15\%$ of the aluminum metallization thickness ($< 90\text{ nm}$ for a nominal $600\text{ nm}$ Al layer).

5. **Contact Resistance & Dielectric Integrity Verification**
   - Measure 2-wire / quasi-Kelvin contact resistance $R_c$; verify $R_c \le 2.0\text{ }\Omega$ to confirm non-rectifying, low-noise contact for high-frequency C-V sweeping.
   - Apply a sub-breakdown test bias ($V_G = +1.0\text{ V}$) and record gate leakage current $I_{leak}$; verify $I_{leak} < 1.0\text{ fA}$ per test node (conforming to the DRAM refresh leakage budget of $< 1\text{ fA/cell}$ at room temperature) to ensure zero dielectric puncture into the underlying $3.5\text{ nm}$ dry gate oxide ($E_{bd} > 10\text{ MV/cm}$).
   - Inspect the pad scrub mark under 50x optical/laser confocal microscope: verify absence of pad peeling, silicon cratering, or micro-cracks propagating toward active capacitor boundaries.

---

### 3. Machine-Measurable Acceptance Criteria Target Metrics

| Metric | Target Value | Physical Unit | Measurement Method & Instrument |
| :--- | :--- | :--- | :--- |
| **Probe Z-Axis Overtravel ($Z_{OT}$)** | `25.0 ± 5.0` | `µm` | Motorized probe station linear encoder / digital micrometer |
| **Horizontal Scrub Length on Al Pad** | `8.0 to 15.0` | `µm` | Calibrated optical reticle / white-light interferometry |
| **Probe Contact Resistance ($R_c$)** | `≤ 2.0` | `Ω` | 4-point Kelvin digital multimeter / low-level LCR meter |
| **Maximum Pad Scrub Penetration Depth** | `< 15` (nominal `< 90 nm`) | `%` (or `nm`) | Contact/optical surface profilometer or laser confocal microscopy |
| **Pre-Bias Oxide Leakage Current ($I_{leak}$)** | `< 1.0` | `fA` | Sub-femtoampere electrometer / SMU at $V_G = 1.0\text{ V}$ |

---

### 4. Verified Literature Citations

- **Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace**:
  - *Context applied*: "Dry Oxidation: Performed at 900°C-1000°C in pure dry O2. Produces dense, high-dielectric breakdown gate oxide ($E_{bd} > 10\text{ MV/cm}$) with minimal interface trap density ($D_{it} < 10^{10}\text{ cm}^{-2}\text{ eV}^{-1}$). Thickness target for 180nm gate dielectric is 3.5 to 4.0 nm."
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - *Context applied*: "Leakage Current Target: Sub-threshold and junction leakage must be kept below 1 fA/cell at 85°C to achieve refresh interval... Access transistor channel length L = 180 nm, width W = 220 nm. Bitline contact shared between two adjacent memory cells."
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
  - *Context applied*: "A classic 180nm DRAM cell uses a 1-Transistor 1-Capacitor (1T1C) architecture... Gate dielectric is thermally grown silicon dioxide (SiO2) at 850°C-900°C dry oxidation with ~3.5 nm physical thickness."

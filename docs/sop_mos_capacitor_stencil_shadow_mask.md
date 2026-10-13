# Standard Operating Procedure (SOP)
## Task: MOS Test Capacitor Stencil Shadow Mask Design & Micro-Machining
- **Module**: Photolithography & Tooling / Front-End Fabrication
- **Platform**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Generation**: Gen 2 (µm) | **Action Type**: Make

---

### 1. Process Overview & Objective
Fabricate high-precision physical shadow stencil masks (micrometer aperture array) used to deposit top metal electrode test dots onto thermally grown SiO2 / high-k dielectric test coupons without organic photoresist contamination, supporting high-frequency C-V extraction and dielectric metrology.

---

### 2. Step-by-Step Operating Procedure

1. **CAD/CAM Stencil Layout Generation**:
   - Design aperture arrays in GDSII/DXF format with pad diameters sized at Gen 2 scale (e.g., 150 µm to 500 µm dots) arranged on a standardized 1.0 mm pitch.
   - Include peripheral fiduciary fiducial marks designed for alignment using the split-field binocular microscope with dual CMOS cameras.
   - Compensate for laser kerf width (~15–20 µm) by applying inward offset to CAD toolpaths.

2. **Substrate Preparation & Tension Mounting**:
   - Select 50 µm thick high-tensile Invar or SUS304 cold-rolled foil (CTE matched to Si handling stages).
   - Clean the foil with sequential ultrasonic degreasing in acetone (5 min), isopropanol (IPA, 5 min), and deionized (DI) water rinse; blow dry with filtered N2.
   - Clamp the foil into a rigid pneumatic or mechanical tensioning frame to maintain planarity (< 10 µm total thickness variation across the active mask area).

3. **Laser Micro-Machining / Direct Ablation**:
   - Mount the tensioned foil onto the CNC micro-machining vacuum chuck.
   - Execute aperture cutting using a pulsed UV (355 nm) or fiber picosecond laser source under coaxial N2 assist gas (2 bar) to minimize thermal heat-affected zone (HAZ) and slag formation.
   - Calibrate spot step-over and beam trepanning to ensure clean vertical sidewalls.

4. **Deburring & Chemical Polishing**:
   - Perform mild electro-chemical deburring or immersion in an acidic micro-etch bath (5% HNO3 / HCl solution for 30 s) to eliminate micro-burrs and molten spatter along aperture rims.
   - Post-rinse thoroughly in 18.2 MΩ·cm DI water cascade and bake dry at 110°C in an N2 purged convection oven.

5. **Metrology & Inspection**:
   - Inspect aperture diameters, circularity, and edge roughness using optical coordinate measuring microscope and the split-field dual CMOS camera inspection station.
   - Store the finished shadow mask in a dry-nitrogen desiccator cabinet (relative humidity < 15%).

---

### 3. Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Target Value | Physical Unit | Measurement Tool / Method |
| :--- | :--- | :--- | :--- |
| **Aperture Diameter Tolerance** | $\pm 5.0$ | $\mu\text{m}$ | Split-field optical microscope / CMOS image analysis |
| **Edge Burrs / Lip Roughness ($R_a$)** | $< 1.5$ | $\mu\text{m}$ | Optical profilometry / laser confocal metrology |
| **Foil In-Plane Planarity (Warp/Bow)** | $< 15.0$ | $\mu\text{m}$ | Multi-point dial indicator / laser distance sensor |
| **Laser Kerf HAZ (Heat-Affected Zone)**| $< 8.0$ | $\mu\text{m}$ | Calibrated metallurgical microscope |

---

### 4. Verified Literature Citations

- **Gate Dielectric Reference**: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*
  - *"Gate dielectric is thermally grown silicon dioxide (SiO2) at 850°C-900°C dry oxidation with ~3.5 nm physical thickness."*
  - Equivalent oxide thickness (EOT) around 3 to 4 nm with stacked capacitors targeting 25 to 30 fF data retention baseline.
- **Capacitance & Leakage Benchmark**: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
  - Minimum capacitance budget: $\ge 28\text{ fF/cell}$ to ensure noise immunity; leakage target: $\le 1\text{ fA/cell}$ at $85^\circ\text{C}$.
- **Alignment System Reference**: *Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose*
  - Stencil and substrate fiducial alignment verified using *"wafer and mask viewed through split-field binocular microscope with dual CMOS cameras."*

# Standard Operating Procedure (SOP)
## Multi-Point Type-S Thermocouple Calibration Tree & Quartz Thermowell Jig Assembly

- **Hierarchy**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > Fused Quartz Tube 3-Zone PID Furnace Assembly > 3-Zone Kanthal Heating Element & Decoupled PID Controller Commissioning > Multi-Point Isothermal Flat-Zone Profiling & ±0.5°C Uniformity Thermal Metrology > Multi-Point Type-S Thermocouple Calibration Tree & Quartz Thermowell Jig Assembly
- **Action Type**: Buy / Metrology Jig Assembly
- **Generation**: Gen 2 (µm)

---

### 1. Scope & Objective
Procure, inspect, encase, and assemble a multi-point Type-S (Platinum-Rhodium) profiling thermocouple tree inside high-purity fused quartz thermowells to profile and verify the 30 cm (300 mm) isothermal flat zone across Load, Center, and Source zones in a 3-zone diffusion/oxidation furnace.

---

### 2. Step-by-Step Operating Procedure

1. **Procurement & Physical Inspection (Action Type: Buy)**
   - Procure calibrated multi-junction Type-S Platinum-Rhodium (Pt-10% Rh/Pt) thermocouple assemblies and high-purity closed-end fused quartz (fused silica) thermowells.
   - Inspect thermocouple junction spacing to ensure measurement points span the central 300 mm wafer boat region across Load, Center, and Source furnace zones.

2. **Solvent & Cleanliness Preparation**
   - Clean the quartz thermowell jig using semiconductor-grade solvent and DI water rinses; dry with filtered N2 gas to eliminate alkali ion and metallic contaminants prior to insertion into the thermal core.

3. **Thermocouple Tree Jig Insertion & Encapsulation**
   - Insert the multi-point Type-S Platinum-Rhodium probe harness into the high-purity quartz thermowell jig.
   - Secure the external flange fitting with gas-tight, high-temperature seals to prevent ambient air back-streaming into the furnace tube.

4. **Furnace Loading & Mechanical Travel Rate Control**
   - Mount the quartz thermowell calibration jig onto the furnace cantilever/boat loading mechanism.
   - Initiate controlled mechanical insertion into the quartz process tube at a travel speed strictly `< 50 mm/minute` under laminar N2 purge (1 to 5 SLPM) to prevent thermal shock and tube damage.

5. **Multi-Zone Isothermal Profiling & Data Acquisition**
   - Connect the Type-S leads to the triple-loop digital PID controller/data-logger with feedforward decoupling.
   - Soak furnace across the operational temperature band (800°C to 1150°C) and log steady-state temperatures across the central 300 mm (30 cm) flat zone.

---

### 3. Machine-Measurable Acceptance Criteria Target Metrics

| Metric | Target Value | Physical Unit | Measurement Method |
| :--- | :--- | :--- | :--- |
| **Flat-Zone Temperature Uniformity** | `±0.5` | `°C` | Multi-point Type-S thermocouple reading across central zone |
| **Isothermal Flat-Zone Length** | `30` (300) | `cm` (`mm`) | Spatial span across Load, Center, and Source profiling points |
| **Max Mechanical Insertion Speed** | `< 50` | `mm/min` | Automated boat loader drive axis velocity |
| **Operating Temperature Range** | `800 to 1150` | `°C` | Digital PID controller setpoint band |
| **Laminar Carrier Gas Purge Flow** | `1 to 5` | `SLPM` | Mass Flow Controller (MFC) N2 delivery |

---

### 4. Verified Literature Citations

- **Source: Three-Zone Quartz Tube Thermal Dynamics and PID Temperature Regulation**:
  - *"Heating Elements: Kanthal-A1 or Super Kanthal molybdenum disilicide (MoSi2) coils divided into Load, Center, and Source zones."*
  - *"Thermocouples (Type R or Type S Platinum-Rhodium) encased in quartz thermowells."*
  - *"Temperature Uniformity: Must maintain ±0.5°C across the central 300 mm wafer boat region between 800°C and 1150°C."*
  - *"Gas Flow Dynamics: Laminar flow of carrier gases (N2 purge, ultra-pure O2, or forming gas) regulated by mass flow controllers (MFC) at 1 to 5 SLPM."*
  - *"Preventing Thermal Shock: Wafer boats must ramp in/out at slow mechanical speed (< 50 mm/minute) to avoid crystallographic slip dislocations."*
- **Source: Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace**:
  - *"Furnace Equipment: High-purity quartz process tube (fused silica), 3-zone PID temperature controller maintaining ±0.5°C over 30 cm flat zone."*

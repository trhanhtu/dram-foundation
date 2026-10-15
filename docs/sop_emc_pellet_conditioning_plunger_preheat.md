# Standard Operating Procedure (SOP)
## Epoxy Molding Compound (EMC) Pellet Conditioning & Plunger Pre-Heat Calibration

- **Document ID:** SOP-PKG-EMC-003
- **Generation:** Gen 3 (180nm CMOS Commercial MPW DRAM Tapeout)
- **Assembly Stage:** BEOL Multi-Layer Metallization, Wafer Sort & Packaging > Transfer Molding Epoxy Plastic Encapsulation (TSOP-54 / 54-ball FBGA Package)
- **Action Type:** Buy (Procured standard semiconductor grade EMC pellets & hydraulic plunger system)
- **Classification:** Level-4 Leaf Process Execution SOP

---

### 1. Process Overview & Operational Context
This procedure defines the rigorous conditioning protocol for B-stage thermosetting Epoxy Molding Compound (EMC) solid pellets and the closed-loop thermal calibration of the hydraulic transfer plunger prior to high-pressure transfer mold injection. 

Proper pellet pre-heating reduces melt viscosity, shortens injection transfer time, prevents wire sweep on fine 25 µm Au/Al wire-bonded interconnects, minimizes void formation (< 5%), and avoids thermal shock induced stress during in-mold encapsulation.

---

### 2. Operational Workflow Architecture

```text
┌────────────────────────┐
│                        │
│      Cold Storage      │
│       Retrieval        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Desiccator Thaw &    │
│     Stabilization      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     RF Pre-Heater      │
│  Calibration & Pellet  │
│          Load          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Plunger & Pot      │
│   Thermal Profiling    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Transfer Injection   │
│       Clearance        │
│                        │
└────────────────────────┘
```

---

### 3. Step-by-Step SOP Procedure

#### Step 1: Cold Storage Retrieval & Moisture-Proof Thawing
1. Retrieve sealed packaging containing semiconductor-grade EMC solid pellets (silica-filled, multi-functional epoxy resin) from cold storage maintained at **-5°C to 5°C**.
2. Transfer the intact, sealed moisture-barrier foil bags directly into a dry nitrogen-purged desiccator cabinet maintained at ambient cleanroom temperature (**25°C**, relative humidity $\le 30\%$).
3. Maintain continuous laminar dry $N_2$ purge sweep to prevent moisture condensation on pellet surfaces.
4. Allow full thermal equilibration for a minimum dwell time of **4.0 hours** until pellets reach room temperature (**25°C**). Do not breach the vacuum foil seal until stabilization is complete.

#### Step 2: Dielectric Radio-Frequency (RF) Pre-Heater Calibration
1. Calibrate the dielectric high-frequency RF pre-heater (operational frequency 27.12 MHz, RF power output regulated between 500 W and 1.5 kW).
2. Set the pre-heating target core temperature window to **90°C to 100°C** (nominal target: **95°C**).
3. Position pellets uniformly onto the non-stick carrier tray between parallel electrode plates.
4. Run RF heating cycle for **15 to 30 seconds**. Measure surface and core temperatures using a calibrated infrared sensor and non-contact pyrometer to confirm uniform internal dielectric heating without entering gelation/cross-linking onset.

#### Step 3: Transfer Plunger & Pot Multi-Zone PID Thermal Calibration
1. Power on the transfer molding press mold chase and plunger resistive heating elements.
2. Engage digital triple-loop PID temperature controllers with feedforward compensation regulating:
   - Upper Mold Chase Zone: Setpoint **175.0°C**.
   - Lower Mold Chase Zone: Setpoint **175.0°C**.
   - Transfer Plunger Tip & Injection Pot Zone: Setpoint **175.0°C**.
3. Insert calibrated dual thermocouples (Pt-Pt/Rh Type S/R) into the diagnostic measurement ports of the plunger tip and pot sleeve.
4. Monitor stabilization across a 30-minute soak window. Ensure temperature uniformity across the plunger circumference and pot bore maintains tight regulation within **±0.5°C**.

#### Step 4: Pellet Transfer, Plunger Loading & Injection Clearance
1. Using pneumatic vacuum suction wands with cleanroom fluoropolymer cups, immediately transfer the pre-heated pellet (core temperature **95°C ± 5°C**) into the pre-heated mold pot (**175°C**). Transfer transit time must not exceed **5.0 seconds** to avoid premature skin cure.
2. Verify mechanical plunger alignment concentricity with the pot bore (clearance gap maintained at **15 µm to 25 µm** to eliminate polymer flash leakage while preventing mechanical jamming).
3. Confirm plunger advance speed profile: fast approach (< 50 mm/s) transitioning to controlled transfer injection velocity (1.0 mm/s to 5.0 mm/s) upon contacting plasticized resin.

---

### 4. Thermal Process Target Profile

```text
                EMC Thermal Conditioning Profile (°C)   
             ┌─────────────────────────────────────────┐
             │█████████████████████████████████████████│
 Mold Chase T┤█████████████████████████████████████████│
             │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
Plunger PID T┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
Pellet Core T┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  │
             │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  │
Ambient Equil┤░░░░░░░                                  │
             │░░░░░░░                                  │
             └┬─────────┬─────────┬─────────┬─────────┬┘
             0.0      43.8      87.5      131.2   175.0 
```

---

### 5. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Inspection / Measurement Method | Target Value | Engineering Unit | Tolerance |
| :--- | :--- | :--- | :--- | :--- |
| **Pellet Core Temperature** | In-line non-contact IR pyrometer / thermal probe | `95.0` | `°C` | `± 5.0 °C` |
| **Plunger & Pot Isothermal Uniformity** | Multi-point Pt-Pt/Rh Type S/R thermocouple grid with PID logging | `175.0` | `°C` | `± 0.5 °C` |
| **Pellet-to-Pot Transfer Dwell Time** | Automated robotic arm / PLC cycle timer | `≤ 5.0` | `s` | `Max limit` |
| **Encapsulation Void Area** | Scanning Acoustic Microscopy (C-SAM) across package & die interface | `< 5.0` | `%` | `Area %` |

---

### 6. Literature Citations & Physical Reference Baseline
- **Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging:**
  - Ambient room temperature baseline (**25°C**) for wire-bonding handling and pre-conditioning staging.
  - Wire pull and mechanical interconnect integrity standards on 25 µm wire spans connecting 100 µm × 100 µm pads, dictating void limits (**void area < 5%** via acoustic microscopy) and gentle rheological flow during molding to avoid wire sweep.
- **Three-Zone Quartz Tube Thermal Dynamics and PID Temperature Regulation:**
  - Multi-zone PID temperature regulation framework utilizing dual Type-R / Type-S Pt-Pt/Rh thermocouples.
  - High-precision isothermal zone stability standards enforcing thermal uniformity within **±0.5°C**.
  - Mechanical velocity ramping constraints preventing thermal shock dislocations.
- **Three-Zone Quartz Tube Diffusion Furnace Thermal Profiling & Gas Delivery:**
  - Inert $N_2$ laminar sweep velocity dynamics (2.0 to 5.0 SLPM) utilized in moisture-controlled desiccator chambers for oxygen and ambient condensation suppression.

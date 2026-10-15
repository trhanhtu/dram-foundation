# Standard Operating Procedure (SOP)
## Precision Tooling & Fixturing for Post-Fill LVS & Electrical Rule Check (ERC) Sign-Off

- **Document ID**: SOP-MECH-180DRAM-LVS-ERC-001
- **Process Generation**: 180nm Open-Source DRAM (Gen 3)
- **Hierarchy Path**: Context: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm CMOS Commercial MPW Tapeout & PDK Implementation [Foundry Tapeout & PDK] > Multi-Project Wafer (MPW) Shuttle GDSII Tapeout Package & Foundry Sign-Off [Foundry Tapeout & PDK] > Full-Chip Physical Verification (DRC/LVS/ERC/Antenna) & Dummy Metal Fill Synthesis [Metrology] > Post-Fill LVS & Electrical Rule Check (ERC) Sign-Off [Metrology] > Precision Tooling & Fixturing for Post-Fill LVS & Electrical Rule Check (ERC) Sign-Off [Mechanical Assembly]
- **Action Type**: Make

---

### 1. Purpose & Scope
This Standard Operating Procedure (SOP) defines the mechanical tooling, fixturing, vacuum stage planarization, and thermal-mechanical stabilization protocols required to perform post-fill Layout Versus Schematic (LVS) and Electrical Rule Check (ERC) hardware validation and metrology sign-off on 180nm open-source DRAM prototypes. The procedure details the alignment, clamp torquing, package fixturing, bonding pad contact geometry, and thermal stabilization necessary to correlate physical netlist extractions (storage capacitance, bitline pitch, leakage, and wire bonding interfaces) against physical verification rule decks.

---

### 2. Tooling & Fixturing Workflow

```text
┌───────────────────────────────────────┐
│ Vacuum Chuck & Substrate Fixturing    │
│  - Anodized Al/Ceramic Stage Leveling │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ Multi-Contact Probe/Package Clamping  │
│  - Torqued Clamp (0.15 - 0.20 N·m)    │
│  - 100 µm x 100 µm Pad Interface      │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ Thermal Stabilization & Chuck Bias    │
│  - T = 85°C ± 0.5°C Retention Soak    │
│  - Ablebond 84-1LMIS Die Attach       │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ Post-Fill LVS & ERC Sign-Off Run      │
│  - Parasitic Extraction Correlation   │
│  - Netlist & Soft-Error Integrity     │
└───────────────────────────────────────┘
```

---

### 3. Step-by-Step Execution Procedure

1. **Precision Chuck & Mechanical Substrate Mounting**:
   - Clean the multi-zone ceramic/anodized vacuum chuck using cleanroom-grade isopropanol and nitrogen purge at 30 psi.
   - Position the 180nm DRAM test vehicle/substrate onto the chuck with planar parallelism alignment $\le 2\ \mu\text{m}$ across a $20\text{ mm} \times 20\text{ mm}$ fixturing field.
   - Engage vacuum hold-down pressure at $-80\text{ kPa}$ nominal to secure the test vehicle against lateral drift during probe head touchdown.

2. **Package Fixturing & Wire Bond Boundary Preparation**:
   - Mount ceramic DIP / QFN package carrier into the zero-insertion-force (ZIF) precision clamping fixture.
   - Fasten mechanical retention clamps diagonally using a calibrated micro-torque wrench set to $0.18\text{ N}\cdot\text{m}$ (tolerance $0.15\text{ to } 0.20\text{ N}\cdot\text{m}$).
   - Verify die attach compliance: Silver-filled conductive epoxy (Ablebond 84-1LMIS) cured at $150^\circ\text{C}$ for $60\text{ minutes}$, verifying thermal resistance $R_{th} \le 5^\circ\text{C/W}$ and acoustic microscopy void area $< 5\%$.
   - Confirm peripheral bond pad coordinates matching $100\ \mu\text{m} \times 100\ \mu\text{m}$ aluminum squares ready for $25\ \mu\text{m}$ diameter wire bonding (thermosonic Au or ultrasonic Al-1% Si wedge).

3. **Thermal Conditioning for Electrical Rule Check (ERC) & Retention Validation**:
   - Connect closed-loop thermal chuck controller and ramp temperature to the physical sign-off corner of $85^\circ\text{C} \pm 0.5^\circ\text{C}$.
   - Allow thermal soak stabilization for a minimum of $15\text{ minutes}$ to eliminate mechanical expansion drift.
   - Verify substrate ground and well tap fixturing continuity to prevent floating bulk nodes or ERC latchup violations during bias application.

4. **Post-Fill LVS & Extraction Hardware Correlation Execution**:
   - Align micro-contact probe cards or packaged lead interfaces with optical alignment aids to target pads with touchdown overtravel limited to $25\ \mu\text{m} \pm 5\ \mu\text{m}$.
   - Execute post-fill LVS verification checking that dummy metal fills induce zero shorts to active folded bitline traces (bitline pitch $360\text{ nm to } 400\text{ nm}$, gate length $L = 180\text{ nm}$, width $W = 220\text{ nm}$).
   - Correlate hardware capacitance and leakage against extraction decks:
     - Verify cell storage capacitance $C_s \ge 28\text{ fF}$ (stacked capacitor ONO / $\text{Ta}_2\text{O}_5$ stack with $\kappa > 15$, EOT $3\text{ to } 4\text{ nm}$).
     - Verify off-state sub-threshold and junction leakage current remains $\le 1\text{ fA/cell at } 85^\circ\text{C}$ to maintain target retention intervals $> 64\text{ ms}$.

5. **Tooling Release & Sign-Off Documentation**:
   - Ramp thermal stage down to ambient room temperature ($25^\circ\text{C}$).
   - Disengage mechanical clamping torque and release vacuum chuck.
   - Archive mechanical fixturing logs, overtravel telemetry, and post-fill LVS/ERC sign-off correlation results into the quality acceptance database.

---

### 4. Machine-Measurable Acceptance Criteria

```text
                 ┌─────────────────────────────────────┐
Wire Pull (gf)   │░░░░                                 │
                 │░░░░                                 │
Storage C_s (fF) │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         │
                 │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         │
Die Attach Void %│▓▓▓▓▓                                │
                 │▓▓▓▓▓                                │
Pad Size (µm)    │█████████████████████████████████████│
                 │█████████████████████████████████████│
                 └┬─────────┬─────────┬────────┬───────┘
                  0        25        50       75     100
```

| Parameter / Metrology Target | Acceptance Metric Target Value | Unit | Verification Method |
| :--- | :--- | :--- | :--- |
| **Die Attach Void Area** | $< 5.0$ | $\%$ | Scanning Acoustic Microscopy (C-SAM) |
| **Bonding Pad Geometry** | $100 \times 100$ | $\mu\text{m}$ | Optical Calibrated Stage Metrology |
| **Interconnect Wire Pull Strength** | $\ge 4.0$ ($25\ \mu\text{m}$ wire) | $\text{grams-force (gf)}$ | Mil-Std-883 Method 2011 Pull Tester |
| **Cell Storage Node Capacitance ($C_s$)** | $\ge 28.0$ (Budget: $25\text{ to } 30$) | $\text{fF}$ | Post-Fill LVS Netlist / Hardware C-V Correlation |
| **Cell Junction & Sub-Threshold Leakage** | $\le 1.0$ at $85^\circ\text{C}$ (Retention $> 64\text{ ms}$) | $\text{fA/cell}$ | Parametric Electrometer / ERC Thermal Soak |

---

### 5. Context Literature Citations
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$; shared bitline contact; stacked capacitor over bitline (COB) crown/MIM topology with W-plug; ONO or $\text{Ta}_2\text{O}_5\text{ / }\text{Al}_2\text{O}_3$ dielectric stack with $\kappa > 15$; minimum capacitance budget $\ge 28\text{ fF/cell}$; leakage current target $\le 1\text{ fA/cell at } 85^\circ\text{C}$ to maintain refresh retention intervals.
- **Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging**: On-chip bonding pad dimensions ($100\ \mu\text{m} \times 100\ \mu\text{m}$ aluminum squares); $25\ \mu\text{m}$ diameter wire bonding (thermosonic Au at $150^\circ\text{C}$, $60\text{ kHz}$, $50\text{--}100\text{ mW}$, $20\text{--}30\text{ ms}$, or ultrasonic Al-1% Si wedge at $25^\circ\text{C}$ for ceramic DIP/QFN); wire pull strength $\ge 4.0\text{ grams-force}$ per Mil-Std-883 Method 2011; Ablebond 84-1LMIS silver-filled conductive epoxy cured at $150^\circ\text{C}$ for $60\text{ min}$ with thermal resistance $R_{th} \le 5^\circ\text{C/W}$ and void area $< 5\%$ under acoustic microscopy.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: 1T1C stacked capacitor architecture ($8F^2 / 6F^2$ layouts); minimum storage capacitance of $25\text{ to } 30\text{ fF/cell}$ for data retention $> 64\text{ ms at } 85^\circ\text{C}$; stacked capacitor equivalent oxide thickness (EOT) $3\text{ to } 4\text{ nm}$; bitline and wordline pitch $360\text{ to } 400\text{ nm}$; gate dielectric $3.5\text{ nm}$ thermally grown $\text{SiO}_2$ at $850^\circ\text{C}\text{--}900^\circ\text{C}$.

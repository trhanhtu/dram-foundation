# Standard Operating Procedure (SOP): Buffered Oxide Etch (BOE 6:1) SiO2 Patterning

- **Document ID**: SOP-180NM-BOE-001
- **Process Step**: Wet Etch & Patterning (Chemical Processing)
- **Node**: 180nm Open-Source DRAM (Gen 1)
- **Author**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Released

---

## 1. Scope & Objective
This SOP defines the wafer-level wet chemical etching process using Buffered Oxide Etch (BOE 6:1) for selective $\text{SiO}_2$ patterning on 180nm DRAM architectures (e.g., access transistor hardmask, dielectric contact window openings, capacitor isolation).

---

## 2. Chemical Formulation & Specifications
- **Solution Ratio**: $6:1$ by volume ($6 \text{ parts } 40\% \text{ NH}_4\text{F} : 1 \text{ part } 49\% \text{ HF}$).
- **Buffer Mechanism**: $\text{NH}_4\text{F}$ maintains constant fluoride ion activity and bath $\text{pH} \approx 4.5$.
- **Surfactant / Wetting Agent**: $0.1\%$ Triton X-100 or Fluorad added to eliminate micro-bubble entrapment across sub-micron topologies.
- **Bath Temperature**: $25^\circ\text{C} \pm 0.5^\circ\text{C}$.

---

## 3. Step-by-Step Operating Procedure

1. **Pre-Etch Adhesion & Lithography Preparation**:
   - Perform HMDS (Hexamethyldisilazane) vapor prime at $120^\circ\text{C}$ prior to photoresist coating to prevent undercut and resist peeling.
   - Inspect patterned photoresist mask under optical/CD inspection before chemical immersion.

2. **Bath Preparation & Thermal Equilibration**:
   - Verify recirculation and bath temperature at $25.0^\circ\text{C} \pm 0.5^\circ\text{C}$.
   - Ensure $0.1\%$ wetting agent is thoroughly dispersed.
   - Confirm HF safety station readiness: calcium gluconate gel inspected and verified on-site.

3. **Immersion Etch**:
   - Calculate immersion duration based on film type and target thickness:
     - Thermally grown $\text{SiO}_2$: nominal rate $80\text{--}100\text{ nm/min}$ ($800\text{--}1000\text{ \AA/min}$).
     - CVD / TEOS $\text{SiO}_2$: nominal rate $150\text{--}220\text{ nm/min}$.
     - Native oxide breakthrough: $10\text{--}15\text{ seconds}$.
   - Submerge wafer cassette smoothly with mild agitation.

4. **Quench & Cascade Rinse**:
   - Rapidly transfer wafer cassette within $< 3\text{ seconds}$ to Quick Dump Rinse (QDR) DI water bath.
   - Execute 3x QDR cycles followed by overflow DI cascade rinse until bath resistivity reaches $> 18.0\text{ M}\Omega\cdot\text{cm}$.

5. **Drying & Post-Etch Metrology**:
   - Spin-rinse dry (SRD) or Marangoni dry with heated $\text{N}_2$.
   - Measure residual oxide thickness using spectroscopic ellipsometry across 9 target points.

---

## 4. Machine-Measurable Acceptance Criteria

| Parameter | Inspection / Metrology Method | Target Metric & Tolerance | Units |
| :--- | :--- | :--- | :--- |
| **Thermal $\text{SiO}_2$ Etch Rate** | Spectroscopic Ellipsometry ($25^\circ\text{C}$) | $80.0 \text{ to } 100.0$ | $\text{nm/min}$ |
| **CVD / TEOS $\text{SiO}_2$ Etch Rate** | Spectroscopic Ellipsometry ($25^\circ\text{C}$) | $150.0 \text{ to } 220.0$ | $\text{nm/min}$ |
| **Selectivity ($\text{SiO}_2$ : Si)** | Thickness loss ratio (Ellipsometry / Profilometry) | $> 100 : 1$ | ratio |
| **Selectivity ($\text{SiO}_2$ : $\text{Si}_3\text{N}_4$)** | Thickness loss ratio (Ellipsometry / Profilometry) | $> 20 : 1$ | ratio |
| **Bath Temperature Control** | Inline RTD Sensor | $25.0 \pm 0.5$ | $^\circ\text{C}$ |
| **DI Cascade Final Resistivity** | Inline Resistivity Meter | $\ge 18.0$ | $\text{M}\Omega\cdot\text{cm}$ |

---

## 5. Citations & References
- *Buffered Oxide Etch (BOE 6:1 & 7:1) Silicon Dioxide Wet Etch Rates*
- *Silicon Dioxide Etching with Buffered Oxide Etch (BOE)*
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*

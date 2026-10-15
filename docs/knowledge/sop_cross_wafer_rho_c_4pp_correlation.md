# SOP: Cross-Wafer Specific Contact Resistivity Mapping and Four-Point Probe Correlation

- **Document ID**: `SOP-MET-TLM-4PP-001`
- **Revision**: 1.0
- **Process Node**: 180nm Open-Source DRAM (DRAM Foundation VN Gen 3)
- **Hierarchy Path**: `[Architecture & Integration] > [Foundry Tapeout & PDK] > [BEOL & Packaging] > [Thin Film Deposition] > [Metrology] > Cross-Wafer Specific Contact Resistivity Mapping and Four-Point Probe Correlation`
- **Action Type**: Buy / Standard Metrology

---

## 1. Scope & Objective
This Standard Operating Procedure (SOP) defines the operational procedure for correlating cross-wafer thin film sheet resistance ($R_s$) measured via collinear four-point probe (4PP) with Transmission Line Measurement (TLM) parameters—specifically contact resistance ($R_c$), transfer length ($L_T$), and specific contact resistivity ($\rho_c$)—on 180nm DRAM metallization and diffusion test structures.

---

## 2. Metrology Workflow

```text
┌────────────────────────┐                             ┌────────────────────────┐
│                        │                             │                        │
│  Four-Point Collinear  │                             │  TLM Test Structures   │
│      Probe (4PP)       │                             │      across Wafer      │
│                        │                             │                        │
└────────────┬───────────┘                             └────────────┬───────────┘
             │                          Vary d: 5, 10, 20, 40, 80 um│
             │Measure V/I, s=1.0mm                                  │
             ▼                                                      ▼
┌────────────────────────┐                             ┌────────────────────────┐
│                        │                             │                        │
│   Extract Film Sheet   │                             │   Extract R_c, L_T,    │
│     Resistance R_s     │                             │         rho_c          │
│                        │                             │                        │
└───────────┬────────────┘                             └────────────┬───────────┘
            │                                                       │
            │ ╭─────────────────────────────────────────────────────╯
            ▼ ▼
┌────────────────────────┐
│                        │
│  Cross-Wafer Spatial   │
│      Correlation       │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   Disposition & PDK    │
│       Acceptance       │
│                        │
└────────────────────────┘
```

---

## 3. Tool Setup & Physical Parameters

### 3.1 Four-Point Probe (4PP) Setup
- **Probe Tip Material**: Tungsten carbide (WC).
- **Tip Radius ($r_{tip}$)**: $50\ \mu\text{m}\text{ to }100\ \mu\text{m}$.
- **Probe Spacing ($s$)**: $1.0\ \text{mm}$ (collinear, equal spacing).
- **Excitation Current Source**: Constant DC current $I = 1.0\ \text{mA}\text{ to }10.0\ \text{mA}$ applied through outer probes 1 and 4.
- **Potential Difference Metrology**: High-impedance floating DC voltage drop ($V$) measured across inner probes 2 and 3.
- **Thin Film Approximation**: Valid for film thickness $t \ll s/2$ ($t \ll 500\ \mu\text{m}$).
  $$R_s = \frac{\pi}{\ln(2)} \cdot \frac{V}{I} \approx 4.5324 \cdot \frac{V}{I}\ [\Omega/\square]$$
- **Geometric Edge Correction**: Apply geometric correction factor $F(d/s)$ when distance from probe to wafer boundary is less than $40 \cdot s$ ($< 40\ \text{mm}$).

### 3.2 Transmission Line Measurement (TLM) Test Die
- **Contact Pad Geometry**: Width $W = 100\ \mu\text{m}$, Length $L_{pad} = 50\ \mu\text{m}$.
- **Gap Spacings ($d$)**: Progressive pitch series of $5\ \mu\text{m}$, $10\ \mu\text{m}$, $20\ \mu\text{m}$, $40\ \mu\text{m}$, and $80\ \mu\text{m}$.
- **Contact Structure**: BEOL metallization contact to doped silicon diffusion (incorporating tungsten plug / bitline contact metallization).

---

## 4. Step-by-Step Operating Procedure

1. **Pre-Alignment & Wafer Loading**:
   - Load post-forming-gas annealed wafer onto automatic prober chuck under laminar cleanroom environment.
   - Perform optical pattern recognition (die alignment) on scribe-line TLM macro structures across designated cross-wafer sample sites (e.g., center, mid-radius, wafer edge).

2. **Four-Point Probe (4PP) Metrology**:
   - Lower the four-point tungsten carbide probe head onto dedicated blanket/scribed test areas adjacent to the TLM die locations.
   - Inject DC current $I = 1.0\ \text{mA}\text{ to }10.0\ \text{mA}$ between probe 1 and 4.
   - Measure floating potential $V$ across probe 2 and 3. Compute bulk/thin-film sheet resistance:
     $$R_{s,\text{4PP}} = 4.5324 \cdot \left(\frac{V}{I}\right) \cdot F(d/s)$$

3. **TLM Pad Resistance Characterization**:
   - Land Kelvin probe tips on adjacent rectangular TLM pads of width $W = 100\ \mu\text{m}$ and length $L_{pad} = 50\ \mu\text{m}$.
   - Sequentially measure total two-terminal resistance $R_T$ across each gap spacing $d \in \{5, 10, 20, 40, 80\}\ \mu\text{m}$ using small-signal DC sweeps.

4. **Parameter Extraction**:
   - Construct linear regression of $R_T$ versus pad spacing $d$:
     $$R_T = 2 R_c + \left(\frac{R_s}{W}\right) d$$
   - Calculate extracted sheet resistance: $R_{s,\text{TLM}} = \text{Slope} \times W = \text{Slope} \times 100\ \mu\text{m}$.
   - Determine contact resistance: $R_c = \frac{\text{Y-intercept}}{2}$.
   - Determine transfer length: $L_T = -\frac{\text{X-intercept}}{2} = \frac{R_c \cdot W}{R_s}$.
   - Compute specific contact resistivity:
     $$\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\ [\Omega\cdot\text{cm}^2]$$

5. **Cross-Wafer Spatial Mapping & Correlation**:
   - Map $\rho_c$, $L_T$, $R_c$, and $R_{s,\text{TLM}}$ against $R_{s,\text{4PP}}$ across the wafer coordinates.
   - Compute correlation coefficient and delta ($\Delta R_s = |R_{s,\text{4PP}} - R_{s,\text{TLM}}|$) to evaluate BEOL metallization and contact interface uniformity.

---

## 5. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Nominal / Target Specification | Tolerance / Boundary | Measurement Method |
| :--- | :--- | :--- | :--- |
| **Collinear Probe Tip Radius** | $50\ \mu\text{m}\text{ to }100\ \mu\text{m}$ | Specified range | Metrology Inspection |
| **Probe Spacing ($s$)** | $1.0\ \text{mm}$ | Nominal collinear spacing | 4PP Head Calibration |
| **4PP DC Test Current** | $1.0\ \text{mA}\text{ to }10.0\ \text{mA}$ | Constant DC compliance | Parameter Analyzer / SMU |
| **TLM Contact Pad Dimensions** | $W = 100\ \mu\text{m}$, $L_{pad} = 50\ \mu\text{m}$ | Exact layout dimension | CD-SEM / Optical Verification |
| **TLM Gap Spacing Series ($d$)** | $5\ \mu\text{m}, 10\ \mu\text{m}, 20\ \mu\text{m}, 40\ \mu\text{m}, 80\ \mu\text{m}$ | Exact test layout sequence | Automated Stepper Metrology |
| **Thin Film Correction Multiplier** | $4.5324$ ($\pi / \ln(2)$) | Analytical exact | 4PP Algorithm Check |

---

## 6. Literature & Context Citations
- **Four-Point Collinear Probe Metrology for Semiconductor Sheet Resistance**: Collinear tungsten carbide tips (radius $50\text{--}100\ \mu\text{m}$, spacing $s = 1.0\ \text{mm}$), DC current excitation $I = 1\text{--}10\ \text{mA}$, thin film relation $R_s = (\pi / \ln(2)) \cdot (V / I) = 4.5324 \cdot (V / I)\ [\Omega/\square]$, edge correction factor $F(d/s)$ for boundary $< 40 \cdot s$.
- **Transmission Line Measurement (TLM) for Specific Contact Resistivity**: Pad width $W = 100\ \mu\text{m}$, pad length $L_{pad} = 50\ \mu\text{m}$, gap steps $d = 5\ \mu\text{m}, 10\ \mu\text{m}, 20\ \mu\text{m}, 40\ \mu\text{m}, 80\ \mu\text{m}$, formulation $R_T = 2 R_c + (R_s / W) \cdot d$, $R_s = \text{Slope} \cdot W$, $Y\text{-intercept} = 2 R_c$, $X\text{-intercept} = -2 L_T$, $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\ [\Omega\cdot\text{cm}^2]$.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: 180nm technology node reference, bitline contact shared between memory cells, tungsten plug (W-plug) connection.

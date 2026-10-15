# Standard Operating Procedure (SOP)
## Collinear 4-Point Probe Mapping & Sheet Resistance Calibration

- **Document ID**: `SOP-MET-4PP-180NM-001`
- **Module**: Back-End of Line (BEOL) Metrology & Thin Film Calibration
- **Node**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Status**: Accepted / Ready for Execution

---

### 1. Scope & Objective
This SOP defines the setup, measurement routine, geometric correction, and calibration procedure for evaluating sheet resistance ($R_s$) of post-anneal Al-0.5%Cu metal-1 interconnect films using a collinear 4-point probe station.

---

### 2. Metrology Workflow

```text
┌───────────────────────┐
│                       │
│   Wafer Loading and   │
│    Edge Alignment     │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Probe Head Descent   │
│      and Contact      │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  DC Current Sourcing  │
│    Probes 1 and 4     │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│    Voltage Sensing    │
│    Probes 2 and 3     │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Rs Calculation and   │
│    Edge Correction    │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Acceptance Criteria  │
│     Verification      │
│                       │
└───────────────────────┘
```

---

### 3. Step-by-Step Operating Procedure

1. **Station Pre-Check & Probe Tip Qualification**:
   - Inspect the collinear probe head containing 4 tungsten carbide tips with radius $r = 50\text{ to }100\ \mu\text{m}$ and uniform tip spacing $s = 1.0\text{ mm}$.
   - Ensure probe tips are free of mechanical deformation or contamination.

2. **Wafer Loading & Alignment**:
   - Load the 180nm post-metal annealed wafer (post 400°C, 30 min forming gas anneal $95\%\ \text{N}_2 / 5\%\ \text{H}_2$, nominal metal-1 thickness $t = 350\text{ nm} \pm 5\%$) onto the vacuum chuck.
   - Record wafer diameter and verify test site positioning to maintain boundary proximity clearance $> 40 \times s$ (or calculate edge correction factor $F(d/s)$ if measuring near wafer boundaries).

3. **Probe Landing & Contact Formation**:
   - Lower the 4-point probe head until all 4 tips make controlled, non-destructive ohmic contact with the Al-0.5%Cu interconnect surface.

4. **Constant DC Current Injection**:
   - Source a calibrated constant DC current $I$ across outer probe pins 1 and 4 within the operating window of $I = 1\text{ mA to }10\text{ mA}$.

5. **Differential Potential Sensing**:
   - Measure the floating potential difference $V$ across inner probe pins 2 and 3 using high-input-impedance digital sensing.

6. **Sheet Resistance ($R_s$) Calculation & Calibration**:
   - For thin conductive films where $t \ll s/2$ ($350\text{ nm} \ll 0.5\text{ mm}$):
     $$R_s = \frac{\pi}{\ln(2)} \cdot \left(\frac{V}{I}\right) \approx 4.5324 \cdot \left(\frac{V}{I}\right)\ [\Omega/\square]$$
   - Apply geometric correction factor $F(d/s)$ for measurement coordinates located within distance $d < 40s$ from wafer boundaries:
     $$R_{s,\text{corrected}} = R_s \cdot F(d/s)$$

---

### 4. Acceptance Criteria & Target Metrics

| Metric | Target / Specification | Inspection Method / Formula | Unit |
| :--- | :--- | :--- | :--- |
| **Metal-1 Sheet Resistance ($R_s$)** | $R_s < 0.08$ | Inner-probe potential sensing ($4.5324 \cdot V/I$) | $\Omega/\square$ |
| **Probe Spacing ($s$)** | $1.0 \pm 0.01$ | Optical / mechanical stage calibration | $\text{mm}$ |
| **Probe Tip Radius ($r$)** | $50\text{ to }100$ | Tip profile inspection (Tungsten Carbide) | $\mu\text{m}$ |
| **Applied DC Test Current ($I$)** | $1\text{ to }10$ | Outer probe (1 & 4) current source | $\text{mA}$ |

---

### 5. Verified Literature Sources
- **Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects**: Film target thickness ($350\text{ nm} \pm 5\%$), post-metal anneal conditions (forming gas $\text{N}_2/\text{H}_2\ 95/5$ at 400°C for 30 minutes), and target sheet resistance requirement ($R_s < 0.08\ \Omega/\square$).
- **Four-Point Collinear Probe Metrology for Semiconductor Sheet Resistance**: Tungsten carbide probe geometry ($r = 50\text{--}100\ \mu\text{m}$, $s = 1.0\text{ mm}$), operating current ($1\text{ to }10\text{ mA}$), floating potential configuration, thin-film formula ($R_s = 4.5324 \cdot V/I$), and edge correction rules ($F(d/s)$ for $< 40s$).

# Four-Point Probe Calibration & TiN Planar Monitor Sheet Resistance Metrology

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure (SOP) for calibrating collinear four-point probe (4PP) metrology tools and executing sheet resistance ($R_s$) mapping on TiN planar test monitors representing the conformal top electrode of 180nm crown capacitor DRAM cells. Accurate sheet resistance control directly governs RC wordline/bitline delay, electrode potential distribution, and soft-error immunity.

## SOP Workflow Diagram
```text
┌────────────────────────┐
│     NIST Standard      │
│      Calibration       │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│     Probe Head Pin     │
│      Conditioning      │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│     Planar Monitor     │
│        Loading         │
└────────────┬───────────┘
             │
             ▼
┌────────────────────────┐
│  49-Point Contour Map  │
│          Scan          │
└────────────┬───────────┘
             │
             ▼
┌────────────◇───────────┐
│     Tolerance Met?     │
└────────────◇───────────┘
             │
             ├──────────────╮No
          Yes│              │
             ▼              ▼
┌────────────────────────┐ ┌────────────────────────┐
│     Lot Release to     │ │       Hold Lot &       │
│     Metrology Gate     │ │      Recalibrate       │
└────────────────────────┘ └────────────────────────┘
```

## Step-by-Step SOP Procedure

### Phase 1: Tool Warmup & Environmental Baseline
1. Ensure the cleanroom ambient temperature is stabilized at $21.0 \pm 0.5^\circ\text{C}$ with relative humidity $\le 45\%$.
2. Power on the high-precision 4PP station (dual-configuration switching system with tungsten carbide or Osmium tips, probe spacing $s = 1.0\,\text{mm}$, tip radius $100\,\mu\text{m}$, tip loading force $40 \text{ to } 70\,\text{g}$).
3. Allow current source and digital electrometer pre-amplifiers to warm up for $\ge 30\,\text{minutes}$.

### Phase 2: Probe Head Inspection & NIST Standard Calibration
1. Inspect probe tips under optical microscope ($50\times$) for tip blunting, mechanical deformation, or metallic accumulation.
2. Load a NIST-traceable calibrated reference wafer (certified bulk standard, nominal $R_s = 10.00\,\Omega/\text{sq} \pm 0.5\%$).
3. Apply test current $I = 1.0\,\text{mA}$. Execute a 5-repetition measurement cycle at center die.
4. Calculate average $R_s$ and verify that deviation from certified standard value is within $\le \pm 0.5\%$.
5. Perform geometric correction factor check ($C(D/s, t/s)$) confirming edge proximity and thin-film boundary condition formulation ($R_s = \frac{\pi}{\ln 2} \frac{V}{I} \cdot f_1 \cdot f_2$).

### Phase 3: TiN Planar Monitor Handling & Measurement
1. Inspect the incoming blanket monitor wafer accompanying the 180nm crown capacitor lot (TiN top electrode deposited via thermal ALD $\text{TiCl}_4 / \text{NH}_3$).
2. Transfer monitor wafer onto the vacuum chuck (vacuum level $\ge 70\,\text{kPa}$). Align wafer notch/flat to $0^\circ$ coordinate.
3. Configure automated polar/Cartesian recipe:
   - Measurement Pattern: 49-point circular contour map.
   - Edge Exclusion: $3.0\,\text{mm}$.
   - Sourcing Current: $I = 10.0\,\text{mA}$ forward and reverse polarity (dual-sweep cancellation of thermoelectric EMF).
4. Run measurement sequence; record raw voltage drop $V$, calculate dual-configuration corrected sheet resistance $R_s$ per site.

### Phase 4: Data Processing & Process Disposition
1. Compute mean sheet resistance $\bar{R}_s$, standard deviation $\sigma$, and percentage non-uniformity:
   $$\text{NU}(\%) = \left(\frac{R_{s,\max} - R_{s,\min}}{2 \cdot \bar{R}_s}\right) \times 100\% \quad \text{or} \quad \left(\frac{1\sigma}{\bar{R}_s}\right) \times 100\%$$
2. Compare metrics against lot acceptance thresholds. If within limits, sign off metrology step in MES and release capacitor lot to post-metal anneal/interconnect metallization.
3. If criteria fail, trigger Out-of-Control Action Plan (OCAP): hold wafer lot, verify probe head resistance, check ALD precursor delivery log.

## Machine-Measurable Acceptance Criteria Target Metrics
1. **Instrument Calibration Baseline Accuracy**: $\le \pm 0.50\%$ deviation against NIST-traceable transfer standard ($R_s = 10.00\,\Omega/\text{sq}$).
2. **TiN Planar Monitor Mean Sheet Resistance ($\bar{R}_s$)**: $25.0 \pm 2.5\,\Omega/\text{sq}$ (target thin-film regime for conformal crown capacitor top electrode, distinct from interconnect Al-0.5% Cu $R_s < 0.08\,\Omega/\text{sq}$).
3. **Cross-Wafer Sheet Resistance Uniformity ($1\sigma / \bar{R}_s$)**: $\le 2.0\%$ across a 49-point map with $3.0\,\text{mm}$ edge exclusion.
4. **Thermoelectric & Contact Repeatability**: Forward-to-reverse current polarity variation $\Delta R_s \le 0.15\%$ across 10 repeated center-point touches.

## References & Related Files
- [180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench](./docs/knowledge/four_point_probe_tin_sop.md)
- [Legacy 180nm DRAM Architecture & Cell Capacitor Engineering](./docs/context.yaml)
- [Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects](./docs/context2.yaml)

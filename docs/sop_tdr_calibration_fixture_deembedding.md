# SOP: TDR Calibration & Microstrip Reference Fixture SOLT De-embedding

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Multi-Agent Council)
- **Status**: Accepted
- **Generation**: Gen 3 (nm) / 180nm CMOS Commercial MPW Tapeout & PDK Implementation
- **Module**: Final Automated Test Equipment (ATE) JEDEC DDR Speed-Bin & HTOL Burn-in Testing > ATE Loadboard Interface Design & JEDEC Timing Vector Pattern Generation > ATE DUT Loadboard PCB Schematic & High-Speed Impedance-Matched Layout > TDR Transmission Line Metrology & S-Parameter Signal Integrity Verification > TDR Calibration & Microstrip Reference Fixture SOLT De-embedding

## Overview & Rationale
High-speed JEDEC DDR timing verification for the 180nm Open-Source DRAM chip requires sub-picosecond signal integrity and controlled microstrip trace characteristic impedance ($Z_0 = 50.0\,\Omega$) on the ATE DUT loadboard. Coaxial cables, high-frequency launch connectors (SMA/SMP/2.92mm), and test fixture lead-in microstrip traces introduce parasitic inductance, capacitance, and insertion loss that mask the true DUT launch pad discontinuities and signal propagation delay. This Standard Operating Procedure (SOP) specifies the physical calibration procedure using Short-Open-Load-Thru (SOLT) coaxial standards and 2x-Thru / Automatic Fixture Removal (AFR) de-embedding to shift the measurement reference plane directly to the ATE DUT microstrip launch pads.

## Workflow Architecture
```text
┌────────────────────────┐
│                        │
│   VNA/TDR Instrument   │
│          Prep          │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  SOLT Coaxial 2-Port   │
│          Cal           │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│    Fixture 2x Thru     │
│    Characterization    │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  AFR/SOLT S-Parameter  │
│      De-embedding      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   TDR Step Response    │
│       Impedance        │
│      Verification      │
│                        │
└────────────────────────┘
```

## Step-by-Step Procedure

1. **Instrument Stabilization & Acquisition Setup**:
   - Power on Vector Network Analyzer (VNA) with time-domain reflectometry (TDR) transform option and high-bandwidth sampling head ($t_r \le 20\,\text{ps}$, $V_{\text{step}} = 200\,\text{mV}$).
   - Allow thermal stabilization period of $\ge 60\,\text{minutes}$ in an environmentally controlled metrology room ($22^\circ\text{C} \pm 1^\circ\text{C}$, $45\% \pm 5\%\,\text{RH}$).
   - Set frequency sweep from $10\,\text{MHz}$ to $20.0\,\text{GHz}$ (IF bandwidth = $1\,\text{kHz}$, 4001 points) with time-domain impulse/step window span of $10.0\,\text{ns}$ ($2.5\,\text{ps}$ sampling resolution).

2. **Coaxial Tier-1 Reference Plane Calibration (SOLT)**:
   - Connect precision $3.5\,\text{mm}$ / SMA coaxial mechanical calibration kit standards to Port 1 and Port 2 test cables.
   - Execute full 2-port Short-Open-Load-Thru (SOLT) calibration sequence:
     - Connect Open standard and measure Port 1 & 2 reflection coefficients ($S_{11}, S_{22}$).
     - Connect Short standard and acquire phase response.
     - Connect precision $50.0\,\Omega$ broadband Load standard; verify directivity calibration baseline ($> 42\,\text{dB}$).
     - Connect zero-length Thru (or calibrated phase adapter); measure transmission coefficients ($S_{21}, S_{12}$).
   - Compute systematic 12-term error coefficients to define coaxial reference plane at cable launch faces.

3. **ATE Loadboard Microstrip 2x-Thru Fixture Characterization**:
   - Align and mate coaxial launches to the on-board 2x-Thru reference coupon fabricated on the ATE DUT loadboard panel sharing identical BEOL stackup, dielectric layer thickness, and microstrip geometries.
   - For microstrip pad launches interfacing wafer sort or probe card test coupons, match dimensions with calibrated Transmission Line Measurement (TLM) geometry: rectangular pads with width $W = 100\,\mu\text{m}$, length $L_{\text{pad}} = 50\,\mu\text{m}$.
   - Acquire full 2-port S-parameters ($S_{11}, S_{21}, S_{12}, S_{22}$) of the 2x-Thru microstrip structure over the $10\,\text{MHz}$ to $20\,\text{GHz}$ spectrum.
   - Verify fixture symmetry ($|S_{11} - S_{22}| \le 0.35\,\text{dB}$, $\text{phase difference} \le 1.5^\circ$).

4. **Fixture Bisection & Mathematical De-embedding (AFR / T-Matrix Inversion)**:
   - Bisect the 2x-Thru total electrical length using time-domain gating / Automatic Fixture Removal (AFR) to isolate the single-ended 1x lead-in fixture s-parameter model $[S_{\text{fixture}}]$.
   - Convert scattering parameters to cascade transfer transmission matrices ($[T]$):
     $$[T_{\text{measured}}] = [T_{\text{fixture\_left}}] \cdot [T_{\text{DUT}}] \cdot [T_{\text{fixture\_right}}]$$
   - Apply matrix inversion de-embedding algorithm:
     $$[T_{\text{DUT}}] = [T_{\text{fixture\_left}}]^{-1} \cdot [T_{\text{measured}}] \cdot [T_{\text{fixture\_right}}]^{-1}$$
   - Shift the measurement reference plane directly to the ATE DUT socket microstrip launch interface pads.

5. **TDR Step Response & Characteristic Impedance Verification**:
   - Apply step-response TDR algorithm (chirp Z-transform of de-embedded $S_{11}$ data).
   - Inspect the characteristic impedance profile $Z(t)$ along a known on-board $50.0\,\Omega$ verification microstrip trace coupon.
   - Confirm cancellation of coaxial launch capacitance and SMA/SMP connector discontinuities.

## Acceptance Criteria Target Metrics
- **Mean Characteristic Impedance ($Z_0$)**: $50.0\,\Omega \pm 1.0\,\Omega$ across the uniform microstrip routing length.
- **Max Launch Discontinuity Delta ($\Delta Z_{\text{discontinuity}}$)**: $\le 2.0\,\Omega$ deviation from nominal $50.0\,\Omega$ at the de-embedded interface plane.
- **Fixture Lead-in Insertion Loss ($S_{21}$)**: $\le 1.2\,\text{dB}$ at $10.0\,\text{GHz}$ for single 1x fixture trace segment.
- **Coaxial Calibration Directivity**: $\ge 42.0\,\text{dB}$ across the calibrated bandwidth ($10\,\text{MHz} - 20\,\text{GHz}$).
- **De-embedded Inter-channel Delay Skew**: $\le 1.8\,\text{ps}$ between matched differential / bitline test channels.

## Verified Literature & Technical Context Citations
1. **Transmission Line Measurement (TLM) for Specific Contact Resistivity**:
   - Rectangular contact pad dimensions $W = 100\,\mu\text{m}$, length $L_{\text{pad}} = 50\,\mu\text{m}$, progressive pad gaps $d = 5\,\mu\text{m}, 10\,\mu\text{m}, 20\,\mu\text{m}, 40\,\mu\text{m}, 80\,\mu\text{m}$.
   - Linear relationship $R_T = 2 \cdot R_c + (R_s / W) \cdot d$, yielding diffusion sheet resistance $R_s$, contact resistance $R_c$, and specific contact resistivity $\rho_c = R_c \cdot W \cdot L_T = R_s \cdot L_T^2\,[\Omega\cdot\text{cm}^2]$.
2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry $L = 180\,\text{nm}$, $W = 220\,\text{nm}$ in $8F^2 / 6F^2$ folded bitline layout with capacitor over bitline (COB) architecture.
   - Dielectric constant $\kappa > 15$, minimum storage node capacitance budget of $28\,\text{fF}$ per cell, and sub-1 fA leakage requirement at $85^\circ\text{C}$ to maintain required JEDEC refresh intervals.
3. **Stage 3 Reality Gate: Discrete Long-Channel MOSFET & CMOS Inverter Verification**:
   - Discrete transistor test structures ($W/L = 20\,\mu\text{m} / 5\,\mu\text{m}$, $10\,\mu\text{m} / 1.0\,\mu\text{m}$, and target $2.0\,\mu\text{m} / 0.18\,\mu\text{m}$).
   - Parameter extraction baseline: $V_{\text{thn}} = +0.55\,\text{V} \pm 50\,\text{mV}$ (NMOS), $V_{\text{thp}} = -0.60\,\text{V} \pm 50\,\text{mV}$ (PMOS), $I_{\text{on}} \ge 500\,\mu\text{A}/\mu\text{m}$ at $V_{\text{GS}} = 1.8\,\text{V}$, $I_{\text{off}} \le 10\,\text{pA}/\mu\text{m}$ at $V_{\text{GS}} = 0\,\text{V}$, and $I_{\text{on}}/I_{\text{off}} > 10^7$.

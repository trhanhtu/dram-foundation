# Pre-Clean Sputter Etch and Forming Gas Sintering Thermal Recalibration Disposition

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
In 180nm open-source DRAM BEOL metallization, electrical contact resistance between aluminum interconnect lines (Metal-1) and active silicon/polysilicon or tungsten plugs directly controls wordline/bitline RC delay and sensing margins. When PCM TLM monitors detect specific contact resistivity $\rho_c > 1.0 \times 10^{-5}\ \Omega\cdot\text{cm}^2$, a hardware recalibration disposition protocol is triggered across both the pre-metallization interfacial cleaning stages (dilute HF wet etch and vacuum in-situ Ar sputter etch) and the post-metallization forming gas sintering anneal.

## Key Details / Architecture
1. **Trigger Condition**:
   - $\rho_c > 1.0 \times 10^{-5}\ \Omega\cdot\text{cm}^2$ triggers mandatory line hold and calibration.
2. **Pre-Clean Sputter Etch Recalibration**:
   - PVD vacuum base pressure: $< 2 \times 10^{-6}\ \text{Torr}$.
   - In-situ Argon plasma gas purity: 99.999% (5N) Ar.
   - Sputter working pressure: $3\text{ to }5\ \text{mTorr}$.
3. **PVD Metallization**:
   - Target: 99.999% (5N) pure Aluminum or Al-0.5% Cu.
   - DC magnetron power: $1.5\text{ to }3.0\ \text{kW}$.
   - Deposition rate: $50\text{ to }100\ \text{nm/min}$.
   - Target thickness (Metal-1): $350\ \text{nm} \pm 5\%$.
4. **Forming Gas Sintering Recalibration**:
   - Ambient: $\text{N}_2/\text{H}_2\ (95/5\%)$ forming gas.
   - Furnace temperature: $400^\circ\text{C}$.
   - Soak duration: $30\ \text{minutes}$.
5. **Acceptance Criteria**:
   - Contact Resistance ($R_c$): $< 10\ \Omega/\text{contact}$.
   - Specific Contact Resistivity ($\rho_c$): $\le 1.0 \times 10^{-6}\ \Omega\cdot\text{cm}^2$.
   - Sheet Resistance ($R_s$): $< 0.08\ \Omega/\Box$ ($80\ \text{m}\Omega/\Box$).
   - Metal-1 Thickness: $350\ \text{nm} \pm 5\%$ ($332.5\text{--}367.5\ \text{nm}$).

## References & Related Files
- [docs/knowledge/sop_preclean_sintering_recalibration.md](./docs/knowledge/sop_preclean_sintering_recalibration.md)

# SOP: Distributed RC Poly/Metal Wordline Transmission Line Modeling & Extraction

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Proposed
- **Generation**: Gen 2 (µm / 180nm Open-Source DRAM Chip)
- **Subsystem**: Address Decoders & Wordline VPP Voltage Pump > Hierarchical Row/Column Address Predecoder & Wordline Driver Sizing > Distributed RC Wordline Slew Rate & Activation Delay Transient Metrology > Distributed RC Poly/Metal Wordline Transmission Line Modeling & Extraction

## Overview & Rationale
In high-density 180nm DRAM architectures (employing $8F^2$ or $6F^2$ folded-bitline stacked capacitor cells), wordlines traverse thousands of access transistors across the memory sub-array. The wordline pitch is tightly constrained to approximately $360\,\text{nm}$ to $400\,\text{nm}$, with access transistor dimensions $L = 180\,\text{nm}$ and $W = 220\,\text{nm}$, and a gate oxide thickness of $\sim 3.5\,\text{nm}$. Due to non-negligible sheet resistance in the polysilicon gate layer and coupling capacitances (gate-to-channel, gate-to-source/drain, and inter-line metal/poly coupling), wordline propagation experiences significant RC delay, edge degradation, and voltage attenuation. To ensure uniform turn-on times and charge transfer across all storage capacitors ($25\,\text{fF} - 30\,\text{fF}$), distributed multi-segment $\Pi$ / T transmission line RC extraction and hierarchical strapping modeling are required.

## Architectural Flow
```text
┌────────────────────────────────────────────────────────┐
│ 180nm Physical Sub-Array Wordline Layout Geometry      │
│ (Pitch: 360 nm - 400 nm, Poly L=180 nm, W=220 nm)     │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Distributed 3D Parasitic Extraction (Field Solver/LPE) │
│ - Poly Sheet & Metal Strapping Interconnect R          │
│ - Gate Oxide Cox (~3.5 nm tox), Overlap & Coupling C   │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Multi-Segment Distributed RC Transmission Line Model   │
│ - Lumped-to-Distributed N-stage Pi/T Equivalent Mesh   │
│ - Metal-Strap to Poly Contact Tap Shunt Network       │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ Transient Wordline Delay & Slew Rate Verification      │
│ - Dynamic Driver Loading & VPP Pulse Propagation       │
│ - Far-End Rise Time & Bitline Delta V Margin Audit     │
└────────────────────────────────────────────────────────┘
```

## Step-by-Step SOP Procedure
1. **Physical Layout Parameter & Layer Deck Configuration**:
   - Import the 180nm sub-array GDSII/OASIS layout containing polysilicon wordline tracks, metal strapping layers (Metal 1/2), and wordline contact tap pitch.
   - Establish physical technology constants: wordline/bitline pitch at $360\,\text{nm} - 400\,\text{nm}$, access transistor channel length $L = 180\,\text{nm}$, access transistor channel width $W = 220\,\text{nm}$, and thermal $\text{SiO}_2$ gate dielectric physical thickness of $3.5\,\text{nm}$ (dry oxidation at $850^\circ\text{C} - 900^\circ\text{C}$).
2. **Parasitic Resistance & Capacitance Layerwise Extraction**:
   - Extract unit-length resistance ($R_{\text{poly}}$) along the wordline track, including contact/via resistance at metal strapping intervals.
   - Extract distributed capacitances per cell: access transistor oxide capacitance ($C_{\text{ox}} = \frac{\varepsilon_{\text{ox}} \cdot W \cdot L}{t_{\text{ox}}}$), gate-to-diffusion overlap capacitance ($C_{\text{ov}}$), and lateral coupling capacitance ($C_{\text{adj}}$) to adjacent wordlines across the $360\,\text{nm} - 400\,\text{nm}$ pitch.
3. **Distributed Transmission Line Network Discretization**:
   - Discretize the continuous wordline into an $N$-stage ladder network (distributed $\Pi$ or T-sections) corresponding to cell units and metal strap stitch points.
   - Incorporate active channel loading effects reflecting the unselected state (accumulation/depletion) and selected state (inversion) when wordlines are driven to $V_{PP}$.
4. **Driver-to-Array Synthesis & Transient SPICE Simulation**:
   - Stitch the extracted distributed RC sub-circuit to the hierarchical wordline driver/level shifter stage.
   - Simulate transient step and ramp responses under nominal and worst-case operating conditions ($85^\circ\text{C}$, nominal $V_{PP}$).
   - Measure near-end versus far-end wordline propagation delay, slew rate (10% to 90% rise time), and peak signal voltage drop along the entire row.
5. **Charge Transfer & Readout Validation**:
   - Couple the far-end wordline node to representative 1T1C storage nodes with cell capacitance $C_s = 25\,\text{fF} - 30\,\text{fF}$ (minimum $28\,\text{fF}$) and bitline capacitance $C_{BL} = 250\,\text{fF}$.
   - Confirm complete access transistor activation without premature cutoff to guarantee differential signal development $\Delta V = 100\,\text{mV} - 150\,\text{mV}$ across the folded bitline sense amplifier.

## Acceptance Criteria Targets
1. **Transistor & Layout Geometry Conformance**: Wordline gate length $L = 180\,\text{nm}$, active width $W = 220\,\text{nm}$, and wordline/bitline array pitch maintained strictly within $360\,\text{nm}$ to $400\,\text{nm}$.
2. **Gate Oxide Physical Thickness**: Thermally grown gate dielectric thickness target of $3.5\,\text{nm}$ $\text{SiO}_2$ (fabricated via dry oxidation at $850^\circ\text{C} - 900^\circ\text{C}$).
3. **Storage Cell Capacitance Coupling Integrity**: Storage capacitor load per cell $C_s \ge 28\,\text{fF}$ (design nominal window: $25\,\text{fF}$ to $30\,\text{fF}$ per cell) to ensure retention time $> 64\,\text{ms}$ at $85^\circ\text{C}$.
4. **Signal Development Margin under Far-End Activation**: Extracted wordline delay must deliver sufficient gate overdrive to yield folded bitline readout differential voltage $\Delta V$ between $100\,\text{mV}$ and $150\,\text{mV}$ with nominal $C_{BL} = 250\,\text{fF}$.

## References & Literature Sources
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry ($L = 180\,\text{nm}$, $W = 220\,\text{nm}$), minimum capacitance budget $\ge 28\,\text{fF/cell}$, leakage target $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$.
- **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**: 1T1C $8F^2 / 6F^2$ cell layout, cell capacitance $25\,\text{fF} - 30\,\text{fF}$ ($> 64\,\text{ms}$ retention at $85^\circ\text{C}$), wordline and bitline pitch $360\,\text{nm} - 400\,\text{nm}$, gate dielectric physical thickness $\sim 3.5\,\text{nm}$ $\text{SiO}_2$ ($850^\circ\text{C} - 900^\circ\text{C}$ dry oxidation).
- **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**: Signal development $\Delta V = \frac{C_s}{C_{BL} + C_s} \cdot (V_{\text{cell}} - V_{DD}/2)$, nominal $C_s = 25\,\text{fF}$, $C_{BL} = 250\,\text{fF}$, target differential voltage $\Delta V = 100\,\text{mV} - 150\,\text{mV}$.

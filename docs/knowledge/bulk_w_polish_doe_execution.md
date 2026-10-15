# High-Removal Rate Bulk W Polish DOE Factorial Execution

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented

## Overview & Rationale
Standard Operating Procedure (SOP) covering the execution of a high-removal rate bulk tungsten (W) chemical mechanical planarization (CMP) factorial DOE. It addresses tungsten overburden removal above contact plugs (access transistor contact geometry $L = 180\text{ nm}$, $W = 220\text{ nm}$), selective endpoint transition on the TiN liner barrier, and post-CMP particle/slurry removal via RCA SC-1 alkaline oxidation and cascade rinsing.

## Key Details / Architecture
- **Stage 1: Platen Prep & Conditioning**: Ex-situ/in-situ diamond disk conditioning on hard polyurethane pad.
- **Stage 2: Bulk Polish DOE Execution**: Multi-factor factorial evaluation (downforce, platen/carrier rpm, slurry delivery rate).
- **Stage 3: Optical/Eddy-Current Endpoint Transition**: Optical motor current / reflectance detection when crossing the bulk W to TiN liner interface.
- **Stage 4: Post-CMP SC-1 Clean & Cascade Dump Rinse**: SC-1 chemistry (5:1:1 $\text{UPW}:\text{NH}_4\text{OH}:\text{H}_2\text{O}_2$) at $70^\circ\text{C}$ to $75^\circ\text{C}$ with $1\text{ MHz}$ megasonic agitation, followed by cascade dump rinse until $> 16\text{ M}\Omega\cdot\text{cm}$.
- **Stage 5: Metrology**: Sheet resistance $R_s$, contact plug recess, and defectivity.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

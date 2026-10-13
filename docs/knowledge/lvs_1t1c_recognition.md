# LVS Rule Deck Setup and 1T1C Primitive Device Recognition Definition

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI)
- **Status**: Implemented

## Overview & Rationale
Defines the Layout Versus Schematic (LVS) rule deck extraction and primitive device recognition methodology for an open-source 180nm 1T1C DRAM array cell (Gen 2 µm technology roadmap). It addresses electrical extraction of sub-micron access NMOS transistors, stacked crown/cylinder MIM capacitors ($C_s$), and bitline/wordline terminal mapping against SPICE netlists.

## Key Details & Architecture
- **Layer Derivation**: Active/Diffusion, Polysilicon (Wordline), Metal 1 (Bitline), Storage Node Contact (SN-via/W-plug), and High-k Capacitor Top Plate (`PLATE`).
- **Primitive Recognition**:
  - `MN_1T1C`: Access NMOS with gate length $L = 180\text{ nm}$, gate width $W = 220\text{ nm}$, gate oxide $t_{ox} \approx 3.5\text{ nm}$.
  - `CAP_1T1C`: Stacked storage capacitor with nominal capacitance $C_s \ge 25\text{ fF}$ (target $28\text{ fF} - 30\text{ fF}$) with ONO/high-k dielectric ($\kappa > 15$).
- **Pin & Connectivity Validation**: Wordline (WL), Bitline (BL), Common Cell Plate ($V_{plate} = V_{DD}/2$), Substrate bulk connection ($V_{BB} \approx -0.5\text{V}$ to $-1.0\text{V}$).

## References & Related Files
- [docs/context.yaml](../context.yaml)
- Verified Local Literature Context: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*, *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*, *Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout*.

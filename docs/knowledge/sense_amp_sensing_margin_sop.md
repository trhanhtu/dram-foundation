# Sense Amplifier Sensing Margin, Latch Delay & Monte Carlo Mismatch Verification

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
Defines the standard operating procedure for verifying the sensing margin, regenerative latching speed, and transistor mismatch immunity under Monte Carlo analysis for a folded-bitline CMOS sense amplifier at the 180nm DRAM node.

## Key Details / Architecture
- **Precharge & Equalization**: Bitlines initialized to $V_{DD} / 2$ prior to wordline activation.
- **Differential Signal Development**: Differential voltage $\Delta V = \left(\frac{C_s}{C_{BL} + C_s}\right) \cdot \left(V_{cell} - \frac{V_{DD}}{2}\right)$, targeting $100\text{ mV}$ to $150\text{ mV}$ with $C_s = 25\text{ fF}$ (min $28\text{ fF}$) and $C_{BL} = 250\text{ fF}$.
- **Strobe & Regeneration**: Sense amplifier latching sequence activating SAN (pulling toward GND) followed by SAP (pulling toward $V_{DD}$), driving bitlines to full rail CMOS levels ($0\text{ V}$ and $V_{DD}$) and completing cell refresh.
- **Layout & Mismatch Verification**: Pitch matched to $360\text{ nm}$ bitline pitch using interleaved layouts; statistical Monte Carlo mismatch verification across threshold voltage ($V_{th}$) and aspect ratio ($W/L$) variations.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)

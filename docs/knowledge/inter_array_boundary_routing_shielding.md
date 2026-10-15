# Inter-Array Boundary Routing & VSS/VDD Ground Plane Shielding Implementation

- **Date**: 2026-10-13
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented

## Overview & Rationale
In high-density 180nm open-source DRAM architecture (Gen 2 µm regime), transitioning between dense memory sub-arrays and peripheral Folded Bitline CMOS Sense Amplifier/Equalizer blocks creates sharp parasitic discontinuities. Signal bitlines carry low differential read voltages ($\Delta V \approx 100\text{--}150\text{ mV}$ from stored $C_s \ge 25\text{--}28\text{ fF}$ against $C_{BL} \approx 250\text{ fF}$). Without dedicated boundary routing and co-axial ground/supply ($V_{SS}/V_{DD}$) shielding, fringe capacitance and substrate injection from adjacent sub-arrays severely degrade the sense margin and cause soft-error latching failures.

## Key Details & SOP Summary
- Pitch matched transition maintaining array bitline/wordline pitch (360 nm to 400 nm).
- Well-tap and substrate guard rings inserted at array margins to eliminate substrate injection.
- Metal-2/Metal-3 ground ($V_{SS}$) and supply ($V_{DD}$) shielding meshed around sensitive differential pairs ($BL / \overline{BL}$).
- Parasitic RC extraction validation confirming $C_{BL} \le 250\text{ fF}$ and $\Delta V \ge 100\text{ mV}$.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)
- [docs/context3.yaml](.../../context3.yaml)

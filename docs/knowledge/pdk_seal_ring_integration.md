# SOP: PDK Standard Seal Ring Boundary Integration and Guard Ring Stitching

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Accepted
- **Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) > Packaging & MPW Shuttle Tapeout

## Overview & Rationale
During wafer sawing (dicing) and die separation, micro-cracks, mechanical shear stresses, ionic contamination, and moisture can propagate laterally into active circuit regions. The seal ring forms an impenetrable mechanical and chemical perimeter around the die boundary. Complementary inner substrate/well guard rings isolate substrate minority-carrier noise induced by high-frequency peripheral pad drivers and protect memory array access transistors.

## Key Technical Parameters & Stack Topology
- **Bonding Pad Geometry**: $100\ \mu\text{m} \times 100\ \mu\text{m}$ aluminum square landing zones.
- **Access Transistor Channel Geometry**: $L = 180\ \text{nm}$, $W = 220\ \text{nm}$.
- **Array Interconnect Pitch**: Bitline and wordline pitch between $360\ \text{nm}$ and $400\ \text{nm}$.
- **Dielectric & Thermal Constraints**: Gate dielectric dry thermal $\text{SiO}_2 \sim 3.5\ \text{nm}$ grown at $850^\circ\text{C}\text{--}900^\circ\text{C}$; epoxy cure budget $150^\circ\text{C}$ for $60\ \text{min}$.
- **Assembly Quality Targets**: Pull test force $\ge 4.0\ \text{gf}$ (Mil-Std-883 Method 2011), die-attach acoustic void area $< 5\%$, thermal resistance $R_{th} \le 5^\circ\text{C/W}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

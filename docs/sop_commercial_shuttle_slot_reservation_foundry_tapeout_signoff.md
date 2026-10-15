# SOP: Commercial Shuttle Slot Reservation & Foundry Tapeout Sign-Off Package Submission

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN Multi-Agent Council)
- **Status**: Proposed
- **Action Type**: Make
- **Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > 180nm CMOS Commercial MPW Tapeout & PDK Implementation [Foundry Tapeout & PDK] > Multi-Project Wafer (MPW) Shuttle GDSII Tapeout Package & Foundry Sign-Off [Foundry Tapeout & PDK] > Commercial Shuttle Slot Reservation & Foundry Tapeout Sign-Off Package Submission [Packaging]

## Overview & Rationale
This Standard Operating Procedure (SOP) defines the protocol for commercial Multi-Project Wafer (MPW) shuttle slot reservation, final physical verification sign-off, and tapeout package delivery for the 180nm open-source 1T1C DRAM test chip. It integrates physical design constraints (8F² and 6F² topologies, crown/MIM capacitor modules, folded bitline pitches) with foundry tapeout deliverables (GDSII/OASIS stream, DRC/LVS decks, dummy metal fill, packaging bondpad definitions).

## Step-by-Step Procedure

1. **Foundry MPW Shuttle Slot Reservation & Design Rule Alignment**:
   - Secure and lock an allocated MPW shuttle run slot with the target 180nm commercial foundry/broker.
   - Verify design rule compatibility with process add-ons: standard 180nm CMOS logic baseline augmented with the Crown/Cylinder stacked capacitor module (or high-density MIM capacitor option) and W-plug contact integration.
   - Obtain official foundry sign-off decks: Golden DRC (Design Rule Check), LVS (Layout Versus Schematic), Antenna, and Density check rule files.

2. **DRAM Array Physical DRC & LVS Clean Sign-Off**:
   - **Cell & Pitch Verification**: Validate unit cell dimensions in the folded bitline matrix ($L = 180\text{ nm}$, $W = 220\text{ nm}$, bitline/wordline pitch between $360\text{ nm}$ and $400\text{ nm}$, cell area $= 0.259\ \mu\text{m}^2$ for $8F^2$, or $0.194\ \mu\text{m}^2$ for $6F^2$). Shared bitline contacts between adjacent cells must strictly comply with W-plug enclosure rules.
   - **Storage Capacitor Integration**: Verify crown/cylinder stacked capacitor layout above the bitline (COB). Confirm dielectric layer definition (ONO or $\text{Ta}_2\text{O}_5 / \text{Al}_2\text{O}_3$ high-k stack with $\text{EOT} = 3\text{ nm to } 4\text{ nm}$, $\kappa > 15$).
   - **LVS Device Extraction**: Run hierarchical LVS verifying exact 1T1C equivalence. Confirm extracted cell storage capacitance $C_s \ge 25\text{ fF to } 30\text{ fF}$ (nominally $28\text{ fF}$) and bitline parasitic capacitance $C_b$ within $150\text{ fF to } 250\text{ fF}$ across blocks of 256 or 512 cells per bitline, satisfying capacitance ratio $C_b / C_s \le 9:1$.

3. **Dummy Metal Fill, Seal Ring & Density Correction**:
   - Run foundry dummy metal fill scripts across metal layers to satisfy layer density thresholds (typically 30% to 70% metal density) while applying strict fill-exclusion keep-out zones around sensitive DRAM analog sense amplifier arrays and folded bitline pairs.
   - Instantiate the foundry-approved die seal ring, corner stress relief structures, and scribe-line alignment/vernier marks around the allocated MPW die boundary.

4. **I/O Pad Ring, Packaging & Bonding Rules Verification**:
   - Place wirebond pads with required minimum pitch and passivation opening size according to the selected package assembly house (e.g., QFP/QFN test package).
   - Ensure clean electrostatic discharge (ESD) clamp placement on all external $V_{DD}$, $V_{PP}$ overdrive ($2.6\text{ V}$ to $2.8\text{ V}$), reference voltage, and clock/control pins.
   - Generate package bond wire bonding diagram and pinout netlist cross-referenced with package cavity dimensions.

5. **GDSII/OASIS Package Generation, Checksum & Foundry Submission**:
   - Stream out the finalized, hierarchy-flattened or cell-preserved GDSII / OASIS layout database.
   - Compute SHA-256 and MD5 cryptographic checksums for all archive files.
   - Complete the Foundry Tapeout Form (specifying process flavor, top metal thickness, passivation type, and wafer split conditions).
   - Upload the sign-off package via secure foundry SFTP / portal prior to the hard shuttle cutoff deadline.

## Machine-Measurable Acceptance Criteria

1. **Storage Node Capacitance & Dielectric Integrity ($C_s$, EOT)**:
   - Target: $C_s \ge 25\text{ fF/cell}$ (Nominal $28\text{ fF/cell}$, minimum range $25\text{ fF to } 30\text{ fF}$) with equivalent oxide thickness $\text{EOT} = 3\text{ nm to } 4\text{ nm}$ ($\kappa > 15$), sustaining cell leakage $I_{leak} \le 1.0\text{ fA/cell}$ and retention time $> 64\text{ ms}$ at $85^\circ\text{C}$.
2. **Bitline-to-Cell Parasitic Capacitance Ratio ($C_b / C_s$)**:
   - Target: $5:1 \le C_b / C_s \le 9:1$ (for $C_b = 150\text{ fF to } 250\text{ fF}$ per 256/512-cell array block), strictly maintaining $C_b / C_s < 10:1$ to prevent read margin degradation.
3. **Array Pitch & Lithographic Feature Dimensions**:
   - Target: Access NMOS channel length $L = 180\text{ nm}$, channel width $W = 220\text{ nm}$, gate dielectric physical thickness $\sim 3.5\text{ nm}$ (dry oxidation at $850^\circ\text{C}-900^\circ\text{C}$), with bitline and wordline pitch within $360\text{ nm to } 400\text{ nm}$.
4. **Physical Verification Zero-Violation Sign-Off (DRC/LVS/Antenna)**:
   - Target: $0$ DRC errors, $0$ LVS mismatches, $0$ antenna violations across full die GDSII database, with verified SHA-256 checksum matching the upload manifest.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- Source: *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*
- Source: *1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets*
- Source: *Legacy 180nm DRAM Architecture & Cell Capacitor Engineering*

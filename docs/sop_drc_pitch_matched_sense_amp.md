# SOP: DRC Rule Deck Execution & Pitch-Matched Sense Amplifier Geometry Clean-up

- **Date**: 2026-10-13
- **Author**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Chip
- **Discipline**: Metrology / Circuit Design Verification

## Overview & Rationale
In high-density 180nm folded-bitline DRAM architectures, the differential CMOS sense amplifier (SA) and equalization circuitry must interface directly with tightly packed 1T1C memory array columns. Bitline spacing dictates an exact pitch-matching constraint of 360 nm. Because a complete CMOS cross-coupled inverter pair (pull-down NMOS `SAN` and pull-up PMOS `SAP`) cannot fit comfortably within a single 360 nm horizontal slice without introducing severe DRC design rule violations, the SA layout is partitioned across an interleaved topology.

Executing hierarchical Design Rule Check (DRC) rule decks and systematically cleaning up pitch-matched geometry guarantees physical tape-out readiness, zero lithographic bridging/necking, and symmetric balanced parasitics between complementary lines `BL` and `/BL`.

---

## 1. Step-by-Step SOP Procedure

### Step 1: Environment & Rule Deck Initialization
1. Ingest the final GDSII/OASIS layout containing the folded-bitline array core, equalization networks, and interleaved CMOS sense amplifier banks.
2. Load the official 180nm foundry open-source physical design rule deck (e.g., covering Diffusion, Poly-Si, Contact/Via, and Metal 1–3 layers).
3. Set the hierarchical DRC engine to isolate boundary cell overlaps, cell abutment borders, and array-to-periphery pitch transitions.

### Step 2: Pitch-Matched SA Strip & Boundary Checking
1. Verify the sense amplifier pitch against the memory array bitline pitch: ensure the cell repeat unit pitch strictly matches **360 nm**.
2. Isolate interleaved sense amplifier unit strips and verify staggering: alternating sense amplifier columns must step out every $2\times$ or $4\times$ array pitch to satisfy lateral transistor spacing rules.
3. Check access transistor channel regions interfacing the bitline taps ($L = 180\text{ nm}$, $W = 220\text{ nm}$) to confirm zero boundary contact overhang or active enclosure infractions.

### Step 3: Rule Deck Execution & Error Classification
1. Execute the full DRC rule deck across the macro boundary.
2. Parse the DRC output database into standard categories:
   - **Minimum Spacing / Width Violations**: Metal 1 bitline rails, diffusion tabs, and poly gates.
   - **Enclosure / Extension Rules**: Contact-to-poly endcaps and via1-to-metal overlap.
   - **Antenna & Density DRC Rules**: Poly/metal layer area-to-gate ratio violations along extended `BL` and `/BL` tracks.

### Step 4: Geometry Clean-up & Differential Symmetry Preservation
1. Perform geometric polygon push/pull corrections within layout editors (e.g., KLayout / Magic):
   - Widen sub-design-rule necking segments while preserving identical track lengths for `BL` and `/BL`.
   - Maintain strict differential layout symmetry across the cross-coupled inverter nodes to prevent sensing offset voltages.
2. Route equalization and precharge transistors ($V_{DD}/2$ generators) with centered balanced source/drain taps.
3. Re-run incremental DRC checks until **0 violations** remain in the core and pitch-matched interface regions.

### Step 5: Clean Layout Freezing & Metrology Sign-Off
1. Verify hierarchical GDSII export checksums.
2. Tag the layout revision as `DRC_CLEAN_REV` and advance the database to Parasitic RC Extraction (PEX) and Layout Versus Schematic (LVS) verification.

---

## 2. Machine-Measurable Acceptance Criteria Target Metrics

| Parameter / Metric | Target Value | Tolerance / Condition | Units | Verification Tool / Method |
| :--- | :--- | :--- | :--- | :--- |
| **Array Bitline Pitch-Match** | `360` | $\pm 0.0$ (Exact Grid Match) | `nm` | Automated Hierarchical DRC Pitch Measurement |
| **Sense Amp Pitch DRC Violations** | `0` | Absolute Zero | `count` | Open-Source 180nm DRC Rule Deck Log |
| **Access Transistor Channel Length ($L$)** | `180` | $\pm 0.0$ (Drawn Layout Target) | `nm` | DRC Gate Width/Length Deck Assertion |
| **Access Transistor Channel Width ($W$)** | `220` | $\pm 0.0$ (Drawn Active Target) | `nm` | DRC Active OD Metric Assertion |
| **Minimum Cell Capacitance ($C_s$) Budget** | $\ge 28$ | Baseline soft-error budget | `fF` | Post-Layout PEX Metric Verification |

---

## 3. Verified Context Citations
1. **Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout**:
   - *Sense amplifier architecture and equalization*: CMOS cross-coupled inverter latch between `BL` and `/BL`; precharged to $V_{DD}/2$ prior to wordline activation.
   - *Pitch matching target*: *"Sense amplifier pitch must match memory array bitline pitch (360 nm in 180nm node), requiring interleaved layout."*
   - *Latching signals*: SAN pulls to GND, SAP pulls to $V_{DD}$.
   - *Capacitance model*: Typical $C_s = 25\text{ fF}$, $C_{BL} = 250\text{ fF}$, developing $\Delta V \approx 100\text{ mV}$ to $150\text{ mV}$.
2. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - *Unit cell geometry*: Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
   - *Capacitance budget*: Minimum $28\text{ fF}$ per cell for noise immunity against alpha-particle soft errors and bitline coupling capacitance.
   - *Leakage target*: Sub-threshold and junction leakage $< 1\text{ fA/cell}$ at 85°C.

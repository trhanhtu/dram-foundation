# SOP: DRC Rule Deck Execution & Pitch-Matched Sense Amplifier Geometry Clean-up

- **Date**: 2026-10-12
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 2 (µm) / 180nm Open-Source DRAM Node
- **Module**: Metrology & Physical Verification

## 1. Scope & Objective
Establish the physical verification and layout clean-up methodology for the CMOS Folded Bitline Sense Amplifier and Equalizer strip, enforcing strict pitch alignment to the memory array bitlines (360 nm pitch) and eliminating DRC design rule errors (spacing, enclosure, overlap, and antenna constraints).

---

## 2. Process Flow Diagram

```text
┌────────────────────────┐
│                        │
│     GDS Ingestion      │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│   DRC Deck Execution   │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│     Pitch Mismatch     │
│        Flagged         │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Interleaved Geometry  │
│        Clean-up        │
│                        │
└────────────┬───────────┘
             │
             │
             ▼
┌────────────────────────┐
│                        │
│  Final Sign-off DRC 0  │
│       Violations       │
│                        │
└────────────────────────┘
```

---

## 3. Step-by-Step Operating Procedure

1. **Database & Rule Deck Initialization**:
   - Ingest GDSII/OASIS layout containing the folded bitline memory cell array, equalizer network, and cross-coupled CMOS latch (SAN/SAP drivers).
   - Load the certified open-source 180nm foundry physical DRC deck.
2. **Pitch Alignment & Boundary Constraint Validation**:
   - Check array-to-periphery pitch matching along the column boundary. Flag pitch mismatches deviating from the 360 nm memory array bitline pitch.
   - Verify access transistor boundary dimensions (channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$) leading into bitline contact regions.
3. **Execution of Full DRC Rule Deck**:
   - Run batch DRC covering active diffusion (OD/RX), polysilicon gate (PO/PC), contact plugs (W-plug), metal layers (M1/M2/M3), and capacitor vias.
   - Filter errors by coordinate cluster; isolate layout violations inside the sense amplifier pitch-matching interface.
4. **Interleaved Geometry Clean-Up**:
   - Restructure cross-coupled PMOS/NMOS sensing pairs into an interleaved multi-row layout architecture to accommodate wide/tall devices within the narrow column pitch.
   - Adjust metal routing jogs, poly extensions, and contact enclosures to satisfy minimum enclosure and end-of-line spacing rules.
5. **Parasitic Consistency Cross-Check**:
   - Confirm layout changes do not compromise nominal parasitic budgets required for charge sharing: target cell storage capacitance $C_s \ge 25\text{ fF}$ (nominal min $28\text{ fF}$) versus bitline parasitic capacitance $C_{BL} \approx 250\text{ fF}$, ensuring differential voltage $\Delta V$ develops between $100\text{ mV}$ and $150\text{ mV}$.
6. **Final Zero-Violation Sign-Off**:
   - Rerun full-chip and modular DRC rule deck. Verify 0 errors, 0 warnings, and archive sign-off GDS with verification hash.

---

## 4. Acceptance Criteria & Target Metrics

| Parameter / Metric | Target Value | Physical Unit | Verification Method |
|---|---|---|---|
| **Bitline Pitch Matching** | **360** | **nm** | Layout Geometric Ruler / DRC Coordinate Check |
| **Access Transistor Channel Length ($L$)** | **180** | **nm** | DRC Gate CD Measurement |
| **Access Transistor Channel Width ($W$)** | **220** | **nm** | DRC Active Diffusion Width Measurement |
| **Minimum Unit Cell Storage Capacitance ($C_s$)** | **25 to 28** | **fF** | Physical Extraction (PEX) / C-V Profiling |
| **Bitline Parasitic Capacitance ($C_{BL}$)** | **250** | **fF** | Post-layout PEX Extraction |
| **Differential Signal Window ($\Delta V$)** | **100 to 150** | **mV** | Post-Layout Transient Readout Simulation |
| **Sign-Off Clean DRC Violations** | **0** | **Count** | Batch DRC Rule Deck Sign-Off Report |

---

## 5. Literature Citations & References
- *Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout*:
  - Specifies CMOS cross-coupled inverter latch, SAN/SAP latching, equalization network, differential signal $\Delta V = 100\text{ mV} - 150\text{ mV}$, $C_s = 25\text{ fF}$, $C_{BL} = 250\text{ fF}$, and 360 nm bitline pitch requirement requiring interleaved layout.
- *180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench*:
  - Defines 180nm unit cell geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$), stacked capacitor over bitline (COB) with W-plug, and minimum capacitance budget of $28\text{ fF}$.

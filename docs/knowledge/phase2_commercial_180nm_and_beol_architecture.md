# Phase 2 Architecture: Commercial 180nm Tapeout, BEOL Packaging & High-Speed FPGA Validation

- **Date**: 2026-10-15
- **Source**: User & Agent Collaborative Design
- **Status**: Implemented

## Overview & Rationale
Phase 1 established 100% empirical grounding and 360° enrichment (Council Critics, Acceptance Test Cases, EHS Hazmat & CAS specifications, Queue-Time constraints, and Completion Assertions / DoD) across 1,003 foundational WBS nodes.

Phase 2 scales the Work Breakdown Structure toward 2,000+ nodes and bridges the gap between university/lab-scale silicon prototyping (Gen 1 mm / Gen 2 µm) and commercial industrial production (Gen 3 nm). This roadmap expansion incorporates:
1. **Commercial Open-Source 180nm CMOS PDK & MPW Shuttle Tapeout**: Rule decks for DRC, LVS, ERC, antenna ratio checking, 3D crown capacitor atomic layer deposition (ALD), optical proximity correction (OPC) reticle masks, electron beam direct write (EBDW), and chemical mechanical planarization (CMP).
2. **Back End of Line (BEOL) Interconnect, Wafer Sort & Packaging**: Dual-damascene copper / tungsten plug metallization, Electrical Die Sort (EDS) with micro-cantilever probe cards, high-speed wafer backgrinding and dicing, thermosonic gold/copper ball wirebonding, epoxy mold transfer encapsulation (TSOP-54 / FBGA-60), and final Automated Test Equipment (ATE) JEDEC DDR speed-binning with HTOL burn-in.
3. **High-Speed FPGA Memory Controller & Validation Hardware**: Synthesizable Verilog DDR PHY state machines, 50-ohm controlled-impedance daughtercard PCBs, automated March C- retention fault test firmware, and real-time VDD vs retention time Shmoo telemetry engines.

## Key Details / Architecture

### 1. New Engineering Modules
- **`data/modules/07_commercial_180nm_tapeout.json`** (`TAPEOUT-07`, 🏭):
  - Encompasses full physical verification golden rule decks (KLayout / Magic / Pegasus).
  - 3D Crown Capacitor ALD high-k dielectric stack (ZrO2/Al2O3/ZrO2 - ZAZ) targeting EOT <= 0.8 nm and leakage < 1.0 fA/cell.
  - Multi-Project Wafer (MPW) shuttle intake submission sign-off.
- **`data/modules/08_beol_interconnect_packaging.json`** (`BEOL-08`, 📦):
  - Multi-layer metal routing (M1, M2, Passivation).
  - EDS cold/hot wafer probe testing with March C- fault mapping.
  - Thermosonic ball bonding (shear force >= 18.0 gf) and TSOP-54 / FBGA-60 encapsulation.
  - Final ATE JEDEC qualification, timing vector generation, and HTOL 125°C 1000h burn-in.
- **`data/modules/01_mcu_cots.json`** (`MCU-01`, ⚙️ Expansion):
  - Refined from passive COTS procurement into active engineering tasks: FPGA DDR PHY RTL core, 50-ohm test daughtercard PCB, March C- firmware, and Shmoo telemetry.

### 2. Multi-Agent Council & Physical Validation Envelopes
Every Phase 2 work package is governed by 5-dimensional verifiable criteria:
- **Council Critics (FMEA)**:
  - *Systems Engineer*: Clock-to-data skew (<= 10 ps), bondwire parasitic inductance (< 1.2 nH), DRC/LVS clean tapeout checks.
  - *Domain Physicist*: ALD dielectric EOT (<= 0.8 nm), wirebond ball shear (>= 18 gf), PCB trace impedance (50.0 +/- 2.5 ohms).
  - *Supply Chain*: MPW shuttle deadline freeze, Sumitomo EMC mold resin, quick-turn impedance-controlled PCB coupons.
  - *Laya PM*: 8-80h work package bounding, tapeout schedule risk containment.
- **Acceptance Test Cases**:
  - Top-down CD-SEM, TEM cross-section, Keysight 4GHz real-time oscilloscope DDR eye diagrams, Dage 4000 micro-tester ball shear.
- **EHS & Chemical Protocols**:
  - CAS-registered pyrophoric ALD precursor handling (TMA `75-24-1`, TEMAZ `175923-04-3`, Ozone `10028-15-6`), lead-free SAC305 soldering (`7440-31-5`), and epoxy mold resins (`29690-82-2`).
- **Queue-Time (Q-Time) Constraints**:
  - Strict 20-minute clean-to-ALD air exposure ceiling to prevent parasitic interfacial oxide growth.
- **Definition of Done (DoD) & Completion Assertions**:
  - Concrete deliverable filenames (`.tar.gz`, `.csv`, `.pdf`, `.tiff`), quantitative pass/fail thresholds, and unambiguous researcher exit conditions.

## References & Related Files
- [data/modules/07_commercial_180nm_tapeout.json](./data/modules/07_commercial_180nm_tapeout.json)
- [data/modules/08_beol_interconnect_packaging.json](./data/modules/08_beol_interconnect_packaging.json)
- [data/modules/01_mcu_cots.json](./data/modules/01_mcu_cots.json)
- [workflow/critic_testcase_engine.py](./workflow/critic_testcase_engine.py)
- [workflow/crawler_engine.py](./workflow/crawler_engine.py)
- [workflow/council/domain_expert.py](./workflow/council/domain_expert.py)
- [run_overnight.bat](./run_overnight.bat)

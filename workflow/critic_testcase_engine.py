"""
DRAM Foundation VN - Multi-Agent Council Critics & Physical Testcase Synthesis Engine
Enriches all WBS nodes with:
1. 4-Pillar Council Critics (Systems Engineer, Domain Physicist, Supply Chain, Laya PM).
2. Machine-Measurable Acceptance Test Cases (Instrumentation, Pre-flight, Procedure, Pass/Fail Thresholds).
3. Live Gemini generative RAG with empirical ChromaDB grounding and resilient fallback.
4. Dual persistence: structured JSON properties + UI Markdown rendering with KaTeX and tables.
"""

import os
import sys
import json
import time
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from workflow.vector_store import SemiconductorVectorStore
from workflow.council.domain_expert import DomainExpertAgent

try:
    from google import genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


class CriticTestCaseEnricher:
    def __init__(self, db=None, vector_store: Optional[SemiconductorVectorStore] = None):
        from workflow.crawler_engine import DRAMGraphDB
        self.db = db or DRAMGraphDB()
        self.vector_store = vector_store or SemiconductorVectorStore()
        self.domain_expert = DomainExpertAgent(vector_store=self.vector_store)

    def _determine_domain_profile(self, node_title: str, category: str, context: str) -> str:
        title_cat = f"{node_title} {category}".lower()
        specific_context = context.replace("180nm Open-Source DRAM Chip", "").lower()

        # Priority 1: Specific process and equipment keywords in Title & Category
        if any(w in title_cat for w in ["pdk", "foundry", "tapeout", "mpw", "shuttle", "drc", "lvs", "gds", "oasis", "opc", "ebdw", "cmp", "crown", "ald"]):
            return "foundry_and_pdk"
        elif any(w in title_cat for w in ["packaging", "package", "beol", "ate", "wirebond", "wire bonding", "ball bond", "dicing", "sawing", "encapsulation", "mold", "epoxy", "fbga", "tsop", "eds", "wafer sort", "probe card", "qualification", "jedec", "htol"]):
            return "packaging_and_ate"
        elif any(w in title_cat for w in ["fpga", "phy", "controller", "daughtercard", "march c", "shmoo", "firmware", "verilog", "vhdl", "rtl", "telemetry", "pcb", "trace impedance", "eye diagram"]):
            return "fpga_and_controller"
        elif any(w in title_cat for w in ["rca", "clean", "wet bench", "hf", "dhf", "sc-1", "sc-2", "boe", "acid", "dump rinse", "rinse", "strip", "etch"]):
            return "wet_chemistry"
        elif any(w in title_cat for w in ["oxidation", "furnace", "deal-grove", "dry ox", "wet ox", "pyrogenic", "quartz", "tox"]):
            return "thermal_oxidation"
        elif any(w in title_cat for w in ["litho", "mask", "aligner", "optics", "photoresist", "exposure", "uv", "duv", "reticle"]):
            return "lithography_and_optics"
        elif any(w in title_cat for w in ["mcu", "stepper", "motor", "driver", "tmc2209", "esp32", "encoder", "lead screw", "backlash", "stage", "motion"]):
            return "mechatronics_and_drive"
        elif any(w in title_cat for w in ["cell", "sense amp", "bitline", "wordline", "decoder", "storage node", "capacitor", "tcad", "spice", "folded", "refresh", "timing"]):
            return "circuit_and_cell"

        # Priority 2: Ancestral context (excluding generic root chip title)
        if any(w in specific_context for w in ["pdk", "foundry", "tapeout", "mpw", "shuttle", "crown", "ald"]):
            return "foundry_and_pdk"
        elif any(w in specific_context for w in ["packaging", "package", "beol", "ate", "wirebond", "dicing", "fbga", "tsop", "eds", "jedec"]):
            return "packaging_and_ate"
        elif any(w in specific_context for w in ["fpga", "phy", "controller", "daughtercard", "march c", "shmoo", "firmware"]):
            return "fpga_and_controller"
        elif any(w in specific_context for w in ["rca", "clean", "wet bench", "hf", "dhf", "boe", "acid"]):
            return "wet_chemistry"
        elif any(w in specific_context for w in ["oxidation", "furnace", "deal-grove"]):
            return "thermal_oxidation"
        elif any(w in specific_context for w in ["litho", "mask", "aligner", "optics", "photoresist"]):
            return "lithography_and_optics"
        elif any(w in specific_context for w in ["mcu", "stepper", "motor", "driver", "stage"]):
            return "mechatronics_and_drive"
        elif any(w in specific_context for w in ["sense amp", "bitline", "wordline", "cell architecture"]):
            return "circuit_and_cell"

        return "general_semiconductor"

    def synthesize_critics(
        self,
        node_id: str,
        title: str,
        category: str,
        generation: str,
        action_type: str,
        context: str
    ) -> Dict[str, Any]:
        """
        Synthesizes structured critiques from the 4 Council Pillars:
        1. Systems Engineer (Causality, DAG, timing, propagation)
        2. Domain Physicist (Thermodynamics, kinetics, leakage, tolerances)
        3. Supply Chain (COTS vs Make, procurement in Vietnam)
        4. Laya PM (8-80h rule, budget, FMEA failure risk)
        """
        domain = self._determine_domain_profile(title, category, context)

        if domain == "circuit_and_cell":
            se_critic = (
                f"Topological check: Requires verified wordline driver timing (t_r <= 1.8 ns) and precharge VBLP (0.90V) "
                f"prior to sense activation. Cascading delay budget must reserve >= 150 mV read margin across folded bitlines."
            )
            dp_critic = (
                f"Physical constraint: Storage capacitor Cs must maintain >= 28 fF to resist alpha-particle soft errors. "
                f"Subthreshold leakage through access NMOS channel (L=180nm, W=220nm) must remain < 1.0 fA/cell at 85°C."
            )
            sc_critic = (
                f"Supply Chain veto: High-k dielectric precursor (ALD/CVD) is unavailable for DIY fabrication in VN. "
                f"Strictly enforce 180nm Crown/Stacked SiO2-Si3N4-SiO2 (ONO) node compatible with legacy wet/dry equipment."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within 40-60 engineer-hours. FMEA Priority: HIGH (Sense amplifier offset mismatch > 15 mV "
                f"will flip read bitline polarity)."
            )
            failure_modes = [
                "Sense amplifier threshold voltage mismatch (Delta Vth > 15 mV) causing read inversion.",
                "Subthreshold access transistor leakage discharging Cs below sense threshold within refresh interval (< 64 ms).",
                "Wordline parasitic resistance-capacitance (RC) delay exceeding access strobe window."
            ]

        elif domain == "thermal_oxidation":
            se_critic = (
                f"Topological check: Strict prerequisite on upstream SC-1 / DHF 1:50 / SC-2 chemical clean. "
                f"Wafers must enter furnace tube within <= 30 minutes of DHF dip to prevent uncontrolled native oxide regrowth."
            )
            dp_critic = (
                f"Physical constraint: Deal-Grove kinetic regime at 850°C-1000°C requires dry O2 with < 1 ppm moisture for gate oxide (3.5 nm +/- 0.2 nm). "
                f"Field wet oxidation (350 nm) requires pyrogenic H2/O2 torch. Flat-zone temperature uniformity must hold within +/- 0.5°C."
            )
            sc_critic = (
                f"Supply Chain veto: High-purity electronic grade Quartz process tube (100mm-150mm) and SiC boat must be sourced COTS; "
                f"do not attempt local machining of quartz seals."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within 36 engineer-hours. FMEA Priority: CRITICAL (Thermal overshoot > 5°C alters gate oxide "
                f"thickness by > 15%, shifting MOS threshold voltage Vth outside 0.45V +/- 0.05V)."
            )
            failure_modes = [
                "Furnace thermal gradient (> +/- 1.5°C) across wafer diameter causing non-uniform oxide breakdown.",
                "Sodium/potassium ionic contamination in quartz tube causing mobile ionic gate oxide hysteresis.",
                "Delayed furnace insertion causing native oxide regrowth and degraded Si-SiO2 interface state density (Dit > 1e11 eV^-1 cm^-2)."
            ]

        elif domain == "wet_chemistry":
            se_critic = (
                f"Topological check: Station exhaust and DI water loop (18.2 MOhm-cm, particle filter 0.1 um) must interlock "
                f"prior to wafer boat immersion. Rinse cascade must terminate downstream acid carries before SC-2."
            )
            dp_critic = (
                f"Physical constraint: BOE 6:1 (NH4F:HF) etch rate must be calibrated at 70-80 nm/min at 25°C. "
                f"SC-1 (5:1:1 H2O:NH4OH:H2O2) must be maintained at 75°C +/- 2°C to eliminate light organics without pitting Si."
            )
            sc_critic = (
                f"Supply Chain veto: Electronic-grade semiconductor reagents (VLSI/MOS grade) must be procured from certified chemical distributors; "
                f"technical-grade chemicals will induce metallic surface poisoning (Fe, Cu, Ni > 1e10 atoms/cm2)."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within 24-32 engineer-hours. FMEA Priority: HIGH (Chemical cross-contamination or incomplete dump rinse "
                f"leaves watermark defects and micro-masking during subsequent etch)."
            )
            failure_modes = [
                "Watermark defect formation during static pull-out from hydrophilic-to-hydrophobic transition.",
                "Exhaust face-velocity drop below 0.5 m/s causing acid vapor condensation on cleanroom tooling.",
                "Over-etch in BOE undercut exceeding 50 nm, destroying contact via dimensional margins."
            ]

        elif domain == "lithography_and_optics":
            se_critic = (
                f"Topological check: Requires spin-coating bake stabilization (Softbake 90°C for 60s, HMDS vapor prime) before exposure. "
                f"Post-exposure bake and develop latency must be strictly monitored."
            )
            dp_critic = (
                f"Physical constraint: UV exposure dose budget (120-150 mJ/cm2 at 365 nm / 248 nm). "
                f"Overlay alignment budget for {generation} must achieve <= +/- 5 um (Gen 2) or <= +/- 35 nm (Gen 3). Depth of focus (DOF) >= 1.2 um."
            )
            sc_critic = (
                f"Supply Chain veto: Precision fused silica chrome reticles and high-NA objective lenses must be COTS sourced; "
                f"stage micrometers and linear encoders should use standard high-resolution industrial modules."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within 48 engineer-hours. FMEA Priority: HIGH (Alignment misregistration directly ruins multi-layer "
                f"interconnect and contact via connectivity)."
            )
            failure_modes = [
                "Vernier misregistration exceeding overlay budget causing short-circuit between gate and bitline contact via.",
                "Non-uniform exposure illumination across field causing critical dimension (CD) line-width variation > 10%.",
                "Photoresist scumming in fine vias due to insufficient MF-319 developer agitation."
            ]

        elif domain == "mechatronics_and_drive":
            se_critic = (
                f"Topological check: Motor driver step/dir pulses must synchronize with closed-loop optical encoder feedback "
                f"before commanding optical alignment moves. Hardware emergency stop and limit switches must be fail-safe."
            )
            dp_critic = (
                f"Physical constraint: Kinematic positioning resolution for {generation} must achieve < 0.1 mm (Gen 1) or < 1 um (Gen 2). "
                f"Vibrational resonance damping must settle stage within <= 150 ms after step command."
            )
            sc_critic = (
                f"Supply Chain veto: TMC2209 silent stepper drivers, NEMA 17/23 motors, and linear ground guide rails are standard COTS. "
                f"Buy off-the-shelf; Make is strictly restricted to stage brackets, anti-backlash nut fixtures, and firmware."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within 24 engineer-hours. FMEA Priority: MEDIUM (Backlash and thermal expansion in lead screws "
                f"degrade positioning repeatability)."
            )
            failure_modes = [
                "Mechanical lead-screw backlash exceeding 5 um during bidirectional fine step motion.",
                "Stepper motor missed steps caused by microstepping resonance or driver thermal throttling.",
                "Ground loop noise on encoder quadrature lines causing position loss."
            ]

        elif domain == "foundry_and_pdk":
            se_critic = (
                f"Topological check: DRC/LVS rule decks must run clean via KLayout/Magic/OpenLane with zero design rule errors. "
                f"Antenna ratio rules (< 250:1) and substrate tap density checks must pass before GDSII reticle handoff to commercial foundry."
            )
            dp_critic = (
                f"Physical constraint: 3D Crown capacitor ALD ZrO2/Al2O3/ZrO2 (ZAZ) stack must achieve equivalent oxide thickness "
                f"(EOT) <= 0.8 nm and leakage current < 1.0 fA/cell at 1.0V. CMP dishing on M1/M2 tungsten/copper features must hold < 15 nm."
            )
            sc_critic = (
                f"Supply Chain veto: Commercial foundry MPW (Multi-Project Wafer) shuttle submission has an unmovable tapeout window; "
                f"GDSII/OASIS files must freeze 21 days prior. Sourced via open-source or commercial shuttle program under standard NDA."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within 60-120 engineer-hours. FMEA Priority: CRITICAL (A single DRC rule deck discrepancy or LVS "
                f"short-circuit ruins the entire multi-thousand dollar commercial shuttle run and incurs a 4-6 month spin delay)."
            )
            failure_modes = [
                "DRC/LVS hierarchy discrepancy causing undetected metal-to-metal bridging or floating substrate tap.",
                "ALD precursor pulse/purge saturation drift inducing pinhole dielectric breakdown in crown capacitor array.",
                "Chemical Mechanical Planarization (CMP) over-polish causing severe interconnect erosion and open circuits."
            ]

        elif domain == "packaging_and_ate":
            se_critic = (
                f"Topological check: Bondwire loop height (< 150 um) and parasitic bondwire inductance (target < 1.2 nH) must not "
                f"degrade DDR power distribution network (PDN) or induce simultaneous switching noise (SSN). Pinout strictly conforms to JEDEC TSOP-54 / FBGA-60."
            )
            dp_critic = (
                f"Physical constraint: Wafer backgrinding to 150 um must maintain total thickness variation (TTV) < 5 um with zero micro-cracking. "
                f"Thermosonic gold/copper wirebond ball shear force must exceed 18 gf. Epoxy mold compound (EMC) CTE must match silicon (~3 ppm/K)."
            )
            sc_critic = (
                f"Supply Chain veto: Leadframes, ceramic carrier substrates, and Sumitomo/Henkel certified mold compound are COTS. "
                f"Wafer saw dicing and thermosonic ball bonding can be performed on local lab bonder or contracted to regional OSAT partner."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within 40-80 engineer-hours. FMEA Priority: HIGH (Die dicing micro-chipping or thermosonic pad "
                f"delamination causes open circuit or moisture ingress popcorning during 260°C solder reflow)."
            )
            failure_modes = [
                "Dicing blade vibration inducing micro-cracks penetrating active guard ring, leading to moisture degradation.",
                "Intermetallic compound (IMC) voiding (Kirkendall effect) at wirebond pad interface causing open circuits.",
                "Package delamination / popcorning during surface-mount reflow soldering due to mold compound moisture absorption."
            ]

        elif domain == "fpga_and_controller":
            se_critic = (
                f"Topological check: FPGA DDR PHY state machine must rigorously implement JEDEC initialization sequences "
                f"(200 us CKE low, precharge all, MRS registers). Skew across high-speed DDR DQ/DQS matched traces must hold <= 10 ps."
            )
            dp_critic = (
                f"Physical constraint: PCB transmission line characteristic impedance must hold strictly at 50-ohm single-ended / "
                f"100-ohm differential (+/- 5%). Eye diagram opening at receiver must maintain >= 65% horizontal width and >= 200 mV vertical height."
            )
            sc_critic = (
                f"Supply Chain veto: Xilinx/Intel FPGA development carrier boards and high-speed SMA fixtures are standard COTS. "
                f"Make is strictly restricted to custom daughtercard PCB layout, Verilog DDR PHY controller RTL, and firmware."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within 32-60 engineer-hours. FMEA Priority: HIGH (Jitter or power rail ripple on FPGA PLL "
                f"induces intermittent read/write pattern errors during high-speed diagnostic telemetry sweeps)."
            )
            failure_modes = [
                "Clock-to-data skew violating tIS/tIH setup/hold timing margin during DDR write bursts.",
                "Power distribution network impedance resonance causing core VDD droop > 100 mV during simultaneous output switching.",
                "Asynchronous clock domain crossing metastability in memory controller telemetry FIFO."
            ]

        else:
            se_critic = (
                f"Topological check: Prerequisite and dependency relationships mapped cleanly to 180nm DRAM Master Architecture. "
                f"Interface boundaries and data contracts comply with modular WBS graph."
            )
            dp_critic = (
                f"Physical constraint: Target metrics must satisfy engineering tolerances established for {generation}. "
                f"All process parameters ground into empirical literature."
            )
            sc_critic = (
                f"Supply Chain veto: Enforce Make vs Buy distinction. Commercial off-the-shelf components must be purchased; "
                f"custom fab is reserved for silicon-specific processes."
            )
            pm_critic = (
                f"Scope & Risk: Scoped within standard 8-80 hour rule. FMEA Priority: MEDIUM (Process verification required before stage gate)."
            )
            failure_modes = [
                "Process drift exceeding acceptable tolerance band.",
                "Upstream dependency variation causing downstream rework.",
                "Interface specification mismatch between adjacent modules."
            ]

        return {
            "systems_engineer": se_critic,
            "domain_expert": dp_critic,
            "supply_chain": sc_critic,
            "laya_pm": pm_critic,
            "critical_failure_modes": failure_modes
        }

    def synthesize_testcases(
        self,
        node_id: str,
        title: str,
        category: str,
        generation: str,
        action_type: str,
        context: str
    ) -> List[Dict[str, Any]]:
        """
        Synthesizes 2 to 3 machine-measurable Acceptance Test Cases satisfying the Bits-to-Atoms Bridge.
        """
        domain = self._determine_domain_profile(title, category, context)
        prefix = node_id.replace("node-", "TC-").upper()

        if domain == "circuit_and_cell":
            return [
                {
                    "id": f"{prefix}-01",
                    "title": "Storage Cell Charge Retention & Leakage Test",
                    "instrumentation": "Semiconductor Parameter Analyzer (Keysight B1500A / Agilent 4156C) & Cryogenic Probe Station",
                    "pre_conditions": "Wafer held at 85°C +/- 0.5°C; VDD = 1.80V; VBLP = 0.90V; Wordline grounded at 0V in standby.",
                    "procedure": (
                        "1. Write logic '1' (charge to 1.80V) into target 1T1C storage capacitor node.\n"
                        "2. Deassert wordline driver to isolate storage node for t_hold = 64 ms (DRAM standard refresh period).\n"
                        "3. Pulse wordline to VPP = 2.50V and sample bitline charge sharing differential voltage Delta V."
                    ),
                    "pass_fail_criteria": "Differential signal Delta V >= 112.2 mV (Pass); subthreshold leakage I_leak <= 1.0 fA/cell (Pass); Delta V < 80 mV (Fail)."
                },
                {
                    "id": f"{prefix}-02",
                    "title": "Sense Amplifier Strobe Timing & Differential Margin Test",
                    "instrumentation": "200 MHz Active Differential Probe & Mixed-Signal Oscilloscope",
                    "pre_conditions": "Bitlines equalized to VBLP = 0.90V +/- 5 mV; SAN/SAP timing generator initialized.",
                    "procedure": (
                        "1. Inject controlled 50 mV differential offset between BL and BL_B.\n"
                        "2. Trigger SAN pulldown to GND and SAP pullup to 1.80V at strobe edge.\n"
                        "3. Measure sensing delay t_sense (time from strobe to 90% rail separation) and power-rail ripple."
                    ),
                    "pass_fail_criteria": "Sense resolution time t_sense <= 4.2 ns; full rail voltage V_rail >= 1.75V; zero state oscillation (Pass)."
                }
            ]

        elif domain == "thermal_oxidation":
            return [
                {
                    "id": f"{prefix}-01",
                    "title": "Gate Dielectric Thickness & Refractive Index Ellipsometry",
                    "instrumentation": "Spectroscopic Ellipsometer (J.A. Woollam / Rudolph AutoEL) with 632.8 nm He-Ne Laser",
                    "pre_conditions": "Wafer cooled to ambient 22°C in Class 100 laminar clean bench post-furnace pull.",
                    "procedure": (
                        "1. Calibrate ellipsometer against standard bare silicon calibration reference.\n"
                        "2. Execute 9-point radial wafer scan across 100mm/150mm substrate (center, 4 mid-radius, 4 edge at 5mm exclusion).\n"
                        "3. Extract physical film thickness Tox and refractive index n_ox from Cauchy model fit."
                    ),
                    "pass_fail_criteria": "Gate Tox: 3.5 nm +/- 0.2 nm (Pass); Refractive index n_ox: 1.457 +/- 0.005 (Pass); Radial non-uniformity <= 2.5% (Pass)."
                },
                {
                    "id": f"{prefix}-02",
                    "title": "High-Field Dielectric Breakdown & Interface Trap Density (C-V)",
                    "instrumentation": "Mercury Probe (Materials Development Corp) & 1 MHz C-V Impedance Analyzer",
                    "pre_conditions": "Backside native oxide stripped for ohmic contact; room temperature 22°C, dry N2 ambient.",
                    "procedure": (
                        "1. Form temporary mercury Schottky/MOS dot contact (area = 0.001 cm2).\n"
                        "2. Sweep gate voltage from accumulation (-3V) to deep inversion (+3V) at 1 MHz to record high-frequency C-V curve.\n"
                        "3. Ramp electric field until dielectric hard breakdown occurs (I_gate > 100 uA)."
                    ),
                    "pass_fail_criteria": "Breakdown field E_ox >= 10.0 MV/cm (Pass); Midgap interface state density Dit <= 2e10 eV^-1 cm^-2 (Pass)."
                }
            ]

        elif domain == "wet_chemistry":
            return [
                {
                    "id": f"{prefix}-01",
                    "title": "Post-Clean Particle & Metallic Trace Contamination Assay",
                    "instrumentation": "Darkfield Laser Surface Particle Scanner (KLA-Tencor / Surfscan) & TXRF Spectrometer",
                    "pre_conditions": "Post-SC-1 and SC-2 cascade dump rinse; surface Marangoni dried; Class 100 cleanroom.",
                    "procedure": (
                        "1. Load unpatterned witness silicon wafer into darkfield laser scatterometer.\n"
                        "2. Scan complete surface for light point defects (LPD) at size bin >= 180 nm.\n"
                        "3. Perform Total Reflection X-Ray Fluorescence (TXRF) for trace Fe, Cu, Ni surface concentrations."
                    ),
                    "pass_fail_criteria": "LPD count (>= 180 nm) < 10 defects/wafer (Pass); Transition metals (Fe, Ni, Cu) < 5e10 atoms/cm2 (Pass)."
                },
                {
                    "id": f"{prefix}-02",
                    "title": "Buffered Oxide Etch (BOE 6:1) Step Height & Lateral Undercut Profilometry",
                    "instrumentation": "Stylus Profilometer (Veeco Dektak XT) / Atomic Force Microscope (AFM)",
                    "pre_conditions": "Post-etch photoresist stripped in piranha clean (4:1 H2SO4:H2O2) and cascade rinsed.",
                    "procedure": (
                        "1. Zero stylus force baseline at 3 mg on planar SiO2 field.\n"
                        "2. Scan 200 um profile across etched contact window step at 20 um/s scan speed.\n"
                        "3. Record step height h_step and lateral undercut under resist margin."
                    ),
                    "pass_fail_criteria": "Etch depth matches target +/- 5% (Pass); lateral undercut <= 35 nm (Pass); surface roughness Ra < 0.5 nm (Pass)."
                }
            ]

        elif domain == "lithography_and_optics":
            return [
                {
                    "id": f"{prefix}-01",
                    "title": "Optical Overlay Vernier Registration & Misalignment Metrology",
                    "instrumentation": "Optical Inspection Microscope (100x Oil/Dry Objective, 0.9 NA) with Digital Vernier Micrometer",
                    "pre_conditions": "Developed photoresist wafer post-softbake & MF-319 immersion; alignment marks visible.",
                    "procedure": (
                        "1. Focus optical system on wafer alignment cross and reticle outer box fiducials at wafer center and 4 corners.\n"
                        "2. Read vernier comb teeth displacement along X-axis and Y-axis.\n"
                        "3. Calculate rotational theta error and linear misregistration vector (Delta X, Delta Y)."
                    ),
                    "pass_fail_criteria": "Max misregistration |Delta X|, |Delta Y| <= 5.0 um for Gen 2 / <= 35 nm for Gen 3 (Pass); Angular theta <= 0.02 deg (Pass)."
                },
                {
                    "id": f"{prefix}-02",
                    "title": "Critical Dimension (CD) Line-Space Profile & Residue Scum Verification",
                    "instrumentation": "Top-Down / Cross-Sectional CD-SEM (Hitachi / FEI) or High-Resolution UV Profiler",
                    "pre_conditions": "Sample grounded with conductive copper tape to prevent electron beam charging.",
                    "procedure": (
                        "1. Position beam at 5 dense line-space arrays (nominal 180 nm or 1.0 um pitch depending on generation).\n"
                        "2. Take high-contrast secondary electron image at 1.0 kV acceleration voltage.\n"
                        "3. Measure linewidth across 10 distinct scanlines and inspect trench bottom for undeveloped resist scum."
                    ),
                    "pass_fail_criteria": "Linewidth within target +/- 8% (Pass); trench floor completely cleared of organic scum (Pass)."
                }
            ]

        elif domain == "mechatronics_and_drive":
            return [
                {
                    "id": f"{prefix}-01",
                    "title": "Stage Motion Repeatability & Anti-Backlash Bi-Directional Sweep",
                    "instrumentation": "Digital Dial Indicator (Mitutoyo 0.001 mm resolution) & Heidenhain Optical Linear Glass Scale",
                    "pre_conditions": "Stage mounted on granite surface plate; ambient temperature 21°C +/- 1°C.",
                    "procedure": (
                        "1. Command stage to advance 10 mm forward in 100 um increments.\n"
                        "2. Reverse motion 10 mm back to initial origin coordinate.\n"
                        "3. Record position hysteresis gap between forward and reverse passes over 10 consecutive cycles."
                    ),
                    "pass_fail_criteria": "Positioning repeatability <= 1.0 um (Pass); Backlash hysteresis <= 2.0 um (Pass); Travel jerk < 0.05 m/s3 (Pass)."
                },
                {
                    "id": f"{prefix}-02",
                    "title": "Driver Closed-Loop Thermal & Jitter Stability Stress Test",
                    "instrumentation": "FLIR Thermal Imaging Camera & 4-Channel Logic Analyzer on Step/Dir Pins",
                    "pre_conditions": "TMC2209 driver running at 1.2A RMS current; continuous 10 kHz step pulse train for 2 hours.",
                    "procedure": (
                        "1. Monitor motor driver heatsink temperature throughout continuous 2-hour exercise run.\n"
                        "2. Capture step pulse jitter and motor coil inductive flyback voltages.\n"
                        "3. Verify zero missed step flag triggered on controller interrupt line."
                    ),
                    "pass_fail_criteria": "Driver heatsink temp <= 65°C without fan throttling (Pass); Zero missed steps over 72,000,000 pulses (Pass)."
                }
            ]

        elif domain == "foundry_and_pdk":
            return [
                {
                    "id": f"{prefix}-01",
                    "title": "Automated DRC/LVS Golden Rule Deck Physical Sign-Off",
                    "instrumentation": "KLayout / Magic / Pegasus Industrial Physical Verification Batch Engine",
                    "pre_conditions": "Full-chip hierarchical GDSII/OASIS database streamed out; foundry standard cell libraries linked.",
                    "procedure": (
                        "1. Run 180nm DRC rule deck across 100% of mask layers (well, diffusion, poly, contact, M1-M3, pad).\n"
                        "2. Execute Layout Versus Schematic (LVS) netlist extraction against golden SPICE schematic.\n"
                        "3. Verify antenna ratio violations (< 250:1) and substrate noise isolation guard rings."
                    ),
                    "pass_fail_criteria": "DRC clean: 0 violations (Pass); LVS netlist match: 100% topological equivalence with 0 discrepancy (Pass)."
                },
                {
                    "id": f"{prefix}-02",
                    "title": "3D Crown Capacitor High-k Dielectric TEM & C-V Metrology",
                    "instrumentation": "Field-Emission TEM (FEI/Thermo Fisher) & High-Frequency C-V Parameter Analyzer (Keysight B1500A)",
                    "pre_conditions": "ALD deposition of ZrO2/Al2O3/ZrO2 high-k stack on 100x100 test array completed and annealed.",
                    "procedure": (
                        "1. Prepare FIB lamella cross-section through 3D crown capacitor trench structure.\n"
                        "2. Measure physical film thickness and step coverage across bottom, sidewall, and top crown lip via HR-TEM.\n"
                        "3. Perform high-frequency (1 MHz) C-V sweep to extract Equivalent Oxide Thickness (EOT) and dielectric breakdown voltage."
                    ),
                    "pass_fail_criteria": "ALD step coverage >= 95% (Pass); EOT <= 0.8 nm (Pass); Dielectric leakage < 1.0 fA/cell at 1.0V (Pass)."
                }
            ]

        elif domain == "packaging_and_ate":
            return [
                {
                    "id": f"{prefix}-01",
                    "title": "Thermosonic Ball Wirebond Shear & Wire Pull Mechanical Strength Test",
                    "instrumentation": "Dage 4000 / Nordson Microtester Bond Pull & Ball Shear Test System",
                    "pre_conditions": "Sample die wirebonded to leadframe/substrate; ambient temperature 25°C; calibrated 50 gf load cartridge.",
                    "procedure": (
                        "1. Position shear chisel 3.0 um above bond pad aluminum metallization.\n"
                        "2. Perform destructive lateral ball shear test on 30 randomly selected bond balls across peripheral pads.\n"
                        "3. Hook bondwire loop at mid-span and execute vertical pull test to wire rupture according to MIL-STD-883 Method 2011."
                    ),
                    "pass_fail_criteria": "Ball shear force >= 18.0 gf with > 75% ductile residual aluminum coverage (Pass); Wire pull strength >= 5.0 gf (Pass)."
                },
                {
                    "id": f"{prefix}-02",
                    "title": "Electrical Die Sort (EDS) Cold/Hot Wafer Sort Array Pattern Test",
                    "instrumentation": "Advantest / Teradyne Automated Wafer Prober with Multi-Contact Epoxy Probe Card",
                    "pre_conditions": "Un-diced wafer loaded on heated vacuum chuck (tested at 25°C and 85°C); VDD = 1.80V.",
                    "procedure": (
                        "1. Step probe card pins to die contact pads with 50 um probe overdrive.\n"
                        "2. Execute JEDEC parametric DC continuity, leakage, and standby IDD current tests.\n"
                        "3. Run algorithmic March C- memory test across all rows and columns to map functional bit yield."
                    ),
                    "pass_fail_criteria": "Parametric DC continuity pass (Pass); Standby current IDD2N <= 150 uA (Pass); Array yield >= 90% functional dies (Pass)."
                }
            ]

        elif domain == "fpga_and_controller":
            return [
                {
                    "id": f"{prefix}-01",
                    "title": "DDR High-Speed Signal Integrity & Eye Diagram Oscilloscope Capture",
                    "instrumentation": "Keysight Infiniium 4 GHz Real-Time Oscilloscope with Differential High-Z Active Probes",
                    "pre_conditions": "FPGA DDR PHY exercising continuous pseudorandom binary sequence (PRBS-7) write/read bursts at 200 MHz.",
                    "procedure": (
                        "1. Probe DQ0-DQ7 and DQS differential strobe lines directly at DRAM test daughtercard receiver pins.\n"
                        "2. Accumulate 1,000,000 signal transitions into persistence eye diagram.\n"
                        "3. Extract horizontal eye width, vertical eye opening height, and RMS clock jitter."
                    ),
                    "pass_fail_criteria": "Eye width >= 65% UI (Pass); Vertical eye height >= 200 mV (Pass); Clock jitter RMS <= 12 ps (Pass)."
                },
                {
                    "id": f"{prefix}-02",
                    "title": "March C- Algorithmic Memory Fault & Retention Telemetry Verification",
                    "instrumentation": "FPGA Hardware-in-the-Loop Diagnostic Firmware & Automated Python Telemetry Suite",
                    "pre_conditions": "DRAM daughtercard mated to FPGA carrier; supply voltage swept across 1.62V - 1.98V (+/- 10% VDD).",
                    "procedure": (
                        "1. Execute March C- sequence: (w0), up(r0, w1), up(r1, w0), down(r0, w1), down(r1, w0), (r0).\n"
                        "2. Sweep retention pause times from 1 ms to 128 ms between write and read phases.\n"
                        "3. Stream per-address failure bitmap via UART/USB to telemetry logging engine."
                    ),
                    "pass_fail_criteria": "March C- 100% address pass at nominal 64 ms refresh window (Pass); Zero bit error rate (BER < 1e-12) (Pass)."
                }
            ]

        else:
            return [
                {
                    "id": f"{prefix}-01",
                    "title": f"Quantitative Metric Verification for {title}",
                    "instrumentation": "Calibrated Metrology Fixture / Digital Multimeter / Optical Comparator",
                    "pre_conditions": "Laboratory cleanroom ambient conditions established (21°C, 45% RH).",
                    "procedure": (
                        "1. Establish zero baseline calibration on reference artifact.\n"
                        "2. Execute 5 operational cycles under nominal load conditions.\n"
                        "3. Record quantitative output metrics and compare against engineering target."
                    ),
                    "pass_fail_criteria": f"Output measurement within specified tolerance band for {generation} (Pass)."
                }
            ]

    def synthesize_ehs_protocol(
        self,
        domain: str,
        title: str,
        category: str,
        generation: str,
        action_type: str
    ) -> Dict[str, Any]:
        """
        Synthesizes EHS & Hazmat protocols including exact CAS registry numbers,
        PPE levels, immediate antidotes, exhaust ventilation, and waste neutralization.
        """
        if domain == "wet_chemistry":
            return {
                "hazard_level": "Critical",
                "ppe_required": [
                    "Heavy-duty butyl/neoprene gloves (0.7 mm thickness, tested for HF permeation)",
                    "Full-face polycarbonate splash shield over ANSI Z87.1 safety goggles",
                    "Acid-resistant chemical apron with sleeves (PVC/Neoprene)",
                    "Acid gas vapor cartridge respirator (NIOSH approved for HF/HCl)"
                ],
                "cas_chemicals": [
                    {"name": "Hydrofluoric Acid (HF)", "cas_number": "7664-39-3", "purity_grade": "VLSI/MOS Electronic Grade (< 1 ppb metals)", "concentration": "49% conc. or 1:50 DHF"},
                    {"name": "Ammonium Fluoride (NH4F)", "cas_number": "12125-01-8", "purity_grade": "Electronic Grade", "concentration": "40% aq (for BOE 6:1 buffer)"},
                    {"name": "Hydrogen Peroxide (H2O2)", "cas_number": "7722-84-1", "purity_grade": "Electronic Grade (unstabilized)", "concentration": "30% aq (for SC-1 & SC-2)"},
                    {"name": "Hydrochloric Acid (HCl)", "cas_number": "7647-01-0", "purity_grade": "Electronic Grade", "concentration": "37% aq (for SC-2 clean)"},
                    {"name": "Ammonium Hydroxide (NH4OH)", "cas_number": "1336-21-6", "purity_grade": "Electronic Grade", "concentration": "29% aq (for SC-1 clean)"}
                ],
                "antidote_and_first_aid": (
                    "MANDATORY ON-SITE ANTIDOTE: Calcium Gluconate Gel (2.5%). In case of HF skin contact: "
                    "Flush immediately under emergency drench shower for 2-3 minutes, then vigorously massage Calcium Gluconate Gel "
                    "into affected skin continuously until emergency medical response arrives. Never apply standard burn creams."
                ),
                "exhaust_and_ventilation": "Dedicated polypropylene wet bench with vertical laminar exhaust face velocity >= 0.55 m/s. Interlocked with wet acid scrubber.",
                "waste_neutralization": "Segregate fluoride effluent. Neutralize with Calcium Hydroxide (Ca(OH)2) slurry to precipitate insoluble Calcium Fluoride (CaF2). Verify pH 7.0-8.5 before drain discharge."
            }

        elif domain == "thermal_oxidation":
            return {
                "hazard_level": "High",
                "ppe_required": [
                    "High-temperature aluminized Kevlar thermal gloves (rated to 500°C for wafer boat loading)",
                    "Infrared/UV protective safety glasses (shade 3.0)",
                    "Cotton cleanroom lab coat (non-synthetic to prevent melting)"
                ],
                "cas_chemicals": [
                    {"name": "Oxygen (O2)", "cas_number": "7782-44-7", "purity_grade": "Ultra-High Purity (UHP 99.999%)", "concentration": "100% dry gas (< 1 ppm H2O)"},
                    {"name": "Nitrogen (N2)", "cas_number": "7727-37-9", "purity_grade": "Electronic Grade UHP (99.9999%)", "concentration": "Furnace idle purge gas (< 0.1 ppm H2O)"},
                    {"name": "Hydrogen (H2)", "cas_number": "1333-74-0", "purity_grade": "Research Grade 99.999%", "concentration": "Pyrogenic torch wet ox (LEL 4.0% - Explosion Risk)"}
                ],
                "antidote_and_first_aid": "Thermal burn first aid station: Cold sterile water irrigation, hydrogel burn dressing. For high-temp quartz contact, seek immediate medical evaluation.",
                "exhaust_and_ventilation": "Quartz process tube exhaust scavenger with continuous N2 ballast (> 100 CFM flow rate). Flame safety interlock on pyrogenic H2/O2 burner torch.",
                "waste_neutralization": "Thermal effluent passing through point-of-use burn box / thermal combustor before facility exhaust stack."
            }

        elif domain == "lithography_and_optics":
            return {
                "hazard_level": "Moderate",
                "ppe_required": [
                    "Nitrile cleanroom gloves (double gloving recommended during resist spin)",
                    "UV-blocking amber safety glasses (certified 100% optical attenuation at 365 nm / 248 nm)",
                    "Conductive cleanroom ESD footwear"
                ],
                "cas_chemicals": [
                    {"name": "Tetramethylammonium Hydroxide (TMAH)", "cas_number": "75-59-5", "purity_grade": "Semiconductor Grade", "concentration": "2.38% aq in Microposit MF-319 developer"},
                    {"name": "1-Methoxy-2-propyl acetate (PGMEA)", "cas_number": "108-65-6", "purity_grade": "Electronic Grade", "concentration": "Resist solvent base (Shipley 1813)"},
                    {"name": "Hexamethyldisilazane (HMDS)", "cas_number": "999-97-3", "purity_grade": "Semiconductor Grade", "concentration": "100% vapor prime adhesion promoter"}
                ],
                "antidote_and_first_aid": "TMAH skin contact warning: TMAH is a systemic neurotoxin capable of causing respiratory arrest upon dermal absorption. Flush with copious water for 15+ minutes.",
                "exhaust_and_ventilation": "Explosion-proof solvent exhaust bench with activated charcoal VOC adsorber bed (exhaust velocity >= 0.45 m/s).",
                "waste_neutralization": "Flammable solvent waste segregated into grounded stainless steel safety cans. Never mix organic developer/solvent with oxidizers or acids."
            }

        elif domain == "mechatronics_and_drive":
            return {
                "hazard_level": "Low",
                "ppe_required": [
                    "Anti-static ESD grounding wrist strap (1 MOhm safety resistor)",
                    "Impact-resistant safety glasses",
                    "Close-toed cleanroom shoes"
                ],
                "cas_chemicals": [
                    {"name": "Isopropyl Alcohol (IPA)", "cas_number": "67-63-0", "purity_grade": "Electronic Grade 99.9%", "concentration": "Precision stage guide rail degreasing"}
                ],
                "antidote_and_first_aid": "Flush eyes with eyewash if IPA splashes. Mechanical pinch point: isolate 24V power supply and mechanically release leadscrew.",
                "exhaust_and_ventilation": "Standard cleanroom HEPA laminar flow bench (ISO Class 5).",
                "waste_neutralization": "Solvent lint-free wipe disposal in approved self-closing oily waste bin."
            }

        elif domain == "foundry_and_pdk":
            return {
                "hazard_level": "Critical",
                "ppe_required": [
                    "Class 100 cleanroom bunny suit with conductive ESD booties",
                    "Pyrophoric precursor handling apron and dual-layer fluoropolymer gloves",
                    "ANSI Z87.1 approved full-face shield and UV-blocking safety glasses"
                ],
                "cas_chemicals": [
                    {"name": "Trimethylaluminum (TMA)", "cas_number": "75-24-1", "purity_grade": "Electronic Grade (99.999% trace metals)", "concentration": "Pyrophoric liquid ALD precursor"},
                    {"name": "Tetrakis(ethylmethylamino)zirconium (TEMAZ)", "cas_number": "175923-04-3", "purity_grade": "High-purity ALD grade", "concentration": "Liquid precursor for ZrO2 dielectric"},
                    {"name": "Ozone (O3)", "cas_number": "10028-15-6", "purity_grade": "Generated in-situ from UHP O2", "concentration": "15-20 wt% in O2 carrier gas (Strong Oxidizer)"},
                    {"name": "Silica / Ceria CMP Slurry", "cas_number": "1344-28-1", "purity_grade": "Semiconductor Colloidal CMP grade", "concentration": "15-30 wt% colloidal abrasive slurry"}
                ],
                "antidote_and_first_aid": (
                    "Pyrophoric precursor emergency: TMA spontaneously ignites upon contact with air or moisture! "
                    "Do NOT use water on metal alkyl fires. Smother immediately with dry vermiculite, dry sand, or Class D metal fire extinguisher. "
                    "In case of ozone inhalation, move patient to fresh air immediately and administer supplemental oxygen."
                ),
                "exhaust_and_ventilation": "Ultra-high vacuum ALD exhaust manifold connected to dedicated point-of-use thermal decomposition burn-box and wet chemical scrubber. Continuous gas leak detection monitors for TMA/TEMAZ and ozone.",
                "waste_neutralization": "Spent ALD bubbler purging into mineral oil bubblers with inert argon ballast. CMP slurry effluent collected in settling basin, flocculated with alum, and neutralized to pH 6.5-8.0."
            }

        elif domain == "packaging_and_ate":
            return {
                "hazard_level": "Moderate",
                "ppe_required": [
                    "Conductive ESD grounding wrist strap and heel grounders",
                    "Nitrile chemical-resistant gloves (for die-attach epoxy dispensing)",
                    "Safety glasses with side shields",
                    "Particulate N95 respirator during wafer sawing wheel changes and dicing sludge cleanup"
                ],
                "cas_chemicals": [
                    {"name": "Epoxy Novolac Resin (Mold Compound)", "cas_number": "29690-82-2", "purity_grade": "Semiconductor Packaging Grade", "concentration": "Solid pellet / transfer mold compound"},
                    {"name": "Amorphous Silica Filler", "cas_number": "14808-60-7", "purity_grade": "Sub-micron spherical particle", "concentration": "75-88 wt% in epoxy mold compound"},
                    {"name": "Silver-Filled Conductive Die Attach Adhesive", "cas_number": "7440-22-4", "purity_grade": "Electronic Grade Silver Flake", "concentration": "70-80 wt% Ag in epoxy base"}
                ],
                "antidote_and_first_aid": "Skin contact with uncured epoxy: Wash with copious soap and warm water (do not use solvents like acetone which increase dermal absorption). Eye contact with silica dicing slurry: Flush at eyewash for 15 minutes.",
                "exhaust_and_ventilation": "Dicing saw fully enclosed with continuous high-volume DI water mist shroud. Mold press and post-mold curing ovens vented through dedicated VOC thermal oxidizer exhaust stack.",
                "waste_neutralization": "Silicon dicing slurry centrifuged and segregated into solid cake for non-hazardous landfill. Cured thermoset epoxy scrap disposed of as regulated solid waste."
            }

        elif domain == "fpga_and_controller":
            return {
                "hazard_level": "Low",
                "ppe_required": [
                    "Anti-static ESD smock and grounded conductive wrist strap (1 MOhm safety resistor)",
                    "Safety glasses with side shields during soldering and PCB prototyping",
                    "Nitrile gloves during circuit board solvent cleaning"
                ],
                "cas_chemicals": [
                    {"name": "Lead-Free Solder Alloy SAC305 (Sn-Ag-Cu)", "cas_number": "7440-31-5", "purity_grade": "RoHS Compliant Electronic Grade", "concentration": "Sn96.5 / Ag3.0 / Cu0.5 wire & paste"},
                    {"name": "Rosin Core Solder Flux (Colophony)", "cas_number": "8050-09-7", "purity_grade": "Type ROL0 / No-Clean", "concentration": "Internal wire core flux (< 3 wt%)"},
                    {"name": "Isopropyl Alcohol (IPA)", "cas_number": "67-63-0", "purity_grade": "Electronic Grade 99.9%", "concentration": "Flux residue cleaning solvent"}
                ],
                "antidote_and_first_aid": "Thermal burn first aid station: Cold sterile water irrigation, hydrogel burn dressing. For flux vapor irritation, move to well-ventilated fresh air.",
                "exhaust_and_ventilation": "Point-of-use HEPA/carbon solder fume extractor at soldering workstation (airflow >= 150 m3/h). Standard laboratory climate-controlled HVAC.",
                "waste_neutralization": "Collect spent solder dross and PCB trimmings in designated recycling bin for precious metal recovery. Solvent cleaning wipes in sealed flammable safety receptacle."
            }

        else:
            return {
                "hazard_level": "Low",
                "ppe_required": [
                    "Standard cleanroom lab coat and ESD wrist strap",
                    "Safety glasses"
                ],
                "cas_chemicals": [
                    {"name": "Silicon (Si Substrate)", "cas_number": "7440-21-3", "purity_grade": "Electronic Grade P-type <100> prime wafer", "concentration": "Single crystal"}
                ],
                "antidote_and_first_aid": "Standard industrial first aid.",
                "exhaust_and_ventilation": "Ambient cleanroom ventilation.",
                "waste_neutralization": "Standard recycling of scrap silicon."
            }

    def synthesize_q_time_constraints(
        self,
        domain: str,
        title: str,
        category: str,
        generation: str
    ) -> Dict[str, Any]:
        """
        Synthesizes queue-time (Q-Time) physical transfer limits and surface state handshakes.
        """
        if domain == "wet_chemistry":
            return {
                "max_queue_time_air_minutes": 30.0,
                "max_queue_time_n2_hours": 4.0,
                "incoming_surface_state": "Hydrophilic with native chemical oxide (Tox ~1.0 nm) and organic particulates.",
                "outgoing_surface_state": "Hydrophobic H-terminated bare silicon (water contact angle > 75°), zero watermarks, Tox < 0.2 nm.",
                "critical_risk_on_expiry": (
                    "Native SiO2 spontaneously regrows in ambient air at ~0.1 nm/hr, degrading interface state density Dit "
                    "and causing uncontrolled threshold voltage shift in downstream gate oxidation."
                )
            }

        elif domain == "thermal_oxidation":
            return {
                "max_queue_time_air_minutes": 45.0,
                "max_queue_time_n2_hours": 8.0,
                "incoming_surface_state": "Freshly rinsed H-terminated silicon post-DHF dip with zero airborne molecular contamination.",
                "outgoing_surface_state": "Grown thermal SiO2 dielectric layer (3.5 nm +/- 0.2 nm dry ox or 350 nm wet ox), highly uniform.",
                "critical_risk_on_expiry": (
                    "Adsorption of airborne trace organics or sodium ions onto unoxidized wafer leads to mobile charge hysteresis "
                    "and premature gate dielectric breakdown (E_ox < 6 MV/cm)."
                )
            }

        elif domain == "lithography_and_optics":
            return {
                "max_queue_time_air_minutes": 60.0,
                "max_queue_time_n2_hours": 6.0,
                "incoming_surface_state": "HMDS vapor-primed, dehydration-baked substrate (150°C for 30 min) to ensure resist adhesion.",
                "outgoing_surface_state": "Softbaked photoresist film (1.2 um thickness, uniform within +/- 10 nm across wafer).",
                "critical_risk_on_expiry": (
                    "Atmospheric moisture uptake and ambient airborne amine contamination neutralizes surface photoacid generators, "
                    "causing resist 'T-topping' and failed contact via opening."
                )
            }

        elif domain == "circuit_and_cell":
            return {
                "max_queue_time_air_minutes": None,
                "max_queue_time_n2_hours": None,
                "incoming_surface_state": "Extracted parasitic netlist / fabricated test die on vacuum chuck.",
                "outgoing_surface_state": "Strobed and characterized bitline/cell nodes with logged margin data.",
                "critical_risk_on_expiry": "Non-physical queue time; electrical drift under continuous DC bias stress."
            }

        elif domain == "foundry_and_pdk":
            return {
                "max_queue_time_air_minutes": 20.0,
                "max_queue_time_n2_hours": 2.0,
                "incoming_surface_state": "Freshly etched 3D crown capacitor trench structure post-DHF strip, completely free of native oxide.",
                "outgoing_surface_state": "Uniform ALD ZrO2/Al2O3/ZrO2 high-k dielectric stack with TiN top electrode encapsulation.",
                "critical_risk_on_expiry": (
                    "Air exposure exceeding 20 minutes allows uncontrolled spontaneous SiO2 interfacial layer regrowth (> 0.4 nm), "
                    "which severely increases Equivalent Oxide Thickness (EOT) and drastically degrades bitcell storage capacitance."
                )
            }

        elif domain == "packaging_and_ate":
            return {
                "max_queue_time_air_minutes": 120.0,
                "max_queue_time_n2_hours": 48.0,
                "incoming_surface_state": "Saw-diced wafer mounted on UV dicing tape, clean and dry with zero particulate or water residue.",
                "outgoing_surface_state": "Epoxy die-attached, cured, and thermosonically wirebonded to leadframe/substrate pads prior to molding.",
                "critical_risk_on_expiry": (
                    "Atmospheric oxidation of exposed aluminum/copper bond pads degrades thermosonic ball bond adhesion, "
                    "inducing high electrical contact resistance or catastrophic non-stick bond pad lifts."
                )
            }

        elif domain == "fpga_and_controller":
            return {
                "max_queue_time_air_minutes": None,
                "max_queue_time_n2_hours": None,
                "incoming_surface_state": "Fabricated bare test daughtercard PCB with immersion gold (ENIG) surface finish.",
                "outgoing_surface_state": "Fully assembled, reflow-soldered, ultrasonic-cleaned, and impedance-tested PCB daughtercard.",
                "critical_risk_on_expiry": (
                    "Non-critical queue time. If bare PCBs exceed MSL shelf-life (> 168 hours in air), pre-bake at 125°C for 4 hours "
                    "before reflow soldering to prevent PCB delamination and blistering."
                )
            }

        else:
            return {
                "max_queue_time_air_minutes": 120.0,
                "max_queue_time_n2_hours": 24.0,
                "incoming_surface_state": "Clean dry substrate or mechanical component fixture.",
                "outgoing_surface_state": "Processed and inspected assembly node.",
                "critical_risk_on_expiry": "Particulate accumulation exceeding cleanroom ISO Class 5 limits."
            }

    def synthesize_expected_result(
        self,
        domain: str,
        title: str,
        category: str,
        generation: str,
        action_type: str
    ) -> Dict[str, Any]:
        """
        Synthesizes deterministic completion assertions, deliverable artifacts,
        and researcher exit sign-off criteria (Definition of Done) for researchers.
        """
        if domain == "circuit_and_cell":
            return {
                "summary": (
                    f"Completion of {title}: Bitcell storage charge retention, sense amplifier signal margin, "
                    f"and read/write access timing confirmed within 180nm CMOS DRAM specifications."
                ),
                "deliverable_artifacts": [
                    "SPICE_transient_simulation_deck.sp",
                    "Keysight_B1500A_retention_margin_plot.csv",
                    "Monte_Carlo_sense_amp_offset_distribution.pdf"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "Storage cell capacitance (Cs)",
                        "target_value": ">= 28.0 fF",
                        "tolerance": "+/- 2.0 fF",
                        "verification_method": "High-frequency C-V meter (1 MHz) on 100x100 test array"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "Subthreshold access transistor leakage current (Ioff)",
                        "target_value": "<= 1.0 fA/cell",
                        "tolerance": "Max ceiling at 85°C junction temperature",
                        "verification_method": "Keysight B1500A sub-fA High-Resolution SMU"
                    },
                    {
                        "id": "ASSERT-03",
                        "assertion": "Folded bitline differential sense voltage margin (Delta VBL)",
                        "target_value": ">= 180 mV",
                        "tolerance": "Min threshold >= 150 mV across all PVT corners",
                        "verification_method": "Strobe sense amplifier latch comparator with calibrated offset voltage"
                    }
                ],
                "signoff_criteria": (
                    "100% of bitcell test structures pass 64ms retention test without refresh decay; "
                    "zero soft-error read inversions across 10,000 consecutive read cycles at nominal VDD (1.80V)."
                )
            }

        elif domain == "thermal_oxidation":
            return {
                "summary": (
                    f"Completion of {title}: Controlled thermal dielectric growth achieves target thickness uniformity "
                    f"across wafer diameter with minimal interface trap density and verified dielectric breakdown field."
                ),
                "deliverable_artifacts": [
                    "Spectroscopic_Ellipsometry_25_point_map.csv",
                    "MOS_CV_quasi_static_characterization.pdf",
                    "Furnace_flat_zone_pyrometer_log.csv"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "Thermal oxide film thickness (Tox)",
                        "target_value": "3.5 nm (gate) / 350 nm (field)",
                        "tolerance": "+/- 0.2 nm (gate) / +/- 5.0 nm (field)",
                        "verification_method": "Multi-wavelength spectroscopic ellipsometry across 25 wafer sites"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "Dielectric breakdown field strength (E_bd)",
                        "target_value": ">= 10.0 MV/cm",
                        "tolerance": "Zero premature breakdown below 8.0 MV/cm",
                        "verification_method": "Ramped voltage dielectric breakdown (J-E curve) on MOS test capacitors"
                    },
                    {
                        "id": "ASSERT-03",
                        "assertion": "Si-SiO2 interface trap density (Dit)",
                        "target_value": "<= 1.0e11 eV^-1 cm^-2",
                        "tolerance": "Max upper bound at midgap",
                        "verification_method": "High-low frequency C-V technique (Terman method)"
                    }
                ],
                "signoff_criteria": (
                    "25-point film thickness radial uniformity within <= +/- 2.5%; breakdown field E_bd >= 10 MV/cm "
                    "with mobile ionic charge flatband hysteresis Delta Vfb <= 50 mV."
                )
            }

        elif domain == "wet_chemistry":
            return {
                "summary": (
                    f"Completion of {title}: Chemical cleaning and surface preparation verified with zero watermark defects, "
                    f"bare hydrophobic hydrogen-terminated silicon, and calibrated oxide etch rate."
                ),
                "deliverable_artifacts": [
                    "Surface_particle_laser_scan_Surfscan.pdf",
                    "Sessile_drop_contact_angle_measurement.png",
                    "DHF_BOE_calibrated_etch_rate_sheet.csv"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "Post-DHF bare silicon water contact angle",
                        "target_value": ">= 75.0 deg",
                        "tolerance": "+/- 5.0 deg",
                        "verification_method": "Automated Sessile Drop Goniometer (DI water droplet)"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "Surface particulate defect density (> 0.1 um)",
                        "target_value": "< 15 particles/wafer",
                        "tolerance": "Max acceptable particle count on 100mm wafer",
                        "verification_method": "Darkfield Laser Surface Inspection (Surfscan)"
                    },
                    {
                        "id": "ASSERT-03",
                        "assertion": "Surface metallic impurity concentration (Fe, Ni, Cu)",
                        "target_value": "< 1.0e10 atoms/cm²",
                        "tolerance": "Max allowable contamination",
                        "verification_method": "Total Reflection X-Ray Fluorescence (TXRF)"
                    }
                ],
                "signoff_criteria": (
                    "Wafer surface exhibits 100% uniform dewetting / hydrophobicity with zero visible drying marks under bright light; "
                    "residual native oxide Tox < 0.2 nm confirmed by spectroscopic ellipsometry."
                )
            }

        elif domain == "lithography_and_optics":
            return {
                "summary": (
                    f"Completion of {title}: Photolithographic exposure and development achieves critical dimension line-width "
                    f"target within tolerance, satisfying layer-to-layer overlay budget."
                ),
                "deliverable_artifacts": [
                    "CD_SEM_top_down_inspection_micrographs.tiff",
                    "Box_in_box_Vernier_overlay_error_map.csv",
                    "Stylus_profiler_resist_step_height_log.pdf"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "Critical Dimension (CD) line width",
                        "target_value": "180 nm (Gen 3) / 2.0 um (Gen 2) / 0.1 mm (Gen 1)",
                        "tolerance": "+/- 10% maximum CD window (3-sigma)",
                        "verification_method": "Calibrated Top-down Critical Dimension SEM (CD-SEM)"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "Layer-to-layer overlay misregistration (delta_x, delta_y)",
                        "target_value": "<= +/- 35 nm (Gen 3) / <= +/- 5.0 um (Gen 2)",
                        "tolerance": "3-sigma statistical distribution across field",
                        "verification_method": "Optical Box-in-Box Vernier overlay metrology"
                    },
                    {
                        "id": "ASSERT-03",
                        "assertion": "Post-develop photoresist sidewall profile angle",
                        "target_value": ">= 85.0 deg",
                        "tolerance": "+/- 3.0 deg",
                        "verification_method": "Cross-sectional SEM / AFM high-aspect profilometry"
                    }
                ],
                "signoff_criteria": (
                    "Zero photoresist bridging, scumming, or micro-pinholes observed in inspection fields; "
                    "overlay registration strictly within design budget across 100% of die locations."
                )
            }

        elif domain == "mechatronics_and_drive":
            return {
                "summary": (
                    f"Completion of {title}: Precision kinematic stage drive motion achieves specified closed-loop positioning accuracy, "
                    f"bidirectional repeatability, and mechanical resonance damping."
                ),
                "deliverable_artifacts": [
                    "Laser_interferometer_calibration_certificate.csv",
                    "Step_response_vibration_settling_FFT.png",
                    "Safety_limit_and_estop_interlock_log.pdf"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "Bidirectional positioning repeatability",
                        "target_value": "<= 50 nm (Gen 3) / <= 1.0 um (Gen 2) / <= 0.1 mm (Gen 1)",
                        "tolerance": "+/- 10% of target value",
                        "verification_method": "Renishaw Laser Interferometer / Linear Optical Glass Scale"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "Resonance settling time post-motion pulse",
                        "target_value": "<= 150 ms",
                        "tolerance": "Upper threshold to settle within +/- 50 nm",
                        "verification_method": "Piezoelectric 3-axis accelerometer and dynamic signal analyzer"
                    },
                    {
                        "id": "ASSERT-03",
                        "assertion": "Holding position jitter / RMS drift",
                        "target_value": "<= 20 nm RMS",
                        "tolerance": "Measured over 10-minute stationary hold",
                        "verification_method": "Optical quadrature encoder high-speed counter telemetry"
                    }
                ],
                "signoff_criteria": (
                    "Continuous 10,000-cycle back-and-forth travel endurance test completed with zero lost microsteps; "
                    "motor driver temperature stabilizes <= 55°C under continuous holding torque."
                )
            }

        elif domain == "foundry_and_pdk":
            return {
                "summary": (
                    f"Completion of {title}: PDK setup, physical verification rule decks, and full-chip GDSII layouts "
                    f"pass 100% DRC/LVS sign-off and satisfy foundry commercial tapeout design rules."
                ),
                "deliverable_artifacts": [
                    "Golden_180nm_PDK_DRC_LVS_Signoff_Report.pdf",
                    "Commercial_MPW_Tapeout_GDSII_OASIS_Archive.tar.gz",
                    "ALD_3D_Crown_TEM_StepCoverage_Analysis.pdf"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "Foundry Design Rule Check (DRC) Violations",
                        "target_value": "0 violations",
                        "tolerance": "Zero tolerance across full chip and seal ring",
                        "verification_method": "Automated batch DRC run using KLayout / Pegasus Golden Rule Deck"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "Layout Versus Schematic (LVS) Netlist Equivalence",
                        "target_value": "100% match",
                        "tolerance": "Zero net/port mismatches, zero floating pins",
                        "verification_method": "Hierarchical LVS extraction against golden SPICE schematic"
                    },
                    {
                        "id": "ASSERT-03",
                        "assertion": "3D Crown Capacitor ALD Equivalent Oxide Thickness (EOT)",
                        "target_value": "<= 0.80 nm",
                        "tolerance": "+/- 0.05 nm across wafer",
                        "verification_method": "High-frequency 1 MHz C-V accumulation capacitance metrology"
                    }
                ],
                "signoff_criteria": (
                    "100% clean DRC/LVS verification logs signed off by lead tapeout architect; "
                    "checksum of streamed GDSII package validated against foundry MPW shuttle intake submission portal."
                )
            }

        elif domain == "packaging_and_ate":
            return {
                "summary": (
                    f"Completion of {title}: BEOL metallization, electrical die sort (EDS), wafer backgrinding/dicing, "
                    f"and wirebond plastic encapsulation successfully yield JEDEC-qualified DRAM packaged units."
                ),
                "deliverable_artifacts": [
                    "Electrical_Die_Sort_Wafer_Yield_Map.csv",
                    "Wirebond_Ball_Shear_And_Pull_CPK_Report.pdf",
                    "JEDEC_TSOP54_Final_ATE_SpeedBin_Report.pdf"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "Wirebond ball shear strength",
                        "target_value": ">= 18.0 gf",
                        "tolerance": "Minimum failure load >= 15.0 gf across 30 samples",
                        "verification_method": "Dage 4000 micro-tester lateral ball shear per MIL-STD-883"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "Electrical Die Sort (EDS) wafer array functional yield",
                        "target_value": ">= 90.0%",
                        "tolerance": "Minimum yield >= 85.0% on prime wafers",
                        "verification_method": "Automated wafer probe array test with March C- diagnostic patterns"
                    },
                    {
                        "id": "ASSERT-03",
                        "assertion": "Packaged DRAM package coplanarity & lead pitch",
                        "target_value": "<= 0.08 mm coplanarity",
                        "tolerance": "JEDEC TSOP-54 mechanical envelope tolerance (+/- 0.05 mm)",
                        "verification_method": "Optical 3D coordinate measuring machine (CMM) metrology"
                    }
                ],
                "signoff_criteria": (
                    "100% passing electrical continuity and JEDEC parametric DC checks; "
                    "destructive wirebond shear CPK >= 1.67 with zero package voiding or delamination detected under scanning acoustic microscopy (C-SAM)."
                )
            }

        elif domain == "fpga_and_controller":
            return {
                "summary": (
                    f"Completion of {title}: High-speed FPGA DDR memory controller, 50-ohm test daughtercard PCB, "
                    f"and automated diagnostic firmware successfully achieve reliable read/write access and telemetry."
                ),
                "deliverable_artifacts": [
                    "FPGA_DDR_Controller_Synthesizable_RTL.tar.gz",
                    "Controlled_Impedance_Daughtercard_Altium_Gerbers.zip",
                    "Automated_March_C_Shmoo_Telemetry_Suite.py"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "PCB transmission line single-ended characteristic impedance (Z0)",
                        "target_value": "50.0 ohms",
                        "tolerance": "+/- 2.5 ohms (+/- 5%)",
                        "verification_method": "Time Domain Reflectometry (TDR) coupon measurement"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "High-speed DDR data eye opening width at 200 MHz",
                        "target_value": ">= 65.0% UI",
                        "tolerance": "Minimum horizontal eye opening >= 60.0% UI",
                        "verification_method": "Real-time 4 GHz digital oscilloscope persistence eye diagram"
                    },
                    {
                        "id": "ASSERT-03",
                        "assertion": "Algorithmic memory pattern test coverage (March C-)",
                        "target_value": "100.0% address pass",
                        "tolerance": "Zero single-bit faults across entire array at nominal VDD (1.80V)",
                        "verification_method": "Automated hardware-in-the-loop diagnostic firmware sweep"
                    }
                ],
                "signoff_criteria": (
                    "Continuous 24-hour March C- stress run completed with zero bit errors (BER < 1e-12); "
                    "Shmoo plot confirms stable voltage-frequency operating window between 1.62V and 1.98V at target clock rates."
                )
            }

        else:
            return {
                "summary": (
                    f"Completion of {title}: Work package deliverables meet semiconductor engineering standards "
                    f"and baseline specifications for {generation}."
                ),
                "deliverable_artifacts": [
                    "Engineering_verification_report.pdf",
                    "Parametric_compliance_datasheet.csv"
                ],
                "quantitative_assertions": [
                    {
                        "id": "ASSERT-01",
                        "assertion": "Functional specification compliance",
                        "target_value": "100% test scenario pass rate",
                        "tolerance": "Zero critical defect tolerance",
                        "verification_method": "Automated regression verification testbench"
                    },
                    {
                        "id": "ASSERT-02",
                        "assertion": "Parametric tolerance envelope",
                        "target_value": "Within design specification band",
                        "tolerance": "+/- 5.0% nominal",
                        "verification_method": "Calibrated laboratory metrology equipment"
                    }
                ],
                "signoff_criteria": (
                    "All primary acceptance criteria passed; verification data packages archived and signed off by lead engineer."
                )
            }

    def build_markdown_additions(
        self,
        critics: Dict[str, Any],
        testcases: List[Dict[str, Any]],
        ehs: Dict[str, Any],
        q_time: Dict[str, Any],
        expected_result: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Formats critics, testcases, EHS protocols, Q-time constraints, and completion assertions into clean Markdown.
        """
        md = "\n\n---\n\n"
        md += "### Multi-Agent Council Critics & Risk Analysis (FMEA)\n\n"
        md += f"- **Systems Engineer Critic**: {critics.get('systems_engineer', 'N/A')}\n"
        md += f"- **Domain Physicist Critic**: {critics.get('domain_expert', 'N/A')}\n"
        md += f"- **Supply Chain Critic**: {critics.get('supply_chain', 'N/A')}\n"
        md += f"- **Project Manager Critic (Laya PM)**: {critics.get('laya_pm', 'N/A')}\n\n"
        
        failure_modes = critics.get("critical_failure_modes", [])
        if failure_modes:
            md += "**Critical Failure Modes & Mitigation**:\n"
            for fm in failure_modes:
                md += f"1. {fm}\n"
            md += "\n"

        md += "### Machine-Measurable Acceptance Test Cases (Bits-to-Atoms Testbench)\n\n"
        md += "| Test ID | Objective | Test Apparatus / Fixture | Procedure & Condition | Pass / Fail Criteria |\n"
        md += "| :--- | :--- | :--- | :--- | :--- |\n"
        for tc in testcases:
            proc_clean = tc.get('procedure', '').replace('\n', ' ')
            md += f"| `{tc.get('id')}` | **{tc.get('title')}** | {tc.get('instrumentation')} | {proc_clean} | `{tc.get('pass_fail_criteria')}` |\n"
        
        # EHS Protocol Section
        md += "\n### Environmental Health & Safety (EHS) & Hazmat Envelopes\n\n"
        md += f"- **Hazard Classification**: `{ehs.get('hazard_level', 'Low')}`\n"
        md += f"- **Mandatory PPE**: {', '.join(ehs.get('ppe_required', []))}\n"
        md += f"- **Antidote & Immediate Action**: {ehs.get('antidote_and_first_aid', 'Standard first aid.')}\n"
        md += f"- **Ventilation & Interlocks**: {ehs.get('exhaust_and_ventilation', 'Standard cleanroom exhaust.')}\n"
        md += f"- **Waste Disposal & Neutralization**: {ehs.get('waste_neutralization', 'Standard disposal.')}\n\n"

        cas_list = ehs.get("cas_chemicals", [])
        if cas_list:
            md += "**Chemical CAS Registry & Sourcing Specifications**:\n\n"
            md += "| Reagent / Chemical Name | CAS Registry No. | Required Purity Grade | Target Concentration |\n"
            md += "| :--- | :--- | :--- | :--- |\n"
            for chem in cas_list:
                md += f"| **{chem.get('name')}** | `{chem.get('cas_number')}` | {chem.get('purity_grade')} | `{chem.get('concentration')}` |\n"
            md += "\n"

        # Queue-Time Section
        md += "### Queue-Time (Q-Time) & Surface State Handshake Constraints\n\n"
        air_limit = f"{q_time.get('max_queue_time_air_minutes')} minutes" if q_time.get('max_queue_time_air_minutes') else "N/A"
        n2_limit = f"{q_time.get('max_queue_time_n2_hours')} hours" if q_time.get('max_queue_time_n2_hours') else "N/A"
        md += f"- **Max Air Exposure Window**: `{air_limit}` | **Max N2 Storage Window**: `{n2_limit}`\n"
        md += f"- **Incoming Wafer Surface State**: {q_time.get('incoming_surface_state', 'N/A')}\n"
        md += f"- **Outgoing Wafer Surface State**: {q_time.get('outgoing_surface_state', 'N/A')}\n"
        md += f"- **Critical Degradation on Q-Time Expiry**: {q_time.get('critical_risk_on_expiry', 'N/A')}\n"

        # Definition of Done / Completion Assertions Section
        if expected_result:
            md += "\n### Verifiable Completion Assertions & Expected Results (Definition of Done)\n\n"
            md += f"**Exit Objective Summary**:\n> {expected_result.get('summary', 'Work package completion objectives satisfied.')}\n\n"
            
            artifacts = expected_result.get("deliverable_artifacts", [])
            if artifacts:
                md += "**Deliverable Artifacts Checklist**:\n"
                for art in artifacts:
                    md += f"- [ ] `{art}`\n"
                md += "\n"

            assertions = expected_result.get("quantitative_assertions", [])
            if assertions:
                md += "**Quantitative Completion Assertions**:\n\n"
                md += "| Assertion ID | Metric / Physical Assertion | Target Value | Acceptable Tolerance | Verification Instrumentation |\n"
                md += "| :--- | :--- | :--- | :--- | :--- |\n"
                for asrt in assertions:
                    md += (
                        f"| `{asrt.get('id', 'ASSERT')}` | **{asrt.get('assertion', '')}** | "
                        f"`{asrt.get('target_value', '')}` | {asrt.get('tolerance', 'Nominal')} | "
                        f"{asrt.get('verification_method', '')} |\n"
                    )
                md += "\n"

            signoff = expected_result.get("signoff_criteria")
            if signoff:
                md += f"**Lead Researcher Exit Sign-Off Criteria**:\n> {signoff}\n"

        return md

    def synthesize_node_with_gemini(
        self,
        node_id: str,
        title: str,
        category: str,
        generation: str,
        action_type: str,
        context: str
    ) -> Optional[Dict[str, Any]]:
        """
        Deep generative synthesis via Gemini (Antigravity CLI or Google GenAI API)
        grounded in ChromaDB empirical literature.
        """
        import shutil
        import subprocess

        # 1. Retrieve RAG literature from ChromaDB
        query_text = f"{title} {category} {generation}"
        rag_hits = self.vector_store.query(query_text=query_text, n_results=2)
        rag_context = "\n".join([f"- Source: {h['metadata'].get('title', 'Ref')} | {h['document']}" for h in rag_hits])
        if not rag_context:
            rag_context = "Empirical 180nm Legacy DRAM Fabrication Specification."

        prefix = node_id.replace("node-", "TC-").upper()

        prompt = f"""You are the Multi-Agent Council for DRAM Foundation VN (180nm Open-Source DRAM Chip).
Synthesize 5 engineering dimensions for this specific semiconductor work package:
Work Package: {title}
Category: {category}
Generation: {generation}
Action Type: {action_type}
Hierarchy Context: {context}

Empirical Literature Context from ChromaDB:
{rag_context}

Requirements:
1. critics: 4 detailed, technical critiques from systems_engineer, domain_expert, supply_chain, and laya_pm, plus 2-3 critical_failure_modes.
2. testcases: 2 machine-measurable test cases with id (starting with {prefix}), exact instrumentation, pre_conditions, step-by-step procedure, and numerical pass/fail criteria.
3. ehs_protocol: hazard_level (Critical, High, Moderate, or Low), ppe_required, cas_chemicals (name, exact cas_number, purity_grade, concentration), antidote_and_first_aid, exhaust_and_ventilation, waste_neutralization.
4. q_time_constraints: max_queue_time_air_minutes, max_queue_time_n2_hours, incoming_surface_state, outgoing_surface_state, critical_risk_on_expiry.
5. expected_result: verifiable Definition of Done for researchers, containing summary, deliverable_artifacts (array of 2-3 concrete filenames e.g. .csv, .pdf, .tiff), quantitative_assertions (array of 2-3 objects with id starting with ASSERT-, assertion, target_value, tolerance, verification_method), and signoff_criteria (unambiguous researcher exit condition).

Return a SINGLE JSON object strictly matching this schema:
{{
  "critics": {{
    "systems_engineer": "string",
    "domain_expert": "string",
    "supply_chain": "string",
    "laya_pm": "string",
    "critical_failure_modes": ["string", "string"]
  }},
  "testcases": [
    {{
      "id": "{prefix}-01",
      "title": "string",
      "instrumentation": "string",
      "pre_conditions": "string",
      "procedure": "string",
      "pass_fail_criteria": "string"
    }}
  ],
  "ehs_protocol": {{
    "hazard_level": "Critical|High|Moderate|Low",
    "ppe_required": ["string"],
    "cas_chemicals": [
      {{"name": "string", "cas_number": "string", "purity_grade": "string", "concentration": "string"}}
    ],
    "antidote_and_first_aid": "string",
    "exhaust_and_ventilation": "string",
    "waste_neutralization": "string"
  }},
  "q_time_constraints": {{
    "max_queue_time_air_minutes": 30,
    "max_queue_time_n2_hours": 4,
    "incoming_surface_state": "string",
    "outgoing_surface_state": "string",
    "critical_risk_on_expiry": "string"
  }},
  "expected_result": {{
    "summary": "string",
    "deliverable_artifacts": ["string"],
    "quantitative_assertions": [
      {{
        "id": "ASSERT-01",
        "assertion": "string",
        "target_value": "string",
        "tolerance": "string",
        "verification_method": "string"
      }}
    ],
    "signoff_criteria": "string"
  }}
}}
Return ONLY valid JSON. No conversational text, no backticks, no markdown fences.
"""
        # Try local Antigravity CLI (agy)
        agy_bin = shutil.which("agy")
        if agy_bin:
            try:
                cmd = [
                    agy_bin,
                    "-p", prompt,
                    "--model", "gemini-3.8-flash-low",
                    "--disable-slash-commands",
                    "--output-format", "json",
                    "--dangerously-skip-permissions"
                ]
                res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", stdin=subprocess.DEVNULL, timeout=45)
                if res.returncode == 0:
                    data = json.loads(res.stdout)
                    resp_text = data.get("response", "").strip()
                    parsed = self._repair_and_parse_json(resp_text)
                    if parsed:
                        return parsed
                    else:
                        logging.warning(f"Could not parse Gemini JSON response for [{node_id}]. Falling back to heuristics.")
            except Exception as e:
                logging.warning(f"Gemini agy call failed for [{node_id}]: {e}. Falling back to domain heuristics.")

        return None

    def _repair_and_parse_json(self, raw_text: str) -> Optional[Dict[str, Any]]:
        """
        Resiliently repairs and parses LLM JSON outputs, handling markdown fences,
        trailing commas, and mismatched array/object closing delimiters.
        """
        import re
        if not raw_text:
            return None
        
        # 1. Direct parse attempt
        try:
            return json.loads(raw_text)
        except Exception:
            pass

        # 2. Extract outermost JSON object
        match = re.search(r"\{.*\}", raw_text, re.DOTALL)
        if not match:
            return None
        s = match.group(0).strip()

        # 3. Direct parse of extracted block
        try:
            return json.loads(s)
        except Exception:
            pass

        # 4. Remove trailing commas before closing brackets/braces
        s = re.sub(r",\s*([\]}])", r"\1", s)
        try:
            return json.loads(s)
        except Exception:
            pass

        # 5. Fix mismatched closing bracket ']' for an object inside an array
        s = re.sub(r'("(?:id|title|pass_fail_criteria|verification_method|target_value|tolerance)":\s*(?:"[^"]*"|[\d\.]+))\s*\n(\s*)\]\s*([,\n\]])', r'\1\n\2}\3', s)
        s = re.sub(r'("pass_fail_criteria":\s*"[^"]*")\s*\n(\s*)\]\s*\n(\s*)\]', r'\1\n\2}\n\3]', s)
        s = re.sub(r'("verification_method":\s*"[^"]*")\s*\n(\s*)\]\s*\n(\s*)\]', r'\1\n\2}\n\3]', s)

        try:
            return json.loads(s)
        except Exception:
            return None

    def enrich_node(self, node_id: str, force: bool = False, use_llm: bool = True) -> bool:
        """
        Enriches a single node with critics, test cases, EHS protocols, Q-time constraints, and completion assertions.
        """
        node = self.db.get_node(node_id)
        if not node:
            return False

        # If already enriched across all 5 dimensions and not forcing, skip
        has_critics = bool(node.get("critics"))
        has_testcases = bool(node.get("testcases"))
        has_ehs = bool(node.get("ehs_protocol"))
        has_q_time = bool(node.get("q_time_constraints"))
        has_expected = bool(node.get("expected_result"))
        if has_critics and has_testcases and has_ehs and has_q_time and has_expected and not force:
            return False

        context = self.db.get_context_travel_up(node_id)
        title = node.get("label", node_id)
        category = node.get("category", "General")
        generation = node.get("generation", "Gen 2 (µm)")
        action_type = node.get("action_type", "Make")
        domain = self._determine_domain_profile(title, category, context)

        # Attempt Gemini generative RAG synthesis first if enabled
        gemini_data = None
        if use_llm:
            gemini_data = self.synthesize_node_with_gemini(
                node_id=node_id,
                title=title,
                category=category,
                generation=generation,
                action_type=action_type,
                context=context
            )

        if gemini_data and isinstance(gemini_data, dict):
            critics = gemini_data.get("critics") or self.synthesize_critics(node_id, title, category, generation, action_type, context)
            testcases = gemini_data.get("testcases") or self.synthesize_testcases(node_id, title, category, generation, action_type, context)
            ehs = gemini_data.get("ehs_protocol") or self.synthesize_ehs_protocol(domain, title, category, generation, action_type)
            q_time = gemini_data.get("q_time_constraints") or self.synthesize_q_time_constraints(domain, title, category, generation)
            expected_result = gemini_data.get("expected_result") or self.synthesize_expected_result(domain, title, category, generation, action_type)
        else:
            # Deterministic heuristic synthesis fallback
            critics = self.synthesize_critics(node_id, title, category, generation, action_type, context)
            testcases = self.synthesize_testcases(node_id, title, category, generation, action_type, context)
            ehs = self.synthesize_ehs_protocol(domain, title, category, generation, action_type)
            q_time = self.synthesize_q_time_constraints(domain, title, category, generation)
            expected_result = self.synthesize_expected_result(domain, title, category, generation, action_type)

        # Format updated SOP content
        current_sop = node.get("sop_content") or f"# Standard Operating Procedure: {title}\n\n**Category**: {category} | **Generation**: {generation}\n"
        
        # Strip prior auto-generated markdown additions if re-enriching
        if "### Multi-Agent Council Critics & Risk Analysis" in current_sop:
            current_sop = current_sop.split("### Multi-Agent Council Critics & Risk Analysis")[0].rstrip()
            if current_sop.endswith("---"):
                current_sop = current_sop[:-3].rstrip()

        md_additions = self.build_markdown_additions(critics, testcases, ehs, q_time, expected_result)
        updated_sop = current_sop + md_additions

        # Update in SQLite
        with self.db._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE nodes SET
                    critics = ?,
                    testcases = ?,
                    ehs_protocol = ?,
                    q_time_constraints = ?,
                    expected_result = ?,
                    sop_content = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = ?;
            """, (
                json.dumps(critics, ensure_ascii=False),
                json.dumps(testcases, ensure_ascii=False),
                json.dumps(ehs, ensure_ascii=False),
                json.dumps(q_time, ensure_ascii=False),
                json.dumps(expected_result, ensure_ascii=False),
                updated_sop,
                node_id
            ))
            conn.commit()

        return True

    def get_enrichment_status(self) -> Dict[str, int]:
        """
        Returns stats on how many nodes have critics, testcases, EHS, Q-time, and expected results.
        """
        with self.db._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT count(*) FROM nodes;")
            total = cursor.fetchone()[0]
            cursor.execute("SELECT count(*) FROM nodes WHERE critics IS NOT NULL AND length(critics) > 5;")
            with_critics = cursor.fetchone()[0]
            cursor.execute("SELECT count(*) FROM nodes WHERE testcases IS NOT NULL AND length(testcases) > 5;")
            with_testcases = cursor.fetchone()[0]
            cursor.execute("SELECT count(*) FROM nodes WHERE ehs_protocol IS NOT NULL AND length(ehs_protocol) > 5;")
            with_ehs = cursor.fetchone()[0]
            cursor.execute("SELECT count(*) FROM nodes WHERE q_time_constraints IS NOT NULL AND length(q_time_constraints) > 5;")
            with_q_time = cursor.fetchone()[0]
            cursor.execute("SELECT count(*) FROM nodes WHERE expected_result IS NOT NULL AND length(expected_result) > 5;")
            with_expected = cursor.fetchone()[0]

            min_enriched = min(with_critics, with_testcases, with_ehs, with_q_time, with_expected)
            return {
                "total": total,
                "with_critics": with_critics,
                "with_testcases": with_testcases,
                "with_ehs": with_ehs,
                "with_q_time": with_q_time,
                "with_expected_result": with_expected,
                "pending_enrichment": total - min_enriched
            }

    def run_enrichment_pipeline(self, limit: Optional[int] = None, force: bool = False, use_llm: bool = True):
        """
        Master overnight enrichment loop: Audits all nodes across 6 disciplines.
        """
        engine_mode = "Gemini 3.8 Flash (Deep RAG Synthesis)" if use_llm else "Fast Heuristic Templates"
        logging.info(f"🔬 DRAM Foundation VN: 360° Node Enrichment Pipeline Activated [{engine_mode}]...")
        
        with self.db._get_connection() as conn:
            cursor = conn.cursor()
            if force:
                cursor.execute("SELECT id FROM nodes ORDER BY rowid ASC;")
            else:
                cursor.execute("""
                    SELECT id FROM nodes 
                    WHERE critics IS NULL OR length(critics) <= 5
                       OR testcases IS NULL OR length(testcases) <= 5
                       OR ehs_protocol IS NULL OR length(ehs_protocol) <= 5
                       OR q_time_constraints IS NULL OR length(q_time_constraints) <= 5
                       OR expected_result IS NULL OR length(expected_result) <= 5
                    ORDER BY rowid ASC;
                """)
            target_ids = [row[0] for row in cursor.fetchall()]

        total_targets = len(target_ids)
        logging.info(f"📋 Identified {total_targets} node(s) requiring 360° Council Critics, Test Cases, EHS, Q-Time & Assertions.")

        if total_targets == 0:
            logging.info("🎉 All nodes across the DRAM WBS tree already possess full 360° enrichment!")
            return

        processed = 0
        start_time = time.time()

        for idx, node_id in enumerate(target_ids, 1):
            if limit and processed >= limit:
                logging.info(f"🎯 Reached requested enrichment limit ({limit}). Halting.")
                break

            success = self.enrich_node(node_id, force=force, use_llm=use_llm)
            if success:
                processed += 1
                elapsed = time.time() - start_time
                avg_time = elapsed / processed if processed > 0 else 0
                logging.info(f"[{processed}/{total_targets}] ⚡ Enriched Node [{node_id}] ({avg_time:.2f}s/node)")

        # Sync all changes back to modular JSON files
        logging.info("💾 Flushing enriched nodes to data/modules/*.json...")
        self.db.sync_to_json()
        logging.info(f"✅ Successfully enriched {processed} node(s) with Council Critics, Test Cases, EHS, Q-Time & Assertions.")


if __name__ == "__main__":
    enricher = CriticTestCaseEnricher()
    status = enricher.get_enrichment_status()
    print("Enrichment Status:", json.dumps(status, indent=2))

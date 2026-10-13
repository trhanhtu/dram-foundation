"""
DRAM Foundation VN - Authoritative Semiconductor Literature Corpus
Contains empirical formulas, PDK rules, equipment manuals, chemical recipes,
and test vehicle specifications for seeding the ChromaDB knowledge base.
"""

from typing import List, Dict, Any

COMPREHENSIVE_SEMICONDUCTOR_CORPUS: List[Dict[str, Any]] = [
    # =========================================================================
    # DISCIPLINE 1: LITHOGRAPHY, OPTICS & ALIGNMENT
    # =========================================================================
    {
        "id": "doc-sky130-pdk-litho-rules",
        "title": "SkyWater SKY130 Open PDK Design Rules & Lithography Grid",
        "source": "SkyWater Technology / Google Open Source Silicon",
        "category": "Optics & Lithography",
        "content": """
        SkyWater SKY130 is a 130nm-to-180nm commercial open-source foundry process technology with a minimum drawn gate length of 150 nm.
        Manufacturing Grid: The physical placement grid resolution is 0.005 um (5 nm).
        Critical Dimensions (CD):
        - Minimum active diffusion (diff) width: 0.15 um.
        - Minimum poly gate length: 0.15 um (150 nm).
        - Minimum poly gate spacing: 0.21 um.
        - Minimum contact hole dimension: 0.17 um x 0.17 um.
        - Metal 1 minimum width: 0.14 um; minimum metal 1 pitch: 0.34 um.
        Lithography Process:
        Exposure uses deep ultraviolet (DUV 248nm KrF excimer laser) for critical poly and contact layers, and i-line (365nm) for upper metal routing layers.
        Overlay Error Budget: Maximum permissible overlay error between gate poly and active diffusion is <= 35 nm.
        Rayleigh Criteria: Feature resolution R = k1 * (lambda / NA). With lambda = 248 nm, NA = 0.65, k1 = 0.40, minimum resolvable half-pitch is 152 nm.
        Depth of Focus: DOF = k2 * (lambda / NA^2) >= 0.5 um, ensuring process window across wafer topography.
        """
    },
    {
        "id": "doc-karl-suss-ma6-operation",
        "title": "Karl Suss MA6 Mask Aligner Standard Operating Procedure & Gap Control",
        "source": "Stanford Nanofabrication Facility (SNF) / Suss MicroTec Manual",
        "category": "Optics & Lithography",
        "content": """
        The Karl Suss MA6 mask aligner is an industry-standard sub-micron contact and proximity photolithography system.
        Alignment Mechanics:
        - Wedge Error Compensation (WEC): Mechanically levels the wafer chuck against the mask holder using spherical air bearings, achieving parallelism < 1 um across 100mm wafers.
        - Split-Field Microscope: Dual-objective binocular optical microscope with 5x, 10x, and 20x objectives paired with dual high-resolution CMOS cameras.
        - Alignment Precision: Operator overlay alignment precision is <= 0.5 um in vacuum contact mode, and +/- 2 to 5 um in proximity mode.
        Operating Modes:
        1. Proximity Exposure: Mask and wafer separated by a calibrated air gap of 10 um to 30 um. Prevents mask damage, resolution limited by Fresnel diffraction to ~2.5 um.
        2. Soft Contact: Nitrogen pressure holds wafer gently against mask (0.1 to 0.5 bar); resolution ~1.5 um.
        3. Hard Contact: Nitrogen pressure under chuck forces wafer into firm contact (1.0 bar); resolution ~1.0 um.
        4. Vacuum Contact: Vacuum chamber evacuated between mask and wafer (< 200 mbar absolute); achieves sub-micron resolution (0.6 to 0.8 um).
        Exposure Source: 350W Mercury short-arc lamp delivering i-line (365 nm, 15 mW/cm^2) and h-line (405 nm).
        """
    },
    {
        "id": "doc-photoresist-processing-az1500-shipley",
        "title": "Positive Photoresist Spin Dynamics, Soft Bake & Development Protocol",
        "source": "Microchem / Shipley Lithography Applications Manual",
        "category": "Optics & Lithography",
        "content": """
        Standard high-resolution positive photoresists (Shipley 1813, AZ 1512, AZ 5214E) are diazonaphthoquinone (DNQ) novolak resin formulations.
        Spin Coating Recipe:
        - Wafer Dehydration: Convection oven bake at 150°C for 30 minutes, or hot plate at 180°C for 2 minutes to desorb moisture.
        - HMDS Vapor Priming: Expose wafer to hexamethyldisilazane vapor for 3 minutes at 120°C to form hydrophobic trimethylsilyl monolayer.
        - Dynamic Dispense: 3 mL resist dispensed at 500 RPM for 4 seconds, followed by acceleration ramp at 10,000 RPM/s to 4,000 RPM for 30 seconds.
        - Resulting film thickness: Shipley 1813 yields 1.33 um +/- 10 nm; AZ 1512 yields 1.20 um +/- 8 nm.
        Bake Profiles:
        - Soft Bake (Pre-Bake): Flat vacuum hot plate at 115°C for 60 seconds. Drives off 85% of solvent (PGMEA) to stabilize resist matrix.
        - Post-Exposure Bake (PEB): Flat hot plate at 110°C for 60 seconds (essential for image reversal resist AZ 5214E to activate cross-linking acid catalyst).
        Development:
        - Developer: Microposit MF-319 or AZ 726 MIF (0.26N tetramethylammonium hydroxide - TMAH, metal-ion-free).
        - Puddle development time: 45 to 60 seconds at 21°C +/- 0.5°C.
        - Rinse & Dry: Continuous overflow dump rinse with 18.2 MOhm-cm deionized water for 60 seconds, followed by spin-dry or filtered N2 gun dry.
        """
    },

    # =========================================================================
    # DISCIPLINE 2: THERMAL OXIDATION, DIFFUSION & FURNACE DYNAMICS
    # =========================================================================
    {
        "id": "doc-deal-grove-quantitative-data",
        "title": "Deal-Grove Silicon Oxidation Kinetic Coefficients & Gate Oxide Thickness",
        "source": "Deal & Grove (1965) / Plummer Silicon VLSI Technology",
        "category": "Thermal Processing",
        "content": """
        The Deal-Grove equation describes thermal oxidation kinetics of single-crystal silicon: x_o^2 + A * x_o = B * (t + tau).
        Arrhenius Rate Constants for (100) Silicon:
        1. Dry Oxygen (Dry O2):
           - At 850°C: Parabolic rate constant B = 0.0031 um^2/hr; Linear rate constant B/A = 0.018 um/hr.
           - At 900°C: B = 0.0054 um^2/hr; B/A = 0.034 um/hr.
           - At 1000°C: B = 0.0117 um^2/hr; B/A = 0.071 um/hr.
           - Activation energies: E_B = 1.24 eV (diffusion through oxide); E_B/A = 2.00 eV (interfacial reaction).
           - Thin oxide initial regime: For dry O2, an anomalous rapid initial oxidation regime occurs for x_o < 25 nm (d_0 = 25 nm, tau = 0.37 hr at 1000°C).
           - 180nm Gate Oxide Target: Dry oxidation at 850°C for 22 minutes in 100% dry O2 yields physical thickness t_ox = 3.5 nm +/- 0.2 nm.
        2. Wet Pyrogenic Steam (H2 + O2 combustion):
           - At 1000°C: B = 0.287 um^2/hr; B/A = 1.45 um/hr.
           - Oxidation rate is approximately 10x to 20x faster than dry O2 due to higher solid solubility of H2O in SiO2.
           - Field Oxide (LOCOS / STI) Target: Wet oxidation at 1000°C for 45 minutes yields t_ox = 350 nm (0.35 um) field isolation dielectric.
        Interface Passivation:
        Post-oxidation anneal (POA) in pure N2 or forming gas (95% N2 / 5% H2) at 450°C for 30 minutes passivates dangling silicon bonds (trivalent Si traps),
        reducing midgap interface state density D_it to < 1.0 x 10^10 cm^-2 eV^-1 and fixed oxide charge Q_f to < 2.0 x 10^10 cm^-2.
        """
    },
    {
        "id": "doc-furnace-three-zone-pid-engineering",
        "title": "Three-Zone Quartz Tube Diffusion Furnace Thermal Profiling & Gas Delivery",
        "source": "Thermco / Bruce Technologies Semiconductor Furnace Manual",
        "category": "Thermal Processing",
        "content": """
        A semiconductor diffusion and oxidation furnace consists of a horizontal fused quartz process tube (outer diameter 150mm to 200mm, purity 99.999% SiO2)
        surrounded by a 3-zone resistive heating element (Kanthal A1 or APM alloy coils).
        Three-Zone Thermal Regulation:
        - Zone division: Source zone (gas inlet), Center zone (wafer process flat zone), and Load zone (door end).
        - Temperature control: Dual Type-R/S Pt-Pt/Rh thermocouples per zone connected to a digital PID temperature controller.
        - Center Flat Zone: The middle 350 mm of the tube must maintain a flat temperature zone with uniformity <= +/- 0.5°C at 1000°C to 1200°C.
        Gas Flow Dynamics:
        - Gas Delivery: Mass flow controllers (MFC) calibrated for high-purity O2 (99.999%), ultra-pure Ar, N2, and dry HCl (1-3% added to clean metallic impurities and mobile Na+ ions).
        - Flow rate: 2.0 to 5.0 SLPM (standard liters per minute) laminar gas sweep velocity prevents ambient air back-diffusion through the exhaust scavenger.
        - Wafer Loading: Silicon wafers loaded on quartz boats (semiconductor cassettes) pushed at controlled cantilever velocity <= 100 mm/min to prevent thermal shock dislocation slip.
        """
    },

    # =========================================================================
    # DISCIPLINE 3: WET CHEMISTRY, ETCHING & CLEANROOM SAFETY
    # =========================================================================
    {
        "id": "doc-rca-complete-chemical-protocol",
        "title": "RCA Standard Clean SC-1, SC-2, and Native Oxide HF Dip Engineering",
        "source": "Kern, W. - Handbook of Semiconductor Wafer Cleaning Technology",
        "category": "Chemical Processing",
        "content": """
        The RCA cleaning sequence is the universal baseline cleaning standard prior to high-temperature furnace operations in microelectronics.
        1. RCA-1 / SC-1 (Standard Clean 1 - Alkaline Oxidation):
           - Chemistry: 5 parts UPW (Ultra-Pure Water) : 1 part 29% NH4OH (Ammonium Hydroxide) : 1 part 30% H2O2 (Hydrogen Peroxide).
           - Bath Temperature: 70°C to 75°C (heated in quartz or PTFE immersion bath with megasonic agitation at 1 MHz).
           - Immersion Time: 10 minutes.
           - Action: Solubilizes organic surface contamination by simultaneous oxidative dissolution and microscopic base etching of silicon (~0.5 nm). Removes sub-micron particles via zeta potential repulsion.
           - Cascade Dump Rinse: 5 cycles with 18.2 MOhm-cm deionized water until bath resistivity > 16 MOhm-cm.
        2. Native Oxide Strip (Dilute HF Dip):
           - Chemistry: 1:50 or 1:100 HF : UPW (0.5% to 1.0% Hydrofluoric Acid).
           - Immersion Time: 15 to 30 seconds at 22°C.
           - Endpoint: Hydrophobic dewetting transition (water sheets off bare silicon without wetting).
        3. RCA-2 / SC-2 (Standard Clean 2 - Acid Desorption):
           - Chemistry: 6 parts UPW : 1 part 37% HCl (Hydrochloric Acid) : 1 part 30% H2O2.
           - Bath Temperature: 75°C +/- 2°C.
           - Immersion Time: 10 minutes.
           - Action: Forms soluble coordination complexes with alkali ions (Na+, K+) and transition metals (Fe, Cu, Ni, Au), preventing furnace contamination.
           - Final Dump Rinse & Dry: Overflow rinse to 18.2 MOhm-cm, followed by filtered N2 Marangoni or isopropyl alcohol (IPA) vapor drying.
        """
    },
    {
        "id": "doc-boe-oxide-etch-mechanics",
        "title": "Buffered Oxide Etch (BOE 6:1 & 7:1) Silicon Dioxide Wet Etch Rates",
        "source": "Williams, K. - Journal of Microelectromechanical Systems (JMEMS)",
        "category": "Chemical Processing",
        "content": """
        Buffered Oxide Etch (BOE) is a buffered solution of hydrofluoric acid and ammonium fluoride used to etch silicon dioxide with high selectivity over silicon.
        Formulation (BOE 6:1):
        - 6 parts 40% NH4F (Ammonium Fluoride) : 1 part 49% HF (Hydrofluoric Acid).
        - Buffering Action: NH4F maintains a constant fluoride ion activity and pH ~4.5, preventing rapid depletion of HF and delivering steady, predictable etch rates.
        Etch Rates at 25°C:
        - Thermally grown SiO2 (dry or wet): 80 nm/min to 100 nm/min (800 to 1000 Angstroms/min).
        - Chemical Vapor Deposition (CVD / TEOS) SiO2: 150 to 220 nm/min (higher etch rate due to lower film density).
        - Native oxide: Etched in 10 to 15 seconds.
        - Etch Selectivity: SiO2 to single-crystal Silicon selectivity > 100 : 1; SiO2 to Silicon Nitride (Si3N4) selectivity > 20 : 1.
        Safety Protocols:
        - HF Hazard: HF penetrates skin deeply, dissociated fluoride ions bind serum calcium (Ca2+) and magnesium (Mg2+), causing life-threatening hypocalcemia and cardiac arrest.
        - First Aid Mandate: Calcium gluconate 2.5% topical gel must be within arm's reach of the wet bench; immediately apply and massage continuously upon any suspected contact.
        - Wet Bench Interlock: Laminar face velocity must be >= 100 FPM (0.5 m/s); acid exhaust scrubber pressure differential monitor interlocked with chemical supply.
        """
    },

    # =========================================================================
    # DISCIPLINE 4: DRAM CELL ARCHITECTURE, SENSE AMPLIFIERS & READOUT
    # =========================================================================
    {
        "id": "doc-dram-cell-keeth-baker-fundamentals",
        "title": "1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets",
        "source": "Keeth, Baker, Johnson, Lin - DRAM Circuit Design: Fundamental and High-Speed Topics",
        "category": "DRAM Architecture",
        "content": """
        The foundational dynamic random access memory (DRAM) cell consists of a single access NMOS transistor and a single storage capacitor (1T1C).
        Physical Cell Footprint:
        - Classic open bitline: 6F^2 footprint (where F is feature size, 180 nm -> cell area = 0.194 um^2). High noise sensitivity.
        - Folded bitline: 8F^2 footprint (cell area = 0.259 um^2 at F = 180 nm). Industry standard for robust common-mode noise rejection.
        Capacitance Budgets:
        - Storage Node Capacitance (C_s): Must be >= 25 fF to 30 fF per cell (nominally 28 fF).
        - Bitline Parasitic Capacitance (C_b): In an array block of 256 or 512 cells per bitline, C_b is typically 150 fF to 250 fF.
        - Capacitance Ratio: C_b / C_s must be maintained between 5 : 1 and 9 : 1. If C_b / C_s exceeds 10 : 1, read margin degrades severely.
        Read Signal Margin:
        Prior to wordline activation, bitlines (BL and /BL) are precharged and equalized to V_DD / 2 (0.9 V for 1.8 V core).
        When the wordline (WL) is pulsed high, cell charge is shared with the bitline:
        Delta V = (C_s / (C_s + C_b)) * (V_cell - V_DD / 2).
        For C_s = 28 fF, C_b = 200 fF, V_cell = 1.8 V (stored '1'):
        Delta V = (28 / 228) * (1.8 - 0.9) = 0.123 * 0.9 V = 110 mV.
        For stored '0' (V_cell = 0 V):
        Delta V = (28 / 228) * (0 - 0.9) = -110 mV.
        The sense amplifier must reliably resolve this +/- 110 mV differential voltage in the presence of thermal noise and transistor V_th mismatch.
        """
    },
    {
        "id": "doc-dram-folded-sense-amp-timing",
        "title": "Cross-Coupled Regenerative Sense Amplifier Timing & Charge Restoration",
        "source": "IEEE Journal of Solid-State Circuits (JSSC) / Micron DRAM Design Manual",
        "category": "DRAM Architecture",
        "content": """
        A DRAM sense amplifier consists of a cross-coupled PMOS pull-up pair (P-sense amp) and an NMOS pull-down pair (N-sense amp) connected between BL and /BL.
        Read / Restore Operational Phase Timing:
        1. Equalization Phase (EQ high): Equalization NMOS transistors short BL and /BL together and tie them to a precision V_BLP (V_DD / 2) voltage reference.
        2. Wordline Turn-On (WL pulse): EQ goes low. WL transitions from 0V to boosted V_PP (2.6 V to 2.8 V) to overdrive NMOS access gate without threshold loss (V_DD + V_th). Charge shares onto BL.
        3. N-Sense Activation (SAN low): The common source node SAN (initially at V_DD/2) is pulled rapidly to GND through an NMOS pulldown switch. The NMOS with higher gate voltage conducts harder, driving the lower bitline toward 0V.
        4. P-Sense Activation (SAP high): Shortly after SAN activates (1-2 ns delay), SAP is pulled to V_DD through a PMOS pullup switch. The cross-coupled PMOS pair pulls the higher bitline fully to V_DD.
        5. Destructive Read Restoration: Because the storage capacitor remains connected to the bitline while the sense amplifier drives full rail CMOS levels, cell charge is 100% restored to original state.
        6. Column Select (CSL): Column access transistors connect the amplified BL and /BL signals to global I/O lines for readout.
        """
    },
    {
        "id": "doc-dram-charge-pump-vpp",
        "title": "High-Voltage Wordline Charge Pump (VPP) Dickson Oscillator Architecture",
        "source": "Dickson, J. - IEEE JSSC On-Chip High-Voltage Generation in MNOS Integrated Circuits",
        "category": "DRAM Architecture",
        "content": """
        In 180nm DRAM cells, the pass transistor is an NMOS enhancement device with threshold voltage V_th ~ 0.5V to 0.7V.
        Threshold Voltage Loss Problem:
        If the wordline were driven only to V_DD (1.8 V), the maximum voltage that could be written into the storage node capacitor is V_DD - V_th = 1.8V - 0.6V = 1.2V.
        This represents a 33% loss in stored charge, drastically shortening retention time and degrading read sense margin.
        V_PP Overdrive Solution:
        The wordline driver must be supplied by an on-chip boosted high voltage: V_PP = V_DD + V_th + Delta V_overdrive >= 2.5V to 2.8V.
        Dickson Charge Pump Design:
        - Topology: 4-stage charge pump using diode-connected NMOS or pass gates with flying capacitors (C_pump = 20 pF to 50 pF) driven by two-phase non-overlapping clocks (Phi1, Phi2 at 20 MHz to 50 MHz).
        - Voltage Regulator: Dynamic feedback voltage divider and bandgap-referenced comparator shut off pump clock when V_PP reaches 2.7V +/- 50 mV.
        - Ripple Voltage: V_PP ripple must be maintained < 30 mV peak-to-peak using an on-chip decoupling reservoir capacitor (C_filter >= 500 pF).
        """
    },

    # =========================================================================
    # DISCIPLINE 5: PHYSICAL TEST VEHICLES & REALITY LADDER GATES
    # =========================================================================
    {
        "id": "doc-reality-gate-stage1-diode",
        "title": "Stage 1 Reality Gate: Bulk PN Junction Diode & Schottky Barrier Characterization",
        "source": "Sze, S.M. - Physics of Semiconductor Devices",
        "category": "Device Physics & Metrology",
        "content": """
        The physical baseline validation of any semiconductor fabrication capability begins with a discrete PN junction diode on a bulk silicon substrate.
        Physical Test Vehicle Structure:
        - Substrate: P-type (100) Silicon, Boron doped, resistivity 1 to 10 Ohm-cm (acceptor concentration N_A ~ 10^15 to 10^16 cm^-3).
        - N+ Diffusion Well: Phosphorus spin-on dopant or predeposition at 950°C; junction depth x_j ~ 0.5 to 1.5 um; surface concentration N_D > 10^19 cm^-3.
        - Anode / Cathode Metallization: Sputtered Al (350 nm) sintered at 420°C for 20 minutes in forming gas to form ohmic contacts.
        Target Metrics & Verification:
        1. Diode Current-Voltage (I-V) Equation: I = I_s * [exp(q * V / (eta * k_B * T)) - 1].
        2. Ideality Factor (eta): Measured in the forward bias range 0.2V <= V <= 0.5V. Target: 1.05 <= eta <= 1.20. (If eta > 1.5, severe recombination in space charge region indicates crystal defects or metallic contamination).
        3. Forward Turn-On Voltage (V_F): V_F = 0.65 V to 0.70 V at 1 mA forward current.
        4. Reverse Saturation Leakage Current (I_s): I_s < 10 nA/cm^2 at -5V reverse bias at 25°C.
        5. Reverse Breakdown Voltage (V_BR): V_BR > 40 V to 60 V (sharp avalanche breakdown without soft pre-breakdown leakage).
        """
    },
    {
        "id": "doc-reality-gate-stage2-moscap",
        "title": "Stage 2 Reality Gate: Planar MOS Capacitor C-V Profiling & Dit Extraction",
        "source": "Nicollian & Brews - MOS Physics and Technology",
        "category": "Device Physics & Metrology",
        "content": """
        The Planar MOS Capacitor (MOSCAP) is the indispensable diagnostic test structure connecting macro thermal oxidation to sub-micron MOSFET devices.
        Test Structure:
        - Aluminum circular gate dots (diameter 200 um, 500 um, 1000 um) sputtered through shadow masks onto thermally grown gate oxide (3.5 nm to 25 nm) on P-type (100) Si.
        - Backside substrate contact: Gold or Aluminum ohmic contact layer.
        High-Frequency (1 MHz) and Quasi-Static C-V Characterization:
        1. Accumulation Region (Gate Voltage V_G < V_fb): High-frequency capacitance saturates at the maximum oxide capacitance C_ox = (epsilon_ox * epsilon_0 * Area) / t_ox.
           - Accurately yields physical oxide thickness t_ox with +/- 0.1 nm precision.
        2. Depletion Region (V_fb < V_G < V_T): Capacitance drops as silicon space-charge depletion layer widens in series with C_ox.
        3. Inversion Region (V_G > V_T): Low-frequency / quasi-static C recovers to C_ox as thermal generation-recombination creates electron inversion layer; high-frequency C remains at minimum C_min.
        Interface Trap Density (D_it) Extraction:
        - Calculated using the High-Low Frequency C-V Method or Terman Method:
          D_it = (C_ox / q) * [ (C_LF / (C_ox - C_LF)) - (C_HF / (C_ox - C_HF)) ] [cm^-2 eV^-1].
        - Acceptance Standard: D_it must be <= 1.0 x 10^11 cm^-2 eV^-1 at midgap.
        Fixed Oxide Charge (Q_f):
        - Extracted from Flatband Voltage shift: Delta V_fb = V_fb(ideal) - V_fb(measured) = - Q_f / C_ox. Target: Q_f / q < 5.0 x 10^10 cm^-2.
        """
    },
    {
        "id": "doc-reality-gate-stage3-mosfet",
        "title": "Stage 3 Reality Gate: Discrete Long-Channel MOSFET & CMOS Inverter Verification",
        "source": "Taur & Ning - Fundamentals of Modern VLSI Devices",
        "category": "Device Physics & Metrology",
        "content": """
        Before attempting dense memory cell arrays, discrete NMOS and PMOS transistors and CMOS inverter logic gates must be physically verified.
        Test Transistor Geometries:
        - Long-channel reference transistor: W / L = 20 um / 5 um.
        - Intermediate transistor: W / L = 10 um / 1.0 um.
        - Target sub-micron transistor: W / L = 2.0 um / 0.18 um (180 nm).
        Static Device Parameters:
        1. Threshold Voltage (V_th): Extracted at linear region (V_DS = 50 mV) via maximum transconductance (g_m) extrapolation.
           - NMOS target: V_thn = +0.55 V +/- 50 mV.
           - PMOS target: V_thp = -0.60 V +/- 50 mV.
        2. On/Off Current Ratio (I_on / I_off): Measured at V_DS = 1.8 V; I_on >= 500 uA/um (at V_GS = 1.8V); I_off <= 10 pA/um (at V_GS = 0V). I_on / I_off ratio > 10^7.
        3. Subthreshold Swing (S): S = ln(10) * (k_B * T / q) * (1 + C_dep / C_ox). Target: S <= 75 to 85 mV/decade at 300K.
        CMOS Inverter Transfer Characteristics:
        - Voltage Transfer Curve (VTC): Measured by sweeping V_in from 0V to 1.8V.
        - Inverter Switching Threshold: V_M = 0.90 V +/- 50 mV (exactly mid-rail for symmetric noise margins).
        - Noise Margins: NM_H = V_OH - V_IH >= 0.65 V; NM_L = V_IL - V_OL >= 0.65 V.
        - Dynamic Ring Oscillator: 11-stage CMOS ring oscillator to measure propagation delay tau_d = 1 / (2 * N * f_osc) <= 80 ps/stage.
        """
    },

    # =========================================================================
    # DISCIPLINE 6: PACKAGING, METROLOGY & ELECTRICAL INTERCONNECTS
    # =========================================================================
    {
        "id": "doc-transmission-line-measurement-tlm",
        "title": "Transmission Line Measurement (TLM) for Specific Contact Resistivity",
        "source": "Schroder, D. - Semiconductor Material and Device Characterization",
        "category": "Metrology & Testing",
        "content": """
        Transmission Line Measurement (TLM) structures determine the specific contact resistivity (rho_c) between metal interconnects and doped silicon diffusion.
        Structure Dimensions:
        - Identical rectangular contact pads (width W = 100 um, length L_pad = 50 um) spaced at progressively increasing gaps: d = 5 um, 10 um, 20 um, 40 um, 80 um.
        Measurement & Calculation:
        - Total measured resistance R_T between two adjacent pads is: R_T = 2 * R_c + (R_s / W) * d.
        - Plotting R_T versus pad spacing d yields a linear regression line:
          - Slope = R_s / W (directly gives diffusion sheet resistance R_s).
          - Y-intercept at d = 0 gives 2 * R_c (twice the contact resistance).
          - X-intercept gives -2 * L_T (where L_T is the transfer length).
        - Specific Contact Resistivity: rho_c = R_c * W * L_T = R_s * L_T^2 [Ohm * cm^2].
        Acceptance Specification for 180nm DRAM:
        - Contact Resistance: R_c < 10 Ohm per contact.
        - Specific Contact Resistivity: rho_c <= 1.0 x 10^-6 Ohm * cm^2.
        - If rho_c > 10^-5 Ohm * cm^2, contact pre-clean (in-situ Ar sputter etch or dilute HF dip) and post-metallization sintering (400°C in forming gas) must be recalibrated.
        """
    },
    {
        "id": "doc-wire-bonding-packaging-standards",
        "title": "Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging",
        "source": "Harman, G. - Wire Bonding in Microelectronics: Materials, Processes, Reliability",
        "category": "Packaging & Metrology Equipment",
        "content": """
        Final packaging of fabricated DRAM dies connects on-chip bonding pads (100 um x 100 um aluminum squares) to external lead frame pins.
        Bonding Methods:
        1. Thermosonic Gold Ball Bonding: 25 um diameter 99.99% gold wire. Electronic flame-off (EFO) forms free-air ball; capillary presses ball onto pad at 150°C with ultrasonic transducer pulse (60 kHz, 50-100 mW, 20-30 ms).
        2. Ultrasonic Aluminum Wedge Bonding: 25 um diameter Al-1% Si wire. Operates at room temperature (25°C), ideal for temperature-sensitive prototypes and ceramic DIP / QFN packages.
        Mechanical Quality Standards:
        - Wire Pull Strength: Mil-Std-883 Method 2011 requires pull test force >= 4.0 grams-force for 25 um wire. Failure must occur in wire span, not at bond interface.
        - Die Attach: Silver-filled conductive epoxy (e.g. Ablebond 84-1LMIS) cured at 150°C for 60 minutes. Thermal resistance R_th <= 5°C/W; void area under die < 5% via acoustic microscopy.
        - Package Hermeticity: Ceramic dual in-line package (CERDIP-24 / CERDIP-28) sealed with low-melting solder glass at 430°C or epoxy lid seal.
        """
    }
]

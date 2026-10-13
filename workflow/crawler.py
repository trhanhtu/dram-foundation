"""
DRAM Foundation VN - Knowledge Ingestion & Web Crawler Pipeline
Crawls URLs, parses technical PDFs, and ingests baseline semiconductor literature into ChromaDB.
"""

from pathlib import Path
import re
from typing import List, Dict, Any, Optional
import httpx
from bs4 import BeautifulSoup
import fitz  # PyMuPDF

from workflow.vector_store import SemiconductorVectorStore

# Built-in seed semiconductor literature for immediate offline verification
SEED_SEMICONDUCTOR_DOCUMENTS = [
    {
        "id": "doc-sam-zeloof-z1",
        "title": "Sam Zeloof Z1 Garage Semiconductor Journal (2018)",
        "source": "https://sam.zeloof.xyz/first-ic/",
        "category": "Lithography & Garage Fabrication",
        "content": """
        Photolithography in a garage requires a stable macroscopic stage and an optical projection or contact aligner.
        Using a modified microscope objective (10x Plan Achromat, NA 0.25) allows micron-scale feature resolution.
        Photoresist: Shipley 1813 spin-coated at 4000 RPM yields ~1.3 micron thickness.
        Soft bake at 115°C for 60 seconds on a flat aluminum hot plate.
        Exposure requires a high-power 365nm i-line UV LED source or mercury vapor lamp.
        Developer: Microposit MF-319 for 45-60 seconds, followed by rigorous deionized (DI) water rinse.
        Alignment tolerance at Gen 1 is ±100 microns (0.1 mm), improving to ±5 microns in Gen 2.
        """
    },
    {
        "id": "doc-dram-180nm-cell",
        "title": "Legacy 180nm DRAM Architecture & Cell Capacitor Engineering",
        "source": "IEEE / Legacy Foundry Technical Reports",
        "category": "DRAM Architecture",
        "content": """
        A classic 180nm DRAM cell uses a 1-Transistor 1-Capacitor (1T1C) architecture with an 8F^2 or 6F^2 cell layout.
        The storage capacitor must maintain a minimum capacitance of 25 to 30 fF (femtofarads) per cell to ensure
        data retention time > 64 ms at 85°C.
        In 180nm nodes, stacked capacitors (Crown or Cylinder type) utilize silicon nitride (Si3N4) or tantalum pentoxide (Ta2O5)
        high-k dielectrics with equivalent oxide thickness (EOT) around 3 to 4 nm.
        Bitline and wordline pitch is approximately 360 nm to 400 nm.
        Gate dielectric is thermally grown silicon dioxide (SiO2) at 850°C-900°C dry oxidation with ~3.5 nm physical thickness.
        """
    },
    {
        "id": "doc-chemical-etch-boe",
        "title": "Silicon Dioxide Etching with Buffered Oxide Etch (BOE)",
        "source": "Semiconductor Chemical Processing Handbook",
        "category": "Chemical Processing",
        "content": """
        Buffered Oxide Etch (BOE 6:1) consists of 6 parts 40% NH4F (Ammonium Fluoride) and 1 part 49% HF (Hydrofluoric Acid).
        Etch rate of thermally grown SiO2 at 25°C is approximately 100 nm/minute (1000 Å/min).
        Buffered etching prevents excessive depletion of HF and maintains constant pH and uniform etch rates.
        Wetting agent (0.1% Triton X-100 or Fluorad) must be added to eliminate bubble entrapment in micro-trenches.
        Photoresist adhesion during BOE requires HMDS (Hexamethyldisilazane) vapor prime at 120°C prior to resist coating.
        Caution: Hydrofluoric acid penetrates skin and binds calcium; calcium gluconate gel must be present at all times.
        """
    },
    {
        "id": "doc-linear-stage-mechanics",
        "title": "Precision Linear Stage Design & Vibration Damping",
        "source": "Slocum - Precision Machine Design",
        "category": "Precision Mechanics",
        "content": """
        Precision linear stages for macroscopic Gen 1 lithography require high structural rigidity and minimal Abbe error.
        Extruded aluminum 4040 frames paired with precision ground linear guide rails (MGN12H) provide straightness < 5 microns/100mm.
        Drive mechanism: C7 rolled ball screws or anti-backlash lead screws driven by NEMA 17 stepper motors with 1/16 microstepping.
        Vibration isolation: Neoprene dampers or sorbothane pads isolate external vibrations above 30 Hz.
        Closed-loop positioning can be achieved with commercial optical encoders or linear magnetic scales (resolution 1 micron).
        """
    },
    {
        "id": "doc-rca-cleaning",
        "title": "Standard RCA-1 and RCA-2 Silicon Wafer Cleaning Procedure",
        "source": "Kern, W. - RCA Review & Semiconductor Cleaning Science",
        "category": "Chemical Processing",
        "content": """
        Standard RCA wafer clean removes organic residues, particle contamination, and metallic ionic traces before oxidation.
        RCA-1 (SC-1): 5 parts Deionized H2O, 1 part Ammonium Hydroxide (29% NH4OH), 1 part Hydrogen Peroxide (30% H2O2).
        Temperature: Heated to 70°C-80°C for 10-15 minutes. Solubilizes organic surface films and oxidizes light trace metals.
        Intermediate Rinse: Dump rinse with 18.2 MOhm-cm deionized water for 3 minutes.
        Hydrofluoric Dip: 1:50 HF:H2O dip for 15-30 seconds to strip native oxide; surface transitions from hydrophilic to hydrophobic.
        RCA-2 (SC-2): 6 parts Deionized H2O, 1 part Hydrochloric Acid (37% HCl), 1 part Hydrogen Peroxide (30% H2O2).
        Temperature: 70°C-80°C for 10 minutes. Eliminates alkali ions (Na+, K+) and heavy metals (Fe, Cu, Ni).
        Final Step: Nitrogen (N2) blow-dry with high-purity filtered gun inside laminar flow clean bench.
        """
    },
    {
        "id": "doc-deal-grove-oxidation",
        "title": "Deal-Grove Silicon Thermal Oxidation Kinetics in Quartz Tube Furnace",
        "source": "Deal & Grove - Journal of Applied Physics",
        "category": "Thermal Processing",
        "content": """
        Thermal oxidation of single-crystal silicon follows the linear-parabolic kinetic model: x0^2 + A*x0 = B*(t + tau).
        In the thin regime (x0 << A/2), oxidation is interface reaction-rate limited with linear rate constant k_l = B/A.
        In the thick regime (x0 >> A/2), oxidation is diffusion-limited through grown SiO2 with parabolic rate constant B.
        Dry Oxidation: Performed at 900°C-1000°C in pure dry O2. Produces dense, high-dielectric breakdown gate oxide (E_bd > 10 MV/cm)
        with minimal interface trap density (D_it < 10^10 cm^-2 eV^-1). Thickness target for 180nm gate dielectric is 3.5 to 4.0 nm.
        Wet Oxidation: Performed with water vapor (pyrogenic steam H2 + O2) at 1000°C. Parabolic rate constant B is roughly 10x higher
        than dry oxidation, ideal for thick field oxide isolation (LOCOS or STI trench fill, 300 nm to 500 nm).
        Furnace Equipment: High-purity quartz process tube (fused silica), 3-zone PID temperature controller maintaining ±0.5°C over 30 cm flat zone.
        """
    },
    {
        "id": "doc-vacuum-sputter-aluminum",
        "title": "Physical Vapor Deposition (PVD) Sputtering of Aluminum Metallization Interconnects",
        "source": "Vossen & Kern - Thin Film Processes",
        "category": "Thin Film Deposition",
        "content": """
        Interconnect metallization for 180nm DRAM bitlines and wordline strapping utilizes aluminum-copper alloy (Al-0.5% Cu)
        or pure aluminum deposited via planar DC magnetron sputtering.
        Vacuum Chamber Parameters: Base pressure must pump down below 2x10^-6 Torr using turbomolecular or cryopump to prevent
        oxygen incorporation. Sputtering process gas is high-purity Argon (Ar 99.999%) maintained at 3 to 5 mTorr working pressure.
        Target: 99.999% (5N) Aluminum target driven by DC magnetron power supply at 1.5 to 3.0 kW.
        Deposition Rate: Calibrated at 50 to 100 nm/minute. Film thickness target for metal-1 is 350 nm ± 5%.
        Sheet Resistance: Measured sheet resistance target is R_s < 0.08 Ohm/sq after post-metal anneal (forming gas N2/H2 95/5 at 400°C for 30 minutes).
        Step Coverage: Substrate stage heated to 200°C-250°C during deposition promotes surface adatom mobility across contact vias.
        """
    },
    {
        "id": "doc-optical-mask-aligner-mechanics",
        "title": "Optical Mask Aligner Mechanics: Gap Control and UV Exposure Dose",
        "source": "Mack, C. - Fundamental Principles of Optical Lithography",
        "category": "Optics & Lithography",
        "content": """
        Optical mask aligners transfer circuit geometry from a chromium-on-quartz mask onto photoresist-coated wafers.
        Alignment Modes:
        1. Contact Printing: Mask contacts photoresist directly. Yields highest resolution (< 1 micron) but risks mask scratch defects.
        2. Proximity Printing: Mask separated by 10 to 20 micron air gap. Eliminates contact damage; diffraction limits resolution to ~2-3 microns.
        Gap Setting: Controlled using three high-precision differential micrometers or closed-loop piezo actuators with 0.1 micron sensitivity.
        UV Exposure Optics: 365nm (i-line) LED array or 200W Mercury short-arc lamp coupled through fly's eye integrator lens for >95% beam uniformity across wafer.
        Exposure Dose: Calibrated using optical radiometer (mW/cm^2). For Shipley 1813 (1.3 um thickness), optimum clear dose is 120-150 mJ/cm^2.
        Fiducial Mark Alignment: Crosshair alignment marks on wafer and mask viewed through split-field binocular microscope with dual CMOS cameras.
        """
    },
    {
        "id": "doc-four-point-probe-metrology",
        "title": "Four-Point Collinear Probe Metrology for Semiconductor Sheet Resistance",
        "source": "ASTM Standard F84 & Semiconductor Material Characterization",
        "category": "Metrology & Testing",
        "content": """
        The four-point probe method measures sheet resistance (R_s) and bulk resistivity of doped silicon wafers and metal thin films.
        Probe Geometry: Four collinear, equally spaced tungsten carbide tips with radius 50-100 um and spacing s = 1.0 mm.
        Operating Principle: A constant DC current (I = 1 mA to 10 mA) passes through the outer two probes (1 and 4).
        The inner two probes (2 and 3) measure the resulting floating potential difference (V).
        For thin semiconductor films (film thickness t << s/2): Sheet Resistance R_s = (pi / ln(2)) * (V / I) = 4.5324 * (V / I) [Ohm/square].
        Geometric Correction Factors: When wafer diameter is finite (< 40 times probe spacing), edge proximity correction factors F(d/s) apply.
        Repeatability Requirement: Gauge R&R must maintain measurement coefficient of variation CV < 1.0% across 9-point wafer mapping.
        """
    },
    {
        "id": "doc-dram-sense-amplifier",
        "title": "Folded Bitline Sense Amplifier Circuit Design for DRAM Cell Readout",
        "source": "Keeth & Baker - DRAM Circuit Design: A Tutorial",
        "category": "DRAM Circuit Design",
        "content": """
        The DRAM sense amplifier performs differential sensing and refresh of minute charge stored in the 1T1C memory cell.
        Architecture: CMOS cross-coupled inverter latch connected between complementary bitlines BL and /BL in a folded-bitline topology.
        Precharge Operation: Prior to wordline assertion, bitlines are equalized to V_DD / 2 using an equalization transistor network.
        Signal Development: Wordline turns on access transistor, dumping cell charge Q_s = C_s * (V_cell - V_BL) onto bitline.
        Differential Voltage Delta V = (C_s / (C_BL + C_s)) * (V_cell - V_DD/2).
        For typical cell capacitance C_s = 25 fF and bitline capacitance C_BL = 250 fF, signal delta V is approximately 100 mV to 150 mV.
        Sensing Operation: Sense amplifier activates latching signals (SAN pulls to GND, SAP pulls to V_DD), rapidly driving
        the differential voltage to full rail CMOS levels (0V and V_DD), simultaneously restoring cell charge to 100%.
        Pitch Matching: Sense amplifier pitch must match memory array bitline pitch (360 nm in 180nm node), requiring interleaved layout.
        """
    },
    {
        "id": "doc-photoresist-spin-hmds",
        "title": "Photoresist Spin Coating Dynamics and HMDS Vapor Priming",
        "source": "Madou - Fundamentals of Microfabrication",
        "category": "Lithography & Garage Fabrication",
        "content": """
        Photoresist spin coating is governed by the Meyerhofer model balancing centrifugal outward force against viscous drag and solvent evaporation.
        Wafer Dehydration: Silicon wafers must be baked at 150°C-200°C for 30 minutes to desorb physisorbed water molecules.
        HMDS Priming: Hexamethyldisilazane vapor reactively silylates hydrophilic silanol (-Si-OH) groups into hydrophobic methyl-siloxane (-Si-O-Si(CH3)3) bonds,
        increasing resist adhesion and preventing peel-off during acid wet etching.
        Spin Recipe: Dispense 2-3 mL Shipley 1813 at 500 RPM for 5 seconds (spread cycle), ramp at 10,000 RPM/s to 4,000 RPM for 30 seconds (spin cycle).
        Film Uniformity: Produces 1.30 um ± 15 nm film across 100mm wafers. Edge bead removal (EBR) using PGMEA solvent jet prevents clamp contamination.
        """
    },
    {
        "id": "doc-wet-chemistry-piranha",
        "title": "Piranha Acid Cleaning Solution Chemistry and Safety Protocols",
        "source": "Plummer, Deal, Griffin - Silicon VLSI Technology",
        "category": "Chemical Processing",
        "content": """
        Piranha solution (Caro's acid, peroxymonosulfuric acid H2SO5) is a strong oxidizing mixture used to strip stubborn photoresist and organic residues.
        Formulation: 3 parts Concentrated Sulfuric Acid (96% H2SO4) to 1 part Hydrogen Peroxide (30% H2O2). Always add peroxide slowly to sulfuric acid, never reverse.
        Reaction Dynamics: Highly exothermic; mixture spontaneously heats to 110°C-130°C. Generates active atomic oxygen that rapidly converts hydrocarbons to CO2 and H2O.
        Immersion Time: Submerge wafers in PTFE (Teflon) or fused quartz carrier for 10-15 minutes.
        Safety Requirements: Strict PPE including heavy neoprene gloves, face shield, and chemical apron. Never store piranha in sealed containers due to continuous gas evolution (O2, SO2).
        """
    },
    {
        "id": "doc-furnace-pid-control",
        "title": "Three-Zone Quartz Tube Thermal Dynamics and PID Temperature Regulation",
        "source": "Levinson - Principles of Lithography & Thermal Processing",
        "category": "Thermal Processing",
        "content": """
        High-temperature quartz tube furnaces require multi-zone heating to counteract convective end-losses and maintain isothermal flat zones.
        Heating Elements: Kanthal-A1 or Super Kanthal molybdenum disilicide (MoSi2) coils divided into Load, Center, and Source zones.
        PID Control: Triple-loop digital PID controller with feedforward decoupling. Thermocouples (Type R or Type S Platinum-Rhodium) encased in quartz thermowells.
        Temperature Uniformity: Must maintain ±0.5°C across the central 300 mm wafer boat region between 800°C and 1150°C.
        Gas Flow Dynamics: Laminar flow of carrier gases (N2 purge, ultra-pure O2, or forming gas) regulated by mass flow controllers (MFC) at 1 to 5 SLPM.
        Preventing Thermal Shock: Wafer boats must ramp in/out at slow mechanical speed (< 50 mm/minute) to avoid crystallographic slip dislocations.
        """
    },
    {
        "id": "doc-lpcvd-silicon-nitride",
        "title": "Low-Pressure Chemical Vapor Deposition (LPCVD) of Silicon Nitride Hard Masks",
        "source": "Kern & Rosler - Chemically Vapor Deposited Synthetic Materials",
        "category": "Thin Film Deposition",
        "content": """
        Silicon Nitride (Si3N4) serves as an oxidation mask for LOCOS isolation and as dielectric in DRAM storage capacitors.
        Reaction Chemistry: 3 SiH2Cl2 (Dichlorosilane) + 4 NH3 (Ammonia) -> Si3N4 + 6 HCl + 6 H2 at 750°C-800°C.
        Operating Pressure: Hot-wall tube furnace maintained at 200 to 400 mTorr by a chemical-duty mechanical booster roots pump.
        Film Characteristics: Extremely dense, amorphous, refractory film with refractive index n = 2.00 ± 0.02 at 632.8 nm.
        Etch Resistance: Highly resistant to concentrated HF and BOE (etch rate < 0.5 nm/min), etched selectively in hot phosphoric acid (H3PO4 85% at 160°C).
        Stress Control: Intrinsic tensile stress (~1 GPa) managed by optimizing DCS-to-ammonia gas flow ratios to prevent wafer bowing.
        """
    },
    {
        "id": "doc-dram-cell-scaling",
        "title": "180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench",
        "source": "Kang & Leblebici - CMOS Digital Integrated Circuits",
        "category": "DRAM Architecture",
        "content": """
        At the 180nm technology generation, DRAM cells transition toward 8F^2 and 6F^2 folded bitline layouts with stacked capacitor over bitline (COB).
        Unit Cell Geometry: Access transistor channel length L = 180 nm, width W = 220 nm. Bitline contact shared between two adjacent memory cells.
        Stacked Capacitor Topology: Crown-shaped polysilicon or metal-insulator-metal (MIM) structure erected above the drain contact via tungsten plug (W-plug).
        Dielectric Layer: ONO (Oxide-Nitride-Oxide) triple dielectric or Ta2O5 / Al2O3 high-k stack providing effective dielectric constant kappa > 15.
        Capacitance Budget: Minimum 28 fF per cell ensures noise immunity against alpha-particle soft errors and bitline coupling capacitance.
        Leakage Current Target: Sub-threshold and junction leakage must be kept below 1 fA/cell at 85°C to achieve refresh interval of 64 ms for 64 Mb array.
        """
    },
    {
        "id": "doc-thin-film-ellipsometry",
        "title": "Spectroscopic Ellipsometry and Reflectometry for Dielectric Film Metrology",
        "source": "Tompkins & Irene - Handbook of Ellipsometry",
        "category": "Metrology & Testing",
        "content": """
        Non-destructive optical metrology is essential for monitoring oxide, nitride, and photoresist thickness throughout fabrication.
        Physical Principle: Measures the change in light polarization upon reflection from a thin film interface, quantified by angles Psi and Delta.
        Fundamental Equation: rho = r_p / r_s = tan(Psi) * exp(i * Delta), where r_p and r_s are the complex Fresnel reflection coefficients.
        Optical Modeling: Cauchy or Sellmeier dispersion models parameterize refractive index n(lambda) and extinction coefficient k(lambda).
        Measurement Precision: Dry gate oxide (3.5 nm) measured with sub-Angstrom precision (±0.05 nm); photoresist (1.3 um) measured within ±2 nm.
        Wafer Mapping: Automated 9-point or 49-point wafer mapping tracks radial film non-uniformity across spin coating and furnace runs.
        """
    }
]


class SemiconductorCrawler:
    def __init__(self, vector_store: Optional[SemiconductorVectorStore] = None):
        self.store = vector_store or SemiconductorVectorStore()

    def ingest_seed_knowledge(self) -> int:
        """Ingests baseline semiconductor literature into the vector database."""
        count = 0
        for doc in SEED_SEMICONDUCTOR_DOCUMENTS:
            chunks = self._chunk_text(doc["content"], chunk_size=120)
            for idx, chunk in enumerate(chunks):
                chunk_id = f"{doc['id']}_chunk_{idx}"
                meta = {
                    "title": doc["title"],
                    "source": doc["source"],
                    "category": doc["category"],
                    "chunk_index": idx
                }
                self.store.add_document(chunk_id, chunk, meta)
                count += 1
        return count

    def ingest_url(self, url: str, category: str = "Web Crawl") -> int:
        """Fetches and extracts text from a public web page into ChromaDB."""
        with httpx.Client(timeout=15.0, follow_redirects=True) as client:
            resp = client.get(url, headers={"User-Agent": "DRAM-Foundation-Crawler/1.0"})
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            
            # Remove scripts, styles, nav
            for s in soup(["script", "style", "nav", "footer", "header"]):
                s.decompose()
            
            text = soup.get_text(separator="\n", strip=True)
            title = soup.title.string.strip() if soup.title else url

            chunks = self._chunk_text(text, chunk_size=500)
            doc_slug = re.sub(r"[^a-zA-Z0-9]+", "_", url)[:40]
            for idx, chunk in enumerate(chunks):
                chunk_id = f"url_{doc_slug}_{idx}"
                meta = {
                    "title": title,
                    "source": url,
                    "category": category,
                    "chunk_index": idx
                }
                self.store.add_document(chunk_id, chunk, meta)
            return len(chunks)

    def ingest_pdf(self, pdf_path: str, category: str = "Technical Literature") -> int:
        """Extracts text from a local PDF document and indexes into ChromaDB."""
        path = Path(pdf_path)
        if not path.exists():
            raise FileNotFoundError(f"PDF not found at {pdf_path}")
        
        doc = fitz.open(str(path))
        full_text = ""
        for page in doc:
            full_text += page.get_text() + "\n"
        doc.close()

        chunks = self._chunk_text(full_text, chunk_size=500)
        doc_slug = re.sub(r"[^a-zA-Z0-9]+", "_", path.stem)[:40]
        for idx, chunk in enumerate(chunks):
            chunk_id = f"pdf_{doc_slug}_{idx}"
            meta = {
                "title": path.stem,
                "source": str(path.resolve()),
                "category": category,
                "chunk_index": idx
            }
            self.store.add_document(chunk_id, chunk, meta)
        return len(chunks)

    def _chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            if len(chunk.strip()) > 30:
                chunks.append(chunk.strip())
        return chunks

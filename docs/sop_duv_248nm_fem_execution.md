# SOP: DUV 248nm Test Reticle Exposure Matrix (FEM) Execution on 180nm Pilot Wafers

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented
- **Layer & Hierarchy**: Gen 3 (nm) / Foundry Tapeout & PDK / Photolithography

## Overview & Rationale
Execution of Focus-Exposure Matrix (FEM) on 180nm pilot wafers using a DUV 248nm KrF excimer stepper and calibrated 5x test reticle. This establishes the overlapping lithographic process window (ED-tree / Bossung curves) for critical polysilicon gates and contact holes prior to tapeout.

## Process Flow & Operational Steps
1. **Substrate Preparation & Bottom Anti-Reflective Coating (BARC)**:
   - Clean 180nm pilot wafers using standard clean sequence.
   - Coat Bottom Anti-Reflective Coating (BARC) to suppress thin-film optical standing waves at $\lambda = 248\,\text{nm}$.
2. **DUV Chemically Amplified Resist (CAR) Spin & Softbake**:
   - Spin-coat KrF-compatible DUV photoresist.
   - Perform post-apply softbake on an inline precision hotplate.
3. **DUV 248nm Stepper Focus-Exposure Matrix (FEM) Exposure**:
   - Load calibrated 5x test reticle aligned to wafer coordinate system on a $0.005\,\mu\text{m}$ ($5\,\text{nm}$) manufacturing grid.
   - Set Stepper Optical Parameters: Numerical Aperture $\text{NA} = 0.65$, illumination factor $k_1 = 0.40$ yielding minimum resolvable half-pitch $R = k_1 \cdot \frac{\lambda}{\text{NA}} = 152\,\text{nm}$.
   - Program a 2D Focus-Exposure Matrix (FEM) array across stepping dies:
     - **Focus Axis**: Step across focus offsets centered around nominal focal plane, validating depth of focus $\text{DOF} = k_2 \cdot \frac{\lambda}{\text{NA}^2} \ge 0.5\,\mu\text{m}$ ($500\,\text{nm}$).
     - **Dose / Exposure Energy Axis**: Vary exposure dose incrementally across columns.
4. **Post-Exposure Bake (PEB) & Track Development**:
   - Perform precision PEB to activate photoacid-catalyzed deprotection.
   - Develop wafer in standard developer chemistry; perform deionized (DI) water rinse and spin-dry.
5. **Metrology & Bossung Window Extraction**:
   - Measure Critical Dimensions (CD) on CD-SEM across matrix dies.
   - Measure gate-to-active overlay errors.
   - Construct Bossung plots and define nominal dose/focus center.

## Acceptance Criteria
- **Minimum Poly Gate Critical Dimension (CD)**: Target $0.15\,\mu\text{m}$ ($150\,\text{nm}$) nominal (minimum spacing $\ge 0.21\,\mu\text{m}$).
- **Minimum Contact Hole Dimension**: Target $0.17\,\mu\text{m} \times 0.17\,\mu\text{m}$ ($170\,\text{nm} \times 170\,\text{nm}$).
- **Usable Depth of Focus (DOF)**: $\text{DOF} \ge 0.5\,\mu\text{m}$ ($500\,\text{nm}$).
- **Poly Gate-to-Active Overlay Error**: Overlay registration error $\le 35\,\text{nm}$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- SkyWater SKY130 Open PDK Design Rules & Lithography Grid

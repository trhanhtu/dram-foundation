# ATE Shmoo Raw Vector Parsing & Pass/Fail Surface Extraction

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Implemented

## Overview & Rationale
Captures the operating principles and automated parsing pipeline for converting raw Automated Test Equipment (ATE) vector datalogs into 2D/3D Pass/Fail operating boundary surfaces ($V_{DD}$ vs. Frequency $f_{CK}$ vs. Temperature $T$). Evaluates physical storage margins ($C_s \ge 28\ \text{fF}$, $L=180\ \text{nm}$, $W=220\ \text{nm}$) and JEDEC DDR speed binning operating margins ($1.8\ \text{V} \pm 10\%$, DDR-266/DDR-333) for 180nm open-source DRAM chips.

## Key Details / Architecture
- Raw ASCII/STIL/WGL datalog stream ingestion and tokenization.
- 2D grid matrix reconstruction ($V_{DD}$ steps $\le 20\ \text{mV}$, $f_{CK}$ steps $\le 2\ \text{MHz}$).
- Marching squares / bilinear interpolation for 0.5 isocline boundary extraction.
- JEDEC operating margin calculation ($V_{DD,\min} \le 1.45\ \text{V}$ at $133\ \text{MHz}$, $f_{\max} \ge 146.3\ \text{MHz}$ at $1.62\ \text{V}$).
- Automated export to structured CSV and HDF5 formats.

## References & Related Files
- [docs/sop_ate_shmoo_raw_vector_parsing_pass_fail_surface_extraction.md](./docs/sop_ate_shmoo_raw_vector_parsing_pass_fail_surface_extraction.md)
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/knowledge/shmoo_validation_pipeline.md](./docs/knowledge/shmoo_validation_pipeline.md)
- [docs/knowledge/trcd_shmoo_margin_metrology.md](./docs/knowledge/trcd_shmoo_margin_metrology.md)

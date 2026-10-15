# Automated Shmoo Operating Window Confidence Validator and Metrology Reporting Pipeline

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Automates the validation of the 2D $V_{DD}$ vs. Retention Time Shmoo operating window for 180nm folded bitline DRAM cells ($8F^2$, $0.259\ \mu\text{m}^2$). The pipeline extracts pass/fail boundary curves, validates signal margin against cell capacitance budgets ($C_s \ge 28\ \text{fF}$, $C_b = 150\text{--}250\ \text{fF}$, $C_b/C_s \in [5:1, 9:1]$) and junction/subthreshold leakage targets ($\le 1.0\ \text{fA/cell}$ at $85^\circ\text{C}$), generating an automated metrology compliance certificate.

## Key Details / Architecture
- Ingestion of ESP32 UART/telemetry test matrices over the 2D grid.
- Bilinear/spline boundary contour interpolation at 50% bit-error cutoffs.
- Signal read margin confidence scoring based on charge sharing equations $\Delta V_{BL} = \frac{V_{DD}/2}{1 + C_b/C_s}$.
- Thermal boundary correlation ensuring test chamber / wafer chuck aligns with isothermal limits.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/knowledge/sop_shmoo_validation_pipeline.md](./docs/knowledge/sop_shmoo_validation_pipeline.md)

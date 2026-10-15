# Spatial Clustering and Die-Level Defect Binning Algorithm Development

- **Date**: 2026-10-15
- **Source**: Agent
- **Status**: Implemented

## Overview & Rationale
Extracts spatial defect coordinates from wafer inspection metrology (KLARF outputs post-CMP and lithography) for the 180nm Open-Source DRAM node (DRAM Foundation VN / SkyWater SKY130 compatible). Implements density-based spatial clustering (DBSCAN) aligned to the foundry physical grid, followed by shape/signature classification (micro-scratches, slurry puddle residue, ring signatures) to evaluate die-level yield impact on stacked capacitor and interconnect structures.

## Key Details / Architecture
- **Coordinate Grid Alignment**: Snapped to SkyWater SKY130 manufacturing grid ($0.005\,\mu\text{m}$ / $5\,\text{nm}$).
- **Clustering Neighborhood Metric**: Density reachability $\epsilon$ calibrated to critical interconnect pitch ($0.34\,\mu\text{m}$ M1 pitch) and minimum contact feature ($0.17\,\mu\text{m} \times 0.17\,\mu\text{m}$).
- **Binning Categories**:
  - Bin 1: Random isolated point defects (background noise).
  - Bin 2: High-aspect CMP micro-scratches (line trajectory).
  - Bin 3: Slurry / rinse puddle clusters (areal concentration).
  - Bin 4: Edge exclusion / bevel peel clusters.
- **Yield Attribution**: Die kill-ratio mapped against active DRAM array ($L=180\,\text{nm}, W=220\,\text{nm}$, cell area $8F^2/6F^2$) and periphery logic.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)

# Statistical In-Line Gate CD Extraction & Charging-Induced Shrinkage Analysis

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Council)
- **Status**: Implemented

## Overview & Rationale
In 180nm DRAM cell fabrication using Electron Beam Direct Write (EBDW) and polysilicon gate patterning, in-line Critical Dimension Scanning Electron Microscopy (CD-SEM) metrology is prone to charging artifacts and resist/feature shrinkage under continuous electron bombardment. To achieve accurate physical gate length extraction ($L = 180\text{ nm}$ nominal, bitline/wordline pitch $360\text{ nm}$ to $400\text{ nm}$), statistical multi-frame decay modeling is used to extrapolate true pre-exposure dimension ($CD_0$) while mitigating dielectric charging across high-density cell arrays.

## Key Details / Architecture
- **Target Cell Geometry**: Access transistor channel length $L = 180\text{ nm}$, access width $W = 220\text{ nm}$, gate dielectric physical thickness $\sim 3.5\text{ nm}$ dry $\text{SiO}_2$.
- **Array Pitch**: Dense memory array wordline pitch $360\text{ nm} - 400\text{ nm}$.
- **Metrology Beam Control**: Ultra-low landing energy beam ($300\text{ eV} - 500\text{ eV}$) with beam current $8\text{ pA} - 15\text{ pA}$.
- **Shrinkage Compensation**: Multi-frame scan acquisition ($N = 16, 32, 64$) fitted to exponential decay $CD(D) = CD_\infty + \Delta CD \cdot e^{-k \cdot D}$ to mathematically recover unbiased initial gate dimension $CD_0$.

## References & Related Files
- [docs/context.yaml](./docs/context.yaml)
- [docs/context2.yaml](./docs/context2.yaml)
- [docs/context3.yaml](./docs/context3.yaml)

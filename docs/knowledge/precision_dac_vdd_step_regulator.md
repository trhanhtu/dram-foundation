# Precision DAC VDD Step Regulator & Control Interface Architecture

- **Date**: 2026-10-15
- **Source**: Agent (DRAM Foundation VN Domain Expert)
- **Status**: Proposed

## Overview & Rationale
For automated $V_{DD}$ vs. retention time shmoo telemetry across a 180nm DRAM testbed, a programmable, low-noise stepped supply regulator is required. The nominal core voltage is $V_{DD} = 1.8\text{ V}$. Because threshold voltage loss ($V_{th} \approx 0.5\text{ V} - 0.6\text{ V}$) without overdrive or during voltage-scaling characterization degrades sensing margins ($\Delta V \approx 100\text{ mV} - 150\text{ mV}$ at nominal $C_s \ge 28\text{ fF}$, $C_{BL} \approx 250\text{ fF}$), the regulator must sweep $V_{DD}$ from $1.0\text{ V}$ to $2.2\text{ V}$ in discrete, sub-millivolt increments while maintaining ripple below $5\text{ mV}_{p-p}$ and settling within $50\ \mu\text{s}$.

## Key Details / Architecture
- **Control Interface**: ESP32 SPI bus commanding a 16-bit low-drift DAC (e.g., AD5662 / DAC8562 or equivalent) with 2.5V precision bandgap reference.
- **Analog Front-End / Output Stage**:
  - Closed-loop op-amp with high bandwidth and Kelvin sensing routed directly to the DRAM DUT power pins to eliminate $I \cdot R$ drop.
  - Low-dropout P-channel power stage rated for $> 500\text{ mA}$ continuous current with low ESR ceramic bypass network ($10\ \mu\text{F} \parallel 100\text{ nF} \parallel 1\text{ nF}$).
- **Target Metrics**:
  - Voltage dynamic range: $1.0\text{ V}$ to $2.2\text{ V}$.
  - Resolution step: $\le 1\text{ mV}$ per LSB.
  - Settling time: $\le 50\ \mu\text{s}$ to within $\pm 0.1\%$ of target step.
  - High-frequency output ripple/noise: $\le 5\text{ mV}_{p-p}$ across $10\text{ Hz} - 20\text{ MHz}$.

## References & Related Files
- [docs/context.yaml](.../../context.yaml)
- [docs/context2.yaml](.../../context2.yaml)

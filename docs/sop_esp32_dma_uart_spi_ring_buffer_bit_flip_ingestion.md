# Standard Operating Procedure (SOP)
## ESP32 DMA UART/SPI Ring-Buffer Pipeline Architecture for Bit-Flip Stream Ingestion

- **Document ID**: SOP-DES-DRAM180-ESP32-DMA-001
- **Process Generation**: Gen 2 (180nm / µm)
- **Action Type**: Make
- **Status**: Released / Operational

---

### 1. Scope & Objective
This SOP specifies the architectural implementation and hardware/firmware execution protocol for an ESP32 Direct Memory Access (DMA) high-speed UART/SPI ring-buffer ingestion pipeline. The system acquires high-throughput continuous bit-flip telemetry generated during parametric retention tests and March C- diagnostic runs on the 180nm Open-Source DRAM Chip ($F = 180\text{ nm}$, folded bitline $8F^2$, $C_s \ge 28\text{ fF}$). The pipeline prevents hardware FIFO overrun, guarantees zero-loss ingestion, and feeds timestamped bit-flip loggers for real-time retention fault localization.

---

### 2. Relevant Sources & Physical Context
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
  - Access transistor channel length $L = 180\text{ nm}$, width $W = 220\text{ nm}$.
  - Stacked capacitor (COB) crown polysilicon / MIM structure over tungsten plug (W-plug).
  - High-$\kappa$ / ONO dielectric stack ($\kappa > 15$).
  - Storage node capacitance budget $C_s \ge 28\text{ fF}$ per cell.
  - Sub-threshold and junction leakage target $< 1\text{ fA/cell}$ at $85^\circ\text{C}$ to maintain required refresh and retention boundaries.
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
  - Folded bitline $8F^2$ footprint (unit cell area $0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$) providing common-mode noise rejection.
  - Storage node capacitance $C_s = 25\text{ to }30\text{ fF}$ (nominally $28\text{ fF}$).
  - Array block configuration: 256 or 512 cells per bitline with bitline parasitic capacitance $C_b = 150\text{ to }250\text{ fF}$.
  - Capacitance ratio constraint: $C_b / C_s$ maintained strictly between $5:1$ and $9:1$ (must not exceed $10:1$ to prevent read margin collapse).
- **SkyWater 130nm Open PDK Overview & Architecture**:
  - Mixed-signal embedded microcontroller interface principles and digital cell library timing boundaries for open-source silicon metrology.

---

### 3. Architecture & Dataflow Overview

```text
┌────────────────────────────────────────────────────────┐
│  180nm DRAM Array (8F^2, 1T1C, Cs >= 28 fF, Cb/Cs 5-9) │
└───────────────────────────┬────────────────────────────┘
                            │ Bit-Flip Event Telemetry
                            ▼
┌────────────────────────────────────────────────────────┐
│      ESP32 Dual-Peripheral Ingestion Engine            │
│   - HS-SPI Slave (up to 40 MHz) / UART (up to 5 Mbps)  │
└───────────────────────────┬────────────────────────────┘
                            │ Autonomous DMA Engine
                            ▼
┌────────────────────────────────────────────────────────┐
│        SRAM Internal DMA Ping-Pong Descriptors         │
│   - Linked-List Circular Descriptors (2 KB - 4 KB/blk) │
└───────────────────────────┬────────────────────────────┘
                            │ Hardware ISR (EOF / Queue)
                            ▼
┌────────────────────────────────────────────────────────┐
│   FreeRTOS Double-Buffered Ring-Buffer Task (Core 0)   │
│   - Lockless Head/Tail Pointers (64 KB - 128 KB Ring)  │
└───────────────────────────┬────────────────────────────┘
                            │ Zero-Copy Telemetry Stream
                            ▼
┌────────────────────────────────────────────────────────┐
│   Telemetry Metrology & Retention Logger (Core 1)      │
│   - Timestamped Bit-Flip Classification & March C- Map │
└────────────────────────────────────────────────────────┘
```

---

### 4. Step-by-Step Implementation Procedure

#### Step 4.1: ESP32 Hardware Pinout & Peripheral Configuration
1. Connect physical telemetry signal lines from the 180nm DRAM testing board / FPGA pattern generator to designated ESP32 General Purpose I/O pins:
   - **SPI Ingestion Path**:
     - `SCLK`: GPIO 18 (Input, pull-down enabled).
     - `MOSI`: GPIO 23 (Data stream input).
     - `CS#`: GPIO 5 (Chip-select / frame synchronization strobe).
     - `READY_HANDSHAKE`: GPIO 22 (Output push-pull to test controller).
   - **UART Ingestion Path (Alternative / Redundant Telemetry)**:
     - `U2_RXD`: GPIO 16 (Hardware Flow Control `RTS`/`CTS` mapped to GPIO 17 / GPIO 19).
2. Configure peripheral clock domains:
   - Set SPI Peripheral (`SPI2_HOST` / `HSPI`) as SPI Slave supporting bus clock frequencies up to $40\text{ MHz}$.
   - Set UART2 baud rate to $3.0\text{ Mbps}$ (or up to $5.0\text{ Mbps}$ with hardware auto-flow control enabled).

#### Step 4.2: DMA Descriptor Chain & SRAM Ring-Buffer Allocation
1. Allocate memory in internal SRAM accessible by the DMA controller (using `MALLOC_CAP_DMA | MALLOC_CAP_INTERNAL`):
   - Allocate dual ping-pong hardware DMA buffers: Size $B_{dma} = 4096\text{ bytes}$ per block (aligned to 32-bit boundary).
2. Initialize circular linked-list `lldesc_t` descriptors:
   - Configure Descriptor 0 pointing to `Buffer_A` and linking to Descriptor 1.
   - Configure Descriptor 1 pointing to `Buffer_B` and linking back to Descriptor 0 (forming an autonomous infinite ring).
   - Set descriptor attributes: `eof = 1`, `owner = 1` (hardware managed), `size = 4096`, `length = 0`.
3. Allocate secondary software ring-buffer in Internal SRAM / SPIRAM:
   - Ring capacity: $N_{ring} = 131072\text{ bytes}$ ($128\text{ KB}$ lockless circular buffer with atomic head and tail pointers).

#### Step 4.3: Interrupt Service Routine (ISR) & Zero-Copy Event Dispatch
1. Register low-latency DMA transfer completion interrupt:
   - Bind `spi_slave_hd_isr` or `uart_rx_dma_isr` with `ESP_INTR_FLAG_IRAM` allocation flag.
2. In the ISR:
   - Read DMA transfer length register upon buffer EOF trigger.
   - Dispatch buffer reference pointer to FreeRTOS Queue (`xQueueSendFromISR`) without memory-to-memory copy.
   - Re-arm the complementary DMA descriptor slot to prevent peripheral receiver stall.

#### Step 4.4: Multi-Core Pipeline & FreeRTOS Stream Processing
1. Pin the Ring-Buffer Ingestion Task to Core 0 with real-time priority (`configMAX_PRIORITIES - 2`):
   - Ingest DMA ping-pong buffers into the circular ring-buffer.
   - Maintain write pointer $P_{write} = (P_{write} + L_{chunk}) \pmod{N_{ring}}$.
   - Detect overrun condition if $(P_{write} - P_{read}) \ge N_{ring} - B_{dma}$ and raise hardware backpressure signal on GPIO 22.
2. Pin the Parsing & Logging Task to Core 1:
   - Read binary telemetry frames consisting of:
     - 64-bit Hardware Microsecond Timestamp ($T_{us}$).
     - 16-bit Row Address ($0 \le \text{Row} < 512$ per sub-block).
     - 16-bit Column Address ($0 \le \text{Col} < 512$).
     - 8-bit Expected Value vs. Actual Readout (Fault vector: Stuck-At $0/1$, Transition, or Leakage Decay).
   - Correlate bit-flip addresses with known array capacitance ratio regions ($C_b / C_s$ range $5:1$ to $9:1$) to flag anomalous weak cells where $C_s < 28\text{ fF}$ or leakage exceeds $1\text{ fA/cell}$.

#### Step 4.5: Pipeline End-to-End Stress Test & Metrology Validation
1. Inject synthetic burst bit-flip streams from pattern generator at $10\text{ MB/s}$ continuous throughput.
2. Monitor DMA descriptor stall cycles, FreeRTOS queue depth, and dropped packet counters over a 60-minute duration.
3. Validate telemetry integrity against the golden pattern.

---

### 5. Acceptance Criteria & Target Metrics

| Parameter / Metric | Physical Target Value | Validation Tolerance | Measurement Method |
| :--- | :--- | :--- | :--- |
| **Max Ingestion Throughput** | $\ge 20.0\text{ Mbit/s}$ (SPI/UART DMA) | $\pm 0.5\text{ Mbit/s}$ | Logic Analyzer bus decode & hardware timestamp delta |
| **Packet / Frame Loss Rate** | $0\text{ frames lost}$ (Zero drop) | Exactly $0.00\%$ loss over $1.0\times 10^7$ frames | Frame sequence counter continuity audit in ring buffer |
| **DMA Buffer Switching Latency** | $\le 1.8\ \mu\text{s}$ | $\pm 0.2\ \mu\text{s}$ | Oscilloscope trigger on DMA ISR entry to descriptor reload |
| **Ring-Buffer Fill Headroom** | $\ge 40.0\%$ reserved margin | $\pm 5.0\%$ under $10\text{ MB/s}$ burst load | Core 0 FreeRTOS watermark memory profile monitor |

---

### 6. Safety, Signal Integrity & Risk Controls
- **Signal Reflections**: Terminate SPI clock line with $33\ \Omega$ series damping resistor at the transmitter to suppress overshoot and ringing at frequencies $> 20\text{ MHz}$.
- **Memory Collision**: Keep DMA buffers strictly in 32-bit aligned internal SRAM (`MALLOC_CAP_DMA`); never map DMA targets directly to external PSRAM cache lines without explicit cache writeback and invalidation primitives.
- **Backpressure Fail-Safe**: If ring-buffer occupancy exceeds $85\%$, assert the physical `READY_HANDSHAKE` low within $500\text{ ns}$ to pause testbench clocking and prevent unlogged DRAM retention bit-flips.

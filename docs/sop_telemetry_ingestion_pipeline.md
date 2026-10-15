# SOP: High-Throughput UART/SPI Telemetry Ingestion Pipeline & Error Frame Parser

- **Document ID**: SOP-MET-DRAM-002
- **Author**: Domain Expert AI (DRAM Foundation VN)
- **Hierarchy Context**: 180nm Open-Source DRAM Chip (DRAM Foundation VN) [Architecture & Integration] > ESP32 Closed-Loop Motor Controller [Electronics & Firmware] > Automated VDD vs Retention Time Shmoo Plot Telemetry Engine [Firmware & Software] > Variable Retention Pause & March Pattern Bit-Flip Audit Firmware [Firmware & Software] > Bit-Flip Error Telemetry Ingestion & Retention Failure Bitmap Metrology [Metrology] > High-Throughput UART/SPI Telemetry Ingestion Pipeline & Error Frame Parser [Metrology]
- **Generation**: Gen 2 (µm) / 180nm CMOS
- **Date**: 2026-10-15
- **Status**: Accepted

---

## 1. Scope & Objective
Establish a high-speed ingestion and deterministic parsing protocol to capture streaming bit-flip failure telemetry from an ESP32 DRAM testing controller. The pipeline ingests UART/SPI diagnostic error frames, verifies frame integrity via cyclic redundancy checks (CRC32), unpacks failed address locations, and streams error vectors to the retention failure bitmap metrology engine for 180nm 1T1C stacked-capacitor arrays.

---

## 2. Hardware & Protocol Specification

| Parameter | Specification | Physical Context / Derivation |
| :--- | :--- | :--- |
| **Physical Interface** | High-speed UART (FTDI FT232H / USB-CDC) / SPI Master-Slave | Decoupled host-testbed link |
| **Baud Rate / SCLK** | UART: 921,600 baud (8-N-1); SPI: 10.0 MHz | Minimizes FIFO overrun during burst refresh failures |
| **Framing Encapsulation** | COBS (Consistent Overhead Byte Stuffing) + 0x00 Delimiter | Zero-byte framed boundary recovery |
| **Array Geometry Target** | 180nm folded bitline ($8F^2$, cell area $0.259\,\mu\text{m}^2$) | Wordline/Bitline address mapping |
| **Cell Capacitance Target** | $C_s \ge 28\,\text{fF}$, $C_b = 150\text{--}250\,\text{fF}$ ($C_b / C_s \le 9:1$) | Baseline storage budget per audited node |

---

## 3. Step-by-Step Operating Procedure

### Step 1: Physical Link & DMA Ring Buffer Initialization
1. Establish physical connection between ESP32 telemetry pins and Host Ingestion Interface:
   - For UART: TXD to Host RXD, RXD to Host TXD, GND common return.
   - Set Host UART line discipline to 921,600 baud, 8 data bits, no parity, 1 stop bit (8-N-1).
2. Allocate circular ring buffer in host memory ($64\,\text{KB}$ contiguous FIFO).
3. Bind non-blocking asynchronous DMA/I/O interrupt handlers to pump incoming serial byte streams directly into the circular buffer.

### Step 2: Stream Delimitation & COBS Framing Extraction
1. Poll ring buffer read pointer against write pointer.
2. Scan for frame delimiter byte `0x00`.
3. Extract raw packet payload between sequential `0x00` markers.
4. Execute in-place COBS (Consistent Overhead Byte Stuffing) decoding to restore original unencoded bytes:
   - Packet structure: `[LEN (1B)][FLAGS (1B)][CYCLE_ID (4B)][VDD_MV (2B)][ROW_ADDR (2B)][COL_ADDR (2B)][EXP_DATA (1B)][ACT_DATA (1B)][CRC32 (4B)]`.

### Step 3: Checksum Validation & CRC32 Rejection Gate
1. Compute IEEE 802.3 CRC32 polynomial ($0x04C11DB7$) over payload bytes `0` through `N-5`.
2. Compare computed CRC32 against received 4-byte CRC32 field at offset `N-4`:
   - If CRC matches: Pass frame to the Metrology Ingestion Dispatcher.
   - If CRC mismatches: Increment `Corrupt_Frame_Counter`, drop payload, and resynchronize at next `0x00` delimiter.

### Step 4: Bit-Flip Error Vector Parsing & Coordinate Mapping
1. Extract Row Address (`ROW_ADDR`) and Column Address (`COL_ADDR`) corresponding to 180nm array architecture ($L = 180\,\text{nm}, W = 220\,\text{nm}$).
2. Compute failing bit mask: `ERROR_MASK = EXP_DATA ^ ACT_DATA`.
3. Normalize logical coordinates to physical $8F^2$ Folded Bitline matrix coordinates ($0.259\,\mu\text{m}^2$ cell footprint).
4. Dispatch bit-flip failure tuple `(CYCLE_ID, VDD_MV, ROW, COL, ERROR_MASK)` into downstream Bitmap Metrology Ring (`Retention Failure Bitmap Store`).

---

## 4. Acceptance Criteria & Target Metrics

1. **Telemetry Ingestion Throughput**: Continuous sustained transfer $\ge 90\,\text{kB/s}$ over UART (at 921,600 baud) and $\ge 1.0\,\text{MB/s}$ over SPI (at 10.0 MHz) without kernel buffer drops.
2. **Buffer Overrun / Frame Drop Rate**: $\le 0.001\%$ ($< 1$ dropped frame per $100,000$ transmitted failure frames) under continuous burst bit-flip activity.
3. **CRC32 Error Rejection Latency**: Frame parsing and integrity check execution time $\le 15\,\mu\text{s}$ per 18-byte telemetry frame on host CPU.
4. **Coordinate Mapping Fidelity**: $100.0\%$ bitline-to-wordline coordinate alignment verification across physical $8F^2$ array boundaries without coordinate inversion.

---

## 5. Verified Literature Citations
- **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**: Folded bitline $8F^2$ cell area ($0.259\,\mu\text{m}^2$ at $F = 180\,\text{nm}$); storage capacitance $C_s \ge 28\,\text{fF}$; bitline parasitic capacitance $C_b = 150\text{--}250\,\text{fF}$; $C_b/C_s$ maintained between $5:1$ and $9:1$.
- **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**: Unit cell geometry $L = 180\,\text{nm}$, $W = 220\,\text{nm}$; minimum $28\,\text{fF}$ per cell budget; leakage target $< 1\,\text{fA/cell}$ at $85^\circ\text{C}$.
- **SkyWater 130nm Open PDK Overview & Architecture**: Open-source EDA tooling integration, design rule validation, and open process verification paradigms.

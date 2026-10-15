* ==============================================================================
* 180nm 1T1C DRAM Bitcell Sensing Margin & Full-Rail Restoration Transient Deck
* Process: Generic 180nm Bulk CMOS / Embedded DRAM Stacked MIM Capacitor
* Key Physical Parameters:
*   Cs   = 28 fF (Stacked High-k Crown Capacitor)
*   Cbl  = 150 fF (Folded Bitline Parasitic, 256 cells/column)
*   VDD  = 1.8 V (Core Logic Supply)
*   VEQ  = 0.9 V (Bitline Half-VDD Precharge)
*   VPP  = 2.8 V (Boosted Wordline Overdrive for non-degraded Vt pass)
* ==============================================================================

.include "dram_1t1c_cell.sp"
.include "sense_amp_folded.sp"

* -------------------------------------------------------------
* 1. 180nm Generic Predictive BSIM / Level-3 MOS Transistor Models
* -------------------------------------------------------------
.model NMOS_180 NMOS (
+ LEVEL=3
+ VTO=0.55 KP=180u GAMMA=0.45 PHI=0.65 TOX=4.0n
+ NSUB=1.2e17 XJ=0.15u LD=0.03u CJ=1.0m CJSW=0.35n
+ CGSO=0.35n CGDO=0.35n THETA=0.08 VMAX=1.5e5)

.model PMOS_180 PMOS (
+ LEVEL=3
+ VTO=-0.58 KP=65u GAMMA=0.48 PHI=0.65 TOX=4.0n
+ NSUB=1.4e17 XJ=0.15u LD=0.03u CJ=1.2m CJSW=0.40n
+ CGSO=0.35n CGDO=0.35n THETA=0.12 VMAX=1.2e5)

* -------------------------------------------------------------
* 2. DC Bias Supplies & Reference Levels
* -------------------------------------------------------------
VDD  VDD_NODE 0 DC 1.8
VSS  VSS_NODE 0 DC 0.0
VEQ  VEQ_NODE 0 DC 0.9
VCP  VCP_NODE 0 DC 0.9

* -------------------------------------------------------------
* 3. Bitline Distributed Parasitic Capacitance (150 fF)
* -------------------------------------------------------------
C_BL   BL     0 150f
C_BLB  BL_BAR 0 150f

* -------------------------------------------------------------
* 4. 1T1C Storage Bitcell (Initialized with Data '1': V(SN) = 1.8V)
* -------------------------------------------------------------
XCELL1 BL WL VCP_NODE dram_1t1c_cell

* -------------------------------------------------------------
* 5. Folded Sense Amplifier & Equalizer Instance
* -------------------------------------------------------------
XSA BL BL_BAR SAN SAP EQ VEQ_NODE VDD_NODE VSS_NODE sense_amp_folded

* -------------------------------------------------------------
* 6. Transient Control Stimuli
* -------------------------------------------------------------
* Equalization signal (Active high during precharge phase)
* High (1.8V) from 0 to 1.0ns, drops to 0V at 1.2ns, returns to 1.8V at 7.0ns
V_EQ EQ 0 PWL(0ns 1.8V  1.0ns 1.8V  1.2ns 0.0V  7.0ns 0.0V  7.2ns 1.8V 10.0ns 1.8V)

* Wordline drive signal (Boosted overdrive VPP = 2.8V)
* Low (0V) until 2.0ns, ramps to 2.8V at 2.2ns, returns to 0V at 6.0ns
V_WL WL 0 PWL(0ns 0.0V  2.0ns 0.0V  2.2ns 2.8V  6.0ns 2.8V  6.2ns 0.0V 10.0ns 0.0V)

* SAN (N-Sense Strobe): Precharged to VEQ=0.9V, strobes to 0V at 3.0ns
V_SAN SAN 0 PWL(0ns 0.9V  2.8ns 0.9V  3.0ns 0.9V  3.3ns 0.0V  6.8ns 0.0V  7.1ns 0.9V 10.0ns 0.9V)

* SAP (P-Sense Strobe): Precharged to VEQ=0.9V, strobes to 1.8V at 3.2ns
V_SAP SAP 0 PWL(0ns 0.9V  3.0ns 0.9V  3.2ns 0.9V  3.5ns 1.8V  6.8ns 1.8V  7.1ns 0.9V 10.0ns 0.9V)

* -------------------------------------------------------------
* 7. Initial Conditions & Transient Execution
* -------------------------------------------------------------
.ic V(BL)=0.9V V(BL_BAR)=0.9V V(XCELL1.SN)=1.8V V(SAN)=0.9V V(SAP)=0.9V
.tran 5ps 10ns UIC

* -------------------------------------------------------------
* 8. Automated Margin & Timing Signoff Measurements
* -------------------------------------------------------------
* Measure bitline differential voltage prior to sense amp strobe (Charge-sharing delta)
.meas tran V_BL_PRE_SENSE FIND V(BL) AT=2.95ns
.meas tran V_BLB_PRE_SENSE FIND V(BL_BAR) AT=2.95ns
.meas tran DELTA_V_SENSE PARAM='V_BL_PRE_SENSE - V_BLB_PRE_SENSE'

* Measure final restored voltage on bitline at end of sensing
.meas tran V_BL_RESTORED FIND V(BL) AT=5.5ns
.meas tran V_BLB_RESTORED FIND V(BL_BAR) AT=5.5ns

* Sensing latency: time from SAN activation (3.0ns) to 90% rail separation (1.62V)
.meas tran T_SENSE TRIG V(SAN) VAL=0.45 FALL=1 TARG V(BL) VAL=1.62 RISE=1

.end

* Folded Bitline CMOS Cross-Coupled Sense Amplifier & Equalizer
* Foundry Target: 180nm CMOS Periphery (VDD = 1.8V, VEQ = 0.9V)
* Matches open-array / folded-bitline layout pitch boundary

.subckt sense_amp_folded BL BL_BAR SAN SAP EQ VEQ VDD VSS
* Ports:
*   BL     - True bitline
*   BL_BAR - Complementary reference bitline
*   SAN    - N-Sense amplifier drive line (strobed to VSS = 0V)
*   SAP    - P-Sense amplifier drive line (strobed to VDD = 1.8V)
*   EQ     - Equalize/Precharge gate control
*   VEQ    - Bitline precharge voltage (VDD/2 = 0.9V)
*   VDD    - Core supply voltage (1.8V)
*   VSS    - Core ground (0V)

* -------------------------------------------------------------
* 1. Equalizer / Precharge Circuitry
* -------------------------------------------------------------
* Cross-bitline equalization transistor
MEQ_BRIDGE BL EQ BL_BAR VSS NMOS_180 W=440n L=180n
* Bitline pull to VEQ (0.9V)
MEQ_BL     BL EQ VEQ VSS    NMOS_180 W=360n L=180n
MEQ_BLB    BL_BAR EQ VEQ VSS NMOS_180 W=360n L=180n

* -------------------------------------------------------------
* 2. Cross-Coupled NMOS Sensing Pair (N-Latch)
* -------------------------------------------------------------
* Gates cross-connected: MN1 gate driven by BL_BAR, MN2 gate driven by BL
MN1 BL     BL_BAR SAN VSS NMOS_180 W=500n L=180n
MN2 BL_BAR BL     SAN VSS NMOS_180 W=500n L=180n

* -------------------------------------------------------------
* 3. Cross-Coupled PMOS Restoration Pair (P-Latch)
* -------------------------------------------------------------
* Gates cross-connected: MP1 gate driven by BL_BAR, MP2 gate driven by BL
MP1 BL     BL_BAR SAP VDD PMOS_180 W=1000n L=180n
MP2 BL_BAR BL     SAP VDD PMOS_180 W=1000n L=180n

.ends sense_amp_folded

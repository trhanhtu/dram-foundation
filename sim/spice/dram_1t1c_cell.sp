* 180nm 1T1C DRAM Storage Bitcell Model
* Foundry Target: 180nm Mixed-Signal / Embedded DRAM Rule Deck
* Cell Area: ~0.28 um^2 (Folded Bitline architecture)

.subckt dram_1t1c_cell BL WL VCP
* Nodes:
*   BL  - Bitline connection
*   WL  - Wordline gate input (driven to VPP=2.8V for access)
*   VCP - Cell plate reference (typically VDD/2 = 0.9V)
*
* M_ACCESS: NMOS Access Pass Transistor
* W=220nm, L=180nm, with junction capacitance and body effect
M_ACCESS BL WL SN VSS NMOS_180 W=220n L=180n AS=0.088p PS=1.24u AD=0.088p PD=1.24u

* C_CELL: Stacked Crown / Deep Trench Storage Capacitor (28 fF)
* High-k Al2O3/Ta2O5 dielectric MIM capacitor
C_CELL SN VCP 28f IC=1.8V

* R_LEAK: Sub-threshold & dielectric leakage path to substrate (R > 100 T-ohm)
R_LEAK SN 0 100T

.ends dram_1t1c_cell

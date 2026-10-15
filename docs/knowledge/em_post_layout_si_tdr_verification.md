# 2.5D/3D EM Post-Layout Signal Integrity & Differential TDR Impedance Verification

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN multi-agent council)
- **Status**: Implemented

## Overview & Rationale
Post-layout high-speed electromagnetic (2.5D/3D EM) and Time-Domain Reflectometry (TDR) impedance verification ensures physical fidelity of the 180nm DRAM ATE loadboard interface prior to fabrication and test-head docking. Discontinuities at microstrip-to-stripline layer transitions, via antipads, socket pads, and differential pair routings (Clock, DQS) cause excessive reflection, insertion loss, and skew that directly degrade JEDEC DDR speed-bin qualification and HTOL burn-in characterization.

## Key Details / Architecture
- **Layer & Interconnect Discontinuity Modeling**: 3D full-wave FEM/BEM electromagnetic extraction of critical breakout zones, BGA/socket pogo pin footprints, and via transitions.
- **Differential & Single-Ended Impedance**: Differential TDR extraction targeting $100\ \Omega \pm 10\%$ ($90\ \Omega\text{ to }110\ \Omega$) on clock/DQS pairs and single-ended $50\ \Omega \pm 10\%$ ($45\ \Omega\text{ to }55\ \Omega$) on DQ/Address lines under $35\text{ ps}$ step excitation.
- **Signal Integrity & Noise Constraints**: Far-end crosstalk (FEXT) $\le -35\text{ dB}$, return loss $S_{11} \le -15\text{ dB}$, and differential insertion loss $S_{dd21} \ge -1.5\text{ dB}$ across operating Nyquist bandwidth.
- **Electrical Verification Against 180nm Physical Budgets**: Preserves 180nm device limits including $V_{\text{DS}} = 1.8\text{ V}$ I/O swing, $V_{\text{thn}} = 0.55\text{ V}$, cell storage capacitance margin ($\ge 28\text{ fF}$ budget), and pin parasitic limits.

## References & Related Files
- [docs/knowledge/ate_dut_loadboard_routing_sop.md](./docs/knowledge/ate_dut_loadboard_routing_sop.md)
- [docs/sop_ate_pin_electronics_channel_deskew_tdr_fixture_calibration.md](./docs/sop_ate_pin_electronics_channel_deskew_tdr_fixture_calibration.md)
- [docs/context.yaml](./docs/context.yaml)

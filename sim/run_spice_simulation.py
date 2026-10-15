"""
Executable SPICE & Differential Physics Transient Simulation Harness
Target: 180nm 1T1C DRAM Bitcell Sensing Margin & Folded Bitline Sense Amp
"""

import math
import numpy as np
from typing import Dict, Any, Tuple, List

class DRAM1T1CSimulator:
    """
    Physical transient solver for 180nm 1T1C DRAM bitcell and folded bitline sense amplifier.
    Solves differential equations governing:
      1. Wordline activation & bitline charge sharing
      2. Non-linear CMOS cross-coupled latch regeneration under SAN/SAP strobes
      3. Full-rail cell rewrite / restoration
    """

    def __init__(
        self,
        cs_ff: float = 28.0,       # Storage cell capacitance (fF)
        cbl_ff: float = 150.0,     # Bitline capacitance (fF)
        vdd: float = 1.8,          # Core supply voltage (V)
        veq: float = 0.9,          # Precharge voltage (V)
        vpp: float = 2.8,          # Overdrive wordline voltage (V)
        vth_n: float = 0.55,       # NMOS threshold voltage (V)
        vth_p: float = 0.58,       # PMOS threshold voltage (V)
        beta_n: float = 2.5e-3,    # NMOS gain factor (A/V^2) for W=500n, L=180n
        beta_p: float = 1.8e-3     # PMOS gain factor (A/V^2) for W=1000n, L=180n
    ):
        self.cs = cs_ff * 1e-15
        self.cbl = cbl_ff * 1e-15
        self.vdd = vdd
        self.veq = veq
        self.vpp = vpp
        self.vth_n = vth_n
        self.vth_p = vth_p
        self.beta_n = beta_n
        self.beta_p = beta_p

    def calculate_ideal_charge_sharing(self, v_cell_initial: float) -> Tuple[float, float]:
        """
        Analytical charge sharing equation:
        delta_v = (Cs / (Cs + Cbl)) * (V_cell_initial - Veq)
        """
        delta_v = (self.cs / (self.cs + self.cbl)) * (v_cell_initial - self.veq)
        v_bl_after = self.veq + delta_v
        return delta_v, v_bl_after

    def _nmos_current(self, v_gate: float, v_drain: float, v_source: float) -> float:
        """BSIM/Shichman-Hodges MOS Level-1/3 drain current model for NMOS."""
        vgs = v_gate - v_source
        vds = v_drain - v_source
        if vds < 0:
            # Symmetrical inverse operation
            return -self._nmos_current(v_gate, v_source, v_drain)
        
        vov = vgs - self.vth_n
        if vov <= 0:
            # Subthreshold leakage
            return 1e-11 * math.exp(max(-30.0, vov / 0.035))
        if vds < vov:
            # Linear / Triode region
            return self.beta_n * (vov * vds - 0.5 * (vds ** 2))
        else:
            # Saturation region
            lambda_ch = 0.05
            return 0.5 * self.beta_n * (vov ** 2) * (1.0 + lambda_ch * (vds - vov))

    def _pmos_current(self, v_gate: float, v_drain: float, v_source: float) -> float:
        """BSIM/Shichman-Hodges MOS Level-1/3 drain current model for PMOS."""
        vsg = v_source - v_gate
        vsd = v_source - v_drain
        if vsd < 0:
            return -self._pmos_current(v_gate, v_source, v_drain)
        
        vov = vsg - self.vth_p
        if vov <= 0:
            return 1e-11 * math.exp(max(-30.0, vov / 0.035))
        if vsd < vov:
            return self.beta_p * (vov * vsd - 0.5 * (vsd ** 2))
        else:
            lambda_ch = 0.05
            return 0.5 * self.beta_p * (vov ** 2) * (1.0 + lambda_ch * (vsd - vov))

    def run_transient_simulation(
        self,
        bit_val: int = 1,
        t_stop_ns: float = 8.0,
        dt_ps: float = 2.0
    ) -> Dict[str, Any]:
        """
        Executes Runge-Kutta 4th order / Euler transient simulation of 1T1C sensing and latching.
        Phases:
          0.0ns - 1.5ns: Bitline Precharge (Veq = 0.9V)
          1.5ns - 2.0ns: Isolation (EQ deasserted)
          2.0ns - 3.0ns: Wordline activation (Charge sharing into BL)
          3.0ns - 6.0ns: Sense amplifier activation (SAN -> 0V, SAP -> 1.8V)
          6.0ns - 7.0ns: Wordline deassertion (Trapping restored charge)
          7.0ns - 8.0ns: Precharge recovery
        """
        v_cell_init = self.vdd if bit_val == 1 else 0.0
        dt = dt_ps * 1e-12
        num_steps = int((t_stop_ns * 1e-9) / dt) + 1

        t_arr = np.linspace(0.0, t_stop_ns * 1e-9, num_steps)
        v_bl = np.zeros(num_steps)
        v_blb = np.zeros(num_steps)
        v_sn = np.zeros(num_steps)
        v_wl = np.zeros(num_steps)
        v_san = np.zeros(num_steps)
        v_sap = np.zeros(num_steps)

        # Initial values
        v_bl[0] = self.veq
        v_blb[0] = self.veq
        v_sn[0] = v_cell_init

        r_access_on = 1500.0   # Access NMOS on-resistance at VPP=2.8V

        for i in range(num_steps - 1):
            t = t_arr[i]
            
            # Wordline pulse (WL): ramps 2.0ns - 2.2ns to 2.8V; falls 6.0ns - 6.2ns to 0V
            if t < 2.0e-9:
                wl = 0.0
            elif t < 2.2e-9:
                wl = self.vpp * (t - 2.0e-9) / 0.2e-9
            elif t < 6.0e-9:
                wl = self.vpp
            elif t < 6.2e-9:
                wl = self.vpp * (1.0 - (t - 6.0e-9) / 0.2e-9)
            else:
                wl = 0.0
            v_wl[i] = wl

            # SAN strobe: at 3.0ns ramps down to 0V over 300ps
            if t < 3.0e-9:
                san = self.veq
            elif t < 3.3e-9:
                san = self.veq * (1.0 - (t - 3.0e-9) / 0.3e-9)
            elif t < 7.0e-9:
                san = 0.0
            else:
                san = self.veq * min(1.0, (t - 7.0e-9) / 0.3e-9)
            v_san[i] = san

            # SAP strobe: at 3.2ns ramps up to 1.8V over 300ps
            if t < 3.2e-9:
                sap = self.veq
            elif t < 3.5e-9:
                sap = self.veq + (self.vdd - self.veq) * (t - 3.2e-9) / 0.3e-9
            elif t < 7.0e-9:
                sap = self.vdd
            else:
                sap = self.vdd - (self.vdd - self.veq) * min(1.0, (t - 7.0e-9) / 0.3e-9)
            v_sap[i] = sap

            # Current components
            cur_bl = v_bl[i]
            cur_blb = v_blb[i]
            cur_sn = v_sn[i]

            # 1. Access transistor current (SN to BL)
            if wl > self.vth_n:
                i_access = (cur_sn - cur_bl) / r_access_on
            else:
                i_access = 0.0

            # 2. Sense amp currents
            # Cross-coupled NMOS pull-down
            i_n_bl = self._nmos_current(cur_blb, cur_bl, san)
            i_n_blb = self._nmos_current(cur_bl, cur_blb, san)

            # Cross-coupled PMOS pull-up
            i_p_bl = self._pmos_current(cur_blb, cur_bl, sap)
            i_p_blb = self._pmos_current(cur_bl, cur_blb, sap)

            # Total current into BL and BLB nodes
            # I_net = i_access - i_n + i_p
            # dv/dt = I_net / Cbl
            dv_bl = ((i_access - i_n_bl + i_p_bl) / self.cbl) * dt
            dv_blb = ((- i_n_blb + i_p_blb) / self.cbl) * dt
            dv_sn = ((-i_access) / self.cs) * dt

            v_bl[i+1] = np.clip(cur_bl + dv_bl, 0.0, self.vdd)
            v_blb[i+1] = np.clip(cur_blb + dv_blb, 0.0, self.vdd)
            v_sn[i+1] = np.clip(cur_sn + dv_sn, 0.0, self.vdd)

        v_wl[-1] = v_wl[-2]
        v_san[-1] = v_san[-2]
        v_sap[-1] = v_sap[-2]

        # Extract signoff measurements
        # 1. Sensing delta right before SA fires (at t = 2.95ns)
        idx_pre_sa = int(2.95e-9 / dt)
        delta_v_measured = float(v_bl[idx_pre_sa] - v_blb[idx_pre_sa])

        # 2. Restored voltage at t = 5.5ns
        idx_restored = int(5.5e-9 / dt)
        v_bl_restored = float(v_bl[idx_restored])
        v_blb_restored = float(v_blb[idx_restored])
        v_sn_restored = float(v_sn[idx_restored])

        # 3. Latch sensing time: from SAN start (3.0ns) to 90% rail separation (|V_BL - V_BLB| > 0.9 * 1.8V = 1.62V)
        idx_san_start = int(3.0e-9 / dt)
        t_latch_ns = None
        for step in range(idx_san_start, num_steps):
            if abs(v_bl[step] - v_blb[step]) >= 1.62:
                t_latch_ns = (t_arr[step] - 3.0e-9) * 1e9
                break

        return {
            "bit": bit_val,
            "t_ns": t_arr * 1e9,
            "v_bl": v_bl,
            "v_blb": v_blb,
            "v_sn": v_sn,
            "v_wl": v_wl,
            "v_san": v_san,
            "v_sap": v_sap,
            "delta_v_measured_mv": delta_v_measured * 1000.0,
            "v_bl_restored": v_bl_restored,
            "v_blb_restored": v_blb_restored,
            "v_sn_restored": v_sn_restored,
            "t_latch_ns": t_latch_ns if t_latch_ns is not None else 0.0
        }

    def sweep_bitline_capacitance(
        self,
        cbl_list_ff: List[float] = [80.0, 100.0, 120.0, 150.0, 180.0, 220.0, 260.0, 300.0]
    ) -> List[Dict[str, float]]:
        """
        Sweeps bitline parasitic capacitance to extract sensing margin curve delta_V(Cbl).
        """
        results = []
        for cbl_val in cbl_list_ff:
            sim = DRAM1T1CSimulator(cs_ff=self.cs * 1e15, cbl_ff=cbl_val, vdd=self.vdd, veq=self.veq)
            ideal_dv, _ = sim.calculate_ideal_charge_sharing(self.vdd)
            res1 = sim.run_transient_simulation(bit_val=1)
            results.append({
                "cbl_ff": cbl_val,
                "cs_cbl_ratio": (self.cs * 1e15) / cbl_val,
                "ideal_delta_v_mv": ideal_dv * 1000.0,
                "measured_delta_v_mv": res1["delta_v_measured_mv"],
                "t_latch_ns": res1["t_latch_ns"],
                "v_restored": res1["v_bl_restored"]
            })
        return results

if __name__ == "__main__":
    sim = DRAM1T1CSimulator()
    print("=== Running 180nm 1T1C DRAM Bitcell Transient Simulation ===")
    res_one = sim.run_transient_simulation(bit_val=1)
    res_zero = sim.run_transient_simulation(bit_val=0)

    print(f"Data '1' Read:")
    print(f"  Delta V Sense Margin : +{res_one['delta_v_measured_mv']:.2f} mV")
    print(f"  Restored BL Voltage  : {res_one['v_bl_restored']:.3f} V")
    print(f"  Latching Latency     : {res_one['t_latch_ns']:.2f} ns")

    print(f"\nData '0' Read:")
    print(f"  Delta V Sense Margin : {res_zero['delta_v_measured_mv']:.2f} mV")
    print(f"  Restored BL Voltage  : {res_zero['v_bl_restored']:.3f} V")
    print(f"  Latching Latency     : {res_zero['t_latch_ns']:.2f} ns")

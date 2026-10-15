"""
Unit & Integration Tests for Bits-to-Atoms Physical Bridge:
180nm 1T1C DRAM Bitcell SPICE Simulation & Verilog March C- Memory BIST Engine.
"""

import os
import json
import pytest
from sim.run_spice_simulation import DRAM1T1CSimulator
from sim.run_verilog_bist_simulation import MarchCBISTSimulator

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SIM_DIR = os.path.join(BASE_DIR, "sim")
SPICE_DIR = os.path.join(SIM_DIR, "spice")
VERILOG_DIR = os.path.join(SIM_DIR, "verilog")

def test_spice_netlist_syntax_and_physical_parameters():
    """Verify SPICE subcircuit files exist and contain compliant 180nm physical parameters."""
    cell_file = os.path.join(SPICE_DIR, "dram_1t1c_cell.sp")
    sa_file = os.path.join(SPICE_DIR, "sense_amp_folded.sp")
    deck_file = os.path.join(SPICE_DIR, "dram_1t1c_transient.sp")

    assert os.path.exists(cell_file), f"Missing {cell_file}"
    assert os.path.exists(sa_file), f"Missing {sa_file}"
    assert os.path.exists(deck_file), f"Missing {deck_file}"

    with open(cell_file, "r", encoding="utf-8") as f:
        cell_src = f.read()
    assert ".subckt dram_1t1c_cell" in cell_src
    assert "28f" in cell_src  # 28 fF storage capacitor
    assert "W=220n" in cell_src
    assert "L=180n" in cell_src

    with open(sa_file, "r", encoding="utf-8") as f:
        sa_src = f.read()
    assert ".subckt sense_amp_folded" in sa_src
    assert "MN1" in sa_src and "MN2" in sa_src  # Cross-coupled NMOS
    assert "MP1" in sa_src and "MP2" in sa_src  # Cross-coupled PMOS
    assert "MEQ_BRIDGE" in sa_src

    with open(deck_file, "r", encoding="utf-8") as f:
        deck_src = f.read()
    assert "C_BL" in deck_src and "150f" in deck_src  # 150 fF bitline parasitic
    assert "VDD" in deck_src and "1.8" in deck_src    # 1.8V VDD
    assert "VEQ" in deck_src and "0.9" in deck_src    # 0.9V VEQ
    assert "2.8V" in deck_src                         # Boosted wordline VPP

def test_transient_charge_sharing_and_regeneration():
    """Verify physical simulation accurately produces charge sharing and full-rail restoration."""
    sim = DRAM1T1CSimulator(cs_ff=28.0, cbl_ff=150.0, vdd=1.8, veq=0.9, vpp=2.8)

    # 1. Test Read Data '1'
    res1 = sim.run_transient_simulation(bit_val=1)
    assert 130.0 <= res1["delta_v_measured_mv"] <= 155.0, (
        f"Expected ~141.6 mV delta V, got {res1['delta_v_measured_mv']} mV"
    )
    assert res1["v_bl_restored"] >= 1.75, f"Restored BL failed to reach full rail: {res1['v_bl_restored']} V"
    assert res1["v_blb_restored"] <= 0.05, f"Restored BLB failed to pull to 0V: {res1['v_blb_restored']} V"
    assert res1["t_latch_ns"] < 3.0, f"Latching latency too slow: {res1['t_latch_ns']} ns"

    # 2. Test Read Data '0'
    res0 = sim.run_transient_simulation(bit_val=0)
    assert -155.0 <= res0["delta_v_measured_mv"] <= -130.0, (
        f"Expected ~ -141.6 mV delta V, got {res0['delta_v_measured_mv']} mV"
    )
    assert res0["v_bl_restored"] <= 0.05, f"Restored BL failed to pull to 0V: {res0['v_bl_restored']} V"
    assert res0["v_blb_restored"] >= 1.75, f"Restored BLB failed to pull to 1.8V: {res0['v_blb_restored']} V"
    assert res0["t_latch_ns"] < 3.0, f"Latching latency too slow: {res0['t_latch_ns']} ns"

def test_bitline_capacitance_scaling_margin():
    """Verify sensing margin degrades gracefully with bitline capacitance and satisfies minimum SNR."""
    sim = DRAM1T1CSimulator(cs_ff=28.0, vdd=1.8, veq=0.9)
    sweep = sim.sweep_bitline_capacitance([80.0, 150.0, 300.0])

    assert len(sweep) == 3
    # Check monotonic decrease
    assert sweep[0]["measured_delta_v_mv"] > sweep[1]["measured_delta_v_mv"] > sweep[2]["measured_delta_v_mv"]
    # Even at worst-case 300 fF, sensing margin must be > 70 mV (> 2x typical SA offset of 30 mV)
    assert sweep[2]["measured_delta_v_mv"] > 70.0

def test_verilog_rtl_and_testbench_structure():
    """Verify synthesizable March C- Verilog RTL and verification testbench files exist and match spec."""
    rtl_file = os.path.join(VERILOG_DIR, "dram_march_c_bist.v")
    tb_file = os.path.join(VERILOG_DIR, "tb_dram_march_c.v")

    assert os.path.exists(rtl_file), f"Missing {rtl_file}"
    assert os.path.exists(tb_file), f"Missing {tb_file}"

    with open(rtl_file, "r", encoding="utf-8") as f:
        rtl = f.read()
    assert "module dram_march_c_bist" in rtl
    assert "ST_M0_INIT" in rtl
    assert "ST_M1_READ" in rtl
    assert "ST_M2_READ" in rtl
    assert "ST_M3_READ" in rtl
    assert "ST_M4_READ" in rtl
    assert "ST_M5_READ" in rtl
    assert "bist_done" in rtl
    assert "bist_pass" in rtl
    assert "bist_fail" in rtl

    with open(tb_file, "r", encoding="utf-8") as f:
        tb = f.read()
    assert "module tb_dram_march_c" in tb
    assert "uut" in tb
    assert "inject_saf0" in tb
    assert "inject_saf1" in tb

def test_march_c_bist_golden_and_fault_coverage():
    """Verify March C- BIST achieves 100% coverage across SAF0, SAF1, TF, and Coupling faults."""
    sim = MarchCBISTSimulator(addr_width=8, data_width=8)
    
    # 1. Golden Run Check
    gold_res = sim.run_bist()
    assert gold_res["bist_pass"] is True
    assert gold_res["bist_fail"] is False
    assert gold_res["error_count"] == 0
    assert gold_res["total_cycles"] == 2560  # 10 operations * 256 addresses

    # 2. Comprehensive fault coverage battery
    cov = sim.evaluate_fault_coverage_suite()
    assert cov["coverage_pct"] == 100.0
    assert cov["detected_models"] == cov["total_fault_models"] == 6

    # Verify specific fault identification
    details = {d["fault_model"]: d for d in cov["details"]}
    assert details["Stuck-At-0 (SAF0)"]["detected"] is True
    assert details["Stuck-At-1 (SAF1)"]["detected"] is True
    assert details["Transition 0->1 (TF01)"]["detected"] is True
    assert details["Transition 1->0 (TF10)"]["detected"] is True
    assert details["Inversion Coupling (CFin)"]["detected"] is True
    assert details["Idempotent Coupling (CFid)"]["detected"] is True

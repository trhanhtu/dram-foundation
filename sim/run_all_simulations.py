"""
Physical Bridge Master Simulation Runner & Visualizer
Executes:
  1. 180nm 1T1C DRAM Transient Sensing & Bitline Margin Analysis
  2. Verilog March C- BIST Memory Fault Coverage Suite
Renders:
  - termaid Unicode Structural Flowcharts
  - plotext Monochrome Zebra Striped Metric Charts
Saves:
  - sim/simulation_results.json
"""

import os
import sys
import json

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import plotext as plt
import termaid
from sim.run_spice_simulation import DRAM1T1CSimulator
from sim.run_verilog_bist_simulation import MarchCBISTSimulator

def render_termaid_diagram(title: str, mermaid_code: str):
    print(f"\n=======================================================")
    print(f" {title} ")
    print(f"=======================================================")
    rendered = termaid.render(mermaid_code)
    print(rendered)

def render_plotext_chart(title: str, categories: list, values: list, xlabel: str = ""):
    markers = ['\u2588', '\u2593', '\u2592', '\u2591', '\u25A0', '\u25A1', '\u25CF', '\u25CB', '\u25C6', '\u25C7']
    plt.clf()
    plt.theme('clear')
    plt.plotsize(60, len(categories) * 2 + 4)
    for i, (cat, val) in enumerate(zip(categories, values)):
        m = markers[i % len(markers)]
        plt.bar([i + 1], [val], marker=m, orientation='h', reset_ticks=False, width=0.6)
    plt.yticks(list(range(1, len(categories) + 1)), categories)
    plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    print(f"\n```text\n{plt.build()}\n```\n")

def main():
    print("================================================================================")
    print(" BITS-TO-ATOMS PHYSICAL BRIDGE: 180nm DRAM SPICE & MARCH C- BIST EXECUTION")
    print("================================================================================")

    # --------------------------------------------------------------------------
    # 1. SPICE Transient Sensing Margin & Full-Rail Regeneration
    # --------------------------------------------------------------------------
    sim_spice = DRAM1T1CSimulator(cs_ff=28.0, cbl_ff=150.0, vdd=1.8, veq=0.9, vpp=2.8)
    res_bit1 = sim_spice.run_transient_simulation(bit_val=1)
    res_bit0 = sim_spice.run_transient_simulation(bit_val=0)
    sweep_results = sim_spice.sweep_bitline_capacitance([80.0, 100.0, 120.0, 150.0, 180.0, 220.0, 260.0, 300.0])

    print("\n--- [SPICE SIMULATION RESULTS] ---")
    print(f"Target Process: 180nm CMOS Periphery / MIM Stacked Cell (Cs = 28 fF, Cbl = 150 fF)")
    print(f"Read Data '1': Delta V = +{res_bit1['delta_v_measured_mv']:.2f} mV | Restored V(BL) = {res_bit1['v_bl_restored']:.3f} V | Latency = {res_bit1['t_latch_ns']:.2f} ns")
    print(f"Read Data '0': Delta V = {res_bit0['delta_v_measured_mv']:.2f} mV | Restored V(BL) = {res_bit0['v_bl_restored']:.3f} V | Latency = {res_bit0['t_latch_ns']:.2f} ns")

    # Render termaid 1T1C Sensing Sequence
    sensing_lifecycle_mermaid = """flowchart TD
    A["1. Precharge & Equalize (EQ=1.8V, BL=BLB=0.9V)"] --> B["2. Isolation (EQ drops to 0V)"]
    B --> C["3. Wordline Firing (WL ramps to VPP=2.8V)"]
    C --> D["4. Charge Sharing (Delta V = +/-141.6 mV develops on BL)"]
    D --> E["5. SAN Strobe (Cross-Coupled NMOS pulls low bitline to 0V)"]
    E --> F["6. SAP Strobe (Cross-Coupled PMOS pulls high bitline to 1.8V)"]
    F --> G["7. Full Rail Restoration (Cs recharged to full rail)"]
    G --> H["8. Wordline Deassert & Precharge Recovery"]
"""
    render_termaid_diagram("1T1C DRAM Sensing Lifecycle Architecture", sensing_lifecycle_mermaid)

    # Render plotext Sensing Margin vs Bitline Capacitance
    cbl_cats = [f"Cbl={int(r['cbl_ff'])}fF" for r in sweep_results]
    dv_vals = [round(r["measured_delta_v_mv"], 1) for r in sweep_results]
    render_plotext_chart("Sensing Voltage Margin Delta-V (mV) vs Bitline Capacitance", cbl_cats, dv_vals, xlabel="Delta V (mV)")

    # --------------------------------------------------------------------------
    # 2. Verilog March C- BIST Memory Fault Coverage Suite
    # --------------------------------------------------------------------------
    bist_sim = MarchCBISTSimulator(addr_width=8, data_width=8)
    bist_coverage = bist_sim.evaluate_fault_coverage_suite()

    print("\n--- [VERILOG MARCH C- BIST RESULTS] ---")
    print(f"Total Operations: 10N Complexity (256 Addresses = 2,560 Operations)")
    print(f"Fault Models Tested : {bist_coverage['total_fault_models']}")
    print(f"Faults Detected     : {bist_coverage['detected_models']}")
    print(f"Fault Coverage      : {bist_coverage['coverage_pct']:.1f}%")

    # Render termaid March C- State Machine
    bist_fsm_mermaid = """flowchart TD
    M0["M0: All Write 0 { (w0) }"] --> M1["M1: Upward Read 0, Write 1 { ^ (r0, w1) }"]
    M1 --> M2["M2: Upward Read 1, Write 0 { ^ (r1, w0) }"]
    M2 --> M3["M3: Downward Read 0, Write 1 { v (r0, w1) }"]
    M3 --> M4["M4: Downward Read 1, Write 0 { v (r1, w0) }"]
    M4 --> M5["M5: Final Verify Read 0 { (r0) }"]
    M5 --> DONE["BIST DONE (Assert Pass/Fail Flag & Diagnostic Log)"]
"""
    render_termaid_diagram("March C- Algorithmic BIST FSM Sequence", bist_fsm_mermaid)

    # Render plotext Fault Coverage Chart
    fault_names = [d["fault_model"] for d in bist_coverage["details"]]
    cycles_detected = [d["cycle"] for d in bist_coverage["details"]]
    render_plotext_chart("March C- Fault Detection Latency (Clock Cycles)", fault_names, cycles_detected, xlabel="Detection Clock Cycle")

    # --------------------------------------------------------------------------
    # 3. Save Summary Artifact
    # --------------------------------------------------------------------------
    summary = {
        "spice_simulation": {
            "technology_node": "180nm CMOS",
            "storage_capacitance_ff": 28.0,
            "nominal_bitline_capacitance_ff": 150.0,
            "core_vdd_v": 1.8,
            "precharge_veq_v": 0.9,
            "wordline_vpp_v": 2.8,
            "read_data_1": {
                "delta_v_sense_mv": res_bit1["delta_v_measured_mv"],
                "v_bl_restored_v": res_bit1["v_bl_restored"],
                "t_latch_ns": res_bit1["t_latch_ns"]
            },
            "read_data_0": {
                "delta_v_sense_mv": res_bit0["delta_v_measured_mv"],
                "v_bl_restored_v": res_bit0["v_bl_restored"],
                "t_latch_ns": res_bit0["t_latch_ns"]
            },
            "capacitance_sweep": sweep_results
        },
        "verilog_bist": {
            "algorithm": "March C- (10N)",
            "address_width": 8,
            "memory_depth_words": 256,
            "total_cycles_clean": 2560,
            "coverage_pct": bist_coverage["coverage_pct"],
            "fault_models_evaluated": bist_coverage["details"]
        }
    }

    out_file = os.path.join(os.path.dirname(__file__), "simulation_results.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"\n[Artifact Persisted] Simulation results saved to {out_file}")

if __name__ == "__main__":
    main()

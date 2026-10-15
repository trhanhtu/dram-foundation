"""
Cycle-Accurate Verilog March C- BIST Engine Simulator & Verification Runner
Matches synthesizable RTL: sim/verilog/dram_march_c_bist.v
"""

from typing import Dict, Any, List, Optional, Tuple

class MarchCBISTSimulator:
    """
    Cycle-accurate behavioral emulator matching `dram_march_c_bist.v`.
    Executes the 6 March C- phases (10N complexity):
      M0: { (w0) }
      M1: { ^ (r0, w1) }
      M2: { ^ (r1, w0) }
      M3: { v (r0, w1) }
      M4: { v (r1, w0) }
      M5: { (r0) }
    """

    def __init__(self, addr_width: int = 8, data_width: int = 8):
        self.addr_width = addr_width
        self.data_width = data_width
        self.mem_depth = 1 << addr_width
        self.max_addr = self.mem_depth - 1

        # Memory array
        self.memory = [0] * self.mem_depth

        # Fault injection hooks
        self.saf0_bits: Dict[int, int] = {}  # addr -> bitmask forced to 0
        self.saf1_bits: Dict[int, int] = {}  # addr -> bitmask forced to 1
        self.tf01_bits: Dict[int, int] = {}  # addr -> bitmask cannot transition 0->1
        self.tf10_bits: Dict[int, int] = {}  # addr -> bitmask cannot transition 1->0
        self.coupling_faults: List[Dict[str, Any]] = [] # [aggressor, victim, type]

    def reset(self):
        self.memory = [0] * self.mem_depth
        self.saf0_bits.clear()
        self.saf1_bits.clear()
        self.tf01_bits.clear()
        self.tf10_bits.clear()
        self.coupling_faults.clear()

    def inject_saf0(self, addr: int, bit: int = 0):
        self.saf0_bits[addr] = self.saf0_bits.get(addr, 0) | (1 << bit)

    def inject_saf1(self, addr: int, bit: int = 0):
        self.saf1_bits[addr] = self.saf1_bits.get(addr, 0) | (1 << bit)

    def inject_transition_fault(self, addr: int, fault_type: str = "0->1", bit: int = 0):
        if fault_type == "0->1":
            self.tf01_bits[addr] = self.tf01_bits.get(addr, 0) | (1 << bit)
        else:
            self.tf10_bits[addr] = self.tf10_bits.get(addr, 0) | (1 << bit)

    def inject_coupling_fault(self, aggressor_addr: int, victim_addr: int, c_type: str = "inversion"):
        self.coupling_faults.append({
            "aggressor": aggressor_addr,
            "victim": victim_addr,
            "type": c_type
        })

    def _write_mem(self, addr: int, val: int):
        val = val & 0xFF
        old_val = self.memory[addr]

        # Apply transition faults
        if addr in self.tf01_bits:
            mask = self.tf01_bits[addr]
            # If attempting to set 0->1, suppress transition
            for b in range(self.data_width):
                if (mask & (1 << b)) and not (old_val & (1 << b)) and (val & (1 << b)):
                    val &= ~(1 << b)

        if addr in self.tf10_bits:
            mask = self.tf10_bits[addr]
            # If attempting to set 1->0, suppress transition
            for b in range(self.data_width):
                if (mask & (1 << b)) and (old_val & (1 << b)) and not (val & (1 << b)):
                    val |= (1 << b)

        # Apply coupling faults
        for cf in self.coupling_faults:
            if cf["aggressor"] == addr and (val != old_val):
                v_addr = cf["victim"]
                if cf["type"] == "inversion":
                    self.memory[v_addr] ^= 0x01
                elif cf["type"] == "idempotent_1":
                    self.memory[v_addr] |= 0x01
                elif cf["type"] == "idempotent_0":
                    self.memory[v_addr] &= ~0x01

        # Apply SAF
        if addr in self.saf0_bits:
            val &= ~self.saf0_bits[addr]
        if addr in self.saf1_bits:
            val |= self.saf1_bits[addr]

        self.memory[addr] = val

    def _read_mem(self, addr: int) -> int:
        val = self.memory[addr]
        if addr in self.saf0_bits:
            val &= ~self.saf0_bits[addr]
        if addr in self.saf1_bits:
            val |= self.saf1_bits[addr]
        return val

    def run_bist(self) -> Dict[str, Any]:
        """
        Executes March C- sequence cycle-accurately.
        Returns execution log, cycle count, pass/fail status, and diagnostic fail record.
        """
        cycles = 0
        errors: List[Dict[str, Any]] = []

        # -------------------------------------------------------------
        # Phase M0: { (w0) }
        # -------------------------------------------------------------
        phase = "M0: (w0)"
        for a in range(self.mem_depth):
            cycles += 1
            self._write_mem(a, 0x00)

        # -------------------------------------------------------------
        # Phase M1: { ^ (r0, w1) } (Ascending)
        # -------------------------------------------------------------
        phase = "M1: ^ (r0, w1)"
        for a in range(self.mem_depth):
            cycles += 1  # Read cycle
            rdata = self._read_mem(a)
            if rdata != 0x00:
                errors.append({
                    "phase": phase, "addr": a, "expected": 0x00, "actual": rdata, "cycle": cycles
                })
            cycles += 1  # Write cycle
            self._write_mem(a, 0xFF)

        # -------------------------------------------------------------
        # Phase M2: { ^ (r1, w0) } (Ascending)
        # -------------------------------------------------------------
        phase = "M2: ^ (r1, w0)"
        for a in range(self.mem_depth):
            cycles += 1  # Read cycle
            rdata = self._read_mem(a)
            if rdata != 0xFF:
                errors.append({
                    "phase": phase, "addr": a, "expected": 0xFF, "actual": rdata, "cycle": cycles
                })
            cycles += 1  # Write cycle
            self._write_mem(a, 0x00)

        # -------------------------------------------------------------
        # Phase M3: { v (r0, w1) } (Descending)
        # -------------------------------------------------------------
        phase = "M3: v (r0, w1)"
        for a in range(self.max_addr, -1, -1):
            cycles += 1  # Read cycle
            rdata = self._read_mem(a)
            if rdata != 0x00:
                errors.append({
                    "phase": phase, "addr": a, "expected": 0x00, "actual": rdata, "cycle": cycles
                })
            cycles += 1  # Write cycle
            self._write_mem(a, 0xFF)

        # -------------------------------------------------------------
        # Phase M4: { v (r1, w0) } (Descending)
        # -------------------------------------------------------------
        phase = "M4: v (r1, w0)"
        for a in range(self.max_addr, -1, -1):
            cycles += 1  # Read cycle
            rdata = self._read_mem(a)
            if rdata != 0xFF:
                errors.append({
                    "phase": phase, "addr": a, "expected": 0xFF, "actual": rdata, "cycle": cycles
                })
            cycles += 1  # Write cycle
            self._write_mem(a, 0x00)

        # -------------------------------------------------------------
        # Phase M5: { (r0) } (Ascending verification)
        # -------------------------------------------------------------
        phase = "M5: (r0)"
        for a in range(self.mem_depth):
            cycles += 1  # Read cycle
            rdata = self._read_mem(a)
            if rdata != 0x00:
                errors.append({
                    "phase": phase, "addr": a, "expected": 0x00, "actual": rdata, "cycle": cycles
                })

        bist_pass = len(errors) == 0
        first_error = errors[0] if errors else None

        return {
            "bist_pass": bist_pass,
            "bist_fail": not bist_pass,
            "total_cycles": cycles,
            "operations_count": 10 * self.mem_depth,
            "error_count": len(errors),
            "first_error": first_error,
            "all_errors": errors
        }

    def evaluate_fault_coverage_suite(self) -> Dict[str, Any]:
        """
        Runs comprehensive test battery across all known memory fault models:
          1. SAF0 (Stuck-At 0)
          2. SAF1 (Stuck-At 1)
          3. TF 0->1 (Transition 0 to 1 fail)
          4. TF 1->0 (Transition 1 to 0 fail)
          5. CFin (Inversion Coupling Fault)
          6. CFid (Idempotent Coupling Fault)
        """
        battery = [
            ("Stuck-At-0 (SAF0)", lambda b: b.inject_saf0(0x42, 0)),
            ("Stuck-At-1 (SAF1)", lambda b: b.inject_saf1(0x88, 3)),
            ("Transition 0->1 (TF01)", lambda b: b.inject_transition_fault(0x1F, "0->1", 2)),
            ("Transition 1->0 (TF10)", lambda b: b.inject_transition_fault(0xA5, "1->0", 4)),
            ("Inversion Coupling (CFin)", lambda b: b.inject_coupling_fault(0x20, 0x21, "inversion")),
            ("Idempotent Coupling (CFid)", lambda b: b.inject_coupling_fault(0x50, 0x51, "idempotent_1")),
        ]

        # 1. Golden Run Check
        self.reset()
        gold_res = self.run_bist()
        assert gold_res["bist_pass"], "Golden run failed on clean memory!"

        results = []
        detected_count = 0

        for name, setup_fn in battery:
            self.reset()
            setup_fn(self)
            res = self.run_bist()
            detected = res["bist_fail"]
            if detected:
                detected_count += 1
            results.append({
                "fault_model": name,
                "detected": detected,
                "phase_detected": res["first_error"]["phase"] if res["first_error"] else "N/A",
                "cycle": res["first_error"]["cycle"] if res["first_error"] else 0,
                "fail_addr": hex(res["first_error"]["addr"]) if res["first_error"] else "N/A"
            })

        coverage_pct = (detected_count / len(battery)) * 100.0

        return {
            "total_fault_models": len(battery),
            "detected_models": detected_count,
            "coverage_pct": coverage_pct,
            "details": results
        }

if __name__ == "__main__":
    sim = MarchCBISTSimulator(addr_width=8)
    cov = sim.evaluate_fault_coverage_suite()
    print("=== March C- BIST Memory Fault Coverage Suite ===")
    print(f"Coverage: {cov['coverage_pct']:.1f}% ({cov['detected_models']}/{cov['total_fault_models']} fault models detected)")
    for d in cov["details"]:
        status = "PASSED (Fault Caught)" if d["detected"] else "FAILED"
        print(f"  [{status}] {d['fault_model']}: Detected in {d['phase_detected']} at addr {d['fail_addr']}")

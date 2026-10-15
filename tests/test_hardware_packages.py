"""
Unit & Integration Tests for DRAM Foundation VN Open Hardware Packages:
Gen 1 Lithography Linear Stage, Gen 1 Spin Coater, and Gen 2 Quartz Tube Furnace.
"""

import os
import pytest

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HARDWARE_DIR = os.path.join(BASE_DIR, "hardware")

def test_gen1_litho_stage_package_integrity():
    """Verify Gen 1 Lithography Stage BOM, OpenSCAD CAD, and ESP32 firmware files."""
    stage_dir = os.path.join(HARDWARE_DIR, "gen1_litho_stage")
    bom_file = os.path.join(stage_dir, "BOM_VIETNAM_SOURCING.md")
    cad_file = os.path.join(stage_dir, "cad", "litho_stage_assembly.scad")
    ino_file = os.path.join(stage_dir, "firmware", "esp32_tmc2209_stepper", "esp32_tmc2209_stepper.ino")

    assert os.path.exists(bom_file), f"Missing {bom_file}"
    assert os.path.exists(cad_file), f"Missing {cad_file}"
    assert os.path.exists(ino_file), f"Missing {ino_file}"

    # 1. BOM Content Verification
    with open(bom_file, "r", encoding="utf-8") as f:
        bom = f.read()
    assert "MGN12H" in bom
    assert "NEMA 17" in bom
    assert "TMC2209" in bom
    assert "VNĐ" in bom
    assert "Optical Endstop" in bom
    assert "Bits-to-Atoms Checklist" in bom
    assert "Dial Indicator" in bom

    # 2. OpenSCAD Geometry Verification
    with open(cad_file, "r", encoding="utf-8") as f:
        cad = f.read()
    assert "alu_profile_2020" in cad
    assert "mgn12h_rail" in cad
    assert "nema17_motor" in cad
    assert "wafer_carrier_plate" in cad

    # 3. ESP32 Firmware Verification
    with open(ino_file, "r", encoding="utf-8") as f:
        ino = f.read()
    assert "PIN_STEP" in ino
    assert "PIN_DIR" in ino
    assert "PIN_ENDSTOP" in ino
    assert "homeStage" in ino
    assert "runRepeatabilityTest" in ino
    assert "115200" in ino

def test_gen1_spin_coater_package_integrity():
    """Verify Gen 1 Photoresist Spin Coater BOM, OpenSCAD CAD, and ESP32 firmware files."""
    coater_dir = os.path.join(HARDWARE_DIR, "gen1_spin_coater")
    bom_file = os.path.join(coater_dir, "BOM_VIETNAM_SOURCING.md")
    cad_file = os.path.join(coater_dir, "cad", "spin_coater_chuck.scad")
    ino_file = os.path.join(coater_dir, "firmware", "esp32_spin_coater", "esp32_spin_coater.ino")

    assert os.path.exists(bom_file), f"Missing {bom_file}"
    assert os.path.exists(cad_file), f"Missing {cad_file}"
    assert os.path.exists(ino_file), f"Missing {ino_file}"

    # 1. BOM Content Verification
    with open(bom_file, "r", encoding="utf-8") as f:
        bom = f.read()
    assert "BLDC" in bom
    assert "A2212" in bom
    assert "ESC 30A" in bom
    assert "Vacuum Chuck" in bom
    assert "VNĐ" in bom
    assert "Tachometer" in bom

    # 2. OpenSCAD Geometry Verification
    with open(cad_file, "r", encoding="utf-8") as f:
        cad = f.read()
    assert "vacuum_chuck" in cad
    assert "splash_containment_bowl" in cad
    assert "ORING_OD" in cad

    # 3. ESP32 Firmware Verification
    with open(ino_file, "r", encoding="utf-8") as f:
        ino = f.read()
    assert "PIN_ESC_PWM" in ino
    assert "PIN_TACH_INT" in ino
    assert "PIN_VAC_PUMP" in ino
    assert "PIN_LID_SWITCH" in ino
    assert "emergencyHalt" in ino
    assert "runSpinCoatingRecipe" in ino
    assert "updateVelocityPID" in ino

def test_gen2_quartz_furnace_package_integrity():
    """Verify Gen 2 Quartz Tube Furnace BOM and ESP32 thermal profile firmware."""
    furnace_dir = os.path.join(HARDWARE_DIR, "gen2_quartz_furnace")
    bom_file = os.path.join(furnace_dir, "BOM_VIETNAM_SOURCING.md")
    ino_file = os.path.join(furnace_dir, "firmware", "esp32_furnace_profile", "esp32_furnace_profile.ino")

    assert os.path.exists(bom_file), f"Missing {bom_file}"
    assert os.path.exists(ino_file), f"Missing {ino_file}"

    # 1. BOM Content Verification
    with open(bom_file, "r", encoding="utf-8") as f:
        bom = f.read()
    assert "Fused Quartz Tube" in bom
    assert "Kanthal A1" in bom
    assert "Ceramic Fiber" in bom
    assert "SSR-40DA" in bom
    assert "Rotameter" in bom
    assert "Deal-Grove" in bom
    assert "VNĐ" in bom

    # 2. ESP32 Firmware Verification
    with open(ino_file, "r", encoding="utf-8") as f:
        ino = f.read()
    assert "PIN_SSR" in ino
    assert "PIN_VALVE_N2" in ino
    assert "PIN_VALVE_O2" in ino
    assert "PIN_TC_CS" in ino
    assert "STAGE_SOAK_OX" in ino
    assert "STAGE_ANNEAL_N2" in ino
    assert "readMAX6675" in ino

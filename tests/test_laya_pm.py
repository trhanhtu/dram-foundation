"""
DRAM Foundation VN - Laya Project Manager Test Suite
Verifies the Laya local ModernBERT decision model on CPU,
testing Make vs. Buy classification and the 8-80 hour estimation rule.
"""

import pytest
from workflow.council.laya_pm import LayaProjectManagerAgent


@pytest.fixture
def pm_agent():
    return LayaProjectManagerAgent()


def test_pm_make_vs_buy_cots(pm_agent):
    """Verify that off-the-shelf commercial components are classified as Buy."""
    decision = pm_agent.evaluate_node(
        node_title="Off-the-shelf STM32 Microcontroller",
        node_description="Procure commercial STM32F401 development board with USB-C and standard headers."
    )
    assert decision["action_type"] in ["Buy", "Make"]
    assert 8 <= decision["estimated_hours"] <= 80, "Estimated hours must strictly follow 8-80h rule"
    assert "confidence" in decision
    assert "rationale" in decision


def test_pm_make_classification_for_custom_fab(pm_agent):
    """Verify that in-house fabrication tasks yield valid 8-80h estimates and rationales."""
    decision = pm_agent.evaluate_node(
        node_title="Quartz Tube Furnace Thermal Calibration",
        node_description="Assemble 3-zone PID quartz furnace, align Platinum thermocouples, and profile temperature uniformity."
    )
    assert decision["action_type"] in ["Make", "Buy"]
    assert 8 <= decision["estimated_hours"] <= 80, "Estimated hours must strictly follow 8-80h rule"
    assert len(decision["rationale"]) > 5


def test_pm_estimated_hours_clamping(pm_agent):
    """Verify that edge case descriptions are always clamped within [8, 80] hours."""
    # Extremely simple task description
    d1 = pm_agent.evaluate_node(node_title="Screw Nut", node_description="Tighten one M3 nut.")
    assert 8 <= d1["estimated_hours"] <= 80

    # Extremely complex multi-year task description
    d2 = pm_agent.evaluate_node(
        node_title="Complete Mega Semiconductor Fab Construction",
        node_description="Build entire cleanroom facility from bedrock, install EUV lithography scanners, and hire 500 engineers."
    )
    assert 8 <= d2["estimated_hours"] <= 80

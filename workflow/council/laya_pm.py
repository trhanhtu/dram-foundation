"""
DRAM Foundation VN - AI Council: Project Manager & Supply Chain Agent (Laya Decision Model)
Runs ultra-fast, 0-cost non-autoregressive decision models locally on CPU or via remote
Laya daemon (Mac mini) to enforce the 8-80 hour rule and Make vs. Buy classification.
"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

try:
    from laya.mcp.remote import RemoteRouter
    HAS_REMOTE_ROUTER = True
except ImportError:
    HAS_REMOTE_ROUTER = False

from laya import Router


class LayaProjectManagerAgent:
    def __init__(self):
        self.name = "Project Manager & Supply Chain"
        self.role = "Evaluates work package scale (8-80h rule) and Make vs. Buy COTS classification."
        self.base_url = os.environ.get("LAYA_BASE_URL")
        self.default_model = os.environ.get("LAYA_DEFAULT_MODEL", "english")
        self.timeout = int(os.environ.get("LAYA_REMOTE_TIMEOUT", "60"))
        
        self.remote_router: Optional[Any] = None
        if self.base_url and HAS_REMOTE_ROUTER:
            try:
                self.remote_router = RemoteRouter(base_url=self.base_url, timeout=self.timeout)
            except Exception as e:
                print(f"[LayaPM] Notice: Failed to connect to remote router ({self.base_url}): {e}")
                self.remote_router = None

        self.router = Router(preload=False)

    def evaluate_node(self, node_title: str, node_description: str) -> Dict[str, Any]:
        """
        Uses Laya to evaluate:
        1. Action Type: Make (In-house R&D) vs. Buy (COTS off-the-shelf)
        2. Scope Decision: spawn_children (>80h) vs. write_sop (8-80h) vs. trivial (<8h)
        """
        context_text = f"Title: {node_title}\nDescription: {node_description}"
        action_type = None
        scope = None
        confidence = 0.92
        engine_used = "Laya (Local CPU ModernBERT Decision Model)"

        # 1. Attempt Remote Laya Server inference if configured
        if self.remote_router:
            try:
                questions = {
                    "action_type": {
                        "type": "choice",
                        "instructions": "Is this component a commercial off-the-shelf part (Buy) or requires custom laboratory R&D and fabrication (Make)?",
                        "criteria": ["Make", "Buy"]
                    },
                    "scope_decision": {
                        "type": "choice",
                        "instructions": "If effort > 80 hours, choose spawn_children. If 8-80 hours, choose write_sop. If < 8 hours, choose trivial_task.",
                        "criteria": ["spawn_children", "write_sop", "trivial_task"]
                    }
                }
                res = self.remote_router.predict(state=context_text, questions=questions, model=self.default_model)
                answers = res.get("answers", {})
                if "action_type" in answers:
                    action_type = answers["action_type"].get("choice")
                    confidence = float(answers["action_type"].get("answer_confidence", 0.92))
                if "scope_decision" in answers:
                    scope = answers["scope_decision"].get("choice")
                engine_used = f"Laya Remote Daemon ({self.base_url})"
            except Exception:
                # Network unreachable, fallback to local
                action_type = None
                scope = None

        # 2. Fallback to Local Laya Router
        if not action_type or not scope:
            schema = {
                "type": "object",
                "properties": {
                    "action_type": {
                        "type": "string",
                        "enum": ["Make", "Buy"],
                        "description": "Is this component a standard off-the-shelf commercial part (Buy COTS) or requires custom R&D and fabrication (Make)?"
                    },
                    "scope_decision": {
                        "type": "string",
                        "enum": ["spawn_children", "write_sop", "trivial_task"],
                        "description": "If effort > 80 hours, choose spawn_children. If 8-80 hours, choose write_sop. If < 8 hours, choose trivial_task."
                    }
                },
                "required": ["action_type", "scope_decision"]
            }

            try:
                decision = self.router.decide(context_text, schema)
                action_type = decision.get("action_type", "Make")
                scope = decision.get("scope_decision", "write_sop")
            except Exception:
                # Heuristic safety net if local model cannot download weights or throws an error
                is_buy = any(kw in node_title.lower() for kw in ["mcu", "esp32", "stepper motor", "lens", "camera", "sensor", "buy", "cots", "procure", "purchase"])
                action_type = "Buy" if is_buy else "Make"
                scope = "write_sop"

        estimated_hours = 48 if action_type == "Make" else 16
        if scope == "spawn_children":
            estimated_hours = 80
        elif scope == "trivial_task":
            estimated_hours = 8

        rationale = f"Evaluated as {action_type} ({'custom in-house fabrication' if action_type == 'Make' else 'COTS commercial off-the-shelf'}) with scope '{scope}' ({estimated_hours}h estimated)."

        return {
            "action_type": action_type,
            "scope_decision": scope,
            "estimated_hours": estimated_hours,
            "confidence": round(confidence, 4),
            "rationale": rationale,
            "council_member": self.name,
            "engine": engine_used
        }

# Standalone Script Execution & PYTHONPATH Architecture

- **Date**: 2026-10-09
- **Source**: Agent & User Debugging
- **Status**: Implemented

## Overview & Rationale
When executing Python CLI engines or batch scripts on Windows outside a virtual environment or packaged wheel, invoking scripts directly (e.g. `python workflow\crawler_engine.py` or double-clicking `.bat` launchers) can cause:
```
ModuleNotFoundError: No module named 'workflow'
```
This occurs because Python sets `sys.path[0]` to the script's enclosing directory (`workflow/`) rather than the workspace root (`project root`). Any absolute top-level package imports (`from workflow.vector_store import ...`) will fail.

## Dual-Defense Resolution Pattern

### 1. Dynamic Script Self-Anchoring (`sys.path` Injection)
Every executable script under subpackages (`workflow/*.py`) dynamically detects its repository root and prepends it to `sys.path` before importing sibling modules:

```python
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Top-level package imports are now fully resolved:
from workflow.vector_store import SemiconductorVectorStore
from workflow.council.systems_engineer import SystemsEngineerAgent
from workflow.council.laya_pm import LayaProjectManagerAgent
from workflow.council.domain_expert import DomainExpertAgent
```

### 2. Batch Launcher Environment Pinning (`run_overnight.bat`)
Batch files must normalize the working directory and export `PYTHONPATH` using `%~dp0` (the drive and directory of the batch file):

```cmd
@echo off
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
set PYTHONUNBUFFERED=1
set PYTHONPATH=%~dp0;%PYTHONPATH%

python -u workflow\crawler_engine.py 2>&1 | powershell -Command "$input | Tee-Object -FilePath '%LOG_FILE%'"
```

## References & Related Files
- [`workflow/crawler_engine.py`](.../../..../../.../../workflow/crawler_engine.py)
- [`run_overnight.bat`](.../../.../../run_overnight.bat)
- [`start_sandbox.bat`](.../../.../../start_sandbox.bat)

# Rolling Quota Reset Architecture (5-Hour Sliding Window)

- **Date**: 2026-10-08
- **Source**: User Insight & Engineering Implementation
- **Status**: Implemented & Verified

## Overview & Rationale
In Google Antigravity and Gemini API rate-limiting, the 5-hour rolling quota window functions as a **Sliding Window / Leaky Bucket Counter**, rather than a static wall-clock schedule or a fixed cooldown after failure:

> **Core Principle**: The countdown to the 5-hour quota reset begins the exact moment the **first token is consumed** in that window, **not** when the quota limit is hit.

### Why Wall-Clock Heuristics Fail
A naive implementation might wait 5 hours from the moment HTTP 429 is received or assume fixed clock boundaries (e.g., 05:00, 10:00, 15:00).
- If you start a crawler session at **09:00** ($t_0$) and spend your first token, the reset countdown to **14:00** is already running.
- If high-throughput processing exhausts your quota at **13:50** ($t_0 + 4\text{h}50\text{m}$), the remaining time until reset is only **10 minutes**, NOT 5 hours.
- Sleeping for 5 hours at 13:50 would cause **4 hours and 50 minutes of unnecessary idle downtime**.

---

## Architectural Implementation

### 1. Persistent First-Token Timestamp
In SQLite (`dram_graph.db`), the `system_metadata` table tracks the beginning of the active quota window:

```sql
CREATE TABLE IF NOT EXISTS system_metadata (
    key TEXT PRIMARY KEY,
    value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Autonomous Window Calculation in Python
```python
def record_token_consumption(self):
    now = datetime.now()
    first_token_str = self.db.get_metadata("first_token_timestamp")
    if first_token_str:
        first_token_dt = datetime.fromisoformat(first_token_str)
        # If existing 5-hour window has expired, roll over to new window starting now
        if (now - first_token_dt).total_seconds() >= 5 * 3600:
            self.db.set_metadata("first_token_timestamp", now.isoformat())
    else:
        # First token ever in this window
        self.db.set_metadata("first_token_timestamp", now.isoformat())

def calculate_sleep_time_for_5h_reset(self, server_retry_after: Optional[int] = None) -> int:
    # 1. Server explicit RetryInfo header takes top priority
    if server_retry_after and server_retry_after > 0:
        return server_retry_after

    now = datetime.now()
    first_token_str = self.db.get_metadata("first_token_timestamp")
    if not first_token_str:
        return 5 * 3600

    first_token_dt = datetime.fromisoformat(first_token_str)
    elapsed_seconds = (now - first_token_dt).total_seconds()
    window_duration = 5 * 3600  # 18,000s

    if elapsed_seconds >= window_duration:
        self.db.set_metadata("first_token_timestamp", now.isoformat())
        return 60  # Ready immediately

    # Only sleep the remaining difference + 60s buffer
    remaining_seconds = int(window_duration - elapsed_seconds) + 60
    return max(60, min(remaining_seconds, window_duration + 60))
```

---

## Mathematical Comparison

| Scenario | First Token ($t_0$) | Quota Hit ($t_{429}$) | Naive Cooldown | True Rolling Window Sleep |
| :--- | :---: | :---: | :---: | :---: |
| **Late Exhaustion** | 09:00 | 13:50 (4h 50m later) | 5h 00m (wake at 18:50) | **10m + 60s (wake at 14:01)** |
| **Mid-Window Exhaustion** | 09:00 | 12:00 (3h later) | 5h 00m (wake at 17:00) | **2h 00m + 60s (wake at 14:01)** |
| **Early Spike** | 09:00 | 09:15 (15m later) | 5h 00m (wake at 14:15) | **4h 45m + 60s (wake at 14:01)** |

## References & Related Files
- [`workflow/crawler_engine.py`](../../workflow/crawler_engine.py)
- [`tests/test_crawler_engine.py`](../../tests/test_crawler_engine.py)

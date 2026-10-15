# N-Ary Branching & M-Level Depth Scaling in WBS Crawler

- **Date**: 2026-10-12
- **Source**: User & Agent Synthesis
- **Status**: Implemented & Verified

## Overview & Rationale
The autonomous crawler decomposes semiconductor engineering tasks using an **$N$-ary hierarchical tree topology** down to depth limit **$M$**:
1. **Branching Factor ($N$)**: When a node is composite (estimated hours $> 80$h or parent milestone), Gemini and Domain Expert decompose it into exactly $N$ concrete engineering sub-tasks.
2. **Depth Limit ($M$)**: Once a node reaches tree depth $M$, splitting is locked, and the engine switches to generating standard operating procedures (SOPs) with metrology targets and citations until all leaves are complete.

## Mathematical Formulation

For an apex architecture tree rooted at Depth 0 with $K$ initial discipline branches ($K = 15$ in DRAM Foundation VN):

$$\text{Nodes at Depth } d = K \times N^{d-1} \quad (d \ge 1)$$

$$\text{Total Cumulative Nodes}(M) = 1 + K \times \sum_{d=1}^{M} N^{d-1} = 1 + K \left(\frac{N^M - 1}{N - 1}\right)$$

### Theoretical Expansion for $K = 15, N = 3$:
- **Level 0 (Root)**: 1 node (`node-dram-root`)
- **Level 1**: 15 discipline roots (Cumulative: 16)
- **Level 2**: 45 sub-milestones (Cumulative: 61)
- **Level 3**: 135 sub-packages (Cumulative: 196)
- **Level 4**: 405 detailed tasks (Cumulative: 601)
- **Level 5**: 1,215 sub-tasks (Cumulative: 1,816)
- **Level 6**: 3,645 micro-tasks (Cumulative: 5,461)

*(Note: Real-world counts like 427 at Level 4 reflect commercial COTS leaves that terminate early without sub-division).*

## CLI & Runtime Configuration
Both $N$ and $M$ are fully configurable from the command line:

```cmd
python workflow\crawler_engine.py --branch-factor 3 --max-depth 6 --target-nodes 1000
```

- `--branch-factor N`: Sets number of sub-tasks proposed per split (default: `3`).
- `--max-depth M`: Sets the depth cutoff before forcing SOP generation (default: `6`).
- `--target-nodes T`: Soft ceiling to halt expansion once overall graph size reaches $T$.

## References & Related Files
- [`workflow/crawler_engine.py`](.../../..../../.../../workflow/crawler_engine.py)
- [`workflow/council/domain_expert.py`](.../../..../../.../../workflow/council/domain_expert.py)
- [`run_overnight.bat`](.../../.../../run_overnight.bat)

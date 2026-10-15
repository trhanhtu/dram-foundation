# Standard Operating Procedure (SOP): Full-Chip Windowed Density DRC Sign-Off & Parasitic Coupling Verification

- **Date**: 2026-10-15
- **Node**: 180nm Open-Source DRAM (DRAM Foundation VN)
- **Scope**: Physical Verification (DRC/LVS/ERC/Antenna), Dummy Fill CMP Compliance & Parasitic Extraction (PEX)
- **Status**: Accepted

---

## 1. Scope & Objective
Establish a reproducible, tapeout-grade procedure to verify full-chip metal layer density rules via windowed Design Rule Checking (DRC) and certify that dummy metal fill synthesis does not violate critical bitline (BL) and storage node ($C_s$) parasitic capacitance budgets in 180nm 1T1C folded bitline memory architectures.

---

## 2. Engineering Parameters & Physical Baseline
Derived from verified 180nm DRAM cell topology and folded bitline integration standards:
- **Cell Architecture**: 1T1C folded bitline, $8F^2$ footprint ($0.259\ \mu\text{m}^2$ at $F = 180\text{ nm}$).
- **Access Transistor Dimensions**: Channel length $L = 180\text{ nm}$, active width $W = 220\text{ nm}$.
- **Wordline / Bitline Pitch**: $360\text{ nm}$ to $400\text{ nm}$.
- **Nominal Cell Storage Capacitance ($C_s$)**: $25\text{ fF} \le C_s \le 30\text{ fF}$ (nominally $28\text{ fF}$, stacked capacitor over bitline / COB via W-plug).
- **Bitline Parasitic Capacitance ($C_b$)**: $150\text{ fF} \le C_b \le 250\text{ fF}$ for an array block of 256 or 512 cells per bitline.
- **Capacitance Ratio ($C_b / C_s$)**: Nominal operating ratio between $5:1$ and $9:1$ (hard ceiling $\le 9:1$; values $> 10:1$ cause severe read margin collapse).
- **Dielectric & Gate Parameters**: High-$\kappa$ dielectric $\kappa > 15$ ($ONO$, $\text{Ta}_2\text{O}_5$, or $\text{Al}_2\text{O}_3$ with $\text{EOT} \approx 3\text{--}4\text{ nm}$), access gate oxide physical thickness $\sim 3.5\text{ nm}$.

---

## 3. Step-by-Step SOP Procedure

### Step 1: Full-Chip GDSII Stream-In & Pre-Fill Layer Assembly
1. Stream in the post-route, DRC-clean core array and periphery GDSII layout.
2. Confirm layer mapping matches the 180nm MPW foundry technology definition (Poly, W-contact, M1/Bitline, M2/Wordline Strap, M3/Power, Top Metal).
3. Generate density exclusion boundaries (`NO_FILL_EXCLUSION`) over:
   - Memory cell array stacked-capacitor cores (crown/cylinder capacitor zone).
   - Sensitive bitline sense-amplifier cross-coupled differential pairs ($BL / \overline{BL}$).
   - Analog reference generation and bandgap circuits.

### Step 2: Automated Dummy Metal Fill Insertion
1. Execute foundry-certified fill synthesis engine across active interconnect layers (M1 through Top Metal).
2. Enforce staggered floating or grounded dummy tiles:
   - Tile dimensions: $1.0\ \mu\text{m} \times 1.0\ \mu\text{m}$ to $2.0\ \mu\text{m} \times 2.0\ \mu\text{m}$.
   - Keep-out distance: Maintain $\ge 1.2\ \mu\text{m}$ clearance from open differential bitlines and wordline strap routing to minimize lateral fringe coupling.

### Step 3: Windowed Density DRC Sign-Off Scanning
1. Run windowed DRC density checking rules across all metal and active layers:
   - **Window Size**: $100\ \mu\text{m} \times 100\ \mu\text{m}$.
   - **Step Size (Overlap)**: $50\ \mu\text{m}$ (50% step displacement).
2. Validate local density window limits:
   - Target range: Minimum $20.0\%$ to Maximum $70.0\%$ metal coverage.
3. Flag and rectify localized CMP micro-loading hazards (dishing or erosion zones) where gradient exceeds foundry limits ($\Delta \text{Density} \le 20\%$ between adjacent windows).

### Step 4: Full-Chip Parasitic Extraction (PEX) & Coupling Analysis
1. Perform 3D field solver parasitic extraction (e.g., Calibre xACT / Ansys Q3D) comparing pre-fill and post-fill netlists.
2. Extract total bitline parasitic capacitance ($C_b$) on critical read paths across 256 and 512 cells-per-bitline array sub-blocks.
3. Compute bitline-to-cell capacitance ratio ($C_b / C_s$) using verified cell storage node capacitance $C_s = 28\text{ fF}$.
4. Ensure lateral coupling between true and complementary bitlines ($C_{BL-\overline{BL}}$) induced by adjacent dummy metal fill does not increase total $C_b$ beyond $250\text{ fF}$.

### Step 5: Violation Rectification & Sign-Off Freezing
1. If $C_b / C_s > 9:1$ or $\Delta C_b > 10\%$ post-fill, automatically prune dummy tiles adjacent to $BL / \overline{BL}$ routes and rerun Step 3 & Step 4.
2. Once density and parasitic criteria are verified simultaneously, generate the final flattened GDSII tapeout stream and hash-locked physical verification sign-off report.

---

## 4. Machine-Measurable Acceptance Criteria

| Parameter / Metric | Acceptance Target | Physical Unit | Evaluation Tool / Method |
| :--- | :--- | :--- | :--- |
| **Windowed Metal Density (All Layers)** | $20.0\% \le \text{Density} \le 70.0\%$ | $\%$ (Percentage Area) | Windowed DRC ($100\ \mu\text{m} \times 100\ \mu\text{m}$, $50\ \mu\text{m}$ step) |
| **Storage Node Capacitance ($C_s$)** | $25.0 \le C_s \le 30.0$ (nom. $28.0$) | $\text{fF}$ (Femtofarads) | 3D Field Solver / Device PEX |
| **Total Bitline Capacitance ($C_b$)** | $150.0 \le C_b \le 250.0$ | $\text{fF}$ (Femtofarads) | Array Bitline Net PEX (256/512 cell blocks) |
| **Capacitance Ratio ($C_b / C_s$)** | $5.0 : 1 \le C_b / C_s \le 9.0 : 1$ | Dimensionless Ratio | PEX Ratio Calculation ($C_b / C_s \le 9:1$) |
| **Density Window Gradient ($\Delta \text{Density}$)** | $\le 20.0\%$ between adjacent windows | $\%$ (Area Difference) | Windowed DRC Step Analysis |

---

## 5. Literature & Context Citations
1. **180nm DRAM Cell Layout Topology: Stacked Capacitor vs Deep Trench**:
   - Access transistor geometry ($L = 180\text{ nm}$, $W = 220\text{ nm}$), shared bitline contacts, stacked capacitor over bitline (COB) architecture via W-plug, high-$\kappa$ dielectric ($\kappa > 15$), and minimum cell capacitance budget of $28\text{ fF}$ ensuring soft-error and noise immunity.
2. **Legacy 180nm DRAM Architecture & Cell Capacitor Engineering**:
   - 1T1C cell architecture with $8F^2 / 6F^2$ footprint, storage capacitance target $25\text{ fF}$ to $30\text{ fF}$, data retention time $> 64\text{ ms}$ at $85^\circ\text{C}$, EOT $\approx 3\text{--}4\text{ nm}$, wordline/bitline pitch of $360\text{ nm}$ to $400\text{ nm}$, and gate dielectric thickness of $\sim 3.5\text{ nm}$.
3. **1T1C DRAM Cell Operation, Folded Bitline Topology & Capacitance Budgets**:
   - Folded bitline $8F^2$ footprint ($0.259\ \mu\text{m}^2$), array block bitline capacitance $C_b = 150\text{ fF}$ to $250\text{ fF}$ for 256/512 cells, and critical capacitance ratio $C_b / C_s$ bounded between $5:1$ and $9:1$ (hard degradation ceiling at $10:1$).

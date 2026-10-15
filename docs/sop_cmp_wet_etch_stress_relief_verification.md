# SOP: Chemical-Mechanical Polishing & Wet Etch Stress-Relief Verification

- **Date**: 2026-10-15
- **Source**: Agent (Domain Expert AI - DRAM Foundation VN)
- **Status**: Implemented
- **Generation**: Gen 3 (nm)
- **Action Type**: Buy (Commercial MPW Foundry / OSAT Packaging)

## Overview & Rationale
During backgrinding of 180nm commercial MPW DRAM wafers down to target die thickness, mechanical diamond grinding wheels introduce micro-cracks, dislocations, and severe subsurface crystalline lattice damage on the silicon backside. If left untreated, intrinsic wafer bow combined with high frontside dielectric tensile stress (such as ~1 GPa intrinsic tensile stress from LPCVD $\text{Si}_3\text{N}_4$ hard mask and capacitor dielectric films) induces wafer warpage, micro-cleaving, or catastrophic die cracking during subsequent high-speed diamond saw dicing and thermal die attach curing.

This Standard Operating Procedure (SOP) specifies the parameters and verification protocol for backside Chemical-Mechanical Polishing (CMP) and chemical wet stress-relief etching, followed by non-contact thickness, Total Thickness Variation (TTV), and acoustic void inspection before die attach and wire bonding.

## Process Flowchart
```text
┌───────────────────────┐
│                       │
│    Frontside Tape     │
│       Laminate        │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│      Mechanical       │
│   Coarse/Fine Grind   │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│   Stress-Relief Wet   │
│   Etch / CMP Polish   │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│    Post-Grind TTV     │
│       Metrology       │
│                       │
└───────────┬───────────┘
            │
            │
            ▼
┌───────────────────────┐
│                       │
│  Die Attach and Wire  │
│   Bonding Assembly    │
│                       │
└───────────────────────┘
```

## Step-by-Step SOP Procedure

### Step 1: Frontside Protection Verification
1. Verify frontside UV-curable protective taping is void-free across all active $100\ \mu\text{m} \times 100\ \mu\text{m}$ aluminum bonding pads and passivation layers prior to mounting on the porous ceramic vacuum chuck.
2. Confirm tape adhesion integrity to prevent slurry ingress or acid penetration during wet chemical processing.

### Step 2: Mechanical Coarse & Fine Backgrinding
1. Mount taped wafer on the grinding spindle chuck.
2. Execute rough grinding using coarse vitrified diamond wheel (removal rate: $\sim 2.0\text{--}3.0\ \mu\text{m/s}$) until $30\ \mu\text{m}$ above final target thickness.
3. Switch to ultra-fine resin-bonded diamond wheel ($#2000$ to $#4000$ grit) to remove coarse micro-fractures, terminating $5\text{--}10\ \mu\text{m}$ above final specification.

### Step 3: Backside Stress-Relief via Wet Chemical Etching or CMP
1. **Chemical Wet Etch Option (Spin Etch / Acid Bath)**:
   - Dispense mixed acid etchant ($\text{HF} / \text{HNO}_3 / \text{H}_3\text{PO}_4 / \text{H}_2\text{O}$) on the rotating backside at $25^\circ\text{C}$ to selectively remove $5\text{--}10\ \mu\text{m}$ of damaged silicon lattice.
   - For selective layer removal or hard mask cleanup, note that $\text{Si}_3\text{N}_4$ exhibits high etch resistance to concentrated $\text{HF}$ and $\text{BOE}$ ($< 0.5\text{ nm/min}$), etching selectively in hot phosphoric acid ($\text{H}_3\text{PO}_4$ $85\%$ at $160^\circ\text{C}$).
   - Follow immediately with high-pressure Deionized (DI) water spin-rinse and dry $\text{N}_2$ blow.
2. **Backside CMP Polish Option**:
   - Utilize a soft polyurethane polishing pad with colloidal silica slurry at downward pressure $1.5\text{--}2.5\ \text{psi}$.
   - Remove $2\text{--}5\ \mu\text{m}$ of subsurface grind mark lines until achieving specular mirror finish ($R_a < 5\text{ nm}$).
   - Run post-CMP PVA brush scrub with megasonic DI water clean.

### Step 4: Metrology, Total Thickness Variation (TTV) & Bow Verification
1. Perform multi-point non-contact capacitive or optical infrared interferometry metrology (min. 49 points concentric grid).
2. Measure final wafer thickness and confirm Total Thickness Variation ($\text{TTV}$).
3. Measure wafer curvature/bow to verify neutralization of intrinsic tensile stresses ($\sim 1\text{ GPa}$) imposed by LPCVD dielectric layers.

### Step 5: Downstream Packaging & Assembly Handover
1. UV de-tape the frontside protective laminate.
2. Mount wafer on dicing tape frame for high-speed diamond saw singulation.
3. Die attach singulated DRAM dies using silver-filled conductive epoxy (Ablebond 84-1LMIS) cured at $150^\circ\text{C}$ for $60\text{ minutes}$.
4. Perform ultrasonic aluminum wedge bonding ($25\ \mu\text{m}$ $\text{Al-1\% Si}$ wire at $25^\circ\text{C}$) or thermosonic gold ball bonding ($25\ \mu\text{m}$ $99.99\%\ \text{Au}$ wire at $150^\circ\text{C}$, $60\text{ kHz}$, $50\text{--}100\text{ mW}$, $20\text{--}30\text{ ms}$) connecting to the $100\ \mu\text{m} \times 100\ \mu\text{m}$ aluminum pad arrays.

---

## Machine-Measurable Acceptance Criteria Targets

| Parameter / Metric | Inspection Tool | Acceptance Limit | Physical Units |
| :--- | :--- | :--- | :--- |
| **Total Thickness Variation (TTV)** | Non-contact Optical / Capacitive Gauge | $\le 3.0$ | $\mu\text{m}$ |
| **Die Attach Void Area** | Scanning Acoustic Microscopy (C-SAM) | $< 5.0$ | $\%$ |
| **Die Attach Thermal Resistance ($R_{th}$)** | Thermal Transient Tester (JEDEC JESD51) | $\le 5.0$ | $^\circ\text{C/W}$ |
| **Wire Pull Strength ($25\ \mu\text{m}$ wire)** | Mil-Std-883 Method 2011 Wire Pull Tester | $\ge 4.0$ | $\text{grams-force (gf)}$ |

```text
                  Mechanical Metrology Acceptance Limits
                  ┌────────────────────────────────────┐
                  │░░░░░░░░░░░░░░░░░░░░░░              │
          TTV (um)┤░░░░░░░░░░░░░░░░░░░░░░              │
                  │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
    Die R_th (C/W)┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
Under-Die Void (%)┤▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                  │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
    Bond Pull (gf)┤█████████████████████████████       │
                  │█████████████████████████████       │
                  └┬────────┬────────┬───────┬────────┬┘
                  0.0      1.2      2.5     3.8     5.0 
```

---

## Literature Context Citations
1. **Low-Pressure Chemical Vapor Deposition (LPCVD) of Silicon Nitride Hard Masks**:
   - Dielectric and oxidation mask intrinsic tensile stress ($\sim 1\text{ GPa}$) contributes to wafer bow, mandating tight backside stress-relief removal.
   - Etch chemistry selectivity: $\text{Si}_3\text{N}_4$ exhibits etch rate $< 0.5\text{ nm/min}$ in concentrated $\text{HF}$ and $\text{BOE}$, but is etched selectively in hot phosphoric acid ($\text{H}_3\text{PO}_4$ $85\%$ at $160^\circ\text{C}$).
2. **Ultrasonic Wedge and Ball Wire Bonding Assembly for Die Packaging**:
   - Aluminum bonding pad dimensions: $100\ \mu\text{m} \times 100\ \mu\text{m}$ aluminum squares.
   - Die attach specification: Ablebond 84-1LMIS cured at $150^\circ\text{C}$ for $60\text{ min}$, void area $< 5\%$ via acoustic microscopy, and thermal resistance $R_{th} \le 5^\circ\text{C/W}$.
   - Wire bond pull strength: Mil-Std-883 Method 2011 minimum pull force $\ge 4.0\ \text{grams-force}$ for $25\ \mu\text{m}$ diameter wire.
   - Bonding mechanisms: Ultrasonic wedge bonding ($25\ \mu\text{m}$ $\text{Al-1\% Si}$ at $25^\circ\text{C}$) or thermosonic gold ball bonding ($25\ \mu\text{m}$ $99.99\%\ \text{Au}$ at $150^\circ\text{C}$, $60\ \text{kHz}$, $50\text{--}100\ \text{mW}$, $20\text{--}30\ \text{ms}$).
3. **Sam Zeloof Z1 Garage Semiconductor Journal (2018)**:
   - Rigorous deionized (DI) water rinse protocols and clean surface preparation constraints.

---

## References & Related Files
- [docs/context.yaml](../context.yaml)
- [docs/context2.yaml](../context2.yaml)
- [docs/context3.yaml](../context3.yaml)
- [docs/feol_beol_stackup_specification.md](../feol_beol_stackup_specification.md)

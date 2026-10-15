# SOP: PDK Hierarchical DRC Deck Setup & Memory Array Cell Exclusion Rule Mapping

- **Date**: 2026-10-15
- **Source**: Domain Expert AI (DRAM Foundation VN)
- **Status**: Implemented
- **Process Generation**: Gen 3 (180nm CMOS DRAM)

## Overview & Rationale
In commercial 180nm CMOS MPW shuttle tapeouts, DRAM bitcell arrays utilize aggressive, sub-design-rule lithographic dimensions (e.g. 8F² folded bitline footprint of $0.259\,\mu\text{m}^2$ or 6F² of $0.194\,\mu\text{m}^2$, with bitline/wordline pitch of $360\text{ nm}$ to $400\text{ nm}$). Applying standard standard-cell/logic DRC rule decks indiscriminately across the dense array core triggers thousands of false violations on access transistor channel lengths ($L = 180\text{ nm}$), widths ($W = 220\text{ nm}$), and stacked capacitor contact geometries.

This Standard Operating Procedure defines the hierarchical DRC deck configuration, exclusion layer tagging (`MEM_ARRAY_EXCL`), boundary rule scoping, and peripheral boundary verification.

## Implementation Details
Refer to the operational procedure executed in the main verification pipeline.

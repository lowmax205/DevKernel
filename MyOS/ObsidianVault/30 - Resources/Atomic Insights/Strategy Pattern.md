---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/strategy
created: 2026-10-26
summary: Encapsulate interchangeable calculation and validation algorithms behind uniform strategy contracts to eliminate nested conditionals.
---
# Strategy Pattern isolates interchangeable calculation algorithms

## Problem Solved
Embedding multiple variant calculation rules (e.g., progressive roofing discounts, custom tariff calculators, cadastral boundary adjustments) within monolithic services leads to deeply nested `if-else` or `switch` statements exceeding 3+ branches. Modifying one formula risks destabilizing all others.

## Zentora Standard
1. **Contract Definition:** Extract the variant algorithm into a clean, uniform interface:
   - **TypeScript:** `interface PricingStrategy { calculate(context: QuoteContext): Money; }`
   - **Python:** `class SurveyComputationStrategy(typing.Protocol): def compute(self, points: list[Coordinate]) -> SurveyResult: ...`
2. **Context Delegation:** The consuming domain service receives the selected strategy via injection or context registry and delegates execution without knowing calculation specifics.
3. **Open for Extension:** Adding a new algorithm requires creating a new strategy class rather than editing existing branch logic.

## Applied In
- [[Starter-Project Hub]]

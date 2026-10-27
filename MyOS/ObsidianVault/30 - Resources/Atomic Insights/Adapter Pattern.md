---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/adapter
created: 2026-10-26
summary: Translate external third-party or legacy schemas into clean internal domain representations at application boundaries.
---
# Adapter Pattern insulates domain models from external schemas

## Problem Solved
Ingesting payloads from external APIs, legacy databases, or government agencies directly into core domain services causes foreign naming conventions (`customer_id` vs `customerId`), dirty types, XML structures, and vendor-specific fields to pollute internal domain models.

## Zentora Standard
1. **Boundary Translation:** Implement dedicated Adapter classes or Anti-Corruption Layers (ACL) at the integration boundary:
   - **TypeScript:** `class LandGovSurveyAdapter implements BoundarySurveyPort { toDomain(raw: GovLandResponse): CadastralPlot { ... } }`
   - **Python:** Use Pydantic schema adapters or mapper classes translating external JSON/XML payloads into clean domain dataclasses.
2. **Two-Way Mapping:** Provide explicit `toDomain()` and `toExternal()` methods; domain services must never see raw vendor wire models.
3. **Resilience to Vendor Changes:** When third-party vendors update their API versions or field names, only the Adapter changes—internal domain logic remains untouched.

## Applied In
- [[Starter-Project Hub]]

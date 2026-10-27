---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/builder
created: 2026-10-26
summary: Construct complex domain entities and test fixtures step-by-step to prevent positional argument bugs and fragile constructors.
---
# Builder Pattern simplifies complex multi-field object construction

## Problem Solved
Constructors and factory methods taking 5+ positional parameters are fragile, error-prone, and hard to read. Developers frequently swap adjacent parameters of the same primitive type (e.g., `startDate`, `endDate`, `userId`, `tenantId`), causing silent bugs.

## Zentora Standard
1. **Fluent Construction:** Use fluent builder classes or typed options objects for constructing complex aggregates, search query filters, and test fixtures:
   - **TypeScript:** `new LeaseAgreementBuilder().withTenant(id).withDeposit(amount).withTenure(12).build()`
   - **Python:** Use Pydantic v2 model builders or method chaining: `RentalContractBuilder().set_tenant(...).set_dates(...).build()`
2. **Step Validation:** Defer structural or cross-field validation until the terminal `.build()` invocation, ensuring half-constructed states cannot leak into application services.
3. **Test Factories:** Mandate Builders for test data generation to keep integration and unit tests resilient against schema additions.

## Applied In
- [[Starter-Project Hub]]

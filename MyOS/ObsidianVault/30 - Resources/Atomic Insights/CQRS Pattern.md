---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/cqrs
created: 2026-10-26
summary: Segregate write commands from read queries for high-throughput contested domains while restricting use in simple CRUD.
---
# CQRS Pattern segregates command writes from read query pipelines

## Problem Solved
In high-throughput systems, complex relational write transactions (handling inventory allocations, reservations, and financial ledger locks) clash with read-heavy dashboard queries that require flattened, denormalized, or cached projections.

## Zentora Standard
1. **Command / Query Segregation:** Explicitly split application logic into:
   - **Commands:** Mutate state, execute domain validation, and return minimal identifiers or status.
   - **Queries:** Return optimized DTO projections without altering data state.
2. **Polyglot Implementation:**
   - **TypeScript:** Separate `CreateOrderCommandHandler` (Prisma transaction) from `GetOrderSummaryQueryHandler` (direct raw SQL / read replica).
   - **Python:** Separate write-side domain service commands from read-side FastAPI response query resolvers.

## Anti-Pattern Warning & Restriction
Strictly restrict CQRS to high-throughput, highly contested domains (e.g., roofing manufacturing inventory and high-concurrency order processing). **Strictly reject** CQRS for standard CRUD entities (user settings, static catalogs, basic CRUD forms) where direct Repository + Service models are vastly superior.

## Applied In
- [[Starter-Project Hub]]

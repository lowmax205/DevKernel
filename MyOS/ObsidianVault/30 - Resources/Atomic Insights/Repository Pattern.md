---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/repository
created: 2026-10-26
summary: Decouple persistence from business logic through domain repository interfaces to prevent controller bloat and database lock-in.
---
# Repository Pattern decouples business logic from persistence

## Problem Solved
Scattering direct database queries (e.g., raw SQL, inline ORM calls) across controllers and route handlers couples domain logic tightly to specific storage engines, produces duplicate query logic, makes unit testing difficult, and causes controller bloat.

## Zentora Standard
1. **Interface First:** Define explicit repository interfaces or protocols in the domain/core layer independent of persistence mechanics.
   - **TypeScript:** Use TypeScript `interface` (e.g., `UserRepository`) implemented by Prisma/Drizzle repositories.
   - **Python:** Use `typing.Protocol` or ABCs (e.g., `UserRepositoryProtocol`) implemented by SQLAlchemy/Pydantic session repositories.
2. **Dependency Injection:** Controllers and services depend only on injected repository abstractions, never on raw ORM models or database drivers.
3. **Simplicity Gate (Tier 1):** In basic CRUD entities, keep repository operations direct and cohesive; do not build unnecessary query-builder wrappers over straightforward ORMs.

## Applied In
- [[Starter-Project Hub]]

---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/singleton
created: 2026-10-26
summary: Manage expensive shared backend resources lifecycle while strictly avoiding mutable global state dumping grounds.
---
# Singleton Pattern controls expensive lifecycle resources

## Problem Solved
Repeated instantiation of heavy, long-lived resources (database connection pools, Redis clients, in-memory graph index caches, metrics collectors) wastes memory, exhausts network sockets, and leads to inconsistent lifecycle states across application runtimes.

## Zentora Standard
1. **Scope to Heavy Infrastructure:** Restrict Singletons exclusively to stateless clients or connection pool managers (e.g., Prisma client instances, SQLAlchemy engines, Graphify index caches).
2. **Container Injection Over Ad-Hoc Globals:** Prefer DI container singletons (e.g., NestJS `@Injectable({ scope: Scope.DEFAULT })` or FastAPI app lifetime dependencies) over untyped global variables.
3. **Thread and Concurrency Safety:** Ensure lazy initialization is concurrency-safe and properly handles process termination hooks (graceful pool drain).

## Anti-Pattern Warning
Strictly avoid using Singletons as dumping grounds for mutable global state, tenant context, or request-specific parameters. Shared mutable singletons cause race conditions, cross-request memory leaks, and untraceable bugs in concurrent environments.

## Applied In
- [[DevKernel Hub]]

---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/decorator
created: 2026-10-26
summary: Attach cross-cutting concerns like caching, telemetry, and rate limiting transparently without mutating core domain functions.
---
# Decorator Pattern attaches cross-cutting concerns transparently

## Problem Solved
Mixing telemetry, in-memory caching, audit logging, rate limiting, and permission checks directly into core domain functions pollutes clean business rules with repetitive boilerplate and violates the Single Responsibility Principle.

## Zentora Standard
1. **Transparent Wrapping:** Wrap domain services with decorators, interceptors, or middleware that conform to the exact same contract:
   - **TypeScript:** Use TypeScript method decorators or NestJS interceptors (`@CacheKey()`, `@UseInterceptors(LoggingInterceptor)`).
   - **Python:** Use Python decorators (`functools.wraps`) or FastAPI dependency wrappers: `@timed_metric`, `@cached(ttl=60)`.
2. **Zero Domain Modification:** Core domain services execute pure business calculations without any knowledge of caching stores, log aggregators, or metric clients.
3. **Composability:** Multiple decorators can be cleanly stacked on a single endpoint or repository call in strict execution order.

## Applied In
- [[DevKernel Hub]]
- [[Starter-Project Hub]]

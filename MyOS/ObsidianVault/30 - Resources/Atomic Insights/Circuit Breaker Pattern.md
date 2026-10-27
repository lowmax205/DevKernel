---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/circuit-breaker
created: 2026-10-26
summary: Prevent cascading timeouts and resource exhaustion when calling external APIs by isolating flaky services with stateful circuit breakers.
---
# Circuit Breaker Pattern prevents cascading failure across external services

## Problem Solved
When external third-party services (payment gateways, AI inference endpoints like DeepSeek/OpenAI, government portals, or SMS providers) experience latency spikes or downtime, backend threads and connection pools hang indefinitely, leading to application-wide failure.

## Zentora Standard
1. **Three-State Machine:** Wrap all network boundaries in a stateful breaker:
   - **`CLOSED`:** Normal operation; requests pass through. Consecutive errors increment failure counters.
   - **`OPEN`:** Failure threshold exceeded; calls fail immediately without touching the remote network, returning a cached or graceful fallback response.
   - **`HALF-OPEN`:** After a cooldown timeout, trial requests probe the remote service. If successful, state resets to `CLOSED`; if failing, resets to `OPEN`.
2. **Implementation Standards:**
   - **TypeScript:** Use resilience libraries (e.g., `opossum`, `cockatiel`) or custom HTTP client interceptors with configured timeouts (e.g., 5s).
   - **Python:** Use `pybreaker` or custom asynchronous tenacity retry wrappers with state checks.
3. **Mandatory Fallback:** Every circuit breaker invocation must define an explicit degradation strategy (e.g., cached results, queued retry, or clear descriptive user status).

## Applied In
- [[DevKernel Hub]]
- [[Starter-Project Hub]]

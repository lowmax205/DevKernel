---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/observer
created: 2026-10-26
summary: Decouple cross-cutting secondary side effects from core transactions through asynchronous domain events and isolated subscribers.
---
# Observer Pattern decouples secondary side effects from core operations

## Problem Solved
When a core domain service directly coordinates all downstream secondary tasks (e.g., creating a sales invoice directly calling email notification, loyalty point accrual, analytics tracking, and warehouse dispatch), any downstream failure or latency threatens the primary transaction.

## Zentora Standard
1. **Domain Event Publication:** Core transactional services only mutate primary aggregate state and emit an immutable domain event:
   - **TypeScript:** `eventEmitter.emit('order.placed', new OrderPlacedEvent(orderId, tenantId))`
   - **Python:** `await event_bus.publish(SurveyCompletedEvent(survey_id=survey.id, timestamp=now()))`
2. **Independent Subscribers:** Secondary tasks subscribe to events in isolated handlers or background jobs. Failures in notifications or analytics do not roll back the primary transaction.
3. **Simplicity Gate:** In Tier 1 CRUD workflows, avoid complex event buses or distributed brokers unless asynchronous side effects or external webhooks genuinely exist.

## Applied In
- [[Starter-Project Hub]]

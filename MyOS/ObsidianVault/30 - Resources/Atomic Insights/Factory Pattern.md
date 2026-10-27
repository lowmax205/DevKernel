---
type: permanent
status: budding
tags:
  - topic/architecture
  - topic/backend
  - pattern/factory
created: 2026-10-26
summary: Centralize complex instantiation and provider-switching logic behind unified factory interfaces.
---
# Factory Pattern encapsulates multi-provider object creation

## Problem Solved
Scattering provider-branching conditionals (`if stripe`, `elif paypal`, `elif cash_on_delivery`) across business workflows leaks construction details, violates the Open/Closed Principle, and forces changes across multiple services whenever a new provider or driver is introduced.

## Zentora Standard
1. **Unified Interface:** Define a shared contract (e.g., `PaymentGateway`, `SmsNotificationProvider`) that all concrete implementations honor.
2. **Factory Encapsulation:** Centralize provider resolution into a dedicated factory class or registry function:
   - **TypeScript:** `PaymentGatewayFactory.get(provider: PaymentProvider): PaymentGateway`
   - **Python:** `class StorageProviderFactory: def get_provider(self, kind: StorageKind) -> StorageProtocol`
3. **Configuration-Driven:** Resolve concrete types dynamically using validated environment config or database tenant settings rather than hardcoded string checks.

## Applied In
- [[Starter-Project Hub]]

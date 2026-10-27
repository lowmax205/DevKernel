---
type: permanent
status: budding
tags:
  - topic/frontend
  - topic/backend
  - topic/architecture
created: 2026-10-21
summary: Public settings hydration hooks must not overwrite authenticated admin state after initial load, and backend partial settings updates must deep-merge stored secret sub-objects.
---
# Public settings synchronization on load must not overwrite authenticated secret configuration state on save

When an application exposes both a public settings context (which strips sensitive fields such as `email_config` SMTP credentials for unauthenticated consumers) and an authenticated admin settings editor, re-running a `useEffect` that syncs local form state from the public context whenever `refreshSettings()` is called will wipe out the admin form's sensitive fields immediately after saving.

To prevent state loss:
1. Guard initial form hydration in the admin page with a ref (`initialLoadedRef`) so background refreshes of public settings do not clobber active editor state.
2. In the backend update service (`SettingsService.update`), merge incoming sub-objects (`email_config`) with the existing persisted JSONB record and preserve stored secrets (`auth_pass`) when the password input is blank.

## Context & Connections
- Discovered during: [[[APS] 2026-10-21 - Zentora Bootstrap and v1.4.0]]
- Applied in: [[Starter-Project Hub]]

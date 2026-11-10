# ZentoraDev - Product requirements

Review: evidence-backed draft; pending developer review of product decisions. The root workspace is the subject of this document, not an individual client application.

## Problem and audience

Developers and AI coding agents working across independent client repositories need reliable context, consistent engineering rules, and persistent project memory. ZentoraDev is the local-first control workspace for those repositories. DevKernel is the reusable starter derived from this system.

## Current capabilities

- Route live status through project cards, history through Obsidian, and connections through Graphify.
- Bootstrap new and existing child repositories using shared guidance and global skills.
- Provision agent adapters and recall focused context without loading entire repositories.
- Create six planning documents through manual bootstrap and automatic sync, followed by repo inspection and a developer interview.
- Provide Cloudflare's security-audit skill globally for explicitly requested audits.

## Acceptance criteria for documentation onboarding

Both onboarding paths create missing documents, preserve authored content, and add an idempotent entrypoint reference. New projects use templates plus interviews; existing projects use evidence-backed drafts plus interviews. Relevant documentation gaps are resolved before planned feature work. Diagnosis, urgent fixes, and documentation work can proceed with gaps recorded.

Consolidation follows developer review. Existing architecture artifacts, central records, ADRs, and tickets keep their canonical locations. Security audits remain on demand and never run during bootstrap.

## Boundaries and open questions

This workspace does not implement client application features or duplicate their domain skills. This change does not backfill all child repositories or require security audits for releases.

Developer review: confirm whether these current capabilities define the ongoing product baseline. No new roadmap or quantitative business target has been approved.

Evidence: [root overview](../README.md), [agent routing](../AGENTS.md), [bootstrap](../MyOS/_meta/bootstrap_repo.ps1), and [automatic sync](../MyOS/_meta/zentora_sync.py).

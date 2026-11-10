# DevKernel Workspace

This Windows workspace can have any folder name or location. Resolve its root
from this file or the setup scripts, never from a hardcoded drive or parent workspace.

- Follow `MyOS/_meta/profiles/core.md`.
- Read live status and next steps in `MyOS/projects/<slug>.md`.
- Keep project history under `MyOS/ObsidianVault/10 - Projects/<Repository Name>/`.
- Keep reusable facts under `MyOS/ObsidianVault/30 - Resources/Atomic Insights/`.
- Never create a second vault or notes directly at the vault root.
- Repository registrations are local and ignored: `.devkernel/local.json`.
- Use `setup.ps1` or `MyOS/_meta/bootstrap_repo.ps1` to register repositories.
- Preserve existing agent instructions and skills by default. Reset only when explicitly requested.
- Global skills and optional apps are installed separately. Never mirror or clear global skills.
- Engineering policies are opt-in per repository through `-EngineeringProfile`.
- Verify script syntax, affected behavior, and clean export before claiming setup changes complete.

## Maintainer source checkout

This checkout retains historical architecture, notes, and external skill bundles.
Use the allowlisted export described in README.md to produce the shareable starter.
The accepted starter scope is in `.docs/starter-decisions.md`.

## Documentation onboarding and security

Read `.docs/README.md` for this checkout's six planning documents. Follow
`.docs/agents/documentation-onboarding.md` for evidence-backed drafts, developer
interviews, and reviewed consolidation. Keep Archify artifacts in place and link
them from `.docs/ARCHITECTURE.md`. The root docs describe this starter, not the
parent ZentoraDev workspace. Registration scaffolds missing project docs; sync
remains read-only. Cloudflare's pinned `security-audit` is the explicit external
skill exception included in clean exports. Global installation remains separate
and audits remain on demand.

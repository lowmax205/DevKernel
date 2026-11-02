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

## Documentation and security

Registration scaffolds six `.docs` project planning files and
`.docs/agents/documentation-onboarding.md` in each registered project. Follow that
workflow to draft from evidence and interview the developer. Preserve existing
docs, canonical records, and Archify artifacts; consolidate only after review.
Sync stays read-only. The pinned Cloudflare `security-audit` skill is included as
an explicit third-party export exception; install it separately into your agent
without replacing existing global skills. Audits run only when requested.

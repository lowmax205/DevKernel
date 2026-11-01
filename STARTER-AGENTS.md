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

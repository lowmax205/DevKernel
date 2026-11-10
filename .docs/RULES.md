# DevKernel - Rules

## Canonical instructions

Follow [AGENTS.md](../AGENTS.md), [core profile](../MyOS/_meta/profiles/core.md), and [accepted starter decisions](starter-decisions.md). Preserve existing project standards; report conflicts for review. Engineering policies remain opt-in. Do not import the parent ZentoraDev workspace's personal registry, history, or mandatory engineering policies.

## Documentation and security

Follow [onboarding](agents/documentation-onboarding.md): inspect evidence, draft, interview, then consolidate reviewed planning docs with redirects. Preserve canonical memory, ADRs, tickets, and architecture artifacts. Resolve feature-relevant gaps before planned features; diagnosis, urgent fixes, and docs work may proceed with gaps recorded.

Cloudflare security-audit is the explicit third-party clean-export exception. Its [provenance](../MyOS/_meta/global-skills/security-audit/UPSTREAM.md) and MIT license travel with the complete skill. Agent installation remains separate; setup never mirrors or clears global skills. Full audits are on demand and must honor upstream sandbox and validator requirements. Native Windows validator CLIs are unsupported at the pinned revision.

## Verification

From this repository:

```powershell
python -m unittest discover -s tests -v
powershell -NoProfile -ExecutionPolicy Bypass -File tests\verify-powershell.ps1
python MyOS/_meta/check_portable_paths.py
git diff --check
```

There are no application lint/build scripts or runtime package dependencies. Validate Python syntax, PowerShell syntax, UTF-8 without BOM, affected behavior, and allowlisted clean exports. Use disposable Git repositories for tests. Read-only sync can be run without changing registrations. For bundled upstream validators, report known Windows failures separately; never bypass their protections.

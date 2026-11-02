# Upstream provenance

- Source: https://github.com/cloudflare/security-audit-skill
- Skill path: skills/security-audit
- Revision: c1c8a8c1471069fb0e188eeaff69b8e8db6564a8
- License: MIT; see LICENSE.
- Complete upstream skill directory retained without modifications.
- Bundled in DevKernel and clean exports as an explicit third-party exception. Install into the agent separately; setup does not change global skills or copy this skill into project repos.
- Invoke on demand: `security audit this codebase`. Requires Node.js and an agent with sub-agent support for full audits. Follow upstream sandbox requirements for target execution.

## Native Windows limitation at this revision

The validator CLIs refuse input when Node does not expose O_NOFOLLOW and O_NONBLOCK. Native Windows is affected (upstream https://github.com/cloudflare/security-audit-skill/issues/117). The full findings test suite has seven failing CLI tests here; the coverage suite skips unsupported cases. Use a supported Linux runtime for full audits and the upstream sandbox controls for target execution. Do not bypass the validators or present an unvalidated audit as complete. Guidance mode remains available. Upstream code is intentionally unchanged.

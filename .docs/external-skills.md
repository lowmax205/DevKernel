# Skills installed separately

DevKernel includes its own `devkernel-manager` and `setup-agent` skills and the
pinned Cloudflare `security-audit` in the clean starter. The security skill is the
explicit third-party exception, not DevKernel-owned code. Setup does not install skills into your user profile automatically.
To use these skills, copy their directories from `MyOS/_meta/global-skills/` into
your agent's documented skills directory, preserving any existing version first.

External skills such as grill-me, to-spec, to-tickets, TDD, code-review, Archify,
Context7, and git-commit are optional. Obtain them from their maintainers, review
their instructions and licenses, and install them using your agent's supported
skill mechanism. Consult [AI Hero](https://www.aihero.dev/) for its workflows and
[the Agent Skills specification](https://agentskills.io/) for skill structure.
There is no universal Skill tool: a workflow must match the tools your agent provides.

The source checkout retains previous bundled assets for review. The export
allowlist excludes other external skills, their dependencies, caches, and licenses.
Never distribute those source bundles as if they were DevKernel-owned code.

## Cloudflare security-audit

The complete upstream skill is in `MyOS/_meta/global-skills/security-audit/`.
Its UPSTREAM.md records revision `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`,
source, MIT attribution, and platform limitations. Keep LICENSE and all supporting
files with it. Install that directory using the agent's supported skill mechanism;
preserve existing installations and never clear global skills. Node.js and audits
are not prerequisites for core workspace setup.

After installation, ask `security audit this codebase`. Full audits require Node.js,
sub-agent support, and upstream sandbox controls. At this revision validator CLIs
reject inputs on native Windows because O_NOFOLLOW/O_NONBLOCK protections are
unavailable; use a supported Linux runtime for full audits. Guidance mode remains
available. Never bypass validators or report an unvalidated full audit as verified.
See https://github.com/cloudflare/security-audit-skill/issues/117.

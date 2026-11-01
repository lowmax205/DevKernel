# Skills installed separately

DevKernel includes only its own `devkernel-manager` and `setup-agent` skills in the
clean starter. Setup does not install skills into your user profile automatically.
To use these skills, copy their directories from `MyOS/_meta/global-skills/` into
your agent's documented skills directory, preserving any existing version first.

External skills such as grill-me, to-spec, to-tickets, TDD, code-review, Archify,
Context7, and git-commit are optional. Obtain them from their maintainers, review
their instructions and licenses, and install them using your agent's supported
skill mechanism. Consult [AI Hero](https://www.aihero.dev/) for its workflows and
[the Agent Skills specification](https://agentskills.io/) for skill structure.
There is no universal Skill tool: a workflow must match the tools your agent provides.

The source checkout retains previous bundled assets for review. The export
allowlist excludes all external skills, their dependencies, caches, and licenses.
Never distribute those source bundles as if they were DevKernel-owned code.

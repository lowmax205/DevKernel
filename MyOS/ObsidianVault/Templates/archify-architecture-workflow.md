---
type: workflow-template
status: active
tags:
  - workflow/archify
  - topic/architecture
created: 2026-10-17
summary: Reusable Zentora Dev workflow prompt and checklist for generating interactive Archify system architecture diagrams inside .docs/architecture/ for any repository.
---
# Archify Interactive System Architecture Workflow

Use this template or say `archify {{Project-Name}}` to generate a verified interactive architecture diagram inside `.docs/architecture/` for any project in `<ZENTORA_ROOT>/Repos/` and wire it into the 3-layer Zentora Dev architecture.

> **Important Convention:** Always output architecture artifacts into `.docs/architecture/` (never `docs/architecture/`), matching the workspace `.docs` standard.

## Prompt Template

```markdown
Use our global `archify` skill (`tt-a1i/archify`) to generate an interactive architecture diagram for `{{Target-Project-Name}}`, and integrate the result into our Zentora Dev architecture:

### 1. Generate Interactive Architecture Diagram
- Inspect the codebase in `<ZENTORA_ROOT>/Repos/{{Target-Project-Name}}` (entry points, directory structure, services, API routes, data layer, state management, and external dependencies).
- Use `archify` to generate a complete visual system architecture diagram.
- Output the diagram as a standalone interactive viewer (`.docs/architecture/system-architecture.html`) and an SVG/Mermaid file (`.docs/architecture/system-architecture.mmd` or `.svg`) inside `<ZENTORA_ROOT>/Repos/{{Target-Project-Name}}/.docs/architecture/`.
- Ensure it includes:
  - Frontend / UI Layer
  - Backend / API Layer
  - Database / External Integrations
  - Data flow directions and key component interactions

### 2. Follow Zentora Dev "One Home Per Fact":
- **Update Obsidian Project Hub Note:** 
  Open `<ZENTORA_ROOT>/MyOS/ObsidianVault/10 - Projects/{{Target-Project-Name}}/{{Target-Project-Name}} Hub.md` and add an `## Architecture` section embedding or linking the new diagram (`[[system-architecture.html]]` at `.docs/architecture/system-architecture.html` and the native Mermaid code block).
- **Update ICM Project Card:**
  Open `<ZENTORA_ROOT>/MyOS/projects/{{target-project-name}}.md` and add the diagram path under the `## Home` table:
  `| Architecture Diagram | <ZENTORA_ROOT>/Repos/{{Target-Project-Name}}/.docs/architecture/system-architecture.html |`

### 3. Open and Verify
- Once created, provide the exact local file URL and terminal command to open `.docs/architecture/system-architecture.html` in my default browser so I can interact with the diagram immediately.
```

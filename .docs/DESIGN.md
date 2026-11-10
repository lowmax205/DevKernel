# DevKernel - Design

## Applicability

This is a Windows command-line starter and Markdown knowledge workspace. Application UI colors, typography tokens, responsive components, and a frontend library are not applicable. Future UI requirements need a separate developer interview.

## Interaction conventions

Maintain one interactive setup entrypoint and repeatable noninteractive flags. Dry runs are previews; existing configuration is preserved unless reset is explicit. Print a useful interview prompt after registration without launching agents or audits. Missing optional tools do not block setup.

Use readable Markdown, verified relative links, copyable PowerShell 5.1 commands, ASCII punctuation, and UTF-8 without BOM. Keep machine-specific locations in ignored pointers. Keep Archify visuals in place and navigate through [ARCHITECTURE.md](ARCHITECTURE.md).

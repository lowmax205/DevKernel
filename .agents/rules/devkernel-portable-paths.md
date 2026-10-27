# DevKernel Portable Paths

- Never hardcode a drive letter or absolute path (e.g. `<drive>:\...`) in committed files. Use workspace-relative paths or `<ZENTORA_ROOT>`.
- Scripts/hooks resolve root from their own location (`Path(__file__)`, `$PSScriptRoot`, `git rev-parse --show-toplevel`), overridable by `ZENTORA_ROOT`.
- Never run blanket search-and-replace for paths or single letters across the repo; it silently corrupts code (a variable like `f` becomes another name). Use anchored, reviewed edits and check `git diff` on `.py/.ps1/.mjs`.
- Discover child repos by scanning `<root>/Repos/**`. A missing repo must warn, never auto-archive or flip a project to Vault-Only.
- Generated machine-specific absolute paths belong in gitignored output only.

### Optional engineering profile
- Inspect exact dependency versions before generating library-specific code.
- For APIs with breaking changes, consult version-specific official documentation through Context7 when available; otherwise use official documentation and report the limitation.
- Investigate dependency errors using official issues and changelogs.
- Keep ordinary CRUD at Repository + Service complexity. Add Strategy, Adapter, Observer, or Circuit Breaker only for demonstrated needs.
- Keep SQL and third-party API calls out of controllers.
- Use the project's lint, build, and affected tests as the completion gate.
- Keep conventional commits and an Unreleased changelog when the repository adopts them.
- Release automation and branch policies remain explicit project choices.

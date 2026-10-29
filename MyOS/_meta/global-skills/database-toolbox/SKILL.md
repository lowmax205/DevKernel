---
name: database-toolbox
description: Inspect database schemas, query tables, and perform data operations safely using Database MCP servers and GCP DB Toolbox.
---

# Database MCP Toolbox & Inspection Skill

Use this skill when interacting with databases (PostgreSQL, SQLite, MySQL, Cloud SQL) via Model Context Protocol database tools.

## Safety First: Two-Tier Execution Policy

### 1. Tier 1: Read-Only Operations (Allowed by Default)
- Schema inspection: `list_tables`, `describe_table`, `show_columns`, `PRAGMA table_info`.
- Read queries: `SELECT` statements with explicit `LIMIT` clauses (maximum 50 rows by default).
- Query plan analysis: `EXPLAIN` or `EXPLAIN ANALYZE` on read operations.

### 2. Tier 2: Mutating Operations (Requires User Confirmation)
- Any statement modifying schema or data: `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`, `TRUNCATE`.
- Never execute destructive mutations without presenting the exact SQL statement and receiving affirmative confirmation from the user.
- Prefer executing mutations inside explicit transactions with rollback capabilities when testing scripts.

## Environment & Secrets
- Never hardcode database credentials in project code, markdown, or chat sessions.
- Reference environment variables (e.g. `DATABASE_URL`, `POSTGRES_PASSWORD`, `SQLITE_PATH`) or load them via local `.env` files.
- Mask sensitive personal identifiable information (PII) and password hashes when displaying table rows.


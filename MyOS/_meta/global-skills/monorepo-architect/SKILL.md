---
name: monorepo-architect
description: Orchestrates full-stack Turborepo monorepo architecture, enforcing strict dependency boundaries between Next.js web, Expo mobile, NestJS API, and shared packages (types, validation, database, shared-ui).
---

# The /monorepo-architect Skill

Use this skill when scaffolding packages, configuring workspace dependencies, adding build scripts, or debugging cross-package compilation issues in full-stack monorepos.

## Monorepo Topography

```
monorepo/
├── apps/
│   ├── web/               # Next.js 15+ (Web Application Portal)
│   ├── mobile/            # Expo 51+ / React Native (Cross-platform Mobile App)
│   └── api/               # NestJS / Express (REST API, WebSockets, ORM, Background Jobs)
├── packages/
│   ├── types/             # Pure TypeScript types, DTO interfaces, enum definitions
│   ├── validation/        # Zod validation schemas shared across Web, Mobile, and API
│   ├── database/          # Database schema (Prisma/Drizzle), relations, migrations, seeders
│   ├── api-client/        # Type-safe client hooks & API service layer
│   └── shared-ui/         # Cross-platform theme tokens, formatters (currency, dates), icons
├── turbo.json             # Turborepo task pipeline configuration
├── pnpm-workspace.yaml    # Workspace definition
└── package.json           # Root package.json
```

## Architectural Rules & Invariants

### 1. Unidirectional Dependency Rule
- **Allowed**: `apps/*` -> `packages/*`
- **Allowed**: `packages/validation` -> `packages/types`
- **Allowed**: `packages/database` -> `packages/types`
- **Allowed**: `packages/api-client` -> `packages/types`, `packages/validation`
- **STRICTLY FORBIDDEN**: `packages/*` importing anything from `apps/*`.
- **STRICTLY FORBIDDEN**: `packages/database` importing from `apps/api`.
- **STRICTLY FORBIDDEN**: Leaking Node-only or backend modules (`pg`, `fs`) into `apps/mobile` or `packages/shared-ui`.

### 2. Package Exports & Internal Linking
- **Backend-Consumed Packages (`@repo/types`, `@repo/validation`, `@repo/database`)**:
  Backend apps (Node / CommonJS / ESM) resolve packages via compiled bundles and `.d.ts` declaration maps:
  ```json
  {
    "name": "@repo/database",
    "version": "0.0.1",
    "main": "./dist/index.js",
    "types": "./dist/index.d.ts",
    "exports": {
      ".": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      }
    }
  }
  ```
  These packages must define a `"build": "tsc"` script and emit to `./dist/`.
- **Client-Only Packages (`@repo/api-client`, `@repo/shared-ui`)**:
  Consumed exclusively by Next.js and Expo with bundler resolution; they may point directly to `./src/index.ts`:
  ```json
  {
    "name": "@repo/shared-ui",
    "version": "0.0.1",
    "main": "./src/index.ts",
    "types": "./src/index.ts",
    "exports": {
      ".": "./src/index.ts"
    }
  }
  ```

### 3. Turborepo Task Pipeline (`turbo.json`)
Ensure tasks declare explicit inputs and outputs for deterministic caching:
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**", "dist/**"]
    },
    "test": {
      "dependsOn": ["^build"]
    },
    "typecheck": {
      "dependsOn": ["^build"]
    },
    "lint": {}
  }
}
```

### 4. Shared Formatting Utilities
All currency, date/time formatters, and calculation display functions must be centralized in `packages/shared-ui` or `packages/types` so Web and Mobile render identical values.

### 5. Fixed Port Allocation & Anti-Collision Standards
To prevent startup race conditions, port collisions, and unpredictable dynamic port hopping, every application must pin its port explicitly:
- **`3000`**: `apps/web` (`next dev --turbopack -p 3000`)
- **`4000`**: `apps/api` (`process.env.API_PORT || process.env.PORT || 4000`)
- **`8081`**: `apps/mobile` (`expo start --port 8081`)
- **`4983`**: `packages/database` (`db studio --port 4983`)
- **`5432`**: Local PostgreSQL daemon
Client packages must consume `NEXT_PUBLIC_API_URL="http://localhost:4000"` and `EXPO_PUBLIC_API_URL="http://localhost:4000"`.

# Graph Report - MyOS  (2026-10-27)

## Corpus Check
- 194 files · ~1,346,689 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 4 file(s) not represented in the graph (top: (none) 2, .mdc 2)

## Summary
- 2595 nodes · 7067 edges · 133 communities (119 shown, 14 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 165 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b8a7d9a1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- archify.mjs
- check-update.mjs
- render-erd.mjs
- architecture-delta.mjs
- render-class.mjs
- workflow-v2.mjs
- zentora_sync.py
- asArray
- render-sequence.mjs
- render-lifecycle.mjs
- atomic-output.mjs
- build
- visual-check.mjs
- generated-validators.mjs
- render-architecture.mjs
- render-waterfall.mjs
- createRouter
- finalize.mjs
- render-timeline.mjs
- brand-marks.mjs
- path-semantics.mjs
- render-tree.mjs
- geometry.mjs
- check-render-output.mjs
- i18n.mjs
- route-quality.mjs
- preview.mjs
- dataflow-compiler.mjs
- validateReadablePinnedGeometry
- anchor
- func3
- Codebase Design
- workflow-compiler.mjs
- ref_node_path
- During the session
- compileWorkflowInternal
- pathFor
- cli.mjs
- package.json
- Delivery contract
- renderMembers
- PipeCdp
- tasteskill: Anti-Slop Frontend Skill
- Appendix B - Canonical Sources (read these before reinventing)
- Diagnosing Bugs
- authoring-contract.md
- portable-path.mjs
- parseAttrs
- scripts
- DevKernel Hub.md
- scenarios.mjs
- Authoring contract
- detail
- desktop-readability.mjs
- diagnostics.mjs
- validatePortablePath
- Steps
- Test-Driven Development
- Process
- generate-brand-marks.mjs
- memberRows
- 4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)
- Mode placement
- generate-validators.mjs
- legend.mjs
- pathFor
- collectArrows
- 10. REFERENCE VOCABULARY (Pattern Names the Agent Should Know)
- Viewer Runtime reference
- Workflow Renderer
- Phase 2: Release, `production` Branch Sync, Tagging & Major-Only GitHub Release (`patch` | `minor` | `major`)
- Architectural Rules & Invariants
- to-spec/SKILL.md
- Entity-Relationship Renderer
- Archify JSON IR Schemas
- Process
- 9. AI TELLS (Forbidden Patterns)
- Repository-backed authoring
- Class and Interface Renderer
- Sequence Renderer
- Hierarchy and Tree Renderer
- Archify
- APPENDICES - Real Source-Backed Reference Material
- 11. REDESIGN PROTOCOL
- 3. DEFAULT ARCHITECTURE & CONVENTIONS
- 6. PERFORMANCE & ACCESSIBILITY GUARDRAILS
- automatic-labels.mjs
- Data Flow Renderer
- Lifecycle Renderer
- analyzeSvgPath
- Third-party notices
- CQRS Pattern segregates command writes from read query pipelines
- Singleton Pattern controls expensive lifecycle resources
- Authoring defaults
- Starter-Project Hub.md
- 12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)
- Claude Code Guidelines — Zentora Dev (MyOS)
- 8. DARK MODE PROTOCOL
- The /selfhost-devops Skill
- DevKernel Hub
- Starter-Project Hub
- Adapter Pattern insulates domain models from external schemas
- Builder Pattern simplifies complex multi-field object construction
- Circuit Breaker Pattern prevents cascading failure across external services
- Decorator Pattern attaches cross-cutting concerns transparently
- Observer Pattern decouples secondary side effects from core operations
- Strategy Pattern isolates interchangeable calculation algorithms
- DevKernel Manager Skill
- hitl-loop.template.sh
- Factory Pattern encapsulates multi-provider object creation
- DevKernel Tracker
- normalizeRoutePoints
- Setup Agent Skill
- DevKernel
- Starter-Project
- brand-marks/README.md
- manifest.json
- update-awareness.md
- [DEV] 2026-10-27 - Multi-Agent Architecture and Knowledge Codification
- routeBudgetMetrics
- Repository Pattern decouples business logic from persistence
- ChatGPT CLI & OpenAI Codex Configuration — Zentora Dev
- 1. THE THREE DIALS (Core Configuration)
- autoViewBox
- sideFor
- devkernel-portable-paths.md
- connectionEndpointSide
- inferredSides

## God Nodes (most connected - your core abstractions)
1. `compileWorkflowInternal()` - 198 edges
2. `asArray()` - 100 edges
3. `textUnits()` - 72 edges
4. `compileDataflow()` - 71 edges
5. `escapeHtml()` - 69 edges
6. `createRouter()` - 63 edges
7. `build()` - 61 edges
8. `rectsOverlap()` - 54 edges
9. `commandDeliver()` - 44 edges
10. `normalizeRoutePoints()` - 40 edges

## Surprising Connections (you probably didn't know these)
- `Layout and routing` --references--> `sideFor()`  [INFERRED]
  MyOS/_meta/global-skills/archify/renderers/erd/README.md → MyOS/_meta/global-skills/archify/renderers/class/render-class.mjs
- `Waterfall` --references--> `detail()`  [INFERRED]
  MyOS/_meta/global-skills/archify/references/authoring-contract.md → MyOS/_meta/global-skills/archify/renderers/class/render-class.mjs
- `Input` --references--> `detail()`  [INFERRED]
  MyOS/_meta/global-skills/archify/renderers/timeline/README.md → MyOS/_meta/global-skills/archify/renderers/class/render-class.mjs
- `Input` --references--> `detail()`  [INFERRED]
  MyOS/_meta/global-skills/archify/renderers/waterfall/README.md → MyOS/_meta/global-skills/archify/renderers/class/render-class.mjs
- `GitHub Copilot Custom Instructions — Zentora Dev` --references--> `build()`  [INFERRED]
  MyOS/_meta/agent-adapters/copilot/copilot-instructions.md → MyOS/_meta/global-skills/archify/renderers/dataflow/dataflow-compiler.mjs

## Import Cycles
- None detected.

## Communities (133 total, 14 thin omitted)

### Community 0 - "archify.mjs"
Cohesion: 0.05
Nodes (123): acquireDeliveryLock(), artifactCheckMaxBuffer(), artifactIdentity(), assertDeliveryOwnership(), assertOwnedDeliveryLock(), beginDeliveryAttempt(), canonicalExistingDeliveryOutput(), captureDeliveryTargetState() (+115 more)

### Community 1 - "check-update.mjs"
Cohesion: 0.06
Nodes (110): acquireOperation(), assertBoundedRegularFile(), assertCacheTargetAbsent(), assertRenameableCacheEntry(), assertSafeCacheEntry(), assertSafeDirectory(), assertSafeRegularFile(), cacheMkdir() (+102 more)

### Community 2 - "render-erd.mjs"
Cohesion: 0.04
Nodes (85): inferredSides(), bandedLayout(), DEFAULT_ER_GRID, entityHeight(), erGridLayout(), gridColumn(), resolvedEntityWidth(), resolveEntityPos() (+77 more)

### Community 3 - "architecture-delta.mjs"
Cohesion: 0.06
Nodes (82): addNodeMarker(), addState(), annotateArchitectureSideSvg(), architectureDeltaChangeRows(), ArchitectureDeltaError, BOUNDARY_FIELDS, boundaryChangeMap(), boundaryElements() (+74 more)

### Community 4 - "render-class.mjs"
Cohesion: 0.06
Nodes (32): bands, busGroups, busPaths, busRouteConflict(), cliArgs, { diagram: cd, template, outPath, sourceEvidence }, __dirname, GENERALIZATION (+24 more)

### Community 5 - "workflow-v2.mjs"
Cohesion: 0.16
Nodes (27): clone(), diagnostic(), expandableViewBox(), legacyLayoutProbe(), legacyRequirementProbe(), migrateWorkflowDocument(), requiredViewBoxFrom(), result() (+19 more)

### Community 6 - "zentora_sync.py"
Cohesion: 0.06
Nodes (29): main(), scan(), tracked_files(), detect_project_context(), extract_keywords(), format_capsule(), load_graph(), main() (+21 more)

### Community 7 - "asArray"
Cohesion: 0.13
Nodes (42): boundaryRect(), componentDiagnosticBox(), hasAutomaticRouteGeometry(), rectContains(), validateArchitecture(), validateClassDiagram(), validateDataflow(), recordDiagnostic() (+34 more)

### Community 8 - "render-sequence.mjs"
Cohesion: 0.07
Nodes (68): renderStageHeader(), preferredWidth(), validateStructure(), arrowClass, automaticCanvasWidth(), automaticHeight, compositionFrames, contentBottom (+60 more)

### Community 9 - "render-lifecycle.mjs"
Cohesion: 0.05
Nodes (63): assignArcLevels(), assignTracks(), bracketOf, brackets, bracketTargets, canvasWidth, countCrossings(), depth (+55 more)

### Community 10 - "atomic-output.mjs"
Cohesion: 0.13
Nodes (49): captureOwnedDeliverySidecars(), args, backupOwnedPublishedEntry(), restoreOwnedBackup(), unlinkOwnedEntry(), backupPublicRegularFileBinding(), captureAtomicOutput(), captureRegularFileBinding() (+41 more)

### Community 11 - "build"
Cohesion: 0.14
Nodes (27): GitHub Copilot Custom Instructions — Zentora Dev, build(), compactCorridors(), crossingFlows(), detourFor(), endpointStubs(), extraLabelLineMasksRoute(), flowSides() (+19 more)

### Community 12 - "visual-check.mjs"
Cohesion: 0.08
Nodes (57): appendEvidenceCleanupWarning(), appendEvidencePublicationFailure(), baseReceipt(), beginVisualEvidenceWrite(), CAPTURE_VIEWPORTS, CHROME_NO_SANDBOX_ENV, CHROME_STARTUP_TIMEOUT_MS, cleanupStagedEvidence() (+49 more)

### Community 13 - "generated-validators.mjs"
Cohesion: 0.04
Nodes (53): pattern10, pattern11, pattern12, pattern13, pattern133, pattern14, pattern15, pattern16 (+45 more)

### Community 14 - "render-architecture.mjs"
Cohesion: 0.06
Nodes (49): DEFAULT_GRID, gridLayout(), resolveComponentPos(), validateGridPlacement(), architectureLegendEntries, autoViewBoxFor(), boundaryLabelWidth(), buildLayoutReport() (+41 more)

### Community 15 - "render-waterfall.mjs"
Cohesion: 0.05
Nodes (47): byId, children, cliArgs, details, { diagram: wf, template, outPath, sourceEvidence }, __dirname, dotX(), footprint (+39 more)

### Community 16 - "createRouter"
Cohesion: 0.15
Nodes (43): createRouter(), alignFacingPorts(), automaticEndpoint(), cachePath(), candidateSidePairs(), collinearBacktrack(), collinearOverlapLength(), computePath() (+35 more)

### Community 17 - "finalize.mjs"
Cohesion: 0.10
Nodes (42): allChecksPassed(), browserEvidence(), captureReceipt(), compactFinalizeReceipt(), consolidateDiagnostics(), defaultFinalizeReceiptPath(), defaultFinalizeSummaryPath(), defaultRunner() (+34 more)

### Community 18 - "render-timeline.mjs"
Cohesion: 0.06
Nodes (44): breaks, buildLayoutReport(), cards, cliArgs, clockLabel(), { diagram: tl, template, outPath, sourceEvidence }, __dirname, durationLabel() (+36 more)

### Community 19 - "brand-marks.mjs"
Cohesion: 0.09
Nodes (36): asUrl(), BASIC_HTML_REFERENCES, beforeDeadline(), captureBrandReference(), captureRemoteBrand(), captureTimeoutMilliseconds(), checkedFetch(), COLLECTIONS (+28 more)

### Community 20 - "path-semantics.mjs"
Cohesion: 0.11
Nodes (53): visualEvidenceOwnershipMatches(), authoredOutputDiagnostic(), nativeOutputDiagnostic(), rejectWindowsIpcShare(), resolveNativeOutputDirectory(), throwNativeOutputDiagnostic(), validateNativeOutputPath(), validateWindowsNativeComponent() (+45 more)

### Community 21 - "render-tree.mjs"
Cohesion: 0.07
Nodes (48): renderBoundaryFrame(), renderBoundaryLabel(), renderConnectionLabel(), renderSvg(), renderSvg(), renderSvg(), markAttrs(), svgAccessibleText() (+40 more)

### Community 22 - "geometry.mjs"
Cohesion: 0.10
Nodes (33): anchorFitsCanvas(), arrowClassMap, AUTHORED_PLAN_KEYS, axisCanvasOverflow(), clampAnchorToCanvas(), collectLabelCanvasOverflow(), collectLabelRouteClearance(), collinearForward() (+25 more)

### Community 23 - "check-render-output.mjs"
Cohesion: 0.08
Nodes (21): checks, collectLegendCollisions(), collectRelationshipCrossings(), composition, crossProduct(), ELEMENT_NUMERIC_ATTRS, HTML_VOID_ELEMENTS, htmlPath (+13 more)

### Community 24 - "i18n.mjs"
Cohesion: 0.08
Nodes (41): componentContext(), BUNDLED_CATALOGS, bundledCatalog(), bundledLocaleFor(), CANONICAL_KEYS, CANONICAL_PLACEHOLDERS, catalogFor(), classifyTranslations() (+33 more)

### Community 25 - "route-quality.mjs"
Cohesion: 0.12
Nodes (27): boundsForPoints(), boundsForRects(), cleanRouteDetourProblems(), collinearOverlap(), DEFAULTS, emptyControlPointClearance(), expandedRect(), inferredSide() (+19 more)

### Community 26 - "preview.mjs"
Cohesion: 0.13
Nodes (32): atomicOutputError(), atomicOutputFailure(), captureOwnedDirectory(), cleanupOwnedDirectory(), cliPath, compactMessage(), diagramTypes, here (+24 more)

### Community 27 - "dataflow-compiler.mjs"
Cohesion: 0.17
Nodes (38): renderComponent(), renderConnectionPath(), renderRelationshipPath(), renderType(), compileDataflow(), attempt(), labelPoint(), renderFlowLabel() (+30 more)

### Community 28 - "validateReadablePinnedGeometry"
Cohesion: 0.16
Nodes (29): acceptsFix(), authoredPinEvidence(), authoredRouteAssertionFields(), combinations(), conflictPinsFromRemovalSets(), endpointSideIsHonored(), hasAuthoredRouteAssertions(), presentChannelPins() (+21 more)

### Community 29 - "anchor"
Cohesion: 0.21
Nodes (28): anchor(), automaticPortSpread(), chosenSide(), defaultFromSide(), defaultToSide(), joinRoutePoints(), automaticEndpointRepairs(), automaticForwardReversePx() (+20 more)

### Community 30 - "func3"
Cohesion: 0.13
Nodes (24): func3(), validate20(), validate22(), validate24(), validate27(), validate28(), validate30(), validate31() (+16 more)

### Community 31 - "Codebase Design"
Cohesion: 0.09
Nodes (21): 1. In-process, 2. Local-substitutable, 3. Remote but owned (Ports & Adapters), 4. True external (Mock), Deepening, Dependency categories, Seam discipline, Testing strategy: replace, don't layer (+13 more)

### Community 32 - "workflow-compiler.mjs"
Cohesion: 0.08
Nodes (41): predictedFixedWidthOverflow(), withDiagnosticRecordingSuppressed(), NODE_CARD_ATTR, nodeCardStyle(), TONES, addVerifiedCrossingRepair(), addVerifiedPlacementRepair(), authoredNodeHeight() (+33 more)

### Community 33 - "ref_node_path"
Cohesion: 0.16
Nodes (14): childPath, normalize(), startDeliveryUpdateCheck(), unavailable(), failureDetails(), launchTarget(), launchTimeout(), openArtifact() (+6 more)

### Community 34 - "During the session"
Cohesion: 0.09
Nodes (19): ADR Format, Numbering, Optional sections, Template, What qualifies, When to offer an ADR, GLOSSARY.md Format, Rules (+11 more)

### Community 35 - "compileWorkflowInternal"
Cohesion: 0.12
Nodes (45): rectsOverlap(), segmentIntersectsRect(), segmentRectClearance(), measureLegend(), compileWorkflowInternal(), boundsOverlap(), candidateLabelRect(), classifyFailedAutomaticCandidatePins() (+37 more)

### Community 36 - "pathFor"
Cohesion: 0.11
Nodes (35): workflow(), finalizeReadableViewBox(), gapYBetween(), groupSpan(), isReadableControlledRoute(), labelRectFor(), measuredContentBounds(), measuredPlanFootprint() (+27 more)

### Community 37 - "cli.mjs"
Cohesion: 0.12
Nodes (27): defaultDeliveryPaths(), stagePreviewCommit(), __dirname, removeOwnedRegularFile(), applyLocaleTranslations(), isFilesystemError(), loadDiagram(), loadDiagramWithBrandMarks() (+19 more)

### Community 38 - "package.json"
Cohesion: 0.11
Nodes (17): bin, archify, description, devDependencies, ajv, simple-icons, engines, node (+9 more)

### Community 39 - "Delivery contract"
Cohesion: 0.12
Nodes (17): Architecture layout repair, Choose the repair scope, One coherent repair, A new candidate at an existing output path, Automated browser evidence, Delivery contract, Failed finalize and candidate repair, Handoff receipt (+9 more)

### Community 40 - "renderMembers"
Cohesion: 0.50
Nodes (5): memberColumns(), memberSpans(), punctuated(), renderMembers(), visibilityChip()

### Community 41 - "PipeCdp"
Cohesion: 0.27
Nodes (4): ChromeVisualBrowser, chromeVisualBrowserArgs(), evaluate(), PipeCdp

### Community 42 - "tasteskill: Anti-Slop Frontend Skill"
Cohesion: 0.13
Nodes (15): 0.A Read these signals first, 0.B Output a one-line "Design Read" before generating, 0. BRIEF INFERENCE (Read the Room Before Anything Else), 0.C If the brief is ambiguous, ask one question, do not guess, 0.D Anti-Default Discipline, 13. OUT OF SCOPE, 14. FINAL PRE-FLIGHT CHECK, 2.A When to reach for a real design system (use official packages) (+7 more)

### Community 43 - "Appendix B - Canonical Sources (read these before reinventing)"
Cohesion: 0.13
Nodes (15): Appendix B - Canonical Sources (read these before reinventing), Apple Liquid Glass (Apple platforms only), Atlassian, Bootstrap, Carbon, Fluent UI, GOV.UK, Material Web (+7 more)

### Community 44 - "Diagnosing Bugs"
Cohesion: 0.13
Nodes (14): Completion criterion: a tight loop that goes red, Diagnosing Bugs, Minimise, Non-deterministic bugs, Phase 1: Build a feedback loop, Phase 2: Reproduce + minimise, Phase 3: Hypothesise, Phase 4: Instrument (+6 more)

### Community 45 - "authoring-contract.md"
Cohesion: 0.22
Nodes (3): Bundled Viewer catalogs, Agent decision path, Brand marks

### Community 46 - "portable-path.mjs"
Cohesion: 0.29
Nodes (12): assertProfile(), classifySemanticCollision(), collisionError(), createSemanticIndex(), findSemanticCollision(), pathError(), PORTABLE_PATH_PROFILES, PortablePathError (+4 more)

### Community 47 - "parseAttrs"
Cohesion: 0.27
Nodes (14): collectArchitectureLeadingSpace(), collectLegendBoxes(), collectRelationshipLabelMasks(), collectSequenceColumnSpace(), collectSequenceNoteBorders(), collectUntransformedNodeRects(), legendTextWidth(), numberAttr() (+6 more)

### Community 48 - "scripts"
Cohesion: 0.12
Nodes (16): scripts, build:gallery, build:guide, build:readme-showcase, build:start, check:brand-marks, check:release-identity, check:validators (+8 more)

### Community 49 - "DevKernel Hub.md"
Cohesion: 0.32
Nodes (4): Context & Connections, One home per fact keeps routing and history separate, Context & Connections, Universal agent adapters decouple tools from repo core

### Community 50 - "scenarios.mjs"
Cohesion: 0.24
Nodes (10): detectGuideLanguage(), formatScenarioList(), listScenarioRecipes(), localized(), normalized(), publicGuideData(), RAW_RECIPES, recommendScenario() (+2 more)

### Community 51 - "Authoring contract"
Cohesion: 0.15
Nodes (13): Authoring contract, Composition repair, Engineering profile default, Hand-placed fallback, Label repair, Language consistency, Legend contract, Node icons (+5 more)

### Community 52 - "detail"
Cohesion: 0.15
Nodes (11): Waterfall, detail(), Axis, Cards, Event Timeline Renderer, Input, Tested size, Execution Waterfall Renderer (+3 more)

### Community 53 - "desktop-readability.mjs"
Cohesion: 0.13
Nodes (16): DECLARED_WIDE_READER_CONTRACT, DECLARED_WIDE_READER_MAX_WIDTH, DECLARED_WIDE_READER_RATIO, DECLARED_WIDE_REFERENCE_BODY_HORIZONTAL_PX, DECLARED_WIDE_REFERENCE_DIAGRAM_HORIZONTAL_PX, declaredWideReadabilityBudget(), describeFixedWidthOverflow(), DESKTOP_FIXED_VERTICAL_CHROME_PX (+8 more)

### Community 54 - "diagnostics.mjs"
Cohesion: 0.11
Nodes (22): Executable geometry rules, Explicit `via` coordinates, Repair evidence, Repair order, Spacing and labels, boundaryKey, fallbackDiagnostic(), formatDiagnostics() (+14 more)

### Community 55 - "validatePortablePath"
Cohesion: 0.38
Nodes (13): architecture(), classDiagram(), dataflow(), erd(), lifecycle(), sequence(), timeline(), tree() (+5 more)

### Community 56 - "Steps"
Cohesion: 0.15
Nodes (12): 1. Detect package manager, 2. Install dependencies, 3. Initialize Husky, 4. Create `.husky/pre-commit`, 5. Create `.lintstagedrc`, 6. Create `.prettierrc` (if missing), 7. Verify, 8. Commit (+4 more)

### Community 57 - "Test-Driven Development"
Cohesion: 0.15
Nodes (10): Designing for Mockability, When to Mock, Anti-patterns, Rules of the loop, Seams: where tests go, Test-Driven Development, What a good test is, Bad Tests (+2 more)

### Community 58 - "Process"
Cohesion: 0.15
Nodes (12): 1. Gather context, 2. Explore the codebase (optional), 3. Draft vertical slices, 4. Quiz the user, 5. Publish the tickets to the configured tracker, Acceptance criteria, Blocked by, <NN>: <Ticket title> (+4 more)

### Community 59 - "generate-brand-marks.mjs"
Cohesion: 0.18
Nodes (13): catalog, catalogPath, domains, fail(), generated, here, ids, lookupForms() (+5 more)

### Community 60 - "memberRows"
Cohesion: 0.18
Nodes (13): attributeText(), compartments(), fillLines(), headerHeight(), headerWidth(), measuredTypes, memberRows(), methodText() (+5 more)

### Community 61 - "4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)"
Cohesion: 0.17
Nodes (12): 4.10 Quotes & Testimonials, 4.11 Page Theme Lock (Light / Dark Mode Consistency), 4.1 Typography, 4.2 Color Calibration, 4.3 Layout Diversification, 4.4 Materiality, Shadows, Cards, 4.5 Interactive UI States, 4.6 Data & Form Patterns (+4 more)

### Community 62 - "Mode placement"
Cohesion: 0.18
Nodes (11): Architecture, Class, Dataflow, ERD, Lifecycle, Mode placement, Sequence, Timeline (+3 more)

### Community 63 - "generate-validators.mjs"
Cohesion: 0.18
Nodes (10): ajv, diagramTypes, __dirname, output, portableOutputWrappers, RESERVED_TYPE_NAMES, root, schemaIds (+2 more)

### Community 64 - "legend.mjs"
Cohesion: 0.26
Nodes (10): ensureAutoLegendFits(), renderLegend(), renderStage(), renderSvg(), legendFootprint(), measuredEntryWidth(), renderedLegendFontSize(), renderLegend() (+2 more)

### Community 65 - "pathFor"
Cohesion: 0.24
Nodes (11): buildLayoutReport(), defaultRelationshipLabelPoint(), legendSwatch(), markerAttrs(), pathFor(), relationshipClass(), relationshipLabelBox(), relationshipLabelPoint() (+3 more)

### Community 66 - "collectArrows"
Cohesion: 0.22
Nodes (11): attrEntries(), collectArrows(), collectCompositionFrames(), collectNonFiniteAttrs(), continuousRoutePoints(), decodeNumericReferences(), inspectedPath(), isNumericAttr() (+3 more)

### Community 67 - "10. REFERENCE VOCABULARY (Pattern Names the Agent Should Know)"
Cohesion: 0.20
Nodes (10): 10. REFERENCE VOCABULARY (Pattern Names the Agent Should Know), Animation Library Choice, Cards & Containers, Galleries & Media, Hero Paradigms, Layout & Grids, Micro-Interactions & Effects, Navigation & Menus (+2 more)

### Community 68 - "Viewer Runtime reference"
Cohesion: 0.22
Nodes (8): Canonical exports, Embedded reading addresses, Exploration, Motion and presentation, Reach Share Card, Route Share Card, Truth boundary, Viewer Runtime reference

### Community 69 - "Workflow Renderer"
Cohesion: 0.22
Nodes (9): Design Rules, Fixed v1, Input, Layout contracts, Legend, Migration and layout receipt, Optional semantic checks, Readable v2 (+1 more)

### Community 70 - "Phase 2: Release, `production` Branch Sync, Tagging & Major-Only GitHub Release (`patch` | `minor` | `major`)"
Cohesion: 0.22
Nodes (8): Core Invariants, Phase 1: Unreleased Commit Workflow (Always Runs When Working Tree Is Dirty), Phase 2: Release, `production` Branch Sync, Tagging & Major-Only GitHub Release (`patch` | `minor` | `major`), Step 1: Promote `## [Unreleased]` & Bump Version Manifests, Step 2: Create Annotated Git Tag Linked to Latest `CHANGELOG.md` Section, Step 3: Ensure & Update `production` Branch from `main`, Step 4: GitHub Release — Trigger ONLY on `major` Updates, The /git-commit Skill (Unreleased + Production Release Pipeline)

### Community 71 - "Architectural Rules & Invariants"
Cohesion: 0.22
Nodes (8): 1. Unidirectional Dependency Rule, 2. Package Exports & Internal Linking, 3. Turborepo Task Pipeline (`turbo.json`), 4. Shared Formatting Utilities, 5. Fixed Port Allocation & Anti-Collision Standards, Architectural Rules & Invariants, Monorepo Topography, The /monorepo-architect Skill

### Community 72 - "to-spec/SKILL.md"
Cohesion: 0.22
Nodes (8): Further Notes, Implementation Decisions, Out of Scope, Problem Statement, Process, Solution, Testing Decisions, User Stories

### Community 73 - "Entity-Relationship Renderer"
Cohesion: 0.25
Nodes (7): Cardinality ink, Domain bands, Entity-Relationship Renderer, Input, Reading a schema, The legend band, Typography

### Community 74 - "Archify JSON IR Schemas"
Cohesion: 0.25
Nodes (8): Archify JSON IR Schemas, Error format, Files, Legend presentation contract, Runtime validation, schema_version policy, Shared definitions (common.schema.json), Visual quality and engineering truth

### Community 75 - "Process"
Cohesion: 0.25
Nodes (7): 1. Pin the fixed point, 2. Identify the spec source, 3. Identify the standards sources, 4. Spawn both sub-agents in parallel, 5. Aggregate, Process, Why two axes

### Community 76 - "9. AI TELLS (Forbidden Patterns)"
Cohesion: 0.25
Nodes (8): 9.A Visual & CSS, 9. AI TELLS (Forbidden Patterns), 9.B Typography, 9.C Layout & Spacing, 9.D Content & Data ("Jane Doe" Effect), 9.E External Resources & Components, 9.F Production-Test Tells (banned outright), 9.G EM-DASH BAN (the single most-violated Tell)

### Community 77 - "Repository-backed authoring"
Cohesion: 0.29
Nodes (7): Repository evidence, Author from evidence, Choose an example by structure, Evidence by diagram type, Explore on demand, Repository-backed authoring, line()

### Community 78 - "Class and Interface Renderer"
Cohesion: 0.29
Nodes (6): Class and Interface Renderer, Input, Layout, Reader and export, Relationships, Tested size

### Community 79 - "Sequence Renderer"
Cohesion: 0.29
Nodes (6): Column fit, Design Rules, Input, Layout budget, Legend, Sequence Renderer

### Community 80 - "Hierarchy and Tree Renderer"
Cohesion: 0.29
Nodes (6): Expand and collapse, Hierarchy and Tree Renderer, Input, Layout, Structure checks, Tested size

### Community 81 - "Archify"
Cohesion: 0.29
Nodes (7): Archify, Delivery, Existing candidate handoff, Optional viewer capabilities, Output, Setup and fallback, Update awareness

### Community 82 - "APPENDICES - Real Source-Backed Reference Material"
Cohesion: 0.29
Nodes (6): APPENDICES - Real Source-Backed Reference Material, Appendix A - Install Commands per Design System, Appendix C - Apple Liquid Glass: Honest Web Approximation, Safer web approximation skeleton, What is NOT official, What is official

### Community 83 - "11. REDESIGN PROTOCOL"
Cohesion: 0.29
Nodes (7): 11.A Detect the Mode (first action), 11.B Audit Before Touching, 11.C Preservation Rules, 11.D Modernisation Levers (priority order), 11.E Decision Tree: Targeted Evolution vs Full Redesign, 11.F What Never Changes Silently, 11. REDESIGN PROTOCOL

### Community 84 - "3. DEFAULT ARCHITECTURE & CONVENTIONS"
Cohesion: 0.29
Nodes (7): 3.A Stack, 3.B State, 3.C Icons, 3.D Emoji Policy, 3. DEFAULT ARCHITECTURE & CONVENTIONS, 3.E Responsiveness & Layout Mechanics, 3.F Dependency Verification (mandatory)

### Community 85 - "6. PERFORMANCE & ACCESSIBILITY GUARDRAILS"
Cohesion: 0.29
Nodes (7): 6.A Hardware Acceleration, 6.B Reduced Motion (mandatory), 6.C Dark Mode (mandatory for any consumer-facing page), 6.D Core Web Vitals Targets, 6.E DOM Cost, 6.F Z-Index Restraint, 6. PERFORMANCE & ACCESSIBILITY GUARDRAILS

### Community 86 - "automatic-labels.mjs"
Cohesion: 0.67
Nodes (3): placeAutomaticLabels(), reservedLabelRect(), createSpatialGrid()

### Community 87 - "Data Flow Renderer"
Cohesion: 0.33
Nodes (5): Data Flow Renderer, Design Rules, Input, Layout budget, Legend

### Community 88 - "Lifecycle Renderer"
Cohesion: 0.33
Nodes (6): Design rules, Input, Layout, Legend and state marks, Lifecycle Renderer, Validation

### Community 89 - "analyzeSvgPath"
Cohesion: 0.53
Nodes (4): analyzeSvgPath(), ARITY, failure(), tokenize()

### Community 90 - "Third-party notices"
Cohesion: 0.33
Nodes (5): JetBrains Mono, No additional rights granted, OpenAI mark, Simple Icons, Third-party notices

### Community 91 - "CQRS Pattern segregates command writes from read query pipelines"
Cohesion: 0.33
Nodes (5): Anti-Pattern Warning & Restriction, Applied In, CQRS Pattern segregates command writes from read query pipelines, Problem Solved, Zentora Standard

### Community 92 - "Singleton Pattern controls expensive lifecycle resources"
Cohesion: 0.33
Nodes (5): Anti-Pattern Warning, Applied In, Problem Solved, Singleton Pattern controls expensive lifecycle resources, Zentora Standard

### Community 93 - "Authoring defaults"
Cohesion: 0.40
Nodes (5): Authoring defaults, Composition and meaning, Evidence and schema, Layout and routing, Presentation and modes

### Community 94 - "Starter-Project Hub.md"
Cohesion: 0.29
Nodes (4): Context & Connections, Graphify CLI, Context & Connections, Public settings synchronization on load must not overwrite authenticated secret configuration state on save

### Community 95 - "12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)"
Cohesion: 0.40
Nodes (5): 12.A File Location, 12.B Required Frontmatter, 12.C Required Body Sections, 12.D Block-Library Discipline, 12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)

### Community 96 - "Claude Code Guidelines — Zentora Dev (MyOS)"
Cohesion: 0.33
Nodes (5): Claude Code Guidelines — Zentora Dev (MyOS), Core Workflows, Master Routing & Invariants, Windows PowerShell 5.1 Terminal Execution, Zero-Token Context Recall

### Community 97 - "8. DARK MODE PROTOCOL"
Cohesion: 0.40
Nodes (5): 8.A Token Strategy (pick one, stick to it), 8.B Do Not Prescribe Specific Colors Here, 8.C Default Mode, 8.D Test in Both Modes Before Finishing, 8. DARK MODE PROTOCOL

### Community 98 - "The /selfhost-devops Skill"
Cohesion: 0.40
Nodes (4): Automated Backup Strategy, Multi-Container Architecture, Security Invariants, The /selfhost-devops Skill

### Community 100 - "DevKernel Hub"
Cohesion: 0.40
Nodes (5): Architecture & Key Decisions, Architecture Patterns, DevKernel Hub, Overview, Session History

### Community 101 - "Starter-Project Hub"
Cohesion: 0.40
Nodes (5): Architecture & Key Decisions, Architecture Patterns, Overview, Session History, Starter-Project Hub

### Community 102 - "Adapter Pattern insulates domain models from external schemas"
Cohesion: 0.40
Nodes (4): Adapter Pattern insulates domain models from external schemas, Applied In, Problem Solved, Zentora Standard

### Community 103 - "Builder Pattern simplifies complex multi-field object construction"
Cohesion: 0.40
Nodes (4): Applied In, Builder Pattern simplifies complex multi-field object construction, Problem Solved, Zentora Standard

### Community 104 - "Circuit Breaker Pattern prevents cascading failure across external services"
Cohesion: 0.40
Nodes (4): Applied In, Circuit Breaker Pattern prevents cascading failure across external services, Problem Solved, Zentora Standard

### Community 105 - "Decorator Pattern attaches cross-cutting concerns transparently"
Cohesion: 0.40
Nodes (4): Applied In, Decorator Pattern attaches cross-cutting concerns transparently, Problem Solved, Zentora Standard

### Community 106 - "Observer Pattern decouples secondary side effects from core operations"
Cohesion: 0.40
Nodes (4): Applied In, Observer Pattern decouples secondary side effects from core operations, Problem Solved, Zentora Standard

### Community 107 - "Strategy Pattern isolates interchangeable calculation algorithms"
Cohesion: 0.40
Nodes (4): Applied In, Problem Solved, Strategy Pattern isolates interchangeable calculation algorithms, Zentora Standard

### Community 108 - "DevKernel Manager Skill"
Cohesion: 0.40
Nodes (4): Core Workflows, DevKernel Manager Skill, Exact Graphify CLI Syntax (NEVER use `--update`), Portability (no hardcoded drive letters)

### Community 109 - "hitl-loop.template.sh"
Cohesion: 0.83
Nodes (3): capture(), hitl-loop.template.sh script, step()

### Community 110 - "Factory Pattern encapsulates multi-provider object creation"
Cohesion: 0.40
Nodes (4): Applied In, Factory Pattern encapsulates multi-provider object creation, Problem Solved, Zentora Standard

### Community 112 - "normalizeRoutePoints"
Cohesion: 0.27
Nodes (17): routeMeetsCompositionFloors(), crossingCount(), distance(), masks(), pinned(), related(), repairLabelRoutes(), segments() (+9 more)

### Community 113 - "Setup Agent Skill"
Cohesion: 0.40
Nodes (4): Command Execution, Setup Agent Skill, Slash Command Usage, Supported Agents

### Community 123 - "[DEV] 2026-10-27 - Multi-Agent Architecture and Knowledge Codification"
Cohesion: 0.40
Nodes (5): Decisions, [DEV] 2026-10-27 - Multi-Agent Architecture and Knowledge Codification, Focus, What was built, Wins

### Community 124 - "routeBudgetMetrics"
Cohesion: 0.29
Nodes (7): routeBudgetMetrics(), segmentPosition(), routeParts(), subpathBudgetMetrics(), subpathCorridors(), subpathLabelClearance(), subpathRhythmIssues()

### Community 125 - "Repository Pattern decouples business logic from persistence"
Cohesion: 0.40
Nodes (4): Applied In, Problem Solved, Repository Pattern decouples business logic from persistence, Zentora Standard

### Community 126 - "ChatGPT CLI & OpenAI Codex Configuration — Zentora Dev"
Cohesion: 0.50
Nodes (3): ChatGPT CLI & OpenAI Codex Configuration — Zentora Dev, Recommended CLI Launch Flags, System Protocol Invariants

### Community 127 - "1. THE THREE DIALS (Core Configuration)"
Cohesion: 0.50
Nodes (4): 1.A Dial Inference (design read → dial values), 1.B Use-Case Presets, 1.C How the Dials Drive Output, 1. THE THREE DIALS (Core Configuration)

### Community 128 - "autoViewBox"
Cohesion: 1.00
Nodes (3): autoViewBox(), contentBounds(), legendLayout()

### Community 129 - "sideFor"
Cohesion: 0.67
Nodes (3): ordinaryRouter(), sideFor(), Layout and routing

## Knowledge Gaps
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `layout()` connect `render-lifecycle.mjs` to `asArray`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `compileWorkflowInternal()` (e.g. with `acceptsFix()` and `compareCost()`) actually correct?**
  _`compileWorkflowInternal()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `archify.mjs` be split into smaller, more focused modules?**
  _Cohesion score 0.05199350081239845 - nodes in this community are weakly interconnected._
- **Why does `5. CONTEXT-AWARE PROACTIVITY` connect `render-lifecycle.mjs` to `tasteskill: Anti-Slop Frontend Skill`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Should `check-update.mjs` be split into smaller, more focused modules?**
  _Cohesion score 0.05592203898050974 - nodes in this community are weakly interconnected._
- **Should `render-erd.mjs` be split into smaller, more focused modules?**
  _Cohesion score 0.04341164453524004 - nodes in this community are weakly interconnected._
- **Should `architecture-delta.mjs` be split into smaller, more focused modules?**
  _Cohesion score 0.057455540355677154 - nodes in this community are weakly interconnected._
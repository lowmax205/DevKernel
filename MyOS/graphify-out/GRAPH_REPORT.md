# Graph Report - MyOS  (2026-10-27)

## Corpus Check
- 184 files · ~1,343,746 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 2)

## Summary
- 2556 nodes · 7032 edges · 127 communities (117 shown, 10 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 164 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- archify.mjs
- check-update.mjs
- render-erd.mjs
- architecture-delta.mjs
- render-class.mjs
- workflow-v2.mjs
- zentora_sync.py
- geometry.mjs
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
- output-path.mjs
- check-render-output.mjs
- i18n.mjs
- route-quality.mjs
- preview.mjs
- workflow-compiler.mjs
- validateReadablePinnedGeometry
- anchor
- func3
- Codebase Design
- acceptsFix
- ref_node_path
- During the session
- compileWorkflowInternal
- laneTop
- cli.mjs
- generate-brand-marks.mjs
- Delivery contract
- escapeHtml
- PipeCdp
- tasteskill: Anti-Slop Frontend Skill
- Appendix B - Canonical Sources (read these before reinventing)
- Diagnosing Bugs
- authoring-contract.md
- portable-path.mjs
- parseAttrs
- planRoutes
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
- engineering-profiles.mjs
- utils.mjs
- 4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)
- Mode placement
- generate-validators.mjs
- readableAutomaticVia
- repository-evidence.mjs
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
- renderSvg
- 12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)
- 5. CONTEXT-AWARE PROACTIVITY
- 8. DARK MODE PROTOCOL
- The /selfhost-devops Skill
- Verification Before Completion (The Iron Law)
- DevKernel Hub
- Starter-Project Hub
- Adapter Pattern insulates domain models from external schemas
- Builder Pattern simplifies complex multi-field object construction
- Circuit Breaker Pattern prevents cascading failure across external services
- Decorator Pattern attaches cross-cutting concerns transparently
- Observer Pattern decouples secondary side effects from core operations
- Strategy Pattern isolates interchangeable calculation algorithms
- 7. DIAL DEFINITIONS (Technical Reference)
- hitl-loop.template.sh
- Factory Pattern encapsulates multi-provider object creation
- DevKernel Tracker
- joint-label-routing.mjs
- createReadableLayout
- DevKernel
- Starter-Project
- brand-marks/README.md
- manifest.json
- update-awareness.md
- renderRow
- routeBudgetMetrics
- Repository Pattern decouples business logic from persistence
- inferredSides

## God Nodes (most connected - your core abstractions)
1. `compileWorkflowInternal()` - 198 edges
2. `asArray()` - 100 edges
3. `textUnits()` - 72 edges
4. `compileDataflow()` - 71 edges
5. `escapeHtml()` - 69 edges
6. `createRouter()` - 63 edges
7. `build()` - 60 edges
8. `rectsOverlap()` - 54 edges
9. `commandDeliver()` - 44 edges
10. `normalizeRoutePoints()` - 40 edges

## Surprising Connections (you probably didn't know these)
- `1. The 5-Step Gate Function` --references--> `build()`  [INFERRED]
  _meta/global-skills/verification-before-completion/SKILL.md → _meta/global-skills/archify/renderers/dataflow/dataflow-compiler.mjs
- `3. Prohibited Rationalizations` --references--> `build()`  [INFERRED]
  _meta/global-skills/verification-before-completion/SKILL.md → _meta/global-skills/archify/renderers/dataflow/dataflow-compiler.mjs
- `5.D Forbidden Animation Patterns` --references--> `layout()`  [INFERRED]
  _meta/global-skills/design-taste-frontend/SKILL.md → _meta/global-skills/archify/renderers/lifecycle/render-lifecycle.mjs
- `Layout and routing` --references--> `sideFor()`  [INFERRED]
  _meta/global-skills/archify/renderers/erd/README.md → _meta/global-skills/archify/renderers/class/render-class.mjs
- `Waterfall` --references--> `detail()`  [INFERRED]
  _meta/global-skills/archify/references/authoring-contract.md → _meta/global-skills/archify/renderers/class/render-class.mjs

## Import Cycles
- None detected.

## Communities (127 total, 10 thin omitted)

### Community 0 - "archify.mjs"
Cohesion: 0.05
Nodes (123): acquireDeliveryLock(), artifactCheckMaxBuffer(), artifactIdentity(), assertDeliveryOwnership(), assertOwnedDeliveryLock(), beginDeliveryAttempt(), canonicalExistingDeliveryOutput(), captureDeliveryTargetState() (+115 more)

### Community 1 - "check-update.mjs"
Cohesion: 0.06
Nodes (110): acquireOperation(), assertBoundedRegularFile(), assertCacheTargetAbsent(), assertRenameableCacheEntry(), assertSafeCacheEntry(), assertSafeDirectory(), assertSafeRegularFile(), cacheMkdir() (+102 more)

### Community 2 - "render-erd.mjs"
Cohesion: 0.04
Nodes (84): renderLegend(), renderSvg(), bandedLayout(), DEFAULT_ER_GRID, entityHeight(), erGridLayout(), gridColumn(), resolvedEntityWidth() (+76 more)

### Community 3 - "architecture-delta.mjs"
Cohesion: 0.07
Nodes (66): addNodeMarker(), addState(), annotateArchitectureSideSvg(), architectureDeltaChangeRows(), ArchitectureDeltaError, BOUNDARY_FIELDS, boundaryChangeMap(), boundaryElements() (+58 more)

### Community 4 - "render-class.mjs"
Cohesion: 0.05
Nodes (62): attributeText(), autoViewBox(), bands, buildLayoutReport(), busGroups, busPaths, cliArgs, compartments() (+54 more)

### Community 5 - "workflow-v2.mjs"
Cohesion: 0.18
Nodes (23): clone(), diagnostic(), expandableViewBox(), legacyLayoutProbe(), legacyRequirementProbe(), migrateWorkflowDocument(), requiredViewBoxFrom(), result() (+15 more)

### Community 6 - "zentora_sync.py"
Cohesion: 0.06
Nodes (29): main(), scan(), tracked_files(), detect_project_context(), extract_keywords(), format_capsule(), load_graph(), main() (+21 more)

### Community 7 - "geometry.mjs"
Cohesion: 0.09
Nodes (74): boundaryRect(), validateArchitecture(), connectionEndpointSide(), validateClassDiagram(), validateDataflow(), validateEr(), spreadParticipantWidth(), validateSequence() (+66 more)

### Community 8 - "render-sequence.mjs"
Cohesion: 0.06
Nodes (60): ensureAutoLegendFits(), autoViewBox(), isFinal(), legendCatalog(), arrowClass, automaticHeight, compositionFrames, contentBottom (+52 more)

### Community 9 - "render-lifecycle.mjs"
Cohesion: 0.06
Nodes (54): assignArcLevels(), assignTracks(), bracketOf, brackets, bracketTargets, canvasWidth, countCrossings(), depth (+46 more)

### Community 10 - "atomic-output.mjs"
Cohesion: 0.13
Nodes (52): args, backupOwnedPublishedEntry(), cleanupStagedEvidence(), commitVisualEvidence(), identityMatches(), restoreOwnedBackup(), unlinkOwnedEntry(), backupPublicRegularFileBinding() (+44 more)

### Community 11 - "build"
Cohesion: 0.16
Nodes (31): build(), compactCorridors(), crossingFlows(), detourFor(), endpointStubs(), extraLabelLineMasksRoute(), flowSides(), flowStrokeWidth() (+23 more)

### Community 12 - "visual-check.mjs"
Cohesion: 0.08
Nodes (54): appendEvidenceCleanupWarning(), appendEvidencePublicationFailure(), baseReceipt(), beginVisualEvidenceWrite(), CAPTURE_VIEWPORTS, CHROME_NO_SANDBOX_ENV, CHROME_STARTUP_TIMEOUT_MS, contactSheetHtml() (+46 more)

### Community 13 - "generated-validators.mjs"
Cohesion: 0.04
Nodes (53): pattern10, pattern11, pattern12, pattern13, pattern133, pattern14, pattern15, pattern16 (+45 more)

### Community 14 - "render-architecture.mjs"
Cohesion: 0.05
Nodes (60): DEFAULT_GRID, gridLayout(), resolveComponentPos(), validateGridPlacement(), architectureLegendEntries, autoViewBoxFor(), boundaryLabelWidth(), buildLayoutReport() (+52 more)

### Community 15 - "render-waterfall.mjs"
Cohesion: 0.05
Nodes (39): byId, children, cliArgs, details, { diagram: wf, template, outPath, sourceEvidence }, __dirname, footprint, height (+31 more)

### Community 16 - "createRouter"
Cohesion: 0.17
Nodes (28): createRouter(), alignFacingPorts(), collinearBacktrack(), collinearOverlapLength(), fanOutSide(), gridComponentObstacles(), inferredSide(), orthogonalTouchOnResolvedInterior() (+20 more)

### Community 17 - "finalize.mjs"
Cohesion: 0.10
Nodes (45): allChecksPassed(), browserEvidence(), captureReceipt(), compactFinalizeReceipt(), consolidateDiagnostics(), defaultDeliveryPaths(), defaultFinalizeReceiptPath(), defaultFinalizeSummaryPath() (+37 more)

### Community 18 - "render-timeline.mjs"
Cohesion: 0.07
Nodes (29): breaks, buildLayoutReport(), cards, cliArgs, { diagram: tl, template, outPath, sourceEvidence }, __dirname, events, footprint (+21 more)

### Community 19 - "brand-marks.mjs"
Cohesion: 0.09
Nodes (36): asUrl(), BASIC_HTML_REFERENCES, beforeDeadline(), captureBrandReference(), captureRemoteBrand(), captureTimeoutMilliseconds(), checkedFetch(), COLLECTIONS (+28 more)

### Community 20 - "path-semantics.mjs"
Cohesion: 0.15
Nodes (39): visualEvidenceOwnershipMatches(), absolutePath(), compareFutureLocations(), compareKnownEntries(), compareUnmaterializedNames(), containedBy(), futureWindowsNameRisk(), hasStableIdentity() (+31 more)

### Community 21 - "render-tree.mjs"
Cohesion: 0.07
Nodes (29): all, ancestorsOf(), attachOf(), bandSize, bandStart, centerOf(), childrenOf, cliArgs (+21 more)

### Community 22 - "output-path.mjs"
Cohesion: 0.26
Nodes (17): authoredOutputDiagnostic(), nativeOutputDiagnostic(), OutputPathError, pathIsInside(), rejectWindowsIpcShare(), resolveNativeOutputDirectory(), throwNativeOutputDiagnostic(), validateAuthoredOutputPath() (+9 more)

### Community 23 - "check-render-output.mjs"
Cohesion: 0.08
Nodes (21): checks, collectLegendCollisions(), collectRelationshipCrossings(), composition, crossProduct(), ELEMENT_NUMERIC_ATTRS, HTML_VOID_ELEMENTS, htmlPath (+13 more)

### Community 24 - "i18n.mjs"
Cohesion: 0.12
Nodes (27): BUNDLED_CATALOGS, bundledCatalog(), bundledLocaleFor(), CANONICAL_KEYS, CANONICAL_PLACEHOLDERS, catalogFor(), classifyTranslations(), DEFAULT_LOCALE (+19 more)

### Community 25 - "route-quality.mjs"
Cohesion: 0.12
Nodes (28): endpointSideIssue(), normalizeRoutePoints(), boundsForPoints(), boundsForRects(), cleanRouteDetourProblems(), collinearOverlap(), DEFAULTS, emptyControlPointClearance() (+20 more)

### Community 26 - "preview.mjs"
Cohesion: 0.10
Nodes (40): failureDetails(), launchTarget(), launchTimeout(), openArtifact(), OPENERS, openLoopbackUrl(), atomicOutputError(), atomicOutputFailure() (+32 more)

### Community 27 - "workflow-compiler.mjs"
Cohesion: 0.09
Nodes (65): renderComponent(), compileDataflow(), attempt(), renderNode(), nodeTextFit, FLOW_LABEL_HEIGHT, flowLabelSize(), wrapBlockedFlowLabels() (+57 more)

### Community 28 - "validateReadablePinnedGeometry"
Cohesion: 0.19
Nodes (24): authoredPinEvidence(), authoredRouteAssertionFields(), combinations(), conflictPinsFromRemovalSets(), hasAuthoredRouteAssertions(), presentChannelPins(), throwExplicitPinConflict(), throwReadableLabelLabelPinConflict() (+16 more)

### Community 29 - "anchor"
Cohesion: 0.18
Nodes (32): anchor(), automaticPortSpread(), chosenSide(), defaultFromSide(), defaultToSide(), joinRoutePoints(), automaticEndpointRepairs(), automaticPortCandidates() (+24 more)

### Community 30 - "func3"
Cohesion: 0.13
Nodes (24): func3(), validate20(), validate22(), validate24(), validate27(), validate28(), validate30(), validate31() (+16 more)

### Community 31 - "Codebase Design"
Cohesion: 0.09
Nodes (21): 1. In-process, 2. Local-substitutable, 3. Remote but owned (Ports & Adapters), 4. True external (Mock), Deepening, Dependency categories, Seam discipline, Testing strategy: replace, don't layer (+13 more)

### Community 32 - "acceptsFix"
Cohesion: 0.21
Nodes (12): withDiagnosticRecordingSuppressed(), workflow(), addVerifiedCrossingRepair(), addVerifiedPlacementRepair(), cloneWorkflow(), absoluteGeometrySizingDiagnostic(), acceptsFix(), finalizeReadableViewBox() (+4 more)

### Community 33 - "ref_node_path"
Cohesion: 0.19
Nodes (9): childPath, normalize(), startDeliveryUpdateCheck(), unavailable(), __dirname, __dirname, outputRoot, skillRoot (+1 more)

### Community 34 - "During the session"
Cohesion: 0.09
Nodes (19): ADR Format, Numbering, Optional sections, Template, What qualifies, When to offer an ADR, GLOSSARY.md Format, Rules (+11 more)

### Community 35 - "compileWorkflowInternal"
Cohesion: 0.09
Nodes (44): compileWorkflowInternal(), automaticForwardReversePx(), boundsOverlap(), compositionFrames(), corridorTopologyMatches(), endpointSideIsHonored(), firstRouteNodeCollision(), isReadableAutomaticRoute() (+36 more)

### Community 36 - "laneTop"
Cohesion: 0.23
Nodes (16): variantAccent(), groupSpan(), measuredContentBounds(), phaseSpan(), renderGroup(), renderLane(), renderPhase(), renderSvg() (+8 more)

### Community 37 - "cli.mjs"
Cohesion: 0.16
Nodes (24): applyLocaleTranslations(), isFilesystemError(), loadDiagram(), loadDiagramWithBrandMarks(), outputPathGuards, RELATIONSHIP_COLLECTIONS, SEMANTIC_COLLECTIONS, stageRenderedHtml() (+16 more)

### Community 38 - "generate-brand-marks.mjs"
Cohesion: 0.04
Nodes (46): bin, archify, description, devDependencies, ajv, simple-icons, engines, node (+38 more)

### Community 39 - "Delivery contract"
Cohesion: 0.12
Nodes (17): Architecture layout repair, Choose the repair scope, One coherent repair, A new candidate at an existing output path, Automated browser evidence, Delivery contract, Failed finalize and candidate repair, Handoff receipt (+9 more)

### Community 40 - "escapeHtml"
Cohesion: 0.18
Nodes (23): componentContext(), headerHeight(), memberColumns(), memberSpans(), punctuated(), renderMembers(), renderType(), visibilityChip() (+15 more)

### Community 41 - "PipeCdp"
Cohesion: 0.27
Nodes (4): ChromeVisualBrowser, chromeVisualBrowserArgs(), evaluate(), PipeCdp

### Community 42 - "tasteskill: Anti-Slop Frontend Skill"
Cohesion: 0.13
Nodes (15): 0.A Read these signals first, 0.B Output a one-line "Design Read" before generating, 0. BRIEF INFERENCE (Read the Room Before Anything Else), 0.C If the brief is ambiguous, ask one question, do not guess, 0.D Anti-Default Discipline, 13. OUT OF SCOPE, 14. FINAL PRE-FLIGHT CHECK, 1.A Dial Inference (design read → dial values) (+7 more)

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

### Community 48 - "planRoutes"
Cohesion: 0.30
Nodes (19): automaticEndpoint(), cachePath(), candidateSidePairs(), computePath(), connectionGeometry(), connectionSides(), crossingCount(), hasAuthoredLabelPlacement() (+11 more)

### Community 49 - "DevKernel Hub.md"
Cohesion: 0.29
Nodes (4): Context & Connections, Graphify CLI, Context & Connections, One home per fact keeps routing and history separate

### Community 50 - "scenarios.mjs"
Cohesion: 0.24
Nodes (10): detectGuideLanguage(), formatScenarioList(), listScenarioRecipes(), localized(), normalized(), publicGuideData(), RAW_RECIPES, recommendScenario() (+2 more)

### Community 51 - "Authoring contract"
Cohesion: 0.11
Nodes (18): Authoring contract, Composition repair, Engineering profile default, Executable geometry rules, Explicit `via` coordinates, Hand-placed fallback, Label repair, Language consistency (+10 more)

### Community 52 - "detail"
Cohesion: 0.15
Nodes (11): Waterfall, detail(), Axis, Cards, Event Timeline Renderer, Input, Tested size, Execution Waterfall Renderer (+3 more)

### Community 53 - "desktop-readability.mjs"
Cohesion: 0.13
Nodes (16): DECLARED_WIDE_READER_CONTRACT, DECLARED_WIDE_READER_MAX_WIDTH, DECLARED_WIDE_READER_RATIO, DECLARED_WIDE_REFERENCE_BODY_HORIZONTAL_PX, DECLARED_WIDE_REFERENCE_DIAGRAM_HORIZONTAL_PX, declaredWideReadabilityBudget(), describeFixedWidthOverflow(), DESKTOP_FIXED_VERTICAL_CHROME_PX (+8 more)

### Community 54 - "diagnostics.mjs"
Cohesion: 0.24
Nodes (12): boundaryKey, fallbackDiagnostic(), formatDiagnostics(), installRendererDiagnosticBoundary(), normalizedDiagnostic(), plainObject(), readerSignal, recorded (+4 more)

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

### Community 59 - "engineering-profiles.mjs"
Cohesion: 0.43
Nodes (6): DEPLOYMENT_BOUNDARY_KINDS, deploymentOwnershipDiagnostics(), membership(), PRIVATE_STATE_TYPES, subject(), validateEngineeringProfile()

### Community 60 - "utils.mjs"
Cohesion: 0.21
Nodes (12): localizeTemplate(), nodeTextFit, applyTemplate(), SEMANTIC_SIGIL_FOOTPRINT, SEMANTIC_SIGIL_INSET, SEMANTIC_SIGIL_SIZE, serializeScriptJson(), SIGIL_SHAPE (+4 more)

### Community 61 - "4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)"
Cohesion: 0.17
Nodes (12): 4.10 Quotes & Testimonials, 4.11 Page Theme Lock (Light / Dark Mode Consistency), 4.1 Typography, 4.2 Color Calibration, 4.3 Layout Diversification, 4.4 Materiality, Shadows, Cards, 4.5 Interactive UI States, 4.6 Data & Form Patterns (+4 more)

### Community 62 - "Mode placement"
Cohesion: 0.18
Nodes (11): Architecture, Class, Dataflow, ERD, Lifecycle, Mode placement, Sequence, Timeline (+3 more)

### Community 63 - "generate-validators.mjs"
Cohesion: 0.17
Nodes (10): ajv, diagramTypes, __dirname, output, portableOutputWrappers, RESERVED_TYPE_NAMES, root, schemaIds (+2 more)

### Community 64 - "readableAutomaticVia"
Cohesion: 0.22
Nodes (14): candidateLabelRect(), classifyFailedAutomaticCandidatePins(), hasAbsoluteRoutePins(), isReadableControlledRoute(), labelRectFor(), measuredPlanReceipt(), pathFor(), renderEdgeLabel() (+6 more)

### Community 65 - "repository-evidence.mjs"
Cohesion: 0.25
Nodes (16): EVIDENCE_NODE_COLLECTIONS, evidenceFailure(), evidenceNodes(), gitValue(), hasRepositoryEvidence(), prefetchBlobs(), readBatchObjects(), runGit() (+8 more)

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

### Community 94 - "renderSvg"
Cohesion: 0.19
Nodes (15): clockLabel(), durationLabel(), kindOf(), legendLayout(), legendSwatch(), multiDay, offsetLabel(), renderAxis() (+7 more)

### Community 95 - "12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)"
Cohesion: 0.40
Nodes (5): 12.A File Location, 12.B Required Frontmatter, 12.C Required Body Sections, 12.D Block-Library Discipline, 12. THE BLOCK LIBRARY (Contract - Implementations Land Here Iteratively)

### Community 96 - "5. CONTEXT-AWARE PROACTIVITY"
Cohesion: 0.40
Nodes (5): 5.A Sticky-Stack - Canonical Skeleton, 5.B Horizontal-Pan - Canonical Skeleton, 5.C Scroll-Reveal Stagger - Canonical Skeleton (lighter alternative), 5. CONTEXT-AWARE PROACTIVITY, 5.D Forbidden Animation Patterns

### Community 97 - "8. DARK MODE PROTOCOL"
Cohesion: 0.40
Nodes (5): 8.A Token Strategy (pick one, stick to it), 8.B Do Not Prescribe Specific Colors Here, 8.C Default Mode, 8.D Test in Both Modes Before Finishing, 8. DARK MODE PROTOCOL

### Community 98 - "The /selfhost-devops Skill"
Cohesion: 0.40
Nodes (4): Automated Backup Strategy, Multi-Container Architecture, Security Invariants, The /selfhost-devops Skill

### Community 99 - "Verification Before Completion (The Iron Law)"
Cohesion: 0.40
Nodes (4): 1. The 5-Step Gate Function, 2. Standard Repository Quality Gates, 3. Prohibited Rationalizations, Verification Before Completion (The Iron Law)

### Community 100 - "DevKernel Hub"
Cohesion: 0.40
Nodes (5): Architecture & Key Decisions, Architecture Patterns, DevKernel Hub, Overview, Session History

### Community 101 - "Starter-Project Hub"
Cohesion: 0.22
Nodes (7): Architecture & Key Decisions, Architecture Patterns, Overview, Session History, Starter-Project Hub, Context & Connections, Public settings synchronization on load must not overwrite authenticated secret configuration state on save

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

### Community 108 - "7. DIAL DEFINITIONS (Technical Reference)"
Cohesion: 0.50
Nodes (4): 7. DIAL DEFINITIONS (Technical Reference), DESIGN_VARIANCE (Level 1-10), MOTION_INTENSITY (Level 1-10), VISUAL_DENSITY (Level 1-10)

### Community 109 - "hitl-loop.template.sh"
Cohesion: 0.83
Nodes (3): capture(), hitl-loop.template.sh script, step()

### Community 110 - "Factory Pattern encapsulates multi-provider object creation"
Cohesion: 0.40
Nodes (4): Applied In, Factory Pattern encapsulates multi-provider object creation, Problem Solved, Zentora Standard

### Community 112 - "joint-label-routing.mjs"
Cohesion: 0.38
Nodes (11): busRouteConflict(), crossingCount(), distance(), length(), masks(), pinned(), related(), repairLabelRoutes() (+3 more)

### Community 113 - "createReadableLayout"
Cohesion: 0.29
Nodes (11): authoredNodeHeight(), authoredNodeWidth(), canonicalReadableWorkflow(), compareWorkflowEdges(), createReadableLayout(), nodeWidthContributor(), readableGroupBounds(), stableCompare() (+3 more)

### Community 123 - "renderRow"
Cohesion: 0.31
Nodes (10): dotX(), formatDuration(), legendSwatch(), number(), percent(), renderAxis(), renderGuides(), renderHeader() (+2 more)

### Community 124 - "routeBudgetMetrics"
Cohesion: 0.29
Nodes (7): routeBudgetMetrics(), segmentPosition(), routeParts(), subpathBudgetMetrics(), subpathCorridors(), subpathLabelClearance(), subpathRhythmIssues()

### Community 125 - "Repository Pattern decouples business logic from persistence"
Cohesion: 0.40
Nodes (4): Applied In, Problem Solved, Repository Pattern decouples business logic from persistence, Zentora Standard

### Community 126 - "inferredSides"
Cohesion: 0.67
Nodes (3): inferredSides(), bandKey(), corridorKey()

## Knowledge Gaps
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `layout()` connect `render-lifecycle.mjs` to `5. CONTEXT-AWARE PROACTIVITY`, `geometry.mjs`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `compileWorkflowInternal()` (e.g. with `acceptsFix()` and `compareCost()`) actually correct?**
  _`compileWorkflowInternal()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `archify.mjs` be split into smaller, more focused modules?**
  _Cohesion score 0.05199350081239845 - nodes in this community are weakly interconnected._
- **Why does `5.D Forbidden Animation Patterns` connect `5. CONTEXT-AWARE PROACTIVITY` to `render-lifecycle.mjs`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Should `check-update.mjs` be split into smaller, more focused modules?**
  _Cohesion score 0.05592203898050974 - nodes in this community are weakly interconnected._
- **Why does `5. CONTEXT-AWARE PROACTIVITY` connect `5. CONTEXT-AWARE PROACTIVITY` to `tasteskill: Anti-Slop Frontend Skill`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Should `render-erd.mjs` be split into smaller, more focused modules?**
  _Cohesion score 0.04231974921630094 - nodes in this community are weakly interconnected._

# Implementation Plan: Rialo Bird Browser Game

**Branch**: `001-title-rialo-bird` | **Date**: 2025-01-27 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-title-rialo-bird/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, or `GEMINI.md` for Gemini CLI).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary
A browser-based 2D game inspired by Flappy Bird, fully rebranded with company identity. Players control a logo-bird character through vertical obstacle pipes to achieve high scores. Core technical approach: Python Arcade for game logic, pygbag for WebAssembly browser deployment, Supabase for online leaderboard, with constitutional enforcement of simplicity and test-first development.

## Technical Context
**Language/Version**: Python 3.11+  
**Primary Dependencies**: Python Arcade (game engine), pygbag (WebAssembly build), Supabase (PostgREST API)  
**Storage**: Local JSON (IndexedDB via pygbag FS), Remote Supabase PostgreSQL  
**Testing**: pytest (unit/integration), Playwright (E2E web), cURL (contract tests)  
**Target Platform**: Web browsers (WASM), Desktop dev (local Python)  
**Project Type**: web (game + API integration)  
**Performance Goals**: 60 FPS gameplay, <3s initial load, <2MB total assets  
**Constraints**: Cross-browser compatibility, mobile responsive, offline-capable leaderboard  
**Scale/Scope**: Anonymous leaderboard, <1MB WASM payload, 6 development milestones

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Simplicity Gate (Article VII) ✅ PASS
- **≤ 3 projects/packages**: game-core (Python Arcade), web-build (pygbag), supabase-integration (PostgREST)
- **No premature microservices**: Single game application with external API integration
- **No over-abstracted wrappers**: Direct use of Arcade and pygbag without custom abstractions

### Anti-Abstraction Gate (Article VIII) ✅ PASS  
- **Use Arcade directly**: Game loop, sprites, UI handled by Arcade framework
- **Use pygbag directly**: Web build via pygbag without custom wrappers
- **Avoid custom wrappers**: No repository patterns or service layers for simple game logic

### Integration-First Gate (Article IX) ✅ PASS
- **Define leaderboard contract first**: Supabase PostgREST API contract defined before implementation
- **Prefer real Supabase table**: Use staging Supabase project for integration tests
- **Contract-driven development**: API contracts generated before implementation

### Test-First Imperative (Article III) ✅ PASS
- **Generate tests before implementation**: Contract tests, integration tests, E2E tests defined first
- **TDD cycle**: Tests written → User approved → Tests fail → Then implement
- **Red-Green-Refactor**: Strictly enforced for all game features

## Project Structure

### Documentation (this feature)
```
specs/[###-feature]/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
# Web application structure (game + API integration)
game/
├── src/
│   ├── game/
│   │   ├── entities/          # Bird, Pipe, Background classes
│   │   ├── states/           # Game states (Menu, Running, Paused, GameOver)
│   │   ├── systems/          # Physics, Collision, Scoring systems
│   │   └── ui/              # HUD, menus, buttons
│   ├── assets/              # Sprites, audio, fonts
│   └── main.py              # Arcade game entry point
├── tests/
│   ├── contract/            # Supabase API contract tests
│   ├── integration/         # Game loop integration tests
│   └── unit/               # Individual component tests
└── build/                   # pygbag WebAssembly output

supabase/
├── migrations/              # Database schema
├── policies/               # RLS policies
└── functions/              # Edge functions (if needed)
```

**Structure Decision**: Web application (Option 2) - game frontend with external Supabase backend

## Phase 0: Outline & Research
1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:
   ```
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Generate contract tests** from contracts:
   - One test file per endpoint
   - Assert request/response schemas
   - Tests must fail (no implementation yet)

4. **Extract test scenarios** from user stories:
   - Each story → integration test scenario
   - Quickstart test = story validation steps

5. **Update agent file incrementally** (O(1) operation):
   - Run `.specify/scripts/bash/update-agent-context.sh cursor` for your AI assistant
   - If exists: Add only NEW tech from current plan
   - Preserve manual additions between markers
   - Update recent changes (keep last 3)
   - Keep under 150 lines for token efficiency
   - Output to repository root

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `.specify/templates/tasks-template.md` as base
- Generate tasks from Phase 1 design docs (contracts, data model, quickstart)
- Each contract → contract test task [P]
- Each entity → model creation task [P] 
- Each user story → integration test task
- Implementation tasks to make tests pass

**Ordering Strategy**:
- TDD order: Tests before implementation 
- Dependency order: Models before services before UI
- Mark [P] for parallel execution (independent files)

**Estimated Output**: 25-30 numbered, ordered tasks in tasks.md

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

### Task Categories Expected:
1. **Contract Tests** [P]: Supabase API contract tests (already created)
2. **Data Models** [P]: Settings, SaveData, GameState, Bird, Pipe, Score entities
3. **Integration Tests**: Game loop, physics, collision, scoring systems
4. **Core Game Logic**: Bird physics, pipe generation, collision detection
5. **Game States**: Menu, Running, Paused, GameOver state management
6. **UI Components**: HUD, menus, buttons, score display
7. **Asset Management**: Sprite loading, audio playback, asset optimization
8. **Supabase Integration**: Leaderboard API client, error handling
9. **Web Build**: pygbag configuration, deployment setup
10. **E2E Tests**: Cross-browser testing, performance validation

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |


## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [x] Complexity deviations documented

---
*Based on Constitution v2.1.1 - See `/memory/constitution.md`*

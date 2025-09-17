# Tasks: Rialo Bird Browser Game

**Input**: Design documents from `/specs/001-title-rialo-bird/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Web application structure**: `game/src/`, `game/tests/` at repository root
- **Supabase integration**: External API with local client
- **Assets**: `game/assets/` for sprites, audio, fonts
- **Build output**: `game/build/web/` for pygbag WebAssembly

## Phase 3.1: Setup
- [ ] T001 Create game project structure per implementation plan
- [ ] T002 Initialize Python project with Arcade and pygbag dependencies
- [ ] T003 [P] Configure linting and formatting tools (black, flake8)
- [ ] T004 [P] Setup virtual environment and requirements.txt
- [ ] T005 [P] Configure pygbag build settings for WebAssembly

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T006 [P] Contract test GET /leaderboard in game/tests/contract/test_leaderboard_get.py
- [ ] T007 [P] Contract test POST /leaderboard in game/tests/contract/test_leaderboard_post.py
- [ ] T008 [P] Integration test game state transitions in game/tests/integration/test_game_states.py
- [ ] T009 [P] Integration test physics system in game/tests/integration/test_physics.py
- [ ] T010 [P] Integration test collision detection in game/tests/integration/test_collision.py
- [ ] T011 [P] Integration test scoring system in game/tests/integration/test_scoring.py
- [ ] T012 [P] Integration test Supabase leaderboard in game/tests/integration/test_leaderboard.py

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T013 [P] Settings entity model in game/src/models/settings.py
- [ ] T014 [P] SaveData entity model in game/src/models/save_data.py
- [ ] T015 [P] GameState enum in game/src/models/game_state.py
- [ ] T016 [P] Bird entity model in game/src/entities/bird.py
- [ ] T017 [P] Pipe entity model in game/src/entities/pipe.py
- [ ] T018 [P] Score entity model in game/src/entities/score.py
- [ ] T019 [P] Background entity model in game/src/entities/background.py
- [ ] T020 Physics system in game/src/systems/physics.py
- [ ] T021 Collision detection system in game/src/systems/collision.py
- [ ] T022 Scoring system in game/src/systems/scoring.py
- [ ] T023 Pipe generation system in game/src/systems/pipe_generator.py

## Phase 3.4: Game States & UI
- [ ] T024 [P] MainMenu state in game/src/states/main_menu.py
- [ ] T025 [P] RunningGame state in game/src/states/running_game.py
- [ ] T026 [P] PausedGame state in game/src/states/paused_game.py
- [ ] T027 [P] GameOver state in game/src/states/game_over.py
- [ ] T028 [P] LeaderboardView state in game/src/states/leaderboard_view.py
- [ ] T029 [P] Settings state in game/src/states/settings.py
- [ ] T030 Game state manager in game/src/states/game_state_manager.py
- [ ] T031 [P] HUD UI components in game/src/ui/hud.py
- [ ] T032 [P] Menu UI components in game/src/ui/menu.py
- [ ] T033 [P] Button UI components in game/src/ui/button.py

## Phase 3.5: Asset Management
- [ ] T034 [P] Sprite loader in game/src/assets/sprite_loader.py
- [ ] T035 [P] Audio manager in game/src/assets/audio_manager.py
- [ ] T036 [P] Asset optimization utilities in game/src/assets/optimizer.py
- [ ] T037 Create placeholder bird sprites (128x128px)
- [ ] T038 Create placeholder pipe sprites (200x1200px)
- [ ] T039 Create placeholder background layers
- [ ] T040 Create placeholder audio files (OGG format)

## Phase 3.6: Supabase Integration
- [ ] T041 [P] Supabase client wrapper in game/src/services/supabase_client.py
- [ ] T042 [P] Leaderboard service in game/src/services/leaderboard_service.py
- [ ] T043 [P] Local storage service in game/src/services/local_storage.py
- [ ] T044 Error handling and offline mode in game/src/services/error_handler.py
- [ ] T045 Data synchronization logic in game/src/services/sync_service.py

## Phase 3.7: Main Game Loop
- [ ] T046 Main game class in game/src/main.py
- [ ] T047 Game initialization and setup
- [ ] T048 Input handling (mouse, touch, keyboard)
- [ ] T049 Game loop with fixed timestep
- [ ] T050 Asset loading and management
- [ ] T051 State transitions and management

## Phase 3.8: Web Build & Deployment
- [ ] T052 [P] pygbag configuration in game/pygbag.toml
- [ ] T053 [P] Web build script in game/build.py
- [ ] T054 [P] Deployment configuration for GitHub Pages
- [ ] T055 [P] Deployment configuration for Netlify
- [ ] T056 Cross-browser compatibility testing

## Phase 3.9: E2E Testing
- [ ] T057 [P] Playwright E2E tests in game/tests/e2e/test_game_flow.py
- [ ] T058 [P] Performance tests in game/tests/e2e/test_performance.py
- [ ] T059 [P] Mobile responsiveness tests in game/tests/e2e/test_mobile.py
- [ ] T060 [P] Cross-browser tests in game/tests/e2e/test_browsers.py

## Phase 3.10: Polish & Optimization
- [ ] T061 [P] Unit tests for all entities in game/tests/unit/test_entities.py
- [ ] T062 [P] Unit tests for all systems in game/tests/unit/test_systems.py
- [ ] T063 [P] Unit tests for all states in game/tests/unit/test_states.py
- [ ] T064 Performance optimization (60 FPS target)
- [ ] T065 Asset size optimization (<2MB target)
- [ ] T066 Memory usage optimization
- [ ] T067 [P] Documentation update in README.md
- [ ] T068 [P] Quickstart validation script

## Dependencies
- Tests (T006-T012) before implementation (T013-T051)
- T013-T019 (models) before T020-T023 (systems)
- T020-T023 (systems) before T024-T033 (states/UI)
- T034-T040 (assets) before T046-T051 (main game)
- T041-T045 (Supabase) before T046-T051 (main game)
- T046-T051 (main game) before T052-T060 (build/testing)
- Implementation before polish (T061-T068)

## Parallel Execution Examples

### Phase 3.2: Contract & Integration Tests [P]
```
# Launch T006-T012 together (all independent test files):
Task: "Contract test GET /leaderboard in game/tests/contract/test_leaderboard_get.py"
Task: "Contract test POST /leaderboard in game/tests/contract/test_leaderboard_post.py"
Task: "Integration test game states in game/tests/integration/test_game_states.py"
Task: "Integration test physics in game/tests/integration/test_physics.py"
Task: "Integration test collision in game/tests/integration/test_collision.py"
Task: "Integration test scoring in game/tests/integration/test_scoring.py"
Task: "Integration test Supabase in game/tests/integration/test_leaderboard.py"
```

### Phase 3.3: Entity Models [P]
```
# Launch T013-T019 together (all independent model files):
Task: "Settings entity model in game/src/models/settings.py"
Task: "SaveData entity model in game/src/models/save_data.py"
Task: "GameState enum in game/src/models/game_state.py"
Task: "Bird entity model in game/src/entities/bird.py"
Task: "Pipe entity model in game/src/entities/pipe.py"
Task: "Score entity model in game/src/entities/score.py"
Task: "Background entity model in game/src/entities/background.py"
```

### Phase 3.4: Game States [P]
```
# Launch T024-T029 together (all independent state files):
Task: "MainMenu state in game/src/states/main_menu.py"
Task: "RunningGame state in game/src/states/running_game.py"
Task: "PausedGame state in game/src/states/paused_game.py"
Task: "GameOver state in game/src/states/game_over.py"
Task: "LeaderboardView state in game/src/states/leaderboard_view.py"
Task: "Settings state in game/src/states/settings.py"
```

## Task Generation Rules
*Applied during main() execution*

1. **From Contracts**:
   - supabase-api.md → T006, T007 (contract tests)
   - GET/POST /leaderboard → T041-T045 (Supabase integration)
   
2. **From Data Model**:
   - Settings, SaveData, GameState → T013-T015 (model tasks)
   - Bird, Pipe, Score, Background → T016-T019 (entity tasks)
   
3. **From User Stories**:
   - Game state transitions → T008 (integration test)
   - Physics system → T009 (integration test)
   - Collision detection → T010 (integration test)
   - Scoring system → T011 (integration test)
   
4. **From Research**:
   - Python Arcade → T002 (dependencies)
   - pygbag → T005, T052 (build configuration)
   - Supabase → T041-T045 (integration)
   - Asset optimization → T034-T040 (asset management)

## Validation Checklist
*GATE: Checked by main() before returning*

- [x] All contracts have corresponding tests (T006-T007)
- [x] All entities have model tasks (T013-T019)
- [x] All tests come before implementation (T006-T012 before T013+)
- [x] Parallel tasks truly independent (marked [P])
- [x] Each task specifies exact file path
- [x] No task modifies same file as another [P] task
- [x] Dependencies properly ordered (models → systems → states → main)
- [x] Complete coverage of all design documents
- [x] TDD approach enforced (tests first)
- [x] Constitutional compliance maintained

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Follow TDD cycle: Red → Green → Refactor
- Maintain 60 FPS performance target
- Keep assets under 2MB total
- Ensure cross-browser compatibility
- Test on mobile devices
- Validate Supabase integration
- Follow constitutional principles (simplicity, test-first, integration-first)

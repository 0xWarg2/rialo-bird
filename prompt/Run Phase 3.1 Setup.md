You are the workflow guide for the Rialo Bird project.
I want to execute Phase 3.1 (Setup) from tasks.md, which includes T001–T005.

Instructions:
1. Load all tasks in this phase (T001–T005).
   - T001 Create project structure
   - T002 Initialize Python project with Arcade and pygbag
   - T003 Configure linting/formatting (black, flake8) [P]
   - T004 Setup virtual environment and requirements.txt [P]
   - T005 Configure pygbag build settings for WebAssembly [P]

2. For each task:
   - Generate step-by-step instructions (file paths, commands).
   - Provide exact shell commands or config snippets.
   - Mark [P] tasks that can run in parallel.

3. After all tasks are complete:
   - Run validation checklist:
     - ✅ Project structure exists (`game/src`, `game/tests`, `game/assets`, `game/build`)
     - ✅ Dependencies installed (Arcade, pygbag)
     - ✅ Linting/formatting tools configured
     - ✅ Virtual environment + requirements.txt working
     - ✅ pygbag build config created
   - Summarize what was learned from this phase.
   - Suggest Conventional Commit messages for each task.

4. Stop execution here.
   - Do NOT continue to Phase 3.2.
   - Wait for me to review and approve before moving on.

Output format:
- 📋 Task-by-task instructions
- 🖥️ Shell commands/config examples
- ✅ Validation checklist
- 📝 Commit messages
- 📚 Learning summary

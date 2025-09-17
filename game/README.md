# Rialo Bird

A Flappy Bird clone built with Python Arcade and compiled to WebAssembly for web browsers.

## Features

- Classic Flappy Bird gameplay
- WebAssembly build for browser compatibility
- Supabase leaderboard integration
- Responsive design for mobile and desktop
- 60 FPS performance target

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the game locally:
   ```bash
   python -m arcade src/main.py
   ```

3. Build for web:
   ```bash
   python -m pygbag src/main.py
   ```

## Development

- **Linting**: `black . && flake8 .`
- **Testing**: `pytest tests/`
- **E2E Testing**: `playwright test`

## Project Structure

```
game/
├── src/                 # Source code
│   ├── models/         # Data models
│   ├── entities/       # Game entities
│   ├── systems/        # Game systems
│   ├── states/         # Game states
│   ├── ui/            # UI components
│   ├── assets/        # Asset management
│   └── services/      # External services
├── tests/              # Test suite
│   ├── contract/      # Contract tests
│   ├── integration/   # Integration tests
│   ├── unit/          # Unit tests
│   └── e2e/           # End-to-end tests
├── assets/             # Game assets
└── build/             # Build output
    └── web/           # WebAssembly build
```


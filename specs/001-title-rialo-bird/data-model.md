# Data Model: Rialo Bird Browser Game

**Feature**: 001-title-rialo-bird  
**Date**: 2025-01-27  
**Status**: Complete

## Local Data Models (JSON via IndexedDB)

### Settings Entity
**Purpose**: Store user preferences and game configuration

```json
{
  "music_volume": 0.8,     // Float 0.0-1.0
  "sfx_volume": 0.9,       // Float 0.0-1.0
  "graphics_quality": "high", // "low" | "high"
  "controls": "touch"      // "mouse" | "touch" | "keyboard"
}
```

**Validation Rules**:
- Volume values must be between 0.0 and 1.0
- Graphics quality must be "low" or "high"
- Controls must be one of the valid options

### Save Data Entity
**Purpose**: Store player progress and achievements

```json
{
  "high_score": 42,                    // Integer >= 0
  "unlocked_themes": ["default"],      // Array of theme names
  "achievements": [                    // Array of achievement objects
    {
      "id": "first_score",
      "unlocked_at": "2025-01-27T10:30:00Z",
      "score_threshold": 1
    }
  ],
  "total_games_played": 15,            // Integer >= 0
  "total_play_time": 1800              // Integer seconds >= 0
}
```

**Validation Rules**:
- High score must be non-negative integer
- Unlocked themes must be valid theme names
- Achievement IDs must be predefined
- Play time must be non-negative

## Remote Data Models (Supabase PostgreSQL)

### Leaderboard Entity
**Purpose**: Store anonymous high scores for competitive ranking

```sql
CREATE TABLE leaderboard (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL CHECK (length(name) <= 16),
  score INTEGER NOT NULL CHECK (score >= 0 AND score <= 1000000),
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

**Fields**:
- `id`: Unique identifier (auto-generated UUID)
- `name`: Player display name (max 16 characters)
- `score`: Game score (0 to 1,000,000 range)
- `created_at`: Timestamp of submission

**Validation Rules**:
- Name length: 1-16 characters
- Score range: 0-1,000,000
- Name sanitization: Remove special characters, trim whitespace

## Game State Models (Runtime)

### Game State Entity
**Purpose**: Track current game phase and transitions

```python
class GameState(Enum):
    MAIN_MENU = "main_menu"
    RUNNING = "running" 
    PAUSED = "paused"
    GAME_OVER = "game_over"
    LEADERBOARD_VIEW = "leaderboard_view"
    SETTINGS = "settings"
```

**State Transitions**:
- MAIN_MENU → RUNNING (Play button)
- RUNNING → PAUSED (ESC key)
- PAUSED → RUNNING (Resume)
- RUNNING → GAME_OVER (Collision)
- GAME_OVER → MAIN_MENU (Restart)
- MAIN_MENU → LEADERBOARD_VIEW (Leaderboard button)
- MAIN_MENU → SETTINGS (Settings button)

### Bird Entity
**Purpose**: Player-controlled character with physics

```python
class Bird:
    position: Vec2          # x, y coordinates
    velocity: Vec2          # dx, dy per frame
    rotation: float         # degrees
    animation_frame: int    # 0-2 for wing flapping
    is_alive: bool          # collision state
```

**Physics Rules**:
- Gravity: constant downward acceleration
- Flap impulse: upward velocity boost
- Terminal velocity: maximum downward speed
- Rotation: tilt based on velocity direction

### Pipe Entity
**Purpose**: Vertical obstacle with collision detection

```python
class Pipe:
    position: Vec2          # x, y coordinates
    gap_y: float           # center of gap
    gap_size: float        # height of gap
    width: float           # pipe width
    height: float          # pipe height
    speed: float           # horizontal movement speed
```

**Generation Rules**:
- Gap position: randomized within screen bounds
- Gap size: decreases with score progression
- Speed: increases with difficulty
- Spawn interval: based on screen width

### Score Entity
**Purpose**: Track game session scoring

```python
class Score:
    current_score: int      # Points this session
    high_score: int         # Best score ever
    pipes_passed: int       # Obstacles cleared
    multiplier: float       # Power-up multiplier
```

**Scoring Rules**:
- +1 point per pipe passed
- Power-ups can modify multiplier
- High score updates on game over
- Score resets on new game

## Data Flow Architecture

### Local Storage Flow
1. Game starts → Load settings.json and save.json from IndexedDB
2. Settings change → Update settings.json immediately
3. Game over → Update save.json with new high score/achievements
4. Game exit → Persist all changes to IndexedDB

### Remote Storage Flow
1. Game over → Validate score and player name
2. Submit to Supabase → POST /leaderboard
3. Success → Update local high score
4. Failure → Graceful degradation, store locally only

### State Synchronization
- Local data is source of truth for user preferences
- Remote data is source of truth for leaderboard rankings
- Conflict resolution: Local preferences override, remote scores are authoritative

## Data Validation Strategy

### Client-Side Validation
- Real-time validation of user inputs
- Range checking for numeric values
- Format validation for text inputs
- Immediate feedback for invalid data

### Server-Side Validation
- Supabase RLS policies enforce data integrity
- Rate limiting prevents abuse
- Input sanitization prevents injection
- Constraint checking ensures valid ranges

## Performance Considerations

### Local Storage Optimization
- JSON files are small (<1KB each)
- IndexedDB provides async access
- Caching prevents repeated reads
- Compression not needed for small files

### Remote Storage Optimization
- Supabase handles connection pooling
- Pagination for large leaderboard queries
- Caching of top scores locally
- Offline mode with sync on reconnect

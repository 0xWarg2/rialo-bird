# Quickstart Guide: Rialo Bird Browser Game

**Feature**: 001-title-rialo-bird  
**Date**: 2025-01-27  
**Status**: Complete

## Overview
This quickstart guide validates the complete Rialo Bird game experience from development setup to web deployment. Follow these steps to verify all features work correctly.

## Prerequisites
- Python 3.11+
- Node.js 18+ (for Playwright E2E tests)
- Supabase account (for leaderboard)
- Modern web browser (Chrome, Firefox, Safari)

## Development Setup

### 1. Install Dependencies
```bash
# Install Python dependencies
pip install arcade pygbag pytest httpx

# Install Node.js dependencies for E2E tests
npm install playwright
npx playwright install
```

### 2. Configure Supabase
```bash
# Set environment variables
export SUPABASE_URL="https://drsyehmbsoofjdhtivdf.supabase.co"
export SUPABASE_ANON_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRyc3llaG1ic29vZmpkaHRpdmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODA4NjEsImV4cCI6MjA3MzY1Njg2MX0.Z5R9KzkkUJL3bxjrFrse4lzziwJSbwG3SyI_caj9CCc"

# Create leaderboard table (run in Supabase SQL Editor)
# Go to: https://drsyehmbsoofjdhtivdf.supabase.co/project/default/sql
CREATE TABLE leaderboard (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL CHECK (length(name) <= 16),
  score INTEGER NOT NULL CHECK (score >= 0 AND score <= 1000000),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enable RLS
ALTER TABLE leaderboard ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY \"Allow anonymous read access\" ON leaderboard FOR SELECT USING (true);
CREATE POLICY \"Allow anonymous insert with constraints\" ON leaderboard FOR INSERT WITH CHECK (
  length(name) >= 1 AND length(name) <= 16 AND
  score >= 0 AND score <= 1000000
);
"
```

### 3. Run Contract Tests
```bash
# Test Supabase API contracts
pytest tests/contract/test_supabase_api.py -v

# Expected: All tests pass, confirming API works
```

## Game Development Testing

### 4. Desktop Development
```bash
# Run game in desktop mode
python game/src/main.py

# Expected behavior:
# - Game window opens
# - Main menu displays with Play, Leaderboard, Settings buttons
# - Click Play → Game starts with bird character
# - Spacebar/click → Bird flaps upward
# - Bird falls due to gravity
# - Pipes spawn and move left
# - Collision with pipe/ground → Game over screen
# - Score displays correctly
# - ESC key pauses game
```

### 5. Game States Validation
```bash
# Test each game state transition
python -m pytest tests/integration/test_game_states.py -v

# Expected: All state transitions work correctly
```

### 6. Physics Testing
```bash
# Test physics system
python -m pytest tests/integration/test_physics.py -v

# Expected:
# - Gravity pulls bird down consistently
# - Flap impulse provides upward velocity
# - Terminal velocity limits downward speed
# - Collision detection works accurately
```

## Web Deployment Testing

### 7. Build Web Version
```bash
# Build WebAssembly version
python -m pygbag --build game/

# Expected: Build completes successfully
# Output: game/build/web/ directory with WASM files
```

### 8. Local Web Testing
```bash
# Serve web version locally
cd game/build/web/
python -m http.server 8000

# Open browser: http://localhost:8000
# Expected:
# - Game loads in browser
# - All controls work (mouse, touch, keyboard)
# - Performance is smooth (60 FPS)
# - Assets load correctly
# - Audio plays (if enabled)
```

### 9. Cross-Browser Testing
```bash
# Run E2E tests across browsers
npx playwright test tests/e2e/ --headed

# Expected:
# - Game loads on Chrome, Firefox, Safari
# - Controls work on all browsers
# - Performance meets targets
# - No console errors
```

## Leaderboard Integration Testing

### 10. Test Score Submission
```bash
# Play game and achieve score
# On game over screen:
# - Enter player name
# - Click Submit Score
# - Verify success message

# Check leaderboard
# - Click Leaderboard button
# - Verify score appears in top 10
# - Verify correct ordering by score
```

### 11. Test Offline Mode
```bash
# Disconnect internet
# Play game and achieve score
# Submit score
# Expected: Graceful degradation, score stored locally
# Reconnect internet
# Expected: Score syncs when possible
```

## Performance Validation

### 12. Performance Testing
```bash
# Run performance tests
python -m pytest tests/performance/ -v

# Expected:
# - 60 FPS maintained during gameplay
# - Initial load < 3 seconds
# - Asset size < 2 MB total
# - Memory usage stable
```

### 13. Mobile Testing
```bash
# Test on mobile device or browser dev tools
# Open game on mobile browser
# Expected:
# - Touch controls work smoothly
# - Performance acceptable on mobile
# - UI scales correctly
# - No layout issues
```

## Asset Validation

### 14. Asset Testing
```bash
# Verify all assets load correctly
python -m pytest tests/integration/test_assets.py -v

# Expected:
# - All sprites load without errors
# - Transparent backgrounds work
# - Audio files play correctly
# - Asset sizes optimized
```

### 15. Branding Validation
```bash
# Verify company branding elements
python -m pytest tests/integration/test_branding.py -v

# Expected:
# - Company colors used correctly
# - Logo appears in appropriate places
# - Typography matches brand guidelines
# - Overall visual consistency
```

## End-to-End User Journey

### 16. Complete User Flow
```bash
# Follow complete user journey
# 1. Open game in browser
# 2. Click Play
# 3. Play game, achieve score
# 4. Game over, enter name, submit score
# 5. View leaderboard
# 6. Play again
# 7. Check settings, adjust volume
# 8. Play with different settings

# Expected: Smooth, intuitive experience throughout
```

## Deployment Validation

### 17. Production Deployment
```bash
# Deploy to hosting platform (GitHub Pages, Netlify, itch.io)
# Test deployed version
# Expected:
# - Game loads from production URL
# - All features work correctly
# - Performance maintained
# - HTTPS works properly
```

### 18. Monitoring Setup
```bash
# Set up basic monitoring
# - Track game loads
# - Monitor error rates
# - Check performance metrics
# Expected: Stable performance, low error rates
```

## Troubleshooting

### Common Issues
1. **Game won't load**: Check browser console for errors
2. **Poor performance**: Enable "Low-Graphics" mode
3. **Audio not playing**: Check browser autoplay policies
4. **Leaderboard not working**: Verify Supabase configuration
5. **Assets missing**: Check build process and file paths

### Debug Commands
```bash
# Check game state
python -c "from game.src.main import Game; print(Game().state)"

# Test Supabase connection
python -c "import httpx; print(httpx.get('$SUPABASE_URL/leaderboard').status_code)"

# Verify asset paths
find game/assets -name "*.png" -o -name "*.ogg"
```

## Success Criteria
- ✅ All contract tests pass
- ✅ Game runs smoothly at 60 FPS
- ✅ Cross-browser compatibility confirmed
- ✅ Leaderboard integration working
- ✅ Mobile responsiveness verified
- ✅ Asset optimization complete
- ✅ Performance targets met
- ✅ User experience is intuitive and engaging

## Next Steps
After completing this quickstart:
1. Run full test suite: `pytest tests/ -v`
2. Deploy to production environment
3. Monitor performance and user feedback
4. Plan next milestone features
5. Iterate based on user testing results

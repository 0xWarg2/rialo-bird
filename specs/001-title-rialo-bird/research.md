# Research: Rialo Bird Browser Game

**Feature**: 001-title-rialo-bird  
**Date**: 2025-01-27  
**Status**: Complete

## Research Tasks Executed

### 1. Python Arcade Game Engine Research
**Task**: Research Python Arcade for 2D game development with WebAssembly deployment

**Decision**: Use Python Arcade 2.6+ as primary game engine  
**Rationale**: 
- Mature 2D game framework with excellent sprite batching and camera support
- Built-in physics timing and collision detection
- Strong community and documentation
- Direct pygbag compatibility for WebAssembly builds
- Minimal learning curve for simple 2D games

**Alternatives considered**:
- Pygame: Older, less maintained, no direct WASM support
- Kivy: Overkill for simple 2D game, complex mobile focus
- Custom OpenGL: Too complex for project scope

### 2. WebAssembly Build Pipeline Research  
**Task**: Research pygbag for Python Arcade WebAssembly compilation

**Decision**: Use pygbag for WebAssembly builds  
**Rationale**:
- Official tool for Python Arcade WASM compilation
- Handles asset bundling and IndexedDB integration automatically
- Static hosting friendly (GitHub Pages, Netlify, itch.io)
- Minimal configuration required
- Active development and Arcade integration

**Alternatives considered**:
- Pyodide: More complex setup, larger runtime
- Custom Emscripten: Too complex for project needs
- Native WebGL: Would require complete rewrite

### 3. Supabase Integration Research
**Task**: Research Supabase for leaderboard API with RLS policies

**Decision**: Use Supabase PostgREST API for leaderboard  
**Rationale**:
- Managed PostgreSQL with automatic REST API generation
- Built-in Row Level Security (RLS) for anonymous access control
- Real-time subscriptions capability for future features
- Generous free tier for development and small-scale deployment
- Simple authentication flow when needed

**Alternatives considered**:
- Firebase: Google dependency, more complex pricing
- Custom API: Too much development overhead
- Local-only: Would miss competitive aspect

### 4. Asset Optimization Research
**Task**: Research asset optimization for web game delivery

**Decision**: Use PNG compression + OGG audio with power-of-two sprite sizes  
**Rationale**:
- PNG with zopfli compression reduces file sizes by 20-30%
- OGG format provides good compression for short audio loops
- Power-of-two textures optimize GPU memory usage
- Transparent PNGs maintain visual quality with small file sizes

**Alternatives considered**:
- WebP: Better compression but limited browser support
- MP3: Larger file sizes than OGG
- Sprite atlases: Premature optimization for initial version

### 5. Cross-Browser Compatibility Research
**Task**: Research WebAssembly browser support and performance considerations

**Decision**: Target modern browsers with WASM support (Chrome 57+, Firefox 52+, Safari 11+)  
**Rationale**:
- WebAssembly has 95%+ browser support in modern browsers
- pygbag handles browser compatibility automatically
- Performance is adequate for 2D games on desktop and mobile
- Fallback to desktop Python version for development

**Alternatives considered**:
- Canvas 2D: Would require complete rewrite
- WebGL: Overkill for simple 2D game
- Native mobile apps: Outside project scope

## Resolved Clarifications

### Brand Colors and Assets
**Clarification**: Exact company brand colors / hex codes for UI, pipes, and background  
**Resolution**: Use placeholder brand colors for initial development, define actual colors in M2 milestone

### Company Logos and Icons  
**Clarification**: Which company logos/icons should be used for pipes and background patterns?  
**Resolution**: Use generic placeholder assets for M1, implement branded assets in M2 milestone

### Audio Style Reference
**Clarification**: Preferred audio style reference (retro chiptune, lo-fi, or branded jingle)?  
**Resolution**: Use upbeat electronic/chiptune style as specified in constitution, create placeholder audio for M1

## Technology Stack Validation

### Performance Targets Achievable
- 60 FPS: Achievable with Arcade's optimized rendering
- <3s initial load: Achievable with compressed assets and WASM
- <2MB total assets: Achievable with PNG compression and short audio loops

### Development Workflow Validated
- Desktop development with Python Arcade
- Web deployment with pygbag
- Supabase integration for leaderboard
- Cross-browser testing with Playwright

## Risk Mitigation Strategies

### WebAssembly Performance on Low-End Devices
- Implement "Low-Graphics" toggle to disable effects
- Reduce parallax layers on mobile devices
- Optimize sprite sizes for mobile screens

### Audio Autoplay Policies
- Start music only on first user interaction
- Provide audio controls in settings menu
- Graceful degradation when audio is blocked

### Asset Size Management
- Use sprite atlases for future optimization
- Compress assets aggressively
- Monitor bundle size during development

## Next Steps
All research complete. Ready to proceed to Phase 1 design with:
- Python Arcade for game engine
- pygbag for WebAssembly builds  
- Supabase for leaderboard API
- PNG/OGG for optimized assets
- Modern browser targeting

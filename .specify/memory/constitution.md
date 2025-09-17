# Rialo Bird Constitution
<!-- 2D Browser-Playable Game Inspired by Flappy Bird -->

## Core Principles

### I. Game Identity
<!-- 🎯 Core Loop & Branding -->
Every design decision must reinforce the core identity: simple, addictive, skill-based gameplay with "easy to play, hard to master" philosophy. All assets (bird, pipes, background) must reflect company branding in a playful but professional style. Tone must be fun, modern, energetic, but never childish.

### II. Visual Design Standards
<!-- 🖼️ Asset Requirements -->
Assets must use clean 2D style with transparent backgrounds. Character (logo-bird): 128x128 base, scalable. Pipes: tall vertical format, modular, scalable (recommended design size 200x1200 → scaled down). Background: layered (sky gradient, skyline silhouettes, clouds/icons) for parallax effect. UI: minimalist, flat, aligned with company typography/colors.

### III. Audio & Feedback Consistency
<!-- 🔊 Sound Design -->
Background music: upbeat electronic/chiptune loop, non-distracting. SFX: consistent, playful, short (flap = "whoosh," score = "bling," hit = "thud"). Audio volume balanced — never overpower visuals. All audio must enhance gameplay without becoming repetitive or annoying.

### IV. Gameplay Mechanics (NON-NEGOTIABLE)
<!-- 🕹️ Core Loop First -->
Start simple: flap → avoid pipes → score points. Add depth gradually: moving pipes, rotating obstacles, power-ups (shield, slow motion, double score). Fair challenge curve: gap sizes and speeds scale with player progress. Achievements & skins tied to score milestones. Core loop must be perfected before adding complexity.

### V. Online Integration & Data
<!-- 🌍 Supabase Integration -->
Leaderboard powered by Supabase. Store: player name + score (anonymous by default). Safe RLS policies for inserts/selects. Future extension: optional Supabase Auth login. Data persistence: local JSON save (IndexedDB). All online features must be optional and gracefully degrade when offline.

## Technical Standards

### VI. Technology Stack
<!-- 🚀 Framework & Deployment -->
Framework: Python Arcade for game logic. Web build: pygbag → WebAssembly for browser play. Hosting: itch.io, GitHub Pages, or Netlify (static deploy). Optimize assets (power-of-two sizes, compressed PNG). All builds must be cross-browser compatible and performant on mobile devices.

### VII. Performance Requirements
<!-- ⚡ Optimization Standards -->
Game must run at 60 FPS on modern browsers. Asset loading must be optimized for web delivery. Audio files must be compressed without quality loss. All animations must be smooth and responsive. Mobile touch controls must be intuitive and responsive.

## Development Workflow

### VIII. Project Phases
<!-- 📅 Development Process -->
1. Prototype core loop with placeholder assets
2. Replace with branded assets (bird, pipes, background)
3. Add HUD, UI, menus
4. Integrate Supabase leaderboard
5. Polish with animations, effects, music, and SFX
6. Test cross-browser & deploy

### IX. Quality Gates
<!-- ✅ Testing Requirements -->
Core gameplay must be tested on multiple browsers before deployment. All assets must be optimized and compressed. Audio must be balanced and non-repetitive. Mobile responsiveness must be verified. Leaderboard functionality must be tested with real data.

## Creative Extensions

### X. Future Features
<!-- 💡 Expansion Ideas -->
Seasonal skins (holidays, events). Endless ticker with company news at screen bottom. Multiplayer (split-screen or score-race). Lucky pipes with bonus effects. All extensions must maintain core gameplay integrity and brand consistency.

## Governance

### XI. Constitution Authority
<!-- 📜 Rule Enforcement -->
This constitution supersedes all other practices and design decisions. Consistency > Complexity. Always prioritize smooth gameplay, strong branding, and accessible design before adding advanced features. All development decisions must align with these principles.

### XII. Amendment Process
<!-- 🔄 Change Management -->
Amendments require documentation, approval, and migration plan. All PRs/reviews must verify compliance with constitution principles. Complexity must be justified against core gameplay goals. Use this constitution for all runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2025-01-27 | **Last Amended**: 2025-01-27
<!-- Rialo Bird Game Constitution - Initial Version -->
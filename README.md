# Rialo Bird Game

A Flappy Bird clone game with Supabase backend for leaderboard functionality.

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Copy the environment template
cp supabase-config.env.template .env

# Edit .env with your Supabase credentials
nano .env
```

### 2. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Test Supabase Connection

```bash
# Verify Supabase setup
python verify_supabase.py

# Test Supabase operations
python test_supabase.py
```

## 📁 Project Structure

```
rialo_bird/
├── .env                          # Environment variables (gitignored)
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── supabase-config.env.template  # Environment template
├── test_supabase.py             # Supabase connection tests
├── verify_supabase.py           # Database setup verification
├── assests/                     # Game assets
└── specs/                       # Project specifications
```

## 🔧 Environment Variables

Required environment variables in `.env`:

```env
SUPABASE_URL=your_supabase_url_here
SUPABASE_ANON_KEY=your_supabase_anon_key_here
NODE_ENV=development
PYTHON_ENV=development
```

## 🛡️ Security

- All sensitive information is stored in `.env` file
- `.env` file is gitignored and will never be committed
- Use `supabase-config.env.template` as a reference for required variables

## 🎮 Game Development

This project is currently in the setup phase. The game assets and Supabase backend are ready for development.

## 📋 Next Steps

1. Set up game engine (Pygame, etc.)
2. Implement game mechanics
3. Connect game to Supabase leaderboard
4. Add sound effects and animations

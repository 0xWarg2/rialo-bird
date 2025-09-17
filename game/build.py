#!/usr/bin/env python3
"""
Build script for Rialo Bird game using pygbag.
This script handles building the game for web deployment.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def clean_build():
    """Clean previous build artifacts."""
    build_dir = Path("build/web")
    if build_dir.exists():
        print("🧹 Cleaning previous build...")
        shutil.rmtree(build_dir)
    build_dir.mkdir(parents=True, exist_ok=True)


def build_web():
    """Build the game for web using pygbag."""
    print("🔨 Building game for web...")
    
    try:
        # Run pygbag build
        cmd = [
            sys.executable, "-m", "pygbag",
            "--build",
            "--template", "default",
            "--title", "Rialo Bird",
            "--icon", "assets/icon.png" if Path("assets/icon.png").exists() else None,
            "src/main.py"
        ]
        
        # Remove None values
        cmd = [arg for arg in cmd if arg is not None]
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Build completed successfully!")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)


def optimize_assets():
    """Optimize assets for web deployment."""
    print("🎨 Optimizing assets...")
    
    assets_dir = Path("assets")
    build_assets_dir = Path("build/web/assets")
    
    if not assets_dir.exists():
        print("⚠️  No assets directory found, skipping optimization")
        return
    
    # Copy assets to build directory
    if build_assets_dir.exists():
        shutil.rmtree(build_assets_dir)
    shutil.copytree(assets_dir, build_assets_dir)
    
    print("✅ Assets copied to build directory")


def create_index_html():
    """Create a custom index.html for the game."""
    index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rialo Bird</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #87CEEB 0%, #98FB98 100%);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        #game-container {
            border: 2px solid #333;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        .loading {
            text-align: center;
            color: #333;
            font-size: 18px;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div id="game-container">
        <div class="loading">
            <h2>🦅 Rialo Bird</h2>
            <p>Loading game...</p>
        </div>
    </div>
    <script type="module" src="./main.py"></script>
</body>
</html>"""
    
    with open("build/web/index.html", "w") as f:
        f.write(index_content)
    
    print("✅ Custom index.html created")


def main():
    """Main build process."""
    print("🚀 Starting Rialo Bird build process...")
    
    # Change to game directory
    os.chdir(Path(__file__).parent)
    
    # Clean previous build
    clean_build()
    
    # Build for web
    build_web()
    
    # Optimize assets
    optimize_assets()
    
    # Create custom index.html
    create_index_html()
    
    print("🎉 Build process completed!")
    print("📁 Build output: build/web/")
    print("🌐 To test locally: cd build/web && python -m http.server 8000")


if __name__ == "__main__":
    main()


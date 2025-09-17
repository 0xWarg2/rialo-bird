#!/usr/bin/env python3
"""
Supabase Database Setup for Rialo Bird Game
Creates the leaderboard table and RLS policies
"""

import httpx
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Supabase Configuration from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

# Validate required environment variables
if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    print("❌ Error: Missing required environment variables!")
    print("   Please ensure SUPABASE_URL and SUPABASE_ANON_KEY are set in .env file")
    print("   You can copy supabase-config.env.template to .env and fill in your values")
    exit(1)

HEADERS = {
    "apikey": SUPABASE_ANON_KEY,
    "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    "Content-Type": "application/json"
}

async def check_table_exists():
    """Check if leaderboard table exists"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{SUPABASE_URL}/rest/v1/leaderboard",
                params={"select": "id", "limit": 1},
                headers=HEADERS
            )
            return response.status_code == 200
        except:
            return False

async def test_basic_operations():
    """Test basic operations to verify setup"""
    print("🔍 Testing basic Supabase operations...")
    
    async with httpx.AsyncClient() as client:
        try:
            # Test GET
            print("📊 Testing GET /leaderboard...")
            response = await client.get(
                f"{SUPABASE_URL}/rest/v1/leaderboard",
                params={"order": "score.desc", "limit": 5},
                headers=HEADERS
            )
            
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.text}")
            
            if response.status_code == 200:
                print("✅ GET operation successful")
            else:
                print(f"❌ GET operation failed: {response.text}")
                return False
            
            # Test POST
            print("\n📝 Testing POST /leaderboard...")
            test_data = {"name": "TestPlayer", "score": 42}
            response = await client.post(
                f"{SUPABASE_URL}/rest/v1/leaderboard",
                json=test_data,
                headers=HEADERS
            )
            
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.text}")
            
            if response.status_code in [200, 201]:
                print("✅ POST operation successful")
            else:
                print(f"❌ POST operation failed: {response.text}")
                return False
            
            return True
            
        except Exception as e:
            print(f"❌ Test failed: {e}")
            return False

async def main():
    """Main function"""
    print("=" * 60)
    print("🚀 RIALO BIRD - SUPABASE SETUP VERIFICATION")
    print("=" * 60)
    print()
    
    print(f"🔗 Supabase URL: {SUPABASE_URL}")
    print(f"🔑 Anon Key: {SUPABASE_ANON_KEY[:20]}...")
    print()
    
    # Check if table exists
    table_exists = await check_table_exists()
    if table_exists:
        print("✅ Leaderboard table exists")
    else:
        print("❌ Leaderboard table does not exist")
        print()
        print("📋 Please run the following SQL in Supabase SQL Editor:")
        print("   Go to: https://drsyehmbsoofjdhtivdf.supabase.co/project/default/sql")
        print()
        print("```sql")
        print("CREATE TABLE leaderboard (")
        print("  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),")
        print("  name TEXT NOT NULL CHECK (length(name) <= 16),")
        print("  score INTEGER NOT NULL CHECK (score >= 0 AND score <= 1000000),")
        print("  created_at TIMESTAMPTZ DEFAULT NOW()")
        print(");")
        print()
        print("-- Enable RLS")
        print("ALTER TABLE leaderboard ENABLE ROW LEVEL SECURITY;")
        print()
        print("-- Create policies")
        print('CREATE POLICY "Allow anonymous read access" ON leaderboard FOR SELECT USING (true);')
        print('CREATE POLICY "Allow anonymous insert with constraints" ON leaderboard FOR INSERT WITH CHECK (')
        print('  length(name) >= 1 AND length(name) <= 16 AND')
        print('  score >= 0 AND score <= 1000000')
        print(');')
        print("```")
        print()
        return
    
    # Test operations
    success = await test_basic_operations()
    
    print()
    print("=" * 60)
    if success:
        print("✅ SUPABASE SETUP VERIFIED - Ready for game development!")
    else:
        print("❌ SUPABASE SETUP NEEDS ATTENTION")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())

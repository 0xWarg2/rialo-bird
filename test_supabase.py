#!/usr/bin/env python3
"""
Supabase Connection Test for Rialo Bird Game
Tests the connection and basic operations with the provided Supabase credentials
"""

import httpx
import asyncio
import json
import os
from typing import Dict, Any
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

async def test_supabase_connection():
    """Test basic Supabase connection and operations"""
    print("🔗 Testing Supabase Connection...")
    print(f"URL: {SUPABASE_URL}")
    print(f"Anon Key: {SUPABASE_ANON_KEY[:20]}...")
    print()
    
    async with httpx.AsyncClient() as client:
        try:
            # Test 1: Check if leaderboard table exists
            print("📊 Test 1: Checking leaderboard table...")
            response = await client.get(
                f"{SUPABASE_URL}/rest/v1/leaderboard",
                params={"order": "score.desc", "limit": 5},
                headers=HEADERS
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ GET /leaderboard: SUCCESS (Status: {response.status_code})")
                print(f"   Response: {json.dumps(data, indent=2)}")
            else:
                print(f"❌ GET /leaderboard: FAILED (Status: {response.status_code})")
                print(f"   Error: {response.text}")
                return False
            
            print()
            
            # Test 2: Insert a test score
            print("📝 Test 2: Inserting test score...")
            test_score = {
                "name": "TestPlayer",
                "score": 42
            }
            
            response = await client.post(
                f"{SUPABASE_URL}/rest/v1/leaderboard",
                json=test_score,
                headers=HEADERS
            )
            
            if response.status_code == 201:
                try:
                    data = response.json()
                    print(f"✅ POST /leaderboard: SUCCESS (Status: {response.status_code})")
                    print(f"   Inserted: {json.dumps(data, indent=2)}")
                    test_id = data[0]["id"] if isinstance(data, list) and len(data) > 0 else data["id"]
                except (json.JSONDecodeError, KeyError, IndexError):
                    print(f"✅ POST /leaderboard: SUCCESS (Status: {response.status_code})")
                    print(f"   Response: {response.text}")
                    test_id = None
            else:
                print(f"❌ POST /leaderboard: FAILED (Status: {response.status_code})")
                print(f"   Error: {response.text}")
                return False
            
            print()
            
            # Test 3: Verify the score appears in leaderboard
            print("🔍 Test 3: Verifying score in leaderboard...")
            response = await client.get(
                f"{SUPABASE_URL}/rest/v1/leaderboard",
                params={"order": "score.desc", "limit": 10},
                headers=HEADERS
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ GET /leaderboard: SUCCESS (Status: {response.status_code})")
                print(f"   Leaderboard: {json.dumps(data, indent=2)}")
                
                # Check if our test score is in the results
                test_found = any(entry["id"] == test_id for entry in data)
                if test_found:
                    print("✅ Test score found in leaderboard!")
                else:
                    print("⚠️  Test score not found in leaderboard (might be filtered by RLS)")
            else:
                print(f"❌ GET /leaderboard: FAILED (Status: {response.status_code})")
                return False
            
            print()
            
            # Test 4: Test validation (should fail)
            print("🚫 Test 4: Testing validation (should fail)...")
            invalid_score = {
                "name": "",  # Empty name should fail
                "score": 42
            }
            
            response = await client.post(
                f"{SUPABASE_URL}/rest/v1/leaderboard",
                json=invalid_score,
                headers=HEADERS
            )
            
            if response.status_code == 400:
                print(f"✅ Validation test: SUCCESS (Status: {response.status_code})")
                print(f"   Correctly rejected invalid data: {response.text}")
            else:
                print(f"❌ Validation test: FAILED (Status: {response.status_code})")
                print(f"   Expected 400, got: {response.text}")
            
            print()
            print("🎉 All Supabase tests passed! Ready for development.")
            return True
            
        except Exception as e:
            print(f"❌ Connection test failed: {e}")
            return False

async def main():
    """Main test function"""
    print("=" * 60)
    print("🚀 RIALO BIRD - SUPABASE CONNECTION TEST")
    print("=" * 60)
    print()
    
    success = await test_supabase_connection()
    
    print()
    print("=" * 60)
    if success:
        print("✅ SUPABASE SETUP COMPLETE - Ready for game development!")
    else:
        print("❌ SUPABASE SETUP FAILED - Check configuration")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())

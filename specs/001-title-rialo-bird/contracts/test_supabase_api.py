# Supabase Leaderboard Contract Tests

**Feature**: 001-title-rialo-bird  
**Date**: 2025-01-27  
**Status**: Complete

## Test Setup

### Prerequisites
- Supabase staging project configured
- Environment variables set:
  - `SUPABASE_URL`: Staging project URL
  - `SUPABASE_ANON_KEY`: Anonymous API key
- Test data cleanup between runs

### Test Configuration
```python
import pytest
import httpx
import os
from typing import Dict, Any

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://drsyehmbsoofjdhtivdf.supabase.co")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRyc3llaG1ic29vZmpkaHRpdmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODA4NjEsImV4cCI6MjA3MzY1Njg2MX0.Z5R9KzkkUJL3bxjrFrse4lzziwJSbwG3SyI_caj9CCc")

HEADERS = {
    "apikey": SUPABASE_ANON_KEY,
    "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
    "Content-Type": "application/json"
}
```

## Contract Tests

### Test GET /leaderboard - Success Cases

```python
@pytest.mark.asyncio
async def test_get_leaderboard_success():
    """Test successful leaderboard retrieval"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SUPABASE_URL}/leaderboard",
            params={"order": "score.desc", "limit": 10},
            headers=HEADERS
        )
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) <= 10
        
        # Verify response structure
        for entry in data:
            assert "id" in entry
            assert "name" in entry
            assert "score" in entry
            assert "created_at" in entry
            assert isinstance(entry["score"], int)
            assert 0 <= entry["score"] <= 1000000
```

```python
@pytest.mark.asyncio
async def test_get_leaderboard_ordering():
    """Test leaderboard is ordered by score descending"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SUPABASE_URL}/leaderboard",
            params={"order": "score.desc", "limit": 5},
            headers=HEADERS
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify descending order
        for i in range(len(data) - 1):
            assert data[i]["score"] >= data[i + 1]["score"]
```

### Test GET /leaderboard - Error Cases

```python
@pytest.mark.asyncio
async def test_get_leaderboard_invalid_order():
    """Test invalid order parameter returns 400"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SUPABASE_URL}/leaderboard",
            params={"order": "invalid"},
            headers=HEADERS
        )
        
        assert response.status_code == 400
```

```python
@pytest.mark.asyncio
async def test_get_leaderboard_invalid_limit():
    """Test limit exceeding maximum returns 400"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SUPABASE_URL}/leaderboard",
            params={"order": "score.desc", "limit": 100},
            headers=HEADERS
        )
        
        assert response.status_code == 400
```

```python
@pytest.mark.asyncio
async def test_get_leaderboard_unauthorized():
    """Test missing API key returns 401"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SUPABASE_URL}/leaderboard",
            params={"order": "score.desc"}
        )
        
        assert response.status_code == 401
```

### Test POST /leaderboard - Success Cases

```python
@pytest.mark.asyncio
async def test_post_leaderboard_success():
    """Test successful score submission"""
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "TestPlayer",
            "score": 42
        }
        
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "TestPlayer"
        assert data["score"] == 42
        assert "id" in data
        assert "created_at" in data
```

```python
@pytest.mark.asyncio
async def test_post_leaderboard_max_score():
    """Test maximum valid score submission"""
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "MaxPlayer",
            "score": 1000000
        }
        
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["score"] == 1000000
```

### Test POST /leaderboard - Error Cases

```python
@pytest.mark.asyncio
async def test_post_leaderboard_invalid_name():
    """Test invalid name returns 400"""
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "",  # Empty name
            "score": 42
        }
        
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 400
```

```python
@pytest.mark.asyncio
async def test_post_leaderboard_name_too_long():
    """Test name exceeding 16 characters returns 400"""
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "ThisNameIsWayTooLongForTheGame",
            "score": 42
        }
        
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 400
```

```python
@pytest.mark.asyncio
async def test_post_leaderboard_negative_score():
    """Test negative score returns 400"""
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "TestPlayer",
            "score": -1
        }
        
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 400
```

```python
@pytest.mark.asyncio
async def test_post_leaderboard_score_too_high():
    """Test score exceeding maximum returns 400"""
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "TestPlayer",
            "score": 1000001
        }
        
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 400
```

```python
@pytest.mark.asyncio
async def test_post_leaderboard_missing_fields():
    """Test missing required fields returns 400"""
    async with httpx.AsyncClient() as client:
        payload = {
            "name": "TestPlayer"
            # Missing score field
        }
        
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        
        assert response.status_code == 400
```

## Rate Limiting Tests

```python
@pytest.mark.asyncio
async def test_rate_limiting():
    """Test rate limiting behavior"""
    async with httpx.AsyncClient() as client:
        # Make multiple rapid requests
        tasks = []
        for i in range(15):  # Exceed 10/minute limit
            task = client.get(
                f"{SUPABASE_URL}/leaderboard",
                params={"order": "score.desc"},
                headers=HEADERS
            )
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        
        # At least one should be rate limited
        rate_limited = any(
            isinstance(r, httpx.HTTPStatusError) and r.response.status_code == 429
            for r in responses
        )
        assert rate_limited
```

## RLS Policy Tests

```python
@pytest.mark.asyncio
async def test_rls_select_policy():
    """Test RLS allows anonymous read access"""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SUPABASE_URL}/leaderboard",
            params={"order": "score.desc"},
            headers=HEADERS
        )
        
        assert response.status_code == 200
```

```python
@pytest.mark.asyncio
async def test_rls_insert_policy():
    """Test RLS enforces insert constraints"""
    async with httpx.AsyncClient() as client:
        # Valid insert should succeed
        payload = {"name": "ValidPlayer", "score": 50}
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        assert response.status_code == 201
        
        # Invalid insert should fail
        payload = {"name": "", "score": 50}
        response = await client.post(
            f"{SUPABASE_URL}/leaderboard",
            json=payload,
            headers=HEADERS
        )
        assert response.status_code == 400
```

## Test Data Management

```python
@pytest.fixture(autouse=True)
async def cleanup_test_data():
    """Clean up test data after each test"""
    yield
    # Clean up any test data created during tests
    async with httpx.AsyncClient() as client:
        # Delete test entries (implement cleanup logic)
        pass
```

## Running Tests

```bash
# Run all contract tests
pytest tests/contract/test_supabase_api.py -v

# Run specific test
pytest tests/contract/test_supabase_api.py::test_get_leaderboard_success -v

# Run with coverage
pytest tests/contract/test_supabase_api.py --cov=src --cov-report=html
```

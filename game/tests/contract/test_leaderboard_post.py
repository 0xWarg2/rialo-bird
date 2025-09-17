import os
import json
import uuid
import pytest

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover
    load_dotenv = None

import httpx


def _load_env():
    if load_dotenv is not None:
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        env_path = os.path.join(root, "supabase-config.env")
        if os.path.exists(env_path):
            load_dotenv(env_path)


def _get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        pytest.fail(f"Missing required environment variable: {name}. Configure in supabase-config.env")
    return value


@pytest.mark.contract
def test_post_leaderboard_valid_body_contract():
    _load_env()

    base_url = os.getenv("SUPABASE_REST_URL", "https://drsyehmbsoofjdhtivdf.supabase.co/rest/v1")
    apikey = _get_required_env("SUPABASE_ANON_KEY")
    bearer = os.getenv("SUPABASE_SERVICE_ROLE_KEY", apikey)

    headers = {
        "apikey": apikey,
        "Authorization": f"Bearer {bearer}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }

    url = f"{base_url}/leaderboard"
    payload = {"name": f"Player-{str(uuid.uuid4())[:8]}", "score": 1}

    resp = httpx.post(url, headers=headers, json=payload)

    assert resp.status_code in (200, 201), f"Expected 200/201, got {resp.status_code}: {resp.text}"

    try:
        data = resp.json()
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")

    # PostgREST may return list or object depending on Prefer header
    if isinstance(data, list):
        assert len(data) >= 1
        item = data[0]
    else:
        item = data

    for key in ("id", "name", "score", "created_at"):
        assert key in item, f"Missing key '{key}' in response"


@pytest.mark.contract
def test_post_leaderboard_validation_errors():
    _load_env()

    base_url = os.getenv("SUPABASE_REST_URL", "https://drsyehmbsoofjdhtivdf.supabase.co/rest/v1")
    apikey = _get_required_env("SUPABASE_ANON_KEY")
    bearer = os.getenv("SUPABASE_SERVICE_ROLE_KEY", apikey)

    headers = {
        "apikey": apikey,
        "Authorization": f"Bearer {bearer}",
        "Content-Type": "application/json",
    }

    url = f"{base_url}/leaderboard"

    # Invalid: name too long
    bad_payload = {"name": "X" * 100, "score": -1}
    resp = httpx.post(url, headers=headers, json=bad_payload)

    assert resp.status_code in (400, 401, 403), (
        f"Expected validation/auth error (400/401/403), got {resp.status_code}: {resp.text}"
    )



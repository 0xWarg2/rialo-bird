import os
import json
import pytest

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover
    load_dotenv = None

import httpx


def _load_env():
    # Load from project root supabase-config.env if python-dotenv available
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
def test_get_leaderboard_top10_contract():
    _load_env()

    base_url = os.getenv("SUPABASE_REST_URL", "https://drsyehmbsoofjdhtivdf.supabase.co/rest/v1")
    apikey = _get_required_env("SUPABASE_ANON_KEY")
    bearer = os.getenv("SUPABASE_SERVICE_ROLE_KEY", apikey)

    headers = {
        "apikey": apikey,
        "Authorization": f"Bearer {bearer}",
        "Accept": "application/json",
    }

    params = {"order": "score.desc", "limit": 10, "select": "id,name,score,created_at", "" : ""}
    # Note: Using table name explicitly as per PostgREST convention
    url = f"{base_url}/leaderboard"

    resp = httpx.get(url, headers=headers, params={k: v for k, v in params.items() if k})

    # Contract: must be 200 and a JSON array with fields
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}: {resp.text}"

    try:
        data = resp.json()
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")

    assert isinstance(data, list), "Leaderboard response must be a list"
    # If empty list, still must conform to schema on potential items
    if data:
        item = data[0]
        for key in ("id", "name", "score", "created_at"):
            assert key in item, f"Missing key '{key}' in leaderboard item"



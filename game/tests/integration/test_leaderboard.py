import os
import pytest

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover
    load_dotenv = None


@pytest.mark.integration
def test_leaderboard_service_contract():
    """
    Requires a Supabase client wrapper and LeaderboardService with methods:
      - fetch_top(limit=10) -> list[{id,name,score,created_at}]
      - submit_score(name, score) -> {id,name,score,created_at}
    Uses env from supabase-config.env for real staging.
    """
    if load_dotenv is not None:
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        env_path = os.path.join(root, "supabase-config.env")
        if os.path.exists(env_path):
            load_dotenv(env_path)

    from game.src.services.supabase_client import SupabaseClient  # expected later
    from game.src.services.leaderboard_service import LeaderboardService  # expected later

    client = SupabaseClient()
    service = LeaderboardService(client)

    top = service.fetch_top(limit=5)
    assert isinstance(top, list)
    if top:
        item = top[0]
        for k in ("id", "name", "score", "created_at"):
            assert k in item

    # Do not actually submit here to avoid polluting staging; instead the contract enforces method presence
    assert hasattr(service, "submit_score")



import pytest


@pytest.mark.integration
def test_game_state_transitions_contract():
    """
    This test encodes required transitions from data-model.md:
    MAIN_MENU → RUNNING → PAUSED → RUNNING → GAME_OVER → MAIN_MENU
    and MAIN_MENU → LEADERBOARD_VIEW, MAIN_MENU → SETTINGS
    Implementation must provide GameState enum and a GameStateManager with methods:
      - start_game(), pause(), resume(), game_over(), to_menu(), to_leaderboard(), to_settings()
    """
    from game.src.models.game_state import GameState  # expected to exist later
    from game.src.states.game_state_manager import GameStateManager  # expected to exist later

    manager = GameStateManager()

    assert manager.state == GameState.MAIN_MENU

    manager.start_game()
    assert manager.state == GameState.RUNNING

    manager.pause()
    assert manager.state == GameState.PAUSED

    manager.resume()
    assert manager.state == GameState.RUNNING

    manager.game_over()
    assert manager.state == GameState.GAME_OVER

    manager.to_menu()
    assert manager.state == GameState.MAIN_MENU

    manager.to_leaderboard()
    assert manager.state == GameState.LEADERBOARD_VIEW

    manager.to_menu()
    manager.to_settings()
    assert manager.state == GameState.SETTINGS



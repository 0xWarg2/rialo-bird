import pytest


@pytest.mark.integration
def test_scoring_rules_contract():
    """
    Encodes scoring rules from data-model.md:
    - +1 per pipe passed
    - multiplier may modify increments
    - high score updates on game over
    Requires Score entity and ScoringSystem with:
      add_pipe_pass(score), apply_multiplier(score, m), on_game_over(score)
    """
    from game.src.entities.score import Score  # expected later
    from game.src.systems.scoring import ScoringSystem  # expected later

    system = ScoringSystem()
    score = Score()
    score.current_score = 0
    score.high_score = 0
    score.multiplier = 1.0

    system.add_pipe_pass(score)
    assert score.current_score == 1

    system.apply_multiplier(score, 2.0)
    system.add_pipe_pass(score)
    assert score.current_score == 3  # +2 with multiplier

    system.on_game_over(score)
    assert score.high_score == 3



class ScoringSystem:
    def add_pipe_pass(self, score) -> None:
        increment = int(round(1 * max(0.0, score.multiplier)))
        score.current_score += increment

    def apply_multiplier(self, score, multiplier: float) -> None:
        score.multiplier = float(multiplier)

    def on_game_over(self, score) -> None:
        if score.current_score > score.high_score:
            score.high_score = score.current_score



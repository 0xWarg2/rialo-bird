class HUD:
    def __init__(self) -> None:
        self.score_text = "0"

    def set_score(self, score: int) -> None:
        self.score_text = str(int(score))

    def draw(self) -> None:
        pass



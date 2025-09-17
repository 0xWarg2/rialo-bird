from game.src.models.game_state import GameState


class GameStateManager:
    def __init__(self) -> None:
        self.state = GameState.MAIN_MENU

    def start_game(self) -> None:
        self.state = GameState.RUNNING

    def pause(self) -> None:
        if self.state == GameState.RUNNING:
            self.state = GameState.PAUSED

    def resume(self) -> None:
        if self.state == GameState.PAUSED:
            self.state = GameState.RUNNING

    def game_over(self) -> None:
        if self.state == GameState.RUNNING:
            self.state = GameState.GAME_OVER

    def to_menu(self) -> None:
        self.state = GameState.MAIN_MENU

    def to_leaderboard(self) -> None:
        self.state = GameState.LEADERBOARD_VIEW

    def to_settings(self) -> None:
        self.state = GameState.SETTINGS



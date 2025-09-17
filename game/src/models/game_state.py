from enum import Enum, auto


class GameState(Enum):
    MAIN_MENU = auto()
    RUNNING = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    LEADERBOARD_VIEW = auto()
    SETTINGS = auto()



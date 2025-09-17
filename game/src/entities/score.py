from dataclasses import dataclass


@dataclass
class Score:
    current_score: int = 0
    high_score: int = 0
    multiplier: float = 1.0



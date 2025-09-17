from dataclasses import dataclass


@dataclass
class SaveData:
    high_score: int = 0
    last_score: int = 0



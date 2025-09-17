from dataclasses import dataclass


@dataclass
class Settings:
    sound_enabled: bool = True
    music_enabled: bool = True
    difficulty: str = "normal"



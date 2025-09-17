from dataclasses import dataclass, field
from game.src.models.vector import Vector2


@dataclass
class Background:
    position: Vector2 = field(default_factory=Vector2)
    scroll_speed: float = 0.0



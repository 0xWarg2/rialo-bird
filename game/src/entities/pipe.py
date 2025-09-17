from dataclasses import dataclass, field
from game.src.models.vector import Vector2


@dataclass
class Pipe:
    position: Vector2 = field(default_factory=Vector2)
    gap_y: float = 300.0
    gap_size: float = 150.0
    width: float = 80.0
    height: float = 600.0



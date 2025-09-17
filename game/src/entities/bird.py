from dataclasses import dataclass, field
from game.src.models.vector import Vector2


@dataclass
class Bird:
    position: Vector2 = field(default_factory=Vector2)
    velocity: Vector2 = field(default_factory=Vector2)
    rotation: float = 0.0
    width: float = 64.0
    height: float = 64.0



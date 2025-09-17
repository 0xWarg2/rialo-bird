from dataclasses import dataclass


@dataclass
class Vector2:
    x: float = 0.0
    y: float = 0.0

    def __iter__(self):
        yield self.x
        yield self.y



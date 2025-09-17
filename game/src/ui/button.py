from dataclasses import dataclass


@dataclass
class Button:
    label: str
    x: float
    y: float
    width: float = 160
    height: float = 48

    def draw(self) -> None:
        pass

    def contains(self, px: float, py: float) -> bool:
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height



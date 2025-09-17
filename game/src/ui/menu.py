from typing import List
from game.src.ui.button import Button


class Menu:
    def __init__(self, buttons: List[Button] | None = None) -> None:
        self.buttons: List[Button] = buttons or []

    def add_button(self, button: Button) -> None:
        self.buttons.append(button)

    def draw(self) -> None:
        for btn in self.buttons:
            btn.draw()



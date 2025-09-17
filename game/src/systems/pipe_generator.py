from dataclasses import dataclass
from typing import List

from game.src.entities.pipe import Pipe
from game.src.models.vector import Vector2


@dataclass
class PipeGenerator:
    spawn_interval: float = 1.5
    pipe_gap: float = 160.0
    pipe_width: float = 80.0
    pipe_height: float = 600.0
    last_spawn_time: float = 0.0

    def spawn_if_needed(self, elapsed_time: float, x: float, gap_y: float) -> List[Pipe]:
        """Return a list with a new Pipe when interval elapsed; otherwise empty list.

        This is a minimal utility to satisfy T023; gameplay tuning can evolve later.
        """
        if elapsed_time - self.last_spawn_time >= self.spawn_interval:
            self.last_spawn_time = elapsed_time
            pipe = Pipe(
                position=Vector2(x, 0.0),
                gap_y=gap_y,
                gap_size=self.pipe_gap,
                width=self.pipe_width,
                height=self.pipe_height,
            )
            return [pipe]
        return []



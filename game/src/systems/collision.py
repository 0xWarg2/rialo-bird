class CollisionSystem:
    def _bird_bbox(self, bird):
        # Axis-aligned bounding box centered at position
        half_w = bird.width / 2
        half_h = bird.height / 2
        left = bird.position.x - half_w
        right = bird.position.x + half_w
        bottom = bird.position.y - half_h
        top = bird.position.y + half_h
        return left, right, bottom, top

    def _pipe_solids(self, pipe):
        # Two solid rectangles: top above gap, bottom below gap
        left = pipe.position.x - pipe.width / 2
        right = pipe.position.x + pipe.width / 2
        top_rect = (left, right, pipe.gap_y + pipe.gap_size / 2, pipe.height)
        bottom_rect = (left, right, 0.0, pipe.gap_y - pipe.gap_size / 2)
        return [top_rect, bottom_rect]

    @staticmethod
    def _overlap(a, b):
        al, ar, ab, at = a
        bl, br, bb, bt = b
        return (al < br) and (ar > bl) and (ab < bt) and (at > bb)

    def check_bird_pipe(self, bird, pipes):
        bird_bb = self._bird_bbox(bird)
        for pipe in pipes:
            for solid in self._pipe_solids(pipe):
                if self._overlap(bird_bb, solid):
                    return True
        return False



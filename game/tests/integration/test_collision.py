import pytest


@pytest.mark.integration
def test_collision_detection_contract():
    """
    Requires a CollisionSystem with method check_bird_pipe(bird, pipes)->bool
    True when bird intersects any pipe (excluding the gap region)
    Also requires Bird and Pipe entities with bounding boxes.
    """
    from game.src.entities.bird import Bird  # expected later
    from game.src.entities.pipe import Pipe  # expected later
    from game.src.systems.collision import CollisionSystem  # expected later

    bird = Bird()
    bird.position.x = 100
    bird.position.y = 200

    # Create a pipe overlapping bird's x but with gap away from bird y
    pipe = Pipe()
    pipe.position.x = 100
    pipe.gap_y = 400
    pipe.gap_size = 150
    pipe.width = 80
    pipe.height = 600

    system = CollisionSystem()
    collided = system.check_bird_pipe(bird, [pipe])

    assert isinstance(collided, bool)
    # With gap at 400 and bird at 200, expect collision with top/bottom pipe
    assert collided is True



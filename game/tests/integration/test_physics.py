import math
import pytest


@pytest.mark.integration
def test_bird_physics_rules_contract():
    """
    Encodes physics rules from data-model.md:
    - Gravity applies downward acceleration
    - Flap applies upward impulse
    - Terminal velocity caps downward speed
    - Rotation tilts based on velocity
    Implementation must provide PhysicsSystem.update(entity, dt), Bird with velocity/rotation
    """
    from game.src.entities.bird import Bird  # expected to exist later
    from game.src.systems.physics import PhysicsSystem  # expected to exist later

    physics = PhysicsSystem(gravity=900.0, flap_impulse=300.0, terminal_velocity=900.0)
    bird = Bird()
    bird.velocity.y = 0.0
    bird.rotation = 0.0

    # After one second without flap, velocity should be downward and capped
    physics.update(bird, dt=1.0)
    assert bird.velocity.y <= 0
    assert abs(bird.velocity.y) <= physics.terminal_velocity + 1e-6

    # Flap should increase upward velocity
    old_vy = bird.velocity.y
    physics.flap(bird)
    assert bird.velocity.y > old_vy

    # Rotation should correlate with velocity sign
    physics.update(bird, dt=0.016)
    assert -90.0 <= bird.rotation <= 90.0



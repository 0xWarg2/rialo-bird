from dataclasses import dataclass


@dataclass
class PhysicsSystem:
    gravity: float = 900.0
    flap_impulse: float = 300.0
    terminal_velocity: float = 900.0

    def update(self, entity, dt: float) -> None:
        # Apply gravity (down is negative y)
        entity.velocity.y -= self.gravity * dt
        # Clamp terminal velocity
        if entity.velocity.y < -self.terminal_velocity:
            entity.velocity.y = -self.terminal_velocity
        # Integrate position
        entity.position.y += entity.velocity.y * dt
        # Simple rotation based on velocity (-90..90)
        max_deg = 90.0
        entity.rotation = max(-max_deg, min(max_deg, (entity.velocity.y / self.terminal_velocity) * max_deg))

    def flap(self, entity) -> None:
        entity.velocity.y += self.flap_impulse



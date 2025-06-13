import pygame

from .utils import wrap_position

SHIP_WIDTH = 30
SHIP_HEIGHT = 20

# Ship Stats
SHIP_MANEUVERABILITY = 4
SHIP_ACCELERATION = 0.05
SHIP_MAX_SPEED = 14.0


class Player(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super(Player, self).__init__()

        self.velocity = pygame.Vector2(0, 0)
        # This is multiplied by velocity, so the higher the number the we start with
        # here the faster the acceleration.
        self.direction = pygame.Vector2(0, -1)
        self.position = position
        self.surface = pygame.Surface(
            (SHIP_WIDTH, SHIP_HEIGHT),
            pygame.SRCALPHA
        )

        # Draw the triangle "spaceship" on the surface
        pygame.draw.polygon(
            self.surface,
            (255, 0, 0),
            [[0, 0], [30, 10], [0, 20]]
        )

    # Move the sprite based on user keypresses
    def handle_input(self):
        pressed_keys = pygame.key.get_pressed()
        # Handle rotation
        if pressed_keys[pygame.K_d]:
            self.direction.rotate_ip(SHIP_MANEUVERABILITY)
        elif pressed_keys[pygame.K_a]:
            self.direction.rotate_ip(-SHIP_MANEUVERABILITY)

        # Accelerate the ship
        if pressed_keys[pygame.K_w]:
            self.velocity += self.direction * SHIP_ACCELERATION
            self.velocity = self.velocity.clamp_magnitude(0, SHIP_MAX_SPEED)

    def draw(self, surface):
        angle = self.direction.angle_to((1, 0))
        rotated_surface = pygame.transform.rotate(self.surface, angle)

        # If we go off one side of the screen, we should appear on the opposite side
        self.position = wrap_position(self.position + self.velocity, surface)

        surface.blit(rotated_surface, rotated_surface.get_rect(
            center=(round(self.position.x), round(self.position.y))))

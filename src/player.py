import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2):
        super(Player, self).__init__()

        self.surf = pygame.Surface((50, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.rect.x = pos.x
        self.rect.y = pos.y

    # Move the sprite based on user keypresses
    def handle_input(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(5, 0)

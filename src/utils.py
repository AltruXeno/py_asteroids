import pygame


def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return pygame.Vector2(x % w, y % h)

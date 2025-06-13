# Import and initialize the pygame library
import pygame

from src.player import Player
from src.config import (SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR)


class Game:
    def __init__(self):
        pygame.init()

        # Set up the drawing window
        pygame.display.set_caption("Asteroids")
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # Create the player in the middle of the screen
        self.player = Player(pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        # Create the game clock for FPS management
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.process_input()
            # Fill the screen with black to clear the screen
            self.screen.fill(BG_COLOR)
            # Draw the player on the screen
            self.player.draw(self.screen)
            # Flip the display and tick the clock
            pygame.display.flip()
            self.clock.tick(30)

    def process_input(self):
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key and was it the escape key?
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == pygame.QUIT:
                quit()

        # Tell the player to check for input
        self.player.handle_input()


if __name__ == "__main__":
    game = Game()
    game.run()

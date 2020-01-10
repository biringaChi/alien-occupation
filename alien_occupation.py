import sys
import pygame
from settings import Settings
from spaceship import Spaceship


class AlienOccupation():
    """A simple game of an army of aliens invasion and occupation"""

    def __init__(self, name, description):
        self.name = name.title()
        self.description = description

    def __repr__(self):
        return f"{self.name} is an {self.description}"

    def run(self):
        pygame.init()
        """Game's settings initialized"""
        game_settings = Settings()
        screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
        pygame.display.set_caption(game_settings.caption_display)

        # Ship
        spaceship = Spaceship(screen)

        # Event monitoring
        while True:
            for event in pygame.event.get():
                screen.fill(game_settings.background_color)
                spaceship.blit_ss()

                if event.type == pygame.QUIT:
                    print("You just exited the game.")
                    sys.exit()

            # Latest screen frame
            pygame.display.flip()

# Object instance
description = "a simple game of an army of aliens' invasion and occupation"
alien_occupation = AlienOccupation("alien occupation", description)
alien_occupation.run()

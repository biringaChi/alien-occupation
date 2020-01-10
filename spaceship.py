import pygame

class Spaceship():
    """A spaceship"""

    def __init__(self, screen):
        """screen's starting point"""
        self.screen = screen

        self.image = pygame.image.load('images/spaceships/spaceship_4.bmp')
        self.rect = self.image.get_rect()

        # Ship's positioning
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blit_ss(self):
        """Draw ship at present location"""
        self.screen.blit(self.image, self.rect)





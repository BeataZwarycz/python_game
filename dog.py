import pygame

from pygame.sprite import Sprite

class Dog(Sprite):
    """Dog's class."""

    def __init__(self, game_settings, screen):
        """Inicialization dog and its start position."""
        super(Dog, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Download dog's image.
        self.image = pygame.image.load('images/dog.bmp')
        self.rect = self.image.get_rect()

        # Every new dog will be on the right corner of screen.
        self.rect.x = 1200
        self.rect.y = self.rect.height

        # Storage of the exact position of the dog.
        self.x = float(self.rect.x)

    def blitme(self):
        """Display dog on its' current position."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True, if dog is on the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= screen_rect.top:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        """Move dog down and up."""
        self.y += self.game_settings.dog_speed_factor * self.game_settings.pack_direction
        self.rect.y = self.y
import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class designed to order bullets fired by cat."""

    def __init__(self, game_settings, screen, cat):
        """Create bullet object at current cat's position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create rectangle of bullets at (0,0) point and then determine its' position.
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centery = cat.rect.centery
        self.rect.left = cat.rect.left

        # Bullet position is defined by a floating point value.
        self.x = float(self.rect.x)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Moving bullet on screen."""
        # Update bullet's position
        self.x += self.speed_factor

        # Update position of bullet's square
        self.rect.x = self.x

    def draw_bullet(self):
        """Display bulley on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
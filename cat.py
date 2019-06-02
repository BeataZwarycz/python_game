import pygame

class Cat():

    def __init__(self, game_settings, screen):
        """Inicialization cat and its start position."""

        self.screen = screen
        self.game_settings = game_settings

        # Loading a picture of a cat and downloading its rectangle.
        self.image = pygame.image.load('images/cat.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Every new cat will be on the left side of screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + 15

        # The cat's midpoint is stored as a floating point.
        self.center = [float(self.rect.centerx), float(self.rect.centery)]

        # Options that indicate the movement of the cat.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the cat's position based on the pointing option on his move."""

        # Update the value of the cat's midpoint, not its rectangle..
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center[0] += self.game_settings.cat_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center[0] -= self.game_settings.cat_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center[1] += self.game_settings.cat_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center[1] -= self.game_settings.cat_speed_factor

        # Update the rect object based on the self. center value.
        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]

    def blitme(self):
        """Display cat at its current position"""
        self.screen.blit(self.image, self.rect)
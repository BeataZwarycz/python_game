class Settings():
    """ A class designed to store all game settings."""

    def __init__(self):
        """Initialization game's settings."""
        # Screen settings.
        self.screen_width = 1350
        self.screen_height = 680
        self.bg_color = (100, 0, 0)

        # Settings of cat.
        self.cat_speed_factor = 1.5

        # Settings of bullets.
        self.bullet_speed_factor = 1.5
        self.bullet_width = 30
        self.bullet_height = 3
        self.bullet_color = (230, 10, 30)
        self.bullets_allowed = 5

        # Setting of dogs.
        self.dog_speed_factor = 1.5
        self.pack_drop_speed = 50
        self.pack_direction = -1
import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from cat import Cat
import game_functions as gf

def run_game():
    # Inicialization Pygame, settings and screen object.
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Cosmic War")

    # Create cat, group of bullets and group of dogs.
    cat = Cat(game_settings, screen)
    bullets = Group()
    # Create dog.
    dogs = Group()

    gf.create_pack(game_settings, screen, dogs)


    # Start main loop of game.
    while True:
        gf.check_events(game_settings, screen, cat, bullets)
        cat.update()
        gf.update_bullets(bullets, dogs)
        gf.update_dogs(game_settings, dogs)
        gf.update_screen(game_settings, screen, cat, bullets, dogs)

run_game()
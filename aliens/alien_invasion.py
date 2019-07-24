import pygame
from ship import Ship
import game_functions as gf
from settings import Settings
from pygame.sprite import Group

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set the background colour
    # bg_colour = (230, 230, 230)

    # Make a Ship
    ship = Ship(ai_settings, screen)
    # Make a group to store the bullets in
    bullets = Group()

    # Start the main loop for game
    while True:
        gf.check_events(ship)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
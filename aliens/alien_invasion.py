import pygame
from ship import Ship
import game_functions as gf
from settings import Settings

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

    # Start the main loop for game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
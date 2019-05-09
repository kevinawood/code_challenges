import sys
import pygame

from settings import Settings

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Set the background colour
    bg_colour = (230, 230, 230)

    # Start the main loop for game
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw screen during ech pass through loop
        screen.fill(ai_settings.bg_colour)

        # Make the most recently drawn visible
        pygame.display.flip()

run_game()
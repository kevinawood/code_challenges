import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Redraw screen during ech pass through loop
    screen.fill(ai_settings.bg_colour)
    ship.blitme()

    # Make the most recently drawn visible
    pygame.display.flip()
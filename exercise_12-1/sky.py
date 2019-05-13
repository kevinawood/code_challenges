import pygame
import sys
# from sky_settings import SkySettings

def sky():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    bg_colour = (38, 38, 198)
    pygame.display.set_caption("Blue Sky")

    screen.fill(bg_colour)

    pygame.display.flip()

sky()
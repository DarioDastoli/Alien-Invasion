import sys
import pygame 
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize game and screen settings, and screen objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    #make a ship
    ship = Ship(ai_settings, screen)
    #make a group to store bullets in.
    bullets = Group()

    running = True 

    while running:
    # watch for events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update_self()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        



run_game()
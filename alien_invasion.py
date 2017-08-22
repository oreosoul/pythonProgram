import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initial the game and create a screen object
    pygame.init()
    #创建 Setting 实例
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #创建一个飞船
    ship = Ship(screen)
    
    #The main loop
    while True:
        #listen keyboard and click events
        gf.check_events()
        #repaint screen in every loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #Let the recently painting screen visible
        pygame.display.flip()

run_game()

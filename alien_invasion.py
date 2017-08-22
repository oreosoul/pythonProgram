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
    ship = Ship(ai_settings,screen)
    
    #The main loop
    while True:
        #listen keyboard and click events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()

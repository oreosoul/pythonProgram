"""游戏主文件"""
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """运行游戏方法"""
    #initial the game and create a screen object
    pygame.init()
    #创建 Setting 实例
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #创建一个飞船
    ship = Ship(ai_settings, screen)

    #创建一个存储子弹的编组 Group
    bullets = Group()

    #The main loop
    while True:
        #检查玩家输入
        gf.check_events(ai_settings, screen, ship, bullets)
        #更新飞船
        ship.update()
        #更新子弹
        gf.update_bullet(bullets)
        #重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()

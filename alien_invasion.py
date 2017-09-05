"""游戏主文件"""
import pygame
from pygame.sprite import Group
from settings import Settings
from game_states import GameStates
from ship import Ship
from button import Button
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

    #创建开始按钮
    play_button = Button(ai_settings, screen, "PLAY!")

    #创建一个用于存储游戏统计信息的实例
    stats = GameStates(ai_settings)

    #创建一个飞船
    ship = Ship(ai_settings, screen)

    #创建一个存储子弹的编组 Group
    bullets = Group()

    #创建一个外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #The main loop
    while True:
        #检查玩家输入
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        #游戏主体需要启动方可运行
        if stats.game_active:
            #更新飞船
            ship.update()
            #更新子弹
            gf.update_bullet(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        #重绘屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()

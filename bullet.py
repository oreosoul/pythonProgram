"""子弹类文件"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对飞船发射子弹管理类"""

    def __init__(self, ai_settings, screen, ship):
        """子弹初始化"""
        super(Bullet, self).__init__()
        self.screen = screen
        #在屏幕(0, 0)处创建子弹并设位置于飞船顶部中央
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储小数表示子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        """子弹发射"""
        #更新子弹的小数
        self.y -= self.speed_factor
        #更新位置
        self.rect.y = self.y
    def draw_bullet(self):
        """在屏幕绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

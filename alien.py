"""外星人类文件"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """单个外星人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图形，并设置其rect
        self.image = pygame.image.load('images/alient.png')
        self.width, self.height = self.image.get_size()
        #设置图片大小
        self.image = pygame.transform.smoothscale(self.image, (self.width//12, self.height//12))
        self.rect = self.image.get_rect()

        #外星人初始位置于左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """判断是否移动至边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

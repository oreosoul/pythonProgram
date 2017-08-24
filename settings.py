"""设置文件"""
class Settings():
    """"存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """"初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        #飞船的速度
        self.ship_speed_factor = 1
        #子弹设置
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 3
        #星星数量
        self.star_number = 10

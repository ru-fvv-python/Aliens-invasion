import math

import pygame


class Shild:
    """Описывает энергитический щит корабля"""

    def __init__(self, ai_settings, screen, ship):
        """инициализирует щит"""
        self.shild_width = ai_settings.shild_width
        self.shild_height = ai_settings.shild_height
        self.color_red = ai_settings.color_red
        self.color_blue = ai_settings.color_blue
        self.shild_reduction = ai_settings.shild_reduction
        self.ship_shild = ai_settings.ship_shild
        self.ship_rect = ship.rect
        self.screen = screen

        # Создание щита в позиции (0,0) и назначение правильной позиции.
        self.surf = pygame.Surface((self.shild_width, self.shild_height))
        self.surf.fill(ai_settings.bg_color)
        self.surf.set_alpha(128)

        # квадрат щита, по центру и спереди корабля
        self.rect = self.surf.get_rect()
        self.rect.centerx = self.ship_rect.centerx
        self.rect.bottom = self.ship_rect.top


    def draw_shild(self):
        """Вывод щита на экран."""
        # рисуем щит
        x = 0
        y = 0
        width = self.rect.width
        height = self.rect.height
        startAngle = 0
        endAngle = math.pi
        lineWidth = 5

        # back part
        pygame.draw.arc(self.surf, self.color_blue, (x, y, width, height),
                        startAngle, endAngle, lineWidth)

        # left part
        startAngle = math.pi / 2 + (math.pi / 2) * self.ship_shild
        endAngle = math.pi
        pygame.draw.arc(self.surf, self.color_red, (x, y, width, height),
                        startAngle, endAngle,
                        lineWidth)

        # right part
        startAngle = 0
        endAngle = (math.pi / 2 - (math.pi / 2) * self.ship_shild)
        pygame.draw.arc(self.surf, self.color_red, (x, y, width, height),
                        startAngle, endAngle, lineWidth)

        self.screen.blit(self.surf, self.rect)

    def update(self):
        """положение: перед кораблем"""
        self.rect.centerx = self.ship_rect.centerx
        self.rect.top = self.ship_rect.top-10

    def shild_reducted(self):
        """показывает энергию щита"""
        self.ship_shild -= self.shild_reduction

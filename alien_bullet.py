import pygame
from pygame.sprite import Sprite


class BulletAlien(Sprite):
    """ Класс для управления пулями, выпущенными пришельцами."""

    def __init__(self, ai_settings, screen, alien):
        """Создает объект пули в текущей позиции пришельца. """
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = ai_settings.bullet_alien_color
        self.speed_factor = ai_settings.bullet_alien_speed_factor

        # Создание пули в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_alien_with,
                                ai_settings.bullet_alien_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        # Позиция пули хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает пулю вниз по экрану."""
        # Обновление позиции пули в вещественном формате.
        self.y += self.speed_factor
        # Обновление позиции прямоугольника.
        self.rect.y = self.y
        # уничтожение снаряда, вышедшего за экран
        if self.rect.top > self.screen_rect.height:
            self.kill()

    def draw_bullet(self):
        """Вывод пули на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)

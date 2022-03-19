import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает его начальную позицию."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # загружаем изображение в переменную sprite
        file_name = 'scout-ufo'
        self.image = pygame.image.load('images/{}.png'.format(file_name)) \
            .convert_alpha()

        # назначение атрибута rect.
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = 0
        self.rect.y = 0

        # Сохранение точной позиции пришельца.
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает пришельца вправо."""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x


from random import randint

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """ Класс для создания звездного неба"""

    def __init__(self, ai_settings):
        """создает звезду со случаным изображением из списка"""
        super(Star, self).__init__()
        self.ai_settings = ai_settings
        # скорость звезд
        self.star_speed = int(self.ai_settings.star_speed * randint(0, 3))

        file_name = 'stars'

        # список с картинками звезд из 5 файлов
        images = [
            pygame.image.load(
                'images/{}{}.png'.format(file_name, sf)
            ).convert_alpha()
            for sf in range(1, 6)
        ]

        # одна из пяти картинок
        sf = images[randint(0, 4)]

        # уменьшение картики нв случайную величину от 1 до 5
        zoom = randint(3, 5)

        # готовая картинка
        self.image = pygame.transform.scale(sf,
                                            (sf.get_width() // zoom,
                                             sf.get_height() // zoom)
                                            )
        self.rect = self.image.get_rect()

        # Каждая новая звезда появляется в левом верхнем углу экрана.
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        """обновление звезды"""
        if self.rect.y >= self.ai_settings.screen_height:
            self.rect.y = 0
        else:
            self.rect.y += self.star_speed

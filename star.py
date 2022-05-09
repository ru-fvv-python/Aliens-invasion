from random import randint

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """ Класс для создания звездного неба"""

    def __init__(self, ai_settings):
        """создает звезду со случаным изображением из списка"""
        super(Star, self).__init__()
        self.ai_settings = ai_settings

        file_name = 'stars'

        # список с картинками звезд из 5 файлов
        images = [
            pygame.image.load(
                'images/{}{}.png'.format(file_name, sf)
            ).convert_alpha()
            for sf in range(1, 6)
        ]

        # одна из пяти картинок
        self.sf = images[randint(0, 4)]

        # уменьшение картики нв случайную величину от 1 до 5
        self.zoom = randint(3, 6)

        # готовая картинка
        self.image = pygame.transform.scale(self.sf,
                                            (self.sf.get_width() // self.zoom,
                                             self.sf.get_height() // self.zoom)
                                            )
        # скорость и затемнение звезд
        if self.zoom == 6:
            self.star_speed = 0
            self.image.set_alpha(100)
        elif self.zoom == 5:
            self.star_speed = 1
            self.image.set_alpha(150)
        elif self.zoom == 4:
            self.star_speed = 2
            self.image.set_alpha(200)
        else:
            self.star_speed = 3

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

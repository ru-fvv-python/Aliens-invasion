from random import randint

import pygame

clock = pygame.time.Clock()


class JetFlame():
    """Реализует огонь реактивного двигателя корабля"""

    def __init__(self, ship, offset, zoom):
        self.ship_rect = ship.rect
        # список картинок анимации огня
        self.images = []
        # смещение координаты огня под двигатель
        # относительно центра корабля
        self.offset = offset
        # коэффициент уменьшения картинки
        self.zoom = zoom
        file_name = 'jet_flame'

        # заполение списка картинками
        for image in range(1, 5):
            image = pygame.image.load(
                'images/{}{}.png'.format(file_name, image)).convert_alpha()
            image_t = pygame.transform.scale(
                    image,
                    (image.get_width() // self.zoom,
                     image.get_height() // self.zoom)
            )
            self.images.append(image_t)

        self.image = self.images[0]
        self.rect = self.image.get_rect()

        # координаты: по центру и снизу корабля
        self.rect.top = self.ship_rect.bottom
        self.rect.centerx = self.ship_rect.centerx

    def update(self):
        """положение огня с учетом смешщения под двигатель
            анимация за счет выбора случайной картинки из списка
        """
        self.rect.top = self.ship_rect.bottom
        self.rect.centerx = self.ship_rect.centerx + self.offset
        self.image = self.images[randint(0, 3)]

import pygame


class Sphere():
    """ Класс анимации щита в вде сферы"""

    def __init__(self, screen, ship):
        """описывает сферу"""
        self.screen = screen
        self.ship_rect = ship.rect
        # сколько колонок и строк в таблице со спрайтами
        self.columns = 5
        self.rows = 4

        # читаем файл со спрайтами
        file_name = 'sphere'
        image_sprites = pygame.image.load(
            'images/{}.png'.format(file_name)).convert_alpha()

        # ширина и высота картины со спрайтами
        width_image_sprites = image_sprites.get_width()
        height_image_sprites = image_sprites.get_height()

        # определяем ширину ивысоту одного спрайта
        width_sprite = width_image_sprites / self.columns
        height_sprite = height_image_sprites / self.rows

        # список для изображний спрайтов из файла
        self.sprites = []

        # счетчик положения кадра на изображении
        count = 0
        # заполняем список для хранения кадров
        for row in range(int(height_image_sprites / height_sprite) - 1):
            for column in range(int(width_image_sprites / width_sprite) - 1):
                image_bt = image_sprites.subsurface(
                    pygame.Rect(
                        column * width_sprite,
                        count,
                        width_sprite,
                        height_sprite
                    )
                )
                image_t = pygame.transform.scale(image_bt,
                                                 (image_bt.get_width() * 1.5,
                                                  image_bt.get_height() * 1.5))

                self.sprites.append(image_t)

            # смещаемся на высоту кадра, т.е. переходим на другую строку
            count += int(height_sprite)

        # картинка из списка
        self.image = self.sprites[0]
        # квадрат картинки
        self.rect = self.image.get_rect()
        # берем координаты корабля игрока
        self.rect.center = self.ship_rect.center

        # координаты: по центру корабля
        self.rect.center = self.ship_rect.center
        # self.rect.centerx = self.ship_rect.centerx

        # номер спрайта (для отрисовки взрыва)
        self.number_sprite = 0

    def update(self):
        """анимация сферы щита"""
        # если номер спрайта менее длины списка спрайтов
        if self.number_sprite < len(self.sprites) - 1:
            # выбор очередного спрайта для отрисовки
            self.image = self.sprites[self.number_sprite]
            self.rect.center = self.ship_rect.center
            # отрисовка
            # self.screen.blit(self.image, self.rect)
            # увеличение счетчика спрайта
            self.number_sprite += 1
        else:
            # иначе сброс счетчика
            self.number_sprite = 0

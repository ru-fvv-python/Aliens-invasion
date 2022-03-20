import pygame


class Explosion():
    """ класс для создания взрыва"""

    def __init__(self, screen):
        """описывает взрыв"""

        self.screen = screen
        # имя файла со спрайтами
        file_sprites = 'explosion'
        # читаем файл
        image_sprites = pygame.image.load(
            'images/{}.png'.format(file_sprites)
        ).convert_alpha()

        # ширина и высота картины
        width_sprites = image_sprites.get_width()
        height_sprites = image_sprites.get_height()

        # сколько колонок и строк в таблице стпрайтов
        columns = 5
        rows = 6

        # определяем ширину ивысоту одного спрайта
        width_sprite = width_sprites / columns
        height_sprite = height_sprites / rows

        # список для изображний спрайтов из файла
        self.sprites = []

        # заполняем список для хранения кадров
        # счетчик положения кадра на изображении
        count = 0
        for row in range(int(height_sprites / height_sprite) - 1):
            for column in range(int(width_sprites / width_sprite) - 1):
                self.sprites.append(
                    image_sprites.subsurface(
                        pygame.Rect(
                            column * width_sprite,
                            count,
                            width_sprite,
                            height_sprite
                        )

                    )
                )
            # смещаемся на высоту кадра, т.е. переходим на другую строку
            count += int(height_sprite)

        self.image = self.sprites[0]
        self.rect = self.image.get_rect()

        # флаг взрыва
        self.flExp = False
        # номер спрайта (для отрисовки взрыва)
        self.number_sprite = 0

    def get_alien(self, aliens):
        """ берем координаты сбитого пришельца и меняет флаг взрыва"""
        for alien in aliens:
            # заводим координаты пришельца на квадрат для взрыва
            self.rect.center = alien.rect.center
            #  активируем флаг взрыва
            self.flExp = True

    def update(self):
        """анимирует взрыв"""
        # если флаг взрыва активен
        if self.flExp:
            # если номер спрайта менее длины списка спрайтов
            if self.number_sprite < len(self.sprites) - 1:
                # выбор очередного спрайта для отрисовки
                self.image = self.sprites[self.number_sprite]
                # отрисовка
                self.screen.blit(self.image, self.rect)
                # увеличение счетчика спрайта
                self.number_sprite += 1
            else:
                # иначе сброс счетчика и отключение флага
                self.number_sprite = 0
                self.flExp = False

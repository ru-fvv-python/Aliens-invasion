import pygame
from pygame.sprite import Sprite


class Explosion(Sprite):
    """ класс для создания взрыва"""

    def __init__(self, file_sprites, columns, rows, screen, downed_aliens=None,
                 rammed_alien=None, ship=None, shild=None):
        """описывает взрыв
            file_sprites - файл со спрайтами,
            columns - число колонок со спрайтами,
            rows - число строк со спрайтами,
            screen - экран,
            downed_aliens - список сбитых пришельцев пулями
            rammed_alien - пришелец протараненный кораблем игрока
            ship - подбитый корабль игрока пулей или протараненный пришельцем
            shild - блок шитом
        """
        super().__init__()
        self.screen = screen
        self.downed_aliens = downed_aliens
        self.rammed_alien = rammed_alien
        self.ship = ship
        self.shild = shild

        # читаем файл со спрайтами
        image_sprites = pygame.image.load(
            'images/{}.png'.format(file_sprites)
        ).convert_alpha()

        # ширина и высота картины со спрайтами
        width_sprites = image_sprites.get_width()
        height_sprites = image_sprites.get_height()

        # сколько колонок и строк в таблице со спрайтами
        self.columns = columns
        self.rows = rows

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

        # номер спрайта (для отрисовки взрыва)
        self.number_sprite = 0

        # определяем координаты для взрыва
        # берем координаты сбитого пулей пришельца
        if self.downed_aliens is not None:
            for downed_alien in self.downed_aliens:
                # присваиваем координаты сбитого корабля поверхности для взрыва
                self.rect.center = downed_alien.rect.center
                #  активируем флаг взрыва
                self.flExp = True

        # берем координаты протараненного кораблем пришельца
        if self.rammed_alien is not None:
            # присваиваем координаты пришельца поверхности для взрыва
            self.rect.center = rammed_alien.rect.center
            #  активируем флаг взрыва
            self.flExp = True

        # берем координаты подбитого корабля игрока
        if self.ship is not None:
            # присваиваем координаты корабля поверхности для взрыва
            self.rect.center = ship.rect.center
            #  активируем флаг взрыва
            self.flExp = True

        # берем координаты щита корабля
        if self.shild is not None:
            # присваиваем координаты переда щита для взрыва
            self.rect.center = shild.rect.center
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
                self.kill()

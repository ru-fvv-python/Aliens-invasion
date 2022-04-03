import pygame


class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Инициализирует статические настройки игры
        # параметры экрана -----------------------------------------
        self.screen_width = 1920
        self.screen_height = 1080
        self.fps = 60
        self.bg_color = (5, 5, 25)

        # параметры карабля ----------------------------------------
        self.ship_limit = 3  # ограничение количества кораблей
        # цвета для щита
        self.shild_width = 200
        self.shild_height = 100
        self.color_back_shild = (255, 0, 0)
        self.color_blue = (0, 212, 255)
        # уменьшение энергии щита за одно отражение снаряда
        self.shild_reduction = 0.1

        # параметры для пламени двигателя игрока -------------------
        self.offset_jet = 17  # смещение относительно центра под двигатель
        self.zoom = 2  # коэффициент уменьшения картинки.

        # параметры пули -------------------------------------------
        self.bullet_with = 3
        self.bullet_height = 25
        self.bullet_color = (219, 138, 17)
        self.bullets_allowed = 3

        # параметры пули пришельцев -------------------------------------
        self.bullet_alien_with = 3
        self.bullet_alien_height = 25
        self.bullet_alien_color = (105, 213, 244)
        self.bullets_alien_allowed = 5
        self.last_shot = pygame.time.get_ticks()

        # настройки пришельцев -----------------------------------------
        self.alien_drop_speed = 20

        # настройки звезд -----------------------------------------
        self.star_speed = 1  # коэффициент скорости звезд
        self.space_between_stars = 0.7  # коэффициент расстояния между звезд
        self.star_width = 150  # ширина звезды
        self.star_height = 300  # высота звезды
        self.offset = 100  # смещение по осям +-

        # Темп ускорения игры
        self.speed_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        # установка начальной скорости
        self.initialize_dynamic_settings()

        # громкость
        self.vol = 1.0

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки изменящиеся в ходе игры """
        self.alien_speed_factor = 5
        self.bullet_speed_factor = 10
        self.bullet_alien_speed_factor = 10
        self.speed = 5
        self.ship_shild = 1.0  # энергетический щит
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = -1
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев"""
        self.speed *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)

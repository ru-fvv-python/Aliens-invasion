class Settings():
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

        # параметры для пламени двигателя игрока -------------------
        self.offset_jet = 17  # смещение относительно центра под двигатель
        self.zoom = 2  # коэффициент уменьшения картинки.

        # параметры пули -------------------------------------------
        self.bullet_with = 5
        self.bullet_height = 25
        self.bullet_color = (219, 138, 17)
        self.bullets_allowed = 3

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

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки изменящиеся в ходе игры """
        self.alien_speed_factor = 3
        self.bullet_speed_factor = 15
        self.speed = 6
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
        print(self.alien_points)

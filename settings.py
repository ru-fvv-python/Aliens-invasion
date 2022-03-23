class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # параметры экрана -----------------------------------------
        self.screen_width = 1920
        self.screen_height = 1080
        self.fps = 60
        self.bg_color = (5, 5, 25)

        # параметры карабля ----------------------------------------
        self.speed = 8
        self.ship_limit = 3  # ограничение количества кораблей

        # параметры для пламени двигателя игрока -------------------
        self.offset_jet = 17  # смещение относительно центра под двигатель
        self.zoom = 2  # коэффициент уменьшения картинки.

        # параметры пули -------------------------------------------
        self.bullet_speed_factor = 20
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = (219, 138, 17)
        self.bullets_allowed = 3

        # настройки пришельцев -----------------------------------------
        self.alien_speed_factor = 3
        self.alien_drop_speed = 20
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = -1

        # настройки звезд -----------------------------------------
        self.star_speed = 1  # коэффициент скорости звезд
        self.space_between_stars = 1  # коэффициент расстояния между звезд
        self.star_width = 150  # ширина звезды
        self.star_height = 400  # высота звезды
        self.offset = 100  # смещение по осям +-



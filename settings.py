class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # параметры экрана -----------------------------------------
        self.screen_width = 1900
        self.screen_height = 1000
        self.fps = 60
        self.bg_color = (15, 15, 100)

        # параметры карабля ----------------------------------------
        self.speed = 10

        # параметры для пламени двигателя игрока -------------------
        self.offset = 17  # смещение относительно центра под двигатель
        self.zoom = 2  # коэффициент уменьшения картинки.

        # параметры пули -------------------------------------------
        self.bullet_speed_factor = 10
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = (219, 138, 17)
        self.bullets_allowed = 4

        # настройки пришельцев -----------------------------------------
        self.alien_speed_factor = 1
        self.alien_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = -1

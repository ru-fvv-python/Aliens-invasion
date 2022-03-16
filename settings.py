class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.fps = 60
        self.bg_color = (15, 15, 100)

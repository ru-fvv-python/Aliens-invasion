class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.ship_left = 0

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ship_left = self.ai_settings.ship_limit

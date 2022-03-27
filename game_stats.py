class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.ship_left = 0  # остаток кораблей у игрока

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        # Рекорд не должен сбрасываться
        self.high_score = 0

        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0  # очки игрока


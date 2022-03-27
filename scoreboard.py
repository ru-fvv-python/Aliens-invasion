import pygame


class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, ai_settings, screen, stats):
        """Инициализирует атрибуты подсчета очков."""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats

        # Настройка шрифта для вывода счета
        self.text_color = (255, 204, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Подготовка исходного изображения счетов
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение"""
        # текущий счет
        rounded_score = int(round(self.stats.score, -1))
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение"""
        # рекорд
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score_str = '{:,}'.format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.ai_settings.bg_color)

        # Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.top = self.screen_rect.top
        self.high_score_rect.centerx = self.screen_rect.centerx

    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color,
                                            self.ai_settings.bg_color)

        # уровень выводится под текущим счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = self.score_rect.bottom + 10
        self.level_rect.right = self.score_rect.right

    def show_score(self):
        """ Выводит счет и уровень на экран """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

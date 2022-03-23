import pygame.font


class Button():
    """ Описывает кнопку """

    def __init__(self, ai_settings, screen, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Назначение размеров и свойств кнопок
        self.width, self.height = 200, 50
        self.button_color = (148, 172, 176)
        self.text_color = (255, 204, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается один раз
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Прреобразует msg в прмоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения"""

        # рисует прямоугольную часть кнопки
        self.screen.fill(self.button_color, self.rect)
        # выводит изображение текста на экран
        self.screen.blit(self.msg_image, self.msg_image_rect)

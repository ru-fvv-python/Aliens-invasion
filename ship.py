import pygame


class Ship():
    """реализует бульшую часть поведения корабля."""

    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image_forward = pygame.image.load('images/forward.png') \
            .convert_alpha()
        self.image = self.image_forward
        file_left = 'left'
        file_right = 'right'
        self.left_images = []
        self.right_images = []
        self.speed_ship = 10
        self.flRightUp = False
        self.flLeftUp = False

        # заполение списка картинками поворота направо
        for image in range(1, 4):
            self.right_images.append(
                pygame.image.load(
                    'images/{}{}.png'.format(file_right, image)
                ).convert_alpha()
            )

        # заполение списка картинками поворота налево
        for image in range(1, 4):
            self.left_images.append(
                pygame.image.load(
                    'images/{}{}.png'.format(file_left, image)
                ).convert_alpha()
            )

        # координаты корабля
        self.rect = self.image.get_rect(
            centerx=ai_settings.screen_width // 2,
            bottom=ai_settings.screen_height - 5
        )
        # сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centerx)


    def move_left(self):
        """разворот корабля налево"""
        for image in self.left_images:
            self.image = image

    def move_from_left(self):
        """разворот корабля обратно"""
        self.left_images.reverse()
        for image in self.left_images:
            self.image = image
        self.left_images.reverse()

    def move_right(self):
        """разворот корабля направо"""
        for image in self.right_images:
            self.image = image

    def move_from_right(self):
        """разворот корабля обратно"""
        self.right_images.reverse()
        for image in self.right_images:
            self.image = image
        self.right_images.reverse()

    def update(self):
        """движение корабля"""
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.move_left()
            self.center -= self.speed_ship
            if self.center < 0:
                self.center = 0
        elif key[pygame.K_RIGHT]:
            self.move_right()
            self.center += self.speed_ship
            if self.center > self.ai_settings.screen_width - self.rect.width:
                self.center = self.ai_settings.screen_width - self.rect.width
        else:
            if self.flLeftUp:
                self.move_from_left()
                self.flLeftUp = False
            elif self.flRightUp:
                self.move_from_right()
                self.flRightUp = False

            self.image = self.image_forward

        # Обновление атрибута rect на основании self.center.
        self.rect.x = self.center

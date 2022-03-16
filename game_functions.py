import pygame

clock = pygame.time.Clock()


def update_screen(ai_settings, screen):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)


    # Отображение последнего прорисованного экрана.
    pygame.display.update()
    clock.tick(ai_settings.fps)

import pygame

from bullet import Bullet

clock = pygame.time.Clock()


def check_events(ship, bullets, ai_settings, screen):
    """Обрабатывает нажатия клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.flRightUp = True
            elif event.key == pygame.K_LEFT:
                ship.flLeftUp = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # стрельба из пушки
                fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум еще не достигнут"""
    # Создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # вызывает bullet.update() для каждой пули, включенной в группу bullets
    bullets.update()
    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, flame_r, flame_l, bullets):
    """Обновляет изображения на экране и отображает новый экран."""
    # рисуем фон экрана
    screen.fill(ai_settings.bg_color)

    # рисуем корабль
    screen.blit(ship.image, ship.rect)

    # рисуем огни двигателя
    screen.blit(flame_r.image, flame_r.rect)
    screen.blit(flame_l.image, flame_l.rect)

    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Отображение последнего прорисованного экрана с заданным FPS
    pygame.display.update()
    clock.tick(ai_settings.fps)

    # движение корабля
    ship.update()
    flame_r.update()
    flame_l.update()

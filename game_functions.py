import pygame

from alien import Alien
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


def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду."""
    # свободное пространсво - три пришельца
    available_space_x = ai_settings.screen_width - alien_width * 2
    #  количество пришельцев с промежутком в два пришельца
    number_aliens_x = int(available_space_x / (alien_width * 3))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количество рядов, помещающихся на экране."""
    # доступное вертикальное пространство =
    # вычитая высоту пришельца (сверху), высоту корабля (снизу)
    # и высоту пришельца * 2 (снизу)
    available_space_y = (ai_settings.screen_height - alien_height * 2 -
                         ship_height)

    # количество строк = свободное пространство / на высоту пришельца *2
    number_rows = int(available_space_y / (alien_height * 2))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    # расположение по горизонтали
    # интервал между соседними пришельцами равен 3 ширине пришельца
    alien.x = 3 * alien_width * alien_number
    alien.rect.x = alien.x

    # по вертикали
    # интервал между соседними пришельцами равен 2 высоте пришельца
    alien.rect.y = 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев."""
    # Создание пришельца и вычисление количества пришельцев в ряду.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # Создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Опускает весь флот и меняет направление флота."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.fleet_direction *= -1


def updates_aliens(ai_settings, aliens):
    """
    Проверяет, достиг ли флот края экрана,
    после чего обновляет позиции всех пришельцев во флоте.
    """
    # вызывает alien.update() для каждого чужого из группы aliens
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def update_screen(ai_settings, screen, ship, flame_r, flame_l, bullets,
                  aliens):
    """Обновляет изображения на экране и отображает новый экран."""
    # рисуем фон экрана
    screen.fill(ai_settings.bg_color)

    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # рисуем корабль
    screen.blit(ship.image, ship.rect)

    # рисуем огни двигателя
    screen.blit(flame_r.image, flame_r.rect)
    screen.blit(flame_l.image, flame_l.rect)

    # вывод пришельцев
    aliens.draw(screen)

    # Отображение последнего прорисованного экрана с заданным FPS
    pygame.display.update()
    clock.tick(ai_settings.fps)

    # движение корабля
    ship.update()
    flame_r.update()
    flame_l.update()

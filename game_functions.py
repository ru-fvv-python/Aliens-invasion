from random import randint
from time import sleep

import pygame
import json

from alien import Alien
from bullet import Bullet
from explosion import Explosion
from star import Star

clock = pygame.time.Clock()


def save_record(new_record):
    """сохраняет рекорд в файл"""
    filename = 'highrecord.json'
    with open(filename, 'w') as f_obj:
        json.dump(new_record, f_obj)


def chec_record(stats) -> int:
    """сравнивает рекорд в файле с текущим
    и возвращает наибольшее"""
    filename = 'highrecord.json'
    try:
        with open(filename, 'r') as f_obj:
            high_score_old = json.load(f_obj)
    except FileNotFoundError:
        return stats.high_score
    else:
        if stats.high_score > high_score_old:
            return stats.high_score
        else:
            return high_score_old


def check_events(sb, ship, aliens, bullets, ai_settings, screen, stats,
                 play_button):
    """Обрабатывает нажатия клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            new_record = chec_record(stats)
            save_record(new_record)
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
            elif event.key == pygame.K_p and not stats.game_active:
                # запускает игру
                start_game(ai_settings, screen, stats, ship, aliens, bullets)
            elif event.key == pygame.K_q:
                new_record = chec_record(stats)
                save_record(new_record)
                exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)


def start_game(ai_settings, screen, stats, ship, aliens, bullets):
    """запускает игру"""
    # указатель мыши скрывается
    pygame.mouse.set_visible(False)

    # Сброс игровой статистики
    stats.reset_stats()
    stats.game_active = True

    # очистка списков пришельцев и пуль.
    aliens.empty()
    bullets.empty()

    # создание нового флота и размещение кораблей
    create_fleet(ai_settings, screen, ship, aliens)

    # установка после рестарта игры начальной скорости корабля
    ship.speed_ship = ai_settings.speed
    ship.center_ship()  # его центровка


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets,
                      mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        # Очистка списков пришельцев и пуль.
        aliens.empty()
        bullets.empty()

        # Сброс игровых настроек
        ai_settings.initialize_dynamic_settings()

        # Сброс игровой статистики.
        stats.reset_stats()
        stats.game_active = True

        # Подготовка исходного изображения счетов.
        sb.prep_image()

        # запускает игру
        start_game(ai_settings, screen, stats, ship, aliens, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум еще не достигнут"""
    # Создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


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
    offset_top = 100
    alien.rect.y = offset_top + 2 * alien.rect.height * row_number
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


# ----------------------------- Звезды ---------------------------------------


def get_number_stars_x(ai_settings):
    """Вычисляет количество звезд в ряду."""
    # коэффициент расстояния между звезд
    space = ai_settings.space_between_stars
    # ширина звезды
    star_width = ai_settings.star_width
    #  количество звезд с промежутком в 'space * star_width'
    total_column_stars = int(ai_settings.screen_width / (star_width * space))
    return total_column_stars


def get_number_stars_y(ai_settings):
    """Определяет количество рядов звезд, помещающихся на экране."""
    # коэффициент расстояния между звезд
    space = ai_settings.space_between_stars
    # высота звезды
    star_height = ai_settings.star_height
    #  количество звезд с промежутком в 'space * star_heigh'
    total_row_stars = int(ai_settings.screen_height / (star_height * space))
    return total_row_stars


def create_star(ai_settings, stars, column, row):
    """ создание и добавление звезды в группу stars"""
    # создание звезды
    star = Star(ai_settings)
    # площадь под звезду
    star_width = ai_settings.star_width
    star_height = ai_settings.star_height
    # интервал между соседними звездами
    space = ai_settings.space_between_stars
    # смещение по осям +-
    offset = ai_settings.offset
    # координата по оси Х
    star.rect.x = space * star_width * column + randint(-offset, offset)
    # координата по оси Y
    star.rect.y = space * star_height * row + randint(-offset, offset)
    stars.add(star)


def create_star_sky(ai_settings, stars):
    """Создает звезд на небе"""
    total_column_stars = get_number_stars_x(ai_settings)
    total_row_stars = get_number_stars_y(ai_settings)

    for row in range(total_row_stars):
        for column in range(total_column_stars):
            create_star(ai_settings, stars, column, row)


# ----------------------------- updates --------------------------------------

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Обрабатывает столкновение корабля с пришельцем."""
    # если у игрока есть дополнительныек корабли
    if stats.ship_left > 0:
        # Уменьшение ships_left.
        stats.ship_left -= 1

        # Обновление игровой информации
        sb.prep_ships()

        # Очистка списков пришельцев и пуль.
        aliens.empty()
        bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        create_fleet(ai_settings, screen, ship, aliens)
        ai_settings.fleet_direction = -1
        ship.center_ship()

        # Пауза.
        sleep(0.5)
    # если нет
    else:
        # игра не активна
        stats.game_active = False
        # отображение мыши
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Проверяет, добрались ли пришельцы до нижнего края экрана."""
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Происходит то же, что при столкновении с кораблем.
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """
    Проверяет, достиг ли флот края экрана,
    после чего обновляет позиции всех пришельцев во флоте.
    """
    check_fleet_edges(ai_settings, aliens)

    # вызывает alien.update() для каждого чужого из группы aliens
    aliens.update()

    # Проверка коллизий "пришелец-корабль".
    if pygame.sprite.spritecollideany(ship, aliens):
        # Обрабатывает столкновение корабля с пришельцем
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    # проверяет пришельцев, добравшихся до нижнего края экрана
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)


def update_stars(stars):
    """обновляет позицию звезд"""
    stars.update()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets,
                   explosions):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # вызывает bullet.update() для каждой пули, включенной в группу bullets
    bullets.update()
    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Обработка коллизий пуль с пришельцами.
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,
                                  bullets,
                                  explosions)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,
                                  bullets,
                                  explosions):
    """Обработка коллизий пуль с пришельцами."""
    # При обнаружении попадания удалить пулю и пришельца.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for downed_aliens in collisions.values():
            # создание взрыва
            new_explosion = Explosion('sprite-explosion', 8, 6, screen,
                                      downed_aliens)
            explosions.add(new_explosion)

            # ведение счета: начисление очков за всех пришельцев из списка
            stats.score += ai_settings.alien_points * len(downed_aliens)
            # обновление изображения счета
            sb.prep_score()
            # Проверка нового рекорда
            check_high_score(stats, sb)

    if len(aliens) == 0:
        # Если весь флот уничтожен, начинается следующий уровень.
        start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets)


def start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """начинает следующий уровень."""
    # Уничтожение пуль
    bullets.empty()
    # повышение скорости
    ai_settings.increase_speed()
    ship.speed_ship = ai_settings.speed
    # создание нового флота
    create_fleet(ai_settings, screen, ship, aliens)
    ai_settings.fleet_direction = -1
    # Увеличение уровня
    stats.level += 1
    sb.prep_level()


def check_high_score(stats, sb):
    """Проверка нового рекорда"""
    if stats.high_score < stats.score:
        stats.high_score = stats.score
        # обновление изображения рекорда
        sb.prep_high_score()


def update_explosions(explosions):
    """обновляет взрывы"""
    explosions.update()


def update_screen(ai_settings, screen, stats, sb, ship, flame_r, flame_l,
                  bullets,
                  aliens, stars, explosion, play_button):
    """Обновляет изображения на экране и отображает новый экран."""
    # рисуем фон экрана
    screen.fill(ai_settings.bg_color)

    # рисуем звезды
    stars.draw(screen)

    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # рисуем корабль
    screen.blit(ship.image, ship.rect)

    # анимация взрыва
    explosion.update()

    # рисуем огни двигателя
    screen.blit(flame_r.image, flame_r.rect)
    screen.blit(flame_l.image, flame_l.rect)

    # вывод пришельцев
    aliens.draw(screen)

    # вывод счета
    sb.show_score()

    # Кнопка Play отображается в том случае, если игра не активна
    if not stats.game_active:
        play_button.draw_button()

    # Отображение последнего прорисованного экрана с заданным FPS
    pygame.display.update()
    clock.tick(ai_settings.fps)

    # движение корабля
    ship.update()
    flame_r.update()
    flame_l.update()

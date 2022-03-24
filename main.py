import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from jet_flame import JetFlame
from settings import Settings
from ship import Ship


def run():
    pygame.init()

    ai_set = Settings()

    sc = pygame.display.set_mode((
        ai_set.screen_width,
        ai_set.screen_height), pygame.FULLSCREEN)

    pygame.display.set_caption('Aliens invasion')
    pygame.display.set_icon(
        pygame.image.load('images/icon_app.png').convert_alpha())

    # Создание кнопки Play
    play_button = Button(ai_set, sc, 'Play')

    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_set)

    # корабль
    ship = Ship(ai_set, sc)
    # огони двигателя: правый и левый
    flame_r = JetFlame(ship, ai_set.offset_jet, ai_set.zoom)
    flame_l = JetFlame(ship, -ai_set.offset_jet, ai_set.zoom)

    # создание группы звезд
    stars = Group()
    # Создание группы для хранения пуль.
    bullets = Group()

    # создание группы для взрывов
    explosions = Group()

    # Создание группы пришельцев
    aliens = Group()

    # создание звездного неба
    gf.create_star_sky(ai_set, stars)

    # Создание флота пришельцев.
    gf.create_fleet(ai_set, sc, ship, aliens)

    while True:
        # отслеживание нажатия клавиш
        gf.check_events(ship, aliens, bullets, ai_set, sc, stats, play_button)

        if stats.game_active:
            # обновление неба
            gf.update_stars(stars)

            # Обновляет позиции пуль и уничтожает старые пули.
            gf.update_bullets(ai_set, sc, ship, aliens, bullets, explosions)

            # Обновляет позицию пришельцев
            gf.update_aliens(ai_set, stats, sc, ship, aliens, bullets)

            # обновляет взрывы
            gf.update_explosions(explosions)

            gf.update_aliens(ai_set, stats, sc, ship, aliens, bullets)

        # Обновляет изображения на экране и отображает новый экран.
        gf.update_screen(ai_set, sc, stats, ship, flame_r, flame_l, bullets,
                         aliens, stars, explosions, play_button)


run()

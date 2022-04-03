import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from jet_flame import JetFlame
from scoreboard import Scoreboard
from settings import Settings
from shild import Shild
from ship import Ship


def run():
    # важно прописать до pygame.init()
    pygame.mixer.pre_init(44100, -16, 1, 512)

    pygame.init()

    ai_set = Settings()

    sc = pygame.display.set_mode((
        ai_set.screen_width,
        ai_set.screen_height), pygame.FULLSCREEN)

    pygame.display.set_caption('Aliens invasion')
    pygame.display.set_icon(
        pygame.image.load('images/icon_app.png').convert_alpha())

    # звуки
    # фоновая музыка
    pygame.mixer.music.load('sounds/space_music.mp3')
    pygame.mixer.music.play(-1)

    # звук выстрела из пушки
    s_cannon = pygame.mixer.Sound('sounds/cannon.wav')
    s_laser = pygame.mixer.Sound('sounds/laser.wav')

    # звук взрыва
    s_explosion = pygame.mixer.Sound('sounds/explosion.mp3')

    # Создание кнопки Play
    play_button = Button(ai_set, sc, 'Play')

    # Создание экземпляра для хранения игровой статистики и счета.
    stats = GameStats(ai_set)
    sb = Scoreboard(ai_set, sc, stats)

    # корабль
    ship = Ship(ai_set, sc, 1)
    # огони двигателя: правый и левый
    flame_r = JetFlame(ship, ai_set.offset_jet, ai_set.zoom)
    flame_l = JetFlame(ship, -ai_set.offset_jet, ai_set.zoom)
    # щит
    shild = Shild(ai_set, sc, ship)

    # создание группы звезд
    stars = Group()
    # Создание группы для хранения пуль.
    bullets = Group()
    # Создание группы для хранения пуль пришельцев.
    bullets_alien = Group()

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
        gf.check_events(sb, ship, aliens, bullets, ai_set, sc, stats,
                        play_button, s_cannon)

        if stats.game_active:
            # обновление неба
            gf.update_stars(stars)

            # Обновляет позиции пуль и уничтожает старые пули.
            gf.update_bullets(ai_set, sc, stats, sb, ship, aliens, bullets,
                              explosions, s_explosion)

            # Обновляет позицию пришельцев
            gf.update_aliens(ai_set, stats, sc, sb, ship, aliens, bullets,
                             explosions, s_explosion)

            # выстрел пришельца
            gf.create_bullet_alien(ai_set, sc, aliens, bullets_alien, s_laser)
            # Обновляет позиции пуль пришельцев
            gf.update_bullets_aliens(sc, bullets_alien, ship, shild,
                                     explosions, s_explosion)

            # обновляет взрывы
            gf.update_explosions(explosions)

        # Обновляет изображения на экране и отображает новый экран.
        gf.update_screen(ai_set, sc, stats, sb, ship, flame_r, flame_l, shild,
                         bullets, bullets_alien, aliens, stars, explosions,
                         play_button)


run()

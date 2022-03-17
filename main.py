import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from jet_flame import JetFlame

def run():
    pygame.init()

    ai_set = Settings()

    sc = pygame.display.set_mode((
        ai_set.screen_width,
        ai_set.screen_height))

    pygame.display.set_caption('Aliens invasion')
    pygame.display.set_icon(
        pygame.image.load('images/icon_app.png').convert_alpha())

    # корабль
    ship = Ship(ai_set)
    # огони двигателя: правый и левый
    flame_r = JetFlame(ship, ai_set.offset, ai_set.zoom)
    flame_l = JetFlame(ship, -ai_set.offset, ai_set.zoom)

    while True:
        # отслеживание нажатия клавиш
        gf.check_events(ship)

        # Обновляет изображения на экране и отображает новый экран.
        gf.update_screen(ai_set, sc, ship, flame_r, flame_l)


run()

import pygame

# размеры окна
WIDTH, HEIGHT = 1200, 800
bg_color = (15, 15, 100)

# число кадров в секунду
clock = pygame.time.Clock()
FPS = 60


sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Aliens invasion')
pygame.display.set_icon(
    pygame.image.load('images/icon_app.png').convert_alpha())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(bg_color)
    pygame.display.update()
    clock.tick(FPS)




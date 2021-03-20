import pygame

SCREE_WIDTH = 800
SCREE_HEIGTH = 600
MC_DEFAULT_POSITION_X = 400
MC_DEFAULT_POSITION_Y = 450
MC_CURRENT_POSITION_X = 400
MC_CURRENT_POSITION_Y = 450
SCREEN_ICON = "images/icon.png"
MAIN_CHARACTER_ICON = "images/icon.png"

def setup_screen():
    screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGTH))
    icon = pygame.image.load(SCREEN_ICON)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Dick Invaders")

    return screen

def update_player(screen):
    screen.blit(player, (MC_CURRENT_POSITION_X, MC_CURRENT_POSITION_Y))

player = pygame.image.load(MAIN_CHARACTER_ICON)

pygame.init()
screen = setup_screen()

run = True
while run:
    screen.fill((255,27,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"YAY event {event}")
            run = False
    update_player(screen)
    pygame.display.update()

import pygame
import random

# Main screen constants
SCREEN_ICON = "images/tortoise.png"
SCREEN_BACKGROUND = "images/ocean.png"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_LEFT_BOUNDARY = 5
SCREEN_RIGHT_BOUNDARY = 729
SCREEN_TOP_BOUNDARY = 5
SCREEN_BOTTOM_BOUNDARY = 529
SCREEN_ENEMY_BOTTOM_BOUNDARY = 250
SCREEN_PLAYER_TOP_BOUNDARY = 250

# Main character (PLAYER) constants
PLAYER_IMAGE = "images/tortoise.png"
PLAYER_DEFAULT_POSITION_X = 370
PLAYER_DEFAULT_POSITION_Y = 450

# Bullet constants
BULLET_IMAGE = "images/crab.png"
BULLET_STATE_READY = "bullet_ready"
BULLET_STATE_RELOADING = "bullet_reloading"

# Enemy constants
ENEMY_01_IMAGE = "images/plastic_bag.png"
ENEMY_02_IMAGE = "images/plastic_bottle.png"
ENEMY_03_IMAGE = "images/straw_01.png"
ENEMY_04_IMAGE = "images/straw_02.png"


def setup_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    icon = pygame.image.load(SCREEN_ICON)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Sea Invaders")
    return screen


def update_player(x, y):
    """ Update position of player image on main screen """
    MAIN_SCREEN.blit(PLAYER, (x, y))


def update_enemy(x, y):
    """ Update position of enemy image on main screen """
    MAIN_SCREEN.blit(ENEMY, (x, y))


def fire_bullet(x, y):
    """ Fire a crab at those damn invaders """
    global BULLET_STATE
    BULLET_STATE = BULLET_STATE_RELOADING
    # TODO fix offset of crab leaving turtle
    MAIN_SCREEN.blit(BULLET, (x, y))


def reload_bullet():
    """ Reset bullet position and state so player can shoot it again """
    global BULLET_STATE
    global BULLET_POSITION_Y
    BULLET_STATE = BULLET_STATE_READY
    BULLET_POSITION_Y = PLAYER_DEFAULT_POSITION_Y


pygame.init()

# Main screen
MAIN_BACKGROUND = pygame.image.load(SCREEN_BACKGROUND)
MAIN_BACKGROUND = pygame.transform.scale(MAIN_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
MAIN_SCREEN = setup_screen()

# Main character (player)
PLAYER = pygame.image.load(PLAYER_IMAGE)
PLAYER_POSITION_X = PLAYER_DEFAULT_POSITION_X
PLAYER_POSITION_Y = PLAYER_DEFAULT_POSITION_Y
PLAYER_POSITION_X_CHANGE = 0

# Bullet (crab lol)
BULLET = pygame.image.load(BULLET_IMAGE)
BULLET_STATE = BULLET_STATE_READY
BULLET_POSITION_X = 0
BULLET_POSITION_Y = PLAYER_DEFAULT_POSITION_Y
BULLET_POSITION_X_CHANGE = 0
BULLET_POSITION_Y_CHANGE = 0.4

# Enemy
ENEMY = pygame.image.load(ENEMY_04_IMAGE)
ENEMY_POSITION_X = random.randint(SCREEN_LEFT_BOUNDARY, SCREEN_RIGHT_BOUNDARY)
ENEMY_POSITION_Y = random.randint(SCREEN_TOP_BOUNDARY, SCREEN_ENEMY_BOTTOM_BOUNDARY)
ENEMY_POSITION_X_CHANGE = 0.1
ENEMY_POSITION_Y_CHANGE = 40

run = True
while run:
    MAIN_SCREEN.fill((0,105,148))
    MAIN_SCREEN.blit(MAIN_BACKGROUND, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Move PLAYER
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER_POSITION_X_CHANGE = -0.2
            if event.key == pygame.K_RIGHT:
                PLAYER_POSITION_X_CHANGE = 0.2
            if event.key == pygame.K_SPACE and BULLET_STATE is BULLET_STATE_READY:
                BULLET_POSITION_X = PLAYER_POSITION_X
                fire_bullet(PLAYER_POSITION_X, BULLET_POSITION_Y)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                PLAYER_POSITION_X_CHANGE = 0

    PLAYER_POSITION_X += PLAYER_POSITION_X_CHANGE

    # Fix player boundaries
    if PLAYER_POSITION_X < SCREEN_LEFT_BOUNDARY:
        PLAYER_POSITION_X = SCREEN_LEFT_BOUNDARY
    if PLAYER_POSITION_X > SCREEN_RIGHT_BOUNDARY:
        PLAYER_POSITION_X = SCREEN_RIGHT_BOUNDARY
    if PLAYER_POSITION_Y < SCREEN_PLAYER_TOP_BOUNDARY:
        PLAYER_POSITION_Y = SCREEN_PLAYER_TOP_BOUNDARY
    if PLAYER_POSITION_Y > SCREEN_BOTTOM_BOUNDARY:
        PLAYER_POSITION_Y = SCREEN_BOTTOM_BOUNDARY

    # Move enemy
    ENEMY_POSITION_X += ENEMY_POSITION_X_CHANGE
    if ENEMY_POSITION_X > SCREEN_RIGHT_BOUNDARY:
        ENEMY_POSITION_X_CHANGE = -ENEMY_POSITION_X_CHANGE
        ENEMY_POSITION_X = SCREEN_RIGHT_BOUNDARY
        ENEMY_POSITION_Y += ENEMY_POSITION_Y_CHANGE
    if ENEMY_POSITION_X < SCREEN_LEFT_BOUNDARY:
        ENEMY_POSITION_X_CHANGE = -ENEMY_POSITION_X_CHANGE
        ENEMY_POSITION_X = SCREEN_LEFT_BOUNDARY
        ENEMY_POSITION_Y += ENEMY_POSITION_Y_CHANGE

    # Crab movement
    if BULLET_STATE is BULLET_STATE_RELOADING:
        fire_bullet(BULLET_POSITION_X, BULLET_POSITION_Y)
        BULLET_POSITION_Y -= BULLET_POSITION_Y_CHANGE
        if BULLET_POSITION_Y < SCREEN_TOP_BOUNDARY:
            reload_bullet()



    update_player(PLAYER_POSITION_X, PLAYER_POSITION_Y)
    update_enemy(ENEMY_POSITION_X, ENEMY_POSITION_Y)
    pygame.display.update()

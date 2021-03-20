import math
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

# Collision constants
COLLISION_DISTANCE = 35


def setup_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    icon = pygame.image.load(SCREEN_ICON)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Sea Invaders")
    return screen


def generate_enemy():
    """ Place enemy in a new location and choose a new random skin for it """
    enemy_skin = random.choice(
        [ENEMY_01_IMAGE, ENEMY_02_IMAGE, ENEMY_03_IMAGE, ENEMY_04_IMAGE]
    )

    global ENEMY
    global ENEMY_POSITION_X
    global ENEMY_POSITION_Y
    ENEMY = pygame.image.load(enemy_skin)
    ENEMY_POSITION_X = random.randint(SCREEN_LEFT_BOUNDARY, SCREEN_RIGHT_BOUNDARY)
    ENEMY_POSITION_Y = random.randint(SCREEN_TOP_BOUNDARY, SCREEN_ENEMY_BOTTOM_BOUNDARY)


def update_player(x, y):
    """ Update position of player image on main screen """
    MAIN_SCREEN.blit(PLAYER, (x, y))


def fix_player_bounds():
    """ Fix player bounds to don't let it slip off the screen """
    global PLAYER_POSITION_X
    global PLAYER_POSITION_Y
    if PLAYER_POSITION_X < SCREEN_LEFT_BOUNDARY:
        PLAYER_POSITION_X = SCREEN_LEFT_BOUNDARY
    if PLAYER_POSITION_X > SCREEN_RIGHT_BOUNDARY:
        PLAYER_POSITION_X = SCREEN_RIGHT_BOUNDARY
    if PLAYER_POSITION_Y < SCREEN_PLAYER_TOP_BOUNDARY:
        PLAYER_POSITION_Y = SCREEN_PLAYER_TOP_BOUNDARY
    if PLAYER_POSITION_Y > SCREEN_BOTTOM_BOUNDARY:
        PLAYER_POSITION_Y = SCREEN_BOTTOM_BOUNDARY


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


def objects_collide(object_A_X, object_A_Y, object_B_X, object_B_Y):
    """ Calculate the collision between two given objects """
    X_difference = object_A_X - object_B_X
    Y_difference = object_A_Y - object_B_Y
    distance = math.sqrt(math.pow(X_difference, 2) + math.pow(Y_difference, 2))
    if distance < COLLISION_DISTANCE:
        return True
    return False


pygame.init()
print("=> Welcome to SEA INVADERS! You better hit these bastards with that crab!")

# Main screen
MAIN_BACKGROUND = pygame.image.load(SCREEN_BACKGROUND)
MAIN_BACKGROUND = pygame.transform.scale(MAIN_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
MAIN_SCREEN = setup_screen()

# Main character (player)
PLAYER = pygame.image.load(PLAYER_IMAGE)
PLAYER_SCORE = 0
PLAYER_POSITION_X = PLAYER_DEFAULT_POSITION_X
PLAYER_POSITION_Y = PLAYER_DEFAULT_POSITION_Y
PLAYER_POSITION_X_CHANGE = 0
PLAYER_POSITION_Y_CHANGE = 0
PLAYER_POSITION_X_PACE = 5

# Bullet (crab lol)
BULLET = pygame.image.load(BULLET_IMAGE)
BULLET_STATE = BULLET_STATE_READY
BULLET_POSITION_X = 0
BULLET_POSITION_Y = PLAYER_DEFAULT_POSITION_Y
BULLET_POSITION_X_CHANGE = 0
BULLET_POSITION_Y_CHANGE = 7

# Enemy
ENEMY = None
ENEMY_POSITION_X = None
ENEMY_POSITION_Y = None
ENEMY_POSITION_X_PACE = 1
ENEMY_POSITION_Y_PACE = 40
generate_enemy()

run = True
while run:
    MAIN_SCREEN.fill((0,105,148))
    MAIN_SCREEN.blit(MAIN_BACKGROUND, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"=> Hope I can see you soon. Your score was {PLAYER_SCORE}!")
            run = False

        # Move PLAYER
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PLAYER_POSITION_X_CHANGE = -PLAYER_POSITION_X_PACE
            if event.key == pygame.K_RIGHT:
                PLAYER_POSITION_X_CHANGE = PLAYER_POSITION_X_PACE
            if event.key == pygame.K_SPACE and BULLET_STATE is BULLET_STATE_READY:
                BULLET_POSITION_X = PLAYER_POSITION_X
                fire_bullet(PLAYER_POSITION_X, BULLET_POSITION_Y)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                PLAYER_POSITION_X_CHANGE = 0

    PLAYER_POSITION_X += PLAYER_POSITION_X_CHANGE

    # Fix player boundaries
    fix_player_bounds()

    # Move enemy
    ENEMY_POSITION_X += ENEMY_POSITION_X_PACE
    if ENEMY_POSITION_X > SCREEN_RIGHT_BOUNDARY:
        ENEMY_POSITION_X_PACE = -ENEMY_POSITION_X_PACE
        ENEMY_POSITION_X = SCREEN_RIGHT_BOUNDARY
        ENEMY_POSITION_Y += ENEMY_POSITION_Y_PACE
    if ENEMY_POSITION_X < SCREEN_LEFT_BOUNDARY:
        ENEMY_POSITION_X_PACE = -ENEMY_POSITION_X_PACE
        ENEMY_POSITION_X = SCREEN_LEFT_BOUNDARY
        ENEMY_POSITION_Y += ENEMY_POSITION_Y_PACE

    # Crab movement
    if BULLET_STATE is BULLET_STATE_RELOADING:
        fire_bullet(BULLET_POSITION_X, BULLET_POSITION_Y)
        BULLET_POSITION_Y -= BULLET_POSITION_Y_CHANGE
        if BULLET_POSITION_Y < SCREEN_TOP_BOUNDARY:
            reload_bullet()

    # Collision check
    collision = objects_collide(
        ENEMY_POSITION_X, ENEMY_POSITION_Y, BULLET_POSITION_X, BULLET_POSITION_Y
    )
    if collision:
        reload_bullet()
        PLAYER_SCORE += 1
        print(f"=> Hit! Your score is {PLAYER_SCORE}")
        generate_enemy()


    update_player(PLAYER_POSITION_X, PLAYER_POSITION_Y)
    update_enemy(ENEMY_POSITION_X, ENEMY_POSITION_Y)
    pygame.display.update()

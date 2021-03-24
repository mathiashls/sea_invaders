import math
import pygame
import random

from screen_items import characters

# Main screen constants
SCREEN_ICON = "images/tortoise.png"
SCREEN_BACKGROUND = "images/ocean.png"
SCREEN_WIDTH = 1270
SCREEN_HEIGHT = 720
SCREEN_LEFT_BOUNDARY = round(SCREEN_WIDTH * (5/100))
SCREEN_RIGHT_BOUNDARY = SCREEN_WIDTH - SCREEN_LEFT_BOUNDARY
SCREEN_TOP_BOUNDARY = round(SCREEN_HEIGHT * (5/100))
SCREEN_BOTTOM_BOUNDARY = SCREEN_WIDTH - SCREEN_TOP_BOUNDARY

PLAYER_SPAWN_X = round(SCREEN_WIDTH / 2)
PLAYER_SPAWN_Y = round(SCREEN_HEIGHT - (SCREEN_HEIGHT * (20/100)))
PLAYER_PACE_X = 10
PLAYER_PACE_Y = 0

ENEMIES_NUMBER = 3
ENEMIES_PACE_X = 1
ENEMIES_PACE_Y = 40

PLAYER_BOUNDARY = {
    "left": SCREEN_LEFT_BOUNDARY,
    "right": SCREEN_RIGHT_BOUNDARY,
    "top": SCREEN_TOP_BOUNDARY,
    "bottom": SCREEN_BOTTOM_BOUNDARY
}

ENEMY_BOUNDARY = {
    "left": SCREEN_LEFT_BOUNDARY,
    "right": SCREEN_RIGHT_BOUNDARY,
    "top": SCREEN_TOP_BOUNDARY,
    "bottom": round(SCREEN_HEIGHT - (SCREEN_HEIGHT * (40/100)))
}


def setup_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    icon = pygame.image.load(SCREEN_ICON)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Sea Invaders")
    return screen


pygame.init()
main_loop = True
stage_loop = True
game_over_loop = True
print("=> Welcome to SEA INVADERS! You better hit these bastards with that crab!")

# Main screen
MAIN_BACKGROUND = pygame.image.load(SCREEN_BACKGROUND)
MAIN_BACKGROUND = pygame.transform.scale(MAIN_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
MAIN_SCREEN = setup_screen()

# Music
# pygame.mixer.music.load('background.wav')
# pygame.mixer.music.play(-1)

# Score
SCORE_FONT = pygame.font.Font('fonts/beach_type.ttf', 32)
SCORE_X = SCREEN_WIDTH * (5/100)
SCORE_Y = SCREEN_HEIGHT * (5/100)

def exit_game():
    # print(f"=> Hope I can see you soon. Your score was {PLAYER_SCORE}!")
    global main_loop
    global stage_loop
    global game_over_loop
    main_loop = False
    stage_loop = False
    game_over_loop = False

def main_menu():
    title_font = pygame.font.Font('fonts/beach_type.ttf', 128)
    press_space_font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 24)
    while main_loop:
        MAIN_SCREEN.fill((0,105,148))
        MAIN_SCREEN.blit(MAIN_BACKGROUND, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    stage_one()

        title = title_font.render(f"Sea Invaders", True, (255, 255, 51))
        title_rect = title.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - (SCREEN_HEIGHT/1.7))
        )
        MAIN_SCREEN.blit(title, title_rect)

        press_space = press_space_font.render(f"Press SPACE to start!", True, (255, 255, 255))
        press_space_rect = press_space.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - (SCREEN_HEIGHT/2.3))
        )
        MAIN_SCREEN.blit(press_space, press_space_rect)

        pygame.display.update()


def stage_one():
    def generate_enemy():
        enemy_pace_x = ENEMIES_PACE_X  + (2 * (player.score + 100)/100)
        position_x = random.choice(
            range(ENEMY_BOUNDARY["left"], ENEMY_BOUNDARY["right"])
        )
        position_y = random.choice(
            range(ENEMY_BOUNDARY["top"], ENEMY_BOUNDARY["bottom"])
        )
        enemy = characters.Enemy(MAIN_SCREEN, ENEMY_BOUNDARY, position_x, position_y, enemy_pace_x, ENEMIES_PACE_Y)
        return enemy

    player = characters.Player(
        MAIN_SCREEN, PLAYER_BOUNDARY, PLAYER_SPAWN_X, PLAYER_SPAWN_Y, PLAYER_PACE_X, PLAYER_PACE_Y
    )
    player_change_x = 0

    enemies = []
    for i in range(ENEMIES_NUMBER):
        new_enemy = generate_enemy()
        enemies.append(new_enemy)

    while stage_loop:
        MAIN_SCREEN.blit(MAIN_BACKGROUND, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            # Capture player movement controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_change_x = -player.pace_x
                if event.key == pygame.K_RIGHT:
                    player_change_x = player.pace_x
                # if event.key == pygame.K_SPACE and BULLET_STATE is BULLET_STATE_READY:
                    # bullet_sound = pygame.mixer.Sound('bullet.wav')
                    # bullet_sound.play()
                    # BULLET_POSITION_X = PLAYER_POSITION_X
                    # fire_bullet(PLAYER_POSITION_X, BULLET_POSITION_Y)
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    player_change_x = 0

        player.move(player_change_x, 0)
        player.render()
        for enemy in enemies:
            enemy.move()
            enemy.render()
        pygame.display.update()


def game_over():
    while game_over_loop:
        MAIN_SCREEN.fill((0,105,148))
        MAIN_SCREEN.blit(MAIN_BACKGROUND, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()

import math
import pygame
import random

# Main screen constants
SCREEN_ICON = "images/tortoise.png"
SCREEN_BACKGROUND = "images/ocean.png"
SCREEN_WIDTH = 1270
SCREEN_HEIGHT = 720
SCREEN_LEFT_BOUNDARY = SCREEN_WIDTH * (5/100)
SCREEN_RIGHT_BOUNDARY = SCREEN_WIDTH - SCREEN_LEFT_BOUNDARY
SCREEN_TOP_BOUNDARY = SCREEN_HEIGHT * (5/100)
SCREEN_BOTTOM_BOUNDARY = SCREEN_WIDTH - SCREEN_TOP_BOUNDARY

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
    "bottom": SCREEN_HEIGHT - (SCREEN_HEIGHT * (15/100))
}


def setup_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    icon = pygame.image.load(SCREEN_ICON)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Sea Invaders")
    return screen


pygame.init()
game_alive = True
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
    print(f"=> Hope I can see you soon. Your score was {PLAYER_SCORE}!")
    global game_alive
    game_alive = False

def main_menu():
    title_font = pygame.font.Font('fonts/beach_type.ttf', 128)
    press_space_font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 24)
    while game_alive:
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
    run = True
    while run:
        MAIN_SCREEN.fill((0,105,148))
        MAIN_SCREEN.blit(MAIN_BACKGROUND, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        pygame.display.update()


def game_over():
    run = True
    while run:
        MAIN_SCREEN.fill((0,105,148))
        MAIN_SCREEN.blit(MAIN_BACKGROUND, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()

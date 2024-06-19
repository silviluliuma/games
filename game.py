import pygame
import sys
import random

# INITIAL SETUP
WIDTH = 800
HEIGHT = 600
player_color = (255, 0, 0)
screen_color = (0, 0, 0)
enemies_color = (0, 0, 255)

player_size = [45, 45]
player_position = [(WIDTH / 2), HEIGHT - (player_size[0] * 2)]

enemy_size = [50, 50]
enemy_positions = [[random.randint(0, WIDTH - enemy_size[0]), 0] for _ in range(5)]

# Game window
window = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False
clock = pygame.time.Clock()

# Fonts
pygame.font.init()
font = pygame.font.SysFont("monospace", 35)

# Functions

def death(player_position, enemy_position):
    px = player_position[0]
    py = player_position[1]
    ex = enemy_position[0]
    ey = enemy_position[1]

    if (ex >= px and ex < (px + player_size[0])) or (px >= ex and px < (ex + enemy_size[0])):
        if (ey >= py and ey < (py + player_size[0])) or (py >= ey and py < (ey + enemy_size[0])):
            return True
    return False

def show_message(message, font, color, position):
    label = font.render(message, True, color)
    window.blit(label, position)

def restart_game():
    global player_position, enemy_positions, game_over
    player_position = [(WIDTH / 2), HEIGHT - (player_size[0] * 2)]
    enemy_positions = [[random.randint(0, WIDTH - enemy_size[0]), 0] for _ in range(5)]
    game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    restart_game()
            else:
                x = player_position[0]
                if event.key == pygame.K_LEFT:
                    x -= player_size[0]
                if event.key == pygame.K_RIGHT:
                    x += player_size[0]
                player_position[0] = x

    if not game_over:
        window.fill(screen_color)

        for enemy_position in enemy_positions:
            if enemy_position[1] >= 0 and enemy_position[1] < HEIGHT:
                enemy_position[1] += 20
            else:
                enemy_position[0] = random.randint(0, WIDTH - enemy_size[0])
                enemy_position[1] = 0

            # Losing the game
            if death(player_position, enemy_position):
                game_over = True

            # Drawing enemies
            pygame.draw.rect(window, enemies_color, (enemy_position[0], enemy_position[1], enemy_size[0], enemy_size[1]))

        # Drawing player
        pygame.draw.rect(window, player_color, (player_position[0], player_position[1], player_size[0], player_size[1]))
    else:
        show_message("Oh, Carlos... :(", font, (255, 255, 255), (WIDTH / 2 - 100, HEIGHT / 2 - 50))
        show_message("Press R to Replay", font, (255, 255, 255), (WIDTH / 2 - 150, HEIGHT / 2))

    # Speed
    clock.tick(25)

    # Update
    pygame.display.update()

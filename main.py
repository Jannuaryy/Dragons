import pygame
import sys
import random

pygame.init()

width, height = 500, 500
FPS = 20

light_gray = (211, 211, 211)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

size = 20

player1_x = 500
player1_y = 500

player2_x = 0
player2_y = 0

num_food = 10
fruits = []

fruits_player1 = 0
fruits_player2 = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дракончики")

countdown = 60
running_timer = False


def generate_food(num_food):
    food_positions = []
    while len(food_positions) < num_food:
        foodx = round(random.randrange(0, width - size) / size) * size
        foody = round(random.randrange(0, height - size) / size) * size
        if (foodx, foody) not in food_positions:
            food_positions.append((foodx, foody))
    return food_positions


def draw_grid():
    for x in range(0, width, size):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, size):
        pygame.draw.line(screen, black, (0, y), (width, y))


fruits = generate_food(num_food)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not running_timer:
            running_timer = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player1_x -= size
    if keys[pygame.K_RIGHT]:
        player1_x += size
    if keys[pygame.K_UP]:
        player1_y -= size
    if keys[pygame.K_DOWN]:
        player1_y += size

    if keys[pygame.K_a]:
        player2_x -= size
    if keys[pygame.K_d]:
        player2_x += size
    if keys[pygame.K_w]:
        player2_y -= size
    if keys[pygame.K_s]:
        player2_y += size

    player1_x = max(0, min(width - size, player1_x))
    player1_y = max(0, min(height - size, player1_y))
    player2_x = max(0, min(width - size, player2_x))
    player2_y = max(0, min(height - size, player2_y))

    if (player1_x, player1_y) in fruits:
        fruits.remove((player1_x, player1_y))
        fruits_player1 += 1

    if (player2_x, player2_y) in fruits:
        fruits.remove((player2_x, player2_y))
        fruits_player2 += 1

    if len(fruits) < num_food:
        new_foods_needed = num_food - len(fruits)
        new_foods = generate_food(new_foods_needed)
        fruits.extend(new_foods)

    if running_timer:
        countdown -= 1 / FPS
        if countdown <= 0:
            running = False

    screen.fill(light_gray)

    draw_grid()

    for foodx, foody in fruits:
        pygame.draw.rect(screen, green, [foodx, foody, size, size])

    pygame.draw.rect(screen, blue, (player1_x, player1_y, size, size))
    pygame.draw.rect(screen, red, (player2_x, player2_y, size, size))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

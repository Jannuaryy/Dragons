import pygame
import sys
import random
import start_screen
from config import *

pygame.init()
start_screen.start_screen()

light_gray = (211, 211, 211)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

player1_x = 500
player1_y = 500

player2_x = 0
player2_y = 0

num_food = 10
fruits = []

fruits_player1 = 0
fruits_player2 = 0

screen = pygame.display.set_mode((dragons_screen_width, dragons_screen_height))
pygame.display.set_caption("Дракончики")

countdown = 60
running_timer = False


def generate_food(num_food):
    food_positions = []
    while len(food_positions) < num_food:
        foodx = round(random.randrange(0 + border_thickness, dragons_screen_width - size_of_field - border_thickness) / size_of_field) * size_of_field
        foody = round(random.randrange(0 + border_thickness, dragons_screen_height - size_of_field - border_thickness) / size_of_field) * size_of_field
        if (foodx, foody) not in food_positions:
            food_positions.append((foodx, foody))
    return food_positions


def draw_grid():
    for x in range(0, dragons_screen_width, size_of_field):
        pygame.draw.line(screen, black, (x, 0), (x, dragons_screen_height))
    for y in range(0, dragons_screen_height, size_of_field):
        pygame.draw.line(screen, black, (0, y), (dragons_screen_width, y))


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
        player1_x -= size_of_field
    if keys[pygame.K_RIGHT]:
        player1_x += size_of_field
    if keys[pygame.K_UP]:
        player1_y -= size_of_field
    if keys[pygame.K_DOWN]:
        player1_y += size_of_field

    if keys[pygame.K_a]:
        player2_x -= size_of_field
    if keys[pygame.K_d]:
        player2_x += size_of_field
    if keys[pygame.K_w]:
        player2_y -= size_of_field
    if keys[pygame.K_s]:
        player2_y += size_of_field

    player1_x = max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, player1_x))
    player1_y = max(border_thickness, min(dragons_screen_height - size_of_field - border_thickness, player1_y))
    player2_x = max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, player2_x))
    player2_y = max(border_thickness, min(dragons_screen_height - size_of_field - border_thickness, player2_y))

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
        pygame.draw.rect(screen, green, [foodx, foody, size_of_field, size_of_field])

    pygame.draw.rect(screen, blue, (player1_x, player1_y, size_of_field, size_of_field))
    pygame.draw.rect(screen, red, (player2_x, player2_y, size_of_field, size_of_field))

    pygame.draw.rect(screen, black, (0, 0, dragons_screen_width, dragons_screen_height), border_thickness)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

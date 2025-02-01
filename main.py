import pygame
import sys
import random
import start_screen, win_lose_screen
from config import *

pygame.init()
start_screen.start_screen()

fruits_player1 = 0
fruits_player2 = 0

coins_player1 = 0
coins_player2 = 0

directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']

next_cage_player1_x = player1_x
next_cage_player1_y = player1_y
next_cage_player2_x = player2_x
next_cage_player2_y = player2_y
directions_player1 = directions[0]
directions_player2 = directions[2]

bullets=[]

screen = pygame.display.set_mode((dragons_screen_width, dragons_screen_height))
pygame.display.set_caption(dragons_game_name)
running_timer = False


def generate_food(num_food):
    food_positions = []
    while len(food_positions) < num_food:
        foodx = round(random.randrange(0 + border_thickness,
                                       dragons_screen_width - size_of_field - border_thickness) / size_of_field) * size_of_field
        foody = round(random.randrange(0 + border_thickness,
                                       dragons_screen_height - size_of_field - border_thickness) / size_of_field) * size_of_field
        if (foodx, foody) not in food_positions:
            food_positions.append((foodx, foody))
    return food_positions


def generate_coin(num_coins):
    coin_positions = []
    while len(coin_positions) < num_coins:
        coinx = round(random.randrange(0 + border_thickness,
                                       dragons_screen_width - size_of_field - border_thickness) / size_of_field) * size_of_field
        coiny = round(random.randrange(0 + border_thickness,
                                       dragons_screen_width - size_of_field - border_thickness) / size_of_field) * size_of_field
        if (coinx, coiny) not in coin_positions:
            if (coinx, coiny) != (player1_x, player1_y) or (coinx, coiny) != (player2_x, player2_y):
                coin_positions.append((coinx, coiny))
    return coin_positions


def draw_grid():
    for x in range(0, dragons_screen_width, size_of_field):
        pygame.draw.line(screen, black, (x, 0), (x, dragons_screen_height))
    for y in range(0, dragons_screen_height, size_of_field):
        pygame.draw.line(screen, black, (0, y), (dragons_screen_width, y))


fruits = generate_food(num_food)

coins = generate_coin(num_coins)

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
        directions_player1 = directions[directions.index(directions_player1) - 1]
    if keys[pygame.K_RIGHT]:
        directions_player1 = directions[directions.index(directions_player1) - 3]
    if keys[pygame.K_UP]:
        if directions.index(directions_player1) == 0:
            player1_y -= size_of_field
        if directions.index(directions_player1) == 1:
            player1_x += size_of_field
        if directions.index(directions_player1) == 2:
            player1_y += size_of_field
        if directions.index(directions_player1) == 3:
            player1_x -= size_of_field
    if keys[pygame.K_DOWN]:
        if directions.index(directions_player1) == 0:
            player1_y += size_of_field
        if directions.index(directions_player1) == 1:
            player1_x -= size_of_field
        if directions.index(directions_player1) == 2:
            player1_y -= size_of_field
        if directions.index(directions_player1) == 3:
            player1_x += size_of_field
    def space():
        if keys[pygame.K_SPACE]:
            for i in range(1, 6):
                bullet_player1_x=-1
                bullet_player1_y=-1
                if directions.index(directions_player1) == 0:
                    bullet_player1_x=player1_x
                    bullet_player1_y=player1_y-size_of_field*i
                if directions.index(directions_player1) == 1:
                    bullet_player1_x=player1_x+size_of_field*i
                    bullet_player1_y=player1_y
                if directions.index(directions_player1) == 2:
                    bullet_player1_x=player1_x
                    bullet_player1_y=player1_y+size_of_field*i
                if directions.index(directions_player1) == 3:
                    bullet_player1_x=player1_x-size_of_field*i
                    bullet_player1_y=player1_y
                pygame.draw.rect(screen, orange, (max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, bullet_player1_x)), max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, bullet_player1_y)), size_of_field, size_of_field))
                bullets=[bullet_player1_x,bullet_player1_y]
    if keys[pygame.K_a]:
        directions_player2 = directions[directions.index(directions_player2) - 1]
    if keys[pygame.K_d]:
        directions_player2 = directions[directions.index(directions_player2) - 3]
    if keys[pygame.K_w]:
        if directions.index(directions_player2) == 0:
            player2_y -= size_of_field
        if directions.index(directions_player2) == 1:
            player2_x += size_of_field
        if directions.index(directions_player2) == 2:
            player2_y += size_of_field
        if directions.index(directions_player2) == 3:
            player2_x -= size_of_field
    if keys[pygame.K_s]:
        if directions.index(directions_player2) == 0:
            player2_y += size_of_field
        if directions.index(directions_player2) == 1:
            player2_x -= size_of_field
        if directions.index(directions_player2) == 2:
            player2_y -= size_of_field
        if directions.index(directions_player2) == 3:
            player2_x += size_of_field

    def q():
        if keys[pygame.K_q]:
            for i in range(1, 6):
                bullet_player2_x=-1
                bullet_player2_y=-1
                if directions.index(directions_player2) == 0:
                    bullet_player2_x=player2_x
                    bullet_player2_y=player2_y-size_of_field*i
                if directions.index(directions_player2) == 1:
                    bullet_player2_x=player2_x+size_of_field*i
                    bullet_player2_y=player2_y
                if directions.index(directions_player2) == 2:
                    bullet_player2_x=player2_x
                    bullet_player2_y=player2_y+size_of_field*i
                if directions.index(directions_player2) == 3:
                    bullet_player2_x=player2_x-size_of_field*i
                    bullet_player2_y=player2_y
                pygame.draw.rect(screen, orange, (max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, bullet_player2_x)), max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, bullet_player2_y)), size_of_field, size_of_field))
                bullets=[bullet_player2_x,bullet_player2_y]

    player1_x = max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, player1_x))
    player1_y = max(border_thickness, min(dragons_screen_height - size_of_field - border_thickness, player1_y))
    player2_x = max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, player2_x))
    player2_y = max(border_thickness, min(dragons_screen_height - size_of_field - border_thickness, player2_y))
    next_cage_player2_x = player2_x
    next_cage_player2_y = player2_y
    next_cage_player1_x = player1_x
    next_cage_player1_y = player1_y

    if directions.index(directions_player1) == 0:
        next_cage_player1_y = player1_y - size_of_field
    if directions.index(directions_player1) == 1:
        next_cage_player1_x = player1_x + size_of_field
    if directions.index(directions_player1) == 2:
        next_cage_player1_y = player1_y + size_of_field
    if directions.index(directions_player1) == 3:
        next_cage_player1_x = player1_x - size_of_field

    if directions.index(directions_player2) == 0:
        next_cage_player2_y = player2_y - size_of_field
    if directions.index(directions_player2) == 1:
        next_cage_player2_x = player2_x + size_of_field
    if directions.index(directions_player2) == 2:
        next_cage_player2_y = player2_y + size_of_field
    if directions.index(directions_player2) == 3:
        next_cage_player2_x = player2_x - size_of_field

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

    if (player1_x, player1_y) in coins:
        coins.remove((player1_x, player1_y))
        coins_player1 += 1

    if (player2_x, player2_y) in coins:
        coins.remove((player2_x, player2_y))
        coins_player2 += 1

    if len(coins) < num_coins:
        new_coins_needed = num_coins - len(coins)
        new_coins = generate_food(new_coins_needed)
        coins.extend(new_coins)

    if running_timer:
        countdown -= 1 / FPS
    if countdown <= 0:
        running = False

    screen.fill(light_gray)
    draw_grid()

    pygame.draw.rect(screen, blue, (player1_x, player1_y, size_of_field, size_of_field))
    pygame.draw.rect(screen, red, (player2_x, player2_y, size_of_field, size_of_field))

    pygame.draw.rect(screen, grey, (next_cage_player1_x, next_cage_player1_y, size_of_field, size_of_field))
    pygame.draw.rect(screen, grey, (next_cage_player2_x, next_cage_player2_y, size_of_field, size_of_field))

    for foodx, foody in fruits:
        pygame.draw.rect(screen, green, [foodx, foody, size_of_field, size_of_field])

    for coinx, coiny in coins:
        pygame.draw.rect(screen, yellow, [coinx, coiny, size_of_field, size_of_field])

    pygame.draw.rect(screen, black, (0, 0, dragons_screen_width, dragons_screen_height), border_thickness)

    shot1=[space()]
    shot2=[q()]

    pygame.display.flip()
    clock.tick(FPS)

win_lose_screen.win_lose_screen(fruits_player1, fruits_player2)

pygame.quit()
sys.exit()

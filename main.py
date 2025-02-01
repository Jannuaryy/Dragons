import pygame
import time
import sys
import random
import start_screen, win_lose_screen
from config import *
import SpriteSheet

pygame.init()
start_screen.start_screen()

# players results:
fruits_player1 = 0
fruits_player2 = 0

coins_player1 = 0
coins_player2 = 0

font = pygame.font.Font('Skatec.ttf', 74)
last_update_time = time.time()
remaining_time = countdown
countdown_active = False

# coin animation:
coin_anim_last_update = pygame.time.get_ticks()
coin_anim_ticks = 80
coin_anim_steps = 8
coin_sprite_sheet = SpriteSheet.SpriteSheet(pygame.image.load('textures/coin animation.png').convert_alpha())
coin_images_list = []

for i in range(coin_anim_steps):
    coin_images_list.append(coin_sprite_sheet.get_image(i, 21, 20, 1, light_gray))
coin_current_frame = 0

items_sheets_list = []
items_sprites_count = 6
items_sprite_sheet = SpriteSheet.SpriteSheet(pygame.image.load('textures/items.png').convert_alpha())


dragon_sheet = SpriteSheet.SpriteSheet(pygame.image.load('textures/dragon sprite.png').convert_alpha())
dragon_sprite = dragon_sheet.get_image(0, 40, 40, 0.5, light_gray)

dragon_sheet_2 = SpriteSheet.SpriteSheet(pygame.image.load('textures/blue dragon.png').convert_alpha())
dragon_sprite_2 = dragon_sheet_2.get_image(0, 40, 40, 0.5, light_gray)

frame_sheet = SpriteSheet.SpriteSheet(pygame.image.load('textures/frame.png').convert_alpha())
frame_image = frame_sheet.get_image(0, 800, 800, 1, light_gray)

for i in range(items_sprites_count):
    items_sheets_list.append(items_sprite_sheet.get_image(i, 21, 20, 1, light_gray))

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
    food_dic = {}
    for foodx, foody in food_positions:
        frame_num = random.randint(0, items_sprites_count - 1)
        food_dic[(foodx, foody)] = frame_num
    return food_dic


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
        if event.type == pygame.KEYDOWN:
            if not countdown_active:
                countdown_active = True
                last_update_time = time.time()

    keys = pygame.key.get_pressed()
    current_ticks = pygame.time.get_ticks()

    new_player1_x = player1_x
    new_player1_y = player1_y
    new_player2_x = player2_x
    new_player2_y = player2_y

    if keys[pygame.K_LEFT]:
        new_player1_x -= size_of_field
    if keys[pygame.K_RIGHT]:
        new_player1_x += size_of_field
    if keys[pygame.K_UP]:
        new_player1_y -= size_of_field
    if keys[pygame.K_DOWN]:
        new_player1_y += size_of_field

    if keys[pygame.K_a]:
        new_player2_x -= size_of_field
    if keys[pygame.K_d]:
        new_player2_x += size_of_field
    if keys[pygame.K_w]:
        new_player2_y -= size_of_field
    if keys[pygame.K_s]:
        new_player2_y += size_of_field

    if not (new_player1_x < new_player2_x + size_of_field and
            new_player1_x + size_of_field > new_player2_x and
            new_player1_y < new_player2_y + size_of_field and
            new_player1_y + size_of_field > new_player2_y):
        player1_x = max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, new_player1_x))
        player1_y = max(border_thickness, min(dragons_screen_height - size_of_field - border_thickness, new_player1_y))

    if not (new_player2_x < player1_x + size_of_field and
            new_player2_x + size_of_field > player1_x and
            new_player2_y < player1_y + size_of_field and
            new_player2_y + size_of_field > player1_y):
        player2_x = max(border_thickness, min(dragons_screen_width - size_of_field - border_thickness, new_player2_x))
        player2_y = max(border_thickness, min(dragons_screen_height - size_of_field - border_thickness, new_player2_y))


    if fruits.get((player1_x, player1_y)) != None:
        fruit_frame = fruits.pop((player1_x, player1_y))
        fruits_player1 += 1

    if fruits.get((player2_x, player2_y)) != None:
        fruit_frame = fruits.pop((player2_x, player2_y))
        fruits_player2 += 1

    if len(fruits) < num_food:
        new_foods_needed = num_food - len(fruits)
        new_foods = generate_food(new_foods_needed)
        fruits = {**fruits, **new_foods}
        # fruits.extend(new_foods)

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

    # screen.blit(frame_image, (0, 0))
    screen.fill(light_gray)

    draw_grid()


    for fruit_item in fruits.items():
        #pygame.draw.rect(screen, green, [foodx, foody, size_of_field, size_of_field])
        screen.blit(items_sheets_list[fruit_item[1]], fruit_item[0])


    # coins:
    if current_ticks - coin_anim_last_update >= coin_anim_ticks:
        coin_current_frame = coin_current_frame + 1 if coin_current_frame < len(coin_images_list) - 1 else 0
        coin_anim_last_update = current_ticks
    for coinx, coiny in coins:
        # pygame.draw.rect(screen, yellow, [coinx, coiny, size_of_field, size_of_field])
        screen.blit(coin_images_list[coin_current_frame], (coinx, coiny))

    screen.blit(dragon_sprite, (player1_x, player1_y))
    #pygame.draw.rect(screen, blue, (player1_x, player1_y, size_of_field, size_of_field))
    #pygame.draw.rect(screen, red, (player2_x, player2_y, size_of_field, size_of_field))
    screen.blit(dragon_sprite_2, (player2_x, player2_y))

    pygame.draw.rect(screen, black, (0, 0, dragons_screen_width, dragons_screen_height), border_thickness)
    # screen.blit(frame_image, (0, 0))

    fruit_score_text = font.render(f'score {fruits_player2} : {fruits_player1}', True, light_gray)
    coin_score_text = font.render(f'coins: {coins_player1 + coins_player2}', True, light_gray)

    screen.blit(frame_image, (0, 0))
    screen.blit(fruit_score_text, (30, 20))
    screen.blit(coin_score_text, (dragons_screen_width // 2 + 120, 20))

    if countdown_active:
        current_time = time.time()
        if current_time - last_update_time >= 1:
            remaining_time = max(0, remaining_time - 1)
            last_update_time = current_time
        if remaining_time == 0:
            countdown_active = False

    countdown_text = font.render(str(remaining_time), True, light_gray)
    text_rect = countdown_text.get_rect(topleft=(30, dragons_screen_height - 30 - countdown_text.get_height()))

    screen.blit(countdown_text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

win_lose_screen.win_lose_screen(fruits_player1, fruits_player2, coins_player1, coins_player2)

pygame.quit()
sys.exit()

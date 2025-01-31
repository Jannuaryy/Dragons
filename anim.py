import pygame
pygame.init()
from config import *
import SpriteSheet

screen = pygame.display.set_mode((dragons_screen_width, dragons_screen_height))
pygame.display.set_caption(dragons_game_name)
running = True



sprite_sheet_image = pygame.image.load('textures/items.png').convert_alpha()
sprite_sheet = SpriteSheet.SpriteSheet(sprite_sheet_image)


animation_list = []
anim_steps = 6
last_update = pygame.time.get_ticks()
anim_cooldown = 700
frame = 0
COLOR = (70, 70, 70)
for i in range(anim_steps):
    animation_list.append(sprite_sheet.get_image(i, 21, 20, 10, COLOR))



while running:
    screen.fill((50, 50, 50))

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= anim_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    screen.blit(animation_list[frame], (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
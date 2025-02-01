import sys

import pygame
from pygame.examples.chimp import load_image

from config import *

screen = pygame.display.set_mode((dragons_screen_width, dragons_screen_height))
pygame.display.set_caption(dragons_game_name)

image = pygame.image.load('textures/landscape 1.png').convert_alpha()

def win_lose_screen(fruits_player1, fruits_player2, coins_player1, coins_player2):
    #screen.fill(light_gray)
    screen.blit(image, (0, 0))

    text_curr_y = 180

    title_rendered = pygame.font.Font('Skatec.ttf', 180).render('game over', 1, pygame.Color('white'))
    title_rect = title_rendered.get_rect()
    title_rect.top = text_curr_y
    title_rect.x = round((dragons_screen_width - title_rect.width) / 2)
    screen.blit(title_rendered, title_rect)

    text_curr_y += title_rect.height + 30

    # result_info = 'draw!'
    # if fruits_player1 != fruits_player2:
    #     result_info = "won player {}".format(1 if fruits_player1 > fruits_player2 else 2)

    player1_result = 'draw!'
    player2_result = 'draw!'
    if fruits_player1 > fruits_player2:
        player1_result = 'won!'
        player2_result = 'lose'
    if fruits_player1 < fruits_player2:
        player1_result = 'lose'
        player2_result = 'won!'

    for line in ['PLAYER 1: X{} {}'.format(fruits_player1, player1_result), 'PLAYER 2: X{} {}'.format(fruits_player2, player2_result)]:
        string_rendered = pygame.font.Font('Skatec.ttf', 70).render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_curr_y
        intro_rect.x = 160
        text_curr_y += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    text_curr_y += 30

    coin_rendered = pygame.font.Font('Skatec.ttf', 120).render(f'{coins_player1 + coins_player2} coins', 1, pygame.Color('white'))
    coin_rect = coin_rendered.get_rect()
    coin_rect.top = text_curr_y
    coin_rect.x = round((dragons_screen_width - coin_rect.width) / 2)
    screen.blit(coin_rendered, coin_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
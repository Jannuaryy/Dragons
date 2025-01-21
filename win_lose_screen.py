import sys
import pygame
from config import *

screen = pygame.display.set_mode((dragons_screen_width, dragons_screen_height))
pygame.display.set_caption(dragons_game_name)

def win_lose_screen(fruits_player1, fruits_player2):
    screen.fill(light_gray)
    result_info = 'Ничья!'
    if fruits_player1 != fruits_player2:
        result_info = "Выиграл игрок {}".format(1 if fruits_player1 > fruits_player2 else 2)

    intro_text = ["ИГРА ОКОНЧЕНА!",
                  'Игрок 1: {}'.format(fruits_player1),
                  'Игрок 2: {}'.format(fruits_player2),
                  result_info]

    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
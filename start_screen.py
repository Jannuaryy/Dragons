import sys

import pygame
from config import *

screen = pygame.display.set_mode((dragons_screen_width, dragons_screen_height))
pygame.display.set_caption(dragons_game_name)

image = pygame.image.load('textures/landscape 2.png').convert_alpha()

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    screen.blit(image, (0, 0))

    text_curr_y = 200

    title_rendered = pygame.font.Font('Skatec.ttf', 180).render('dragons', 1, pygame.Color('white'))
    title_rect = title_rendered.get_rect()
    title_rect.top = text_curr_y
    title_rect.x = round((dragons_screen_width - title_rect.width) / 2)
    screen.blit(title_rendered, title_rect)

    text_curr_y += title_rect.height + 320

    intro_rendered = pygame.font.Font('Skatec.ttf', 70).render('PRESS ANY KEY TO START...', 1, pygame.Color('white'))
    intro_rect = intro_rendered.get_rect()
    intro_rect.top = text_curr_y
    intro_rect.x = round((dragons_screen_width - intro_rect.width) / 2)
    screen.blit(intro_rendered, intro_rect)

    text_curr_y +=  100

    version_rendered = pygame.font.Font('Skatec.ttf', 50).render('0.1 ALFA', 1, pygame.Color('white'))
    version_rect = version_rendered.get_rect()
    version_rect.top = text_curr_y
    version_rect.x = 650
    screen.blit(version_rendered, version_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
import pygame
import sys

pygame.init()

width, height = 500, 500
FPS = 20

light_gray = (211, 211, 211)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

size = 20

player1_x = 500
player1_y = 500

player2_x = 0
player2_y = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дракончики")


def draw_grid():
    for x in range(0, width, size):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, size):
        pygame.draw.line(screen, black, (0, y), (width, y))


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    screen.fill(light_gray)

    draw_grid()

    pygame.draw.rect(screen, blue, (player1_x, player1_y, size, size))
    pygame.draw.rect(screen, red, (player2_x, player2_y, size, size))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

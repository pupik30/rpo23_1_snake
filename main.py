import pygame
import random
import time

white = (255, 255, 255)
green = (0, 255, 0)
black = (10, 10, 10)

WIDTH = 800
HEIGHT = 800

tile_size = 20

snake_tiles = []
snake_size = 1
snake_speed = 2
snake_x = WIDTH // 2
snake_y = HEIGHT // 2

change_x = change_y = 0

pygame.init()
pygame.display.set_caption('Snake')
main_screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_x = -tile_size
                change_y = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_x = tile_size
                change_y = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                change_x = 0
                change_y = -tile_size
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_x = 0
                change_y = tile_size

    snake_x += change_x
    snake_y += change_y

    new_snake_tile = [snake_x, snake_y]
    snake_tiles.append(new_snake_tile)

    for x, y in snake_tiles:
        pygame.draw.rect(main_screen, white, (x, y, tile_size, tile_size))

    pygame.display.update()


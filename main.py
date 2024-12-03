import pygame
import random
import time



wight = (255,255,255)
green = (0, 255, 0)
black = (10,10,10)


WIDGHT = 800
HEIGHT = 800

tile_tiles = 20

snake_tiles = []
snake_size = 1
snake_speed = 3

pygame.init()
pygame.display.set_caption('Snake')
main_screen = pygame.display.set_mode(WIDGHT, HEIGHT)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


import pygame
import sys

screen_width = 800
screen_height = 800

pygame.init()

# WINDOW
pygame.display.set_caption("Blokus")
view = pygame.display.set_mode((screen_width, screen_height))
view.fill((255, 255, 255))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
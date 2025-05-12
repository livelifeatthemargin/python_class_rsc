#created to help with understanding imports, initialization, while loops, for loops, and if statements

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))  # window size
pygame.display.set_caption("My First Pygame Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background (white)
    screen.fill((255, 255, 255))

    pygame.display.update()

pygame.quit()
sys.exit()